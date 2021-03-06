import tkinter
import webbrowser
import Enigma
from time import sleep

#init of the display
root = tkinter.Tk()
root.geometry("1000x1000")
root.title("Enigma")
head = tkinter.Label(root, text="Enigma Toolkit", anchor='w', font=("Helvetica", 13))

#All the boring text
welcome_message = "Hello and welcome to Enigma Toolkit. This small software will allow you to simulate the simplified functioning of an Enigma machine, used by the Germans during the Second World War. Several options are offered to you, I let you Explore them and have fun with these little cryptography tools!"
github = "Enigma Tool is still being developped, as other Efrei related-projects such as EfreiZ, or personal projects. Follow all these here :  "
#functions
slow = tkinter.IntVar()

def shuffle():
    entry_rotor1.delete(0, tkinter.END)
    entry_rotor2.delete(0, tkinter.END)
    entry_rotor1.insert(0, Enigma.shuffle())
    entry_rotor2.insert(0, Enigma.shuffle())


def entry_to_tab(entry):
    tab = [0 for i in range(26)]
    i = 0
    for j in entry:
        if j != " ":
            tab[i] = j
            i += 1
    return tab


def decode():
    if entry_rotor1.get() == "Rotor1" or entry_rotor2.get() == "Rotor2":
        return None
    else:
        code, rotor1, rotor2 = coded_message.get("1.0", tkinter.END)[:-1], entry_to_tab(entry_rotor1.get()), entry_to_tab(entry_rotor2.get())
        decoded_message.delete("1.0", tkinter.END)
        if slow.get() == 0:
            decoded_message.insert("1.0", Enigma.decode(rotor1, rotor2, code))
        else:
            message = Enigma.decode(rotor1, rotor2, code)
            for i in message:
                decoded_message.insert(tkinter.END, i)
                root.update()
                sleep(.1)

def code():
    if entry_rotor1.get() == "Rotor1" or entry_rotor2.get() == "Rotor2":
        return None
    else:
        decode, rotor1, rotor2 = decoded_message.get("1.0", tkinter.END)[:-1], entry_to_tab(entry_rotor1.get()), entry_to_tab(entry_rotor2.get())
        coded_message.delete("1.0", tkinter.END)
        if slow.get() == 0:
            coded_message.insert("1.0", Enigma.code(rotor1, rotor2, decode))
        else:
            message = Enigma.code(rotor1, rotor2, decode)
            for i in message:
                coded_message.insert(tkinter.END, i)
                root.update()
                sleep(.1)


def enigma_decode():
    if len(init1.get()) != 1 or len(init2.get()) != 1 or entry_rotor1.get() == "Rotor1" or entry_rotor2.get() == "Rotor2":
        return None
    else:
        code, rotor1, rotor2, r1, r2 = coded_message.get("1.0", tkinter.END)[:-1], entry_to_tab(entry_rotor1.get()), entry_to_tab(entry_rotor2.get()), init1.get(), init2.get()
        decoded_message.delete("1.0", tkinter.END)
        if slow.get() == 0:
            decoded_message.insert("1.0", Enigma.enigma_decode(rotor1, rotor2, r1, r2, code))
        else:
            message = Enigma.enigma_decode(rotor1, rotor2, r1, r2, code)
            for i in message:
                decoded_message.insert(tkinter.END, i)
                root.update()
                sleep(.1)


def enigma_code():
    if len(init1.get()) != 1 or len(init2.get()) != 1 or entry_rotor1.get() == "Rotor1" or entry_rotor2.get() == "Rotor2":
        return None
    else:
        decode, rotor1, rotor2, r1, r2 = decoded_message.get("1.0", tkinter.END)[:-1], entry_to_tab(entry_rotor1.get()), entry_to_tab(entry_rotor2.get()), init1.get(), init2.get()
        coded_message.delete("1.0", tkinter.END)
        if slow.get() == 0:
            coded_message.insert("1.0", Enigma.enigma_code(rotor1, rotor2, r1, r2, decode))
        else:
            message = Enigma.enigma_code(rotor1, rotor2, r1, r2, decode)
            for i in message:
                coded_message.insert(tkinter.END, i)
                root.update()
                sleep(.1)


def turing_decode():
    if entry_rotor1.get() == "Rotor1" or entry_rotor2.get() == "Rotor2":
        return None
    else:
        rotor1, rotor2, code, guess = entry_to_tab(entry_rotor1.get()), entry_to_tab(entry_rotor2.get()), coded_message.get("1.0", tkinter.END)[:-1], probable_message.get()
        decoded_message.delete("1.0", tkinter.END)
        if slow.get() == 0:
            decoded_message.insert("1.0", Enigma.turing_decode(rotor1, rotor2, code, guess))
        else:
            message = Enigma.turing_decode(rotor1, rotor2, code, guess)
            for i in message:
                decoded_message.insert(tkinter.END, i)
                root.update()
                sleep(.1)

    
def go_to_git():
    webbrowser.open("https://github.com/RousselotN")


#widgets
welcome = tkinter.Frame(root, width=300, height=200, borderwidth=1)
welcome_text = tkinter.Label(welcome, text=welcome_message, wraplength=1000, anchor='w', justify='center', font=("Helvetica", 11))
github_text = tkinter.Label(root, text=github, wraplength=1000, anchor='w', justify="center", font=("Helvetica", 11))
github_button = tkinter.Button(root, text="My GitHub", command=go_to_git)
coded = tkinter.LabelFrame(root, width=500, height=200, borderwidth=1, text="Coded Text")
coded_b_frame = tkinter.Frame(coded)
coded_message = tkinter.Text(coded, height=7, width=80)
decoded = tkinter.LabelFrame(root, width=500, height=200, borderwidth=1, text="Decoded Text")
decoded_b_frame = tkinter.Frame(decoded)
decoded_message = tkinter.Text(decoded, height=7, width=80) 
rotor = tkinter.LabelFrame(root, width=500, height=200, borderwidth=1, text="Rotors")
abc = tkinter.Label(rotor, text="A B C D E F G H I J K L M N O P Q R S T U V W X Y Z")
entry_rotor1 = tkinter.Entry(rotor, width=41)
entry_rotor1.insert(0, "Rotor1")
entry_rotor2 = tkinter.Entry(rotor, width=41)
entry_rotor2.insert(0, "Rotor2")
shuffle = tkinter.Button(rotor, text="Create random rotors", command=shuffle)
decode_b = tkinter.Button(coded_b_frame, text="Simple decode", command=decode)
code_b = tkinter.Button(decoded_b_frame, text="Simple code", command=code)
enigma_decode_b = tkinter.Button(coded_b_frame, text="Enigma Decode", command=enigma_decode)
enigma_code_b = tkinter.Button(decoded_b_frame, text="Enigma Code", command=enigma_code)
init = tkinter.LabelFrame(rotor, text="Initial Positions")
init1 = tkinter.Entry(init, width=4)
init2 = tkinter.Entry(init, width=4)
init1.insert(0, "Init1")
init2.insert(0, "Init2")
turing_decode_b = tkinter.Button(coded_b_frame, text="Turing Decode", command=turing_decode)
probable_message = tkinter.Entry(coded_b_frame, width=15)
probable_message.insert(0, "Probable word(s)")
slow_mode = tkinter.Checkbutton(rotor, text="Slow", onvalue=1, offvalue=0, variable=slow)


#Display construction
head.pack(side="top")
welcome.pack(side="top")
welcome_text.pack(fill="both")
coded.pack(padx=50, pady=5, fill="both")
coded_message.pack(fill="both", padx=10, pady=5)
coded_b_frame.pack()
decode_b.pack(in_=coded_b_frame, side="left")
enigma_decode_b.pack(in_=coded_b_frame, side="left")
turing_decode_b.pack(in_=coded_b_frame, side="left")
probable_message.pack(in_=coded_b_frame, side="left")
rotor.pack(padx=50, pady=5, fill="both")
abc.pack()
entry_rotor1.pack()
entry_rotor2.pack()
shuffle.pack()
init.pack()
init1.pack(in_=init, side="left")
init2.pack(in_=init, side="left")
slow_mode.pack()
decoded.pack(padx=50, pady=5, fill="both")
decoded_message.pack(fill="both", padx=10, pady=5)
decoded_b_frame.pack()
code_b.pack(in_=decoded_b_frame, side="left")
enigma_code_b.pack(in_=decoded_b_frame, side="left")
decoded.pack(padx=50, pady=5, fill="both")
decoded_message.pack(fill="both", padx=10, pady=5)
github_text.pack()
github_button.pack()
root.mainloop()
