from enum import Enum

from generater_data.roles_type_func import RolesTypeFunc


def get_roles_type_dict():
    roles_type_list = []
    for k, v in RolesTypeFunc.__dict__.items():
        if "fake_" in k:
            roles_type_list.append(k.split("fake_")[1])
    roles_dict = dict(zip(roles_type_list, roles_type_list))
    return roles_dict



RoleEnum = Enum('A',
             dict((k, v) for k, v in get_roles_type_dict().items()),
             module=__name__
             )



if __name__ == '__main__':
    for e in RoleEnum:
        print(e.name)





