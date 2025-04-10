import FreeSimpleGUI as sg
def convert(feet,inches):
    conversion = feet * 0.3048 + inches * 0.0254
    return conversion

label_Feet = sg.Text("Enter feet: ")
input_box_feet = sg.InputText( key = "feet")

label_inches = sg.Text("Enter inches: ")
input_box_inches = sg.InputText( key = "inches")

convert_button = sg.Button("Convert")
output_label = sg.Text("", key="output")

window = sg.Window("Converter",
                   [[label_Feet, input_box_feet], [label_inches, input_box_inches],[convert_button, output_label]],
                   font= ("Helvetica", 8))

while True:
    event, values = window.read()
    feet = float(values["feet"])
    inches = float(values["inches"])

    result = convert(feet,inches)
    window["output"].update(value = f"{result}m", text_color="white")


window.close()
print("test")