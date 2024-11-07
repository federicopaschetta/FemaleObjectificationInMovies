import json

# Chemin vers le fichier JSON contenant les données de keypoints
file_path = r'annotations_trainval2017\annotations\person_keypoints_train2017.json'
# Chemin pour le fichier de sortie où les résultats seront enregistrés
output_file_path = 'c:/Users/salma/Downloads/PER_2024_2025/vis_face_ratio.txt'

# Charger les données JSON
with open(file_path, 'r') as file:
    data = json.load(file)

# Indices des keypoints du visage
face_keypoints_indices = [0, 1, 2, 3, 4]

# Ouvrir le fichier de sortie pour écrire les résultats
with open(output_file_path, 'w') as output_file:
    output_file.write("Annotation ID,Vis Face Ratio\n")

    # Itérer sur toutes les annotations de personnes
    for anno in data['annotations']:
        keypoints = anno['keypoints']
        visible_count = 0
        total_face_keypoints = 0

        # Compter les keypoints du visage visibles
        for index in face_keypoints_indices:
            if keypoints[index*3+2] == 2:  # Vérifier si le keypoint est visible
                visible_count += 1
            if keypoints[index*3+2] > 0:  # Vérifier si le keypoint est marqué
                total_face_keypoints += 1

        # Calculer le vis_face_ratio si des keypoints du visage sont marqués
        if total_face_keypoints > 0:
            vis_face_ratio = visible_count / total_face_keypoints
        else:
            vis_face_ratio = 0  # Aucun keypoint du visage marqué

        # Écrire le résultat dans le fichier de sortie
        output_file.write(f"{anno['id']},{vis_face_ratio:.2f}\n")

    print("Les résultats ont été sauvegardés dans:", output_file_path)
