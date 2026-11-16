"""Temperature Converter uses tkinter to create a GUI for converting 
temperatures between Fahrenheit and Celsius."""

import tkinter as tk
from tkinter import messagebox


def main():
    window = tk.Tk()
    window.title("Temperature Converter")

    fahrenheit_value = tk.StringVar(value="32.0")
    celsius_value = tk.StringVar(value="0.0")

    def convert_to_celsius():
        try:
            fahrenheit = float(fahrenheit_value.get())
        except ValueError:
            messagebox.showerror("Invalid value", "Enter a valid Fahrenheit temperature.")
            return

        celsius_value.set(str((fahrenheit - 32) * 5 / 9))

    def convert_to_fahrenheit():
        try:
            celsius = float(celsius_value.get())
        except ValueError:
            messagebox.showerror("Invalid value", "Enter a valid Celsius temperature.")
            return

        fahrenheit_value.set(str(celsius * 9 / 5 + 32))

    tk.Label(window, text="Fahrenheit").grid(row=0, column=0, padx=8, pady=4)
    tk.Label(window, text="Celsius").grid(row=0, column=1, padx=8, pady=4)

    tk.Entry(window, textvariable=fahrenheit_value).grid(
        row=1, column=0, padx=8, pady=4
    )
    tk.Entry(window, textvariable=celsius_value).grid(
        row=1, column=1, padx=8, pady=4
    )

    tk.Button(window, text=">>>>", command=convert_to_celsius).grid(
        row=2, column=0, padx=8, pady=8
    )
    tk.Button(window, text="<<<<", command=convert_to_fahrenheit).grid(
        row=2, column=1, padx=8, pady=8
    )

    window.mainloop()


if __name__ == "__main__":
    main()
