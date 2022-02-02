
from tkinter import *
from tkinter.ttk import Treeview
from ttkwidgets import CheckboxTreeview
import preferences


def init(parentWin):

    global trvFiltrosCheckbox

    filtrosWindow = Toplevel(name="filtros_window")
    filtrosWindow.title("Filtros")
    filtrosWindow.attributes("-topmost", True)

    trvFiltrosCheckbox = CheckboxTreeview(filtrosWindow)
    trvFiltrosCheckbox.heading("#0", text="Zonas de Servicio")
    
    Button(filtrosWindow, text="ACEPTAR", width=20, command=guardar_zonas_seleccionadas).pack(pady=10)
    
    zonas_servicio = obtener_zonas_servicio()
    zonas_seleccionadas = preferences.recuperar_datos(nombre="zonas")

    for categoria in zonas_servicio:
        row = trvFiltrosCheckbox.insert("", index=END, text=categoria["categoria"], open=True)
        # Variable para indicar si el registro padre está marcado
        estado_row = "unchecked"
        # Se recorre el array
        for provincia in categoria["provincias"]:
            sub_row = trvFiltrosCheckbox.insert(parent=row, index=END, text=provincia["nombre"], open=True)
            # Variable para indicar si el registro subpadre está marcado
            indicador_sub_row = 0
            
            for zona in provincia["zonas"]:
                z = trvFiltrosCheckbox.insert(parent=sub_row, index=END, text=zona["display_name"],iid=zona["id"])
                # Si la zona ya está en las preferencias de usuario entonces se marca con el check
                if str(zona["id"]) in zonas_seleccionadas:
                    indicador_sub_row += 1
                    trvFiltrosCheckbox.change_state(item=z,state="checked")

            # Si la cantidad de hijos del nodo es igual al contador indicador_sub_row entonces se marca el check
            if indicador_sub_row == len(trvFiltrosCheckbox.get_children(sub_row)):
                trvFiltrosCheckbox.change_state(item=sub_row,state="checked")
                estado_row = "checked"
                # Si la cantidad de hijos del nodo es mayor que cero entonces se marca el check a medias 
            elif indicador_sub_row > 0:
                trvFiltrosCheckbox.change_state(item=sub_row,state="tristate")
                estado_row="tristate"
        
        trvFiltrosCheckbox.change_state(item=row,state=estado_row)
                
    trvFiltrosCheckbox.pack(fill=X, ipady=40)

    return filtrosWindow


def guardar_zonas_seleccionadas():
    zonas_seleccionadas = trvFiltrosCheckbox.get_checked()
    preferences.guardar_datos(nombre="zonas",data=zonas_seleccionadas)


def obtener_zonas_servicio():

    # DATA TEST
    return [
        {
            "categoria": "Z1",
            "provincias": [
                {
                    "nombre": "Quevedo",
                    "zonas": [
                        {
                            "display_name": "Norte",
                            "id": 1
                        }
                    ]
                }
            ],
        },
        {
            "categoria": "Z2",
            "provincias": [
                {
                    "nombre": "Quevedo",
                    "zonas": [
                        {
                            "display_name": "Norte",
                            "id": 2
                        },
                        {
                            "display_name": "Norte",
                            "id": 3
                        },
                        {
                            "display_name": "Norte",
                            "id": 4
                        },
                    ]
                }
            ],
        },
        {
            "categoria": "Z2",
            "provincias": [
                {
                    "nombre": "Quevedo",
                    "zonas": [
                        {
                            "display_name": "Norte",
                            "id": 5
                        }
                    ]
                }
            ],
        },
        {
            "categoria": "Z2",
            "provincias": [
                {
                    "nombre": "Quevedo",
                    "zonas": [
                        {
                            "display_name": "Norte",
                            "id": 6
                        }
                    ]
                }
            ],
        },
    ]
