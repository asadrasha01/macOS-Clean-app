import PySimpleGUI as sg
import quit_app
import clean_bin

sg.theme('Dark Grey 13')   

layout = [  [sg.Text('Welcome to MacOS Cleaner')],
            [sg.Text('Choose:'), ],
            [sg.Button('Quit all app'), sg.Button('Clean bin')] ]

window = sg.Window("MacOS Clean", layout)

while True:
    event, values = window.read()
    if event == 'Quit all app':
        try:
            quit_app.quit_all_app()
            sg.popup('All applications successfully have been closed')
            break
        except Exception as e:
            sg.popup(f"An error occurred: {e}")
    elif event == 'Clean bin':
        try:
            clean_bin.cleaning_bin()
            sg.popup('Your bin has been cleaned')
            break
        except Exception as e:
            sg.popup(f"An error occurred: {e}")
    elif event == sg.WINDOW_CLOSED:
        break

window.close()
