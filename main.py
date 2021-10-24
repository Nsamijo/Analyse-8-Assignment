from CDMS import CDMS
from Controller.DataHandler import Database



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    person = {"id": "2", "firstName": "elevate", "lastName": "karijo", "streetName": "snelspoor",
              "houseNumber": "8", "zipCode": "2908AK", "city": "1", "email": "nsamijo@gmail.com",
              "phoneNumber": "0615500140", "priviledge": "3"}
    # me = Advisor()
    # me.setData(person)
    # # Encryption().encrypt(me.getPerson())
    # me.pid = "3"
    # me.username = "nathan"
    # me.password = "2001nathan"
    # # print(me.privilege)
    # temp = me.dictUser()
    # Encryption().encrypt(temp)
    # me.setUser(temp)
    # print(me.dictUser())
    # db = Datahandler()
    # db.addUser(list(me.dictUser().values()))
    # # print(db.getPeople())
    # print(db.getUsers())
    CDMS().execute()


