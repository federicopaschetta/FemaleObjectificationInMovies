import json

# Charger les données JSON
file_path = r'annotations_trainval2017\annotations\person_keypoints_train2017.json'
output_file_path = 'c:/Users/salma/Downloads/PER_2024_2025/body_avg_ratio.txt'

with open(file_path, 'r') as file:
    data = json.load(file)

# Indices des keypoints pertinents pour le corps (exemple hypothétique)
body_keypoints_indices = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

with open(output_file_path, 'w') as output_file:
    output_file.write("Image ID,Body Avg Ratio\n")

    # Itérer sur les images
    for image in data['images'][:10]:  # Limiter à 10 images pour l'exemple
        image_id = image['id']
        annotations = [anno for anno in data['annotations'] if anno['image_id'] == image_id]
        sum_body_ratios = 0
        count_people = 0

        for anno in annotations:
            keypoints = anno['keypoints']
            visible_count = sum(1 for i in body_keypoints_indices if keypoints[i*3+2] == 2)
            total_body_keypoints = len(body_keypoints_indices)
            if total_body_keypoints > 0:
                vis_body_ratio = visible_count / total_body_keypoints
                sum_body_ratios += vis_body_ratio
                count_people += 1

        # Calculer la moyenne des ratios pour l'image
        body_avg_ratio = sum_body_ratios / count_people if count_people > 0 else 0
        output_file.write(f"{image_id},{body_avg_ratio:.2f}\n")

    print("Les résultats ont été sauvegardés dans:", output_file_path)
