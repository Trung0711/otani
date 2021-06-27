from tkinter import*
win=Tk()
win.title('quản ly sinh viên')
# win.resizable(height=False,width=False)
# win.size(height=300,width=300)
scrW=win.winfo_screenwidth()
scrH=win.winfo_screenheight()
win.geometry('%dx%d'%(scrW, scrH))
win.mainloop()
