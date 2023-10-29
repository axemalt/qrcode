from qr_code import make_code, decode_code
from tkinter import *
import tkinter.filedialog

CANVAS_SIZE = "700x300"
TITLE_FONT = "Arial 20"

def encode(root):
    frame0 = Frame(root)
    Label(frame0, text="Make Qrcode", font=TITLE_FONT).pack()
    frame0.pack()

    frame1 = Frame(root)
    Label(frame1, text="Content of Qrcode").pack(side=LEFT)
    content_entry = Entry(frame1)
    content_entry.pack(side=LEFT)
    frame1.pack()

    frame2 = Frame(root)
    browse_label = Label(frame2, wraplength=root.winfo_width()/2)
    browse_label.pack(side=LEFT)
    def get_path():
        file_path = tkinter.filedialog.askdirectory()
        browse_label.config(text=file_path)
        submit_button["state"] = NORMAL
    Button(frame2, text="Select Download Path", command=get_path).pack(side=LEFT)
    frame2.pack()

    frame3 = Frame(root)
    def submit_stuff():
        code = make_code(content_entry.get())
        code.save(browse_label.cget("text") + "/qrcode.png")
    submit_button = Button(frame3, text="Submit", command=submit_stuff, state=DISABLED)
    submit_button.pack()
    frame3.pack()

def decode(root):
    frame0 = Frame(root)
    Label(frame0, text="Decode Qrcode", font=TITLE_FONT).pack()
    frame0.pack()

    frame1 = Frame(root)
    browse_label = Label(frame1, wraplength=root.winfo_width()/2)
    browse_label.pack(side=LEFT)
    def get_path():
        file_path = tkinter.filedialog.askopenfilename()
        browse_label.config(text=file_path)
        submit_button["state"] = NORMAL
    Button(frame1, text="Select Qrcode Path", command=get_path).pack(side=LEFT)
    frame1.pack()

    frame2 = Frame(root)
    def submit_stuff():
        data = decode_code(browse_label.cget("text"))
        print(data)
    submit_button = Button(frame2, text="Submit", command=submit_stuff, state=DISABLED)
    submit_button.pack()
    frame2.pack()

root = Tk()
root.title("Qrcode App")
root.geometry(CANVAS_SIZE)
root.grid_columnconfigure(0, weight=1, uniform="group1")
root.grid_columnconfigure(1, weight=1, uniform="group1")
root.grid_rowconfigure(0, weight=1, uniform="group1")

encode_frame = Frame(root, background="red")
decode_frame = Frame(root, background="green")
encode_frame.grid(row=0, column=0, sticky="nsew")
decode_frame.grid(row=0, column=1, sticky="nsew")

root.update()

encode(encode_frame)
decode(decode_frame)

root.mainloop()