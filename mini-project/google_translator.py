#Google Translator
from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES

def change(text="type", src="en", dest="hi"):
    trans = Translator()
    trans1 = trans.translate(text, src=src, dest=dest)
    return trans1.text

def get_lang_code(lang_name):
    for code, name in LANGUAGES.items():
        if name.lower() == lang_name.lower():
            return code
    return "en"

def data():
    s = get_lang_code(cmb_src.get())
    d = get_lang_code(cmb_dest.get())
    msg = src_txt.get(1.0, END)
    text_get = change(text=msg, src=s, dest=d)
    dest_txt.delete(1.0, END)
    dest_txt.insert(END, text_get)

root = Tk()
root.title("Translator")
root.geometry("500x600")
root.config(bg='lightblue')

lbl_txt = Label(root, text="Translator", font=("Times New Roman", 30, "bold"))
lbl_txt.place(x=100, y=40, height=50, width=300)

lbl_txt = Label(root, text="Source Text", font=("Times New Roman", 20, "bold"), bg='lightblue', fg='Black')
lbl_txt.place(x=100, y=100, height=20, width=300)

frame = Frame(root)
frame.pack(side=BOTTOM)

src_txt = Text(root, font=("Times New Roman", 20, "bold"), wrap=WORD)
src_txt.place(x=10, y=130, height=150, width=480)

list_text = list(LANGUAGES.values())

cmb_src = ttk.Combobox(root, value=list_text)
cmb_src.place(x=10, y=300, height=40, width=150)
cmb_src.set("English")

button_change = Button(root, text="Translate To", relief=RAISED, command=data)
button_change.place(x=170, y=300, height=40, width=150)

cmb_dest = ttk.Combobox(root, value=list_text)
cmb_dest.place(x=330, y=300, height=40, width=150)
cmb_dest.set("Hindi")

lbl_txt = Label(root, text="Dest Text", font=("Times New Roman", 20, "bold"), bg='lightblue', fg='Black')
lbl_txt.place(x=100, y=360, height=20, width=300)

dest_txt = Text(root, font=("Times New Roman", 20, "bold"), wrap=WORD)
dest_txt.place(x=10, y=400, height=150, width=480)

root.mainloop()
