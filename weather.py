
import tkinter as tk
import requests
from tkinter import messagebox
from PIL import Image, ImageTk
import ttkbootstrap


#function for getting the weather info from OpenWeatherMap
def get_weather(city):
    Key="use your key here"
    urlowm=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={Key}"
    res = requests.get(urlowm)

    if res.status_code == 404:
        messagebox.showerror("Error", "City not found")
        return None

    #parsing the response to JSON to get weather info
    weather = res.json()
    icon_id = weather['weather'][0]['icon']
    temperature = weather['main']['temp'] - 273.15
    description = weather['weather'][0]['description']
    city = weather['name']
    country = weather['sys']['country']

    # get icon url
    icon_url = f"http://openweathermap.org/img/wn/{icon_id}@2x.png"
    return (icon_url, temperature, description, city, country)


#function for searching the city
def search():
    city = cityn.get()
    result = get_weather(city)
    if result is None:
        return
    #if the city is found, unpack info
    icon_url, temperature, description, city, country = result
    loc_label.configure(text=f"{city}, {country}")

    #get the icon image
    image =Image.open(requests.get(icon_url, stream=True).raw)
    icon = ImageTk.PhotoImage(image)
    icon_label.configure(image=icon)
    icon_label.image = icon

    #update temp and descr labels
    temp_label.configure(text=f"Temperature: {temperature:.2f}C")
    discr_label.configure(text=f"description: {description}")

root = ttkbootstrap.Window(themename="morph")
root.title("Weather forecast")
root.geometry("400x400")

#entering city name
cityn = ttkbootstrap.Entry(root, font="Helvetica, 18")
cityn.pack(pady=10)

#button 
searchb = ttkbootstrap.Button(root, text="Search", command=search,bootstyle="warning")
searchb.pack(pady=10)

#label for city name
loc_label = tk.Label(root, font="Helvetica, 25")
loc_label.pack(pady=20)

#label for weather
icon_label = tk.Label(root)
icon_label.pack()

#lable for temperature 
temp_label = tk.Label(root, font="helvetiva, 20")
temp_label.pack()

#lable for discription
discr_label = tk.Label(root, font="helvetiva, 20")
discr_label.pack()
