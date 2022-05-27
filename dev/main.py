from TIPLSB import tiplsb
from TIPLSB import tip_decode
import os


# i = tiplsb("img/600x600.jpg", hash='sha512')
# i.add("PruebaPrimera", "PlataformaPrimera")
# i.save('img/600x600_P1.png')
#
# i2 = tiplsb("img/600x600_P1.png")
# i2.add("PruebaSegunda", "PlataformaSegunda")
# i2.save('img/600x600_P2.png')
#
# i3 = tiplsb("img/600x600_P2.png")
# i3.add("PruebaTercera", "PlataformaTercera")
# i3.save('img/600x600_P3.png')

sol = tip_decode('img/img_original.png', 'img/img_modificada.png')
print(sol)

#os.remove("img/600x600_P1.png")
#os.remove("img/600x600_P2.png")
#os.remove("img/600x600_P3.png")



