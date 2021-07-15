from Controllers.Encryption import Encryption
from Models.Priviledges import Priviledge as pv




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    database = pv(0, 'data')
    database.deleteRoles()
    database.updateRole()
    roles = database.getRoles()
    for x in roles:
        print(Encryption().decrypt(x[1], 'role'))