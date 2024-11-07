import json

# Chemin vers votre fichier JSON contenant les données de keypoints
file_path = r'annotations_trainval2017\annotations\person_keypoints_train2017.json'
# Chemin pour le fichier de sortie où les résultats seront enregistrés
output_file_path = 'c:/Users/salma/Downloads/PER_2024_2025/res_formule2.txt'

# Charger les données JSON
with open(file_path, 'r') as file:
    data = json.load(file)

# Définir l'ID de catégorie pour les personnes
person_category_id = 1

# Ouvrir le fichier de sortie pour écrire les résultats
with open(output_file_path, 'w') as output_file:
    output_file.write("Image ID,Nombre de personnes détectées,Size Difference (people_size_diff)\n")

    # Itérer seulement sur les 10 premières images
    for image in data['images'][:10]:  # Limiter à 10 images
        image_id = image['id']
        people_annotations = [anno for anno in data['annotations'] if anno['category_id'] == person_category_id and anno['image_id'] == image_id and anno['num_keypoints'] > 0]
        n_people = len(people_annotations)

        # Calcul de la somme des tailles des personnes (hauteur * largeur pour chaque boîte englobante)
        total_size = sum(anno['bbox'][2] * anno['bbox'][3] for anno in people_annotations)  # bbox[2] est la largeur, bbox[3] est la hauteur

        # Calcul de la formule people_size_diff
        if n_people > 0:
            people_size_diff = 1 - ((1 / n_people) * total_size)
        else:
            people_size_diff = 1  # Aucune personne détectée

        # Écrire les résultats dans le fichier de sortie
        output_file.write(f"{image_id},{n_people},{people_size_diff}\n")