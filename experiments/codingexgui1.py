import PySimpleGUI as sg
from converters import convert


label_feet = sg.Text("Enter Feet: ")
input_feet = sg.Input(key="feet")

label_inches = sg.Text("Enter Inches: ")
input_inches = sg.Input(key="inches")

convert_button = sg.Button("Convert")
output_label = sg.Text(key="output", text_color="Black")

window = sg.Window("Convertor", [[label_feet, input_feet],
                                 [label_inches, input_inches],
                                 [convert_button, output_label]])

while True:
    event, values = window.read()
    print(event, values)
    feet = float(values["feet"])
    inches = float(values["inches"])
    meter = convert(feet, inches)
    window["output"].update(value=f"{meter}m")



window.close()


