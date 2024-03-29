import tkinter as Tk
from tkinter import Button, Entry, Label, StringVar, ttk
from matplotlib.figure import Figure
max_freq=1000
class CRT(ttk.Notebook):
    def creattab(self):
        tab1 = Tk.Frame(self, relief="raised", borderwidth=1)
        tab2 = Tk.Frame(self, relief="raised", borderwidth=1)
        tab3 = Tk.Frame(self, relief="raised", borderwidth=1)
        self.add(tab1, text="Tab1")
        self.add(tab2, text="Tab2")
        self.add(tab3, text="Tab3")
        self.pack(side='bottom',fill="both",padx=1,pady=1,expand=0)

        return [tab1,tab2,tab3]
    def creatFrame(self):
        tab1Frame1 = Tk.Frame(self,bd=1,bg='white',cursor='none')
        tab1Frame2 = Tk.Frame(self,bd=1,bg='white',cursor='none',width=810)
        tab1Frame3 = Tk.Frame(self,bd=1,bg='white',cursor='none')
        return [tab1Frame1,tab1Frame2,tab1Frame3]
    def drawLeftTab(self, arr,arr1,arr2):
        setButton = Tk.Button(self, text=arr[0], width=8, height=8, activebackground='blue',bg=arr2[0],
                              state=arr1[0])
        setButton1 = Tk.Button(self, text=arr[1], width=8, height=7, activebackground='blue',bg=arr2[1],
                               state=arr1[1])
        setButton2 = Tk.Button(self, text=arr[2], width=8, height=7, activebackground='blue',bg=arr2[2],
                               state=arr1[2])
        setButton3 = Tk.Button(self, text=arr[3], width=8, height=8, activebackground='blue',bg=arr2[3],
                               state=arr1[3])
        setButton.grid(column=0, row=0)
        setButton1.grid(column=0, row=1)
        setButton2.grid(column=0, row=2)
        setButton3.grid(column=0, row=3)
        return [setButton,setButton1,setButton2,setButton3]
    def draw_entry(self,a,b,arr,arr1,x,y):
    
        lb1=Tk.Label(self,text=arr).grid(row=a,column=b)
        lb2=Tk.Label(self,text=arr1).grid(row=a,column=b+2)
        
        en1=Tk.Entry(self, width=30,textvariable=x).grid(row=a,column=b+1)
        en2=Tk.Entry(self, width=30,textvariable=y).grid(row=a,column=b+3)
        return [lb1,lb2,en1,en2]
        

    def drawRightTab(self, arr, arr1, arr2):
        setButton = Tk.Button(self, text=arr[0], width=8, height=8, activebackground='blue', bg=arr2[0],
                                state=arr1[0])
        setButton1 = Tk.Button(self, text=arr[1], width=8, height=7, activebackground='blue', bg=arr2[1],
                                state=arr1[1])
        setButton2 = Tk.Button(self, text=arr[2], width=8, height=7, activebackground='blue', bg=arr2[2],
                               state=arr1[2])
        setButton3 = Tk.Button(self, text=arr[3], width=8, height=8, activebackground='blue', bg=arr2[3],
                               state=arr1[3])
        setButton.grid(column=0, row=0, sticky='E')
        setButton1.grid(column=0, row=1, sticky='E')
        setButton2.grid(column=0, row=2, sticky='E')
        setButton3.grid(column=0, row=3, sticky='E')
        return [setButton, setButton1, setButton2, setButton3]
    def creatFigure(self,num):
        ax=[]
    
        fig1 = Figure(figsize=(8.1, 8))
        fig1.subplots_adjust(left=0.1, right=0.95, top=0.95, bottom=0.1, wspace=1, hspace=0.5)

        for idx in range(1,num+1):
            ax.append(fig1.add_subplot(num, 1, idx))
        for idx in range(num):
            # tit = "CHANEL" + str(idx)
            # ax[idx].set_title(tit)
            ax[idx].set_ylabel('')
            # ax[idx].set_xlim(xmax=max_freq)
            ax[idx].grid()
        return fig1
