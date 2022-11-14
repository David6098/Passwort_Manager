import pickle
import tkinter
from tkinter import *
from tkinter import ttk
import tkinter.messagebox
from cryptography.fernet import Fernet
class Passwort_Manager:
    def __init__(self):

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


        try:
            with open('filekey.key', 'rb') as filekey:
                key = filekey.read()
            # using the key
            fernet = Fernet(key)

            # opening the encrypted file
            with open('passworter.pickle', 'rb') as enc_file:
                encrypted = enc_file.read()

            # decrypting the file
            decrypted = fernet.decrypt(encrypted)

            # opening the file in write mode and
            # writing the decrypted data
            with open('passworter.pickle', 'wb') as dec_file:
                dec_file.write(decrypted)
            with open('passworter.pickle', 'rb') as PasswortListe:
                self.Passwortliste = pickle.load(PasswortListe)
        except:
            self.Passwortliste = []
            key = Fernet.generate_key()

            # string the key in a file
            with open('filekey.key', 'wb') as filekey:
                filekey.write(key)
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
        with open('filekey.key', 'rb') as filekey:
            key = filekey.read()

            # using the generated key
        fernet = Fernet(key)
        # opening the original file to encrypt
        with open('passworter.pickle', 'rb') as file:
            original = file.read()

        # encrypting the file
        encrypted = fernet.encrypt(original)

        # opening the file in write mode and
        # writing the encrypted data
        with open('passworter.pickle', 'wb') as encrypted_file:
            encrypted_file.write(encrypted)
