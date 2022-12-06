from db_driver.driver import load_session


class BaseDB:

    def __init__(self, connect):
        self.session = load_session(connect=connect)

    @classmethod
    def format_mysql_sql(cls, table_name, column_list):
        """
        {('插入讲师', 'user'): [('user_no', 6104887796040106), ('mobile', '19935364436')], ('插入讲师', 'user_account'): [('user_no', 5022264513878125), ('sign', 4443414348222906), ('bank_card_no', 9521528062970088), ('bank_name', 'sjdka'), ('bank_branch_name', 'jkads'), ('bank_user_name', 'ksajd'), ('bank_id_card_no', 1714495404772866), ('bank_mobile', '19947594987')], ('插入会议', 'user'): [('user_no', 1128894617958351), ('mobile', '19914473947')], ('插入会议', 'user_account'): [('user_no', 3675188854567534), ('sign', 6186047296812600), ('bank_card_no', 4622304693175358), ('bank_name', 'skdaj'), ('bank_branch_name', 'dkjsa'), ('bank_user_name', 'sdkja'), ('bank_id_card_no', 7370968421836130), ('bank_mobile', '19911506360')], ('插入会议', 'user_ext'): [('user_no', 9937475437394865), ('mobile', '19933901508')]}
        """
        column_names = [name for name, value in column_list]
        column_values = [value for name, value in column_list]
        print(column_names.__repr__())
        print("++++++++")
        print(column_values.__repr__())
        sql = f"INSERT INTO {table_name} ({u','.join(column_names)}) values ({u','.join(column_values)})"
        print(sql)
        return sql



if __name__ == '__main__':
    table_name = "user"
    column_list = [('username', "'hsdjhsujsudsadaa'"), ('phone', "'19949884831'")]

    print(BaseDB.format_mysql_sql(table_name, column_list))
