import time
import json
import os 
import platform
import tkinter as tk
from tkinter import ttk, messagebox

def generate_device_info():
    start_time = time.time()
    dfw = 1.0
    w = dfw 


    if os.path.exists('dt.json'):
        try:
            with open('dt.json', 'r', encoding='utf-8') as f:
                oldw = json.load(f)
                w = oldw["metadata"]["Version"]
        except Exception:
            w = dfw


    w = round(w + 0.1, 1)
    end_time = time.time()
 
    data = {
        "metadata": {
            "Version": w,
            "Creator": "Kirassan"
        },
        "base": {
            "Time_init": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
            "Time_scwork": end_time - start_time,
            "OS": platform.system(),
        }
    }

    try:
        with open('dt.json', 'w', encoding='utf-8') as f:
            f.write(json.dumps(data, ensure_ascii=False, indent=4))
        return data
    except Exception as e:
        messagebox.showerror("Ошибка", f"Не удалось сохранить файл: {e}")
        return None

def on_click_generate():
    res = generate_device_info()
    
    if res:
        version_label.config(text=f"Версия: {res['metadata']['Version']}")
        os_label.config(text=f"Операционная система: {res['base']['OS']}")
        time_label.config(text=f"Время создания: {res['base']['Time_init']}")
        
        messagebox.showinfo("Успех", "Информация об устройстве успешно создана и сохранена в dt.json!")

root = tk.Tk()
root.title("Device Info Utility")
root.geometry("1024x768")
root.resizable(False, False)


style = ttk.Style()
style.theme_use('clam')
\
main_frame = ttk.Frame(root, padding="20 20 20 20")
main_frame.pack(fill=tk.BOTH, expand=True)

title_label = ttk.Label(main_frame, text="Системная Утилита", font=("Helvetica", 16, "bold"))
title_label.pack(pady=(0, 5))

creator_label = ttk.Label(main_frame, text="Создатель: Skafall", font=("Helvetica", 10, "italic"), foreground="gray")
creator_label.pack(pady=(0, 20))

separator = ttk.Separator(main_frame, orient='horizontal')
separator.pack(fill='x', pady=(0, 15))

info_frame = ttk.LabelFrame(main_frame, text=" Текущие данные ", padding="10 10 10 10")
info_frame.pack(fill='x', pady=(0, 20))

version_label = ttk.Label(info_frame, text="Версия: —", font=("Helvetica", 10))
version_label.pack(anchor='w', pady=2)

os_label = ttk.Label(info_frame, text="Операционная система: —", font=("Helvetica", 10))
os_label.pack(anchor='w', pady=2)

time_label = ttk.Label(info_frame, text="Время создания: —", font=("Helvetica", 10))
time_label.pack(anchor='w', pady=2)

generate_button = ttk.Button(
    main_frame, 
    text="Создать информацию об устройстве", 
    command=on_click_generate
)
generate_button.pack(fill='x', ipady=5)

root.mainloop()