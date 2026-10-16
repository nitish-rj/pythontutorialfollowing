import tkinter as tk
from tkinter import messagebox
import subprocess
shortcuts = {"Valorant": lambda: subprocess.Popen(r"C:\Users\Nitish\Desktop\dah\mpVALORANT.lnk", shell=True),
    "CK3": lambda: subprocess.Popen(r"D:\Crusader Kings 3\binaries\ck3.exe"),
    "Epic Games": lambda: subprocess.Popen(r"C:\Program Files (x86)\Epic Games\Launcher\Portal\Binaries\Win32\EpicGamesLauncher.exe"),
    "FC25": lambda: subprocess.Popen(r"D:\SteamLibrary\steamapps\common\EA SPORTS FC 25 Demo\FC25.exe"),
    "Brawlhalla": lambda: subprocess.Popen(r"C:\Users\Nitish\Desktop\dah\mpBrawlhalla.url", shell=True),
    "Minecraft": lambda: subprocess.Popen(r"C:\Users\Nitish\AppData\Roaming\.minecraft\TLauncher.exe"),
    "Risk of Rain 2": lambda: subprocess.Popen(r"C:\Risk of Rain 2\Risk of Rain 2.exe"),
    "Roblox": lambda: subprocess.Popen(r"C:\Users\Nitish\AppData\Local\Roblox\Versions\version-89b6c70d8f7f42ac\RobloxPlayerBeta.exe"),
    "Riot Client": lambda: subprocess.Popen(r"D:\Riot Games\Riot Client\RiotClientServices.exe"),
    "Skyrim SE": lambda: subprocess.Popen(r"D:\The Elder Scrolls V Skyrim Anniversary Edition\skse64_loader.exe"),
    "Steam": lambda: subprocess.Popen(r"C:\Program Files (x86)\Steam\steam.exe"),
    "Black Myth Wukong": lambda: subprocess.Popen(r"D:\BlackMythWukong\b1.exe"),
    "Cyberpunk 2077": lambda: subprocess.Popen(r"C:\Games\Cyberpunk 2077\bin\x64\Cyberpunk2077.exe"),
    "Mortal Kombat 11": lambda: subprocess.Popen(r"C:\Games\Mortal Kombat 11\Binaries\Retail\MK11.exe"),
    "Oblivion Remastered": lambda: subprocess.Popen(r"D:\The Elder Scrolls IV - Oblivion Remastered\OblivionRemastered.exe"),}
def center_window(win, width, height):
    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    win.geometry(f"{width}x{height}+{x}+{y}")
def run_action(action_name, root):
    try:
        action = shortcuts.get(action_name)
        if action:
            action()
            root.destroy()
        else:
            messagebox.showerror("Error", f"No action assigned to '{action_name}'")
    except Exception as e:
        messagebox.showerror("Execution Error", str(e))
def create_gui():
    root = tk.Tk()
    root.overrideredirect(True)
    window_width = 568
    window_height = 380
    center_window(root, window_width, window_height)
    root.configure(bg="#1e1e1e")
    def start_move(event):
        root.x_offset = event.x
        root.y_offset = event.y
    def on_move(event):
        x = event.x_root - root.x_offset
        y = event.y_root - root.y_offset
        root.geometry(f"+{x}+{y}")
    def on_close():
        root.destroy()
    title_bar = tk.Frame(root, bg="#444444", relief="raised", bd=0, height=30)
    title_bar.pack(fill=tk.X)
    title_label = tk.Label(title_bar,
        text="Games Hub",
        bg="#444444",
        fg="white",
        font=("Arial", 12, "bold"))
    title_label.pack(side=tk.TOP, fill=tk.X, expand=True)
    close_btn = tk.Button(title_bar,
        text="✕",
        bg="#444444",
        fg="white",
        borderwidth=0,
        font=("Arial", 12, "bold"),
        command=on_close,
        activebackground="#ff5555",
        activeforeground="white")
    close_btn.pack(side=tk.RIGHT, padx=5, pady=0)
    title_bar.bind("<ButtonPress-1>", start_move)
    title_bar.bind("<B1-Motion>", on_move)
    title_label.bind("<ButtonPress-1>", start_move)
    title_label.bind("<B1-Motion>", on_move)
    button_frame = tk.Frame(root, bg="#1e1e1e")
    button_frame.pack(expand=True, fill=tk.BOTH)
    columns = 3
    row = 0
    col = 0
    for name in shortcuts:
        btn = tk.Button(button_frame,
            text=name,
            width=20,
            height=2,
            command=lambda n=name: run_action(n, root),
            bg="#333333",
            fg="white",
            activebackground="#555555",
            activeforeground="white",
            relief="flat",
            font=("Arial", 10, "bold"))
        btn.grid(row=row, column=col, padx=10, pady=10)
        col += 1
        if col == columns:
            col = 0
            row += 1
    root.mainloop()
if __name__ == "__main__":
    create_gui()