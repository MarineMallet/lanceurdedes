
import os
import time
import random

Cloque = True
Vérton = "[3.2]"

os.system(f"title Lanceur de Dée {Vérton}")

def Visu():
	os.system("cls")
	print("")
	print(f"Lanceur de Dée {Vérton}")
	print("/help (pour avoir les commande)")
	print("Enter pour commancer")
	print("")

def Visu0():
	os.system("cls")
	print("")
	print("[pour lancer un Dée]\n")

def Help():
		print(">Dée\n[pérmet de lancer les Dée]\n")
		print(">s\n[pérmet d'aréter le programme]\n")
		print(">cls\n[nétois la consolle]\n")
		
def Help0():
	Help1()
	print("=>s\n[pérmer de revenire au menu principale`\n")
	print("=>cls\n[nétois la consolle]\n")

def Help1():
	print("il est important de faire une opération a la fois")
	print("ex:\n>1d100 \n\n[1 = le Nombre de Dée lancer\n d est obligatoir\n 100 = le nombre de face du Dée]\n")
	print("[pour faire une addition]\nex:\n>1 + 2 \n")
	print("[pour faire une soustraction]\nex:\n>1 - 2 \n")
	print("[pour faire une division]\nex:\n>1 / 2 \n")
	print("[pour faire une multiplication]\nex:\n>1 * 2 \nou\n>1 x 2 \nmarche aussi\n>1 X 2\n")
	print("[pour faire un pourcentage]\nex:\n>20 % 100")

def Ana(Chois):
	t = ""

	for x in Chois[0]:

		try:
			x = int(x)			
		except:
			pass
		else:
			x = str(x)
			t += x
	return t


def Ana0(Chois):
	t0 = ""

	for x in Chois[1]:

		try:
			x = int(x)
		except:
			pass
		else:
			x = str(x)
			t0 += x
	return t0

def tretemant(t, t0):
	res = 0
	for x in range(t):
		alé = random.randint(1, t0)
		res += alé

		print(f"[{alé}]")
	print(f"[total:{res}]")

def tretemantp(t, t0):
	opéra = t + t0
	print(f"[{opéra}]")

def tretemantm(t, t0):
	opéra = t - t0
	print(f"[{opéra}]")

def tretemantf(t, t0):
	opéra = t * t0
	print(f"[{opéra}]")

def tretemantd(t, t0):
	opéra = t / t0
	print(f"[{opéra}]")

def tretemantpo(t, t0):
	opéra = ((t0 * t) / 100 )
	print(f"[{opéra}]")

Visu()

while Cloque:
	Cloque0 = True

	Chois = input("> ").lower()

	if Chois == "dée":
		Visu0()

		while Cloque0:
			Chois = input("\n=>").lower()
			print("")

			if Chois == "s":
				Cloque0 = False
				os.system("cls")
				Visu()

			elif Chois == "/help":
				os.system("cls")
				Visu0()
				Help0()

			elif Chois.count("d") == 1:
				Chois = Chois.split("d")
				
				t = Ana(Chois)

				if t == "":
					Help1()
				
				elif t != "":
					t0 = Ana0(Chois)

					if t0 == "":
						Help1()
				
					elif t0 != "":
						t = int(t)
						t0 = int(t0)

						tretemant(t, t0)

			elif Chois.count("+") == 1:
				Chois = Chois.split("+")
				
				t = Ana(Chois)

				if t == "":
					Help1()
				
				elif t != "":
					t0 = Ana0(Chois)

					if t0 == "":
						Help1()
				
					elif t0 != "":
						t = int(t)
						t0 = int(t0)

						tretemantp(t, t0)

			elif Chois.count("-") == 1:
				Chois = Chois.split("-")
				
				t = Ana(Chois)

				if t == "":
					Help1()
				
				elif t != "":
					t0 = Ana0(Chois)

					if t0 == "":
						Help1()
				
					elif t0 != "":
						t = int(t)
						t0 = int(t0)

						tretemantm(t, t0)

			elif Chois.count("*") == 1 or Chois.count("x") == 1:
				print(Chois)

				if Chois.count("*") == 1:
					Chois = Chois.split("*")
					print(Chois)

				elif Chois.count("x") == 1:
					Chois = Chois.split("x")
					print(Chois)

				t = Ana(Chois)

				if t == "":
					Help1()
				
				elif t != "":
					t0 = Ana0(Chois)

					if t0 == "":
						Help1()
				
					elif t0 != "":
						t = int(t)
						t0 = int(t0)

						tretemantf(t, t0)

			elif Chois.count("/") == 1:
				Chois = Chois.split("/")
				
				t = Ana(Chois)

				if t == "":
					Help1()
				
				elif t != "":
					t0 = Ana0(Chois)

					if t0 == "":
						Help1()
				
					elif t0 != "":
						t = int(t)
						t0 = int(t0)

						tretemantd(t, t0)

			elif Chois.count("%") == 1:
				Chois = Chois.split("%")
				
				t = Ana(Chois)

				if t == "":
					Help1()
				
				elif t != "":
					t0 = Ana0(Chois)

					if t0 == "":
						Help1()
				
					elif t0 != "":
						t = int(t)
						t0 = int(t0)

						tretemantpo(t, t0)

			elif Chois == "cls":
				os.system("cls")
				Visu0()	

			else:
				print("aucunne commande ne sapelle comme sa \n /help poura vous aider")

	elif Chois == "cls":
		os.system("cls")
		Visu()

	elif Chois == "/help":
		os.system("cls")
		Visu()
		Help()

	elif Chois == "s":
		Cloque = False

	else:
		print("aucunne commande ne sapelle comme sa \n /help poura vous aider")


print("revenner cuant vous vouler ^^")
time.sleep(3.0)
os.system("cls")