""" Entry point"""

import PySimpleGUI as sg
from storage import storage_service
from deltalake import PyDeltaTableError

id = "123"

try:
    table = storage_service.get_data(id)
except PyDeltaTableError as err:
    print(err)
    exit()

sg.Window(title="Hello World", layout=[[]], margins=(100, 50)).read()
