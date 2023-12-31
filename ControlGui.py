import aiohttp
import asyncio
import tkinter as tk
from tkinter import font
from tkinter import *
from PIL import ImageTk, Image


#TEST VARIABLES
class TkinterGui:
    def __init__(self):
        #WINDOW
        self.window = tk.Tk()
        self.window.title('Brum Brum GUI')
        self.window.geometry('1200x700')

        """
        for i in font.families():
            self.el = Label(self.window, text = i, font = (i, 15))
            self.el.pack()
        """

        #SETTINGS
        #self.settings_frame = Frame(self.window, highlightbackground = "black", highlightthickness = 2)
        #self.settings_frame.place(relx = 0.9, rely = 0.9, relwidth = 0.2, relheight = 0.2, anchor = tk.SW)
        #self.settings_button = Button(self.settings_frame, text = '=', highlightbackground = "black", highlightthickness = 2)
        #self.settings_button.place(relx = 0.9, rely = 0.9, relwidth = 0.2, relheight = 0.2, anchor = tk.NE)

        #MAIN FRAME
        self.main_frame = Frame(self.window)
        self.main_frame.place(relx = 0.1, rely = 0.1, relwidth = 0.8, relheight = 0.8)

        #LEFT FRAME
        self.left_frame = Frame(self.main_frame)
        self.left_frame.place(relwidth = 0.3, relheight = 1, anchor = tk.NW)

        #BLANK FRAME
        self.blank_frame = Frame(self.left_frame)
        self.blank_frame.place(relx = 1, relwidth = 0.5, relheight = 1, anchor = tk.NE)

        #CONTROL FRAME
        self.control_frame = Frame(self.left_frame, background = '#16161d', highlightbackground = '#36454F', highlightthickness = 6, padx=10)
        self.control_frame.place(relwidth = 0.5, relheight = 1, anchor = tk.NW)
        #KEY
        self.key_icon = Image.open("Icons/key.png")
        self.keycv = tk.Canvas(self.control_frame, background = '#16161d', highlightthickness = 0)
        self.keycv.place(rely = 0.025, relwidth = 1, relheight = 0.2, anchor = tk.NW)
        #LOCK
        self.lock_icon = Image.open("Icons/lock.png")
        self.lockcv = tk.Canvas(self.control_frame, background = '#16161d', highlightthickness = 0)
        self.lockcv.place(rely = 0.275, relwidth = 1, relheight = 0.2, anchor = tk.NW)
        #SEC
        self.sec_icon = Image.open("Icons/sec.png")
        self.seccv = tk.Canvas(self.control_frame, background = '#16161d', highlightthickness = 0)
        self.seccv.place(rely = 0.525, relwidth = 1, relheight = 0.2, anchor = tk.NW)
        #ABS
        self.abs_icon = Image.open("Icons/abs.png")
        self.abscv = tk.Canvas(self.control_frame, background = '#16161d', highlightthickness = 0)
        self.abscv.place(rely = 0.775, relwidth = 1, relheight = 0.2, anchor = tk.NW)

        self.abscv.bind('<Configure>', lambda e : self.stretch_image(e)) #sus solution

        #RIGHT FRAME
        self.right_frame = Frame(self.main_frame)
        self.right_frame.place(relx = 1, relwidth = 0.7, relheight = 1, anchor = tk.NE)

        #RADIO FRAME
        self.radio_frame = Frame(self.right_frame, highlightbackground = '#36454F', highlightthickness = 6)
        self.radio_frame.place(relwidth = 1, relheight = 0.1, anchor = tk.NW)

        self.station = Label(self.radio_frame, text = '-----------', bg = '#16161d', fg = 'white', font = ('Small Fonts', 20))
        self.prev_st = Button(self.radio_frame, text = '<', bg = '#36454F', fg = 'white', font = ('System', 20))
        self.next_st = Button(self.radio_frame, text = '>', bg = '#36454F', fg = 'white', font = ('System', 20))
  
        self.station.place(relx = 0.2, relwidth = 0.6, relheight = 1, anchor = tk.NW)
        self.prev_st.place(relwidth = 0.2, relheight = 1, anchor = tk.NW)
        self.next_st.place(relx = 0.8, relwidth = 0.2, relheight = 1, anchor = tk.NW)
        
        #BLANK FRAME
        self.blank_frame_1 = Frame(self.right_frame)
        self.blank_frame_1.place(rely = 0.1, relwidth = 1, relheight = 0.1, anchor = tk.NW)

        #DMS FRAME
        self.dms_bg = '#16161d'

        self.dms_frame = Frame(self.right_frame, bg = self.dms_bg, highlightbackground = "#36454F", highlightthickness = 6)
        self.dms_frame.place(rely = 0.2, relwidth = 0.45, relheight = 0.8, anchor = tk.NW)

        self.state_frame = [0 for i in range(10)]

        self.state = [0 for i in range(10)]

        for i in range(10):
            self.state_frame[i] = Frame(self.dms_frame, bg = self.dms_bg, highlightbackground = "#36454F", highlightthickness = 2)
            self.state_frame[i].place(relx = 0, rely = 0.1 * i, relwidth = 1, relheight = 0.1, anchor = tk.NW)

            self.state[i] = Label(self.state_frame[i], text = 'Pilot State', bg = self.dms_bg, fg = '#2b2b30', font = ('Small Fonts', 14))

            self.state[i].place(relx = 0.3, rely = 0, relwidth = 0.5, relheight = 1, anchor = tk.NW)

        #WEATHER FRAME
        self.weather_bg = '#4848ff'
        self.weather_frame = Frame(self.right_frame, background = self.weather_bg, highlightbackground = "#36454F", highlightthickness = 6)
        self.weather_frame.place(relx = 0.55, rely = 0.2, relwidth = 0.45, relheight = 0.8, anchor = tk.NW)

        self.current_weather_frame = Frame(self.weather_frame, bg = self.weather_bg, highlightbackground = "#36454F", highlightthickness = 3, padx = 5, pady = 5)
        self.current_weather_frame.place(relx = 0, rely = 0, relwidth = 1, relheight = 0.3, anchor = tk.NW)

        self.current_city = Label(self.current_weather_frame, text = 'Placeholder', bg = self.weather_bg, fg = 'white', font = ('Small Fonts', 20))
        self.current_time = Label(self.current_weather_frame, text = '00:00', bg = self.weather_bg, fg = 'white', font = ('Small Fonts', 20))
        self.current_weather = Label(self.current_weather_frame, text = '--------', bg = self.weather_bg, fg = 'white', font = ('Small Fonts', 20))
        self.current_temperature = Label(self.current_weather_frame, text = '----', bg = self.weather_bg, fg = 'white', font = ('Small Fonts', 20))

        self.current_city.place(relx = 0, rely = 0, relwidth = 0.5, relheight = 0.5, anchor = tk.NW)
        self.current_time.place(relx = 0.5, rely = 0, relwidth = 0.5, relheight = 0.5, anchor = tk.NW)
        self.current_weather.place(relx = 0.3, rely = 0.5, relwidth = 0.5, relheight = 0.5, anchor = tk.NW)
        self.current_temperature.place(relx = 0.8, rely = 0.5, relwidth = 0.2, relheight = 0.5, anchor = tk.NW)

        self.forecast_frame = [0 for i in range(7)]

        self.time = [0 for i in range(7)]
        self.weather = [0 for i in range(7)]
        self.temperature = [0 for i in range(7)]

        for i in range(7):
            self.forecast_frame[i] = Frame(self.weather_frame, bg = self.weather_bg, highlightbackground = "#36454F", highlightthickness = 2)
            self.forecast_frame[i].place(relx = 0, rely = 0.3 + 0.1 * i, relwidth = 1, relheight = 0.1, anchor = tk.NW)

            self.time[i] = Label(self.forecast_frame[i], text = '00:00', bg = self.weather_bg, fg = 'white', font = ('Small Fonts', 14))
            self.weather[i] = Label(self.forecast_frame[i], text = '--------', bg = self.weather_bg, fg = 'white', font = ('Small Fonts', 14))
            self.temperature[i] = Label(self.forecast_frame[i], text = '----', bg = self.weather_bg, fg = 'white', font = ('Small Fonts', 14))

            self.time[i].place(relx = 0, rely = 0, relwidth = 0.2, relheight = 1, anchor = tk.NW)
            self.weather[i].place(relx = 0.4, rely = 0, relwidth = 0.4, relheight = 1, anchor = tk.NW)
            self.temperature[i].place(relx = 0.8, rely = 0, relwidth = 0.2, relheight = 1, anchor = tk.NW)

    def stretch_image(self, event):
        #WINDOW SIZE 
        width = event.width
        height = event.height
        
        #RESIZED IMAGES
        global tk_key
        global tk_lock
        global tk_sec
        global tk_abs

        #RESIZE
        resized_image = self.key_icon.resize((width, height))
        tk_key = ImageTk.PhotoImage(resized_image)

        resized_image = self.lock_icon.resize((width, height))
        tk_lock = ImageTk.PhotoImage(resized_image)

        resized_image = self.sec_icon.resize((width, height))
        tk_sec = ImageTk.PhotoImage(resized_image)

        resized_image = self.abs_icon.resize((width, height))
        tk_abs = ImageTk.PhotoImage(resized_image)

        #PLACE ON CANVAS
        self.keycv.create_image(0, 0, image = tk_key, anchor = tk.NW)
        self.lockcv.create_image(0, 0, image = tk_lock, anchor = tk.NW)
        self.seccv.create_image(0, 0, image = tk_sec, anchor = tk.NW)
        self.abscv.create_image(0, 0, image = tk_abs, anchor = tk.NW)


    def start_main_loop(self):
        self.window.mainloop()

        

class InfotainmentSystem:
    def __init__(self, gui, st):
        #STATION SETTINGS
        self._stations = ['Radio Station 1', 'Radio Station 2', 'Radio Station 3', 'Radio Station 4', 'Radio Station 5', 'Radio Station 6', 'Radio Station 7']
        self._sindex = st
        
        #GUI CONFIGURATION
        self._gui = gui
        self._gui.station.config(text = self._stations[self._sindex])
        self._gui.next_st.config(command = lambda : asyncio.run(self.next_station()))
        self._gui.prev_st.config(command = lambda : asyncio.run(self.previous_station()))

    def get_current_station(self):
        current_station = self._stations[self._sindex]
        return current_station
    
    async def change_station(self):
        async with aiohttp.ClientSession() as session:

            payload = {'station': self.get_current_station()}

            async with session.post(url = 'http://localhost:8080/radio-change/', data = payload) as response:

                print("Status:", response.status)
                print("Content-type:", response.headers['content-type'])

                html = await response.text()
                print("Body:", html[:100])

                self._gui.station.config(text = self.get_current_station())

    async def next_station(self):
        if(self._sindex == len(self._stations) - 1):
            self._sindex = 0
        else:
            self._sindex += 1

        await self.change_station()

    async def previous_station(self):
        if(self._sindex == 0):
            self._sindex = len(self._stations) - 1
        else:
            self._sindex -= 1

        await self.change_station()

class WeatherInformation:
    def __init__(self, gui):
        #GUI CONFIGURATION
        self._gui = gui
        self._gui.current_city.config(text = 'Parma')
        self._gui.current_time.config(text = '10:00')
        self._gui.current_weather.config(text = 'Sunny')
        self._gui.current_temperature.config(text = '20 °C')
        

    async def get_current_weather(self):
        """ DA CAMBIARE UN PO'
        async with aiohttp.ClientSession() as session:

            async with session.get(url = 'http://localhost:8080//vehicle-status/current-weather') as response:

                print("Status:", response.status)
                print("Content-type:", response.headers['content-type'])

                html = await response.text()
                print("Body:", html[:100])

                self._gui.station.config(text = self.get_current_station())
        """
        current_city = 'Parma'
        current_time = '10:00'
        current_weather = 'Sunny'
        current_temperature = '20 °C'

        self._gui.current_city.config(text = current_city)
        self._gui.current_time.config(text = current_time)
        self._gui.current_weather.config(text = current_weather)
        self._gui.current_temperature.config(text = current_temperature)

        if(current_weather == ''):
            # display icon
            img = ''

        elif(current_weather == ''):
            # display icon
            img = ''

        else:
            # display default icon
            img = ''

    def get_forecast_weather(self):
        # pain
        # ciclo for vvv
        time = '10:00'
        weather = 'Sunny'
        temperature = '20 °C'
        
        for i in range(7):
            self._gui.time[i].config(text = time)
            self._gui.weather[i].config(text = weather)
            self._gui.temperature[i].config(text = temperature)

#MAIN
gui = TkinterGui()
radio = InfotainmentSystem(gui, 0)
meteo = WeatherInformation(gui)
meteo.get_forecast_weather()
gui.start_main_loop()




"""
async def main():

    async with aiohttp.ClientSession() as session:

        payload = {'station': 'RTL'}

        async with session.post(url = 'http://localhost:8080/radio-change/', data = payload) as response:

            print("Status:", response.status)
            print("Content-type:", response.headers['content-type'])

            html = await response.text()
            print("Body:", html[:100])
        
        async with session.get('http://localhost:8080/radio') as response:

            print("Status:", response.status)
            print("Content-type:", response.headers['content-type'])

            html = await response.text()
            print("Body:", html[:100])

asyncio.run(main())
"""