from tkinter import*
from PIL import ImageTk,Image
import requests

url = 'http://api.openweathermap.org/data/2.5/weather'
api_key = 'e3351bc99fe803efbc461384c40650ac'
iconUrl = 'http://openweathermap.org/img/wn/{}@2x.png'

def getWeather(city):
    params = {'q':city, 'appid':api_key, 'lang':'tr'}
    data = requests.get(url, params=params).json()
    if data:
        city = data['name'].capitalize()
        country = data['sys']['country']
        temp = int(data['main']['temp'] - 273.15)
        icon = data['weather'][0]['icon']
        condition = data['weather'][0]['description']
        return(city,country,temp,icon,condition)

def main():
    city = cityEntry.get()
    weather = getWeather(city)
    if weather:
        locationLabel['text'] = '{},{}'.format(weather[0],weather[1])
        tempLabel['text'] = '{}°C'.format(weather[2])
        conditionLabel['text'] = weather[4]
        icon = ImageTk.PhotoImage(Image.open(requests.get(iconUrl.format(weather[3]), stream = True).raw))
        iconLabel.configure(image=icon)
        iconLabel.image = icon


app = Tk()
app.geometry('450x450')
app.title('HAVA DURUMU')
app.configure(background="light blue")

cityEntry = Entry(app,justify='center', font=('Arial', 20), fg="light pink")
cityEntry.pack(fill=BOTH,ipady=10,padx=20,pady=5)
cityEntry.focus()

searchButton = Button(app,text='ARAMA', font=('Arial', 20,'bold'), fg="violet", bg="lavender", command=main)
searchButton.pack(fill=BOTH,ipady=10,padx=20)

iconLabel = Label(app) #ikon
iconLabel.pack()
iconLabel.configure(background="light blue")

locationLabel = Label(app,font=('Arial', 40), fg="light yellow")   #şehir adı
locationLabel.pack()
locationLabel.configure(background="light blue")

tempLabel = Label(app,font=('Arial', 50,'bold'), fg="light yellow")  #derecesi
tempLabel.pack()
tempLabel.configure(background="light blue")

conditionLabel = Label(app,font=('Arial',30), fg="light yellow")   #açık, kapalı, bulutlu vb.
conditionLabel.pack()
conditionLabel.configure(background="light blue")

app.mainloop()
