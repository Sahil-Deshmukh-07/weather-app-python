import tkinter as tk
import weather as w

class WeatherApp:
    def __init__(self):
        root = tk.Tk()
        self.root = root
        self.root.configure(bg="#006758")
        self.root.title("Weather App")
        root.geometry("400x400")
        self.root.resizable(False,False)

        self.input =  tk.Entry(root,border=2, relief="solid", justify="center", font=("Arial",12,"bold"))
        self.input.focus_set()
        self.input.pack(pady=20)

        self.button = tk.Button(root, text="Get Weather", command=self.on_button_click,border=2, relief="raised", padx=10, pady=5,font=("Arial",12,"bold"),background="#015f4f",foreground="white", activebackground="#00796b", activeforeground="white")
        self.button.pack(pady=10)
        root.bind("<Return>", func=lambda event: self.on_button_click())


        root.mainloop()

    def on_button_click(self):
        city = self.input.get()
        self.result = tk.Label(self.root, text=w.get_weather(city), bg="#070707", fg="white",border=2, relief="solid", padx=10, pady=10,font=("Arial",12,"bold"))
        self.result.pack(pady=30)
        self.input.delete(0, tk.END)
        self.root.bind("<Key>", func=lambda event: self.root.after(100,self.result.destroy()))



if __name__ == "__main__":
    app = WeatherApp()


