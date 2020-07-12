from tkinter import *
from constructor import construct

class Ripper(Frame):
    def __init__(self, master=None):
        self.sites = []
        self.numSites = 0

        Frame.__init__(self, master)

        self.master = master
        self.start()
        self.base()
        self.form()

    def start(self):

        self.master.title = "Anime Ripper"
        self.pack(fill=BOTH, expand=1)

    def base(self):
        self.descrip = Label(self, text="Type in a twist.moe link to rip it!")
        self.descrip.place(x=0,y=10)

        self.saveSpace = Label(self, text="File location:")
        self.saveSpace.place(x=0,y=30)

        self.saveSpaceI = Entry(self)
        self.saveSpaceI.place(x=100,y=30)

        self.submit = Button(self, text="Download", command=self.rip)
        self.submit.place(x=0,y=75)

        self.addSite = Button(self, text="+", command=self.form)


    def form(self):

        if self.numSites == 0:
            yValue = 50
        else:
            yValue = self.numSites*20 + 50

        self.page = Label(self, text="Link:")
        self.page.place(x=0, y=yValue)

        self.pageI = Entry(self)
        self.pageI.place(x=100, y=yValue)
        self.addSite.place(x=240, y=yValue)
        self.sites.append(self.pageI) #Creates a list of all the entries made by the user

        self.submit.place(x=0, y=(yValue + 25))

        self.numSites += 1
    def rip(self):
        locationF = self.saveSpaceI.get()
        pages = []

        self.saveSpaceI.delete(0,END)

        for i in self.sites:
            print(i.get())
            pages.append(rf"{i.get()}")
            i.delete(0,END)

        for i in pages:
            construct(locationF, i)



if __name__ == "__main__":
    root = Tk()
    root.geometry("400x300")

    app = Ripper(root)

    root.mainloop()