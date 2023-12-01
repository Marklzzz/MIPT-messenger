
import random
import string
import hashlib
import test
import pygame

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

def register(mail,text_pwd,displayname,user_arr):
    new_user = User(displayname,mail,hashlib.md5(text_pwd.encode()).hexdigest())
    user_arr.append(new_user)
    return True
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

pygame.init()
window = pygame.display.set_mode((500, 200))
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 40)

displayname_box = test.TextInputBox(50, 50, 400, font, 'Displayname')
email_box = test.TextInputBox(50,80,400,font, 'Email')
pwd_box = test.TextInputBox(50,110,400,font,'Password')
group = pygame.sprite.Group(displayname_box)
group.add(email_box)
group.add(pwd_box)

Result = {}
users = []
mails = []

for user in users:
    mails.append(user.mail)

run = True
while run:
    clock.tick(60)
    event_list = pygame.event.get()
    for event in event_list:
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                for box in group:
                    Result[box.inactive_text]=box.text
                print(Result)
                register(Result['Email'],Result['Password'],Result['Displayname'],users)
                print(users)
                run = False
    group.update(event_list, Result)

    window.fill(0)
    group.draw(window)
    pygame.display.flip()


pygame.quit()
exit()