import pickle
import tkinter
from tkinter import *
from tkinter import ttk
import tkinter.messagebox
class Passwort_Manager:
    def __init__(self):
        with open('passworter.pickle', 'rb') as PasswortListe:
            try:
                self.Passwortliste = pickle.load(PasswortListe)
            except:
                self.Passwortliste = []
        self.root = Tk()
        self.root.title('Passwort Manager')
        self.root.geometry('600x400+50+50')
        passwHinzu = ttk.Button(self.root, text='Passwort hinzufügen', command=lambda: self.Passwort_Hinzufuegen())
        passwAus = ttk.Button(self.root, text='Passwort ausgeben', command=lambda: self.Passwort_Ausgeben())
        allePasswaus = ttk.Button(self.root, text= 'Alle Passwörter ausgeben', command=lambda: self.alleElementeAusgeben())
        PasswLoeschen = ttk.Button(self.root, text= 'Passwort löschen', command=lambda: self.ElementLoeschen())
        allepasswloeschen = ttk.Button(self.root, text='Alle Passwörter löschen', command=lambda: self.alleElementeLoeschen())
        Schliessen = ttk.Button(self.root, text='Schließen', command=lambda: self.root.quit())
        passwHinzu.pack(ipadx=5, ipady=5, expand=True)
        passwAus.pack(ipadx=5, ipady=5, expand=True)
        allePasswaus.pack(ipadx=5, ipady=5, expand=True)
        PasswLoeschen.pack(ipadx=5, ipady=5, expand=True)
        allepasswloeschen.pack(ipadx=5, ipady=5, expand=True)
        Schliessen.pack(ipadx=5, ipady=5, expand=True)
        self.root.mainloop()


    def Passwort_Hinzufuegen(self):
        website = tkinter.StringVar()
        username = tkinter.StringVar()
        password = tkinter.StringVar()
        passwHinzu = Tk()
        passwHinzu.title('Passwort hinzufügen')
        passwHinzu.geometry('300x150')
        # Website
        website_label = ttk.Label(passwHinzu, text="Website:")
        website_label.pack(fill='x', expand=True)

        website_entry = ttk.Entry(passwHinzu, textvariable=website)
        website_entry.pack(fill='x', expand=True)
        # Benutzername
        user_label = ttk.Label(passwHinzu, text="Benutzername/ Email:")
        user_label.pack(fill='x', expand=True)

        user_entry = ttk.Entry(passwHinzu, textvariable=username)
        user_entry.pack(fill='x', expand=True)
        # Passwort
        passw_label = ttk.Label(passwHinzu, text="Passwort:")
        passw_label.pack(fill='x', expand=True)

        passw_entry = ttk.Entry(passwHinzu, textvariable=password, show='*')
        passw_entry.pack(fill='x', expand=True)

        Fertig = ttk.Button(passwHinzu, text='Fertig', command=lambda: passwortandern())
        Fertig.pack(fill='x', expand=True)
        def passwortandern():
            web = website_entry.get()
            usern = user_entry.get()
            passw = passw_entry.get()
            self.Passwortliste.append((web, usern, passw))
            self.Aenderungen_Speichern()
            passwHinzu.destroy()

    def Passwort_Ausgeben(self):
        passwaus = Tk()
        web = tkinter.StringVar()
        passwaus.title('Passwort ausgeben')
        passwaus.geometry('300x150')
        website_label = ttk.Label(passwaus, text="Website:")
        website_label.pack(fill='x', expand=True)
        website_entry = ttk.Entry(passwaus, textvariable=web)
        website_entry.pack(fill='x', expand=True)
        Fertig = ttk.Button(passwaus, text='Fertig', command=lambda: return_Passwort())
        Fertig.pack(fill='x', expand=True)
        def return_Passwort():
            website = website_entry.get()
            listenel = self.ListenelementGeben(website)
            if listenel is None:
                tkinter.messagebox.showerror(title='Passwort ausgeben', message='Für die Website ' + website + ' existiert kein Eintrag')
            else:
                w, user, passw = listenel
                # print('Website: ' + str(website) + '\n' + 'Benutzername: ' + str(user) + '\n' + 'Passwort: ' + str(passw))
                website_entry.destroy()
                website_entry_2 = ttk.Label(passwaus, text=w)
                website_entry_2.pack(fill='x', expand=True)
                user_label = ttk.Label(passwaus, text="Benutzername/ Email:")
                user_label.pack(fill='x', expand=True)

                user_entry = ttk.Label(passwaus, text=user)
                user_entry.pack(fill='x', expand=True)
                # Passwort
                passw_label = ttk.Label(passwaus, text="Passwort:")
                passw_label.pack(fill='x', expand=True)

                passw_entry = ttk.Label(passwaus, text=passw)
                passw_entry.pack(fill='x', expand=True)
                Fertig.destroy()
                Leave = ttk.Button(passwaus, text='Fertig', command=lambda: passwaus.destroy())
                Leave.pack(fill='x', expand=True)

    def alleElementeAusgeben(self):
        elementeListe = []
        passwaus = Tk()
        passwaus.title('Alle Passwörter')
        i = 0
        for element in self.Passwortliste:
            web, user, passw = element
            i += 1
            entry = ttk.Label(passwaus,text=str(i)+'. Eintrag:')
            entry.pack(fill='x', expand=True)
            # Website

            website_label = ttk.Label(passwaus, text="      Website:")
            website_label.pack(fill='x', expand=True)

            website_entry_2 = ttk.Label(passwaus, text="            "+web)
            website_entry_2.pack(fill='x', expand=True)
            # Username
            user_label = ttk.Label(passwaus, text="      Benutzername/ Email:")
            user_label.pack(fill='x', expand=True)

            user_entry = ttk.Label(passwaus, text="            "+user)
            user_entry.pack(fill='x', expand=True)
            # Passwort
            passw_label = ttk.Label(passwaus, text="      Passwort:")
            passw_label.pack(fill='x', expand=True)

            passw_entry = ttk.Label(passwaus, text="            "+passw)
            passw_entry.pack(fill='x', expand=True)

            Abschluss = Canvas(passwaus, height=5, width=150, bg='black')
            Abschluss.pack(fill='x', expand=True)
            elementeListe.append((entry, website_label, website_entry_2, user_label, user_entry, passw_label, passw_entry))

            print(str(i) + '.Eintrag \n   Website: ' + str(web) + '\n' + '   Benutzername: ' + str(user) + '\n' + '   Passwort: ' + str(passw))
        # Fertig
        Leave = ttk.Button(passwaus, text='Fertig', command=lambda: passwaus.destroy())
        Leave.pack(fill='x', expand=True)

        geo = '300x' + str(150*len(elementeListe))
        passwaus.geometry(geo)
    def ElementLoeschen(self):
        passwaus = Tk()
        webe = tkinter.StringVar()
        passwaus.title('Passwort löschen')
        passwaus.geometry('300x150')
        website_label = ttk.Label(passwaus, text="Von welcher Website möchten Sie den Eintrag löschen?")
        website_label.pack(fill='x', expand=True)
        website_entry = ttk.Entry(passwaus, textvariable=webe)
        website_entry.pack(fill='x', expand=True)
        button = ttk.Button(passwaus, text='Passwort löschen', command=lambda: passwortandern())
        button.pack(fill='x', expand=True)
        def passwortandern():
            web = website_entry.get()
            passwaus.destroy()
            ele = self.ListenelementGeben(web)
            if ele is None:
                tkinter.messagebox.showinfo('Passwort_Manager', 'Für die Website ' + web + ' existiert kein Eintrag')
            else:
                result = tkinter.messagebox.askquestion('Passwort_Manager', 'Sind Sie sicher? ')
                if result == 'yes':
                    self.Passwortliste.remove(ele)
                    self.Aenderungen_Speichern()
    def alleElementeLoeschen(self):
        result = tkinter.messagebox.askquestion('Passwort_Manager', 'Sind Sie sicher? ')
        if result == 'yes':
            self.Passwortliste.clear()
            self.Aenderungen_Speichern()
            theLabel = Label(self.root, text="Liste gelöscht.")
            theLabel.pack()



    def ListenelementGeben(self, website):
        for element in self.Passwortliste:
            a, b, c = element
            if a == website:
                return element

    def Aenderungen_Speichern(self):
        with open('passworter.pickle', 'wb') as PasswortListe:
            pickle.dump(self.Passwortliste, PasswortListe)
