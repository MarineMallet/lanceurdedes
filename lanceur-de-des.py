
import os
import time
import random

Cloque = True
Vérton = "[3.2]"

os.system(f"title Lanceur de Dé {Vérton}")

def Visu():
	os.system("cls")
	print("")
	print(f"Lanceur de Dé {Vérton}")
	print("/help (pour avoir les commandes)")
	print("Enter pour commencer")
	print("")

def Visu0():
	os.system("cls")
	print("")
	print("[pour lancer un Dé]\n")

def Help():
		print(">Dée\n[permet de lancer les Dés]\n")
		print(">s\n[permet d'arréter le programme]\n")
		print(">cls\n[vide la consolle]\n")
		
def Help0():
	Help1()
	print("=>s\n[permet de revenir au menu principale`\n")
	print("=>cls\n[vide la consolle]\n")

def Help1():
	print("il est important de faire une opération a la fois")
	print("ex:\n>1d100 \n\n[1 = le Nombre de Dée lancer\n d est obligatoir\n 100 = le nombre de face du Dée]\n")
	print("[pour faire une addition]\nex:\n>1 + 2 \n")
	print("[pour faire une soustraction]\nex:\n>1 - 2 \n")
	print("[pour faire une division]\nex:\n>1 / 2 \n")
	print("[pour faire une multiplication]\nex:\n>1 * 2 \nou\n>1 x 2 \nmarche aussi\n>1 X 2\n")
	print("[pour faire un pourcentage]\nex:\n>20 % 100")

def Ana(Choix):
	t = ""

	for x in Choix[0]:

		try:
			x = int(x)			
		except:
			pass
		else:
			x = str(x)
			t += x
	return t


def Ana0(Choix):
	t0 = ""

	for x in Choix[1]:

		try:
			x = int(x)
		except:
			pass
		else:
			x = str(x)
			t0 += x
	return t0

def traitement(t, t0):
	res = 0
	for x in range(t):
		alé = random.randint(1, t0)
		res += alé

		print(f"[{alé}]")
	print(f"[total:{res}]")

def traitementp(t, t0):
	opéra = t + t0
	print(f"[{opéra}]")

def traitementm(t, t0):
	opéra = t - t0
	print(f"[{opéra}]")

def traitementf(t, t0):
	opéra = t * t0
	print(f"[{opéra}]")

def traitementd(t, t0):
	opéra = t / t0
	print(f"[{opéra}]")

def traitementpo(t, t0):
	opéra = ((t0 * t) / 100 )
	print(f"[{opéra}]")

Visu()

while Cloque:
	Cloque0 = True

	Choix = input("> ").lower()

	if Choix == "dé":
		Visu0()

		while Cloque0:
			Choix = input("\n=>").lower()
			print("")

			if Choix == "s":
				Cloque0 = False
				os.system("cls")
				Visu()

			elif Choix == "/help":
				os.system("cls")
				Visu0()
				Help0()

			elif Choix.count("d") == 1:
				Choix = Choix.split("d")
				
				t = Ana(Choix)

				if t == "":
					Help1()
				
				elif t != "":
					t0 = Ana0(Choix)

					if t0 == "":
						Help1()
				
					elif t0 != "":
						t = int(t)
						t0 = int(t0)

						traitement(t, t0)

			elif Choix.count("+") == 1:
				Choix = Choix.split("+")
				
				t = Ana(Choix)

				if t == "":
					Help1()
				
				elif t != "":
					t0 = Ana0(Choix)

					if t0 == "":
						Help1()
				
					elif t0 != "":
						t = int(t)
						t0 = int(t0)

						traitementp(t, t0)

			elif Choix.count("-") == 1:
				Choix = Choix.split("-")
				
				t = Ana(Choix)

				if t == "":
					Help1()
				
				elif t != "":
					t0 = Ana0(Choix)

					if t0 == "":
						Help1()
				
					elif t0 != "":
						t = int(t)
						t0 = int(t0)

						traitemxntm(t, t0)

			elif Choix.count("*") == 1 or Choix.count("x") == 1:
				print(Choix)

				if Choix.count("*") == 1:
					Choix = Choix.split("*")
					print(Choix)

				elif Choix.count("x") == 1:
					Chois = Choix.split("x")
					print(Choix)

				t = Ana(Choix)

				if t == "":
					Help1()
				
				elif t != "":
					t0 = Ana0(Choix)

					if t0 == "":
						Help1()
				
					elif t0 != "":
						t = int(t)
						t0 = int(t0)

						traitemxntf(t, t0)

			elif Choix.count("/") == 1:
				Choix = Choix.split("/")
				
				t = Ana(Choix)

				if t == "":
					Help1()
				
				elif t != "":
					t0 = Ana0(Choix)

					if t0 == "":
						Help1()
				
					elif t0 != "":
						t = int(t)
						t0 = int(t0)

						traitementd(t, t0)

			elif Choix.count("%") == 1:
				Choix = Choix.split("%")
				
				t = Ana(Choix)

				if t == "":
					Help1()
				
				elif t != "":
					t0 = Ana0(Choix)

					if t0 == "":
						Help1()
				
					elif t0 != "":
						t = int(t)
						t0 = int(t0)

						traitementpo(t, t0)

			elif Choix == "cls":
				os.system("cls")
				Visu0()	

			else:
				print("aucunne commande ne sapelle comme sa \n /help poura vous aider")

	elif Choix == "cls":
		os.system("cls")
		Visu()

	elif Choix == "/help":
		os.system("cls")
		Visu()
		Help()

	elif Choix == "s":
		Cloque = False

	else:
		print("aucune commande ne s'apelle comme ça \n /help pourras vous aider")


print("à bientot")
time.sleep(3.0)
os.system("cls")
