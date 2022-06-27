""" Entry point"""

import PySimpleGUI as sg
from storage import storage_service
from deltalake import PyDeltaTableError
from elements import table_element

# id = "123"

# try:
#     table = storage_service.get_data(id)
# except PyDeltaTableError as err:
#     print(err)
#     exit()

layout = [table_element.table]

window = sg.Window(title="Hello World", layout=layout, resizable=True).read()

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

window.close()