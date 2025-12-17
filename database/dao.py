from database.DB_connect import DBConnect
from model.gene import Gene
from model.interazione import Interazione

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
    def get_gene():
        conn = DBConnect.get_connection()
        cursor = conn.cursor()
        query = """ SELECT * FROM gene"""
        cursor.execute(query)
        result=[]
        for row in cursor:
            result.append(Gene(row[0],row[1],row[2],row[3]))
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def get_interazione():
        conn = DBConnect.get_connection()
        cursor = conn.cursor()
        query = """ SELECT * FROM interazione"""
        cursor.execute(query)
        result=[]
        for row in cursor:
            result.append(Interazione(row[0],row[1],row[2],row[3]))
        cursor.close()
        conn.close()
        return result

