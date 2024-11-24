from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import Screen, ScreenManager

# Function definitions for calculations
def calculate_cube_volume(side):
    return side ** 3

def calculate_sphere_volume(radius):
    return (4 / 3) * 3.14159 * (radius ** 3)

def calculate_parallelepiped_volume(length, width, height):
    return length * width * height

def calculate_cylinder_volume(radius, height):
    return 3.14159 * (radius ** 2) * height

def calculate_mass_density(mass, volume):
    return mass / volume

def calculate_weight_density(weight, gravity=9.81):
    return weight / gravity

def calculate_specific_gravity(mass_density, reference_density):
    return mass_density / reference_density

# Main screen for navigation
class MainScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # Title
        layout.add_widget(Label(text="Measurement and Unit Calculator", font_size=24, size_hint_y=None, height=50))
        
        # Navigation buttons
        btn_area = Button(text="Area", on_press=lambda x: setattr(self.manager, 'current', 'area'))
        btn_volume = Button(text="Volume", on_press=lambda x: setattr(self.manager, 'current', 'volume'))
        btn_density = Button(text="Density", on_press=lambda x: setattr(self.manager, 'current', 'density'))
        btn_exit = Button(text="Exit", on_press=lambda x: App.get_running_app().stop())
        
        layout.add_widget(btn_area)
        layout.add_widget(btn_volume)
        layout.add_widget(btn_density)
        layout.add_widget(btn_exit)
        
        self.add_widget(layout)

class AreaScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        self.inputs = {}  # Dictionary to hold input widgets
        
        # Title
        self.layout.add_widget(Label(text="Area Calculator", font_size=20, size_hint_y=None, height=50))
        
        # Buttons for area calculations
        btn_square = Button(text="Square", on_press=lambda x: self.display_input_screen("Square Area", ["Side"], lambda s: s**2))
        btn_rectangle = Button(text="Rectangle", on_press=lambda x: self.display_input_screen("Rectangle Area", ["Length", "Width"], lambda l, w: l * w))
        btn_triangle = Button(text="Triangle", on_press=lambda x: self.display_input_screen("Triangle Area", ["Base", "Height"], lambda b, h: 0.5 * b * h))
        btn_circle = Button(text="Circle", on_press=lambda x: self.display_input_screen("Circle Area", ["Radius"], lambda r: 3.14159 * r**2))
        btn_back = Button(text="Back", on_press=lambda x: setattr(self.manager, 'current', 'main'))
        
        self.layout.add_widget(btn_square)
        self.layout.add_widget(btn_rectangle)
        self.layout.add_widget(btn_triangle)
        self.layout.add_widget(btn_circle)
        self.layout.add_widget(btn_back)
        
        self.add_widget(self.layout)

    def display_input_screen(self, title, input_labels, calculation_function):
        self.layout.clear_widgets()
        self.inputs.clear()
        
        # Title
        self.layout.add_widget(Label(text=title, font_size=20, size_hint_y=None, height=50))
        
        # Input fields
        for label in input_labels:
            self.layout.add_widget(Label(text=label))
            input_field = TextInput(multiline=False)
            self.inputs[label] = input_field
            self.layout.add_widget(input_field)
        
        # Calculation button
        def calculate_result(instance):
            try:
                values = [float(self.inputs[label].text) for label in input_labels]
                result = calculation_function(*values)
                self.layout.add_widget(Label(text=f"Result: {result} m²", size_hint_y=None, height=30))
            except ValueError:
                self.layout.add_widget(Label(text="Invalid input! Please enter numeric values.", size_hint_y=None, height=30))
        
        btn_calculate = Button(text="Calculate", on_press=calculate_result)
        btn_back = Button(text="Back", on_press=lambda x: self.reload_layout())
        
        self.layout.add_widget(btn_calculate)
        self.layout.add_widget(btn_back)

    def reload_layout(self):
        self.layout.clear_widgets()
        self.__init__()

class VolumeScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        self.inputs = {}
        # Title
        self.layout.add_widget(Label(text="Volume Calculator", font_size=20, size_hint_y=None, height=50))
        
        # Buttons for volume calculations
        btn_cube = Button(text="Cube", on_press=lambda x: self.display_input_screen("Cube Volume", ["Side"], calculate_cube_volume))
        btn_sphere = Button(text="Sphere", on_press=lambda x: self.display_input_screen("Sphere Volume", ["Radius"], calculate_sphere_volume))
        btn_cylinder = Button(text="Cylinder", on_press=lambda x: self.display_input_screen("Cylinder Volume", ["Radius", "Height"], calculate_cylinder_volume))
        btn_parallelepiped = Button(text="Parallelepiped", on_press=lambda x: self.display_input_screen("Parallelepiped Volume", ["Length", "Width", "Height"], calculate_parallelepiped_volume))
        btn_back = Button(text="Back", on_press=lambda x: setattr(self.manager, 'current', 'main'))
        
        self.layout.add_widget(btn_cube)
        self.layout.add_widget(btn_sphere)
        self.layout.add_widget(btn_cylinder)
        self.layout.add_widget(btn_parallelepiped)
        self.layout.add_widget(btn_back)
        
        self.add_widget(self.layout)

    def display_input_screen(self, title, input_labels, calculation_function):
        self.layout.clear_widgets()
        self.inputs.clear()
        
        # Title
        self.layout.add_widget(Label(text=title, font_size=20, size_hint_y=None, height=50))
        
        # Input fields
        for label in input_labels:
            self.layout.add_widget(Label(text=label))
            input_field = TextInput(multiline=False)
            self.inputs[label] = input_field
            self.layout.add_widget(input_field)
        
        # Calculation button
        def calculate_result(instance):
            try:
                values = [float(self.inputs[label].text) for label in input_labels]
                result = calculation_function(*values)
                self.layout.add_widget(Label(text=f"Result: {result} m³", size_hint_y=None, height=30))
            except ValueError:
                self.layout.add_widget(Label(text="Invalid input! Please enter numeric values.", size_hint_y=None, height=30))
        
        btn_calculate = Button(text="Calculate", on_press=calculate_result)
        btn_back = Button(text="Back", on_press=lambda x: self.reload_layout())
        
        self.layout.add_widget(btn_calculate)
        self.layout.add_widget(btn_back)
    def reload_layout(self):
        self.layout.clear_widgets()
        self.__init__()

class DensityScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        self.inputs = {}
        # Title
        self.layout.add_widget(Label(text="Density Calculator", font_size=20, size_hint_y=None, height=50))
        
        # Buttons for density calculations
        btn_mass_density = Button(text="Mass Density", on_press=lambda x: self.display_input_screen_mass("Mass Density", ["Mass", "Volume"], calculate_mass_density))
        btn_weight_density = Button(text="Weight Density", on_press=lambda x: self.display_input_screen_weight("Weight Density", ["Weight(In Newtons)", "Volume"], calculate_weight_density))
        btn_specific_gravity = Button(text="Specific Gravity", on_press=lambda x: self.display_input_screen("Specific Gravity", ["Object Weight", "Reference"], calculate_specific_gravity))
        btn_back = Button(text="Back", on_press=lambda x: setattr(self.manager, 'current', 'main'))
        
        self.layout.add_widget(btn_mass_density)
        self.layout.add_widget(btn_weight_density)
        self.layout.add_widget(btn_specific_gravity)
        self.layout.add_widget(btn_back)
        
        self.add_widget(self.layout)

    def display_input_screen(self, title, input_labels, calculation_function):
        self.layout.clear_widgets()
        self.inputs.clear()
        
        # Title
        self.layout.add_widget(Label(text=title, font_size=20, size_hint_y=None, height=50))
        
        # Input fields
        for label in input_labels:
            self.layout.add_widget(Label(text=label))
            input_field = TextInput(multiline=False)
            self.inputs[label] = input_field
            self.layout.add_widget(input_field)
        
        # Calculation button
        def calculate_result(instance):
            try:
                values = [float(self.inputs[label].text) for label in input_labels]
                result = calculation_function(*values)
                self.layout.add_widget(Label(text=f"Result: {result}", size_hint_y=None, height=30))
            except ValueError:
                self.layout.add_widget(Label(text="Invalid input! Please enter numeric values.", size_hint_y=None, height=30))
        
        btn_calculate = Button(text="Calculate", on_press=calculate_result)
        btn_back = Button(text="Back", on_press=lambda x: self.reload_layout())
        
        self.layout.add_widget(btn_calculate)
        self.layout.add_widget(btn_back)

    def display_input_screen_mass(self, title, input_labels, calculation_function):
        self.layout.clear_widgets()
        self.inputs.clear()
        
        # Title
        self.layout.add_widget(Label(text=title, font_size=20, size_hint_y=None, height=50))
        
        # Input fields
        for label in input_labels:
            self.layout.add_widget(Label(text=label))
            input_field = TextInput(multiline=False)
            self.inputs[label] = input_field
            self.layout.add_widget(input_field)
        
        # Calculation button
        def calculate_result(instance):
            try:
                values = [float(self.inputs[label].text) for label in input_labels]
                result = calculation_function(*values)
                self.layout.add_widget(Label(text=f"Result: {result} Kg/m³", size_hint_y=None, height=30))
            except ValueError:
                self.layout.add_widget(Label(text="Invalid input! Please enter numeric values.", size_hint_y=None, height=30))
        
        btn_calculate = Button(text="Calculate", on_press=calculate_result)
        btn_back = Button(text="Back", on_press=lambda x: self.reload_layout())
        
        self.layout.add_widget(btn_calculate)
        self.layout.add_widget(btn_back)

    def reload_layout(self):
        self.layout.clear_widgets()
        self.__init__()

    def display_input_screen_weight(self, title, input_labels, calculation_function):
        self.layout.clear_widgets()
        self.inputs.clear()
        
        # Title
        self.layout.add_widget(Label(text=title, font_size=20, size_hint_y=None, height=50))
        
        # Input fields
        for label in input_labels:
            self.layout.add_widget(Label(text=label))
            input_field = TextInput(multiline=False)
            self.inputs[label] = input_field
            self.layout.add_widget(input_field)
        
        # Calculation button
        def calculate_result(instance):
            try:
                values = [float(self.inputs[label].text) for label in input_labels]
                result = calculation_function(*values)
                self.layout.add_widget(Label(text=f"Result: {result} N/m³", size_hint_y=None, height=30))
            except ValueError:
                self.layout.add_widget(Label(text="Invalid input! Please enter numeric values.", size_hint_y=None, height=30))
        
        btn_calculate = Button(text="Calculate", on_press=calculate_result)
        btn_back = Button(text="Back", on_press=lambda x: self.reload_layout())
        
        self.layout.add_widget(btn_calculate)
        self.layout.add_widget(btn_back)

class MeasurementApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScreen(name='main'))
        sm.add_widget(AreaScreen(name='area'))
        sm.add_widget(VolumeScreen(name='volume'))
        sm.add_widget(DensityScreen(name='density'))
        return sm

if __name__ == '__main__':
    MeasurementApp().run()
