import shutil
import os
from datetime import datetime
import tkinter as tk
from tkinter import messagebox

DOSSIERS_SOURCE = [
    (r"C:\F1000.DTA", r"Acomba\F1000.DTA"),
    (r"C:\Fortune",   r"Acomba\Fortune"),
    (r"C:\Users\Utilisateur\Documents", "Documents"),
    (r"C:\Users\Utilisateur\Pictures",  "Pictures")
]

DEST_BASE = r"D:\\"

def sauvegarder():
    try:
        date = datetime.now().strftime("%Y-%m-%d")
        dest = os.path.join(DEST_BASE, date)
        os.makedirs(dest, exist_ok=True)

        for source, nom_dest in DOSSIERS_SOURCE:
            shutil.copytree(source, os.path.join(dest, nom_dest), dirs_exist_ok=True)

        messagebox.showinfo("Sauvegarde", "Sauvegarde terminée avec succès.")
    except Exception as e:
        messagebox.showerror("Erreur", str(e))

app = tk.Tk()
app.title("Sauvegarde Maman")

btn = tk.Button(app, text="Sauvegarder mes dossiers", command=sauvegarder, height=2, width=30)
btn.pack(padx=70, pady=90)

app.mainloop()