import PySimpleGUI as sg
sg.theme("Darkblue4")
sg.theme_text_color("#FFFf00")
window = sg.Window(title="Profile",
layout=[[sg.Text("SELAMAT DATANG DI KELAS",
font=("Arial",25,"italic","bold","underline"))],
[sg.Text("NPM : 2210010639 ")],
[sg.Text("Nama : Ahmad Zainur Makruf  ")],
[sg.Text("Kelas: 5A Non-Regular Banjarmasin ")]
],
size=(510,200),
font=("Times", 18))
window()
window.close()