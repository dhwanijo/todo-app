import PySimpleGUI as sg
from zip_creator import make_archive

label1 = sg.Text("Choose file to compress: ")
text_input1 = sg.Input(tooltip="Enter a filename")
button1 = sg.FilesBrowse("Choose", key="files")

label2 = sg.Text("Select destination folder: ")
text_input2 = sg.Input(tooltip="Enter the folder name")
button2 = sg.FolderBrowse("Choose", key="folder")

button3 = sg.Button("Compress")
output_label = sg.Text(key="output", text_color="Black")

window = sg.Window("File Zipper",
                   [[label1, text_input1, button1],
                         [label2, text_input2, button2],
                         [button3, output_label]])
while True:
    event, values = window.read()
    print(event, values)
    filepaths = values["files"].split(";")
    folder = values["folder"]
    make_archive(filepaths, folder)
    window["output"].update("Compression completed !")

window.close()