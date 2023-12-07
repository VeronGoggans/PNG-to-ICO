from tkinter import filedialog, PhotoImage
import customtkinter
from PIL import Image
import os

class Converter:
    def __init__(self) -> None:
        self.input_format = '.png'
        self.output_format = '.ico'
        self.cwd = os.getcwd()
        self.window = customtkinter.CTk()
        customtkinter.set_appearance_mode('light')
        self.icon = PhotoImage(file=f'{self.cwd}/img/ico_window_icon.png')
        self.window.title = 'ICO'
        self.window.geometry('600x500')
        self.window.iconphoto(False, self.icon)

        # App colors.
        self.primary = '#ffffff'
        self.secondary = '#83caff'
        self.tertiary = '#0076cf'
        self.text_color = '#444863'

        # Customtkinter widgets below.
        self.frame = customtkinter.CTkFrame(self.window, fg_color=self.primary)
        self.image = customtkinter.CTkImage(light_image=Image.open(f'{self.cwd}/img/ico_window_image.png'), size=(200, 200))
        self.image_label = customtkinter.CTkLabel(self.frame, text='', image=self.image, fg_color=self.primary, bg_color=self.primary)
        self.button = customtkinter.CTkButton(self.frame, text='Open', fg_color=self.secondary, hover_color=self.tertiary, text_color=self.primary, width=220, height=40, corner_radius=25, font=('helvetica', 20), command=self.png_to_ico)
        self.message_label = customtkinter.CTkLabel(self.frame, text="Press 'open' to select a PNG file.", font=('helvetica', 16))

        # Setting the mainloop of the program & calling the render method.
        self.__render()
        self.window.mainloop()


    def __render(self):
        self.frame.pack(fill='both', expand=True)
        self.image_label.pack(pady=50, fill='x', expand=False)
        self.button.pack(expand=False, side='top')
        self.message_label.pack(pady=15, expand=False, side='top')

    def png_to_ico(self):
        file_path = filedialog.askopenfilename()
        if file_path.endswith(self.input_format):
            try:
                png_image = Image.open(file_path)
                new_file_path = file_path.replace(self.input_format, self.output_format)
                png_image.save(new_file_path, format='ICO', sizes=[(png_image.width, png_image.height)])
                self.message_label.configure(text='Conversion succesfull')
            except Exception as e:
                self.message_label.configure(text=f'{e}')
        else:
            self.message_label.configure(text='Please select a PNG file.')

my_converter = Converter()