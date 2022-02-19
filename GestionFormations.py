from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3


class GestionFormations:
    def __init__(self, root):
        self.root = root
        self.root.title("Système de gestion d'un établissement de formations")

        largeur_ecran = root.winfo_screenwidth()
        hauteur_ecran = root.winfo_screenheight()

        self.root.geometry('%dx%d' % (largeur_ecran, hauteur_ecran))
        self.root.configure(bg='#434448')

        # ================Titre de la fenetre de la gestion des étudiants=====================
        title = Label(self.root, text="Gestion des formations", bd=2, relief=GROOVE, font=('ubunto', 20, 'bold'),
                      padx=20, bg="#ff5c33")
        title.pack(side=TOP, fill=X)

        global codeFormationText
        global intituleFormationText
        global langueFormationText
        global niveauFormationText
        global objectifsFormationText

        global rechercheText

        # ==================Frame de menu principal===========================

        menuFrame = Frame(self.root, bd=2, relief=GROOVE, bg="#323232")
        menuFrame.place(x=20, y=50, width=0.97 * largeur_ecran, height=80)

        gestionEtudiantBouton = Button(menuFrame, text="Gestion des étudiants", font=('ubunto', 14, 'bold'), width=28,
                                       height=3, cursor='hand2', command=self.gestionEtudiants)
        gestionEtudiantBouton.grid(row=0, column=1, padx=10, pady=10)

        gestionInscriptionBouton = Button(menuFrame, text="Gestion des inscriptions", font=('ubunto', 14, 'bold'),
                                          width=28,
                                          height=3, cursor='hand2', command=self.gestionInscriptions)
        gestionInscriptionBouton.grid(row=0, column=2, padx=10, pady=10)

        gestionFormateursBouton = Button(menuFrame, text="Gestion des formateurs", font=('ubunto', 14, 'bold'),
                                         width=28, height=3, cursor='hand2', command=self.gestionFormateurs)
        gestionFormateursBouton.grid(row=0, column=3, padx=10, pady=10)

        # =====================Frame: formulaire de saisie des donnees des etudiants =========
        manageFrame = Frame(self.root, bd=2, relief=GROOVE, bg="#323232")
        manageFrame.place(x=20, y=130, width=0.32 * largeur_ecran, height=560)

        titleLabel = Label(manageFrame, text="Infos des formations", font=('ubunto', 30, 'bold'), bg="#323232",
                           fg="white")
        titleLabel.grid(row=0, columnspan=2, pady=15)

        codeFormationLabel = Label(manageFrame, text='Code:', font=('ubunto', 14, 'bold'), bg="#323232", fg='white')
        codeFormationLabel.grid(row=1, column=0, pady=10, sticky='w')

        codeFormationText = Entry(manageFrame, font=('Times new roman', 14), bd=2, relief=GROOVE, width=30)
        codeFormationText.grid(row=1, column=1, padx=10, pady=10, sticky='w')

        intituleFormationLabel = Label(manageFrame, text='Intitulé:', font=('ubunto', 14, 'bold'), bg="#323232",
                                       fg='white')
        intituleFormationLabel.grid(row=2, column=0, pady=10, sticky='w')

        intituleFormationText = Entry(manageFrame, font=('Times new roman', 14), bd=2, relief=GROOVE, width=30)
        intituleFormationText.grid(row=2, column=1, padx=10, pady=10, sticky='w')

        langueFormationLabel = Label(manageFrame, text='Langue:', font=('ubunto', 14, 'bold'), bg="#323232", fg='white')
        langueFormationLabel.grid(row=3, column=0, pady=10, sticky='w')

        langueFormationText = Entry(manageFrame, font=('Times new roman', 14), bd=2, relief=GROOVE, width=30)
        langueFormationText.grid(row=3, column=1, padx=10, pady=10, sticky='w')

        niveauFormationLabel = Label(manageFrame, text='Niveau:', font=('ubunto', 14, 'bold'), bg="#323232",
                                     fg='white')
        niveauFormationLabel.grid(row=4, column=0, pady=10, sticky='w')

        niveauFormationText = Entry(manageFrame, font=('Times new roman', 14), bd=2, relief=GROOVE, width=30)
        niveauFormationText.grid(row=4, column=1, padx=10, pady=10, sticky='w')

        objectifsFormationLabel = Label(manageFrame, text='Objectifs:', font=('ubunto', 14, 'bold'), bg="#323232",
                                        fg='white')
        objectifsFormationLabel.grid(row=5, column=0, pady=10, sticky='w')

        objectifsFormationText = Text(manageFrame, font=('Times new roman', 14), bd=2, relief=GROOVE, width=30,
                                      height=3)
        objectifsFormationText.grid(row=5, column=1, padx=10, pady=10, sticky='w')

        # ==========Boutons d'action pour la gestion des etudiants =======
        boutonFrame = Frame(manageFrame, bd=2, relief=GROOVE, bg="#323232")
        boutonFrame.place(x=20, y=450, width=0.27 * largeur_ecran, height=80)

        enregistrerBouton = Button(boutonFrame, text="Enregistrer", width=8, height=3,
                                   command=self.enregistrer_formation, cursor="hand2")
        enregistrerBouton.grid(row=0, column=0, padx=10, pady=10)

        modifierBouton = Button(boutonFrame, text="Modifier", width=8, height=3,
                                command=self.modifier_formation, cursor="hand2")
        modifierBouton.grid(row=0, column=1, padx=10, pady=10)

        supprimerBouton = Button(boutonFrame, text="Supprimer", width=8, height=3,
                                 command=self.supprimer_formation, cursor="hand2")
        supprimerBouton.grid(row=0, column=2, padx=10, pady=10)

        rafraichirBouton = Button(boutonFrame, text="Rafraichir", width=8, height=3,
                                  command=self.rafraichir_formation, cursor="hand2")
        rafraichirBouton.grid(row=0, column=3, padx=10, pady=10)

        # ===============Frame d'affichage des données des étudiants ==============

        detailFrame = Frame(self.root, bd=2, relief=GROOVE, bg="#434448")
        detailFrame.place(x=0.34 * largeur_ecran, y=130, width=0.643 * largeur_ecran, height=560)

        rechercheLabel = Label(detailFrame, text="Rechercher par intitulé ou par code:", font=('ubunto', 14, 'bold'),
                               bg="#434448", fg='white')
        rechercheLabel.grid(row=0, column=0, pady=10, padx=10, sticky='w')

        rechercheText = Entry(detailFrame, font=('Times new roman', 14), bd=2, relief=GROOVE, width=30)
        rechercheText.grid(row=0, column=1, pady=10, padx=10, sticky='w')

        rechercheBouton = Button(detailFrame, text="Rechercher", width=10, cursor="hand2", command=self.chercher_par)
        rechercheBouton.grid(row=0, column=2, pady=10, padx=10)

        afficherTousBouton = Button(detailFrame, text="Afficher toutes", width=20, cursor="hand2",
                                    command=self.afficher_formations)
        afficherTousBouton.grid(row=0, column=3, pady=10, padx=10)

        tableFrame = Frame(detailFrame, bd=2, relief=GROOVE, bg="#434448")
        tableFrame.place(x=10, y=50, width=0.625 * largeur_ecran, height=500)

        defilement_x = Scrollbar(tableFrame, orient=HORIZONTAL)
        defilement_y = Scrollbar(tableFrame, orient=VERTICAL)

        self.formationTable = ttk.Treeview(tableFrame, columns=("code", "intitule", "langue", "niveau", "objectifs"),
                                           xscrollcommand=defilement_x.set, yscrollcommand=defilement_y.set)

        defilement_x.pack(side=BOTTOM, fill=X)
        defilement_y.pack(side=RIGHT, fill=Y)
        defilement_x.config(command=self.formationTable.xview)
        defilement_y.config(command=self.formationTable.yview)

        self.formationTable.heading("code", text="Code")
        self.formationTable.heading("intitule", text="Intitulé")
        self.formationTable.heading("langue", text="Langue")
        self.formationTable.heading("niveau", text="Niveau")
        self.formationTable.heading("objectifs", text="Objectifs")

        self.formationTable['show'] = 'headings'

        self.formationTable.column('code', width=70)
        self.formationTable.column('intitule', width=100)
        self.formationTable.column('langue', width=100)
        self.formationTable.column('niveau', width=100)
        self.formationTable.column('objectifs', width=270)

        self.formationTable.pack(fill=BOTH, expand=True)

        self.afficher_formations()

        self.formationTable.bind("<ButtonRelease-1>", self.recuperer_donnees_selectionnees)

    def enregistrer_formation(self):

        champs = []
        if codeFormationText.get() == "":
            champs.append(codeFormationText)

        if intituleFormationText.get() == "":
            champs.append(intituleFormationText)

        if langueFormationText.get() == "":
            champs.append(langueFormationText)

        if niveauFormationText.get() == "":
            champs.append(niveauFormationText)

        if len(objectifsFormationText.get(1.0, END + '-1c')) == 0:
            champs.append(objectifsFormationText)

        if champs != []:
            for champ in champs:
                champ['bg'] = "#F9E2E4"
            messagebox.showerror("Erreurs", "Veuillez remplir tous les champs recquis !")
            champs.clear()

            return champs


        else:
            bdd = "bdd/gestion_formation.db"
            connexion = sqlite3.connect(bdd)
            cursor = connexion.cursor()

            n = codeFormationText.get()
            requete = "SELECT* FROM formations WHERE code_formation = :code"
            cursor.execute(requete, {'code': n})
            result = cursor.fetchall()

            if len(result) > 0:
                messagebox.showerror("Erreurs", "Une formation est dèja enregistrée avec le code que vous avez saisi")

            else:
                data = (codeFormationText.get(), intituleFormationText.get(), langueFormationText.get(),
                        niveauFormationText.get(),
                        objectifsFormationText.get("1.0", END))
                req = "INSERT INTO formations(code_formation, intitule_formation,langue_formation,niveau_formation,objectifs_formation) VALUES(?,?,?,?,?)"
                cursor.execute(req, data)
                connexion.commit()
                cursor.close()
                connexion.close()

                messagebox.showinfo("Enregistrement d'une formation",
                                    "L'enregistrement de la formation " + intituleFormationText.get() + " a été bien faite")
                self.rafraichir_formation()
                self.afficher_formations()

    def recuperer_donnees_selectionnees(self, evenement):

        codeFormationText['state'] = 'normal'
        ligne_selectionnee = self.formationTable.focus()
        contenu = self.formationTable.item(ligne_selectionnee)
        ligne = contenu['values']

        codeFormationText.delete(0, END)
        intituleFormationText.delete(0, END)
        langueFormationText.delete(0, END)
        niveauFormationText.delete(0, END)
        objectifsFormationText.delete('1.0', END)

        codeFormationText.insert(END, ligne[0])
        intituleFormationText.insert(END, ligne[1])
        langueFormationText.insert(END, ligne[2])
        niveauFormationText.insert(END, ligne[3])
        objectifsFormationText.insert(END, ligne[4])

        codeFormationText['state'] = 'disabled'

    def modifier_formation(self):

        champs = []

        if intituleFormationText.get() == "":
            champs.append(intituleFormationText)

        if langueFormationText.get() == "":
            champs.append(langueFormationText)

        if niveauFormationText.get() == "":
            champs.append(niveauFormationText)

        if len(objectifsFormationText.get(1.0, END + '-1c')) == 0:
            champs.append(objectifsFormationText)

        if champs != []:
            for champ in champs:
                champ['bg'] = "#F9E2E4"
            messagebox.showerror("Erreurs", "Veuillez remplir tous les champs recquis !")
            champs.clear()

            return champs


        else:
            bdd = "bdd/gestion_formation.db"
            connexion = sqlite3.connect(bdd)
            cursor = connexion.cursor()

            data = (intituleFormationText.get(), langueFormationText.get(), niveauFormationText.get(),
                    objectifsFormationText.get("1.0", END), codeFormationText.get())
            req = "UPDATE formations SET intitule_formation = ?, langue_formation=?, niveau_formation=?, objectifs_formation=? WHERE code_formation =?"
            cursor.execute(req, data)
            connexion.commit()
            cursor.close()
            connexion.close()

            messagebox.showinfo("Modification d'une formation",
                                "La modification de la formation " + intituleFormationText.get() + "  a été bien faite")
            self.rafraichir_formation()
            self.afficher_formations()

    def supprimer_formation(self):
        if codeFormationText.get() != "":
            supp = messagebox.askyesno("Supprimer?", "Vous voulez vraiment supprimer cette formation?")
            if supp <= 0:
                self.afficher_formations()
            else:
                bdd = "bdd/gestion_formation.db"
                connexion = sqlite3.connect(bdd)
                cursor = connexion.cursor()

                data = (codeFormationText.get(),)
                req = "DELETE FROM formations WHERE code_formation =?"

                cursor.execute(req, data)
                connexion.commit()

                cursor.close()
                connexion.close()

                messagebox.showinfo("Confirmation de suppression", "La formation a bien été supprimée")

                self.rafraichir_formation()
                self.afficher_formations()


        else:
            messagebox.showerror("selection", "Veuillez selectionner la formation à supprimer!")

    def rafraichir_formation(self):

        codeFormationText['state'] = 'normal'

        codeFormationText.delete(0, END)
        intituleFormationText.delete(0, END)
        langueFormationText.delete(0, END)
        niveauFormationText.delete(0, END)
        objectifsFormationText.delete("1.0", END)

        codeFormationText['bg'] = "white"
        intituleFormationText['bg'] = "white"
        langueFormationText['bg'] = "white"
        niveauFormationText['bg'] = "white"
        objectifsFormationText['bg'] = "white"

    def afficher_formations(self):
        bdd = "bdd/gestion_formation.db"
        connexion = sqlite3.connect(bdd)
        cursor = connexion.cursor()

        req = "SELECT * FROM formations"
        cursor.execute(req)
        result = cursor.fetchall()

        if len(result) > 0:
            self.formationTable.delete(*self.formationTable.get_children())
            for row in result:
                self.formationTable.insert('', END, values=row)

        cursor.close()
        connexion.close()

    def chercher_par(self):
        bdd = "bdd/gestion_formation.db"
        connexion = sqlite3.connect(bdd)
        cursor = connexion.cursor()

        b = rechercheText.get()

        req = "SELECT * FROM formations WHERE intitule_formation = :intitule or code_formation = :code"
        cursor.execute(req, {'intitule': b, 'code': b})
        result = cursor.fetchall()

        if len(result) > 0:
            self.formationTable.delete(*self.formationTable.get_children())
            for row in result:
                self.formationTable.insert('', END, values=row)
        else:
            messagebox.showinfo("Recherche", "Aucune formation ne répond à votre recherche")

        cursor.close()
        connexion.close()

    def gestionEtudiants(self):
        e = compile(open('./GestionEtudiants.py').read(), './GestionEtudiants.py', 'exec')
        exec(e)

    def gestionInscriptions(self):
        e = compile(open('./GestionInscriptions.py').read(), './GestionInscriptions.py', 'exec')
        exec(e)

    def gestionFormateurs(self):
        pass


root = Tk()
application = GestionFormations(root)
root.mainloop()
