# Problèmes de construction
import math
geotechnical_investigation_prices = {
    "étude topographique": 2.16,  # € par mètre carré
    "rapport ingénieur": 2100  # €
}

demolition_prices = {
    "lavabo": 51,  # € chacun
    "baignoire": 82,  # € chacune
    "douche": 137,  # € chacune
    "lampe incandescente": 17,  # € chacune
    "lave-vaisselle": 31,  # € chacun
    "porte": 55,  # € chacune
    "fenêtre": 56,  # € chacune
    "poutre": 16.40,  # € par mètre linéaire
    "cloison en plâtre": 4.95,  # € par mètre carré
    "charpente": 11.08,  # € par mètre linéaire
    "tuiles": 15.50,  # € par mètre carré
    "murs": 43.92,  # € par mètre carré
    "murs porteurs": 174.04,  # € par mètre carré
    "sol en béton": 48.70,  # € par mètre carré
    "location camion hydraulique 12T": 1400  # € par jour
}

# Dégats des eaux
mold_prices = {
    "inspection de la zone": 481,  # €
    "réduction de la moisissure": 1923,  # €
    "enlèvement de zones contaminées par la moisissure": 18132  # €
}

mold_demolition_prices = {
    "sol": 3.29,  # € par pied carré (10.79 € par mètre carré)
    "plafond": 2.17  # € par pied carré (7.12 € par mètre carré)
}

# Problèmes électriques
electrical_replacement_prices = {
    "remplacement du panneau électrique": (879, 2747.25),  # €
    "réparation ou remplacement des fils et des câbles": (546, 1638),  # €
    "installation de nouveaux circuits électriques": (546, 1638),  # €
    "installation de systèmes d'éclairage": (227, 1137)  # € par pièce
}

electrical_upgrade_prices = {
    # € par prise ou interrupteur
    "mise à niveau des prises de courant et des interrupteurs": (72.50, 108.75),
    "mise à jour des systèmes de sécurité": (546, 2185)  # €
}

# Problèmes de plomberie
bathroom_prices = {
    "lavabo": 60.06,  # €
    "baignoire/douche": 150.15,  # €
    "toilette": (200, 600),  # €
    "robinet de douche": (60, 120),  # €
    "robinet de lavabo": (30, 100)  # €
}

plumbing_repair_prices = {
    "réparation d'une fuite": (200, 550),  # €
    "remplacement d'un tuyau": (100, 200),  # €
    "remplacement d'un robinet": (100, 250),  # €
    "débouchage d'un évier": (100, 200),  # €
    "remplacement d'un évier": (200, 500)  # €
}

# Problème de chauffage, ventilation, climatisation
hvac_maintenance_prices = {
    "entretien annuel d'une chaudière": (120, 200),  # €
    "entretien du système électronique": 74.62,  # €
    "entretien d'une pompe à chaleur": (100, 300),  # €
    "nettoyage des conduits de ventilation": (200, 500)  # €
}

hvac_replacement_repair_prices = {
    "ventilation + conduits": 546,  # €
    "chaudière": [1500, 3000, 4000, 7000],  # €
    # €
    "installation d'un nouveau système de chauffage (pompe à chaleur)": (5000, 12000),
    "réparation ou remplacement de la climatisation": (1000, 5000),  # €
    # €
    "installation d'un système de ventilation mécanique contrôlée (VMC)": (1000, 4000),
    # €
    "installation d'un système de climatisation centralisée": (3000, 8000)
}

# Problème d'isolation
insulation_prices = {
    "isolation des combles": (20, 80),  # € par mètre carré
    "isolation des murs": (50, 150),  # € par mètre carré
    "isolation des planchers": (30, 80),  # € par mètre carré
    "installation de fenêtres isolantes": (300, 1000),  # € par fenêtre
    "isolation des portes": (50, 500)  # € par porte
}

# Présence de nuisibles
pest_control_prices = {
    "élimination de souris et de rats": (150, 500),  # €
    "élimination de punaises de lit": (200, 1000),  # €
    "élimination des guêpes et des nids de frelons": (60, 250),  # €
    "élimination des fourmis": (70, 200)  # €
}

pest_damage_repair_prices = {
    "réparation des dommages causés par les rongeurs": (150, 500),  # €
    "réparation des dommages causés par les insectes": (200, 1000),  # €
    # € par mètre carré
    "nettoyage et désinfection de la zone touchée": (50, 100)
}

# Problèmes d'humidité
humidity_detection_treatment_prices = {
    "diagnostic de l'humidité": (80, 150),  # €
    # € par mètre linéaire
    "traitement de l'humidité par injection": (100, 150),
    "traitement de l'humidité par ventilation": (1500, 5000),  # €
    "traitement de l'humidité par drainage": (1000, 5000)  # €
}

# Problèmes de toiture
roof_repair_prices = {
    "remplacement de tuiles": (2, 4),  # € par tuile
    "réparation de fuite": (200, 400),  # €
    "remplacement du revêtement de toit": (40, 100),  # € par mètre carré
    "nettoyage de la toiture": (200, 500)  # €
}

roof_replacement_prices = {
    "toiture en tuiles": (60, 150),  # € par mètre carré
    "toiture en ardoise": (80, 250),  # € par mètre carré
    "toiture en zinc": (120, 200),  # € par mètre carré
    "toiture en bac acier": (30, 100)  # € par mètre carré
}

# Problèmes de fondation
foundation_crack_repair_prices = {
    # € par fissure
    "réparation de fissures - injection de résine époxy": (100, 300),
    "ancrage de la fondation": (2000, 5000)  # €
}

foundation_subsidence_repair_prices = {
    "injection de mousse polyuréthane": (1000, 3000),  # €
    "remplacement des pieux": (3000, 7000)  # €
}

foundation_wall_repair_prices = {
    # € par mètre carré
    "rénovation de mur en blocs de béton": (100, 150),
    # € par mètre carré
    "réparation de murs de fondation en briques": (100, 250),
    "rénovation de mur en béton coulé": (300, 500)  # € par mètre carré
}

# Problèmes de construction
geotechnical_investigation_prices = {
    "étude topographique": 2.16,  # € par mètre carré
    "rapport ingénieur": 2100  # €
}

demolition_prices = {
    "lavabo": 51,  # € chacun
    "baignoire": 82,  # € chacune
    "douche": 137,  # € chacune
    "lampe incandescente": 17,  # € chacune
    "lave-vaisselle": 31,  # € chacun
    "porte": 55,  # € chacune
    "fenêtre": 56,  # € chacune
    "poutre": 16.40,  # € par mètre linéaire
    "cloison en plâtre": 4.95,  # € par mètre carré
    "charpente": 11.08,  # € par mètre linéaire
    "tuiles": 15.50,  # € par mètre carré
    "murs": 43.92,  # € par mètre carré
    "murs porteurs": 174.04,  # € par mètre carré
    "sol en béton": 48.70,  # € par mètre carré
    "location camion hydraulique 12T": 1400  # € par jour
}

# Dégats des eaux
mold_prices = {
    "inspection de la zone": 481,  # €
    "réduction de la moisissure": 1923,  # €
    "enlèvement de zones contaminées par la moisissure": 18132  # €
}

mold_demolition_prices = {
    "sol": 3.29,  # € par pied carré (10.79 € par mètre carré)
    "plafond": 2.17  # € par pied carré (7.12 € par mètre carré)
}

# Problèmes électriques
electrical_replacement_prices = {
    "remplacement du panneau électrique": (879, 2747.25),  # €
    "réparation ou remplacement des fils et des câbles": (546, 1638),  # €
    "installation de nouveaux circuits électriques": (546, 1638),  # €
    "installation de systèmes d'éclairage": (227, 1137)  # € par pièce
}

electrical_upgrade_prices = {
    # € par prise ou interrupteur
    "mise à niveau des prises de courant et des interrupteurs": (72.50, 108.75),
    "mise à jour des systèmes de sécurité": (546, 2185)  # €
}

# Problèmes de plomberie
bathroom_prices = {
    "lavabo": 60.06,  # €
    "baignoire/douche": 150.15,  # €
    "toilette": (200, 600),  # €
    "robinet de douche": (60, 120),  # €
    "robinet de lavabo": (30, 100)  # €
}

plumbing_repair_prices = {
    "réparation d'une fuite": (200, 550),  # €
    "remplacement d'un tuyau": (100, 200),  # €
    "remplacement d'un robinet": (100, 250),  # €
    "débouchage d'un évier": (100, 200),  # €
    "remplacement d'un évier": (200, 500)  # €
}

# Problème de chauffage, ventilation, climatisation
hvac_maintenance_prices = {
    "entretien annuel d'une chaudière": (120, 200),  # €
    "entretien du système électronique": 74.62,  # €
    "entretien d'une pompe à chaleur": (100, 300),  # €
    "nettoyage des conduits de ventilation": (200, 500)  # €
}

hvac_replacement_repair_prices = {
    "ventilation + conduits": 546,  # €
    "chaudière": [1500, 3000, 4000, 7000],  # €
    # €
    "installation d'un nouveau système de chauffage (pompe à chaleur)": (5000, 12000),
    "réparation ou remplacement de la climatisation": (1000, 5000),  # €
    # €
    "installation d'un système de ventilation mécanique contrôlée (VMC)": (1000, 4000),
    # €
    "installation d'un système de climatisation centralisée": (3000, 8000)
}

# Problème d'isolation
insulation_prices = {
    "isolation des combles": (20, 80),  # € par mètre carré
    "isolation des murs": (50, 150),  # € par mètre carré
    "isolation des planchers": (30, 80),  # € par mètre carré
    "installation de fenêtres isolantes": (300, 1000),  # € par fenêtre
    "isolation des portes": (50, 500)  # € par porte
}

# Présence de nuisibles
pest_control_prices = {
    "élimination de souris et de rats": (150, 500),  # €
    "élimination de punaises de lit": (200, 1000),  # €
    "élimination des guêpes et des nids de frelons": (60, 250),  # €
    "élimination des fourmis": (70, 200)  # €
}

pest_damage_repair_prices = {
    "réparation des dommages causés par les rongeurs": (150, 500),  # €
    "réparation des dommages causés par les insectes": (200, 1000),  # €
    # € par mètre carré
    "nettoyage et désinfection de la zone touchée": (50, 100)
}

# Problèmes d'humidité
humidity_detection_treatment_prices = {
    "diagnostic de l'humidité": (80, 150),  # €
    # € par mètre linéaire
    "traitement de l'humidité par injection": (100, 150),
    "traitement de l'humidité par ventilation": (1500, 5000),  # €
    "traitement de l'humidité par drainage": (1000, 5000)  # €
}

# Problèmes de toiture
roof_repair_prices = {
    "remplacement de tuiles": (2, 4),  # € par tuile
    "réparation de fuite": (200, 400),  # €
    "remplacement du revêtement de toit": (40, 100),  # € par mètre carré
    "nettoyage de la toiture": (200, 500)  # €
}

roof_replacement_prices = {
    "toiture en tuiles": (60, 150),  # € par mètre carré
    "toiture en ardoise": (80, 250),  # € par mètre carré
    "toiture en zinc": (120, 200),  # € par mètre carré
    "toiture en bac acier": (30, 100)  # € par mètre carré
}

# Problèmes de fondation
foundation_crack_repair_prices = {
    # € par fissure
    "réparation de fissures - injection de résine époxy": (100, 300),
    "ancrage de la fondation": (2000, 5000)  # €
}

foundation_subsidence_repair_prices = {
    "injection de mousse polyuréthane": (1000, 3000),  # €
    "remplacement des pieux": (3000, 7000)  # €
}

foundation_wall_repair_prices = {
    # € par mètre carré
    "rénovation de mur en blocs de béton": (100, 150),
    # € par mètre carré
    "réparation de murs de fondation en briques": (100, 250),
    "rénovation de mur en béton coulé": (300, 500)  # € par mètre carré
}
