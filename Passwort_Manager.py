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
        Schliessen = ttk.Button(self.root, text='Schließen', command=lambda: self.root.quit())
        passwHinzu.pack(ipadx=5, ipady=5, expand=True)
        passwAus.pack(ipadx=5, ipady=5, expand=True)
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
        website = input('Von welcher Website wollen Sie das Passwort?  ')
        listenel = self.ListenelementGeben(website)
        if listenel is None:
            raise Exception('Für die Website ' + website + ' existiert kein Eintrag')
        w, user, passw = listenel
        print('Website: ' + str(website) + '\n' + 'Benutzername: ' + str(user) + '\n' + 'Passwort: ' + str(passw))

    def alleElementeAusgeben(self):
        i = 0
        for element in self.Passwortliste:
            web, user, passw = element
            i += 1
            print(str(i) + '.Eintrag \n   Website: ' + str(web) + '\n' + '   Benutzername: ' + str(user) + '\n' + '   Passwort: ' + str(passw))

    def ElementLoeschen(self):
        web = input('Welches Passwort möchten sie löschen? ')
        ele = self.ListenelementGeben(web)
        if ele is None:
            raise Exception('Für die Website ' + web + ' existiert kein Eintrag')
        self.Passwortliste.remove(ele)
        self.Aenderungen_Speichern()

    def alleElementeLoeschen(self):
        result = tkinter.messagebox.askquestion('Passwort_Manager', 'Sind Sie sicher? ')
        if result == 'yes':
            self.Passwortliste.clear()
            self.Aenderungen_Speichern()
            theLabel = Label(self.root, text="Liste gelöscht.")
            theLabel.pack()
        else:
            self.root.destroy()  # Closing Tkinter window forcefully.


    def ListenelementGeben(self, website):
        for element in self.Passwortliste:
            a, b, c = element
            if a == website:
                return element

    def Aenderungen_Speichern(self):
        with open('passworter.pickle', 'wb') as PasswortListe:
            pickle.dump(self.Passwortliste, PasswortListe)
