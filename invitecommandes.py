#coding:utf-8

import time
import os

print(r"""                     
             ,----------------,              ,---------,
        ,-----------------------,          ,"        ,"|
      ,"                      ,"|        ,"        ,"  |
     +-----------------------+  |      ,"        ,"    |
     |  .-----------------.  |  |     +---------+      |
     |  |                 |  |  |     | -==----'|      |
     |  |  miniterminal   |  |  |     |         |      |
     |  |  by oumaki      |  |  |/----|`---=    |      |
     |  |  C:\>_          |  |  |   ,/|==== ooo |      ;
     |  |                 |  |  |  // |(((( [33]|    ,"
     |  `-----------------'  |," .;'| |((((     |  ,"
     +-----------------------+  ;;  | |         |,"
        /_)______________(_/  //'   | +---------+
   ___________________________/___  `,
  /  oooooooooooooooo  .o.  oooo /,   \,"-----------
 / ==ooooooooooooooo==.o.  ooo= //   ,`\--{)B     ,"
/_==__==========__==_ooo__ooo=_/'   /___________,"              
""")


def interface_message(msg):
    print("\n" + ''.center(50, '*') + '\n' + msg.center(50, '*') + '\n' + ''.center(50, '*') + '\n')

interface_message(" Interface d'authentification ")

hidden_username = "msfconsole"
hidden_password = "msfconsole"


while True:
    username =  input("Nom d'utilisateur ==> ")
    password =  input("Mot de passe ==> ")
    if username != hidden_username or password != hidden_password:
        print("L'authentification a échoué, veuillez réessayer !\n")
    else:
        print("l'authentification a réussi, \nBienvenue {} !\n".format(username))
        break

for x in range(4):
	print("Veuillez patienter...")
	time.sleep(0.5)

interface_message(" Votre miniterminal ")


#################### LA PARTIE EN DESSOUS L'EXECUTION DU PROGRAMMES ####################

#liste des variables 

terminal_name = "[CMD]"
print("Type help for all commands")

user_commande = ""
compteur = 0


while True:
    
	user_commande = input(f"{terminal_name}")
    
	if user_commande == "quit":
	    terminal_name = input("Voulez vous quitter le programme [o/n]:")
	    if terminal_name == "o":
	    	print("Bravo vous avez quitté le programme.")
	    	break
	    	if terminal_name == "n":
	    		continue
	        
	   
	
	     #On demande à python de se fermer

	elif user_commande == "shutdown":
		 os.system(shutdown)
	          
			
	elif user_commande == "nom":

	     terminal_name = input("Change name==>")
	     print("Le nom vient d'être:)\
	     	changer par user")

	elif user_commande == "ipconfig":
	     os.system("ipconfig")

	elif user_commande == "systeminfo":
	     os.system("systeminfo")         

	elif user_commande == "help":
	
	     print("\
----++++++++++++++++++++++++++++------\n\
nom: Modifier le nom du terminal\n\
help: Afficher la liste des commandes\n\
quit: Terminer l'éxecution du programme...\n\
shutdown: Arrêter le système :(\n\
ipconfig: Configuration IP de Windows\n\
systeminfo: Propriété du système\n\
--------------------------------------------") 
