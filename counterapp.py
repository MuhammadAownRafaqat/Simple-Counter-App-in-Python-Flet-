import flet as ft
import os

app_data_path = os.getenv("FLET_APP_STORAGE_DATA")
my_file_path = os.path.join(app_data_path, "fletfilestorage.txt")

def save_state(value):
    with open(my_file_path, "w") as f:
        f.write(str(value))


def load_state():
        try:
            with open(my_file_path, "r") as f:
                 returnvariable = f.read()
                 return int(returnvariable) if returnvariable else 0
        except FileNotFoundError:
             return 0



def afunction(page: ft.Page):
    page.window.width = 500
    page.window.height = 500
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"

    thebutton = ft.TextButton(text= "Press", on_click = lambda _: increasenumber())
    

    thenumber = load_state() 

    def increasenumber():
        nonlocal thenumber 
        thenumber += 1        
        page.controls.clear()
        page.add(thebutton)
        shownumber = ft.Text(str(thenumber))   
        page.add(shownumber)               
        save_state(thenumber)     
    





    
    page.add(thebutton)

ft.app(afunction)