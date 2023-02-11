import tkinter as tk
from tkinter import ttk, font
from tkinter.messagebox import showinfo
import fonctions

#region       (Définition des classes)
### Definition des classes principales utilisés:
# la classe livre :
class Livre:
    def __init__(self, name, domain, subdomain, price, remaining_quantity, total_quantity, affectations):
        self.name = name
        self.domain = domain
        self.subdomain = subdomain
        self.price = price
        self.remaining_quantity = remaining_quantity
        self.total_quantity = total_quantity
        self.affectations = affectations


# la classe Client :
class Client:
     def __init__(self, nom, prenom, Ncin_Netudiant, Id_client, membre_club, livposs):
        self.nom = nom
        self.prenom = prenom
        self.Ncin_Netudiant = Ncin_Netudiant
        self.Id_client = Id_client
        self.membre_club = membre_club
        self.livposs = livposs
#endregion


#region          (Appel des données livres et clients (Allbooks et Allclients))
def call_data():
        # Globaliser les variables déclarées dans cette fonction
        global Allbooks,Allname,Alldomain,DictDomain,DictDombk,Allsubdomain,DictSubdomain,Dictbook
        global Allclients,Allid,Dictid

        # Chargement des Données livre
        Allbooks = fonctions.import_data('livres')
        Allclients = fonctions.import_data('clients')
        # Listes des Identifiants clients
        Allid = []
        for i in range(len(Allclients)):
                Allid.append(Allclients[i].Id_client)
        # Dictionnaire des clients avec identifiants comme clés et les objets clients comme valeurs
        Dictid = {}
        for i in range(len(Allclients)):
                Dictid[Allclients[i].Id_client] = Allclients[i]
        # Liste des nomes des livres trié par ordre alphabétique
        Allname = []
        for i in range(len(Allbooks)):
                Allname.append(Allbooks[i].name)
        Allname.sort()        

        # Liste des Domaines
        Alldomain = []
        for i in range(len(Allbooks)):
                Alldomain.append(Allbooks[i].domain)
        Alldomain = [*set(Alldomain)]

        # Dictionnaire des domaines et sous-domaines avec domaine comme clé et liste des sous-domaine correspondant comme valeur
        DictDomain = {}

        for d in Alldomain:
                sd = []
                for i in range(len(Allbooks)):
                        if Allbooks[i].domain == d:
                                sd.append(Allbooks[i].subdomain)
                sd = [*set(sd)]
                DictDomain[d] = sd
        # Dictionnaire des domaines et livres avec domaine comme clé et liste des livres correspondant comme valeur
        DictDombk = {}

        for d in Alldomain:
                lv = []
                for i in range(len(Allbooks)):
                        if Allbooks[i].domain == d:
                                lv.append(Allbooks[i].name)
                lv.sort()
                DictDombk[d] = lv
        # Listes des sous-domaines
        Allsubdomain = []
        for i in range(len(Allbooks)):
                Allsubdomain.append(Allbooks[i].subdomain)
        Allsubdomain = [*set(Allsubdomain)]

        # Dictionnaire des sous-domaines et livres correspondants
        DictSubdomain = {}
        for sd in Allsubdomain:
                lv = []
                for i in range(len(Allbooks)):
                        if Allbooks[i].subdomain == sd:
                                lv.append(Allbooks[i].name)
                lv = [*set(lv)]
                DictSubdomain[sd] = lv

        # Dictionnaire des noms des livres et objets livres correspondants
        Dictbook = {}
        for i in range(len(Allbooks)):
                Dictbook[Allbooks[i].name] = Allbooks[i]
        
#endregion
#region                    (sauvegarder les changements sur les variables Allbooks et Allclients)
def save_data():
        # Sauvegarde des changements impactant les objets livres et clients
        fonctions.export_data(Allclients,'clients')      
        fonctions.export_data(Allbooks,'livres')
#endregion        
#region              (Fonction mise à jour des données)
def MAJ():
        save_data()
        call_data()
#endregion

# Appel de la fonction appel des données:
call_data()












# Definition de la fonction principale
def enter():

#region                   (Fonction Validation opération de prêt)
        def Valid_op_pr():
                MAJ()
                # Ajout du livre selectionné dans la liste de possessions du clients 
                Dictid[id].livposs.append(lendselectbook.get())
                # Ajout du client dans la liste des affectations du livre selectionné et modification quantité restante
                Dictbook[lendselectbook.get()].affectations.append(id)
                Dictbook[lendselectbook.get()].remaining_quantity = Dictbook[lendselectbook.get()].remaining_quantity - 1
                save_data()
                
#endregion                

#region                     (Fonction Valider pour nouveau client())              
        def Valider_pret_N():
                global id
                a = lendnom.get()
                b = lendprenom.get()
                c = lendcin.get()
                m = lendselectbook.get()
                if a == '':
                        showinfo('Information','Veuillez saisir un nom valid!')
                        return
                if b == '':
                        showinfo('Information','Veuillez saisir un prénom valid!')
                        return
                if c == '':
                        showinfo('Information','Veuillez saisir un N° CIN ou N° étudiant valid!')
                        return
                if m == '':
                        showinfo('Information','Veuillez choisir un livre de la liste déroulante!')
                        return
                Allclients.append(Client(lendnom.get().title(),lendprenom.get().title(),lendcin.get().upper(), 
                                         Allclients[-1].Id_client + 1, 'Non', []))                        
                pretwind = tk.Toplevel(root)
                
        #region                (Fonts et dimensions fenetre)       
                # Création des Fonts objects:
                bahnGras = font.Font(family='bahnschrift', size=9, weight='bold')
                font.families()
                bahnGrasgr = font.Font(family='bahnschrift', size=19, weight='bold')
                font.families()       
                pretwind_width = 800
                pretwind_height = 400
                pretwind.resizable(False,False)
                center_x3 = int(screen_width/2 - pretwind_width / 2)
                center_y3 = int(screen_height/2 - pretwind_height / 2)
                pretwind.geometry(f'{pretwind_width}x{pretwind_height}+{center_x3}+{center_y3}')
                pretwind.title('Prêt d\'un livre')
                pretwind.iconbitmap('librairie.ico')
        #endregion        
                
                
                
                headerlendframe = ttk.Frame(pretwind)
                headerlendlabel = ttk.Label(headerlendframe, text='Prêter un Livre', font=bahnGrasgr, anchor='center')
                headerlendlabel.pack(fill='x')
                headerlendframe.grid(row=0,columnspan=10,padx=10,pady=20)       
                # Information sur le Client
                Linfopersonlabel = ttk.Label(pretwind,
                                        text='Information sur le Client',
                                        justify=tk.CENTER,
                                        anchor='center',
                                        width=48,
                                        font= bahnGras)        
                Linfoperson = ttk.LabelFrame(pretwind, 
                                        borderwidth=3, 
                                        relief='sunken',
                                        labelanchor='n',
                                        labelwidget=Linfopersonlabel)
                        # Membre du club ou non       
                Lmembreinfo = ttk.Label(Linfoperson, text='- Le Client est un membre du Club ?')
                Lmembreinfo.pack(fill='x')       
                Lmembreres = ttk.Button(Linfoperson, command=None, text='Non! Devenir un membre ?')      
                Lmembreres.pack()
                        # Nom et prénom du client 
                Lmembreid = ttk.Label(Linfoperson, 
                                      text=f'- Nom et prénom du client : {Allclients[-1].nom} {Allclients[-1].prenom}')
                Lmembreid.pack(fill='x')
                        # Identifiant du Client
                id = Allclients[-1].Id_client 
                Lclientid = ttk.Label(Linfoperson, 
                                      text=f'- Identifiant Client : {id}')
                Lclientid.pack(fill='x')
                print(len(Allclients))
                        # Nombre de livre déjà en possession
                Lnumbook = ttk.Label(Linfoperson, text=f'- Nombre de livre en possession : {len(Allclients[-1].livposs)}')
                Lnumbook.pack(fill='x')
                Linfoperson.grid(row=1,column=0,columnspan=4,sticky='N', padx=10, pady=20, ipadx=10,ipady=10)
                # Information sur le Livre
                Linfobooklabel = ttk.Label(pretwind,
                                        text='Information sur le Livre',
                                        justify=tk.CENTER,
                                        anchor='center',
                                        width=48,
                                        font= bahnGras)        
                Linfobook = ttk.LabelFrame(pretwind, 
                                        borderwidth=3, 
                                        relief='sunken',
                                        labelanchor='n',
                                        labelwidget=Linfobooklabel)
                        # Quantité restant du livre
                Lbookquantity = ttk.Label(Linfobook, text=f'- Quantité restant du livre : {Dictbook[lendselectbook_combo.get()].remaining_quantity}')
                Lbookquantity.pack(fill='x')
                        # Prix d'achat du livre
                Lbookbuyprice = ttk.Label(Linfobook, text=f'- Le prix d\'achat du livre : {Dictbook[lendselectbook_combo.get()].price} DH')
                Lbookbuyprice.pack(fill='x')
                Lbookbuy = ttk.Button(Linfobook,text='Acheter le livre!', command=pretwind.destroy)
                Lbookbuy.pack()
                        # Prix de Prêt du livre
                Lbooklendprice = ttk.Label(Linfobook, text=f'- Le prix de Prêt du livre : {float(Dictbook[lendselectbook_combo.get()].price/10)} DH')
                Lbooklendprice.pack(fill='x')

                Linfobook.grid(row=1,column=5,columnspan=4,sticky='NS', padx=10, pady=20, ipadx=10,ipady=10)        
                # Validation de l'opération de pret
                lendvalidoperation = ttk.Button(pretwind, text='Valider l\'opération de Prêt !',padding=(10,10,10,10),command=Valid_op_pr)
                lendvalidoperation.grid(row=2, columnspan=10, sticky='N')
#endregion
                
#region                     (Fonction Valider pour ancien client())               
        def Valider_pret_A():
                global id
                a = lendidclt.get() 
                m = lendselectbook.get() 
                if a == '':
                        showinfo('Information','Veuillez saisir un Identifiant client valid!')
                        return
                if m == '':
                        showinfo('Information','Veuillez choisir un livre de la liste déroulante!')
                        return
                pretwind = tk.Toplevel(root)
                
        #region                (Fonts et dimensions fenetre)       
                # Création des Fonts objects:
                bahnGras = font.Font(family='bahnschrift', size=9, weight='bold')
                font.families()
                bahnGrasgr = font.Font(family='bahnschrift', size=19, weight='bold')
                font.families()       
                pretwind_width = 800
                pretwind_height = 400
                pretwind.resizable(False,False)
                center_x3 = int(screen_width/2 - pretwind_width / 2)
                center_y3 = int(screen_height/2 - pretwind_height / 2)
                pretwind.geometry(f'{pretwind_width}x{pretwind_height}+{center_x3}+{center_y3}')
                pretwind.title('Prêt d\'un livre')
                pretwind.iconbitmap('librairie.ico')
        #endregion        
                
                
                
                headerlendframe = ttk.Frame(pretwind)
                headerlendlabel = ttk.Label(headerlendframe, text='Prêter un Livre', font=bahnGrasgr, anchor='center')
                headerlendlabel.pack(fill='x')
                headerlendframe.grid(row=0,columnspan=10,padx=10,pady=20)       
                # Information sur le Client
                Linfopersonlabel = ttk.Label(pretwind,
                                        text='Information sur le Client',
                                        justify=tk.CENTER,
                                        anchor='center',
                                        width=48,
                                        font= bahnGras)        
                Linfoperson = ttk.LabelFrame(pretwind, 
                                        borderwidth=3, 
                                        relief='sunken',
                                        labelanchor='n',
                                        labelwidget=Linfopersonlabel)
                        # Membre du club ou non       
                Lmembreinfo = ttk.Label(Linfoperson, text='- Le Client est un membre du Club ?')
                Lmembreinfo.pack(fill='x')       
                Lmembreres = ttk.Button(Linfoperson, command=None, text=Lyesnoclub['text'])
                if Lyesnoclub['text'] == 'Non':
                        Lmembreres.config(text = 'Non! Devenir un membre ?')
                else:
                        Lmembreres.config(state=tk.DISABLED)       
                Lmembreres.pack()
                        # Nom et prénom du client 
                Lmembreid = ttk.Label(Linfoperson, text=f'- Nom et prénom du client : {Dictid[int(lendidclt_entry.get())].nom} {Dictid[int(lendidclt_entry.get())].prenom}')
                Lmembreid.pack(fill='x')
                        # Identifiant du Client
                id = int(lendidclt_entry.get())
                Lclientid = ttk.Label(Linfoperson, text=f'- Identifiant Client : {id}')
                Lclientid.pack(fill='x')
                        # Nombre de livre déjà en possession
                Lnumbook = ttk.Label(Linfoperson, text=f'- Nombre de livre en possession : {len(Dictid[int(lendidclt_entry.get())].livposs)}')
                Lnumbook.pack(fill='x')
                Linfoperson.grid(row=1,column=0,columnspan=4,sticky='N', padx=10, pady=20, ipadx=10,ipady=10)
                # Information sur le Livre
                Linfobooklabel = ttk.Label(pretwind,
                                        text='Information sur le Livre',
                                        justify=tk.CENTER,
                                        anchor='center',
                                        width=48,
                                        font= bahnGras)        
                Linfobook = ttk.LabelFrame(pretwind, 
                                        borderwidth=3, 
                                        relief='sunken',
                                        labelanchor='n',
                                        labelwidget=Linfobooklabel)
                        # Quantité restant du livre
                Lbookquantity = ttk.Label(Linfobook, text=f'- Quantité restant du livre : {Dictbook[lendselectbook_combo.get()].remaining_quantity}')
                Lbookquantity.pack(fill='x')
                        # Prix d'achat du livre
                Lbookbuyprice = ttk.Label(Linfobook, text=f'- Le prix d\'achat du livre : {Dictbook[lendselectbook_combo.get()].price} DH')
                Lbookbuyprice.pack(fill='x')
                Lbookbuy = ttk.Button(Linfobook,text='Acheter le livre!', command=pretwind.destroy)
                Lbookbuy.pack()
                        # Prix de Prêt du livre
                Lbooklendprice = ttk.Label(Linfobook, text=f'- Le prix de Prêt du livre : {float(Dictbook[lendselectbook_combo.get()].price/10)} DH')
                Lbooklendprice.pack(fill='x')

                Linfobook.grid(row=1,column=5,columnspan=4,sticky='NS', padx=10, pady=20, ipadx=10,ipady=10)        
                # Validation de l'opération de pret
                lendvalidoperation = ttk.Button(pretwind, text='Valider l\'opération de Prêt !',padding=(10,10,10,10),command=Valid_op_pr)
                lendvalidoperation.grid(row=2, columnspan=10, sticky='N')
#endregion 
                
                
                
                
                
    # if  login.get()!='login' or password.get()!='0000':
    #     showinfo(title='Information', message=f'Login ou Mot de passe erroné')
    # else:
        setwind = tk.Toplevel(root)
        root.iconify()
        
        def on_select1(event):
                selected = lenddomain_combo.get()
                lendsubdomain_combo.set('')
                lendselectbook_combo.set('')
                lendsubdomain_combo['values'] = DictDomain[selected]
                lendselectbook_combo['values'] = DictDombk[selected]
        def on_select2(event):
                selected = lendsubdomain_combo.get()
                lendselectbook_combo.set('')
                lendselectbook_combo['values'] = DictSubdomain[selected]
        def on_select6(event):
                selected = lendselectbook_combo.get()
                lenddomain_combo.set(Dictbook[selected].domain)
                lendsubdomain_combo.set(Dictbook[selected].subdomain)
        def focus_out1(event):
                selected = int(lendidclt_entry.get())
                if selected in Allid:
                        Lyesnoclub.config(text=Dictid[selected].membre_club)
                else:
                        showinfo("Information", "Identifiant ou client inexistant!")
                     
                
#region               (Fonts et dimensions fenetre)   
        # Création des Fonts objects:
        bahnGras = font.Font(family='bahnschrift', size=9, weight='bold')
        font.families()
        bahnGrasgr = font.Font(family='bahnschrift', size=19, weight='bold')
        font.families()
        
        # Définition des dimensions et caractéristiques de la fenetre:
        setwind_width = 800
        setwind_height = 600
        setwind.resizable(False,False)
        center_x2 = int(screen_width/2 - setwind_width / 2)
        center_y2 = int(screen_height/2 - setwind_height / 2)
        setwind.geometry(f'{setwind_width}x{setwind_height}+{center_x2}+{center_y2}')
        setwind.title('Acceuil')
        setwind.iconbitmap('librairie.ico')
        
        
        
        menu_tab = ttk.Notebook(setwind)
#endregion        
         
#region           (Prêt d'un Livre)       
        MAJ()
        # Cadre de Prêt d'un livre

        lendframe = ttk.Frame(menu_tab)
        headerlendframe = ttk.Frame(lendframe)
        headerlendlabel = ttk.Label(headerlendframe, text='Prêter un Livre', font=bahnGrasgr, anchor='center')
        headerlendlabel.pack(fill='x')
        headerlendframe.grid(row=0,columnspan=10,padx=10,pady=20)
            # Nouveau Client :
        lendpersonlabel1 = ttk.Label(lendframe,
                                    text='Nouveau Client',
                                    justify=tk.CENTER,
                                    anchor='center',
                                    width=48,
                                    font= bahnGras)
        
        lendperson1 = ttk.LabelFrame(lendframe, 
                                    borderwidth=3, 
                                    relief='sunken',
                                    labelanchor='n',
                                    labelwidget=lendpersonlabel1)
                # Nom
        Lnom = ttk.Label(lendperson1,text='Nom :')
        Lnom.pack(fill='x')
        lendnom = tk.StringVar()
        lendnom_entry= ttk.Entry(lendperson1,textvariable=lendnom)
        lendnom_entry.pack(fill='x')
                # Prénom
        Lprenom = ttk.Label(lendperson1,text='Prénom :')
        Lprenom.pack(fill='x')
        lendprenom = tk.StringVar()
        lendprenom_entry= ttk.Entry(lendperson1,textvariable=lendprenom)
        lendprenom_entry.pack(fill='x')
                # N° CIN ou N° étudiant
        Lcin = ttk.Label(lendperson1,text='N° CIN ou N° étudiant :')
        Lcin.pack(fill='x')
        lendcin = tk.StringVar()
        lendcin_entry= ttk.Entry(lendperson1,textvariable=lendcin)
        lendcin_entry.pack(fill='x')
                # Bouton de validation
        lendvalid1 = ttk.Button(lendperson1, text='Valider!', command=Valider_pret_N)
        lendvalid1.pack(padx=10,pady=10)        
        
            
        lendperson1.grid(column=0,row=1,columnspan=4,sticky='N', padx=5, pady=20, ipadx=10,ipady=10)
            # Ancien Client :
        lendpersonlabel2 = ttk.Label(lendframe,
                                    text='Ancien Client',
                                    justify=tk.CENTER,
                                    anchor='center',
                                    width=48,
                                    font= bahnGras)
        
        lendperson2 = ttk.LabelFrame(lendframe, 
                                    borderwidth=3, 
                                    relief='sunken',
                                    labelanchor='n',
                                    labelwidget=lendpersonlabel2)
                # Id Client
        Lidclient = ttk.Label(lendperson2,text='Identifiant du Client :')
        Lidclient.pack(fill='x')
        lendidclt = tk.StringVar()
        lendidclt_entry= ttk.Entry(lendperson2,textvariable=lendidclt)
        lendidclt_entry.pack(fill='x')
        lendidclt_entry.bind("<FocusOut>", focus_out1)
                # Id membre du club
        Lmembreclub = ttk.Label(lendperson2,text='Membre du Club ?')
        Lmembreclub.pack(fill='x')
        Lyesnoclub = ttk.Label(lendperson2)
        Lyesnoclub.pack(fill='x')        
                # Bouton de validation
        lendvalid2 = ttk.Button(lendperson2, text='Valider!', command=Valider_pret_A)
        lendvalid2.pack(padx=10,pady=10)        
        
        
        lendperson2.grid(column=5,row=1,columnspan=4,sticky='N', padx=5, pady=20, ipadx=10,ipady=10)         
            # Identité du Livre :
        lendbooklabel = ttk.Label(lendframe,
                                    text='Identité du Livre',
                                    justify=tk.CENTER,
                                    anchor='center',
                                    width=104,
                                    font= bahnGras)        
        lendbook = ttk.LabelFrame(lendframe, 
                                    borderwidth=3, 
                                    relief='sunken',
                                    labelanchor='n',
                                    labelwidget=lendbooklabel)
                # Domaine
        Ldomain = ttk.Label(lendbook,text='Domaine')
        Ldomain.pack(fill='x')
        lenddomain = tk.StringVar()
        lenddomain_combo= ttk.Combobox(lendbook,
                                       textvariable=lenddomain,
                                       state='readonly',
                                       values=Alldomain)
        lenddomain_combo.pack(fill='x')
        lenddomain_combo.bind("<<ComboboxSelected>>", on_select1)
                # sous Domaine
        Lsubdomain = ttk.Label(lendbook,text='Sous-domaine')
        Lsubdomain.pack(fill='x')
        lendsubdomain = tk.StringVar()
        lendsubdomain_combo= ttk.Combobox(lendbook,
                                          textvariable=lendsubdomain,
                                          state='readonly',
                                          values=Allsubdomain)
        
        lendsubdomain_combo.pack(fill='x')
        lendsubdomain_combo.bind("<<ComboboxSelected>>", on_select2)
                # Selection du Livre par ordre alphabétique
        Lselectbook = ttk.Label(lendbook,text='Sélection du livre (par ordre alphabétique)')
        Lselectbook.pack(fill='x')
        lendselectbook = tk.StringVar()
        lendselectbook_combo= ttk.Combobox(lendbook,
                                           textvariable=lendselectbook,
                                           state='readonly',
                                           values=Allname)
        lendselectbook_combo.pack(fill='x')
        lendselectbook_combo.bind("<<ComboboxSelected>>", on_select6)
        lendbook.grid(column=0,row=2,columnspan=8,sticky='N', padx=10, pady=20, ipadx=10,ipady=10)
#endregion       
        
        
        
        
        
        
       
       
       
        
        
        
        
        
#region               (Récupération d'un Livre)
        MAJ()
        def click1(event):
                try :
                        selected = int(Rid_entry.get())
                        for i in range(Rbook_listbox.size()):
                                Rbook_listbox.delete(0)
                        for i in Dictid[selected].livposs :
                                Rbook_listbox.insert(tk.END, i)
                except :
                        pass
        def Valider_recup():
                # supprimer le livre des possessions du client
                selected = Rbook_listbox.get(Rbook_listbox.curselection()[0])
                Dictid[int(Rid_entry.get())].livposs.remove(selected)
                # supprimer le id client des affectations du livre
                Dictbook[selected].affectations.remove(int(Rid.get()))
                MAJ()
        # Cadre de récupération d'un livre
        recoverframe = ttk.Frame(menu_tab)
        headerrecupframe = ttk.Frame(recoverframe)
        headerrecuplabel = ttk.Label(headerrecupframe, text='Récupérer un Livre', font=bahnGrasgr, anchor='center')
        headerrecuplabel.pack(fill='x')
        headerrecupframe.pack(fill='x')
        # Cadre Information client/livre
        inforecupframe = ttk.Frame(recoverframe)
        inforecupframe.pack(fill='x')
                # Id client:
        Ridlabel = ttk.Label(inforecupframe,text='Identifiant du Client : (Appuyer sur la touche ENTRER pour voir les livres en possession)')
        Ridlabel.pack(fill='x')
        Rid = tk.StringVar()
        Rid_entry= ttk.Entry(inforecupframe,textvariable=Rid)
        Rid_entry.pack(fill='x')
        
                # Selection du livre à récupérer parmis la liste des livres possédés par le client
        Rbooklabel = ttk.Label(inforecupframe,text='Livre à récupérer :')
        Rbooklabel.pack(fill='x')

        Rbook_listbox= tk.Listbox(inforecupframe)
        
        Rbook_listbox.pack(fill='x')
                # Bouton de validation
        recupvalid = ttk.Button(inforecupframe, text='Valider!', command=Valider_recup)
        recupvalid.pack(padx=20,pady=20)
        recoverframe.pack()
        recoverframe.bind("<Button-1>", click1)

#endregion

        
#region               (Vente d'un Livre)
        # Cadre de vente d'un livre
        sellframe = ttk.Frame(menu_tab)
        sellperson = ttk.LabelFrame(sellframe, 
                                    text='Information sur le Client',
                                    borderwidth=3, 
                                    relief='sunken')
        sellperson.grid(column=0,row=0,columnspan=4,sticky='N')
       
        sellbook = ttk.LabelFrame(sellframe, 
                                    text='Information sur le Livre',
                                    borderwidth=3, 
                                    relief='sunken')
        sellbook.grid(column=0,row=0,columnspan=4,sticky='N')   
#endregion       
        
    
#region               (Insértion d'un Livre)
        # Cadre Insertion d'un livre
        def Valider_insert():
        
                a = insertbook.get()
                b = insertdombk.get()
                c = insertsbdombk.get()
                try :
                        d = float(prixventbk.get())
                except :
                        showinfo('Information','Veuillez saisir un prix valid!')
                try :
                        e = int(insquantity.get())
                except :
                        showinfo('Information','Veuillez saisir une quantité valide!')
                
                if a.strip() == '':
                       showinfo('Information','Veuillez saisir le Nom du Livre!') 
                if b.strip() == '':
                       showinfo('Information','Veuillez saisir le Domain du Livre!')
                if c.strip() == '':
                       showinfo('Information','Veuillez saisir le Sous-domain du Livre!')
        
                if a in Allname:
                        
                        Dictbook[a].total_quantity = Dictbook[a].total_quantity + e
                        Dictbook[a].remaining_quantity = Dictbook[a].remaining_quantity + e
                else:
                        Allbooks.append(Livre(a,b,c,d,e,e,[]))
                        
                save_data()
                
                
                
                
        def on_select3(event):
                selected = insertbook_combo.get()
                if selected in Allname:
                     insertdombk_combo.set(Dictbook[selected].domain)
                     insertdombk_combo.config(state=tk.DISABLED)
                     insertsbdombk_combo.set(Dictbook[selected].subdomain)
                     insertsbdombk_combo.config(state=tk.DISABLED)
                     insquantrest.config(text=f'Quantité existante du livre sélectionné : {Dictbook[selected].remaining_quantity}')
                     insquanttot.config(text=f'Quantité totale du livre sélectionné : {Dictbook[selected].total_quantity}')
                     prixventbk_entry.config(state=tk.NORMAL)
                     prixventbk_entry.delete(0,tk.END)
                     prixventbk_entry.insert(0,Dictbook[selected].price)
                     prixventbk_entry.config(state=tk.DISABLED)
                     
                else:
                     insertdombk_combo.config(state=tk.NORMAL)
                     insertdombk_combo.set(value='')
                     insertsbdombk_combo.config(state=tk.NORMAL)
                     insertsbdombk_combo.set(value='')
                     insquantrest.config(text=f'Quantité existante du livre sélectionné : {00}')
                     insquanttot.config(text=f'Quantité totale du livre sélectionné : {00}')
                     prixventbk_entry.config(state=tk.NORMAL)
                     prixventbk_entry.delete(0,tk.END)   
        
        def on_select4(event):
                selected = insertdombk_combo.get()
                if selected in Alldomain:
                     insertsbdombk_combo.config(values=DictDomain[selected],
                                                   state='readonly')
                else:
                     insertsbdombk_combo.config(values=Allsubdomain,
                                                   state=tk.NORMAL)              
                
                
        insertframe = ttk.Frame(menu_tab)
        headerinsertframe = ttk.Frame(insertframe)
        headerinsertlabel = ttk.Label(headerinsertframe, text='Insérer un Livre', font=bahnGrasgr, anchor='center')
        headerinsertlabel.pack(fill='x')
        headerinsertframe.grid(row=0,columnspan=10,padx=10,pady=20)
            # Nom du livre :
        booknamelabel = ttk.Label(insertframe,
                                    text='Nom du Livre',
                                    justify=tk.CENTER,
                                    anchor='center',
                                    width=48,
                                    font= bahnGras)
        
        booknamelf = ttk.LabelFrame(insertframe, 
                                    borderwidth=3, 
                                    relief='sunken',
                                    labelanchor='n',
                                    labelwidget=booknamelabel)
                # Liste des livres existants ou insertion d'un nouveau livre:
        Bookslabel = ttk.Label(booknamelf,text='Choisir un livre existant ou insérer le nom d\'un nouveau livre :')
        Bookslabel.pack(fill='x')
        insertbook = tk.StringVar()
        insertbook_combo= ttk.Combobox(booknamelf,
                                       textvariable=insertbook,
                                       values=Allname)
        insertbook_combo.pack(fill='x')
        insertbook_combo.bind("<<ComboboxSelected>>", on_select3)
        insertbook_combo.bind("<Key>", on_select3)
        booknamelf.grid(column=0,row=1,sticky='N', padx=10, pady=20, ipadx=10,ipady=10)
        
            # Domain et sous-domain du livre
        bkdomlabel = ttk.Label(insertframe,
                                    text='Domain du Livre',
                                    justify=tk.CENTER,
                                    anchor='center',
                                    width=48,
                                    font= bahnGras)
        
        bkdomlf = ttk.LabelFrame(insertframe, 
                                    borderwidth=3, 
                                    relief='sunken',
                                    labelanchor='n',
                                    labelwidget=bkdomlabel)            
                # Domain du livre:
        Bkdomainlabel = ttk.Label(bkdomlf,text='Choisir un domain ou insérer un nouveau domain :')
        Bkdomainlabel.pack(fill='x')
        insertdombk = tk.StringVar()
        insertdombk_combo= ttk.Combobox(bkdomlf,
                                       textvariable=insertdombk,
                                       values=Alldomain)
        insertdombk_combo.pack(fill='x')
        insertdombk_combo.bind("<<ComboboxSelected>>", on_select4)
        insertdombk_combo.bind("<Key>", on_select4)
                # Sous-domain du livre
        Bksbdomainlabel = ttk.Label(bkdomlf,text='Choisir un sous-domain ou insérer un nouveau sous-domain :')
        Bksbdomainlabel.pack(fill='x')
        insertsbdombk = tk.StringVar()
        insertsbdombk_combo= ttk.Combobox(bkdomlf,
                                       textvariable=insertsbdombk,
                                       values=Allsubdomain)
        insertsbdombk_combo.pack(fill='x')
        
        bkdomlf.grid(column=0,row=2,sticky='N', padx=10, pady=20, ipadx=10,ipady=10)
            # Quantités :
        insquantitylb = ttk.Label(insertframe,
                                    text='Quantité',
                                    justify=tk.CENTER,
                                    anchor='center',
                                    width=48,
                                    font= bahnGras)
        
        insquantitylf = ttk.LabelFrame(insertframe, 
                                    borderwidth=3, 
                                    relief='sunken',
                                    labelanchor='n',
                                    labelwidget=insquantitylb)

                # Quantité restant
        exquant = 00
        insquantrest = ttk.Label(insquantitylf,text= f'Quantité existante du livre sélectionné : {exquant}')
        insquantrest.pack(fill='x')
                # Quantité Total
        totquant = 00
        insquanttot = ttk.Label(insquantitylf,text= f'Quantité totale du livre sélectionné : {totquant}')
        insquanttot.pack(fill='x')
                # Quantité à ajouter
        ajquantity = ttk.Label(insquantitylf,text='Quantité à ajouter :')
        ajquantity.pack(fill='x')
        insquantity = tk.StringVar()
        insquantity_entry= ttk.Entry(insquantitylf,textvariable=insquantity)
        insquantity_entry.pack(fill='x')
        insquantitylf.grid(column=4,row=2,sticky='N', padx=10, pady=20, ipadx=10,ipady=10)
            # Prix :

        insprixlb = ttk.Label(insertframe,
                                    text='Prix du Livre',
                                    justify=tk.CENTER,
                                    anchor='center',
                                    width=48,
                                    font= bahnGras)
        
        insprixlf = ttk.LabelFrame(insertframe, 
                                    borderwidth=3, 
                                    relief='sunken',
                                    labelanchor='n',
                                    labelwidget=insprixlb)

                # Prix de vente
        prixventlb = ttk.Label(insprixlf,text='Prix de vente (MAD) :')
        prixventlb.pack(fill='x')
        prixventbk = tk.StringVar()
        prixventbk_entry= ttk.Entry(insprixlf,textvariable=prixventbk)
        prixventbk_entry.pack(fill='x') 
        
        insprixlf.grid(column=4,row=1,sticky='N', padx=10, pady=20, ipadx=10,ipady=10)
        
        
           # Bouton de validation
        insertvalid = ttk.Button(insertframe, text='Valider!', command=Valider_insert)
        insertvalid.grid(columnspan=10,row=3,sticky='N', padx=10, pady=20, ipadx=10,ipady=10)
#endregion       
        
        


        
        
        
        
        
        
        
        
        
        
        
               
                
        # Ajout des cadres dans le Notebook     
        menu_tab.add(lendframe,text='Prêt d\'un livre')
        menu_tab.add(recoverframe,text='Récupération d\'un livre')
        # menu_tab.add(sellframe,text='Vente d\'un livre')
        menu_tab.add(insertframe,text='Insertion d\'un livre')
        menu_tab.pack(expand=1,pady=10,fill='both')
        
#region               (Création de la fenetre principale)
root = tk.Tk()
root.title('Gestionnaire de la librairie')
root_width = 600
root_height = 400

# get the screen dimension
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# find the center point
center_x = int(screen_width/2 - root_width / 2)
center_y = int(screen_height/2 - root_height / 2)

# set the position of the window to the center of the screen
root.geometry(f'{root_width}x{root_height}+{center_x}+{center_y}')

root.iconbitmap('librairie.ico')
login = tk.StringVar()
password = tk.StringVar()

login_Frame = tk.Frame(root)
login_label = ttk.Label(login_Frame, text= 'Login :')
login_label.grid(columnspan=2, column=0, sticky='W')
login_entry = ttk.Entry(login_Frame, textvariable=login, justify='center')
login_entry.grid(columnspan=4,row=0,column=2, pady=10)
password_label = ttk.Label(login_Frame,text= 'Password :')
password_label.grid(columnspan=2, column=0, row=1, sticky='W')
password_entry = ttk.Entry(login_Frame, textvariable=password, show='*', justify='center')
password_entry.grid(columnspan=4, column=2, row=1,pady=10)
login_button = ttk.Button(login_Frame,text='Enter!',command=enter)
login_button.grid(columnspan=2,column=3, row=3, pady=10)
login_Frame.place(in_=root, anchor='c', relx=0.5, rely=0.3)
root.mainloop()
#endregion







                
