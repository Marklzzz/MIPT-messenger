
import random
import string
import hashlib

mails = ['golovinov.ga@phystech.edu']
hashed_pwd = ['d4b126fc3e49ef51512a2aedb90bfc55']

def check_for_user(mail):
    '''
    Проверяет, что пользователь с такой почтой уже есть
    '''
    if mail in mails:
        return True #нужно чтобы возвращало самого User
    else:
        return False
def check_hashed_pwd(text_pwd, user):
    '''
    Проверяет что введенный пользователем пароль совпадает с паролем в базе
    loginuser - пользователь под чьим именем пытаемся залогиниться
    '''
    hashed = hashlib.md5(text_pwd.encode())
    if user.hash_pwd == hashed.hexdigest():
        return True
    else:
        return False

def register(mail,text_pwd,displayname):
    new_user = User(displayname,mail,hashlib.md5(text_pwd.encode()).hexdigest())
    # должно отправить нового юзера в базу данных

class User:
    '''
    displayname - имя пользователя на экране
    mail - почта использованная для регистрации
    hash_pwd - хэшированный пароль
    chats - массив чатов в которых пользователь находится
    seenat - время последнего выхода
    '''
    def __init__(self, displayname, mail, hash_pwd):
        self.displayname = displayname
        self.mail = mail
        self.hash_pwd = hash_pwd
        self.chats = []
class Chat:
    '''
    id - скрытый идентификатор
    code - код для приглашения (доступа)
    messages - сообщения в чате
    users - пользователи чата

    '''
    def __init__(self, id):
        self.id = id
        # проверка на то, что в базе кодов такого кода еще не было (на всякий случай)
        rndstring = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(12)])
        # while rndstring in ChatDataBase.codes:
        #     rndstring = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(12)])
        self.code = rndstring
        self.messages = []
class Message:
    '''
    id - идентификатор
    text - текст сообщения
    '''
    def __init__(self, id, text):
        self.id = id
        self.text = text

golovinov = User('barsikkeglya','golovinov.ga@phystech.edu','d4b126fc3e49ef51512a2aedb90bfc55')

print(check_for_user('golovinov.ga@phystech.edu'))
print(check_hashed_pwd('Phystech',golovinov))