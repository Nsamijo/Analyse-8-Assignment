import Controllers.Encryption as S
from Controllers import *




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    encrypt = S.Encryption()
    print(encrypt.encrypt({1: 'hello world'}, 'role'))
    print(encrypt.decrypt(encrypt.encrypt({1: 'hello world'}, 'role'), 'role'))