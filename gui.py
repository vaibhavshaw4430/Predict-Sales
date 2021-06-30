from tkinter import *
import pickle

#Loading the model

model = pickle.load(open('finalized_model.sav', 'rb'))


#Initializing the tkinter window
master = Tk()
master.geometry("700x400")
master.configure(background='#b82a11')
master.title('Sales Estimater')

#Label to show the estimated sale
sale_label = Label(master, bg='#b82a11', fg="#3b231e", font=("Times", 40, "bold"), text="Predict Sale")
sale_label.pack(padx=5, pady=20)

#calculating sales w.r.t input
def calculate_sale(arg):
    res = model.predict([[tv.get(),radio.get(),newspaper.get()]])
    sale_label.config(text="Expected Sale : {:.2f}/-".format(res[0][0]))



#Scale to take TV advertising investment ammount from user
tv = Scale(master, length=650, label="TV", bg='#C4DFE6', fg="black", from_=0, to=2000, orient=HORIZONTAL , command=calculate_sale)
tv.set(0)
tv.pack(padx=5, pady=5)

#Scale to take Radio advertising investment ammount from user
radio = Scale(master, length=650, label="Radio", bg='#C4DFE6', fg="black",from_=0, to=2000, orient=HORIZONTAL, command=calculate_sale)
radio.set(0)
radio.pack(padx=5, pady=5)

#Scale to take Newspaper advertising investment ammount from user
newspaper = Scale(master, length=650, label="Newspaper", bg='#C4DFE6', fg="black", from_=0, to=2000, orient=HORIZONTAL, command=calculate_sale)
newspaper.set(0)
newspaper.pack(padx=5, pady=5)

mainloop()