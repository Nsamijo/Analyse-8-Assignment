import yaml
import os


class Encryption:
    """"Encryption class which implements the ceasar cipher"""

    def blackmagic(self, value, sort, decrypt=False):
        """"transform the value with the power of black magic | shift chars to different position"""
        shift = 0
        result = ''
        # read the shift key in
        with open(os.getcwd() + '\Controllers\data.yml') as f:
            shift = yaml.load(f, yaml.SafeLoader)['resources']['keys'][sort][0]
        # if it is decrypt mode we must shift back tot the original position
        if decrypt:
            shift = -(shift)
        # black magic | iterate over the entire string and encrypt/decrypt
        for x in value:
            if x == ' ':
                result += x
            # check for uppercase | different char positions | A has pos 65 and a has pos 97
            elif x.isupper():
                result += chr((ord(x) + shift - 65) % 26 + 65)
            else:
                result += chr((ord(x) + shift - 97) % 26 + 97)
        return result

    def encrypt(self, elements, type, decrypt=False):
        """"Encrypt data"""
        if isinstance(elements, str):
            return self.blackmagic(elements, type, decrypt)
        encrypted = []
        for value in elements:
            encrypted.append(self.blackmagic(value, type, decrypt))
        return encrypted

    def decrypt(self, elements, type):
        """"decrypt data"""
        return self.encrypt(elements, type, True)
