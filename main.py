from qr_code import make_code, decode_code
from tkinter import *
from tkinter import filedialog, messagebox
import os

CANVAS_SIZE = "700x300"
TITLE_FONT = "Arial 20"
FRAME_PADDING = 5

paths = ["", ""]

def encode(root):
    frame0 = Frame(root, pady=FRAME_PADDING)
    Label(frame0, text="Create QR Code", font=TITLE_FONT).pack()
    frame0.pack()

    frame1 = Frame(root, pady=FRAME_PADDING)
    Label(frame1, text="Content of QR Code").pack(side=LEFT)
    content_entry = Entry(frame1)
    content_entry.pack(side=LEFT)
    frame1.pack()

    frame2 = Frame(root, pady=FRAME_PADDING)
    browse_label = Label(frame2, wraplength=root.winfo_width()/2)
    browse_label.pack(side=LEFT)
    def get_path():
        file_path = filedialog.askdirectory()
        browse_label.config(text=file_path.split("/")[-1])
        submit_button["state"] = NORMAL
        paths[0] = file_path
    Button(frame2, text="Select Download Path", command=get_path).pack(side=LEFT)
    frame2.pack()

    frame3 = Frame(root, pady=FRAME_PADDING)
    def submit_stuff():
        code = make_code(content_entry.get())
        if not os.path.isfile(f"{paths[0]}/qrcode.png"):
            i = ""
            code.save(f"{paths[0]}/qrcode.png")
        else:
            i = 0
            while os.path.isfile(f"{paths[0]}/qrcode{i}.png"):
                i += 1
            code.save(f"{paths[0]}/qrcode{i}.png")
        messagebox.showinfo(title="Success", message=f"QR code saved as \"qrcode{i}.png.\"")
    submit_button = Button(frame3, text="Download", command=submit_stuff, state=DISABLED)
    submit_button.pack()
    frame3.pack()

def decode(root):
    frame0 = Frame(root, pady=FRAME_PADDING)
    Label(frame0, text="Decode QR Code", font=TITLE_FONT).pack()
    frame0.pack()

    frame1 = Frame(root, pady=FRAME_PADDING)
    browse_label = Label(frame1, wraplength=root.winfo_width()/2)
    browse_label.pack(side=LEFT)
    def get_path():
        file_path = filedialog.askopenfilename()
        browse_label.config(text=file_path.split("/")[-1])
        submit_button["state"] = NORMAL
        paths[1] = file_path
    Button(frame1, text="Select QR Code Path", command=get_path).pack(side=LEFT)
    frame1.pack()

    frame2 = Frame(root, pady=FRAME_PADDING)
    def submit_stuff():
        data = decode_code(paths[1])
        root.clipboard_clear()
        root.clipboard_append(data)
        root.update()
        messagebox.showinfo(title="Success", message=f"QR code data \"{data}\" copied to clipboard.")
    submit_button = Button(frame2, text="Decode", command=submit_stuff, state=DISABLED)
    submit_button.pack()
    frame2.pack()

root = Tk()
root.title("QR Code App")
root.geometry(CANVAS_SIZE)
root.grid_columnconfigure(0, weight=1, uniform="group1")
root.grid_columnconfigure(1, weight=1, uniform="group1")
root.grid_rowconfigure(0, weight=1, uniform="group1")

encode_frame = Frame(root)
decode_frame = Frame(root)
encode_frame.grid(row=0, column=0, sticky="nsew")
decode_frame.grid(row=0, column=1, sticky="nsew")

root.update()

encode(encode_frame)
decode(decode_frame)

root.mainloop()