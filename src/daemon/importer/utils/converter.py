import csv

#Converter string para XML\
def convert_row(row):
    return  """     <flight id="%s" name="%s" airline="%s">
        <route source="%s" destination="%s" />
        <details>
            <price value="%s" class="%s" />
            <stops count="%s"/>
            <time departure="%s" arrival="%s" duration="%s" days="%s" />
        </details>
    </flight> """ % (row[0], row[2], row[1], row[3], row[7], row[11], row[8], row[5], row[4], row[6], row[9], row[10])

def convert_csv_to_xml(csv_path, xml_path):
    f = open(csv_path)
    f_csv = csv.reader(f)
    data = []


    # Substituir caracteres invalidos por algo valido
    for row in f_csv:
        tags = row

        for i in range(len(tags)):
            row[i] = row[i].replace('&', "and")
        data.append(row)

    f.close()
    

    # Escreve o XML num ficheiro
    with open(xml_path, 'w') as f: f.write(
      '<flights>\n' + '\n'.join([convert_row(row) for row in data[1:]]) + '\n</flights>\n') 