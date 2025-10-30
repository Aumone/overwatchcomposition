from random import randint
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os

# Dossier racine du script
BASE_DIR = r"C:\Users\utilisateur\Desktop\Overwatch compo\images"
ICON_DIR = os.path.join(BASE_DIR, "icon")
HERO_DIR = os.path.join(BASE_DIR, "heros")

# DIVE COMP
dive_tank = ["DVA","Bouldozer", "Winston", "Doomfist"]
dive_flex_dps = ["Tracer","Sombra", "Genji", "Reaper","Venture"]
dive_hitscan = ["Cassidy","Freja","Sojourn"]
dive_main_heal = ["Lucio", "Wuyang"]
dive_flex_heal = ["Kiriko", "Wuyang", "Juno"]

# POKE COMP
poke_tank = ["Sigma","Orisa","Ramattra"]
poke_flex_dps = ["Pharah", "Sojourn", "Torbjorn","Soldier"]
poke_hitscan = ["Ashe","Freja","Widowmaker","Hanzo"]
poke_main_heal = ["Ana", "Wuyang","Baptiste"]
poke_flex_heal = ["Zenyatta", "Kiriko", "Ana","Illari"]

# BRAWL COMP
brawl_tank = ["Zarya","Reinhardt","Ramattra","Roadhog", "Sigma"]
brawl_flex_dps = ["Tracer", "Sombra", "Genji","Mei","Reaper"]
brawl_hitscan = ["Sojourn","Soldier","Symmetra","Bastion"]
brawl_main_heal = ["Lucio", "Wuyang", "Brigitte"]
brawl_flex_heal = ["Wuyang", "Kiriko", "Juno", "Mercy"]

rush_tank = ["Mauga", "Junker Queen"]
rush_flex_dps = ["Tracer", "Sombra", "Genji","Reaper"]
rush_hitscan = ["Sojourn","Soldier","Bastion"]
rush_main_heal = ["Lucio", "Wuyang","Bastiste"]
rush_flex_heal = ["Kiriko", "Juno"]

def generer_compo(compo):
    if compo == "Brawl":
        tank = brawl_tank[randint(0, len(brawl_tank)-1)]
        flex_dps = brawl_flex_dps[randint(0, len(brawl_flex_dps)-1)]
        hitscan = brawl_hitscan[randint(0, len(brawl_hitscan)-1)]
        main_heal = brawl_main_heal[randint(0, len(brawl_main_heal)-1)]
        flex_heal = brawl_flex_heal[randint(0, len(brawl_flex_heal)-1)]
        while flex_heal == main_heal:
            flex_heal = brawl_flex_heal[randint(0, len(brawl_flex_heal)-1)]
    elif compo == "Poke":
        tank = poke_tank[randint(0, len(poke_tank)-1)]
        flex_dps = poke_flex_dps[randint(0, len(poke_flex_dps)-1)]
        hitscan = poke_hitscan[randint(0, len(poke_hitscan)-1)]
        main_heal = poke_main_heal[randint(0, len(poke_main_heal)-1)]
        flex_heal = poke_flex_heal[randint(0, len(poke_flex_heal)-1)]
        while flex_heal == main_heal:
            flex_heal = poke_flex_heal[randint(0, len(poke_flex_heal)-1)]
    elif compo == "Dive":
        tank = dive_tank[randint(0, len(dive_tank)-1)]
        flex_dps = dive_flex_dps[randint(0, len(dive_flex_dps)-1)]
        hitscan = dive_hitscan[randint(0, len(dive_hitscan)-1)]
        main_heal = dive_main_heal[randint(0, len(dive_main_heal)-1)]
        flex_heal = dive_flex_heal[randint(0, len(dive_flex_heal)-1)]
        while flex_heal == main_heal:
            flex_heal = dive_flex_heal[randint(0, len(dive_flex_heal)-1)]
    else:
        tank = rush_tank[randint(0, len(rush_tank)-1)]
        flex_dps = rush_flex_dps[randint(0, len(rush_flex_dps)-1)]
        hitscan = rush_hitscan[randint(0, len(rush_hitscan)-1)]
        main_heal = rush_main_heal[randint(0, len(rush_main_heal)-1)]
        flex_heal = rush_flex_heal[randint(0, len(rush_flex_heal)-1)]
        while flex_heal == main_heal:
            flex_heal = dive_flex_heal[randint(0, len(dive_flex_heal)-1)]
    return tank, flex_dps, hitscan, main_heal, flex_heal


def charger_image(chemin, taille=(120,120)):
    if os.path.exists(chemin):
        img = Image.open(chemin).resize(taille)
        return ImageTk.PhotoImage(img)
    else:
        print(f"❌ Image introuvable: {chemin}")
        return None


def afficher_resultat():
    compo = combo_compo.get()
    tank, flex_dps, hitscan, main_heal, flex_heal = generer_compo(compo)
    equipe = [
        ("Tank", tank, "tank.png"),
        ("Flex DPS", flex_dps, "dps.png"),
        ("Hitscan", hitscan, "dps.png"),
        ("Main Heal", main_heal, "support.png"),
        ("Flex Heal", flex_heal, "support.png")
    ]

    for i, (role, hero, icon) in enumerate(equipe):
        icone_path = os.path.join(ICON_DIR, icon)
        hero_path = os.path.join(HERO_DIR, f"{hero}.png")

        icone = charger_image(icone_path, (60,60))
        if icone:
            labels_role[i].config(image=icone, text=role, compound="left")
            labels_role[i].image = icone
        else:
            labels_role[i].config(text=role)

        hero_img = charger_image(hero_path)
        if hero_img:
            labels_hero[i].config(image=hero_img, text="")
            labels_hero[i].image = hero_img
        else:
            labels_hero[i].config(text=hero, fg="white", font=("Arial", 15, "bold"))


# Interface TKINTER
fenetre = tk.Tk()
fenetre.title("Overwatch 2 - Générateur de compositions")
fenetre.geometry("1920x1080")

bg_path = os.path.join(BASE_DIR, "fond.jpg")
if os.path.exists(bg_path):
    bg_img = Image.open(bg_path).resize((1920,1080))
    fond_photo = ImageTk.PhotoImage(bg_img)
    label_fond = tk.Label(fenetre, image=fond_photo)
    label_fond.place(x=0, y=0, relwidth=1, relheight=1)
else:
    fenetre.config(bg="#1c1f26")

titre = tk.Label(
    fenetre,
    text=" Sélecteur de composition Overwatch 2 ",
    bg="#1c1f26",
    fg="white",
    font=("Orbitron", 18, "bold")
)
titre.pack(pady=20)

combo_compo = ttk.Combobox(fenetre, values=["Brawl","Poke","Dive","Rush"], state="readonly", font=("Arial",14))
combo_compo.current(0)
combo_compo.pack(pady=10)

btn_generer = tk.Button(
    fenetre,
    text="🔁 Générer la composition",
    command=afficher_resultat,
    bg="#ff9c00",
    fg="black",
    font=("Arial", 14, "bold"),
    relief="flat",
    padx=10,
    pady=5
)
btn_generer.pack(pady=15)

cadre = tk.Frame(fenetre, bg="#2b2f38")
cadre.pack(pady=30)

labels_role = []
labels_hero = []

for i in range(5):
    lbl_role = tk.Label(cadre, text="", bg="#2b2f38", fg="white", font=("Arial",13))
    lbl_role.grid(row=i, column=0, padx=20, pady=15, sticky="w")
    lbl_hero = tk.Label(cadre, bg="#2b2f38")
    lbl_hero.grid(row=i, column=1, padx=10, pady=15)
    labels_role.append(lbl_role)
    labels_hero.append(lbl_hero)

fenetre.mainloop()
