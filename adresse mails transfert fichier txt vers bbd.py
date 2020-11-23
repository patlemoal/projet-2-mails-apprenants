
import mysql.connector as mysqlpyth

#connexion base de données
bdd = mysqlpyth.connect(user='root', 
password='root', 
host='localhost', 
port="8082", 
database='microsoftia')

cursor = bdd.cursor()

cursor.execute("SELECT id_apprenant, prenom, nom FROM apprenants")
donnees = cursor.fetchall()


#on organise les données sous forme de liste avec des tuples  en dictionnaire
dico_apprenants = {}
for i in donnees:
    # POUR CHAQUE TUPLE (for i in données) on ajoute un item dans le dictionnaire
    dico_apprenants[i[0]]=f"{i[1]}"+"."+f"{i[2]}"

for cle, valeur in dico_apprenants.items():
#on appelle la foncion en mettant les ()
    dico_apprenants[cle]= valeur.lower().replace("'",'').replace(" ","-")
print(dico_apprenants)

#ouverture du fichier txt apprennants 
chemin = "C:/Users/utilisateur/Google Drive/microsoft_ia/Google Drive/projets/projet n°2 apprenants/apprenants.txt"

# récupération des données du fichier spécifié ci dessus avec affichage des données en liste
with open(chemin, "r") as f:
     listemails = f.read().splitlines()


lst = []
for apprenant in dico_apprenants.items() : # il prend les apprenants dans l'odre du dico
    nom = apprenant[1]
    for mail in listemails: #il lit la liste amory en premier
        if nom in mail: 
            query = f"UPDATE apprenants SET mails='{mail}' WHERE id_apprenant={apprenant[0]};" 
            cursor.execute(query)   
print(lst)



bdd.commit()
 
cursor.close()

bdd.close()

#ALTER TABLE `apprenants` ADD `mails` VARCHAR(50) NOT NULL AFTER `prenom`; 


# query = "ALTER TABLE apprenants DROP COLUMN mail"
# cursor.execute(query)

# query = "ALTER TABLE apprenants ADD COLUMN mail VARCHAR(100) NOT NULL"
# cursor.execute(query)
# for elem in liste :
#query = f"UPDATE apprenants SET mail_apprenant='{elem[3]}' WHERE id_apprenant={str(elem[0])};"     
#     cursor.execute(query)



