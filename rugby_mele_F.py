import numpy as np
import math as mh
import matplotlib.pyplot as plt
import tkinter as tk

pas_de_temps = 0.01  # pas de temps pour la simulation
temps_total = 3.0  # temps total de simulation
nombre_de_pas = int(temps_total / pas_de_temps)


# Definition de la classe Joueur
class Joueur:
    def __init__(self, orteils, chevilles, hanches, genoux, epaules, taille, masse, force_initiale):
        self.orteils = np.array(orteils)
        self.chevilles = np.array(chevilles)
        self.hanches = np.array(hanches)
        self.genoux = np.array(genoux)
        self.epaules = np.array(epaules)
        self.taille = taille
        self.masse = masse
        self.force_initiale = force_initiale * masse / 90
        self.vitesse = np.zeros(2)  # vitesse initiale de 0
        self.position = (self.hanches + self.epaules) / 2  # Position initiale comme point median
        self.positions = [self.position.copy()]
        self.vec_chevilles_orteils = self.chevilles - self.orteils
        self.vec_genoux_chevilles = self.genoux - self.chevilles
        self.vec_hanches_genoux = self.hanches - self.genoux
        self.vec_epaules_hanches = self.epaules - self.hanches

    def calculer_angles(self):
        ab = mh.sqrt((self.chevilles[0]- self.orteils[0])**2 + (self.chevilles[1]- self.orteils[1])**2)
        bc = mh.sqrt((self.genoux[0]- self.chevilles[0])**2 + (self.genoux[1]- self.chevilles[1])**2)
        ca = mh.sqrt((self.orteils[0]- self.genoux[0])**2 + (self.orteils[1]- self.genoux[1])**2)
        
        self.angle_pied = mh.acos((bc**2 + ab**2 - ca**2) / (2 * bc * ab))
        
        ab2 = mh.sqrt((self.genoux[0]- self.chevilles[0])**2 + (self.genoux[1]- self.chevilles[1])**2)
        bc2 = mh.sqrt((self.hanches[0]- self.genoux[0])**2 + (self.hanches[1]- self.genoux[1])**2)
        ca2 = mh.sqrt((self.chevilles[0] - self.hanches[0] )**2 + (self.chevilles[1] - self.hanches[1])**2)
        
        self.angle_jambe = mh.acos((bc2**2 + ab2**2 - ca2**2) / (2 * bc2 * ab2))
        
        ab3 = mh.sqrt((self.hanches[0]- self.genoux[0])**2 + (self.hanches[1]- self.genoux[1])**2)
        bc3 = mh.sqrt((self.epaules[0]- self.hanches[0])**2 + (self.epaules[1]- self.hanches[1])**2)
        ca3 = mh.sqrt((self.genoux[0]- self.epaules[0])**2 + (self.genoux[1]- self.epaules[1])**2)
        
        self.angle_torse = mh.acos((bc3**2 + ab3**2 - ca3**2) / (2 * bc3 * ab3))
        
        
        


# Fonction pour simuler le ruck
def simuler_ruck(joueur1, joueur2,fx1,fy1,fx2,fy2):

    joueur1.calculer_angles()
    joueur2.calculer_angles()
   
    forces_resultantes_x = fx1 - fx2
    forces_resultantes_y = fy1 - fy2
    
    # si la magnitude est petite c'est bon
    magnitude = round(mh.sqrt((forces_resultantes_x)**2 + (forces_resultantes_y)**2), 3)
    # nous voulons peut-être proche de zero pour horizontal
    direction = round(mh.degrees(mh.atan(forces_resultantes_y / forces_resultantes_x)), 4)
    
    # Determiner le gagnant en fonction du mouvement vers l'arrière
    if direction >= 1 and magnitude >= 100:
        gagnant = "Le Joueur 1 gagne le ruck"
    elif direction <= -1 and magnitude >= 100:
        gagnant = "Le Joueur 2 gagne le ruck"
    else:
        gagnant = "C'est un match nul"
        
    return gagnant, forces_resultantes_x, forces_resultantes_y, magnitude, direction

# Fonction pour normaliser et definir une longueur specifique pour les flèches
def definir_longueur_fleche(fx, fy, longueur):
    magnitude = np.sqrt(fx**2 + fy**2)
    echelle = longueur / magnitude
    return fx * echelle, fy * echelle

# Function to calculate the angle between two vectors
def angle_between(v1, v2):
    dot_product = np.dot(v1, v2)
    magnitude_v1 = np.linalg.norm(v1)
    magnitude_v2 = np.linalg.norm(v2)
    cosine_angle = dot_product / (magnitude_v1 * magnitude_v2)
    angle = np.arccos(np.clip(cosine_angle, -1.0, 1.0))
    return np.degrees(angle)

def utiliser_valeur_exemple1():
    orteils1 = np.array([0, 0])
    chevilles1 = np.array([0.02, 0.07])
    genoux1 = np.array([0.5, 0.075])
    hanches1 = np.array([0.75, 0.225])
    epaules1 = np.array([1.45, 0.225])
    taille1 = 1.65
    masse1 = 95
    force_initiale1 = 2000
    
    x1.delete(0, tk.END)
    x1.insert(0, orteils1[0])
    y1.delete(0, tk.END)
    y1.insert(0, orteils1[1])

    x2.delete(0, tk.END)
    x2.insert(0, chevilles1[0])
    y2.delete(0, tk.END)
    y2.insert(0, chevilles1[1])

    x3.delete(0, tk.END)
    x3.insert(0, genoux1[0])
    y3.delete(0, tk.END)
    y3.insert(0, genoux1[1])

    x4.delete(0, tk.END)
    x4.insert(0, hanches1[0])
    y4.delete(0, tk.END)
    y4.insert(0, hanches1[1])

    x5.delete(0, tk.END)
    x5.insert(0, epaules1[0])
    y5.delete(0, tk.END)
    y5.insert(0, epaules1[1])

    x6.delete(0, tk.END)
    x6.insert(0, masse1)

    x7.delete(0, tk.END)
    x7.insert(0, taille1)

    x8.delete(0, tk.END)
    x8.insert(0, force_initiale1)
    
    utiliser_valeur_exemple2()



def utiliser_valeur_exemple2():
    orteils2 = np.array([0, 0])
    chevilles2 = np.array([0.0, 0.07])
    genoux2 = np.array([0.5, 0.075])
    hanches2 = np.array([0.95, 0.18])
    epaules2 = np.array([1.55, 0.23])
    taille2 = 1.60
    masse2 = 95
    force_initiale2 = 2000
    
    vx1.delete(0, tk.END)
    vx1.insert(0, orteils2[0])
    vy1.delete(0, tk.END)
    vy1.insert(0, orteils2[1])

    vx2.delete(0, tk.END)
    vx2.insert(0, chevilles2[0])
    vy2.delete(0, tk.END)
    vy2.insert(0, chevilles2[1])

    vx3.delete(0, tk.END)
    vx3.insert(0, genoux2[0])
    vy3.delete(0, tk.END)
    vy3.insert(0, genoux2[1])

    vx4.delete(0, tk.END)
    vx4.insert(0, hanches2[0])
    vy4.delete(0, tk.END)
    vy4.insert(0, hanches2[1])

    vx5.delete(0, tk.END)
    vx5.insert(0, epaules2[0])
    vy5.delete(0, tk.END)
    vy5.insert(0, epaules2[1])

    vx6.delete(0, tk.END)
    vx6.insert(0, masse2)

    vx7.delete(0, tk.END)
    vx7.insert(0, taille2)

    vx8.delete(0, tk.END)
    vx8.insert(0, force_initiale2)

def simuler_mele():
    orteils1 = [float(x1.get()), float(y1.get())]
    chevilles1 = [float(x2.get()), float(y2.get())]
    genoux1 = [float(x3.get()), float(y3.get())]
    hanches1 = [float(x4.get()), float(y4.get())]
    epaules1 = [float(x5.get()), float(y5.get())]
    taille1 = float(x7.get())
    masse1 = float(x6.get())
    force_initiale1 = float(x8.get())
    
    orteils2 = [float(vx1.get()), float(vy1.get())]
    chevilles2 = [float(vx2.get()), float(vy2.get())]
    genoux2 = [float(vx3.get()), float(vy3.get())]
    hanches2 = [float(vx4.get()), float(vy4.get())]
    epaules2 = [float(vx5.get()), float(vy5.get())]
    taille2 = float(vx7.get())
    masse2 = float(vx6.get())
    force_initiale2 = float(vx8.get())
    
    joueur1 = Joueur(orteils1, chevilles1, hanches1, genoux1, epaules1, taille1, masse1, force_initiale1)
    joueur2 = Joueur(orteils2, chevilles2, hanches2, genoux2, epaules2, taille2, masse2, force_initiale2)

    
    # Force vector (assuming horizontal push from shoulders)
    force_vector = np.array([1, 0])

    resultant_vector1 = joueur1.vec_epaules_hanches + joueur1.vec_hanches_genoux + joueur1.vec_genoux_chevilles
    normalized_resultant_vector1 = resultant_vector1 / np.linalg.norm(resultant_vector1)
    angle_effectif1 = angle_between(normalized_resultant_vector1, force_vector)
                                            
    resultant_vector2 = joueur2.vec_epaules_hanches + joueur2.vec_hanches_genoux + joueur2.vec_genoux_chevilles
    normalized_resultant_vector2 = resultant_vector2 / np.linalg.norm(resultant_vector2)
    angle_effectif2 = angle_between(normalized_resultant_vector2, force_vector)

    fx1 = round(joueur1.force_initiale * mh.cos(angle_effectif1), 4)
    fy1 = round(joueur1.force_initiale * mh.sin(angle_effectif1), 4)

    fx2 = round(joueur2.force_initiale * mh.cos(angle_effectif2), 4)
    fy2 = round(joueur2.force_initiale * mh.sin(angle_effectif2), 4)

    # Executer la simulation
    gagnant, forces_x, forces_y, magnitude, direction = simuler_ruck(joueur1, joueur2,fx1,fy1,fx2,fy2)

    # Imprimer les resultats
    print(gagnant, "\n")
    print("Score des metriques du Joueur 1 :")
    print("Angle pied: ",round(mh.degrees(joueur1.angle_pied),3),"D")
    print("Angle jambe: ",round(mh.degrees(joueur1.angle_jambe),3),"D")
    print("Angle torse: ",round(mh.degrees(joueur1.angle_torse),3),"D")
    print("Force horizontale :", fx1, "N")
    print("Force verticale :", fy1, "N\n")

    print("Score des metriques du Joueur 2 :")
    print("Angle pied: ",round(mh.degrees(joueur2.angle_pied),3),"D")
    print("Angle jambe: ",round(mh.degrees(joueur2.angle_jambe),3),"D")
    print("Angle torse: ",round(mh.degrees(joueur2.angle_torse),3),"D")
    print("Force horizontale :", fx2, "N")
    print("Force verticale :", fy2, "N\n")
    if forces_x > 0 :
        print("Forces horizontales totales :", round(forces_x, 4), "N vers la droite")
    else:
        print("Forces horizontales totales :", abs(round(forces_x, 4)), "N vers la gauche")
    print("Forces verticales totales :", round(forces_y, 4), "N")
    print("Force restante :", magnitude, "N")
    print("Direction de la force restante :", direction, "D ")


    # Definir la longueur souhaitee des flèches
    longueur_fleche = 0.5  # Longueur d'exemple

    # Calculer les composantes des flèches mises à l'echelle
    joueur1_fx_mise_echelle, joueur1_fy_mise_echelle = definir_longueur_fleche(fx1, fy1, longueur_fleche)
    joueur2_fx_mise_echelle, joueur2_fy_mise_echelle = definir_longueur_fleche(fx2, fy2, longueur_fleche)
    resultante_fx_mise_echelle, resultante_fy_mise_echelle = definir_longueur_fleche(forces_x, forces_y, longueur_fleche)

    # Calcul pour le joueur 2
    axe_miroir = max(joueur1.taille,joueur2.taille)
    orteils2_miroir = [2 * axe_miroir - x for x in orteils2]
    chevilles2_miroir = [2 * axe_miroir - x for x in chevilles2]
    genoux2_miroir = [2 * axe_miroir - x for x in genoux2]
    hanches2_miroir = [2 * axe_miroir - x for x in hanches2]
    epaules2_miroir = [2 * axe_miroir - x for x in epaules2]

    # Tracer les resultats
    fig, ax = plt.subplots()

    print("X:",joueur1.orteils[0], joueur1.chevilles[0], joueur1.genoux[0], joueur1.hanches[0], joueur1.epaules[0])
    print("Y:", joueur1.orteils[1], joueur1.chevilles[1], joueur1.genoux[1], joueur1.hanches[1], joueur1.epaules[1])
    # Tracer les positions du joueur 1
    ax.plot([joueur1.orteils[0], joueur1.chevilles[0], joueur1.genoux[0], joueur1.hanches[0], joueur1.epaules[0]],
            [joueur1.orteils[1], joueur1.chevilles[1], joueur1.genoux[1], joueur1.hanches[1], joueur1.epaules[1]], 'bo-', label='Joueur 1')

    # Marquer chaque articulation pour le Joueur 1
    ax.plot(joueur1.orteils[0], joueur1.orteils[1], 'bo')
    ax.plot(joueur1.chevilles[0], joueur1.chevilles[1], 'bo')
    ax.plot(joueur1.genoux[0], joueur1.genoux[1], 'bo')
    ax.plot(joueur1.hanches[0], joueur1.hanches[1], 'bo')
    ax.plot(joueur1.epaules[0], joueur1.epaules[1], 'bo')

    # Tracer les positions du joueur 2
    ax.plot([joueur2.orteils[0], joueur2.chevilles[0], joueur2.genoux[0], joueur2.hanches[0], joueur2.epaules[0]],
            [joueur2.orteils[1], joueur2.chevilles[1], joueur2.genoux[1], joueur2.hanches[1], joueur2.epaules[1]], 'ro-', label='Joueur 2')

    # Marquer chaque articulation pour le Joueur 2
    ax.plot(joueur2.orteils[0], joueur2.orteils[1], 'ro')
    ax.plot(joueur2.chevilles[0], joueur2.chevilles[1], 'ro')
    ax.plot(joueur2.genoux[0], joueur2.genoux[1], 'ro')
    ax.plot(joueur2.hanches[0], joueur2.hanches[1], 'ro')
    ax.plot(joueur2.epaules[0], joueur2.epaules[1], 'ro')

    # Tracer les vecteurs de force separement
    ax.arrow(joueur1.epaules[0], joueur1.epaules[1], joueur1_fx_mise_echelle, joueur1_fy_mise_echelle, head_width=0.05, head_length=0.1, fc='blue', ec='blue', label='Force du Joueur 1')
    ax.arrow(joueur2.epaules[0], joueur2.epaules[1], joueur2_fx_mise_echelle, joueur2_fy_mise_echelle, head_width=0.05, head_length=0.1, fc='red', ec='red', label='Force du Joueur 2')

    # Tracer le vecteur de force resultante
    resultante_x = (joueur1.epaules[0] + joueur2.epaules[0]) / 2
    resultante_y = (joueur1.epaules[1] + joueur2.epaules[1]) / 2
    ax.arrow(resultante_x, resultante_y, resultante_fx_mise_echelle, resultante_fy_mise_echelle, head_width=0.05, head_length=0.1, fc='green', ec='green', label='Force resultante')

    # Annoter les articulations
    ax.annotate('Orteils', (joueur1.orteils[0], joueur1.orteils[1]), textcoords="offset points", xytext=(-10,5), ha='center', color='blue')
    ax.annotate('Chevilles', (joueur1.chevilles[0], joueur1.chevilles[1]), textcoords="offset points", xytext=(-10,5), ha='center', color='blue')
    ax.annotate('Genoux', (joueur1.genoux[0], joueur1.genoux[1]), textcoords="offset points", xytext=(-10,5), ha='center', color='blue')
    ax.annotate('Hanches', (joueur1.hanches[0], joueur1.hanches[1]), textcoords="offset points", xytext=(-10,5), ha='center', color='blue')
    ax.annotate('epaules', (joueur1.epaules[0], joueur1.epaules[1]), textcoords="offset points", xytext=(-10,5), ha='center', color='blue')

    ax.annotate('Orteils', (joueur2.orteils[0], joueur2.orteils[1]), textcoords="offset points", xytext=(-10,5), ha='center', color='red')
    ax.annotate('Chevilles', (joueur2.chevilles[0], joueur2.chevilles[1]), textcoords="offset points", xytext=(-10,5), ha='center', color='red')
    ax.annotate('Genoux', (joueur2.genoux[0], joueur2.genoux[1]), textcoords="offset points", xytext=(-10,5), ha='center', color='red')
    ax.annotate('Hanches', (joueur2.hanches[0], joueur2.hanches[1]), textcoords="offset points", xytext=(-10,5), ha='center', color='red')
    ax.annotate('epaules', (joueur2.epaules[0], joueur2.epaules[1]), textcoords="offset points", xytext=(-10,5), ha='center', color='red')

    # Definir les limites de la trame et les etiquettes
    ax.set_xlim(-0.2, 2.5)
    ax.set_ylim(-0.05, 0.9)
    ax.set_xlabel('Position X (m)')
    ax.set_ylabel('Position Y (m)')
    ax.set_title('Forces de la mêlee de rugby')
    ax.legend()
    plt.grid()

    fig, bx = plt.subplots()

    # Tracer les positions du joueur 1
    bx.plot([joueur1.orteils[0], joueur1.chevilles[0], joueur1.genoux[0], joueur1.hanches[0], joueur1.epaules[0]],
            [joueur1.orteils[1], joueur1.chevilles[1], joueur1.genoux[1], joueur1.hanches[1], joueur1.epaules[1]], 'bo-', label='Joueur 1')

    # Marquer chaque articulation pour le Joueur 1
    bx.plot(joueur1.orteils[0], joueur1.orteils[1], 'bo')
    bx.plot(joueur1.chevilles[0], joueur1.chevilles[1], 'bo')
    bx.plot(joueur1.genoux[0], joueur1.genoux[1], 'bo')
    bx.plot(joueur1.hanches[0], joueur1.hanches[1], 'bo')
    bx.plot(joueur1.epaules[0], joueur1.epaules[1], 'bo')

    # Tracer les positions du joueur 2 (miroir)
    bx.plot([orteils2_miroir[0], chevilles2_miroir[0], genoux2_miroir[0], hanches2_miroir[0], epaules2_miroir[0]],
            [orteils2[1], chevilles2[1], genoux2[1], hanches2[1], epaules2[1]], 'ro-', label='Joueur 2')

    # Marquer chaque articulation pour le Joueur 2 (miroir)
    bx.plot(orteils2_miroir[0], orteils2[1], 'ro')
    bx.plot(chevilles2_miroir[0], chevilles2[1], 'ro')
    bx.plot(genoux2_miroir[0], genoux2[1], 'ro')
    bx.plot(hanches2_miroir[0], hanches2[1], 'ro')
    bx.plot(epaules2_miroir[0], epaules2[1], 'ro')

    # Tracer les vecteurs de force separement pour le Joueur 2 (miroir)
    bx.arrow(joueur1.epaules[0], joueur1.epaules[1], joueur1_fx_mise_echelle, joueur1_fy_mise_echelle, head_width=0.05, head_length=0.1, fc='cyan', ec='cyan', label='Force du Joueur 1')
    bx.arrow(epaules2_miroir[0], epaules2[1], -joueur2_fx_mise_echelle, joueur2_fy_mise_echelle, head_width=0.05, head_length=0.1, fc='orange', ec='orange', label='Force du Joueur 2')

    # Tracer le vecteur de force resultante
    resultante_x = (joueur1.epaules[0] + epaules2_miroir[0]) / 2
    resultante_y = (joueur1.epaules[1] + epaules2[1]) / 2
    bx.arrow(resultante_x, resultante_y, resultante_fx_mise_echelle, resultante_fy_mise_echelle, head_width=0.05, head_length=0.1, fc='green', ec='green', label='Force resultante')

    # Annoter les articulations
    bx.annotate('Orteils', (joueur1.orteils[0], joueur1.orteils[1]), textcoords="offset points", xytext=(-10,5), ha='center', color='blue')
    bx.annotate('Chevilles', (joueur1.chevilles[0], joueur1.chevilles[1]), textcoords="offset points", xytext=(-10,5), ha='center', color='blue')
    bx.annotate('Genoux', (joueur1.genoux[0], joueur1.genoux[1]), textcoords="offset points", xytext=(-10,5), ha='center', color='blue')
    bx.annotate('Hanches', (joueur1.hanches[0], joueur1.hanches[1]), textcoords="offset points", xytext=(-10,5), ha='center', color='blue')
    bx.annotate('epaules', (joueur1.epaules[0], joueur1.epaules[1]), textcoords="offset points", xytext=(-10,5), ha='center', color='blue')

    bx.annotate('Orteils', (orteils2_miroir[0], orteils2[1]), textcoords="offset points", xytext=(-10,5), ha='center', color='red')
    bx.annotate('Chevilles', (chevilles2_miroir[0], chevilles2[1]), textcoords="offset points", xytext=(-10,5), ha='center', color='red')
    bx.annotate('Genoux', (genoux2_miroir[0], genoux2[1]), textcoords="offset points", xytext=(-10,5), ha='center', color='red')
    bx.annotate('Hanches', (hanches2_miroir[0], hanches2[1]), textcoords="offset points", xytext=(-10,5), ha='center', color='red')
    bx.annotate('epaules', (epaules2_miroir[0], epaules2[1]), textcoords="offset points", xytext=(-10,5), ha='center', color='red')

    # Definir les limites de la trame et les etiquettes
    bx.set_xlim(-0.2, 3.5)
    bx.set_ylim(-0.05, 0.9)
    bx.set_xlabel('Position X')
    bx.set_ylabel('Position Y')
    bx.set_title('Forces de la mêlee de rugby')
    bx.legend()

    plt.grid()
    plt.show()
    

def clear_all_entries(entries):
    for entry in entries:
        entry.delete(0, tk.END)

root = tk.Tk()
root.title("Comparateur de joueur en mêlée")

soustitre = tk.Label(root, text='Entrer les coordonées des articulations :')
soustitre.grid(row=0, column=0, columnspan=3, pady=(10, 20))

x = tk.Label(root, text='X')
x.grid(row=1, column=1)

y = tk.Label(root, text='Y')
y.grid(row=1, column=2)

xp2 = tk.Label(root, text='X')
xp2.grid(row=1, column=4)

yp2 = tk.Label(root, text='Y')
yp2.grid(row=1, column=5)

toe = tk.Label(root, text='Coordonées de doigt de pied')
toe.grid(row=2, column=0, padx=10, pady=5, sticky='w')

x1 = tk.Entry(root)
x1.grid(row=2, column=1, padx=10, pady=5)

y1 = tk.Entry(root)
y1.grid(row=2, column=2, padx=10, pady=5)

vx1 = tk.Entry(root)
vx1.grid(row=2, column=4, padx=10, pady=5)

vy1 = tk.Entry(root)
vy1.grid(row=2, column=5, padx=10, pady=5)

ankle = tk.Label(root, text='Coordonées de cheville')
ankle.grid(row=3, column=0, padx=10, pady=5, sticky='w')

x2 = tk.Entry(root)
x2.grid(row=3, column=1, padx=10, pady=5)

y2 = tk.Entry(root)
y2.grid(row=3, column=2, padx=10, pady=5)

vx2 = tk.Entry(root)
vx2.grid(row=3, column=4, padx=10, pady=5)

vy2 = tk.Entry(root)
vy2.grid(row=3, column=5, padx=10, pady=5)

knee = tk.Label(root, text='Coordonées de genoux')
knee.grid(row=4, column=0, padx=10, pady=5, sticky='w')

x3 = tk.Entry(root)
x3.grid(row=4, column=1, padx=10, pady=5)

y3 = tk.Entry(root)
y3.grid(row=4, column=2, padx=10, pady=5)

vx3 = tk.Entry(root)
vx3.grid(row=4, column=4, padx=10, pady=5)

vy3 = tk.Entry(root)
vy3.grid(row=4, column=5, padx=10, pady=5)

hip = tk.Label(root, text='Coordonées de hanche')
hip.grid(row=5, column=0, padx=10, pady=5, sticky='w')

x4 = tk.Entry(root)
x4.grid(row=5, column=1, padx=10, pady=5)

y4 = tk.Entry(root)
y4.grid(row=5, column=2, padx=10, pady=5)

vx4 = tk.Entry(root)
vx4.grid(row=5, column=4, padx=10, pady=5)

vy4 = tk.Entry(root)
vy4.grid(row=5, column=5, padx=10, pady=5)

shoulders = tk.Label(root, text='Coordonées d\'épaule')
shoulders.grid(row=6, column=0, padx=10, pady=5, sticky='w')

x5 = tk.Entry(root)
x5.grid(row=6, column=1, padx=10, pady=5)

y5 = tk.Entry(root)
y5.grid(row=6, column=2, padx=10, pady=5)

vx5 = tk.Entry(root)
vx5.grid(row=6, column=4, padx=10, pady=5)

vy5 = tk.Entry(root)
vy5.grid(row=6, column=5, padx=10, pady=5)

weight = tk.Label(root, text='Poids')
weight.grid(row=7, column=0, padx=10, pady=5, sticky='w')

x6 = tk.Entry(root)
x6.grid(row=7, column=1, padx=10, pady=5)

vx6 = tk.Entry(root)
vx6.grid(row=7, column=4, padx=10, pady=5)

size = tk.Label(root, text='Taille')
size.grid(row=8, column=0, padx=10, pady=5, sticky='w')

x7 = tk.Entry(root)
x7.grid(row=8, column=1, padx=10, pady=5)

vx7 = tk.Entry(root)
vx7.grid(row=8, column=4, padx=10, pady=5)

impulse = tk.Label(root, text='Impulsion de départ')
impulse.grid(row=9, column=0, padx=10, pady=5, sticky='w')

x8 = tk.Entry(root)
x8.grid(row=9, column=1, padx=10, pady=5)

vx8 = tk.Entry(root)
vx8.grid(row=9, column=4, padx=10, pady=5)

vs = tk.Label(root, text="Contre")
vs.grid(row=4, column=3, padx=10, pady=5, sticky='w')

start_button = tk.Button(root, text="Simuler", command=simuler_mele)
start_button.grid(row=10, column=2, columnspan=2, pady=20)

# List of all Entry widgets
all_entries = [x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, x7, x8, vx1, vy1, vx2, vy2, vx3, vy3, vx4, vy4, vx5, vy5, vx6, vx7, vx8]

clear_button = tk.Button(root, text="Clear all values", command=lambda: clear_all_entries(all_entries))
clear_button.grid(row=10, column=3, pady=20)

exemple_button = tk.Button(root, text="Utiliser valeurs exemple", command=utiliser_valeur_exemple1)
exemple_button.grid(row=10, column=4, pady=20)

root.mainloop()
