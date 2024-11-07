import json
import math

# Chemin vers le fichier JSON contenant les données de keypoints et bounding boxes
file_path = r'annotations_trainval2017\annotations\person_keypoints_train2017.json'
# Chemin pour le fichier de sortie où les résultats seront enregistrés
output_file_path = 'c:/Users/salma/Downloads/PER_2024_2025person_offset.txt'

# Charger les données JSON
with open(file_path, 'r') as file:
    data = json.load(file)

# Ouvrir le fichier de sortie pour écrire les résultats
with open(output_file_path, 'w') as output_file:
    output_file.write("Image ID,Annotation ID,Person Offset\n")

    # Itérer sur toutes les images
    for image in data['images']:
        image_id = image['id']
        image_width = image['width']
        image_height = image['height']
        annotations = [anno for anno in data['annotations'] if anno['image_id'] == image_id]

        # Itérer sur toutes les annotations de personnes dans cette image
        for anno in annotations:
            bbox = anno['bbox']
            # Calculer le centre de la boîte englobante
            bbox_center_x = bbox[0] + bbox[2] / 2
            bbox_center_y = bbox[1] + bbox[3] / 2

            # Calculer les offsets par rapport au centre de l'image
            offset_x = bbox_center_x - (image_width / 2)
            offset_y = bbox_center_y - (image_height / 2)

            # Calculer le person_offset en utilisant la formule fournie
            person_offset = (math.sqrt(offset_x**2 + offset_y**2) / math.sqrt(2)) * 2

            # Écrire le résultat dans le fichier de sortie
            output_file.write(f"{image_id},{anno['id']},{person_offset:.2f}\n")

    print("Les résultats ont été sauvegardés dans:", output_file_path)

