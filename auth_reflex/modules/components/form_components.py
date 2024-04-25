import reflex as rx

def field_form_component(label:str, placeholder: str, name_var:str, 
                         on_change_function, type_field: str) -> rx.Component:
    return rx.form.field(
                rx.flex(
                    rx.form.label(label),
                    rx.form.control(
                        rx.input.input(
                            placeholder=placeholder,
                            on_change=on_change_function,
                            name=name_var,
                            type=type_field,
                            required=True,
                        ),
                        as_child=True,
                ),
                rx.form.message(
                        "Este campo es requerido",
                        match="valueMissing",
                        color="red",
                ),
                direction="column",
                spacing="2",
                align="stretch",
                ),
                name=name_var,
                width= "30vw"
            )

def field_form_component_general(label: str, placeholder: str, message_validate: str, name: str,
                       on_change_function, show  ) -> rx.Component:
    return rx.form.field(
                rx.flex(
                    rx.form.label(label),
                    rx.form.control(
                        rx.input.input(
                            placeholder=placeholder,
                            on_change=on_change_function,
                            name=name,
                            required=True
                        ),
                    as_child=True
                    ),
                    rx.form.message(
                        message_validate,
                        name=name,
                        match="valueMissing",
                        force_match=show,
                        color="red"
                    ),
                direction="column",
                spacing="2",
                align="stretch"
                ),
                name=name,
                width= "30vw"
            )



