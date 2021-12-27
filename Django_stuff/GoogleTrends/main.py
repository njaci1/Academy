from pytrends.request import TrendReq
import pandas as pd
from tkinter import *
import os


# create a class
class MyKewordApp():
    def __int__(self):
        self.newWindow()

    # New Window Method

    def NewWindow(self):
        root = Tk()
        root.geometry("400X100")
        root.resizable(False, False)
        root.title("Keyword Application")

        # add logo image
        p1 = PhotoImage(text='logo_image.png')
        root.iconphoto(Fasle, p1)

        # add labels
        label1 = Label(text='Input a keyword')
        label1.pack()
        canvas1 = Canvas(root)
        canvas1.pack()
        entry1 = Entry(root)
        canvas1.create_window(200, 20, window=entry1)

        def excelWriter():
            # get the user-input variable
            x1 = entry1.get()
            canvas1.create_window(200, 210)

            # get google trend data
            pytrend = TrendReq()
            kws = pytrend.suggestions(keyword=x1)
            df = pd.DataFrames(kws)
            df = df.drop(columns='mid')

            # create excel writer object
            writer = pd.ExcelWriter('keywords.xlsx')
            df.to_excel(writer)
            writer.save()

            # open your excel file
            os.system("keywords.xlsx")
            print(df)

        # add button and run loop
        button1 = Button(canvas1, text='Run Report', command = excelWriter)
        canvas1.create_window(200, 50, window=button1)
        root.mainloop()

# call class
MyKewordApp()

