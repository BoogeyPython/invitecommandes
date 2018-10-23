#coding:utf-8


import time
import sys
import os



print("miniterminal CMD")
print("For the Interface connexion login and password is :\n\
[msfconsole]")
print("-----------------")

Identifiant = "msfconsole"

Password = "msfconsole"
#liste des variables suivi des structures conditionnnel
Chargement = 0
user_id = 1
user_id =  int(user_id)
print(user_id)

user_password = True or False

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
		user_password = user_password + 1
		print("Mot de passe incorrect", user_password)




while Chargement < 4:

	print("Veuillez patienter...")
	Chargement += 1
	time.sleep(1)
#Création de mini terminal en python

#liste des variables 
terminal = True

terminal_name = "[CMD]"
print("Type help for all command")
shutdown = True
user_commande = ""
compteur = 0


while terminal:
    
	user_commande = input(f"{terminal_name}")
    
	if user_commande == "quit":
	    terminal_name = input("Voulez vous quitter le programme [o/n]") 
	    if terminal_name == "o":
	    	break
	    	if terminal_name == "n":
	    		continue
	    	else:
	    		print("Bravo vous avez quitté le programme")
	
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