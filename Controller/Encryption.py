from Models.Person import Person

class Encryption:
####SECURITY HANDLER####
    specialChars = "!@$%#&/:.?()=,*_[]~^-+`|\{};'<>"

    def encrypter(self, value, decyper=False):
        ''''ENCRYPT OR DECRYPT VALUE BASED ON PRIVILEDGE || value = data , sort = encryption, decrypt = to decrypt data or not'''
        if value == None or isinstance(value, int):
            return value

        # Hier kan je een simpele oneliner van maken dmv een ternary operator
        # dat is in dit geval leesbaarder:
        # (en het is decypher, niet decyper)
        shift = -5 if decyper else 5
        # if decyper:
        #     shift = -5
        # else:
        #     shift = 5

        result = ""
        for x in value:
            x = str(x)
            if x in self.specialChars or x.isdigit() or x == ' ':
                result += x
            elif x.isupper():
                result += chr((ord(x) + shift - 65) % 26 + 65)
            else:
                result += chr((ord(x) + shift - 97) % 26 + 97)
        return result

    def encrypt(self, elements):
        ''''ENCRYPT VALUES'''
        # Er gaan hier meerdere dingen mis, je permute een input parameter.
        # Dit veroorzaakt vaak lastig te traceren bugs, ik zou een value returnen instead.
        # Dan kan het ook meer pythonic dmv een map:
        return list(map(self.encrypter, elements))
        # Deze voert self.encrypter uit op ieder element van elements.
        # De list(...) is nodig omdat python lazy is en de mapping niet uitvoert totdat het nodig is.
        # Daarom maken we er een lisjt van.

        # for value in range(0, len(elements)):
        #     elements[value] = (self.encrypter(elements[value]))

    def decrypt(self, elements):
        # Hier hetzelfde als bij encrypt.
        ''''DECRYPT VALUES FROM DATABASE'''
        elements = [list(person) for person in elements]
        for value in range(0, len(elements)):
            for person in range(0, len(elements[value])):
                elements[value][person] = (self.encrypter(elements[value][person], True))
        return elements