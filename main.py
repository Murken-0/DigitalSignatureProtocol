from tkinter import *
from tkinter.messagebox import showinfo
import math
from protocol.utils.integer import *
from protocol.curve import *
from protocol.privateKey import *
from protocol.publicKey import *

def prime_test1():
    global p
    if is_prime_simple(p):
        showinfo(title="Перебор", message="Тест 1: P простое")
    else:
        showinfo(title="Перебор", message="Тест 1: P составное")

def prime_test2():
    global p
    if is_prime_whilson(p):
        showinfo(title="Теорема Вильсона", message="Тест 2: P простое")
    else:
        showinfo(title="Теорема Вильсона", message="Тест 2: P составное")

def is_prime_simple(number: int):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def is_prime_whilson(n):
    if (math.factorial(n-1)+1) % n!=0:
        return False
    else:
        return True
    
def generate_prime():
    global p
    p = 2
    while not is_prime_simple(p):
        p = RandomInteger.between(1, secp256k1.N - 1)
    label_p.configure(text=str(p))

def gen_keys():
    global private, public, p
    private = PrivateKey(secret=p)
    lab
    

form_sender = Tk()
form_reciever = Tk()

form_sender.geometry("550x550+400+200")
form_reciever.geometry("550x550+1000+200")
form_sender.title("Отправитель")
form_reciever.title("Получатель")
p_prost = Button(form_sender,text="Сгенерировать число P", command=generate_prime).place(x = 10, y = 230)
p_prov1 = Button(form_sender,text="Тест1. Проверка числа P на простоту", command=prime_test1).place(x = 300, y = 230)
p_prov2 = Button(form_sender,text="Тест2. Проверка числа P на простоту", command=prime_test2).place(x = 300, y = 260)
label_p = Label(form_sender, text="P: ")
label_p.place(x = 160, y = 230)
gen_keys = Button(form_sender, text="Сгенерировать ключи", command=gen_keys).place(x = 10, y = 290)
label_public = Label(form_sender, text="Открытый ключ: ")
label_public.place(x = 160, y = 290)
label_private = Label(form_sender, text="Закрытый ключ: ")
label_private.place(x = 350, y = 290)
otpr1 = Button(form_sender, text="Отправить открытый ключ", command= otpr1).place(x = 10, y = 320)
sash = Button(form_sender, text="Вычислить хэш значение", command= hashir).place(x = 10, y = 350)
labelH = Label(form_sender, text="H: ")
labelH.place(x = 200, y = 350)
podp = Button(form_sender, text="Подпись", command = podp).place(x = 10, y = 380)
labelrs = Label(form_sender, text="(r,s)")
labelrs.place(x = 100, y = 380)
labelk = Label(form_sender, text = "K: ")
labelk.place(x= 400, y = 380)
otpr2 = Button(form_sender, text="Отправить получателю", command= otpr2).place(x = 10, y = 410)

editor1 = Text(form_sender)
editor2 = Text(form_sender)
editor3 = Text(form_reciever)
editor4 = Text(form_reciever)
editor5 = Text(form_reciever)
editor1.place(relx=0.01, rely=0.01, width=280, height=200)
editor2.place(relx=0.50, rely=0.01, width=280, height=200)
editor3.place(relx=0.01, rely=0.01, width=280, height=200)
editor4.place(relx=0.50, rely=0.01, width=280, height=200)
editor5.place(relx=0.50, rely=0.40, width=280, height=200)
labelY2 = Label(form_reciever, text="Y: ")
labelY2.place(x = 10, y = 230)
labelp2 = Label(form_reciever, text="P: ")
labelp2.place(x = 10, y = 260)
labelg2 = Label(form_reciever, text="G: ")
labelg2.place(x = 10, y = 290)
labelrs2 = Label(form_reciever, text="(r, s): ")
labelrs2.place(x = 10, y = 320)
labelH2 = Label(form_reciever, text="H: ")
labelH2.place(x = 10, y = 350)
labelgen2 = Label(form_reciever, text="Открытый ключ: ")
labelgen2.place(x = 10, y = 380)
button1 = Button(form_reciever, text = "Вычислить хэш-значение", command= button1).place(x = 10, y = 410)
button2 = Button(form_reciever, text = "Проверить хэш-значения", command= button2).place(x = 10, y = 440)
verify_signature = Button(form_reciever, text = "Проверить подпись", command= verify_signature).place(x = 10, y = 470)
form_reciever.mainloop()
