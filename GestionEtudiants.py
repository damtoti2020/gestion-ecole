from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from validate_email import validate_email
import sqlite3


class GestionEtudiants:
    def __init__(self, root):
        self.root = root
        self.root.title("Système de gestion d'un établissement de formations")

        largeur_ecran = root.winfo_screenwidth()
        hauteur_ecran = root.winfo_screenheight()

        self.root.geometry('%dx%d'% (largeur_ecran,hauteur_ecran))
        self.root.configure(bg='#434448')


        #================Titre de la fenetre de la gestion des étudiants=====================
        title = Label(self.root, text="Gestion des étudiants", bd=2, relief= GROOVE, font=('ubunto', 20, 'bold'), padx=20, bg= "#0584FB")
        title.pack(side=TOP, fill=X)


        global ineEtudiantText
        global nomEtudiantText
        global prenomEtudiantText
        global emailEtudiantText
        global adresseEtudiantText
        global villeEtudiantText
        global rechercheText

        #==================Frame de menu principal===========================

        menuFrame = Frame(self.root, bd=2, relief = GROOVE, bg= "#323232")
        menuFrame.place(x=20, y=50, width= 0.97*largeur_ecran, height = 80)

        gestionFormationBouton = Button(menuFrame, text="Gestion des formations", font=('ubunto',14,'bold'), width=28, height=3, cursor= 'hand2', command= self.gestionFormations)
        gestionFormationBouton.grid(row=0, column=1, padx=10, pady=10)

        gestionInscriptionBouton = Button(menuFrame, text="Gestion des inscriptions", font=('ubunto', 14, 'bold'), width=28,
                                        height=3, cursor='hand2', command=self.gestionInscriptions)
        gestionInscriptionBouton.grid(row=0, column=2, padx=10, pady=10)

        gestionFormateursBouton = Button(menuFrame, text="Gestion des formateurs", font=('ubunto', 14, 'bold'),width=28,height=3, cursor='hand2', command=self.gestionFormateurs)
        gestionFormateursBouton.grid(row=0, column=3, padx=10, pady=10)

        #=====================Frame: formulaire de saisie des donnees des etudiants =========
        manageFrame = Frame(self.root, bd=2, relief= GROOVE, bg= "#323232")
        manageFrame.place(x=20, y=130, width=0.32 * largeur_ecran, height= 560)

        titleLabel= Label(manageFrame, text="Infos des étudiants", font=('ubunto', 30, 'bold'), bg="#323232", fg= "white")
        titleLabel.grid(row=0, columnspan = 2, pady=15)

        ineEtudiantLabel = Label(manageFrame, text='INE:', font=('ubunto',14,'bold'), bg= "#323232", fg= 'white')
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

        emailEtudiantLabel = Label(manageFrame, text='Adresse email:', font=('ubunto', 14, 'bold'), bg="#323232", fg='white')
        emailEtudiantLabel.grid(row=4, column=0, pady=10, sticky='w')

        emailEtudiantText = Entry(manageFrame, font=('Times new roman', 14), bd=2, relief=GROOVE, width=30)
        emailEtudiantText.grid(row=4, column=1, padx=10, pady=10, sticky='w')

        adresseEtudiantLabel = Label(manageFrame, text='Adresse:', font=('ubunto', 14, 'bold'), bg="#323232", fg='white')
        adresseEtudiantLabel.grid(row=5, column=0, pady=10, sticky='w')

        adresseEtudiantText = Text(manageFrame, font=('Times new roman', 14), bd=2, relief=GROOVE, width=30, height=3)
        adresseEtudiantText.grid(row=5, column=1, padx=10, pady=10, sticky='w')

        villeEtudiantLabel = Label(manageFrame, text='Ville:', font=('ubunto', 14, 'bold'), bg="#323232", fg='white')
        villeEtudiantLabel.grid(row=6, column=0, pady=10, sticky='w')

        villeEtudiantText = Entry(manageFrame, font=('Times new roman', 14), bd=2, relief=GROOVE, width=30)
        villeEtudiantText.grid(row=6, column=1, padx=10, pady=10, sticky='w')


        #==========Boutons d'action pour la gestion des etudiants =======
        boutonFrame = Frame(manageFrame, bd=2, relief=GROOVE, bg="#323232")
        boutonFrame.place(x=20, y=450, width=0.27 * largeur_ecran, height=80)

        enregistrerBouton = Button(boutonFrame, text="Enregistrer", width=8, height=3, command=self.enregistrer_etudiant, cursor="hand2")
        enregistrerBouton.grid(row=0, column=0, padx=10, pady=10)

        modifierBouton = Button(boutonFrame, text="Modifier", width=8, height=3,
                                   command=self.modifier_etudiant, cursor="hand2")
        modifierBouton.grid(row=0, column=1, padx=10, pady=10)

        supprimerBouton = Button(boutonFrame, text="Supprimer", width=8, height=3,
                                   command=self.supprimer_etudiant, cursor="hand2")
        supprimerBouton.grid(row=0, column=2, padx=10, pady=10)

        rafraichirBouton = Button(boutonFrame, text="Rafraichir", width=8, height=3,
                                   command=self.rafraichir_etudiant, cursor="hand2")
        rafraichirBouton.grid(row=0, column=3, padx=10, pady=10)

        #===============Frame d'affichage des données des étudiants ==============

        detailFrame = Frame(self.root, bd=2, relief=GROOVE, bg="#434448")
        detailFrame.place(x=0.34*largeur_ecran, y=130, width=0.643 * largeur_ecran, height=560)

        rechercheLabel = Label(detailFrame, text="Rechercher par nom ou par email:", font=('ubunto',14, 'bold'), bg="#434448", fg='white')
        rechercheLabel.grid(row=0, column=0, pady=10, padx=10, sticky='w')

        rechercheText = Entry(detailFrame, font=('Times new roman', 14), bd=2, relief=GROOVE, width=30)
        rechercheText.grid(row=0, column=1, pady=10, padx=10, sticky='w')

        rechercheBouton = Button(detailFrame, text="Rechercher", width=10, cursor="hand2", command=self.chercher_par)
        rechercheBouton.grid(row=0, column=2, pady=10, padx=10)

        afficherTousBouton = Button(detailFrame, text="Afficher tous", width=20, cursor="hand2", command=self.afficher_etudiants)
        afficherTousBouton.grid(row=0, column=3, pady=10, padx=10)

        tableFrame = Frame(detailFrame, bd= 2, relief=GROOVE, bg="#434448")
        tableFrame.place(x=10, y=50, width=0.625*largeur_ecran, height= 500)

        defilement_x= Scrollbar(tableFrame,orient=HORIZONTAL)
        defilement_y= Scrollbar(tableFrame, orient=VERTICAL)

        self.etudiantTable = ttk.Treeview(tableFrame, columns = ("ine", "nom", "prenom","email","adresse","ville"),
                                     xscrollcommand = defilement_x.set, yscrollcommand=defilement_y.set)

        defilement_x.pack(side=BOTTOM, fill=X)
        defilement_y.pack(side=RIGHT,fill=Y)
        defilement_x.config(command = self.etudiantTable.xview)
        defilement_y.config(command = self.etudiantTable.yview)

        self.etudiantTable.heading("ine", text="INE")
        self.etudiantTable.heading("nom", text="Nom")
        self.etudiantTable.heading("prenom", text="Prénom")
        self.etudiantTable.heading("email", text="Email")
        self.etudiantTable.heading("adresse", text="Adresse")
        self.etudiantTable.heading("ville", text="Ville")
        
        self.etudiantTable['show']='headings'

        self.etudiantTable.column('ine', width=70)
        self.etudiantTable.column('nom', width=100)
        self.etudiantTable.column('prenom', width=100)
        self.etudiantTable.column('email', width=100)
        self.etudiantTable.column('adresse', width=270)
        self.etudiantTable.column('ville', width=100)

        self.etudiantTable.pack(fill = BOTH, expand = True)

        self.afficher_etudiants()

        self.etudiantTable.bind("<ButtonRelease-1>", self.recuperer_donnees_selectionnees)


    def enregistrer_etudiant(self):

        is_valide = validate_email(emailEtudiantText.get())

        champs = []
        if ineEtudiantText.get()=="":
            champs.append(ineEtudiantText)

        if nomEtudiantText.get()=="":
            champs.append(nomEtudiantText)

        if prenomEtudiantText.get()=="":
            champs.append(prenomEtudiantText)

        if emailEtudiantText.get()=="":
            champs.append(emailEtudiantText)

        if len(adresseEtudiantText.get(1.0,END +'-1c'))==0:
            champs.append(adresseEtudiantText)

        if villeEtudiantText.get()=="":
            champs.append(villeEtudiantText)

        if champs != []:
            for champ in champs:
                champ['bg'] = "#F9E2E4"
            messagebox.showerror("Erreurs", "Veuillez remplir tous les champs recquis !")
            champs.clear()

            return champs

        if  not(is_valide):
            messagebox.showerror("Erreurs", "L'email que vous avez saisi n'est pas valide!")
            emailEtudiantText['bg']="#F9E2E4"

        else:
            bdd = "bdd/gestion_formation.db"
            connexion = sqlite3.connect(bdd)
            cursor = connexion.cursor()


            n = ineEtudiantText.get()
            requete = "SELECT* FROM etudiants WHERE ine_etudiant = :ine"
            cursor.execute(requete, {'ine': n})
            result = cursor.fetchall()

            if len(result)>0:
                messagebox.showerror("Erreurs", "Un étudiant est dèja enregistré avec l'INE que vous avez saisi")

            else:
                data = (ineEtudiantText.get(), nomEtudiantText.get(),prenomEtudiantText.get(),emailEtudiantText.get(),adresseEtudiantText.get("1.0",END),villeEtudiantText.get())
                req = "INSERT INTO etudiants(ine_etudiant, nom_etudiant,prenom_etudiant,email_etudiant,adresse_etudiant,ville_etudiant) VALUES(?,?,?,?,?,?)"
                cursor.execute(req, data)
                connexion.commit()
                cursor.close()
                connexion.close()

                messagebox.showinfo("Enregistrement d'un étudiant", "L'enregistrement de l'etudiant "+nomEtudiantText.get()+ " "+prenomEtudiantText.get()+ " a été bien faite")
                self.rafraichir_etudiant()
                self.afficher_etudiants()

    def recuperer_donnees_selectionnees(self, evenement):

        ineEtudiantText['state'] = 'normal'
        ligne_selectionnee = self.etudiantTable.focus()
        contenu = self.etudiantTable.item(ligne_selectionnee)
        ligne = contenu['values']


        ineEtudiantText.delete(0,END)
        nomEtudiantText.delete(0, END)
        prenomEtudiantText.delete(0, END)
        emailEtudiantText.delete(0, END)
        villeEtudiantText.delete(0, END)
        adresseEtudiantText.delete('1.0', END)


        ineEtudiantText.insert(END, ligne[0])
        nomEtudiantText.insert(END, ligne[1])
        prenomEtudiantText.insert(END, ligne[2])
        emailEtudiantText.insert(END, ligne[3])
        adresseEtudiantText.insert(END, ligne[4])
        villeEtudiantText.insert(END, ligne[5])

        ineEtudiantText['state']='disabled'


    def modifier_etudiant(self):

        is_valide = validate_email(emailEtudiantText.get())

        champs = []

        if nomEtudiantText.get()=="":
            champs.append(nomEtudiantText)

        if prenomEtudiantText.get()=="":
            champs.append(prenomEtudiantText)

        if emailEtudiantText.get()=="":
            champs.append(emailEtudiantText)

        if len(adresseEtudiantText.get(1.0,END +'-1c'))==0:
            champs.append(adresseEtudiantText)

        if villeEtudiantText.get()=="":
            champs.append(villeEtudiantText)

        if champs != []:
            for champ in champs:
                champ['bg'] = "#F9E2E4"
            messagebox.showerror("Erreurs", "Veuillez remplir tous les champs recquis !")
            champs.clear()

            return champs

        if  not(is_valide):
            messagebox.showerror("Erreurs", "L'email que vous avez saisi n'est pas valide!")
            emailEtudiantText['bg']="#F9E2E4"

        else:
            bdd = "bdd/gestion_formation.db"
            connexion = sqlite3.connect(bdd)
            cursor = connexion.cursor()


            n = ineEtudiantText.get()
            m = emailEtudiantText.get()

            requete = "SELECT* FROM etudiants WHERE ine_etudiant != :ine AND email_etudiant = :email "
            cursor.execute(requete, {'ine': n, 'email':m})
            result = cursor.fetchall()

            if len(result)>0:
                messagebox.showerror("Erreurs", "Un étudiant est dèja enregistré avec l'email que vous avez saisi")

            else:
                data = (nomEtudiantText.get(),prenomEtudiantText.get(),emailEtudiantText.get(),adresseEtudiantText.get("1.0",END),villeEtudiantText.get(), ineEtudiantText.get())
                req = "UPDATE etudiants SET nom_etudiant = ?, prenom_etudiant=?, email_etudiant=?, adresse_etudiant=?, ville_etudiant=? WHERE ine_etudiant =?"
                cursor.execute(req, data)
                connexion.commit()
                cursor.close()
                connexion.close()

                messagebox.showinfo("Modification d'un étudiant", "La modification de l'etudiant "+nomEtudiantText.get()+ " "+prenomEtudiantText.get()+ " a été bien faite")
                self.rafraichir_etudiant()
                self.afficher_etudiants()

    def supprimer_etudiant(self):
        if ineEtudiantText.get() != "":
            supp = messagebox.askyesno("Supprimer?", "Vous voulez vraiment supprimer cet étudiant?")
            if supp<=0:
                self.afficher_etudiants()
            else:
                bdd = "bdd/gestion_formation.db"
                connexion = sqlite3.connect(bdd)
                cursor = connexion.cursor()

                data = (ineEtudiantText.get(),)
                req = "DELETE FROM etudiants WHERE ine_etudiant =?"

                cursor.execute(req, data)
                connexion.commit()

                cursor.close()
                connexion.close()

                messagebox.showinfo("Confirmation de suppression", "L'etudiant a bien été supprimé")

                self.rafraichir_etudiant()
                self.afficher_etudiants()


        else:
            messagebox.showerror("selection", "Veuillez selectionner un étudiant à supprimer!")

    def rafraichir_etudiant(self):

        ineEtudiantText['state'] = 'normal'

        ineEtudiantText.delete(0,END)
        nomEtudiantText.delete(0, END)
        prenomEtudiantText.delete(0, END)
        emailEtudiantText.delete(0, END)
        adresseEtudiantText.delete("1.0",END)
        villeEtudiantText.delete(0, END)


        ineEtudiantText['bg']="white"
        nomEtudiantText['bg'] = "white"
        prenomEtudiantText['bg'] = "white"
        emailEtudiantText['bg'] = "white"
        adresseEtudiantText['bg'] = "white"
        villeEtudiantText['bg'] = "white"


    def afficher_etudiants(self):
        bdd= "bdd/gestion_formation.db"
        connexion = sqlite3.connect(bdd)
        cursor = connexion.cursor()

        req = "SELECT * FROM etudiants"
        cursor.execute(req)
        result = cursor.fetchall()

        if len(result)>0:
            self.etudiantTable.delete(*self.etudiantTable.get_children())
            for row in result:
                self.etudiantTable.insert('',END, values=row)

        cursor.close()
        connexion.close()


    def chercher_par(self):
        bdd = "bdd/gestion_formation.db"
        connexion = sqlite3.connect(bdd)
        cursor = connexion.cursor()

        b = rechercheText.get()

        req = "SELECT * FROM etudiants WHERE nom_etudiant = :nom or email_etudiant = :email"
        cursor.execute(req, {'nom':b, 'email':b})
        result = cursor.fetchall()

        if len(result) > 0:
            self.etudiantTable.delete(*self.etudiantTable.get_children())
            for row in result:
                self.etudiantTable.insert('', END, values=row)
        else:
            messagebox.showinfo("Recherche", "Aucun étudiant ne répond à votre recherche")

        cursor.close()
        connexion.close()


    def gestionFormations(self):
        e = compile(open('./GestionFormations.py').read(), './GestionFormations.py', 'exec')
        exec(e)


    def gestionInscriptions(self):
        pass

    def gestionFormateurs(self):
        pass






root = Tk()
application = GestionEtudiants(root)
root.mainloop()
