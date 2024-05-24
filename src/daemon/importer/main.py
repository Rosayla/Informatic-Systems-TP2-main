import asyncio
import time
import uuid

import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler, FileCreatedEvent

import psycopg2
from psycopg2 import OperationalError

from utils import convert_csv_to_xml

def get_csv_files_in_input_folder():
    return [os.path.join(dp, f) for dp, dn, filenames in os.walk(CSV_INPUT_PATH) for f in filenames if
            os.path.splitext(f)[1] == '.csv']

def generate_unique_file_name(directory):
    return f"{directory}/{str(uuid.uuid4())}.xml"

class CSVHandler(FileSystemEventHandler):

    def __init__(self, input_path, output_path, db_xml_connection):
        self._output_path = output_path
        self._input_path = input_path
        self.db_xml = db_xml_connection

        # generate file creation events for existing files
        for file in [os.path.join(dp, f) for dp, dn, filenames in os.walk(input_path) for f in filenames]:
            event = FileCreatedEvent(os.path.join(CSV_INPUT_PATH, file))
            event.event_type = "created"
            self.dispatch(event)

    async def convert_csv(self, csv_path):
        # here we avoid converting the same file again
        # !TODO: check converted files in the database
        if csv_path in await self.get_converted_files():
            return

        print(f"new file to convert: '{csv_path}'")

        # we generate a unique file name for the XML file
        xml_path = generate_unique_file_name(self._output_path)

        # we do the conversion
        
        convert_csv_to_xml(csv_path, xml_path)

        # !TODO: once the conversion is done, we should updated the converted_documents tables
        self.insert_doc_into_converted_documents(csv_path=csv_path, xml_path=xml_path)

        print(f"new xml file generated: '{xml_path}'")

        # !TODO: we should store the XML document into the imported_documents table
        self.insert_xml_into_imported_documents(xml_path=xml_path)

    async def get_converted_files(self):
        # !TODO: you should retrieve from the database the files that were already converted before
        src_from_converted_docs = []
        cursor = self.db_xml.cursor()
        cursor.execute("SELECT src FROM converted_documents")

        for row in cursor.fetchall():
            src_from_converted_docs.append(row[0])

        return src_from_converted_docs

    def insert_doc_into_converted_documents(self, csv_path, xml_path):
        cursor = self.db_xml.cursor()
        cursor.execute(
            "INSERT INTO converted_documents(src, file_size, dst) VALUES(%s, %s, %s)",
           [ 
                csv_path,
                os.path.getsize(csv_path),
                xml_path
            ]
        )
        self.db_xml.commit()
    
    def insert_xml_into_imported_documents(self, xml_path):
        f = open(xml_path, "r")
        xml_data = f.read()

        cursor = self.db_xml.cursor()
        cursor.execute(
            "INSERT INTO imported_documents(file_name, xml) VALUES(%s, %s)",
           [ 
                xml_path,
                xml_data
            ]
        )
        self.db_xml.commit()

    def on_created(self, event):
        if not event.is_directory and event.src_path.endswith(".csv"):
            asyncio.run(self.convert_csv(event.src_path))


if __name__ == "__main__":
    db_xml = None
    CSV_INPUT_PATH = "/csv"
    XML_OUTPUT_PATH = "/shared/output"

    while True:
        try:
            db_xml = psycopg2.connect(host='db-xml', database='is', user='is', password='is')
        except OperationalError as err:
            print(err)
            
        if not db_xml is None:
            break

        time.sleep(60)

    # create the file observer
    observer = Observer()
    observer.schedule(
        CSVHandler(CSV_INPUT_PATH, XML_OUTPUT_PATH, db_xml),
        path=CSV_INPUT_PATH,
        recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        observer.join()
