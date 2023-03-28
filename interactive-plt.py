import matplotlib.pyplot as plt
from matplotlib.widgets import Button
from matplotlib.widgets import Slider


class InteractiveConstruction:
    def __init__(self, steps):
        self.steps = steps
        self.current_step = 0
        self.fig, self.ax = plt.subplots()
        plt.subplots_adjust(bottom=0.3)

        # Register key press event
        self.fig.canvas.mpl_connect('key_press_event', self.on_key_press)

        # Create buttons
        button_labels = ['Start', 'End', 'Back', 'Forward', 'Play', 'Stop']
        button_callbacks = [self.on_start, self.on_end, self.on_back, self.on_forward, self.on_play, self.on_stop]
        button_width = 0.1
        button_height = 0.075
        button_spacing = 0.01
        button_y = 0.05

        self.buttons = []
        for i, (label, callback) in enumerate(zip(button_labels, button_callbacks)):
            ax_button = plt.axes([0.01 + i * (button_width + button_spacing), button_y, button_width, button_height])
            button = Button(ax_button, label)
            button.on_clicked(callback)
            self.buttons.append(button)

        # Create slider
        ax_slider = plt.axes([0.01, 0.15, 0.98, 0.03])
        self.slider = Slider(ax_slider, 'Step', 0, len(self.steps) - 1, valinit=0, valstep=1)
        self.slider.on_changed(self.on_slider_change)

        self.update_plot()

    # Other methods remain the same...
    def on_back(self, event):
        if self.current_step > 0:
            self.current_step -= 1
            self.update_plot()

    def on_forward(self, event):
        if self.current_step < len(self.steps) - 1:
            self.current_step += 1
            self.update_plot()


    def on_start(self, event):
        self.current_step = 0
        self.update_plot()

    def on_end(self, event):
        self.current_step = len(self.steps) - 1
        self.update_plot()

    def on_play(self, event):
        # Implement play functionality, e.g., automatically move forward through the steps
        pass

    def on_stop(self, event):
        # Implement stop functionality, e.g., stop automatically moving forward through the steps
        pass

    def on_slider_change(self, val):
        self.current_step = int(val)
        self.update_plot()

    def on_key_press(self, event):
         if event.key == 'left':
             self.on_back(event)
         elif event.key == 'right':
             self.on_forward(event)

    def update_plot(self):
        self.ax.clear()
        self.steps[self.current_step](self.ax)
        plt.draw()

def step1(ax):
    # Draw first construction step
    circle = plt.Circle((0, 0), 1, fill=False)
    ax.add_artist(circle)
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 1.5)
    ax.set_title("Step 1: Draw a circle")

def step2(ax):
    # Draw second construction step
    step1(ax)
    ax.plot([0, 1], [0, 0], 'r-')
    ax.set_title("Step 2: Draw a line segment")

def main():
    steps = [step1, step2]
    interactive_construction = InteractiveConstruction(steps)
    plt.show()

if __name__ == "__main__":
    main()

