from tkinter import *
from tkinter.messagebox import showinfo

from random import SystemRandom
from hashlib import sha256
from protocol.curve import *
from protocol.privateKey import PrivateKey
from protocol.ecdsa import Ecdsa
from protocol.curve import secp256k1

def generate_multiplyer():
    global n
    n = SystemRandom().randrange(1, secp256k1.N - 1)
    label_n.configure(text="n: " + str(n))

def generate_keys():
    global private, public, n
    private = PrivateKey(secret=n)
    label_private.configure(text="Приватный ключ: " + private.toString())
    public = private.publicKey()
    label_public.configure(text="Открытый ключ: " + public.toString())

def send_key():
    global public
    label_public2.configure(text="Открытый ключ: " + public.toString())

def sign_message():
    global h, signature, private, message
    message = editor_msg1.get("1.0", END)[:-1]
    editor_hash1.delete("1.0", END)
    editor_hash1.insert("1.0", sha256(editor_msg1.get("1.0", END).encode("utf-8")).digest())
    signature, h = Ecdsa.sign(message, private)
    label_H.configure(text="H:" + str(h))
    labelrs.configure(text="(r, s) = " + str(signature.r) + ", " + str(signature.s))

def send_info():
    global signature, public, h, message, hash
    hash = editor_hash1.get("1.0", END)
    label_public2.configure(text="Открытый ключ: " + public.toString())
    label_H2.configure(text="H: " + str(h))
    labelrs2.configure(text="(r, s) = " + str(signature.r) + ", " + str(signature.s))
    editor_msg2.delete("1.0", END)
    editor_msg2.insert("1.0", message)
    editor_hash2.delete("1.0", END)
    editor_hash2.insert("1.0", hash)

def hash_again():
    editor_check_hash.delete("1.0", END)
    editor_check_hash.insert("1.0", sha256(editor_msg2.get("1.0", END).encode("utf-8")).digest())

def check_hash_equal():
    global hash
    if hash == editor_check_hash.get("1.0", END):
        showinfo("Результат", "Совпадают")
    else:
        showinfo("Результат", "Не совпадают, сообщение повреждено")

def verify_signature():
    global message, public, signature
    if Ecdsa.verify(message, signature, public):
        showinfo("Проверка подписи", "Подпись верна")
    else:
        showinfo("Проверка подписи", "Подпись не верна")

form_sender = Tk()
form_sender.title("Отправитель")
form_sender.geometry("750x550+0+200")

Button(form_sender,text="Сгенерировать число n", command=generate_multiplyer).place(x = 10, y = 230)
label_n = Label(form_sender, text="n: ")
label_n.place(x = 10, y = 260)

Button(form_sender, text="Сгенерировать ключи", command=generate_keys).place(x = 10, y = 290)
label_private = Label(form_sender, text="Закрытый ключ: ")
label_private.place(x = 10, y = 320)
label_public = Label(form_sender, text="Открытый ключ: ")
label_public.place(x = 10, y = 350)
Button(form_sender, text="Отправить открытый ключ", command=send_key).place(x = 10, y = 380)

Button(form_sender, text="Подпись", command=sign_message).place(x = 10, y = 410)
label_H = Label(form_sender, text="H: ")
label_H.place(x = 10, y = 440)
labelrs = Label(form_sender, text="(r,s)")
labelrs.place(x = 10, y = 470)
Button(form_sender, text="Отправить получателю", command=send_info).place(x = 10, y = 500)

editor_msg1 = Text(form_sender)
editor_msg1.place(relx=0.01, rely=0.01, width=280, height=200)

editor_hash1 = Text(form_sender)
editor_hash1.place(relx=0.50, rely=0.01, width=280, height=200)

form_reciever = Tk()
form_reciever.title("Получатель")
form_reciever.geometry("750x550+760+200")

editor_msg2 = Text(form_reciever)
editor_msg2.place(relx=0.01, rely=0.01, width=280, height=200)

editor_hash2 = Text(form_reciever)
editor_hash2.place(relx=0.50, rely=0.01, width=280, height=200)

editor_check_hash = Text(form_reciever)
editor_check_hash.place(relx=0.50, rely=0.40, width=280, height=200)

Button(form_reciever, text = "Вычислить хэш-значение", command=hash_again).place(x = 10, y = 320)
Button(form_reciever, text = "Проверить хэш-значения", command=check_hash_equal).place(x = 10, y = 350)
Button(form_reciever, text = "Проверить подпись", command=verify_signature).place(x = 10, y = 380)

label_public2 = Label(form_reciever, text="Открытый ключ: ")
label_public2.place(x = 10, y = 440)

label_H2 = Label(form_reciever, text="H: ")
label_H2.place(x = 10, y = 470)

labelrs2 = Label(form_reciever, text="(r, s): ")
labelrs2.place(x = 10, y = 500)
form_reciever.mainloop()
