from db_driver.udbs.mysql import Mysql


class DBServer:

    def init(self, type: str, connect):
        if "mysql" == type.lower():
            return Mysql(connect)

