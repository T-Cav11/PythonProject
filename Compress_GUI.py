import FreeSimpleGUI as sg
from zip_creator import make_archive

label_1 = sg.Text("Select files to compress: ")
input_1 = sg.Input()
choose_button_1 = sg.FileBrowse("Choose", key= "files")

label_2 = sg.Text("Select destination folder: ")
input_2 = sg.Input()
choose_button_2 = sg.FolderBrowse("Choose", key="folder")

compress_button = sg.Button("Compress")

window = sg.Window("File Compressor",
                   [[label_1, input_1, choose_button_1], [label_2, input_2, choose_button_2]
                    ,[compress_button]])

while True:
    event, values = window.read()
    print(event,values)
    filepaths = values["files"].split(";")
    folder = values["folder"]
    make_archive(filepaths,folder)


window.read()
window.close()