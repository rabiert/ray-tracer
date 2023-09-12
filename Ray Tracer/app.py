from config import *

class window(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.wm_title("Ray Tracer") #ray tracer
        self.geometry('600x400')
        self.resizable(width=False, height=False)
        self.iconbitmap("icons.icns")
        self.createFrames()

    def showFrame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
    
    def createFrames(self):
        container = tk.Frame(self, height=400, width=600)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}
        for F in (MainPage, SettingsPage, AboutPage):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.showFrame(MainPage)

class MainPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.Background("img/src/setting_scene32x32_.png")
        self.createWidgets()

    def Background(self, file):
        self.canvas = tk.Canvas(self, width=0, height=0) #Why use width=0 & height=0? Redundant.
        self.canvas.place(relwidth=1, relheight=1)
        img = Image.open(file)
        self.photo = ImageTk.PhotoImage(img) ##images needs to be an attribute in a class. See 2nd comment in your question for explanation. 
        self.canvas.create_image(0, 0, anchor='nw', image=self.photo)  ##use self.photo
        bold_font = font.Font(family="Times New Roman", size=36, weight="bold")
        self.canvas.create_text((300,75),font = bold_font, text="Ray Tracing Simulator", fill='darkgray')

    def createButtons(self):
        self.startButton = ttk.Button(self, text = "Start", command = lambda: self.controller.showFrame(SettingsPage))
        self.aboutButton = ttk.Button(self, text="About", command = lambda: self.controller.showFrame(AboutPage))
        self.quitButton = ttk.Button(self, text="Quit", command = self.controller.destroy)
        self.startButton.pack(pady = (150, 5))
        self.aboutButton.pack(pady = 5)
        self.quitButton.pack(side = "bottom", pady = 50)


    def createLabels(self):
        self.title = ttk.Label(self, text = "Ray Tracing Simulator", font=("Comic Sans", 32), background = "white", foreground = "darkgray")
        self.title.pack(pady = 50)

    def createWidgets(self):
        #self.createLabels()
        self.createButtons()


class SettingsPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg = "white")
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("TRadiobutton", background = "white", foreground = "black")
        style.configure("TLabel", background = "white", foreground = "black")
        style.configure("TButton", background = "white", foreground = "black")
        self.controller = controller
        self.createWidgets()

    def createFrames(self):
        self.frame0 = tk.Frame(self, padx=10, pady=10, bg = "white")
        self.frame1 = tk.Frame(self, padx=10, pady=0, bg = "white")
        self.frame2 = tk.Frame(self, padx=10, pady=0, bg = "white")
        self.frame3 = tk.Frame(self, padx=10, pady=0, bg = "white")
        self.frame4 = tk.Frame(self, padx=10, pady=0, bg = "white")
        self.frame5 = tk.Frame(self, padx=10, pady=0, bg = "white")
        self.frame6 = tk.Frame(self, padx=10, pady=0, bg = "white")

        # Grid configuration for resizable behavior
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)

        # Place LabelFrame widgets in the grid
        self.frame0.grid(row=0, column=0, padx=10, pady=(5, 0), sticky = "nsew")
        self.frame1.grid(row=1, column=0, padx=10, pady=0, sticky="nsew")
        self.frame2.grid(row=1, column=1, padx=10, pady=0, sticky="nsew")
        self.frame3.grid(row=1, column=2, padx=10, pady=0, sticky="nsew")
        self.frame4.grid(row=1, column=3, padx=10, pady=0, sticky="nsew")
        self.frame5.grid(row=2, column=3, sticky="nsew")
        self.frame6.grid(row=2, column=0, sticky="nsew")

    def createRadioButtons(self):
        self.variableDiopter = tk.IntVar(self, 0)
        self.variableSample = tk.IntVar(self, 4)
        self.variableDepth = tk.IntVar(self, 5)
        self.variableRendOpt = tk.IntVar(self, 1)
        valuesDiopters = {"4" : 4,
                "3" : 3,
                "2" : 2,
                "1" : 1,
                "0" : 0,
                "-1" : -1,
                "-2" : -2,
                "-3" : -3,
                "-4" : -4}
            
        valuesSamples = {"1x1" : 1,
                "2x2" : 2,
                "3x3" : 3,
                "4x4" : 4,
                "5x5" : 5,
                "7x7" : 7,
                "10x10" : 10,
                "15x15" : 15,
                "25x25" : 25}

        valuesDepth = {"1" : 1,
                "2" : 2,
                "3" : 3,
                "4" : 4,
                "5" : 5,
                "10" : 10,
                "15" : 15,
                "20" : 20,
                "30" : 30}
        
        valuesRenderOpt = {"Ray trace" : 1,
                           "Path trace" : 2}
        
        for (text, value) in valuesDiopters.items():
            ttk.Radiobutton(self.frame1, text = text, variable = self.variableDiopter,
                        value = value).pack(ipady = 2)

        for (text, value) in valuesSamples.items():
            ttk.Radiobutton(self.frame2, text = text, variable = self.variableSample,
                        value = value).pack(ipady = 2)

        for (text, value) in valuesDepth.items():
            ttk.Radiobutton(self.frame3, text = text, variable = self.variableDepth,
                        value = value).pack(ipady = 2)
            
        for (text, value) in valuesRenderOpt.items():
            ttk.Radiobutton(self.frame4, text = text, variable = self.variableRendOpt,
                        value = value).pack(ipady = 2)
    
    def createLabels(self):
        settings = ttk.Label(self.frame0, text = "Select your settings:")
        diopters = ttk.Label(self.frame1, text = "Diopters")
        samples = ttk.Label(self.frame2, text = "Samples per pixel")
        depth = ttk.Label(self.frame3, text = "Ray Depth")
        renderOpt = ttk.Label(self.frame4, text = "Rendering options")
        settings.pack()
        diopters.pack()
        samples.pack()
        depth.pack()
        renderOpt.pack()

    def createButtons(self):
        renderButton = ttk.Button(self.frame5, text = "Render", command = self.renderWindow)
        backButton = ttk.Button(self.frame6, text="Go back", command=lambda: self.controller.showFrame(MainPage))
        backButton.pack()
        renderButton.pack()

    def createWidgets(self):
        self.createFrames()
        self.createLabels()
        self.createRadioButtons()
        self.createButtons()


    def renderWindow(self):
        rendered = RenderWindow(self, diopter = self.variableDiopter.get(), samples = self.variableSample.get(), depth = self.variableDepth.get(), renderOpt = self.variableRendOpt.get())

class AboutPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg = "white")
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("TLabel", background = "white", foreground = "black")
        style.configure("TButton", background = "white", foreground = "black")
        self.controller = controller
        self.createWidgets()

    def createFrames(self):
        self.frame0 = tk.Frame(self, padx=10, pady=10, bg = "white")
        self.frame1 = tk.Frame(self, padx=10, pady=0, bg = "white")
        self.frame2 = tk.Frame(self, padx=10, pady=0, bg = "white")
        self.frame3 = tk.Frame(self, padx=10, pady=0, bg = "white")

        # Grid configuration for resizable behavior
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)

        # Place LabelFrame widgets in the grid
        self.frame0.grid(row=0, column=0, padx=10, pady=20, sticky = "nsew")
        self.frame1.grid(row=1, column=0, padx=10, pady=15, sticky = "nsew")
        self.frame2.grid(row=2, column=0, padx=10, pady=15, sticky = "nsew")
        self.frame3.grid(row=3, column=0, sticky="nsew")

    def createLabels(self):
        intitle = ttk.Label(self.frame0, text = "Ray Tracing to simulate refraction errors", font = ("Times New Roman", 32))
        intext1 = ttk.Label(self.frame1, text = "This is an application to simulate the effecst of myopia and hypermetropia.", font = ("Times New Roman", 16))
        intext2 = ttk.Label(self.frame2, text = "Select a diopter and try yourself!", font = ("Times New Roman", 16))
        intitle.pack()
        intext1.pack()
        intext2.pack()

    def createButtons(self):
        backButton = ttk.Button(self.frame3, text="Go back", command=lambda: self.controller.showFrame(MainPage))
        backButton.pack()

    def createWidgets(self):
        self.createFrames()
        self.createLabels()
        self.createButtons()

if __name__ == "__main__":
    root = window()
    root.mainloop()
    