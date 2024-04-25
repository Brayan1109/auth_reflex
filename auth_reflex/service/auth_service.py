from ..repositoy.user_repository import select_userb_by_email
import bcrypt as bc
import reflex as rx

def auth_user(email: str, password: str):
    #buscar usuario
    user = select_userb_by_email(email)
    if(user == None):
        raise BaseException('El usuario no existe')
    if(not validate_password(password, user.password)):
        raise BaseException('Credenciales incorrectas')
    rx.LocalStorage("pruebatoken", name="TOKEN")
    rx.Cookie(name="pruebatoken", max_age=3600)
    return True

def validate_password(password: str, password_db:str):
    #hashed = bc.hashpw(password.encode('utf-8'), bc.gensalt())
    return bc.checkpw(password.encode('utf-8'), password_db.encode('utf-8'))
    