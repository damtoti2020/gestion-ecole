from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from validate_email import validate_email
import sqlite3
from datetime import *


class GestionInscriptions:
    def __init__(self, root):
        self.root = root
        self.root.title("Système de gestion d'un établissement de formations")

        largeur_ecran = root.winfo_screenwidth()
        hauteur_ecran = root.winfo_screenheight()

        self.root.geometry('%dx%d' % (largeur_ecran, hauteur_ecran))
        self.root.configure(bg='#434448')

        # ================Titre de la fenetre de la gestion des étudiants=====================
        title = Label(self.root, text="Gestion des inscriptions", bd=2, relief=GROOVE, font=('ubunto', 20, 'bold'),
                      padx=20, bg="#b30086")
        title.pack(side=TOP, fill=X)

        global ineEtudiantText
        global nomEtudiantText
        global prenomEtudiantText
        global emailEtudiantText
        global adresseEtudiantText
        global villeEtudiantText
        global rechercheText
        global formationDeroulant
        global rechercheFormationDeroulantText

        # ==================Frame de menu principal===========================

        menuFrame = Frame(self.root, bd=2, relief=GROOVE, bg="#323232")
        menuFrame.place(x=20, y=50, width=0.97 * largeur_ecran, height=80)

        gestionFormationBouton = Button(menuFrame, text="Gestion des formations", font=('ubunto', 14, 'bold'), width=28,
                                        height=3, cursor='hand2', command=self.gestionFormations)
        gestionFormationBouton.grid(row=0, column=1, padx=10, pady=10)

        gestionInscriptionBouton = Button(menuFrame, text="Gestion des étudiants", font=('ubunto', 14, 'bold'),
                                          width=28,
                                          height=3, cursor='hand2', command=self.gestionEtudiants)
        gestionInscriptionBouton.grid(row=0, column=2, padx=10, pady=10)

        gestionFormateursBouton = Button(menuFrame, text="Gestion des formateurs", font=('ubunto', 14, 'bold'),
                                         width=28, height=3, cursor='hand2', command=self.gestionFormateurs)
        gestionFormateursBouton.grid(row=0, column=3, padx=10, pady=10)

        # =====================Frame: formulaire de saisie des donnees des etudiants =========
        manageFrame = Frame(self.root, bd=2, relief=GROOVE, bg="#323232")
        manageFrame.place(x=20, y=130, width=0.32 * largeur_ecran, height=410)

        titleLabel = Label(manageFrame, text="Inscription à une formation", font=('ubunto', 30, 'bold'), bg="#323232",
                           fg="white")
        titleLabel.grid(row=0, columnspan=2, pady=15)

        ineEtudiantLabel = Label(manageFrame, text='INE:', font=('ubunto', 14, 'bold'), bg="#323232", fg='white')
        ineEtudiantLabel.grid(row=1, column=0, pady=10, sticky='w')

        ineEtudiantText = Entry(manageFrame, font=('Times new roman', 14), bd=2, relief=GROOVE, width=30)
        ineEtudiantText.grid(row=1, column=1, padx=10, pady=10, sticky='w')

        nomEtudiantLabel = Label(manageFrame, text='Nom:', font=('ubunto', 14, 'bold'), bg="#323232", fg='white')
        nomEtudiantLabel.grid(row=2, column=0, pady=10, sticky='w')

        nomEtudiantText = Entry(manageFrame, font=('Times new roman', 14), bd=2, relief=GROOVE, width=30)
        nomEtudiantText.grid(row=2, column=1, padx=10, pady=10, sticky='w')

        prenomEtudiantLabel = Label(manageFrame, text='Prénom:', font=('ubunto', 14, 'bold'), bg="#323232", fg='white')
        prenomEtudiantLabel.grid(row=3, column=0, pady=10, sticky='w')

        prenomEtudiantText = Entry(manageFrame, font=('Times new roman', 14), bd=2, relief=GROOVE, width=30)
        prenomEtudiantText.grid(row=3, column=1, padx=10, pady=10, sticky='w')

        emailEtudiantLabel = Label(manageFrame, text='Adresse email:', font=('ubunto', 14, 'bold'), bg="#323232",
                                   fg='white')
        emailEtudiantLabel.grid(row=4, column=0, pady=10, sticky='w')

        emailEtudiantText = Entry(manageFrame, font=('Times new roman', 14), bd=2, relief=GROOVE, width=30)
        emailEtudiantText.grid(row=4, column=1, padx=10, pady=10, sticky='w')

        formationLabel = Label(manageFrame, text="Formations:", font=('ubunto', 14, 'bold'), bg="#323232", fg='white')
        formationLabel.grid(row=5, column=0, pady=10, sticky='w')

        formationDeroulant = ttk.Combobox(manageFrame,font=('Times new roman', 14) )
        formationDeroulant['values'] = (self.recuperer_formations())
        formationDeroulant.grid(row=5, column=1, pady=10, padx=10, sticky='w')

        # ==========Boutons d'action pour la gestion des etudiants =======
        boutonFrame = Frame(manageFrame, bd=2, relief=GROOVE, bg="#323232")
        boutonFrame.place(x=150, y=330, width=0.18 * largeur_ecran, height=70)

        inscrireBouton = Button(boutonFrame, text="Inscrire", width=8, height=3,
                                   command=self.inscrire_etudiant, cursor="hand2")
        inscrireBouton.grid(row=0, column=1, padx=30, pady=5)

        desinscrireBouton = Button(boutonFrame, text="Désinscrire", width=8, height=3,
                                command=self.desinscrire_etudiant, cursor="hand2")
        desinscrireBouton.grid(row=0, column=2, padx=10, pady=10)

        #================Frame d'affichage des formations auxquelles est inscrit un etudiant=======

        formationsEtudiantFrame = Frame(self.root, bd=2, relief=GROOVE, bg= "#323232")
        formationsEtudiantFrame.place(x=20, y=550, width= 0.32*largeur_ecran, height=230)

        formationEtudiantLabel = Label(formationsEtudiantFrame, text="Formations auxquelles est inscrit: "+nomEtudiantText.get(), font=("ubunto",14, 'bold'), bg="#323232", fg="white")
        formationEtudiantLabel.grid(row=0, column=0, pady=10, padx=5, sticky='w')

        formationsTableFrame = Frame(formationsEtudiantFrame, bd=2, relief=GROOVE, bg="#434448")
        formationsTableFrame.place(x=5, y=50, width=0.31 * largeur_ecran, height=170)

        defilement_x = Scrollbar(formationsTableFrame, orient=HORIZONTAL)
        defilement_y = Scrollbar(formationsTableFrame, orient=VERTICAL)

        self.fromationsEtudiantTable = ttk.Treeview(formationsTableFrame, columns=("code", "intitule", "date_inscription"),
                                          xscrollcommand=defilement_x.set, yscrollcommand=defilement_y.set)

        defilement_x.pack(side=BOTTOM, fill=X)
        defilement_y.pack(side=RIGHT, fill=Y)
        defilement_x.config(command=self.fromationsEtudiantTable.xview)
        defilement_y.config(command=self.fromationsEtudiantTable.yview)

        self.fromationsEtudiantTable.heading("code", text="Code")
        self.fromationsEtudiantTable.heading("intitule", text="Intitulé")
        self.fromationsEtudiantTable.heading("date_inscription", text="Date d'inscription")


        self.fromationsEtudiantTable['show'] = 'headings'

        self.fromationsEtudiantTable.column('code', width=40)
        self.fromationsEtudiantTable.column('intitule', width=180)
        self.fromationsEtudiantTable.column("date_inscription", width=60)


        self.fromationsEtudiantTable.pack(fill=BOTH, expand=True)


        # ===============Frame d'affichage des données des étudiants ==============
        
        detailFrame = Frame(self.root, bd=2, relief=GROOVE, bg="#434448")
        detailFrame.place(x=0.34 * largeur_ecran, y=130, width=0.643 * largeur_ecran, height=650)

        rechercheLabel = Label(detailFrame, text="Rechercher par nom ou par email:", font=('ubunto', 14, 'bold'),
                               bg="#434448", fg='white')
        rechercheLabel.grid(row=0, column=0, pady=10, padx=10, sticky='w')

        rechercheText = Entry(detailFrame, font=('Times new roman', 14), bd=2, relief=GROOVE, width=30)
        rechercheText.grid(row=0, column=1, pady=10, padx=10, sticky='w')

        rechercheBouton = Button(detailFrame, text="Rechercher", width=10, cursor="hand2", command=self.chercher_par)
        rechercheBouton.grid(row=0, column=2, pady=10, padx=10)

        afficherTousBouton = Button(detailFrame, text="Afficher tous", width=20, cursor="hand2",
                                    command=self.afficher_etudiants)
        afficherTousBouton.grid(row=0, column=3, pady=10, padx=10)

        formationRechercheLabel = Label(detailFrame, text="Sélectionner une formation:", font=('ubunto', 14, 'bold'),
                               bg="#434448", fg='white')
        formationRechercheLabel.grid(row=1, column=0, pady=10, padx=10, sticky='w')

        rechercheFormationDeroulantText = ttk.Combobox(detailFrame, font=("ubunto",14, 'bold'))
        rechercheFormationDeroulantText['values'] = (self.recuperer_formations())
        rechercheFormationDeroulantText.grid(row=1, column=1, pady=10, padx=5, sticky='w')

        rechercheFormationBouton = Button(detailFrame, command=self.chercher_par_formation, text="Rechercher", width=10)
        rechercheFormationBouton.grid(row=1, column = 2, pady=10, padx=5)

        tableFrame = Frame(detailFrame, bd=2, relief=GROOVE, bg="#434448")
        tableFrame.place(x=10, y=100, width=0.625 * largeur_ecran, height=540)

        defilement_x = Scrollbar(tableFrame, orient=HORIZONTAL)
        defilement_y = Scrollbar(tableFrame, orient=VERTICAL)

        self.etudiantTable = ttk.Treeview(tableFrame, columns=("ine", "nom", "prenom", "email", "adresse", "ville"),
                                          xscrollcommand=defilement_x.set, yscrollcommand=defilement_y.set)

        defilement_x.pack(side=BOTTOM, fill=X)
        defilement_y.pack(side=RIGHT, fill=Y)
        defilement_x.config(command=self.etudiantTable.xview)
        defilement_y.config(command=self.etudiantTable.yview)

        self.etudiantTable.heading("ine", text="INE")
        self.etudiantTable.heading("nom", text="Nom")
        self.etudiantTable.heading("prenom", text="Prénom")
        self.etudiantTable.heading("email", text="Email")
        self.etudiantTable.heading("adresse", text="Adresse")
        self.etudiantTable.heading("ville", text="Ville")

        self.etudiantTable['show'] = 'headings'

        self.etudiantTable.column('ine', width=70)
        self.etudiantTable.column('nom', width=100)
        self.etudiantTable.column('prenom', width=100)
        self.etudiantTable.column('email', width=100)
        self.etudiantTable.column('adresse', width=270)
        self.etudiantTable.column('ville', width=100)

        self.etudiantTable.pack(fill=BOTH, expand=True)

        self.afficher_etudiants()

        self.etudiantTable.bind("<ButtonRelease-1>", self.recuperer_donnees_selectionnees)
        


    def inscrire_etudiant(self):

        bdd = "bdd/gestion_formation.db"
        connexion = sqlite3.connect(bdd)
        cursor = connexion.cursor()

        if formationDeroulant.get()=="":
            messagebox.showerror("Erreurs", "Veuillez choisir une formation")
        else:
            data1 = (ineEtudiantText.get(), formationDeroulant.get())
            req1 = "SELECT * FROM inscriptions WHERE ine_etudiant = ? AND code_formation=?"
            cursor.execute(req1, data1)
            result1 = cursor.fetchall()

            if len(result1) !=0:
                messagebox.showerror("Erreur", "L'étudiant ayant l'INE: "+ineEtudiantText.get()+" est déja inscrit à la formation choisie!")
            else:
                ma_date = date.today()
                date_actuelle = ma_date.strftime("%d/%m/%y")
                data2 = (ineEtudiantText.get(), formationDeroulant.get(), date_actuelle)
                req2 = "INSERT INTO inscriptions(ine_etudiant, code_formation, date_inscription) VALUES(?,?,?)"
                cursor.execute(req2,data2)
                connexion.commit()

                messagebox.showinfo("Inscription à une formation", "L'inscription de l'étudiant "+nomEtudiantText.get()+ " à la formation ayant le code: " +formationDeroulant.get()+ "a été faite avec succès!")

                self.afficher_etudiants()
                self.afficher_formations_etudiant()
        cursor.close()
        connexion.close()


    def desinscrire_etudiant(self):
        bdd = "bdd/gestion_formation.db"
        connexion = sqlite3.connect(bdd)
        cursor = connexion.cursor()

        if formationDeroulant.get() =="":
            messagebox.showerror("Erreur", "Veuillez choisir une formation!")
        else:
            data =(ineEtudiantText.get(), formationDeroulant.get())
            req = "SELECT * FROM inscriptions WHERE ine_etudiant = ? AND code_formation=?"
            cursor.execute(req, data)
            result1 = cursor.fetchall()
            if len(result1) == 0:
                messagebox.showerror("Erreur", "Veuillez choisir une formation à laquelle est inscrit l'étudiant ayant l'INE: "+ineEtudiantText.get())

            else:
                supp = messagebox.askyesno("Désinscription", "Voulez vous vraiment désinscrire cet étudiant?")
                if supp>0:
                    req1 = "DELETE FROM inscriptions WHERE ine_etudiant=? AND code_formation=?"
                    cursor.execute(req1, data)
                    connexion.commit()

                    messagebox.showinfo("Désinscription", "La désinscription de l'étudiant "+nomEtudiantText.get()+ " a été bien faite!")

            self.afficher_formations_etudiant()
        cursor.close()
        connexion.close()


    def afficher_formations_etudiant(self):
        bdd = "bdd/gestion_formation.db"
        connexion = sqlite3.connect(bdd)
        cursor = connexion.cursor()

        data = (ineEtudiantText.get(),)
        req = """SELECT formations.code_formation, formations.intitule_formation, inscriptions.date_inscription
        From formations JOIN inscriptions ON formations.code_formation = inscriptions.code_formation
        JOIN etudiants ON etudiants.ine_etudiant = inscriptions.ine_etudiant AND inscriptions.ine_etudiant = ? """

        cursor.execute(req, data)
        result = cursor.fetchall()

        if len(result)>0:
            self.fromationsEtudiantTable.delete(*self.fromationsEtudiantTable.get_children())
            for ligne in result:
                self.fromationsEtudiantTable.insert('', END, values=ligne)

        cursor.close()
        connexion.close()


    def chercher_par(self):
        bdd = "bdd/gestion_formation.db"
        connexion = sqlite3.connect(bdd)
        cursor = connexion.cursor()

        b = rechercheText.get()

        req = "SELECT * FROM etudiants WHERE nom_etudiant = :nom or email_etudiant = :email"
        cursor.execute(req, {'nom': b, 'email': b})
        result = cursor.fetchall()

        if len(result) > 0:
            self.etudiantTable.delete(*self.etudiantTable.get_children())
            for row in result:
                self.etudiantTable.insert('', END, values=row)
        else:
            messagebox.showinfo("Recherche", "Aucun étudiant ne répond à votre recherche")

        cursor.close()
        connexion.close()


    def chercher_par_formation(self):
        bdd = "bdd/gestion_formation.db"
        connexion = sqlite3.connect(bdd)
        cursor = connexion.cursor()

        if rechercheFormationDeroulantText.get() == "":
            messagebox.showerror("Erreur", "Veuillez choisir une formation!")
        else:
            data = (rechercheFormationDeroulantText.get(),)

            req = """ SELECT etudiants.ine_etudiant, etudiants.nom_etudiant, etudiants.prenom_etudiant,
                        etudiants.email_etudiant, etudiants.adresse_etudiant, etudiants.ville_etudiant
                        FROM etudiants
                        JOIN inscriptions ON etudiants.ine_etudiant = inscriptions.ine_etudiant
                        AND inscriptions.code_formation = ?"""

            cursor.execute(req, data)
            result = cursor.fetchall()

            if len(result)>0:
                self.etudiantTable.delete(*self.etudiantTable.get_children())
                for row in result:
                    self.etudiantTable.insert('',END, values=row)
            else:
                messagebox.showinfo("Information", "Il n'exite aucun étudiant inscrit à la formation choisie!")

        cursor.close()
        connexion.close()


    def afficher_etudiants(self):
        bdd = "bdd/gestion_formation.db"
        connexion = sqlite3.connect(bdd)
        cursor = connexion.cursor()

        req = "SELECT * FROM etudiants"
        cursor.execute(req)
        result = cursor.fetchall()

        if len(result) > 0:
            self.etudiantTable.delete(*self.etudiantTable.get_children())
            for row in result:
                self.etudiantTable.insert('', END, values=row)

        cursor.close()
        connexion.close()

    def recuperer_formations(self):

        bdd = "bdd/gestion_formation.db"
        connexion = sqlite3.connect(bdd)
        cursor = connexion.cursor()

        req = "SELECT * FROM formations"
        cursor.execute(req)

        result = []
        for data in cursor:
            result.append(data[0])
        cursor.close()
        connexion.close()
        return result



    def recuperer_donnees_selectionnees(self, evenement):

        ineEtudiantText['state'] = 'normal'
        nomEtudiantText['state'] = 'normal'
        prenomEtudiantText['state'] = 'normal'
        emailEtudiantText['state'] = 'normal'

        ligne_selectionnee = self.etudiantTable.focus()
        contenu = self.etudiantTable.item(ligne_selectionnee)
        ligne = contenu['values']

        ineEtudiantText.delete(0, END)
        nomEtudiantText.delete(0, END)
        prenomEtudiantText.delete(0, END)
        emailEtudiantText.delete(0, END)


        ineEtudiantText.insert(END, ligne[0])
        nomEtudiantText.insert(END, ligne[1])
        prenomEtudiantText.insert(END, ligne[2])
        emailEtudiantText.insert(END, ligne[3])


        ineEtudiantText['state'] = 'disabled'
        nomEtudiantText['state'] = 'disabled'
        prenomEtudiantText['state'] = 'disabled'
        emailEtudiantText['state'] = 'disabled'

        self.fromationsEtudiantTable.delete(*self.fromationsEtudiantTable.get_children())
        self.afficher_formations_etudiant()


    def gestionFormations(self):
        e = compile(open('./GestionFormations.py').read(), './GestionFormations.py', 'exec')
        exec(e)

    def gestionEtudiants(self):
        e = compile(open('./GestionEtudiants.py').read(), './GestionEtudiants.py', 'exec')
        exec(e)

    def gestionFormateurs(self):
        pass


root = Tk()
application = GestionInscriptions(root)
root.mainloop()