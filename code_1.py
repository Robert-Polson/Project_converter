import tkinter as tk

from tkinter import filedialog

import pandas as pd

def convert_to_json():

    file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx")])

    if file_path:

        df = pd.read_excel(file_path)

        json_file_path = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON files", "*.json")])

        if json_file_path:

            df.to_json(json_file_path, orient='records', force_ascii=False, lines=True, default_handler=str)

            status_label.config(text="Conversion successful!")


# Создание графической оболочки

root = tk.Tk()

root.title("Excel to JSON Converter")


# Кнопка для выбора файла и конвертации

convert_button = tk.Button(root, text="Convert to JSON", command=convert_to_json)

convert_button.pack(pady=20)


# Метка для отображения статуса конвертации

status_label = tk.Label(root, text="")

status_label.pack()


root.mainloop()