import tkinter
from tkinter import messagebox
import requests
from PIL import Image, ImageTk
from io import BytesIO

def get_dog():
    try:
        response = requests.get("https://dog.ceo/api/breeds/image/random").json()
        image = requests.get(response["message"], timeout = 5).content
        photo = ImageTk.PhotoImage(Image.open(BytesIO(image)))
        lbl.config(image = photo)
        lbl.image = photo
    except requests.exceptions.Timeout:
        messagebox.showerror("Ошибка", "Превышено время ожидания ответа")
    except Exception as e:
        messagebox.showerror("Ошибка", f"Не удалось загрузить картинку: {e}")

root = tkinter.Tk()
root.title("Собаки")
tkinter.Button(root, text = "Получить собаку", command = get_dog).pack(pady = 5)
lbl = tkinter.Label(root)
lbl.pack()

get_dog()
root.mainloop()