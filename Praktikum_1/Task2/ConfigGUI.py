import tkinter as tk
from tkinter import ttk

class ConfigGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Grid Configuration")

        # Default values
        self.defaultConfig = {
            "grid_width": 700,
            "grid_height": 700,
            "tile_width": 18,
            "tile_height": 18,
            "padding": 20,
            "margin": 2,
            "animation_speed": 2,  # 1 = Slow, 2 = Fast, 3 = Instant, Custom = user-defined
        }

        self.config = self.defaultConfig.copy()
        self.sliderUpdateTimer = {}  # Track timers for each slider

        # Control variables
        self.controlVars = {
            key: tk.IntVar(value=val) if isinstance(val, int) else tk.StringVar(value=val)
            for key, val in self.defaultConfig.items()
        }

        # Attach traces to control variables for fields
        for key, var in self.controlVars.items():
            if isinstance(var, tk.StringVar):
                var.trace_add("write", lambda *args, k=key: self.onEntryChange(k))

        # Create notebook for tabs
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
        
        # Tab 2: Mouse-only input
        self.tabMouse = ttk.Frame(self.notebook)
        self.notebook.add(self.tabMouse, text="Mouse-Only")
        self.createMouseTab(self.tabMouse)

        #DISABLED FOR NOW
        # # Tab 1: Keyboard & mouse input
        # self.tabKeyboard = ttk.Frame(self.notebook)
        # self.notebook.add(self.tabKeyboard, text="Keyboard + Mouse")
        # self.createKeyboardTab(self.tabKeyboard)

        # Start GUI loop
        self.root.mainloop()

    def createKeyboardTab(self, parent):
        frame = ttk.Frame(parent, padding="10")
        frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Labels and Entry widgets
        self.createEntry(frame, "Grid Width", "grid_width", 0)
        self.createEntry(frame, "Grid Height", "grid_height", 1)
        self.createEntry(frame, "Tile Width", "tile_width", 2)
        self.createEntry(frame, "Tile Height", "tile_height", 3)
        self.createEntry(frame, "Padding", "padding", 4)
        self.createEntry(frame, "Margin", "margin", 5)

        # Animation Speed
        self.createAnimationSpeed(frame, 6)

        # Buttons
        ttk.Button(frame, text="Start Program", command=self.startProgram).grid(column=0, row=8, columnspan=2, pady=10)

    def createMouseTab(self, parent):
        frame = ttk.Frame(parent, padding="10")
        frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Labels and sliders
        self.createSlider(frame, "Grid Width", "grid_width", 100, 2000, 0)
        self.createSlider(frame, "Grid Height", "grid_height", 100, 2000, 1)
        self.createSlider(frame, "Tile Width", "tile_width", 5, 100, 2)
        self.createSlider(frame, "Tile Height", "tile_height", 5, 100, 3)
        self.createSlider(frame, "Padding", "padding", 0, 100, 4)
        self.createSlider(frame, "Margin", "margin", 0, 20, 5)

        # Animation Speed
        self.createAnimationSpeed(frame, 6, mouseOnly=True)

        # Buttons
        ttk.Button(frame, text="Start Program", command=self.startProgram).grid(column=0, row=8, columnspan=2, pady=10)

    def createEntry(self, parent, label, key, row):
        ttk.Label(parent, text=label).grid(column=0, row=row, sticky=tk.W)
        entry = ttk.Entry(parent, textvariable=self.controlVars[key])
        entry.grid(column=1, row=row, sticky=(tk.W, tk.E))
        entry.bind("<KeyRelease>", lambda e, k=key: self.redraw(k))

    def createSlider(self, parent, label, key, minVal, maxVal, row)-> ttk.Scale:
        ttk.Label(parent, text=label).grid(column=0, row=row, sticky=tk.W)
        # Slider Widget
        slider = ttk.Scale(
            parent, from_=minVal, to=maxVal, orient=tk.HORIZONTAL, variable=self.controlVars[key]
        )
        slider.grid(column=1, row=row, sticky=(tk.W, tk.E))
        slider.bind("<ButtonRelease-1>", lambda e, k=key: self.onSliderChange(k))

        # Label to show current slider value
        valueLabel = ttk.Label(parent, text=str(self.controlVars[key].get()))
        valueLabel.grid(column=2, row=row, sticky=tk.W)

        # Update value label dynamically
        self.controlVars[key].trace_add("write", lambda *args, v=valueLabel, var=self.controlVars[key]: v.config(text=str(var.get())))
        return slider

    def onEntryChange(self, key):
        """Handle entry field changes."""
        self.redraw(key)

    def onSliderChange(self, key):
        """Handle slider changes with debounce."""
        if key in self.sliderUpdateTimer:
            self.root.after_cancel(self.sliderUpdateTimer[key])
        self.sliderUpdateTimer[key] = self.root.after(100, lambda: self.redraw(key))

    def createAnimationSpeed(self, parent, row, mouseOnly=False):
        ttk.Label(parent, text="Animation Speed").grid(column=0, row=row, sticky=tk.W)

        # Animation Speed Radio Buttons
        speedVar = self.controlVars["animation_speed"]
        speedFrame = ttk.Frame(parent)
        speedFrame.grid(column=1, row=row, sticky=tk.W)

        ttk.Radiobutton(speedFrame, text="Slow", variable=speedVar, value=1, command=lambda: self.disableCustomSpeed(customSpeedWidget)).pack(side=tk.LEFT)
        ttk.Radiobutton(speedFrame, text="Fast", variable=speedVar, value=2, command=lambda: self.disableCustomSpeed(customSpeedWidget)).pack(side=tk.LEFT)
        ttk.Radiobutton(speedFrame, text="Instant", variable=speedVar, value=3, command=lambda: self.disableCustomSpeed(customSpeedWidget)).pack(side=tk.LEFT)

        if mouseOnly:
            customSpeedWidget = self.createSlider(parent,"","animation_speed",1,100,row+1)
            # customSpeedWidget = ttk.Scale(
            #     parent, from_=1, to=1000, orient=tk.HORIZONTAL, variable=self.controlVars["animation_speed"]
            # )
        else:
            customSpeedWidget = ttk.Entry(parent, textvariable=self.controlVars["animation_speed"])

        ttk.Radiobutton(
            speedFrame,
            text="Custom",
            variable=speedVar,
            value=4,
            command=lambda: customSpeedWidget.configure(state="normal"),
        ).pack(side=tk.LEFT)

        customSpeedWidget.grid(column=1, row=row + 1, sticky=(tk.W, tk.E))
        customSpeedWidget.configure(state="disabled")  # Initially disabled

    def enableCustomSpeed(self, widget):
        widget.configure(state="normal")

    def disableCustomSpeed(self, widget):
        widget.configure(state="disabled")

    def redraw(self, key=None):
        """Function called whenever any value changes."""
        if key:
            print(f"Redrawing triggered by {key}: {self.controlVars[key].get()}")
        else:
            print("Redrawing with new config:", {key: var.get() for key, var in self.controlVars.items()})

    def startProgram(self):
        """Start the program with the current configuration."""
        print("Starting program with config:", {key: var.get() for key, var in self.controlVars.items()})
        self.root.destroy()

# Run the GUI
if __name__ == "__main__":
    gui = ConfigGUI()
