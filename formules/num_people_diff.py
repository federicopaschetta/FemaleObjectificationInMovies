import json

# Chemin vers votre fichier JSON contenant les données de keypoints
file_path = r'annotations_trainval2017\annotations\person_keypoints_train2017.json'
# Chemin pour le fichier de sortie où les résultats seront enregistrés
output_file_path = 'res_formule1.txt'

# Charger les données JSON
with open(file_path, 'r') as file:
    data = json.load(file)

# ID de catégorie pour les personnes, utilisé pour filtrer les annotations
person_category_id = 1

# Ouvrir le fichier de sortie pour écrire les résultats
with open(output_file_path, 'w') as output_file:
    output_file.write("Image ID,Nombre de personnes détectées,Différence calculée (num-people-dif)\n")

    # Itérer sur toutes les images disponibles dans le fichier JSON
    for image in data['images']:
        image_id = image['id']
        # Filtrer les annotations pour obtenir seulement celles qui correspondent à des personnes avec keypoints dans l'image spécifiée
        people_annotations = [anno for anno in data['annotations'] if anno['category_id'] == person_category_id and anno['image_id'] == image_id and anno['num_keypoints'] > 0]
        n_people = len(people_annotations)

        # Calcul de la formule num-people-dif
        num_people_diff = 1 - (1 / (n_people + 1)) if n_people > 0 else 1  # Vérifier que n_people est non-nul pour éviter la division par zéro
        
        # Écrire les résultats dans le fichier de sortie
        output_file.write(f"{image_id},{n_people},{num_people_diff}\n")

    print("Les résultats ont été sauvegardés dans:", output_file_path)