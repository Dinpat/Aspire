from pathlib import Path
import tkinter as tk
from tkinter import ttk

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"D:\Semester II\UAS Semester 2\Python\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = tk.Tk()
window.geometry("950x600")
window.configure(bg="#FFD74A")

canvas = tk.Canvas(
    window,
    bg="#FFD74A",
    height=600,
    width=950,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x=0, y=0)
canvas.create_text(
    101.0,
    88.0,
    anchor="nw",
    text="WELCOME TO ASPIRA",
    fill="#000000",
    font=("Bold", 24 * -1)
)

entry_image_1 = tk.PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    231.5,
    211.5,
    image=entry_image_1
)
name_entry = tk.Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
name_entry.place(
    x=65.0,
    y=191.0,
    width=333.0,
    height=39.0
)

entry_image_2 = tk.PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    231.5,
    279.5,
    image=entry_image_2
)
class_entry = tk.Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
class_entry.place(
    x=65.0,
    y=259.0,
    width=333.0,
    height=39.0
)

entry_image_3 = tk.PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    231.5,
    403.0,
    image=entry_image_3
)
aspiration_entry = tk.Text(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
aspiration_entry.place(
    x=65.0,
    y=327.0,
    width=333.0,
    height=150.0
)

canvas.create_text(
    66.0,
    172.0,
    anchor="nw",
    text="Nama",
    fill="#1E1E1E",
    font=("Inter SemiBold", 12 * -1)
)

canvas.create_text(
    66.0,
    240.0,
    anchor="nw",
    text="Kelas",
    fill="#1E1E1E",
    font=("Inter SemiBold", 12 * -1)
)

canvas.create_text(
    66.0,
    308.0,
    anchor="nw",
    text="Aspirasi",
    fill="#1E1E1E",
    font=("Inter SemiBold", 12 * -1)
)

def submit_data():
    # Get data from entry fields
    name = name_entry.get()
    class_ = class_entry.get()
    aspiration = aspiration_entry.get("1.0", "end-1c")
    
    # Save data to a file
    with open("aspiration_data.txt", "a") as f:
        f.write(f"Nama: {name}\nKelas: {class_}\nAspirasi: {aspiration}\n\n")

    # Clear entry fields
    name_entry.delete(0, tk.END)
    class_entry.delete(0, tk.END)
    aspiration_entry.delete("1.0", tk.END)

button_image_1 = tk.PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = tk.Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=submit_data,
    relief="flat"
)
button_1.place(
    x=144.0,
    y=519.0,
    width=175.0,
    height=41.0
)

image_image_1 = tk.PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    78.0,
    44.0,
    image=image_image_1
)

canvas.create_text(
    250.0,
    130.0,
    anchor="center",
    text="Tuangkan aspirasimu dan jadikan pedoman menuju kesuksesan.\n\tWujudkan mimpi menjadi kenyataan!",
    fill="#000000",
    font=("Inter SemiBold", 12 * -1)
)

image_image_2 = tk.PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    706.0,
    300.0,
    image=image_image_2
)
window.resizable(False, False)
window.mainloop()