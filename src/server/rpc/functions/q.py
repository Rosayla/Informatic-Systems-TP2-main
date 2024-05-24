import psycopg2

#LISTAR TODOS OS VOOS COM O PREÇO SUPERIOR OU IGUAL A "VALUE"
def searchValue(value):
    
    connection = None
    try:
        connection = psycopg2.connect(user="is",
                                  password="is",
                                  host="localhost",
                                  port="5432",
                                  database="is")

    
        cursor = connection.cursor()

        sql = "SELECT unnest(xpath('/flights/flight/details/price[@value>=" + value + "]/..', xml)) AS Numero_Voos FROM imported_documents WHERE file_name='output2.xml' LIMIT 10;"
        cursor.execute(sql)       
        records = cursor.fetchall()
        print("Total de voos:  ", len(records))
    
        cursor.close()
        return records
        
    
    except (Exception, psycopg2.DatabaseError) as error:
        print("Erro: ", error)
        msg = "\nErro ao realizar pesquisa!"
        return msg

    finally:
        # Encerrar a conexão à base de dados
        if connection is not None:
            connection.close()
            


#LISTAR TODOS OS VOOS com destino a mumbai

def query1():
    connection = None
    try:
        
        connection = psycopg2.connect(user="is",
                                 password="is",
                                  host="localhost",
                                  port="5432",
                                  database="is")
        
        if connection:
            cursor = connection.cursor()

            sql = "SELECT unnest(XPATH('/flights/flight/route[@destination=\"Mumbai\"]/..', xml)) AS FLIGHTS_TO_MUMBAI FROM imported_documents WHERE file_name = 'output2.xml' LIMIT 10 "
            print(sql)
            
            cursor.execute(sql)
            result = cursor.fetchall()

            cursor.close()
            return result

       
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection:
            
            connection.close()


#PESQUISAR VOO POR ID
def searchId(apple):

    connection = None
    try:
        connection = psycopg2.connect(user="is",
                                  password="is",
                                  host="localhost",
                                  port="5432",
                                  database="is")


        cursor = connection.cursor()

        sql = "SELECT unnest(XPATH('/flights/flight[@id=" + apple + "]/.', xml)) as flights FROM imported_documents WHERE file_name ='output2.xml';"
        cursor.execute(sql)
        infoSearch = cursor.fetchone()
        print("Total de voos:  ", len(infoSearch))  # type: ignore

        cursor.close()
        return infoSearch

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection:

            connection.close()

#MOSTRA NUMERO DE VOOS QUE TENHAM UM VALOR DE PREÇO SUPERIOR AO DADO E DE FORMA ORDENADA CRESCENTE
def orderValue(order):
    
    connection = None
    try:
        connection = psycopg2.connect(user="is",
                                  password="is",
                                  host="localhost",
                                  port="5432",
                                  database="is")

    
        cursor = connection.cursor()

        sql = "SELECT unnest(xpath('/flights/flight/details/price[@value>=" + order + "]/..', xml)) AS Numero_Voos FROM imported_documents WHERE file_name='output2.xml' LIMIT 10;"
        cursor.execute(sql)       
        records = cursor.fetchall()
        result = sorted(records)
        cursor.close()
        return result
        
    
    except (Exception, psycopg2.DatabaseError) as error:
        print("Erro: ", error)
        msg = "\nErro ao realizar pesquisa!"
        return msg

    finally:
        # Encerrar a conexão à base de dados
        if connection is not None:
            connection.close()

#PROCURA OS VOOS POR DEPARTURE TIME RECEBIDO
def classFind(tempo):
    connection = None
    try:

        connection = psycopg2.connect(user="is",
                                  password="is",
                                  host="localhost",
                                  port="5432",
                                  database="is")



        if connection:
            cursor = connection.cursor()

            sql = f"SELECT unnest(XPATH('/flights/flight/details/time[@departure=\"{tempo}\"]/..', xml)) AS FLIGHTS_DEPARTURE FROM imported_documents WHERE file_name = 'output5.xml' LIMIT 10 "
            print(sql)

            cursor.execute(sql)
            for result in cursor:
                print(result)
            cursor.close()
            return result

       
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection:
            connection.close()