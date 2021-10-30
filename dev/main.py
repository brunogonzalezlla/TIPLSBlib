from TIPLSB import tiplsb

try:
    tip = tiplsb('/home/bruno/Escritorio/Universidad/TFG/py/img/gato.png')
    tip.init('Bruno', 'US')
    print("Imagen inicializada")
    print(tip.details())
    tip.save()
except Exception as e:
    print("Añadida nueva persona")
    print(tip.details())
    tip.add('Pepe', 'Facebook')
    print(tip.details())
    tip.save()