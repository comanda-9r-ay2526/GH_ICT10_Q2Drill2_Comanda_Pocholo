# data from textbox
from pyscript import display, document


def naemu(e):
    document.getElementById("duy").innerHTML = " "
    Fname = document.getElementById("firstname").value
    Lname = document.getElementById("lolname").value
    F2name = Fname + ' ' + Lname
    ruby_last = ['mohammad calaca', 'jm piansay', 'joaquin tabije', 'lucian veran', 'daphne mariano', 'macy panela', 'bela allas']

    LAname = document.getElementById('lolname').value.lower().strip()
    FIname = document.getElementById('firstname').value.lower().strip()
    FUname = FIname + ' ' + LAname
    print(FUname)
    check = FUname in ruby_last # reel(1) or feyk(0)

    display_message = (f'Sorry, your name is not in the list.', f'{F2name} is in the list')
    display(display_message[check], target="duy")