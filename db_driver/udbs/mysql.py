from db_driver.base_db import BaseDB


class Mysql(BaseDB):

    def __init__(self, connect):
        """
        mysql://scott:tiger@hostname/dbname"
        :param connect:
        """
        super(Mysql, self).__init__(connect)

    def save(self, sql):
        self.session.execute(sql)
        self.session.commit()


