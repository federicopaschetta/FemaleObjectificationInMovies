import json

# Chemin vers votre fichier JSON contenant les données de keypoints
file_path = r'annotations_trainval2017\annotations\person_keypoints_train2017.json'
# Chemin pour le fichier de sortie où les résultats seront enregistrés
output_file_path = 'c:/Users/salma/Downloads/PER_2024_2025/res_formule3.txt'

# Charger les données JSON
with open(file_path, 'r') as file:
    data = json.load(file)

# Définir l'ID de catégorie pour les personnes
person_category_id = 1

# Ouvrir le fichier de sortie pour écrire les résultats
with open(output_file_path, 'w') as output_file:
    output_file.write("Image ID,Nombre de personnes détectées,Offset Difference (offset_diff),Individual Offsets\n")

    # Itérer seulement sur les 10 premières images
    for image in data['images'][:10]:  # Limiter à 10 images
        image_id = image['id']
        image_width = image['width']
        people_annotations = [anno for anno in data['annotations'] if anno['category_id'] == person_category_id and anno['image_id'] == image_id and anno['num_keypoints'] > 0]
        n_people = len(people_annotations)

        # Calcul de la somme des décalages des centres x des boîtes englobantes par rapport au centre de l'image
        individual_offsets = []
        for anno in people_annotations:
            center_x = anno['bbox'][0] + anno['bbox'][2] / 2
            person_offset = abs(center_x - image_width / 2)
            individual_offsets.append(person_offset)
        
        total_offset = sum(individual_offsets)

        # Calcul de la formule offset_diff en normalisant par la largeur de l'image multipliée par le nombre de personnes
        if n_people > 0:
            offset_diff = 1 - (total_offset / (image_width * n_people))
        else:
            offset_diff = 1  # Aucune personne détectée

        # Écrire les résultats dans le fichier de sortie
        output_file.write(f"{image_id},{n_people},{offset_diff},{individual_offsets}\n")

    print("Les résultats ont été sauvegardés dans:", output_file_path)
