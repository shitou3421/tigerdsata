import datetime
import random
import time

from generater_data.Mfaker import MFaker


class RolesTypeFunc:

    def __init__(self):
        self.f = MFaker()

    # mysql 插入数字类型

    def fake_tinyint(self, unsigned=None):
        return self.f.get("random_int", 0, 255) if unsigned else self.f.get("random_int", -128, 127).__repr__()

    def fake_smallint(self, unsigned=None):
        return self.f.get("random_int", 0, 65535) if unsigned else self.f.get("random_int", -32768, 32767).__repr__()

    def fake_mediumint(self, unsigned=None):
        return self.f.get("random_int", 0, 16777215) if unsigned else self.f.get("random_int", -8388608, 8388607).__repr__()

    def fake_int(self, min=None, max=None, unsigned=False):
        if min or max:
            return self.f.get("random_int", min, max).__repr__()
        return self.f.get("random_int", 0, 4294967295) if unsigned else self.f.get("random_int", -2147483648,
                                                                                   2147483647).__repr__()

    def fake_integer(self, min=None, max=None, unsigned=False):
        return self.fake_int(min=min, max=max, unsigned=unsigned).__repr__()

    def fake_bigint(self, *args):
        return self.f.get("random_int", 0, 18446744073709551615) if len(args) > 0 \
            else self.f.get("random_int", -9223372036854775808, 9223372036854775807).__repr__()

    def fake_float(self, *args):
        return self.f.get("pyfloat").__repr__()

    def fake_double(self, *args):
        return self.fake_float().__repr__()

    def fake_decimal(self, digits, right_digits, flag=None,
                     min_value=None, max_value=None):
        if flag is None:
            flag = random.randint(0, 1)
        number = self.f.get("pyfloat", left_digits=(digits - right_digits), right_digits=right_digits,
                            positive=True, min_value=min_value, max_value=max_value)
        return number.__repr__() if flag == 1 else (-number).__repr__()

    # mysql 日期类型

    def fake_date(self, start_date='-30y', end_date='today', format='%Y-%m-%d'):
        thedate = self.f.get("date_between", start_date, end_date)
        return thedate.strftime(format).__repr__()

    def fake_datetime_between(self, sdt, edt, foramt='%Y-%m-%d %H:%M:%S'):
        sdatetime = datetime.datetime.strptime(sdt, '%Y-%m-%d %H:%M:%S')
        stimestamp = time.mktime(sdatetime.timetuple())

        edatetime = datetime.datetime.strptime(edt, '%Y-%m-%d %H:%M:%S')
        etimestamp = time.mktime(edatetime.timetuple())

        timestamp = random.randint(stimestamp, etimestamp)
        ltime = time.localtime(timestamp)
        return time.strftime(foramt, ltime).__repr__()

    def fake_date_between(self, start_date, end_date, format='%Y-%m-%d'):
        start_date_time = '{0} 00:00:00'.format(start_date)
        end_date_time = '{0} 23:59:59'.format(end_date)
        random_datetime = self.fake_datetime_between(start_date_time, end_date_time)
        random_date = datetime.datetime.strptime(random_datetime.split()[0], '%Y-%m-%d').date()
        return datetime.datetime.strftime(random_date, format).__repr__()

    def fake_time(self, *args):
        return self.f.get(time).__repr__()

    def fake_year(self, *args):
        return self.f.get("year").__repr__()

    def fake_datetime(self, now=0, format='%Y-%m-%d %H:%M:%S'):
        dt = datetime.datetime.now() if now else self.f.get("date_time")
        return dt.strftime(format).__repr__()

    def fake_timestamp(self, now=0, *args):

        timestamp = int(time.time()) if now else self.f.get("unix_time")
        return timestamp

    # mysql 字符串类型

    def fake_char(self, *args):
        return self.f.get("pystr", min_chars=1, max_chars=255).__repr__()

    def fake_varchar(self, max_chars=255, *args):
        return self.f.get("pystr", min_chars=1, max_chars=max_chars).__repr__()

    def fake_tinytext(self, *args):
        max_nb_chars = args[0] if len(args) else 255
        return self.f.get("text", max_nb_chars=max_nb_chars).__repr__()

    def fake_text(self, *args):
        max_nb_chars = args[0] if len(args) else 65535
        return self.f.get("text", max_nb_chars=max_nb_chars).__repr__()

    def fake_longtext(self, *args):
        """暂不支持"""
        return self.fake_tinytext(*args)

    def fake_tinyblob(self, *args):
        """暂不支持"""
        # todo: 需要实现
        return

    def fake_mediumblob(self, *args):
        """暂不支持"""
        # todo: 需要实现
        return

    def fake_longblob(self, *args):
        """暂不支持"""
        # todo: 需要实现
        return

    def fake_enum(self, *args):
        """暂不支持"""
        # todo: 需要实现
        return

    def fake_set(self, *args):
        """暂不支持"""
        # todo: 需要实现
        return

    def fake_phone_number(self, prefix=None):
        """随机生成电话"""
        if prefix is None:
            return self.f.get("phone_number").__repr__()
        else:
            return (str(prefix) + str(self.f.get("pyint", min_value=10000000, max_value=99999999))).__repr__()

    # 句子
    def fake_paragraph(self):
        return self.f.get("paragraph", nb_sentences=5).__repr__()

    # 实际业务    指定字符集生成特定长度的字符串
    def fake_charset(self, charset, length):
        if length <= len(charset):
            return "".join(random.sample(charset, length)).__repr__()
        return "".join(random.sample(charset * length, length)).__repr__()

    def get(self, func_name, *args, **kwargs):
        # print(args)
        if args:
            if args[0] is None:
                return getattr(self, "fake_" + func_name)()
        return getattr(self, "fake_" + func_name)(*args, **kwargs)


if __name__ == '__main__':
    a = {'digits': 5, 'right_digits': 2}
    print(RolesTypeFunc().get('decimal', **a))
    # print(RolesTypeFunc().get('paragraph'))
    # print(RolesTypeFunc().get('varchar', None))
    # print(RolesTypeFunc().get('phone_number',prefix=199))
    # print(RolesTypeFunc().get('charset',charset="anshdfgf", length=16))
    # print(RolesTypeFunc().get('decimal', digits=5, right_digits=2))
    # print(RolesTypeFunc().get('datetime_between', digits=5, right_digits=2))
    # a = None
    # print(RolesTypeFunc().get("time"))

    # print(RolesTypeFunc().fake_charset("ksj 😊df", 30))
    # print(RolesTypeFunc().get("charset", charset="absd", length=2))
    # print(RolesTypeFunc().get("integer", length=16))
    # a = {
    #     "length": 15
    # }
    # b = {
    #     "unsigned": False
    # }
    # # print(RolesTypeFunc().get('integer', **a))

    # c = {
    #     "digits": 5,
    #     "right_digits": 2
    # }
    # print(RolesTypeFunc().get('decimal', **c))
    # d = {
    #     "sdt": "2022-06-01 00:00:00",
    #     "edt": "2023-06-01 00:00:00"
    # }
    #
    # print(RolesTypeFunc().get('datetime_between', **d))
    # e = {
    #     "start_date": "2022-06-01",
    #     "end_date": "2023-06-01"
    # }
    # print(RolesTypeFunc().get('date_between', **e))
    #
    # print(RolesTypeFunc().get('tinytext'))
