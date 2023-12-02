import aiohttp
import asyncio
import tkinter as tk
from tkinter import ttk, font
from time import sleep

#TEST VARIABLES
class TkinterGui:
    def __init__(self):
        #WINDOW
        self.window = tk.Tk()
        self.window.title('Brum Brum GUI')
        self.window.geometry('1200x700')

        """for i in font.families():
            self.el = ttk.Label(self.window, text = i, font = (i, 15))
            self.el.pack()"""
 

        #RADIO FRAME
        self.radio_frame = ttk.Frame(self.window, borderwidth = 10, relief="solid")
        self.radio_frame.place(relx = 0.9, rely = 0.1, relwidth = 0.4, relheight = 0.8, anchor = tk.NE)
        self.station = ttk.Label(self.radio_frame, text = '-----------', width = 80, background = 'black', foreground = 'white', font = ('Small Fonts', 20) )
        self.next_st = ttk.Button(self.radio_frame, text = '>')
        self.prev_st = ttk.Button(self.radio_frame, text = '<')
        self.station.pack()
        self.next_st.pack(side=tk.RIGHT)
        self.prev_st.pack(side=tk.LEFT)

    def start_main_loop(self):
        self.window.mainloop()

        

class InfotainmentSystem:
    def __init__(self, gui, st):
        #STATION SETTINGS
        self._stations = ['station 1', 'station 2', 'station 3', 'station 4']
        self._sindex = st

        #GUI CONFIGURATION
        self._gui = gui
        self._gui.station.config(text = self._stations[self._sindex])
        self._gui.next_st.config(command = self.next_station)
        self._gui.prev_st.config(command = self.previous_station)

    def get_current_station(self):
        current_station = self._stations[self._sindex]
        return current_station
    
    def next_station(self):
        #ADD IF INDEX <= _STATIONS.LENGHT
        self._sindex += 1
        current_station = self.get_current_station()
        self._gui.station.config(text = current_station)
        #ADD CLIENT REQUEST TO RADIOHANDLER

    def previous_station(self):
        #ADD IF INDEX >= 0
        self._sindex -= 1
        current_station = self.get_current_station()
        self._gui.station.config(text = current_station)
        #ADD CLIENT REQUEST TO RADIOHANDLER


#MAIN
gui = TkinterGui()
radio = InfotainmentSystem(gui, 0)
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