def portada_de_app():
   # print('Primer app')
   # print('Gabriel A. Mendez Zarate')
    print("""
██╗  ██╗ █████╗ ███████╗██╗  ██╗     ██████╗ █████╗ ██╗      ██████╗██╗   ██╗██╗      █████╗ ████████╗███████╗
██║  ██║██╔══██╗██╔════╝██║  ██║    ██╔════╝██╔══██╗██║     ██╔════╝██║   ██║██║     ██╔══██╗╚══██╔══╝██╔════╝
███████║███████║███████╗███████║    ██║     ███████║██║     ██║     ██║   ██║██║     ███████║   ██║   █████╗  
██╔══██║██╔══██║╚════██║██╔══██║    ██║     ██╔══██║██║     ██║     ██║   ██║██║     ██╔══██║   ██║   ██╔══╝  
██║  ██║██║  ██║███████║██║  ██║    ╚██████╗██║  ██║███████╗╚██████╗╚██████╔╝███████╗██║  ██║   ██║   ███████╗
╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝     ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝   ╚═╝   ╚══════╝
                                                           < By Gabriel Adrian Mendez Zarate >
    """)

def calculando_el_hash(palabra):
    ubicacion = hash(palabra)
    print(f'Tu numero hash es el siguiente: {ubicacion}')

def solicitud_al_usuario():
    palabra = input('Favor de ingresar una frase: ')
    calculando_el_hash(palabra)

def main():
    portada_de_app()
    solicitud_al_usuario()

if main() == __name__:
    main()


