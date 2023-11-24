
import random
import string


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
        while rndstring in ChatDataBase.codes:
            rndstring = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(12)])
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