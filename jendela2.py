import PySimpleGUI as sg
sg.theme("DarkBlue4")
sg.theme_text_color("#FFFff0")
window = sg.Window(title="Profile",
layout=[[sg.Text("NPM : 2210010639 ")],
[sg.Text("Nama : Ahmad Zainur Makruf  ")],
[sg.Text("Kelas: 5A Non-Regular Banjarmasin ")]
],
size=(400,200),
font=("Times", 18))
window()
window.close()