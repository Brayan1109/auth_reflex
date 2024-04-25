import reflex as rx
import re
import asyncio
from ..service.auth_service import auth_user
from .components.form_components import field_form_component,field_form_component_general
from .components.notify_component import notify_component


class LoginState(rx.State):
    username: str = 'example@mail.com'
    password: str
    loader: bool = False
    error_create_user: str = ''

    @rx.background
    async def auth_user(self, data: dict):
        async with self:
            self.loader = True
            try:
                resp = auth_user(data['username'], data['password'])
                self.loader = False
                if(resp == True):
                    return rx.redirect('/')
            except BaseException as be:
                self.error_create_user = be.args
                self.loader = False
                print(be.args)
        await self.handleNotify()

    async def handleNotify(self):
        async with self:
            await asyncio.sleep(2)
            self.error_create_user = ''

    @rx.var
    def user_invalid(self)->bool:
        return not (re.match(r"[^@]+@[^@]+.[^@]+", self.username) and "example@mail.com")
    
    @rx.var
    def user_empty(self)->bool:
        return not self.username.strip()

    @rx.var
    def password_empty(self)->bool:
        return not (self.password.strip())

    @rx.var
    def validate_fields(self) -> bool:
        return (
            self.user_empty
            or self.user_invalid
            or self.password_empty
        )
    

@rx.page(route='/login', title='Login')
def login_page() -> rx.Component:
    return rx.section(
        rx.flex(
            #rx.image(src='/login.jpeg', width="300px", border_radius="15px 50px"),
            rx.heading('Inicio de sesión'),
            rx.form.root(
                rx.flex(
                    field_form_component_general("Usuario", "Ingrese su correo", "Ingrese un correo valido", "username",
                                                     LoginState.set_username, LoginState.user_invalid),

                    field_form_component("Contraseña", "Ingrese su contraseña", "password", 
                                             LoginState.set_password, "password"),
                    
                    rx.form.submit(
                            rx.cond(
                                LoginState.loader,
                                rx.chakra.spinner(color="red", size="xs"),
                                rx.button(
                                    "Iniciar sesión",
                                    disabled=LoginState.validate_fields,
                                    width="30vw"
                                ),
                            ),
                            as_child=True,  
                        ),
                        direction="column",
                        justify="center",
                        align="center",
                        spacing="2",
                ),
                on_submit=LoginState.auth_user,
                reset_on_submit=False,
                width="80%",
            ),
            width="100%",
            direction="column",
            align="center",
            justify="center",
        ),
        rx.cond(
                LoginState.error_create_user != '',
                notify_component(LoginState.error_create_user, 'shield-alert', 'yellow'),
                ),
        style=style_section,
        justify="center",
        width="100%",
    )

style_section = {
    "height": "90vh",
    "width": "80%",
    "margin": "auto",
}