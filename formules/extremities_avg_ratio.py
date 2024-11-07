import json

# Chemin vers le fichier JSON contenant les données de keypoints
file_path = r'annotations_trainval2017\annotations\person_keypoints_train2017.json'
# Chemin pour le fichier de sortie où les résultats seront enregistrés
output_file_path = 'c:/Users/salma/Downloads/PER_2024_2025/extremities_avg_ratio.txt'

# Charger les données JSON
with open(file_path, 'r') as file:
    data = json.load(file)

# Indices des keypoints des extrémités
extremities_keypoints_indices = [9, 10, 15, 16]

# Ouvrir le fichier de sortie pour écrire les résultats
with open(output_file_path, 'w') as output_file:
    output_file.write("Image ID,Extremities Avg Ratio\n")

    # Itérer sur les images
    for image in data['images']:
        image_id = image['id']
        annotations = [anno for anno in data['annotations'] if anno['image_id'] == image_id]
        sum_extremities_ratios = 0
        count_people = 0

        for anno in annotations:
            keypoints = anno['keypoints']
            visible_count = sum(1 for i in extremities_keypoints_indices if keypoints[i*3+2] == 2)
            total_extremities_keypoints = len(extremities_keypoints_indices)
            if total_extremities_keypoints > 0:
                extremities_ratio = visible_count / total_extremities_keypoints
                sum_extremities_ratios += extremities_ratio
                count_people += 1

        # Calculer la moyenne des ratios pour l'image
        extremities_avg_ratio = sum_extremities_ratios / count_people if count_people > 0 else 0
        output_file.write(f"{image_id},{extremities_avg_ratio:.2f}\n")

    print("Les résultats ont été sauvegardés dans:", output_file_path)
