import PySimpleGUI as sg

label_feet = sg.Text("Enter Feet: ")
input_feet = sg.Input()

label_inches = sg.Text("Enter Inches: ")
input_inches = sg.Input()

convert_button = sg.Button("Convert")

window = sg.Window("Convertor", [[label_feet, input_feet],
                                 [label_inches, input_inches],
                                 [convert_button]])
window.read()
window.close()

