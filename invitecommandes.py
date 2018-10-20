#coding:utf-8


import time
import sys
import os



print("miniterminal CMD")
print("-----------------")

Identifiant = "msfconsole"

Password = "msfconsole"
#liste des variables en boucles/while, if
Chargement = 0

user_id = True and False

user_id = 0 

user_passworde = True and False

user_password = 0



print("Interface de connexion...", user_id)
print("")

user_id = input("Nom d'utilisateur ==>")

print("---------------------------------\n\
	")

user_password = input("Password ==>")


while user_id:

	if user_id != Identifiant:
	    print("Identifiant incorrect", user_id)

	
	elif user_password != Password:
		user_password = False
		break
		print("Mot de passe incorrect", user_password)




while Chargement < 4:

	print("Veuillez patienter...")
	Chargement += 1
	time.sleep(1)
#Création de mini terminal en python

#liste des variables 
terminal = True

terminal_name = "[CMD]"
shutdown = True
user_commande = ""
compteur = 0

while terminal:
    
	user_commande = input(f"{terminal_name}")
    
	if user_commande == "quit": 
		sys.exit(0)
	     #On demande à python de se fermer

	elif user_commande == "shutdown":
		 os.system(shutdown)
	          
			
	elif user_commande == "name":

	     terminal_name = input("Change name==>")
	     print("Le nom vient d'être:)\
	     	changer par user")

	elif user_commande == "help":
	
	     print("\
----++++++++++++++++++++++++++++------\n\
name: modifier le nom du terminal\n\
help: afficher la liste des commandes\n\
quit: terminer l'éxecution du programme...\n\
shutdown: arrêter le système :(\n\
---------------------------------------------") 
