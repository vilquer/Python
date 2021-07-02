 8 import sys
    9 
   10 try:
   11     import Tkinter as tk
   12 except ImportError:
   13     import tkinter as tk
   14 
   15 try:
   16     import ttk
   17     py3 = False
   18 except ImportError:
   19     import tkinter.ttk as ttk
   20     py3 = True
   21 
   22 import button_support
   23 import os.path
   24 
   25 def vp_start_gui():
   26     '''Starting point when module is the main routine.'''
   27     global val, w, root
   28     global prog_location
   29     prog_call = sys.argv[0]
   30     prog_location = os.path.split(prog_call)[0]
   31     root = tk.Tk()
   32     top = Toplevel1 (root)
   33     button_support.init(root, top)
   34     root.mainloop()
   35 
   36 w = None
   37 def create_Toplevel1(rt, *args, **kwargs):
   38     '''Starting point when module is imported by another module.
   39        Correct form of call: 'create_Toplevel1(root, *args, **kwargs)' .'''
   40     global w, w_win, root
   41     global prog_location
   42     prog_call = sys.argv[0]
   43     prog_location = os.path.split(prog_call)[0]
   44     #rt = root
   45     root = rt
   46     w = tk.Toplevel (root)
   47     top = Toplevel1 (w)
   48     button_support.init(w, top, *args, **kwargs)
   49     return (w, top)
   50 
   51 def destroy_Toplevel1():
   52     global w
   53     w.destroy()
   54     w = None
   55 
   56 class Toplevel1:
   57     def __init__(self, top=None):
   58         '''This class configures and populates the toplevel window.
   59            top is the toplevel containing window.'''
   60         _bgcolor = 'wheat'  # X11 color: #f5deb3
   61         _fgcolor = '#000000'  # X11 color: 'black'
   62         _compcolor = '#b2c9f4' # Closest X11 color: 'SlateGray2'
   63         _ana1color = '#eaf4b2' # Closest X11 color: '{pale goldenrod}'
   64         _ana2color = '#f4bcb2' # Closest X11 color: 'RosyBrown2'
   65 
   66         top.geometry("600x450+650+150")
   67         top.minsize(120, 1)
   68         top.maxsize(1905, 1170)
   69         top.resizable(1,  1)
   70         top.title("Button Example")
   71         top.configure(background="wheat")
   72         top.configure(highlightbackground="wheat")
   73         top.configure(highlightcolor="black")
   74 
   75         self.Button1 = tk.Button(top)
   76         self.Button1.place(relx=0.383, rely=0.267, height=67, width=132)
   77         self.Button1.configure(activebackground="#f4bcb2")
   78         self.Button1.configure(activeforeground="black")
   79         self.Button1.configure(background="wheat")
   80         self.Button1.configure(command=button_support.quit)
   81         self.Button1.configure(compound='top')
   82         self.Button1.configure(disabledforeground="#b8a786")
   83         self.Button1.configure(font="-family {DejaVu Sans} -size 14")
   84         self.Button1.configure(foreground="#000000")
   85         self.Button1.configure(highlightbackground="wheat")
   86         self.Button1.configure(highlightcolor="black")
   87         photo_location = os.path.join(prog_location,"./examples/button/stop.gif")
   88         global _img0
   89         _img0 = tk.PhotoImage(file=photo_location)
   90         self.Button1.configure(image=_img0)
   91         self.Button1.configure(pady="0")
   92         self.Button1.configure(text='''Push to Quit''')
   93 
   94 if __name__ == '__main__':
   95     vp_start_gui()
   96 