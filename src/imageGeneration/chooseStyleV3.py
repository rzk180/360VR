import random
from imageGeneration import postGen
from . import CURRENTDIR

def read_ids_from_file(file_path):
    """
    Lit un fichier contenant des IDs séparés par des virgules et les stocke dans une liste d'entiers.
    
    :param file_path: Chemin vers le fichier contenant les IDs
    :return: Liste des IDs sous forme d'entiers
    """
    with open(file_path, 'r') as file:
        content = file.read()
        id_list = [int(id.strip()) for id in content.split(',') if id.strip().isdigit()]
    
    return id_list

def main(text):
    # Chemin vers le fichier de sortie
    output_file_path = CURRENTDIR + '\\data\\style2.txt'
    
    # Récupérer les IDs depuis le fichier
    ids = read_ids_from_file(output_file_path)
    
    random_id = random.choice(ids)
    
    print("choose Style : DONE -> " + str(random_id))

    return postGen.main(random_id,text)

if __name__ == "__main__":
    main()
