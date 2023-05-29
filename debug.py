

def calculate_building_rehabilitation_cost(surface_terrain, salon_surface, chambres_surface,  salle_de_bain_surface, cuisine_surface, salle_a_manger_surface, nombre_chambres, indice_standing):

    surface_totale = salon_surface + salle_a_manger_surface + salle_de_bain_surface + chambres_surface + cuisine_surface
    
    ############ Define variables ##############
    surface_tuile = 0.16 #constant
    probleme_terrain = 0
    renovation_interieure = 0
    renovation_salon = 0
    renovation_chambres = 0
    renovation_salle_de_bain = 0
    renovation_cuisine = 0
    renovation_salle_a_manger = 0
    renovation_toiture = 0
    surface_toiture = 0
    surface_toiture_reparation = 0
    remplacement_toiture = 0
    remplacement_toiture_materiau = 0
    reparation_charpente = 0
    probleme_moisissure = 0
    probleme_moisissure_plafond = 0
    probleme_moisissure_sol = 0
    probleme_moisissure_gravite = 0
    probleme_electriques = 0
    probleme_norme_electriques = 0
    probleme_plomberie = 0
    probleme_plomberie_indice = 0
    probleme_hvac = 0
    probleme_hvac_indice = 0
    choix_chauffage = 0
    reparation_clim = 0
    installation_vmc = 0
    probleme_isolation = 0
    probleme_isolation_murs = 0
    probleme_isolation_murs_surface = 0
    probleme_isolation_combles = 0
    probleme_isolation_combles_surface = 0
    probleme_isolation_plancher = 0
    probleme_isolation_plancher_surface = 0
    probleme_nuisibles = 0
    probleme_rats = 0
    probleme_punaises = 0
    probleme_guepes = 0
    probleme_fourmis = 0
    probleme_nuisibles_reparation = 0
    probleme_nuisibles_surface = 0
    probleme_humidite = 0
    probleme_humidite_traitement = 0
    probleme_fondations = 0
    probleme_fondations_fissure = 0
    probleme_fondations_affaissement = 0
    remplacement_fondations_pieux = 0
    probleme_fondations_murs = 0
    probleme_fondations_murs_type = 0
    probleme_fondations_murs_surface = 0


    


