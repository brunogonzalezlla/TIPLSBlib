from TIPLSB import tiplsb
from TIPLSB import tip_decode
from TIPLSB import read_ring_redundancy
from TIPLSB import read_ring
from PIL import Image

import time
import numpy as np
import random
from datetime import datetime
import hashlib

# start_time = time.time()
#i = tiplsb("img/600x600.jpg")
#i.add("Prueba", "pRUEBA")
#i.save('img/600x600_P1.png')


#i = tiplsb("img/600x600.jpg")
#i.add("PruebaPrimera", "PlataformaPrimera")
#i.save('img/600x600_P1.png')


sol = tip_decode('img/600x600.jpg', 'img/600x600_P2.png')
print(sol)


#i = tiplsb("img/600x600_P1.png")
#i.add("PruebaSegunda", "PlataformaSegunda")
#i.save('img/600x600_P2.png')

# print("Inicializada la imagen")
# print("--- %s seconds ---" % (time.time() - start_time))
#print(i.init)
# print(i.hash_image)

# img = Image.open("img/600x600_1.png", 'r').convert('RGB')
# width, height = img.size
# img_array = np.array(list(img.getdata()))
# #
# # print("-------------------------------")
# #seed_image = hex(int(i.hash_image, 16) + int(str(2), 16))[2:]
# aa = read_ring_redundancy(img_array, 1, "b76956a930c73a2391ca8dafae2007f6c81a8119cd137cf24f19e8af94310aab", 5, width, height)
# for i in aa:
#     print(i)
# print("....")
# print(aa)

#sol = tip_decode('img/600x600_P1.png', 'img/600x600_P2.png')
#print(sol)

#start_time = time.time()
#i = tiplsb("img/600_original.png")
#print("Hash despues INIT:"+i.hash_image)
#i.add("Insert1", "PLATPRUEBA1")
#i.save('img/600_1.png')
#print("Inicializada la imagen")
#print("--- %s seconds ---" % (time.time() - start_time))
#print("Hash despues add:"+i.hash_image)

# Hash despues INIT:1edfff3692e20a91e6a51b54ba4d88ede819b80421a39fd48637e0f963ec141d
# Hash despues add:6c59b4275a25b98e059069832d69e33dc7fad328df38298c3284f98cb92b2de5

#start_time = time.time()
#i = tiplsb("img/600_1.png")
#print("Hash despues INIT:"+i.hash_image)
#i.add("Insert2", "PLATPRUEBA2")
#i.save('img/600_2.png')
#print("Inicializada la imagen")
#print("--- %s seconds ---" % (time.time() - start_time))
#print("Hash despues add:"+i.hash_image)

# Hash despues INIT:6c59b4275a25b98e059069832d69e33dc7fad328df38298c3284f98cb92b2de5
# Hash despues add:5d55e12a0872e83ade8ddbce1602de28168003141de1496862305944acbe31f3

#start_time = time.time()
#i = tiplsb("img/600_2.png")
#print("Hash despues INIT:"+i.hash_image)
#i.add("Insert3", "PLATPRUEBA3")
#i.save('img/600_3.png')
#print("Inicializada la imagen")
#print("--- %s seconds ---" % (time.time() - start_time))
#print("Hash despues add:"+i.hash_image)

# Hash despues INIT:5d55e12a0872e83ade8ddbce1602de28168003141de1496862305944acbe31f3
# Hash despues add:d5f38816e733e2c33458abc519620fbb97eb4316c0da1f53f0a2aaf7c87ca905
