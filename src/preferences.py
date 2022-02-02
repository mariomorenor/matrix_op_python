import pickle
from pathlib import Path
import os

user_path = f'{Path.home()}/AppData/Roaming'
os.chdir(user_path)
try: 
    os.mkdir("matrix_operator")
except:
    print("Ya existe la carpeta")
    
def guardar_datos(nombre,data):
    archivo = open(f'{user_path}/matrix_operator/{nombre}',"wb")
    pickle.dump(data,archivo)

def recuperar_datos(nombre):
    archivo = open(f'{user_path}/matrix_operator/{nombre}',"rb")
    return pickle.load(archivo)

