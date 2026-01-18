from database.DB_connect import DBConnect

class DAO:

    @staticmethod
    def query_esempio():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ SELECT * FROM esempio """

        cursor.execute(query)

        for row in cursor:
            result.append(row)

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def get_nodi():
        conn = DBConnect.get_connection()
        cursor = conn.cursor()
        query = """ SELECT DISTINCT cromosoma FROM `gene` WHERE cromosoma!=0 """
        cursor.execute(query)
        result=[]
        for row in cursor:
            result.append(row[0])
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def get_archi():
        conn = DBConnect.get_connection()
        cursor = conn.cursor()
        query = """SELECT  g1.cromosoma,g2.cromosoma,g1.id,g2.id,i.correlazione FROM interazione as i 
                    JOIN gene g1 ON g1.id=i.id_gene1 JOIN gene g2 ON g2.id=i.id_gene2
                    WHERE g1.cromosoma!=g2.cromosoma AND g1.cromosoma!=0"""
        cursor.execute(query)
        result=[]
        for row in cursor:
            result.append((row[0],row[1],row[2],row[3],row[4]))
        cursor.close()
        conn.close()
        return result