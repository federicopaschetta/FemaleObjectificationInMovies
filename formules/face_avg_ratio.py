import json

# Chemin vers votre fichier JSON contenant les données de keypoints
file_path = r'annotations_trainval2017\annotations\person_keypoints_train2017.json'
# Chemin pour le fichier de sortie où les résultats seront enregistrés
output_file_path = 'c:/Users/salma/Downloads/PER_2024_2025/res_formule4.txt'

# Charger les données JSON
with open(file_path, 'r') as file:
    data = json.load(file)

# ID de catégorie pour les personnes, utilisé pour filtrer les annotations
person_category_id = 1

# Indices des keypoints pertinents pour le visage (ex : yeux, nez, oreilles)
face_keypoints_indices = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]  # Exemple hypothétique

# Ouvrir le fichier de sortie pour écrire les résultats
with open(output_file_path, 'w') as output_file:
    output_file.write("Image ID,Nombre de personnes détectées,Face Avg Ratio\n")

    # Itérer seulement sur les 10 premières images
    for image in data['images'][:10]:  # Limiter à 10 images
        image_id = image['id']
        people_annotations = [anno for anno in data['annotations'] if anno['category_id'] == person_category_id and anno['image_id'] == image_id and anno['num_keypoints'] > 0]
        n_people = len(people_annotations)
        total_face_ratio = 0

        for anno in people_annotations:
            keypoints = anno['keypoints']
            visible_count = sum(1 for i in face_keypoints_indices if keypoints[i*3+2] == 2)
            total_face_ratio += visible_count / len(face_keypoints_indices)  # Calculer la ratio de visibilité pour cette personne

        # Calculer le face_avg_ratio
        face_avg_ratio = total_face_ratio / n_people if n_people > 0 else 0

        # Écrire les résultats dans le fichier de sortie
        output_file.write(f"{image_id},{n_people},{face_avg_ratio}\n")

    print("Les résultats ont été sauvegardés dans:", output_file_path)
