import functions
import PySimpleGUI as sg

label = sg.Text("Napiš ulohu:")
input_box = sg.InputText(tooltip="Enter todo")
add_button = sg.Button("Add")

window = sg.Window("Nas velky program ty chuju glupy", layout=[[label, input_box, add_button]])
window.read()
window.close()