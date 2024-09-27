def portada_de_app():
   # print('Primer app')
   # print('Gabriel A. Mendez Zarate')
    print("""
                   _____      _                                                                                      
                  |  __ \    (_)                                                                                     
                  | |__) | __ _ _ __ ___   ___ _ __    __ _ _ __  _ __                                               
                  |  ___/ '__| | '_ ` _ \ / _ \ '__|  / _` | '_ \| '_ \                                              
                  | |   | |  | | | | | | |  __/ |    | (_| | |_) | |_) |                                             
                  |_|   |_|  |_|_| |_| |_|\___|_|     \__,_| .__/| .__/                                              
      _____       _          _      _                __  __| |   | |       _            ______               _       
     / ____|     | |        (_)    | |     /\       |  \/  |_|   |_|      | |          |___  /              | |      
    | |  __  __ _| |__  _ __ _  ___| |    /  \      | \  / | ___ _ __   __| | ___ ____    / / __ _ _ __ __ _| |_ ___ 
    | | |_ |/ _` | '_ \| '__| |/ _ \ |   / /\ \     | |\/| |/ _ \ '_ \ / _` |/ _ \_  /   / / / _` | '__/ _` | __/ _ 
    | |__| | (_| | |_) | |  | |  __/ |  / ____ \ _  | |  | |  __/ | | | (_| |  __// /   / /_| (_| | | | (_| | ||  __/
     \_____|\__,_|_.__/|_|  |_|\___|_| /_/    \_(_) |_|  |_|\___|_| |_|\__,_|\___/___| /_____\__,_|_|  \__,_|\__\___|
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


