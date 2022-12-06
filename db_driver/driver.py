from sqlalchemy import create_engine, MetaData, inspect
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import reflection


def load_session(connect):
    """
    engine = create_engine("mysql://scott:tiger@hostname/dbname",
                            encoding='latin1', echo=True)
    :return:
    """

    engine = create_engine(connect, pool_recycle=1800)
    db_session = sessionmaker(engine)
    session = db_session()
    return session


def get_db_columns_type(connect):
    """获取所有表的所有字段的类型"""
    engine = create_engine(connect, pool_recycle=1800)
    tables = engine.table_names()
    insp = reflection.Inspector.from_engine(engine)
    db_indo_dict = {}
    for t in tables:
        cs = {}
        colums = insp.get_columns(t)  # 这里是写的表名
        for i in colums:
            cs.update({i.get("name"): i.get("type").__str__().split(" ")[0].split("(")[0]})
        db_indo_dict.update({t: cs})

    # print(db_indo_dict)
    return db_indo_dict


if __name__ == '__main__':
    driver = "mysql://root:password@192.168.51.200:3306/xinhe_education_user"
    get_db_columns_type(driver)
