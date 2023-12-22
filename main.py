from PIL import Image, ImageDraw, ImageFont
import tkinter as tk
from tkinter import filedialog
import time

image_path = None
output_path = f"outputs/{time.strftime('%Y%m%d%H%M%S')}.jpg"
print(output_path)
watermark_text = None


def output_file():
    path_output = filedialog.askopenfilename(title="Output path:")
    return path_output


def add_watermark():
    file_path = filedialog.askopenfilename(title="Choose your file:")
    if file_path is not None:
        image_opened = Image.open(file_path)
        draw = ImageDraw.Draw(image_opened)

        font = ImageFont.truetype("font.ttf", 12)

        width, height = image_opened.size

        x_position = width/2
        y_position = height/2

        text_color = (255, 255, 255, 150)

        draw.text((x_position, y_position), wm_entry.get(), font=font, fill=text_color)

        image_opened.save(output_path)
        print("ok")
    else:
        print("passed")
        pass


window = tk.Tk()
window.title("Watermark adder")
window.geometry("500x500")

wm_entry = tk.Entry(window, width=20)
wm_entry.pack()
wm_button = tk.Button(window, text="Add watermark", command=add_watermark)
wm_button.pack()


window.mainloop()
