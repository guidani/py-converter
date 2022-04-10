import PySimpleGUI as sg

layout = [
    [sg.Text('From: '), sg.Spin(['Km to Miles', 'Miles to Km'], key='-SPIN1-')],
    [sg.Input(key='-INPUT1-')],
    [sg.Button('Calculate', key = '-CALCULATE-', tooltip = 'Executar', size=(10, 1), button_color = '#ff6600', font = 30, expand_x = True)],
    [sg.Text(' ', enable_events = True, key = '-RESULT_SHOW-')]
    
]

def km_to_miles(input_value):
    result = round(float(input_value) * 0.6214, 2)
    result_string = f'{input_value} Kilometers are equal to {result} Miles'
    update_window(result_string)
    


def miles_to_km(input_value):
    result = round(float(input_value) * 1.609, 2)
    result_string = f'{input_value} Miles are equal to {result} Kilometers'
    update_window(result_string)


def update_window(result_string):
    window['-RESULT_SHOW-'].update(result_string)

window = sg.Window('Converter', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == '-CALCULATE-':     
        spin_1 = values['-SPIN1-']
        input_value = values['-INPUT1-']
        if input_value.replace(' ', '') == '':
            window['-RESULT_SHOW-'].update('Insert numeric value')
        else:
            if spin_1 == 'Km to Miles':
                km_to_miles(input_value)
            elif spin_1 == 'Miles to Km':
                miles_to_km(input_value)

    
window.close()