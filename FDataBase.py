import sqlite3



class FDataBase:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()

    def getCards(self):

        sql = '''SELECT * FROM thoth LIMIT 5 '''
        try:
            self.__cur.execute(sql)
            res = self.__cur.fetchall()
            if res: return res
        except:
            print("Ошибка чтения из БД")
        return []

    def getCard(self, cardId):
        try:
            self.__cur.execute(f"SELECT name_orig, pic_bin, description FROM thoth WHERE id = {cardId} LIMIT 1")
            res = self.__cur.fetchone()
            if res:
                return res
        except sqlite3.Error as e:
            print("Ошибка получения данных из БД " + str(e))
        return  (False, False)

    def divination(self):
        try:
            self.__cur.execute(f"SELECT * FROM thoth")
            res = self.__cur.fetchall()
            if res: return res
        except sqlite3.Error as e:
            print("Ошибка получения карт из БД " + str(e))
        return []