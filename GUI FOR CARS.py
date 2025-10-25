import tkinter as tk
from PIL import Image, ImageTk


#Create a class of all cars
class CarOrderApp:
    def __init__(self,application):
        self.application = application
        self.application.title("Car Order")
        self.application.geometry("1200x800")
        self.background_color = "#2f4f7f"
        self.application.configure(bg=self.background_color)
        self.welcome_screen()



    def welcome_screen(self):
        self.clear_screen()
        background_image = Image.open("mercedes-benz-sls-amg-7026071_1280.jpg")
        background_image = background_image.resize((1200, 800))
        background_photo = ImageTk.PhotoImage(background_image)
        background_label = tk.Label(self.application, image=background_photo)
        background_label.image = background_photo
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        welcome_label = tk.Label(self.application, text="Welcome to CAPTAIN AUTOMOBILE!", font=('Arial Black', 40), bg="Azure4", fg="black", relief="ridge")
        welcome_label.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

        get_started_button = tk.Button(self.application, text="GET STARTED", command=self.car_list_screen, font=("Calibri", 18,"bold"), bg="azure4")
        get_started_button.place(relx=0.8, rely=0.8, anchor=tk.CENTER)


    def car_list_screen(self):
        self.clear_screen()
        background_image = Image.open("cars-6863557_1280.jpg")
        background_image = background_image.resize((1200, 800))
        background_photo = ImageTk.PhotoImage(background_image)
        background_label = tk.Label(self.application, image=background_photo)
        background_label.image = background_photo
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        car_list_label = tk.Label(self.application, text="CARS", font=("italic", 36, "bold"), bg="bisque", relief="sunken")
        car_list_label.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

        image_width = 250
        image_height = 150

        toyota_camry_image = Image.open("toyota-4422348_1280.jpg")
        toyota_camry_image = toyota_camry_image.resize((image_width, image_height))
        toyota_camry_photo = ImageTk.PhotoImage(toyota_camry_image)

        honda_civic_image = Image.open('honda-civic-8070391_1280.jpg')
        honda_civic_image = honda_civic_image.resize((image_width, image_height))
        honda_civic_photo = ImageTk.PhotoImage(honda_civic_image)

        ford_mustang_image = Image.open('automobile-3344988_1280.jpg')
        ford_mustang_image = ford_mustang_image.resize((image_width, image_height))
        ford_mustang_photo = ImageTk.PhotoImage(ford_mustang_image)

        mercedes_benz_image = Image.open("mercedes-benz-3585098_1280.jpg")
        mercedes_benz_image = mercedes_benz_image.resize((image_width, image_height))
        mercedes_benz_photo = ImageTk.PhotoImage(mercedes_benz_image)

        # Display Car images and details
        car1_image_label = tk.Label(self.application, image=toyota_camry_photo)
        car1_image_label.image = toyota_camry_photo
        car1_image_label.place(x=100, y=100)

        car1_label = tk.Label(self.application, text="CAR 1: TOYOTA CAMRY\nPRICE - $20,000", font=("Arial", 15, "italic"), bg="DarkSeaGreen1")
        car1_label.place(x=100, y=250)

        car1_order_button = tk.Button(self.application, text="ORDER NOW", command=lambda: self.order_car("toyota-4422348_1280.jpg", "TOYOTA CAMRY"), font=("Arial", 18, "bold"), bg="purple3")
        car1_order_button.place(x=100, y=320)
        # love all this
        car2_image_label = tk.Label(self.application, image=honda_civic_photo)
        car2_image_label.image = honda_civic_photo
        car2_image_label.place(x=900, y=100)

        car2_label = tk.Label(self.application, text="CAR 2: HONDA CIVIC\nPRICE - $18,000", font=("Arial", 15, "italic"), bg="SlateGray4")
        car2_label.place(x=900, y=250)

        car2_order_button = tk.Button(self.application, text="ORDER NOW", command=lambda: self.order_car("honda-civic-8070391_1280.jpg", "HONDA CIVIC"), font=("Arial", 18, 'bold'), bg="purple3")
        car2_order_button.place(x=900, y=320)

        car3_image_label = tk.Label(self.application, image=ford_mustang_photo)
        car3_image_label.image = ford_mustang_photo
        car3_image_label.place(x=100, y=400)

        car3_label = tk.Label(self.application, text="CAR 1: FORD MUSTANG\nPRICE - $30,000", font=("Arial", 15, "italic"), bg="chocolate3")
        car3_label.place(x=100, y=550)

        car3_order_button = tk.Button(self.application, text="ORDER NOW", command=lambda: self.order_car("automobile-3344988_1280.jpg", "FORD MUSTANG"), font=("Arial", 18, "bold"), bg="purple3")
        car3_order_button.place(x=100, y=620)

        car4_image_label = tk.Label(self.application, image=mercedes_benz_photo)
        car4_image_label.image = mercedes_benz_photo
        car4_image_label.place(x=900, y=400)

        car4_label = tk.Label(self.application, text="CAR 1: FORD MUSTANG\nPRICE - $45,000", font=("Arial", 15, 'italic'), bg="thistle")
        car4_label.place(x=900,y=550)

        car4_order_button = tk.Button(self.application, text="ORDER NOW",
                                      command=lambda: self.order_car("mercedes-benz-3585098_1280.jpg", "MERCEDES BENZ"),
                                      font=("Arial", 18, "bold"), bg="purple3")
        car4_order_button.place(x=900, y=620)

    def order_car(self, image_path, car_name):
        self.clear_screen()
        car_image = Image.open(image_path)
        car_image = car_image.resize((400,300))
        car_photo = ImageTk.PhotoImage(car_image)
        car_image_label = tk.Label(self.application, image=car_photo)
        car_image_label.image = car_photo
        car_image_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        order_label = tk.Label(self.application, text=f"YOU HAVE NOW ORDERED {car_name}!", font=("Arial, 20"), bg="LightGoldenrod4")
        order_label.place(relx=0.5, rely=0.1, anchor=tk.CENTER)
        back_button = tk.Button(self.application, text="BACK TO CAR LIST", command=self.car_list_screen, font=("Arial, 18"), bg="grey13")
        back_button.place(relx=0.5, rely=0.9, anchor=tk.CENTER)


    def clear_screen(self):
        for widget in self.application.winfo_children():
            widget.destroy()


if __name__ == "__main__":
    application = tk.Tk()
    app = CarOrderApp(application)
    application.mainloop()

