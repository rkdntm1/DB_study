import pymysql as mysql

class DB:

    def __init__(self, host, user, pwd, db):
        self.host=host
        self.user=user
        self.pwd=pwd
        self.db=db

    def connect(self):
        self.conn = mysql.connect(host=self.host,
                             user=self.user,
                             password=self.pwd,
                             db=self.db,
                             charset='utf8',
                             cursorclass=mysql.cursors.DictCursor)


    def close(self):
       if self.conn :
          self.conn.close()


    def listdata(self):
        self.connect()
        result=[]
        try:
            with self.conn.cursor() as cursor:
                # Read a single record
                sql = "select distinct title, url from news "

                cursor.execute(sql)
                newsurls=cursor.fetchall()
                for newsurl in newsurls:
                  result.append(newsurl)

        finally:
            self.conn.close()
            return result


    def inserdata(self, title, news_url):
        try :
          self.connect()
          with self.conn.cursor() as cursor:
            # Create a new record
              sql = "insert into news(`title`, `url`) VALUES (%s, %s)"
              data=(title, news_url)
              #cursor.execute(sql, (title, news_url))
              cursor.execute(sql, (title, news_url))
              self.conn.commit()

        except Exception as e:
            print(e)

        finally :
            self.conn.close()

