import tkinter
from tkinter import *
import requests

def value(city):
    api_address = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=2d51146760a767933e3f6cc244601853'.format(city)
    key = requests.get(api_address)
    data = key.json()
    print(key)
    try:
        temp = data['main']['temp']
        temp1 = data['main']['temp_min']
        temp2 = data['main']['temp_max']
        pressure = data['main']['pressure']
        wind_speed = data['wind']['speed']
        lat = data['main']['humidity']
        long = data['coord']['lon']
        desc = data['weather'][0]['description']
        weather = data['weather'][0]['main']
        clouds = data['clouds']['all']
        rain = data['weather'][0]['main']


        lb21 = Label(frame1, text="Temperature:                   ", font=("arial", 20, "bold"),bg="light goldenrod")
        lb21.place(x=670, y=370, anchor="center")

        lb22 = Label(frame1, text=data['main']['temp'], font=("arial", 20, "bold"), bg="light goldenrod")
        lb22.place(x=770, y=370, anchor="center")

        lb23 = Label(frame1, text="Wind Speed:                   ", font=("arial", 20, "bold"), bg="light goldenrod")
        lb23.place(x=670, y=690, anchor="center")

        lb24 = Label(frame1, text=data['wind']['speed'], font=("arial", 20, "bold"), bg="light goldenrod")
        lb24.place(x=770, y=690, anchor="center")

        lb25 = Label(frame1, text="Humidity:                   ", font=("arial", 20, "bold"), bg="light goldenrod")
        lb25.place(x=670, y=490, anchor="center")

        lb26 = Label(frame1, text=data['main']['humidity'], font=("arial", 20, "bold"), bg="light goldenrod")
        lb26.place(x=770, y=490, anchor="center")

        lb27 = Label(frame1, text="Condition:                   ", font=("arial", 20, "bold"), bg="light goldenrod")
        lb27.place(x=670, y=530, anchor="center")

        lb28 = Label(frame1, text=data['weather'][0]['main'], font=("arial", 20, "bold"), bg="light goldenrod")
        lb28.place(x=770, y=530, anchor="center")

        lb29 = Label(frame1, text="Description:                   ", font=("arial", 20, "bold"), bg="light goldenrod")
        lb29.place(x=670, y=570, anchor="center")

        lb30 = Label(frame1, text=data['weather'][0]['description'], font=("arial", 20, "bold"), bg="light goldenrod")
        lb30.place(x=770, y=570, anchor="center")

        lb31 = Label(frame1, text="Pressure:                   ", font=("arial", 20, "bold"), bg="light goldenrod")
        lb31.place(x=670, y=610, anchor="center")

        lb32 = Label(frame1, text= data['main']['pressure'], font=("arial", 20, "bold"), bg="light goldenrod")
        lb32.place(x=770, y=610, anchor="center")

        lb33 = Label(frame1, text="Clouds:                   ", font=("arial", 20, "bold"), bg="light goldenrod")
        lb33.place(x=670, y=650, anchor="center")

        lb34 = Label(frame1, text=data['clouds']['all'], font=("arial", 20, "bold"), bg="light goldenrod")
        lb34.place(x=770, y=650, anchor="center")

        lb35 = Label(frame1, text="Minimum Temp:                   ", font=("arial", 20, "bold"), bg="light goldenrod")
        lb35.place(x=670, y=410, anchor="center")

        lb36 = Label(frame1, text=data['main']['temp_min'], font=("arial", 20, "bold"), bg="light goldenrod")
        lb36.place(x=770, y=410, anchor="center")

        lb37 = Label(frame1, text="Maximum Temp:                   ", font=("arial", 20, "bold"), bg="light goldenrod")
        lb37.place(x=670, y=450, anchor="center")

        lb38 = Label(frame1, text=data['main']['temp_max'], font=("arial", 20, "bold"), bg="light goldenrod")
        lb38.place(x=770, y=450, anchor="center")


    except:
        lbllll = Label(frame1, text = "Invalid City!", font=("arial", 40, "bold"), bg = "light goldenrod")
        lbllll.place(x=525, y=365)
        btnn = Button(frame1, text = "Ok", bd= 10, padx = 100, pady = 10, font = ("arial", 15, "bold"), width = 1, height = 2, bg = "grey", command = lbllll.destroy)
        btnn.place(x = 550, y = 500)

tk = tkinter.Tk()

tk.title("Weather API")
frame1 = Frame(tk, width = 5000, height = 900, bg = "light goldenrod")
frame1.grid(row = 0, column = 0)

lbl1 = Label(frame1, text = "Check Weather", font = ("arial", 40, "bold"), bg = "light goldenrod")
lbl1.place(x=665, y=45, anchor="center")

lbl1 = Label(frame1, text = "City:  ", font = ("arial", 20, "bold"), bg = "light goldenrod")
lbl1.place(x=490, y=155, anchor="center")

entry1 = Entry(frame1, textvariable =input, font = ("arial", 20, "bold"), bd = 10, insertwidth = 5 , bg = "bisque2")
entry1.place(x=556, y=125)

btn1 = Button(frame1, text = "Show Weather", bd= 10, padx = 200, pady = 10, font = ("arial", 15, "bold"), width = 1, height = 2, bg = "grey" ,command=lambda: value(entry1.get()))
btn1.place(x = 460, y = 210)

tk.mainloop()
