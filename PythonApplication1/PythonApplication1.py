import tkinter as tk
from tkinter import messagebox

fereastra = tk.Tk()
fereastra.title("X și 0")
fereastra.geometry("500x400")

# Functie impartire fereastra 
def update_frames(event=None):
    latime = fereastra.winfo_width()
    inaltime = fereastra.winfo_height()
    inaltime_sus = inaltime // 3
    inaltime_jos = inaltime - inaltime_sus
    sus.config(height=inaltime_sus)
    jos.config(height=inaltime_jos)


sus = tk.Frame(fereastra)
sus.pack(fill=tk.X, side=tk.TOP, expand=True)


jos = tk.Frame(fereastra)
jos.pack(fill=tk.BOTH, side=tk.BOTTOM, expand=True)

def verificare_linii_pline(butoane):
    contor = 0
    for i in range(9):
        if butoane[i]["text"] != "":
            contor += 1
    if contor == 9:
        messagebox.showinfo("Sfarsit joc", "Jocul s-a terminat la egalitate!")
        resetare_joc()

def resetare_joc():
    for buton in butoane:
        buton["text"] = ""
    activeaza_buton_sus(buton0)

def verificare_linii(butoane):
    for i in range(0, 3,6):
        if butoane[i]["text"] == butoane[i+1]["text"] == butoane[i+2]["text"] and butoane[i]["text"] != "":
            return butoane[i]["text"]
    for i in range(3):
        if butoane[i]["text"] == butoane[i+3]["text"] == butoane[i+6]["text"] and butoane[i]["text"] != "":
            return butoane[i]["text"]
    if butoane[0]["text"] == butoane[4]["text"] == butoane[8]["text"] and butoane[0]["text"] != "":
        return butoane[0]["text"]
    if butoane[2]["text"] == butoane[4]["text"] == butoane[6]["text"] and butoane[2]["text"] != "":
        return butoane[2]["text"]
    return None

def apasa_buton(buton):
    if buton["text"] == "":
        buton["text"] = buton_activ["text"]
        castigator = verificare_linii(butoane)
        if castigator:
            messagebox.showinfo("Avem un câștigător!", f"Jucătorul {castigator} a câștigat!")
            resetare_joc()
        else:
            verificare_linii_pline(butoane)
            activeaza_buton_sus(buton0 if buton_activ == butonX else butonX)

butoane = []
for i in range(9):
    buton = tk.Button(jos, text="")
    buton.config(command=lambda b=buton: apasa_buton(b))
    butoane.append(buton)
    row = i // 3
    column = i % 3
    buton.grid(row=row, column=column, sticky="nsew")

#redimensiune cele 9 butoane
for i in range(3):
    jos.grid_rowconfigure(i, weight=1)
    jos.grid_columnconfigure(i, weight=1)


buton0 = tk.Button(sus, text="0", command=lambda: activeaza_buton_sus(buton0))
butonX = tk.Button(sus, text="X", command=lambda: activeaza_buton_sus(butonX))


buton0.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
butonX.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")

buton_activ = None

def activeaza_buton_sus(buton):
    global buton_activ
    if buton_activ is not None:
        buton_activ.config(bg="SystemButtonFace")  
    buton.config(bg="LightBlue")
    buton_activ = buton


sus.grid_columnconfigure(0, weight=1)
sus.grid_columnconfigure(1, weight=1)
sus.grid_rowconfigure(0, weight=1)


update_frames()


fereastra.bind("<Configure>", update_frames)

fereastra.mainloop()
