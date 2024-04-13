import tkinter as tk
from tkinter import filedialog
from tkinter import *
import numpy as np
from PIL import ImageTk, Image
import cv2
import os
from tensorflow.keras.models import load_model

model = load_model('my_model.h5')

classes = {0: 'Honda', 1: 'Mercedes', 2: 'Suzuki', 3: 'Vinfast'}


def classify(file_path):
    if (e1.get() != ""):
        file_path = e1.get()

    global label_packed
    image = Image.open(file_path)
    image = image.resize((30, 30))
    image = np.expand_dims(image, axis=0)
    image = np.array(image)
    pred = np.argmax(model.predict([image])[0], axis=-1)
    brand = classes[pred]
    print(brand)
    label.configure(foreground='#011638', text=brand)

    img = cv2.imread(file_path)
    img = cv2.putText(img, brand, (10, 30), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255),3)
    img_path, img_name = os.path.split(file_path)
    cv2.imwrite(os.path.join(r".\KetQua", img_name + ".jpg"), img)

def show_classify_button(file_path):
    classify_b = Button(top, text="Nhận diện", command=lambda: classify(file_path), padx=10, pady=5)
    classify_b.configure(background='#364156', foreground='white', font=('Time', 10, 'bold'))
    classify_b.place(x=50, y=200)

def upload_image():
    try:
        file_path = filedialog.askopenfilename(initialdir=r".\Test")
        uploaded = Image.open(file_path)
        uploaded.thumbnail(((top.winfo_width() / 2), (top.winfo_height() / 2)))
        im = ImageTk.PhotoImage(uploaded)

        logo_image.configure(image=im)
        logo_image.image = im
        label.configure(text='')
        show_classify_button(file_path)
    except:
        pass

def btnKQ_Click():
    file_path = filedialog.askopenfilename(initialdir=r".\KetQua")
    uploaded = Image.open(file_path)
    uploaded.thumbnail(((top.winfo_width() / 2.25), (top.winfo_height() / 2.25)))
    im = ImageTk.PhotoImage(uploaded)

    logo_image.configure(image=im)
    logo_image.image = im
    label.configure(text='')


# Tạo giao diện
top = tk.Tk()
top.geometry('800x400')
top.title('Nhận diện logo oto')
top.configure(background='#CDCDCD')

label = Label(top, background='#CDCDCD', font=('Time', 15, 'bold'))
logo_image = Label(top)


Link = Label(top, text = "File: ").place(x = 50, y = 50)
e1 = Entry(top)
e1.place(x=80, y=50)

show_classify_button(file_path="")

result_b = Button(top, text="  Kết quả  ", command=btnKQ_Click, padx=10, pady=5)
result_b.configure(background='#364156', foreground='white', font=('Time', 10, 'bold'))
result_b.place(x=50, y=300)

upload = Button(top, text="Tải ảnh lên", command=upload_image, padx=10, pady=5)
upload.configure(background='#364156', foreground='white', font=('Time', 10, 'bold'))
upload.place(x=50, y=100)

logo_image.pack(side=BOTTOM, expand=True)
label.pack(side=BOTTOM, expand=True)
heading = Label(top, text="Nhận diện Logo Oto", pady=20, font=('Time', 20, 'bold'))

heading.configure(background='#CDCDCD', foreground='#364170')
heading.pack()
top.mainloop()
