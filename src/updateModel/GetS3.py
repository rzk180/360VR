import random
def read_ids_from_file(file_path):
    """
    Lit un fichier contenant des IDs séparés par des virgules et les stocke dans une liste d'entiers.
    
    :param file_path: Chemin vers le fichier contenant les IDs
    :return: Liste des IDs sous forme d'entiers
    """
    with open(file_path, 'r') as file:
        # Lire le contenu du fichier
        content = file.read()
        # Séparer les valeurs par la virgule et les convertir en entiers
        id_list = [int(id.strip()) for id in content.split(',') if id.strip().isdigit()]
    
    return id_list

def main():
    # Chemin vers le fichier de sortie
    output_file_path = 'style2.txt'
    
    # Récupérer les IDs depuis le fichier
    ids = read_ids_from_file(output_file_path)
    
    random_id = random.choice(ids)
    # Afficher la liste des IDs
    print("Les IDs récupérés du fichier sont :", ids)
    print("\n"+str(random_id))

if __name__ == "__main__":
    main()
