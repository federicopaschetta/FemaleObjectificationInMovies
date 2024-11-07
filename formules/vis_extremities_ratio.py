import json

# Chemin vers le fichier JSON contenant les données de keypoints
file_path = r'annotations_trainval2017\annotations\person_keypoints_train2017.json'
# Chemin pour le fichier de sortie où les résultats seront enregistrés
output_file_path = 'c:/Users/salma/Downloads/PER_2024_2025/vis_extremities_ratio.txt'

# Charger les données JSON
with open(file_path, 'r') as file:
    data = json.load(file)

# Indices des keypoints des extrémités incluant coudes, poignets, genoux et chevilles
extremities_keypoints_indices = [7, 8, 9, 10, 13, 14, 15, 16]

# Ouvrir le fichier de sortie pour écrire les résultats
with open(output_file_path, 'w') as output_file:
    output_file.write("Annotation ID,Vis Extremities Ratio\n")

    # Itérer sur toutes les annotations de personnes
    for anno in data['annotations']:
        keypoints = anno['keypoints']
        visible_count = 0
        total_extremities_keypoints = len(extremities_keypoints_indices)

        # Compter les keypoints des extrémités visibles
        for index in extremities_keypoints_indices:
            if keypoints[index*3+2] == 2:  # Vérifier si le keypoint est visible
                visible_count += 1

        # Calculer le vis_extremities_ratio
        if total_extremities_keypoints > 0:
            vis_extremities_ratio = visible_count / total_extremities_keypoints
        else:
            vis_extremities_ratio = 0  # Éviter la division par zéro en cas de données manquantes

        # Écrire le résultat dans le fichier de sortie
        output_file.write(f"Annotation ID: {anno['id']}, Vis Extremities Ratio: {vis_extremities_ratio:.2f}\n")

    print("Les résultats ont été sauvegardés dans:", output_file_path)
