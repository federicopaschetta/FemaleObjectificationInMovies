import json

# Charger les données JSON
file_path = r'annotations_trainval2017/annotations/instances_train2017.json'  # Remplacez par votre chemin de fichier
with open(file_path, 'r') as file:
    data = json.load(file)

# Préparer pour traiter les 10 premières images
person_category_id = 1
first_ten_images = data['images'][:10]

# Filtrer les annotations pour obtenir seulement celles qui correspondent à des personnes dans l'image spécifiée
for image in first_ten_images:
    image_id = image['id']
    people_annotations = [anno for anno in data['annotations'] if anno['category_id'] == person_category_id and anno['image_id'] == image_id]
    n_people = len(people_annotations)

    #Form1 Calcul de la formule num-people-dif
    num_people_dif = 1 - (1 / (n_people + 1))
    
    #Form2 Calcul de la somme des tailles (hauteurs) des personnes
    total_height = sum(anno['bbox'][3] for anno in people_annotations)  # bbox[3] est la hauteur

    # Calcul de la formule people_size_dif
    if n_people > 0:
        people_size_dif = 1 - (1 / n_people) * total_height
    else:
        people_size_dif = 1  # Aucune personne détectée, people_size_dif est défini à 1
    
    # Fomr3 Calcul de la somme des offsets (x positions) des personnes
    total_offset = sum(anno['bbox'][0] for anno in people_annotations)  # bbox[0] est la position x

    # Calcul de la formule offset_dif
    if n_people > 0:
        offset_dif = 1 - ((1 / n_people) * total_offset)
    else:
        offset_dif = 1  # Aucune personne détectée, offset_dif est défini à 1    
        
    # Afficher les résultats pour chaque image
    print(f"Image ID: {image_id}")
    print(f"Nombre de personnes: {n_people}")
    print(f"Différence calculée (num-people-dif): {num_people_dif}")
    print("-" * 40)
    print(f"Somme des hauteurs des personnes: {total_height}")
    print(f"Différence calculée (people_size_dif): {people_size_dif}")
    print("-" * 40)
    print(f"Somme des offsets des personnes: {total_offset}")
    print(f"Différence calculée (offset_dif): {offset_dif}")
    print("-" * 40)