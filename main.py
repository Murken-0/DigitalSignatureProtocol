from tkinter import *
from tkinter.messagebox import showinfo

from protocol.privateKey import PrivateKey
from hashlib import sha256
from protocol.binary import *
from protocol.ecdsa import Ecdsa

def generate_keys():
    global private, public
    private = PrivateKey()
    label_private.configure(text="Приватный ключ: " + str(private))
    public = private.publicKey()
    label_public.configure(text="Открытый ключ: " + str(public))

def send_key():
    global public
    label_public2.configure(text="Открытый ключ: " + str(public))

def sign_message():
    global signature, private, message, hashed_message
    message = editor_msg1.get("1.0", END)[:-1]
    hashed_message = sha256(message.encode("utf-8")).hexdigest()
    editor_hash1.delete("1.0", END)
    editor_hash1.insert("1.0", hashed_message)
    signature = Ecdsa.sign(intFromHex(hashed_message), private)
    labelrs.configure(text="(r, s) = " + str(signature))

def send_info():
    global signature, message, hashed_message
    labelrs2.configure(text="(r, s):" + str(signature))
    editor_msg2.delete("1.0", END)
    editor_msg2.insert("1.0", message)
    editor_hash2.delete("1.0", END)
    editor_hash2.insert("1.0", hashed_message)

def hash_again():
    global message
    editor_check_hash.delete("1.0", END)
    editor_check_hash.insert("1.0", sha256(message.encode("utf-8")).hexdigest())

def check_hash_equal():
    global hashed_message
    if hashed_message == editor_check_hash.get("1.0", END)[:-1]:
        showinfo("Результат", "Совпадают")
    else:
        showinfo("Результат", "Не совпадают, сообщение повреждено")

def verify_signature():
    global hashed_message, public, signature
    if Ecdsa.verify(intFromHex(hashed_message), signature, public):
        showinfo("Проверка подписи", "Подпись верна")
    else:
        showinfo("Проверка подписи", "Подпись не верна")

form_sender = Tk()
form_sender.title("Отправитель")
form_sender.geometry("750x550+0+200")

Button(form_sender, text="Сгенерировать ключи", command=generate_keys).place(x = 10, y = 210)
label_private = Label(form_sender, text="Закрытый ключ: ")
label_private.place(x = 10, y = 240)
label_public = Label(form_sender, text="Открытый ключ: ")
label_public.place(x = 10, y = 270)
Button(form_sender, text="Отправить открытый ключ", command=send_key).place(x = 10, y = 330)

Button(form_sender, text="Подпись", command=sign_message).place(x = 10, y = 380)
labelrs = Label(form_sender, text="(r,s)")
labelrs.place(x = 10, y = 410)
Button(form_sender, text="Отправить получателю", command=send_info).place(x = 10, y = 470)

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

Button(form_reciever, text = "Вычислить хэш-значение", command=hash_again).place(x = 10, y = 290)
Button(form_reciever, text = "Проверить хэш-значения", command=check_hash_equal).place(x = 10, y = 320)
Button(form_reciever, text = "Проверить подпись", command=verify_signature).place(x = 10, y = 350)

label_public2 = Label(form_reciever, text="Открытый ключ: ")
label_public2.place(x = 10, y = 420)

labelrs2 = Label(form_reciever, text="(r, s)")
labelrs2.place(x = 10, y = 480)
form_reciever.mainloop()
