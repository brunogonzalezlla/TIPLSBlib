from .config import __version__
from .config import __redundancy__

from PIL import Image
import hashlib
import numpy as np
from datetime import datetime
from .function_additional import *

#__version__ = "0.0.1"
#__redundancy__ = 5


class tiplsb:
    def __init__(self, path):
        self.path = path
        # Open image
        img = Image.open(path, 'r').convert('RGB')
        self.width, self.height = img.size
        self.img_array = np.array(list(img.getdata()))
        # Hash Image
        self.hash_image = hashlib.sha256(img.tobytes()).hexdigest()
        # Check details
        self.init = self.initialized()
        # Initialize it if not
        if not bool(self.init):
            list_index = []
            txt_init = "TIPLSB|Version:" + str(__version__) + "|Line:1|Redundancy:" + str(__redundancy__) + "#"
            txt_bin = txt_to_bin(txt_init)
            for i in range(0, len(txt_bin)):
                list_index.append(index_element_ring(i, 0, self.width, self.height))
            self.write(zip(list_index, txt_bin))
            self.init = {
                "Version": __version__,
                "Line": 1,
                "Redundancy": __redundancy__
            }

    def initialized(self):
        bits = ""
        dic_init = {}
        for i in range(0, 48):
            pixel, color = index_element_ring(i, 0, self.width, self.height)
            bits += bin(self.img_array[pixel][color])[2:][-1]
        text = bin_to_txt(bits)
        if not text == "TIPLSB":
            return dic_init
        else:
            for i in range(48, max_index_element_ring(0, self.width, self.height), 8):
                character_bin = ""
                for j in range(i, i + 8):
                    pixel, color = index_element_ring(j, 0, self.width, self.height)
                    character_bin += bin(self.img_array[pixel][color])[2:][-1]
                character = bin_to_txt(character_bin)
                if character == "#":
                    break
                else:
                    text += character
            st = text.split('|')
            dic_init = {
                "Version": st[1].split(':')[1],
                "Line": int(st[2].split(':')[1]),
                "Redundancy": int(st[3].split(':')[1])
            }
            return dic_init

    def add(self, author, platform):
        ring = self.init['Line']
        text = "TIPLSB|" + author + "|" + platform + "|" + str(datetime.now().time()) + "#"
        text_bin = txt_to_bin(text)
        for i in range(0, self.init['Redundancy']):
            seed_image = hex(int(self.hash_image, 16) + int(str(i), 16))[2:]
            random.seed(seed_image)
            l = random.sample(range(0, max_index_element_ring(ring, self.width, self.height)), k=520)
            list_index = []
            for i in l:
                list_index.append(index_element_ring(i, ring, self.width, self.height))
            self.write(zip(list_index, text_bin))
            ring += 1
        # Update ring
        list_index = []
        txt_init = "TIPLSB|Version:" + str(self.init['Version']) + "|Line:" + str(ring) + "|Redundancy:" + str(
            self.init['Redundancy']) + "#"
        txt_bin = txt_to_bin(txt_init)
        for i in range(0, len(txt_bin)):
            list_index.append(index_element_ring(i, 0, self.width, self.height))
        self.write(zip(list_index, txt_bin))
        self.init['Line'] = ring

    def write(self, zip_txt_index):
        for ((pixel, color), bit) in zip_txt_index:
            self.img_array[pixel][color] = int(bin(self.img_array[pixel][color])[2:9] + bit, 2)

    def save(self, path=''):
        if path == '':
            new_path = self.path.split('.')[0]
        else:
            new_path = path.split('.')[0]
        array = self.img_array.reshape(self.height, self.width, 3)
        res_img = Image.fromarray(array.astype('uint8'), 'RGB')
        res_img.save(new_path + ".png")
        return new_path + ".png"