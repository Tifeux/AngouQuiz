import tkinter as tk
from tkinter import messagebox
import random

# Liste des questions et réponses
all_questions = [
    {"question": "Quelle est la capitale de la BD en France ?", "answers": ["Angoulême", "Paris", "Lyon", "Marseille"], "correct": 0},
    {"question": "Quel festival célèbre la BD à Angoulême ?", "answers": ["Comic Con", "Festival d'Angoulême", "Japan Expo", "Salon du Livre"], "correct": 1},
    {"question": "Quel monument est célèbre à Angoulême ?", "answers": ["Tour Eiffel", "Cathédrale Saint-Pierre", "Mont Saint-Michel", "Château de Versailles"], "correct": 1},
    {"question": "Quel est le nom du musée de la BD à Angoulême ?", "answers": ["Musée de la BD", "Cité de la BD", "Maison de la BD", "Galerie de la BD"], "correct": 1},
    {"question": "Quel fleuve traverse Angoulême ?", "answers": ["La Seine", "La Loire", "La Charente", "Le Rhône"], "correct": 2},
    {"question": "Quel est le nom de l'équipe de basket-ball d'Angoulême ?", "answers": ["Angoulême Basket", "Charente Basket", "Les Dragons", "Les Lions"], "correct": 0},
    {"question": "Quel est le plat traditionnel de la région d'Angoulême ?", "answers": ["La choucroute", "La bouillabaisse", "Le cassoulet", "Le poulet à la charentaise"], "correct": 3},
    {"question": "Quel est le nom de la gare principale d'Angoulême ?", "answers": ["Gare d'Angoulême", "Gare Saint-Lazare", "Gare de Lyon", "Gare Montparnasse"], "correct": 0},
    {"question": "Quel est le nom du théâtre principal d'Angoulême ?", "answers": ["Théâtre d'Angoulême", "Théâtre des Quatre Saisons", "Théâtre National", "Théâtre de la Ville"], "correct": 0},
    {"question": "Quel est le nom du parc principal d'Angoulême ?", "answers": ["Parc de la Belle", "Parc de la Charente", "Parc de l'Hôtel de Ville", "Parc des Expositions"], "correct": 0},
    {"question": "Quel est le nom du cinéma principal d'Angoulême ?", "answers": ["Cinéma Le Nef", "Cinéma Le Palace", "Cinéma Le Mega CGR", "Cinéma Le Capitole"], "correct": 2},
    {"question": "Quel est le nom du stade principal d'Angoulême ?", "answers": ["Stade Chanzy", "Stade de France", "Stade Vélodrome", "Stade de la Mosson"], "correct": 0},
    {"question": "Quel est le nom du lycée principal d'Angoulême ?", "answers": ["Lycée Guez de Balzac", "Lycée de l'Image et du Son", "Lycée Charles de Gaulle", "Lycée Marguerite de Valois"], "correct": 0},
    {"question": "Quel est le nom de la bibliothèque principale d'Angoulême ?", "answers": ["Bibliothèque Municipale", "Bibliothèque Nationale", "Bibliothèque de l'Alpha", "Bibliothèque de la Cité"], "correct": 2},
    {"question": "Quel est le nom du marché principal d'Angoulême ?", "answers": ["Marché Victor Hugo", "Marché des Halles", "Marché Central", "Marché de la Place"], "correct": 1},
    {"question": "Quel est le nom de la piscine principale d'Angoulême ?", "answers": ["Piscine de Nautilis", "Piscine Municipale", "Piscine Olympique", "Piscine des Halles"], "correct": 0},
    {"question": "Quel est le nom du centre commercial principal d'Angoulême ?", "answers": ["Centre Commercial des Halles", "Centre Commercial de Champniers", "Centre Commercial de l'Houmeau", "Centre Commercial de la Belle"], "correct": 1},
    {"question": "Quel est le nom de la salle de concert principale d'Angoulême ?", "answers": ["La Nef", "Le Zénith", "L'Olympia", "Le Bataclan"], "correct": 0},
    {"question": "Quel est le nom du jardin botanique d'Angoulême ?", "answers": ["Jardin Vert", "Jardin des Plantes", "Jardin de l'Hôtel de Ville", "Jardin de la Belle"], "correct": 1},
    {"question": "Quel monument est célèbre à Angoulême ?", "answers": ["Tour Eiffel", "Cathédrale Saint-Pierre", "Mont Saint-Michel", "Château de Versailles"], "correct": 1},
    {"question": "Quel est le nom du musée de la BD à Angoulême ?", "answers": ["Musée de la BD", "Cité de la BD", "Maison de la BD", "Galerie de la BD"], "correct": 1},
    {"question": "Quel est le nom de l'équipe de rugby d'Angoulême ?", "answers": ["SA XV Charente", "Stade Rochelais", "Racing 92", "Toulouse Rugby"], "correct": 0},
    {"question": "Quel est le plat typique de la Charente ?", "answers": ["Gratin dauphinois", "Pineau des Charentes", "Bœuf bourguignon", "Aligot"], "correct": 1},
    {"question": "Quelle entreprise de cognac est basée près d'Angoulême ?", "answers": ["Hennessy", "Rémy Martin", "Martell", "Camus"], "correct": 2},
    {"question": "Quelle ligne de train relie Angoulême à Paris ?", "answers": ["TGV Atlantique", "TGV Méditerranée", "TER Nouvelle-Aquitaine", "TGV Est"], "correct": 0},
    {"question": "Quel célèbre écrivain a étudié à Angoulême ?", "answers": ["Victor Hugo", "Honoré de Balzac", "Gustave Flaubert", "Marcel Proust"], "correct": 1},
    {"question": "Quel parc est le plus connu d'Angoulême ?", "answers": ["Parc de l'Houmeau", "Parc de Frégeneuil", "Parc de la Belle", "Jardin Vert"], "correct": 3},
    {"question": "Quelle célèbre spécialité est produite en Charente ?", "answers": ["Champagne", "Cognac", "Calvados", "Armagnac"], "correct": 1},
    {"question": "Quel célèbre circuit automobile se déroule dans les rues d'Angoulême ?", "answers": ["24 Heures du Mans", "Grand Prix de Monaco", "Circuit des Remparts", "Rallye de Monte-Carlo"], "correct": 2},
    {"question": "Quel château se trouve près d'Angoulême ?", "answers": ["Château de Versailles", "Château de La Rochefoucauld", "Château de Chambord", "Château d'Amboise"], "correct": 1},
    {"question": "Quelle est l'université présente à Angoulême ?", "answers": ["Université de Bordeaux", "Université de Poitiers", "Université de La Rochelle", "Université de Limoges"], "correct": 1},
    {"question": "Quel célèbre auteur de BD est associé à Angoulême ?", "answers": ["Hergé", "Moebius", "Uderzo", "Jacques Tardi"], "correct": 3},
    {"question": "Quel est le code postal principal d'Angoulême ?", "answers": ["16000", "75000", "33000", "69000"], "correct": 0},
    {"question": "Quel est le nom du festival du film d'Angoulême ?", "answers": ["Festival de Cannes", "Festival Lumière", "Festival du Film Francophone", "Festival de Deauville"], "correct": 2},
    {"question": "Quel est l'autre nom d'Angoulême ?", "answers": ["La Perle du Sud", "Le Balcon du Sud-Ouest", "La Cité des Images", "La Ville Lumière"], "correct": 2},
]

def start_new_game():
    global questions, current_question, score
    if len(all_questions) < 20:
        messagebox.showerror("Erreur", "Il n'y a pas assez de questions pour commencer le quiz.")
        return
    questions = random.sample(all_questions, 20)
    current_question = 0
    score = 0
    display_question()

def check_answer(choice):
    global current_question, score
    if choice == questions[current_question]["correct"]:
        score += 1

    current_question += 1
    if current_question < len(questions):
        display_question()
    else:
        messagebox.showinfo("Quiz terminé", f"Votre score : {score}/{len(questions)}")
        root.quit()

def display_question():
    question_label.config(text=questions[current_question]["question"])
    for i in range(4):
        answer_buttons[i].config(text=questions[current_question]["answers"][i], command=lambda i=i: check_answer(i))

root = tk.Tk()
root.title("Quiz Angoulême")
root.geometry("600x400")
root.configure(bg="#f0f0f5")

question_label = tk.Label(root, text="", font=("Helvetica", 16, "bold"), bg="#f0f0f5", fg="#333", wraplength=550, justify="center")
question_label.pack(pady=30)

answer_buttons = []
for i in range(4):
    btn = tk.Button(root, text="", font=("Helvetica", 14), width=30, height=2, bg="#e0e0e0", fg="#333",
                    borderwidth=0, highlightthickness=0, relief="flat", activebackground="#d0d0d0")
    btn.pack(pady=10)
    answer_buttons.append(btn)

start_button = tk.Button(root, text="Commencer une nouvelle partie", font=("Helvetica", 14), bg="#4CAF50", fg="white",
                         borderwidth=0, highlightthickness=0, relief="flat", activebackground="#45a049", command=start_new_game)
start_button.pack(pady=20)

start_new_game()
root.mainloop()






