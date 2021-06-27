from ctypes import string_at

import time
import tkinter as Tk
from tkinter import Label, StringVar, ttk,Entry
from tkinter.constants import COMMAND
from matplotlib import pyplot as plt
from matplotlib import animation
import serial
import serial.tools.list_ports
import tab_creator.creatTab as creatTab
from tkinter import messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import math
import numpy as np
import matplotlib.animation as animation
class Application():
    def __init__(self, parent):
        self.parent = parent
        self.frames()
        self.port_names = []
        self.serial_avr = None
        self.status_serial = False
        self.init_serial()
        
    def scan_serial_port(self):
        port_name = []
        ports = list(serial.tools.list_ports.comports())
        for index in range(len(ports)):
            port_name.append(ports[index][1])
        return port_name

    def scan_ports(self):
        self.port_names = self.scan_serial_port()
        print("kieu cua portname: ", self.port_names)
        self.tab1Bt4.configure(text="Active port"+"\n"+str(self.port_names[1])+"\n"+"Ready")

    def init_serial(self):
        self.status_serial = False
        try:
            self.serial_avr = serial.Serial(port='COM5', baudrate=9600,
                                       bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE,
                                       stopbits=serial.STOPBITS_ONE, timeout=0)
            time.sleep(2)
            print("Initializing...")
            # print('ten tap la:',str(self.port_names[0]))
            if self.serial_avr.isOpen():
                self.status_serial=True
                print('KET NOI TOT')
            else:
                self.status_serial = False

        except(serial.SerialException, ValueError) as ex:
            messagebox.showerror("Result", "Can not open serial port"+ str(ex))
            
    def run_callback(self):
        if self.status_serial:
            self.serial_avr.write(b'a')
            print('OK')
    def run_revert_callback(self):
        if self.status_serial:
            self.serial_avr.write(b'b')
            print('OK')

    def Send(self):
        x=self.hsa.get()
        y=self.hsb.get()
        if self.status_serial:
            self.serial_avr.write(b'*'+y.encode()+b'*'+x.encode())
        print(y+x)
    def On(self):
        if self.status_serial:
            self.serial_avr.write(b'on')
    def off(self):
        if self.status_serial:
            self.serial_avr.write(b'off')
            print('off')
    def draw(self):

        self.t=np.arange(0,5,0.1)
        self.ax1.plot(self.t,2*np.sin(np.pi*self.t)) 
        self.line1.draw()
    def draw_animate(self):
        self.a=serial.Serial('COM5')
        self.a.flushInput()
        self.b=[]
        self.c=[]
        while True:
            self.bye=self.a.readline()
            self.bye_decoded=float(self.bye[0:len(self.bye)-2].decode("utf-8"))
            self.b.append(self.bye_decoded)
            self.c.append(self.c+1)
            self.ax1.clear()
            self.ax1.plot(self.c,self.b)
            self.ani=animation.FuncAnimation(self.figure1,self.draw_animate,interval=1000)
            self.line1.draw()

        
    def frames(self):
        self.hsa=Tk.StringVar()
        self.hsb=Tk.StringVar()
        style = ttk.Style()
        style.configure('TNotebook.Tab', width=50, height=50, font=('Helvetica', 20), relief='raised', fg='red')
        style.configure('TNotebook', tabposition='s', font=('Helvetica', 18), fg='red')
        note = ttk.Notebook(root, cursor="arrow", height=2000, width=200, style='TNotebook')
        [self.tab1, self.tab2, self.tab3] = creatTab.CRT.creattab(note)
        [self.tab1Frame1, self.tab1Frame2, self.tab1Frame3] = creatTab.CRT.creatFrame(self.tab1)
        [self.tab2Frame1, self.tab2Frame2, self.tab2Frame3] = creatTab.CRT.creatFrame(self.tab2)
        [self.tab3Frame1, self.tab3Frame2, self.tab3Frame3] = creatTab.CRT.creatFrame(self.tab3)
        #tạo hai fram cho frame 2 tab1
        self.tab1Frame2_frame1=Tk.Frame(self.tab1Frame2)
        self.tab1Frame2_frame1.pack()
        self.tab1Frame2_frame2=Tk.Frame(self.tab1Frame2)
        self.tab1Frame2_frame2.pack()
        self.tab1Frame2_frame2.configure(width=500,height=500)
        #tạo khung đồ thị cho frame 2 của frame 2 của tab 1
        self.figure1 = plt.Figure(figsize=(10,4), dpi=80)
        self.ax1 = self.figure1.add_subplot()
        self.line1 = FigureCanvasTkAgg(self.figure1, self.tab1Frame2_frame2)
        self.line1.get_tk_widget().pack()
        
        

        
        
        self.tab1Frame1.pack(side='left')
        self.tab1Frame2.pack(side='left', fill='both',expand='true')
        self.tab1Frame3.pack(side='right')
        [self.tab1Bt1, self.tab1Bt2, self.tab1Bt3, self.tab1Bt4] = creatTab.CRT.drawLeftTab(self.tab1Frame1,
                                                                                            ['out of \n service', 'DAW', 'ON',
                                                                                             'SCAN'],
                                                                                            ['disable', 'normal',
                                                                                             'normal', 'normal'],
                                                                                            ['grey', 'cyan', 'cyan',
                                                                                             'cyan'])
        [self.tab1Bt5, self.tab1Bt6, self.tab1Bt7, self.tab1Bt8] = creatTab.CRT.drawRightTab(self.tab1Frame3,
                                                                                             ['ut of \n service', 'OFF',
                                                                                              'RUN BACKWARD',
                                                                                              'RUN FORWARD'],
                                                                                             ['disable', 'normal',
                                                                                              'normal', 'normal'],
                                                                                             ['grey', 'cyan',
                                                                                              'cyan', 'cyan'])
    
        self.tab1entry1=creatTab.CRT.draw_entry(self.tab1Frame2_frame1,0,0,"degri","Dir",self.hsa,self.hsb)
        # lb1=Label(self.tab1Frame2,text="dergi").grid(row=0,column=0)
        # lb2=Label(self.tab1Frame2,text="Dir").grid(row=0,column=2)
        
        # self.en1=Tk.Entry(self.tab1Frame2).grid(row=0,column=1)
        # self.en2=Tk.Entry(self.tab1Frame2).grid(row=0,column=3)
        
        

        # self.tab1Photo = PhotoImage(file="/home/pi/Downloads/project/image/channel1.gif")
        # self.tab1Photo1 = PhotoImage(file="/home/pi/Downloads/project/image/serial1.gif")
        # self.tab1Photo2 = PhotoImage(file="/home/pi/Downloads/project/image/readdata.gif")
        # self.tab6Photo1 = PhotoImage(file="/home/pi/Downloads/project/image/shutdown1.gif")
        self.tab1Bt1.configure(width=12, height=8)
        self.tab1Bt2.configure(width=12, height=9,command=self.draw)
        self.tab1Bt3.configure(width=12, height=9,command=self.On)
        self.tab1Bt4.configure(width=12, height=9, command=self.scan_ports)
        self.tab1Bt5.configure(width=12, height=8)
        self.tab1Bt6.configure(width=12, height=9,command=self.off)
        self.tab1Bt7.configure(width=12, height=9, command=self.run_revert_callback)
        # self.en1.configure(width=30)
        # self.en2.configure(width=30)
        self.tab1Bt8.configure(width=12, height=9, command=self.Send)

if __name__ == '__main__':
    root = Tk.Tk()
    #root.iconbitmap(r"/home/pi/Downloads/project/image/otani_icon.ico")
    root.geometry("1024x600")
    root.resizable(0,0)
    root.title('DONG CO')
    app = Application(root)
    root.mainloop()