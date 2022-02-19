from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sqlite3
from datetime import *
from validate_email import validate_email
from PIL import Image, ImageTk

class MenuAccueil:
    def __init__(self, root):
        self.root = root
        self.root.title("Menu d'accueil")

        largeur_ecran = root.winfo_screenwidth()
        hauteur_ecran = root.winfo_screenheight()

        self.root.geometry('%dx%d'%(largeur_ecran, hauteur_ecran))
        self.root.configure(bg="#434448")

        self.arriere_plan = ImageTk.PhotoImage(file = "images/bg.jpg")
        arriere_plan = Label(self.root, image= self.arriere_plan)
        arriere_plan.place(x=0, y=0, relwidth = 1, relheight=1)


        self.imgGaucheLabel = ImageTk.PhotoImage(file = "images/imageLeft.jpg")
        imgGaucheLabel = Label(self.root, image=self.imgGaucheLabel)
        imgGaucheLabel.place(x=200, y=100, width=300, height = 450)

        frameMenu = Frame(self.root, bd=2, relief=GROOVE, bg="#0584FB")
        frameMenu.place(x=500, y=100, width = 600, height =450)

        bouton_1 = Button(frameMenu, text="GESTION DES ÉTUDIANTS ", font=('Arial',16,'bold'), width=28, height= 3, cursor='hand2', command= self.gestion_etudiants)
        bouton_1.grid(row=0, column=1, padx = 50, pady=20)

        bouton_2 = Button(frameMenu, text="GESTION DES FORMATIONS ", font=('Arial', 16, 'bold'), width=28, height=3,
                          cursor='hand2', command=self.gestion_formations)
        bouton_2.grid(row=1, column=1, padx=50, pady=20)

        bouton_3 = Button(frameMenu, text="GESTION DES INSCRPTIONS ", font=('Arial', 16, 'bold'), width=28, height=3,
                          cursor='hand2', command=self.gestion_inscriptions)
        bouton_3.grid(row=2, column=1, padx=50, pady=20)

        bouton_4 = Button(frameMenu, text="GESTION DES FORMATEURS ", font=('Arial', 16, 'bold'), width=28, height=3,
                          cursor='hand2', command=self.gestion_formateurs)
        bouton_4.grid(row=3, column=1, padx=50, pady=20)




    def gestion_etudiants(self):
        e = compile(open('./GestionEtudiants.py').read(),'./GestionEtudiants.py','exec')
        exec(e)

    def gestion_formations(self):
        e = compile(open('./GestionFormations.py').read(), './GestionFormations.py', 'exec')
        exec(e)

    def gestion_inscriptions(self):
        e = compile(open('./GestionInscriptions.py').read(), './GestionInscriptions.py', 'exec')
        exec(e)

    def gestion_formateurs(self):
        pass


if __name__ =='__main__':
    root = Tk()
    application = MenuAccueil(root)
    root.mainloop()










