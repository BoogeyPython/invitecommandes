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


#################### LA PARTIE EN DESSOUS C'EST A TOI DE LA CORRIGER OUMAKI ####################

#liste des variables 
terminal = True

terminal_name = "[CMD]"
print("Type help for all commands")

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