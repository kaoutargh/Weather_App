from tkinter import *
from tkinter import messagebox
import requests
from datetime import datetime
from timezonefinder import TimezoneFinder
from geopy.geocoders import Nominatim
import pytz

url = 'https://api.openweathermap.org/data/2.5/weather?q={}&APPID=babe22546bb93eaad031776826f2adc4'


api_key ='abe22546bb93eaad031776826f2adc4'

def get_weather(city):
    result = requests.get(url.format(city,api_key))
    if result:
        json = result.json()
     #(City, Country, temp_celsiws, temp_fatrenheit, icon, weather)
        city = json['name']
        country = json['sys']['country']
        temp_kelvin = json['main']['temp']
        temp_celsius = temp_kelvin - 273.15
        temp_fahrenheit = (temp_kelvin - 273.15) * 9 / 5 + 32
        icon = json['weather'][0]['icon']
        weather = json['weather'][0] ['main']
        final = (city, country, temp_celsius, temp_fahrenheit, icon, weather)

        geolocator= Nominatim(user_agent="geoapiExercises")
        location= geolocator.geocode(city)
        obj = TimezoneFinder()
        result = obj.timezone_at(lng=location. longitude, lat=location.latitude)
        home=pytz.timezone(result)
        local_time=datetime.now(home)
        current_time=local_time.strftime("%I:%M %p")
        clock.config(text=current_time)
        #name. config(text="")


        return final
    else:
        return None







def search():
    city =city_text.get()
    weather = get_weather(city)
    img["file"] = 'C:/Users/kawta/Desktop/Projectstopractice/.venv/Weather_App/weather_icons/{}.png'.format(weather[4])
    if weather:
        location_lbl['text'] = '{}, {}'.format(weather[0], weather[1])
        #image['bitmap'] = 'weather_icons/{}.png'.format(weather[3])
        temp_lbl['text'] = '{:.2f}°C, {:.2f}°F'.format(weather[2],weather[3])
        weather_lbl['text'] = weather[5]
    else:
        messagebox.showerror('error', 'Cannot find the city'.format(city))



app=Tk()
app.title("Weather App")
app.geometry("700x350")


city_text = StringVar()
city_entry = Entry(app, textvariable=city_text)
city_entry.pack()

search_btn = Button(app, text='Search weather', width=12, command=search)
search_btn.pack()

location_lbl = Label(app, text='', font=('bold',20))
location_lbl.pack()

img = PhotoImage(file="")
image = Label(app, image=img)
image.pack()

temp_lbl = Label(app, text='')
temp_lbl.pack()

#logo
Logo_image=PhotoImage(file="C:/Users/kawta/Downloads/weather_icons/logo.png")
logo=Label(image=Logo_image)
logo.place(x=10,y=10)

#time
#name=Label(app,font=("arial",15,"bold"))
#name.place(x=500,y=300)
clock=Label(app, font=("Helvetica", 10))
clock.place(x=322,y=145)

weather_lbl = Label(app, text='')
weather_lbl.pack()

app.mainloop()