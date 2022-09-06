# VALEUR FONCIÈRE MOYENNE

#from concurrent.futures.process import _ExecutorManagerThread
#from dis import dis
import statistics
import requests 
import json
import math

rayon = 50
lat = 48.85 #latitude
lon = 2.35 #longitude

def valeur_fonciere_au_m2(rayon, lat, lon):

    params = {"format": "json"}
    response = requests.get(f"https://api.cquest.org/dvf?lat={lat}&lon={lon}&dist={rayon}", params=params)

    def jprint(obj):
        # create a formatted string of the Python JSON object
        text = json.dumps(obj, indent=4)
        print(text)

    valeur_fonciere_moyenne = [] # tableau où on stocke les valeurs foncières se trouvant dans le périmètre choisi

    valeur_api = response.json() #la valeur foncière que l'on cherche avec l'API

    for i in range(len(valeur_api["features"])): 
        surface = (valeur_api["features"][i]["properties"]["surface_relle_bati"]) #on cherche la surface du logement
        if surface != 0 :
            prix = (valeur_api["features"][i]["properties"]["valeur_fonciere"]) #on cherche la valeur foncière
            prix_au_m2 = prix/surface
            valeur_fonciere_moyenne.append(prix_au_m2)

    return round(statistics.mean(valeur_fonciere_moyenne))

print(f"a valeur foncière moyenne sur un rayon de {rayon}m est de {valeur_fonciere_au_m2(rayon, lat, lon)} euros par m2.\n")

#SCHÉMA DES LIEUX DE STATIONNEMENT

from csv import DictReader

def prix_parking(long,lat):
    # reading csv file
    with open('bnls.csv', 'r') as read_obj:
        csv_dict_reader = DictReader(read_obj)

        # get column names from a csv file
        # column_names = csv_dict_reader.fieldnames
        # print(column_names )

        distanceX = 6.2366534 - long 
        distanceY = 44.0932836 - lat
        distance_carree = distanceX**2 + distanceY**2
        distanceActu = 0
        n = 0
        indice = 0

        #calcule les coordonnées

        test = []

        for row in csv_dict_reader:
            test.append(list(row.values()))
            if float(row['Xlong']) == long and float(row['Ylat']) == lat :
                return row['Xlong'] , row['Ylat'] , row['tarif_1h']
            else:
                distanceX = float(row['Xlong']) - long 
                distanceY = float(row['Ylat']) - lat 
                distanceActu = distanceX**2 + distanceY**2
                if distanceActu < distance_carree :
                    distance_carree = distanceActu
                    indice = n
            n += 1
        
        return (test[indice][21],test[indice][19],test[indice][18])
   
print(prix_parking(2.444997, 44.930953))

surface_loyer = 24 

print(f"Avec un taux de rentabilité brut de 5.2% et un logement de {surface_loyer}m², le loyer est :{ round(surface_loyer*0.05*valeur_fonciere_au_m2(rayon, lat, lon)/12)}")

def cout_construction_immeuble1(surface, lon, lat): #CELUI PAS TRES FIABLE
    assert(surface >= 0)
    surface += surface/10 #surface totale = surface logement + partie commune ≈ 10%
    prix_loyer = valeur_fonciere_au_m2(20, lon, lat)*surface #rayon de 20m pour le calcul de valeur_fonciere_au_m2
    prix_etudes_de_sol = prix_loyer*0.02
    prix_controles_techniques = prix_loyer*0.03
    prix_honoraires_architectes = prix_loyer*0.08
    return round(prix_loyer + prix_etudes_de_sol + prix_controles_techniques + prix_honoraires_architectes)

surface_immeuble = 220

print(f"Le prix de construction d'un immeuble est {cout_construction_immeuble1(surface_immeuble, lat, lon)}")
