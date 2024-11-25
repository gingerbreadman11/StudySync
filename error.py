import PySimpleGUI as sg
import tkinter as tk

# Custom event binding to handle light taps on macOS
def enable_tap_click(window):
    window.bind('<Button-1>', lambda e: e.widget.event_generate('<ButtonRelease-1>'))

# Define the GUI layout
layout = [[sg.Text('Tap anywhere to test.')], [sg.Button('Exit')]]
window = sg.Window('Tap-to-Click Fix', layout, finalize=True)

# Enable tap-to-click for the Tkinter window
enable_tap_click(window.TKroot)

while True:
    event, values = window.read()
    if event in (sg.WINDOW_CLOSED, 'Exit'):
        break
window.close()

