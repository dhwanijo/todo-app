import PySimpleGUI as sg

label1 = sg.Text("Choose file to compress: ")
text_input1 = sg.Input(tooltip="Enter a filename")
button1 = sg.FilesBrowse("Choose")

label2 = sg.Text("Select destination folder: ")
text_input2 = sg.Input(tooltip="Enter the folder name")
button2 = sg.FolderBrowse("Choose")

button3 = sg.Button("Compress")

window = sg.Window("File Zipper",
                   [[label1, text_input1, button1],
                                   [label2, text_input2, button2],
                                   [button3]])
window.read()
window.close()