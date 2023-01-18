from Modules.functions import *
import PySimpleGUI as sg

lable = sg.Text("Type in a To-Do")
input_box = sg.InputText(tooltip="Enter a To-Do")
add_button = sg.Button("Add")

window = sg.Window("My To-Do App", layout=[[lable], [input_box, add_button]])
window.read()
window.close()