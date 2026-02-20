import tkinter
from tkinter import messagebox
import requests
from PIL import Image, ImageTk
from io import BytesIO

cat_api = "live_C2x59wtDabv5S7ZVomxUS7G4XHTUxkolRdboDYrWgI0Ytkq9eUtPeeXxjDFGKkfD"

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

def get_cat():
    try:
        headers = {"x-api-key": cat_api}
        url = "https://api.thecatapi.com/v1/images/search?size=med&mime_types=jpg&format=json&has_breeds=true&order=RANDOM&limit=1"
        response = requests.get(url, headers = headers, timeout = 5)
        data = response.json()

        if data and len(data) > 0:
            img_url = data[0]['url']
            img_data = requests.get(img_url, timeout = 5).content
            photo = ImageTk.PhotoImage(Image.open(BytesIO(img_data)))
            lbl.config(image=photo)
            lbl.image = photo
        else:
            messagebox.showerror("Ошибка", "Не удалось получить данные о коте")
    except requests.exceptions.Timeout:
        messagebox.showerror("Ошибка", "Превышено время ожидания ответа (кот)")
    except Exception as e:
        messagebox.showerror("Ошибка", f"Не удалось загрузить кота: {e}")

root = tkinter.Tk()
root.title("Собаки и кошки")

button_frame = tkinter.Frame(root)
button_frame.pack(pady = 10)

tkinter.Button(button_frame, text = "Показать собаку", command = get_dog).pack(side = 'left', padx = 5)
tkinter.Button(button_frame, text = "Показать кота", command = get_cat).pack(side = 'left', padx = 5)

lbl = tkinter.Label(root)
lbl.pack()

get_dog()
root.mainloop()