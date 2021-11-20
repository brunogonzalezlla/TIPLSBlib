from .class_tiplsb import tiplsb
from .function_additional import *
from PIL import Image
import hashlib
import random

def tip_decode(path_original, path_modified):
    # Open original image
    img_original = Image.open(path_original, 'r').convert('RGB')
    # Open modified image
    img_modified = tiplsb(path_modified)


    h = hashlib.sha256(img.tobytes()).hexdigest()
    width, height = img.size
    img_array = np.array(list(img.getdata()))
    print("Hash abierta")
    print(hashlib.sha256(img.tobytes()).hexdigest())
    img_modified = tiplsb(path_modified)
    # Hash Image
    with open(path_original, "rb") as f:
        bytes_image = f.read()
        hash_actual = hashlib.sha256(bytes_image).hexdigest()
    random.seed(hash_actual)
    l = random.sample(range(0, max_index_element_ring(img_modified.init['Line'], img_modified.width, img_modified.height)), k=48)


# Función que lea un registro con su redundancia. Devuelve String obtenido y list_index consultado
