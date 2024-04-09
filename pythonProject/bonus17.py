import PySimpleGUI as sg
from extractor import *

sg.theme("Black")

label1 = sg.Text("Select Archive: ")
input1 = sg.Input()
choose_button1 = sg.FileBrowse("Choose", key="files")

label2 = sg.Text("Select Folder: ")
input2 = sg.Input()
choose_button2 = sg.FolderBrowse("Choose", key="folder")

button_decompress = sg.Button("Extract")
label_output = sg.Text(key="Output", text_color="green")

window = sg.Window("Archive Extractor", layout=[[label1, input1, choose_button1],
                                                [label2, input2, choose_button2],
                                                [button_decompress, label_output]])

while True:
    event, values = window.read()
    print(event, values)
    archive_path = values["files"]
    folder = values["folder"]
    archive_extract(archive_path, folder)
    window["Output"].update(value="File Extracted Successfully!")



window.close()