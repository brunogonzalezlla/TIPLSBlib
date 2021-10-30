import numpy as np
from PIL import Image
import hashlib
import random
from datetime import datetime

class tiplsb:
    def __init__(self, path):
        self.version = '1.0.0'
        self.path = path
        # Open image
        self.img = Image.open(path, 'r')
        self.width, self.height = self.img.size
        self.img_array = np.array(list(self.img.getdata()))
        # Hash Image
        self.hash_image = self.get_hash(self.path)
        # Mode image
        if self.img.mode == 'RGB':
            self.image_mode = 3
        elif self.img.mode == 'RGBA':
            self.image_mode = 4
        # Check details
        self.details_dic = self.details()
        if bool(self.details_dic):
            self.initialized = True
        else:
            self.initialized = False

    def init(self, author, platform, type_encrypt='ring', datetime=True, redundancy=5, overwrite=False):
        if (self.initialized and overwrite) or not self.initialized:
            # Details
            parameters = [
                ('TIPLSB'),
                ('Version:', self.version),
                ('Line:', '1'),
                ('Type:', type_encrypt),
                ('Author:', author),
                ('Platform:', platform),
                ('Datetime:', datetime),
                ('Redundancy:', redundancy),
            ]
            identifier = ''
            for p in parameters:
                for s in p:
                    identifier += str(s)
                identifier += '|'
            identifier = identifier[:-1] + '#'
            bin_identifier = ''.join([format(ord(i), "08b") for i in identifier])
            bin_identifier_len = len(bin_identifier)
            character_index = 0
            list_index = self.get_ring(0)
            # Encode details
            if (len(list_index) * 3 > bin_identifier_len):
                for p in self.get_ring(0):
                    for q in range(0, 3):
                        if character_index < bin_identifier_len:
                            self.img_array[p][q] = int(bin(self.img_array[p][q])[2:9] + bin_identifier[character_index],
                                                       2)
                            character_index += 1
                self.details_dic = {
                    "Version": self.version,
                    "Line": 1,
                    "Type": type_encrypt,
                    "Author": author,
                    "Platform": platform,
                    "Datetime": datetime,
                    "Redundancy": redundancy
                }
                return True
            else:
                raise ValueError("The image does not have the necessary dimensions.")
        else:
            raise Exception("This image is already initialized.")

    def details(self):
        details = ""
        for p in self.get_ring(0):
            for q in range(0, 3):
                details += (bin(self.img_array[p][q])[2:][-1])
        details = [details[i:i + 8] for i in range(0, len(details), 8)]
        message = ""
        for i in range(len(details)):
            if message[-1:] == "#":
                break
            else:
                message += chr(int(details[i], 2))
        dic_details = {}
        if "TIPLSB" in message:
            st = message[:-1].split('|')
            dic_details = {
                "Version": st[1].split(':')[1],
                "Line": int(st[2].split(':')[1]),
                "Type": st[3].split(':')[1],
                "Author": st[4].split(':')[1],
                "Platform": st[5].split(':')[1],
                "Datetime": st[6].split(':')[1],
                "Redundancy": int(st[7].split(':')[1])
            }
            return dic_details
        else:
            return dic_details

    def add(self, author, platform):
        # Generate list index with 3 bits
        l_index = self.get_ring(self.details_dic['Line'])
        if len(l_index) == 0:
            list_index = []
            for i in l_index:
                for j in range(0, 3):
                    list_index.append((i, j))
            # Details
            if self.details_dic['Datetime']:
                details = "TIPLSB|" + str(author) + "|" + str(platform) + "|" + str(datetime.now().time()) + "#"
            else:
                details = "TIPLSB|" + str(author) + "|" + str(platform) + "#"
            bin_identifier = ''.join([format(ord(i), "08b") for i in details])
            bin_identifier_len = len(bin_identifier)
            character_index = 0
            if (len(list_index) > bin_identifier_len):
                random.shuffle(list_index, random.seed(self.hash_image))
                for (p, q) in list_index:
                    if character_index < bin_identifier_len:
                        self.img_array[p][q] = int(bin(self.img_array[p][q])[2:9] + bin_identifier[character_index], 2)
                        character_index += 1
                    else:
                        break
                self.update_ring(self.details_dic['Line'] + 1)
            else:
                raise ValueError("The image does not have the necessary dimensions.")
        else:
            raise Exception("The image is not large enough to add another user.")

    def update_ring(self, value):
        parameters = [
            ('TIPLSB'),
            ('Version:', self.details_dic['Version']),
            ('Line:', str(value)),
            ('Type:', self.details_dic['Type']),
            ('Author:', self.details_dic['Author']),
            ('Platform:', self.details_dic['Platform']),
            ('Datetime:', self.details_dic['Datetime']),
            ('Redundancy:', self.details_dic['Redundancy']),
        ]
        identifier = ''
        for p in parameters:
            for s in p:
                identifier += str(s)
            identifier += '|'
        identifier = identifier[:-1] + '#'
        bin_identifier = ''.join([format(ord(i), "08b") for i in identifier])
        bin_identifier_len = len(bin_identifier)
        character_index = 0
        list_index = self.get_ring(0)
        # Encode details
        for p in self.get_ring(0):
            for q in range(0, 3):
                if character_index < bin_identifier_len:
                    self.img_array[p][q] = int(bin(self.img_array[p][q])[2:9] + bin_identifier[character_index], 2)
                    character_index += 1
                else:
                    break
        self.details_dic['Line'] = value
        return True

    def get_ring(self, ring):
        list_index = []
        size_width = self.width - (ring + 1) * 2 + 2
        size_height = self.height - (ring + 1) * 2 + 2

        side_A = self.width * ring + ring
        side_B = side_A + size_width - 1
        side_C = side_B + self.width * (size_height - 1)
        side_D = side_A + self.width * (size_height - 1)
        aux = side_A + self.width

        for i in range(side_A, side_B):
            list_index.append(i)

        for i in range(side_B, side_C + 1, self.width):
            list_index.append(i)

        ls_aux = []
        for i in range(side_D, side_C):
            ls_aux.append(i)
        list_index += reversed(ls_aux)

        ls_aux = []
        for i in range(aux, side_D, self.width):
            ls_aux.append(i)
        list_index += reversed(ls_aux)

        return list_index

    def get_hash(self, path):
        with open(path, "rb") as f:
            bytes_image = f.read()
            hash_image = hashlib.sha256(bytes_image).hexdigest()
            return hash_image

    def save(self, overwrite=True, path=''):
        if self.image_mode == 3:
            mode = 'RGB'
        elif self.image_mode == 4:
            mode = 'RGBA'
        if path == '':
            new_path = self.path.split('.')[0]
        else:
            new_path = path.split('.')[0]
        array = self.img_array.reshape(self.height, self.width, self.image_mode)
        res_img = Image.fromarray(array.astype('uint8'), mode)
        res_img.save(new_path + ".png")
        return self.get_hash(new_path + ".png")