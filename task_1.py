import requests
import tkinter
from tkinter import scrolledtext, messagebox

def get_weather():
    city_name = entry.get()
    api_key = "b8af6b706ec6dc2d422287dd1f2899b5"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric&lang=ru"
    response = requests.get(url, timeout = 10)
    data = response.json()

    if response.status_code == 200:
        city = data['name']
        country = data['sys']['country']
        temp = data['main']['temp']
        description = data['weather'][0]['description']

        txt.delete(1.0, tkinter.END)
        txt.insert(tkinter.END, f"Погода в городе {city}, {country}:\n")
        txt.insert(tkinter.END, f"Температура: {temp}°C\n")
        txt.insert(tkinter.END, f"Описание: {description}\n")
    elif response.status_code == 404:
        print(f"Ошибка: Город '{city_name}' не найден!")
    else:
        print("Неизвестная ошибка!")

root = tkinter.Tk()
root.title("Погода")

main_frame = tkinter.Frame(root)
main_frame.pack()

tkinter.Label(main_frame, text = "Введите город:").pack(anchor = 'w')
entry = tkinter.Entry(main_frame)
entry.pack(anchor = 'w')

tkinter.Button(main_frame, text="Узнать погоду", command = get_weather).pack(anchor='w', pady = 8)

txt = scrolledtext.ScrolledText(main_frame)
txt.pack(anchor = 'w')

root.mainloop()