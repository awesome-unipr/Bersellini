import aiohttp
import asyncio
import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image


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


        #MAIN FRAME
        self.main_frame = Frame(self.window, highlightbackground = "black", highlightthickness = 2)
        self.main_frame.place(relx = 0.1, rely = 0.1, relwidth = 0.8, relheight = 0.8)

        #LEFT FRAME
        self.left_frame = Frame(self.main_frame, highlightbackground = "red", highlightthickness = 2)
        self.left_frame.place(relwidth = 0.3, relheight = 1, anchor = tk.NW)

        #BLANK FRAME
        self.blank_frame = Frame(self.left_frame, highlightbackground = "green", highlightthickness = 2)
        self.blank_frame.place(relx = 1, relwidth = 0.5, relheight = 1, anchor = tk.NE)

        #CONTROL FRAME
        self.control_frame = Frame(self.left_frame, highlightbackground = "green", highlightthickness = 2, padx=10, background = '#23281e')
        self.control_frame.place(relwidth = 0.5, relheight = 1, anchor = tk.NW)
        
        #KEY
        self.key_icon = Image.open("../Icons/key.png")
        self.keycv = tk.Canvas(self.control_frame, background = '#23281e', highlightthickness = 0)
        self.keycv.place(rely = 0.025, relwidth = 1, relheight = 0.2, anchor = tk.NW)

        #LOCK
        self.lock_icon = Image.open("../Icons/lock.png")
        self.lockcv = tk.Canvas(self.control_frame, background = '#23281e', highlightthickness = 0)
        self.lockcv.place(rely = 0.275, relwidth = 1, relheight = 0.2, anchor = tk.NW)

        #SEC
        self.sec_icon = Image.open("../Icons/sec.png")
        self.seccv = tk.Canvas(self.control_frame, background = '#23281e', highlightthickness = 0)
        self.seccv.place(rely = 0.525, relwidth = 1, relheight = 0.2, anchor = tk.NW)

        #ABS
        self.abs_icon = Image.open("../Icons/abs.png")
        self.abscv = tk.Canvas(self.control_frame, background = '#23281e', highlightthickness = 0)
        self.abscv.place(rely = 0.775, relwidth = 1, relheight = 0.2, anchor = tk.NW)

        self.abscv.bind('<Configure>', lambda e : self.stretch_image(e)) #sus solution

        #RIGHT FRAME
        self.right_frame = Frame(self.main_frame, highlightbackground = "yellow", highlightthickness = 2)
        self.right_frame.place(relx = 1, relwidth = 0.7, relheight = 1, anchor = tk.NE)

        #RADIO FRAME
        self.radio_frame = Frame(self.right_frame, highlightbackground = "blue", highlightthickness = 1)
        self.radio_frame.place(relwidth = 1, relheight = 0.1, anchor = tk.NW)

        self.station = Label(self.radio_frame, text = '-----------', width =20, background = '#23281e', foreground = 'white', font = ('Small Fonts', 20))
        self.prev_st = Button(self.radio_frame, text = '<')
        self.next_st = Button(self.radio_frame, text = '>')
  
        self.station.place(relx = 0.2, relwidth = 0.6, relheight = 1, anchor = tk.NW)
        self.prev_st.place(relwidth = 0.2, relheight = 1, anchor = tk.NW)
        self.next_st.place(relx = 0.8, relwidth = 0.2, relheight = 1, anchor = tk.NW)
        
        #BLANK FRAME
        self.blank_frame_1 = Frame(self.right_frame, highlightbackground = "green", highlightthickness = 2)
        self.blank_frame_1.place(rely = 0.1, relwidth = 1, relheight = 0.1, anchor = tk.NW)

        #DMS FRAME
        self.dms_frame = Frame(self.right_frame, highlightbackground = "blue", highlightthickness = 1)
        self.dms_frame.place(rely = 0.2, relwidth = 0.45, relheight = 0.8, anchor = tk.NW)

        #WEATHER FRAME
        self.weather_frame = Frame(self.right_frame, highlightbackground = "blue", highlightthickness = 1)
        self.weather_frame.place(relx = 0.55, rely = 0.2, relwidth = 0.45, relheight = 0.8, anchor = tk.NW)

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