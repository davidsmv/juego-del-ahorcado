import os
import random
def run():
    #para abrir el archivo que tiene todas la palabras y agregar las palabras a una lista

    with open("./archivos/data.txt", "r", encoding="utf-8") as f:
        palabras = [line.replace("\n", "") for line in f]
    
    #para que salgan las palabras aleatoriamente
    random.shuffle(palabras)
    #inicio del juego
    #elige una palabra del documento
    for palabra in palabras:
        #usuario -> palabra que se va creando por lo que inicia el usuario
        usuario = ""

        #El juego iniciará con 15 vidas
        vidas = 15

        #palabra_usuario -> para crear  los _ _ _ _ con base en el largo de la palabra a adivinar
        palabra_usuario = ["_" for letra in range(1, len(palabra)+1)]

        #para eliminar las tildes de la palabra y el usuario no tenga que colocar las vocales con tilde
        tildes = palabra.maketrans('áéíóú', 'aeiou')
        sin_tilde_palabra = palabra.translate(tildes)

        #crear la palabra en lista para poder iterarla más adelante
        palabra_lista = list(sin_tilde_palabra)

        #mientras la palabra del usuario no sea igual a la palabra a adivinar se ejecuta este ciclo while
        while sin_tilde_palabra != usuario:

            #para poder jugar el usuario debe tener más de 0 vidas
            if vidas > 0:

                #imprime en pantalla -> le solicitara al usuario una letra
                print("\nAdivina la palabra! \n")
                print("Tienes "+ str(vidas)+" vidas \n")
                print(" ".join(palabra_usuario))
                letra = input("\ningresa una letra:")

                #depende la letra que ingrese el usuario empezará con este ciclo for a reemplazar los "_ " con la letra que ingreso el usuario para que en el siguiente ciclo se muestre lo del usuario con base en las letras que hace match.
                indice = -1 #el ciclo siempre inicia en -1 porque el primero en revisar será el indice 0
                for caracter in palabra_lista:
                    #este ciclo reemplaza la letra en el mismo index que la palabra que se intenta adivinar
                    indice +=1
                    if letra == caracter:
                        palabra_usuario[indice]=letra
                #crea la nueva palabra que hasta el momento a creado el usuario ej_: _ _a _
                usuario = "".join(palabra_usuario)

                #para limpiar la pantalla 
                os.system("cls")

                #se va ajustando las vidas en cada ciclo
                vidas -= 1

                #si el usuario adivina la palabra si aún no ha perdido todas las vidas
                if sin_tilde_palabra == usuario:
                    print("""
                            ⢀⡴⠑⡄⠀⠀⠀⠀⠀⠀⠀⣀⣀⣤⣤⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ 
                            ⠸⡇⠀⠿⡀⠀⠀⠀⣀⡴⢿⣿⣿⣿⣿⣿⣿⣿⣷⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀ 
                            ⠀⠀⠀⠀⠑⢄⣠⠾⠁⣀⣄⡈⠙⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀ 
                            ⠀⠀⠀⠀⢀⡀⠁⠀⠀⠈⠙⠛⠂⠈⣿⣿⣿⣿⣿⠿⡿⢿⣆⠀⠀⠀⠀⠀⠀⠀ 
                            ⠀⠀⠀⢀⡾⣁⣀⠀⠴⠂⠙⣗⡀⠀⢻⣿⣿⠭⢤⣴⣦⣤⣹⠀⠀⠀⢀⢴⣶⣆ 
                            ⠀⠀⢀⣾⣿⣿⣿⣷⣮⣽⣾⣿⣥⣴⣿⣿⡿⢂⠔⢚⡿⢿⣿⣦⣴⣾⠁⠸⣼⡿ 
                            ⠀⢀⡞⠁⠙⠻⠿⠟⠉⠀⠛⢹⣿⣿⣿⣿⣿⣌⢤⣼⣿⣾⣿⡟⠉⠀⠀⠀⠀⠀ 
                            ⠀⣾⣷⣶⠇⠀⠀⣤⣄⣀⡀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀ 
                            ⠀⠉⠈⠉⠀⠀⢦⡈⢻⣿⣿⣿⣶⣶⣶⣶⣤⣽⡹⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀ 
                             ⠀⠀⠀⠀⠀⠀⠀⠉⠲⣽⡻⢿⣿⣿⣿⣿⣿⣿⣷⣜⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀ 
                            ⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣷⣶⣮⣭⣽⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀ 
                            ⠀⠀⠀⠀⠀⠀⣀⣀⣈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀ 
                            ⠀⠀⠀⠀⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀ 
                            ⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀ 
                            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠻⠿⠿⠿⠿⠛⠉
   .g8MMMbgd       db      `7MN.   `7MF'    db       .MMMMbgd MMP""MM""YMM `7MMMMMYMM  
.dP'     `M      ;MM:       MMN.    M      ;MM:     ,MI    "Y P'   MM   `7   MM    `7  
dM'       `     ,V^MM.      M YMb   M     ,V^MM.    `MMb.          MM        MM   d    
MM             ,M  `MM      M  `MN. M    ,M  `MM      `YMMNq.      MM        MMmmMM    
MM.    `7MMF'  AbmmmqMA     M   `MM.M    AbmmmqMA   .     `MM      MM        MM   Y  , 
`Mb.     MM   A'     VML    M     YMM   A'     VML  Mb     dM      MM        MM     ,M 
  `"bmmmdPY .AMA.   .AMMA..JML.    YM .AMA.   .AMMA.P"Ybmmd"     .JMML.    .JMMmmmmMMM   
---------------------------------------------------------------------------------------""") 
                    print("La palabra correcta era: "+ palabra)
                    vidas = 15
                    respuesta = input("\n ¿Quieres volver a jugar? Marca 1 si quieres o 0 para terminar: ")
                    if respuesta == "1":
                        os.system("cls")
                    else:
                        #si el usuario no quiere volver a jugar se cierra el programa
                        quit()
            #si el usuario pierde todas sus vidas
            else:
                print("""
                    ⠄⢀⣀⣤⣴⣶⣶⣤⣄⡀⠄⠄⣀⣤⣤⣤⣤⡀⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
                    ⣴⣏⣹⣿⠿⠿⠿⠿⢿⣿⣄⢿⣿⣿⣿⣿⣿⣋⣷⡄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
                    ⣿⢟⣩⣶⣾⣿⣿⣿⣶⣮⣭⡂⢛⣭⣭⣭⣭⣭⣍⣛⣂⡀⠄⠄⠄⠄⠄⠄⠄⠄
                    ⣿⣿⣿⣿⡿⢟⣫⣭⣷⣶⣾⣭⣼⡻⢛⣛⣭⣭⣶⣶⣬⣭⣅⡀⠄⠄⠄⠄⠄⠄
                    ⣿⡿⢏⣵⣾⣿⣿⣿⡿⢉⡉⠙⢿⣇⢻⣿⣿⣿⣿⡟⠉⠉⢻⡷⠄⠄⠄⠄⠄⠄
                    ⣿⣷⣾⣍⣛⢿⣿⣿⣿⣤⣁⣤⣿⢏⠸⣿⣿⣿⣿⣷⣬⣥⣾⠁⣿⣿⣷⠄⠄⠄
                    ⣿⣿⣿⣿⣭⣕⣒⠿⠭⠭⠭⡷⢖⣫⣶⣶⣬⣭⣭⣭⣭⣥⡶⢣⣿⣿⣿⠄⠄⠄
                    ⣿⣿⣿⣿⣿⣿⣿⡿⣟⣛⣭⣾⣿⣿⣿⣝⡛⣿⢟⣛⣛⣁⣀⣸⣿⣿⣿⣀⣀⣀
                    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
                    ⣿⡿⢛⣛⣛⣛⣙⣛⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣬⣭⣭⠽⣛⢻⣿⣿⣿⠛⠛⠛
                    ⣿⢰⣿⣿⣿⣿⣟⣛⣛⣶⠶⠶⠶⣦⣭⣭⣭⣭⣶⡶⠶⣾⠟⢸⣿⣿⣿⠄⠄⠄
                    ⡻⢮⣭⣭⣭⣭⣉⣛⣛⡻⠿⠿⠷⠶⠶⠶⠶⣶⣶⣾⣿⠟⢣⣬⣛⡻⢱⣇⠄⠄
                    ⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⠶⠒⠄⠄⠄⢸⣿⢟⣫⡥⡆⠄⠄
                    ⢭⣭⣝⣛⣛⣛⣛⣛⣛⣛⣿⣿⡿⢛⣋⡉⠁⠄⠄⠄⠄⠄⢸⣿⢸⣿⣧⡅⠄⠄
                    ⣶⣶⣶⣭⣭⣭⣭⣭⣭⣵⣶⣶⣶⣿⣿⣿⣦⡀⠄⠄⠄⠄⠈⠡⣿⣿⡯⠁⠄⠄
`7MMMMMMq.`7MMMMMYMM  `7MMMMMMMq.  `7MMMMMYb.`7MMF' .MMMMbgd MMP""MM""YMM `7MMMMMYMM  
  MM   `MM. MM    `7    MM   `MM.   MM    `Yb. MM  ,MI    "Y P'   MM   `7   MM    `7  
  MM   ,M9  MM   d      MM   ,M9    MM     `Mb MM  `MMb.          MM        MM   d    
  MMmmdM9   MMmmMM      MMmmdM9     MM      MM MM    `YMMNq.      MM        MMmmMM    
  MM        MM   Y  ,   MM  YM.     MM     ,MP MM  .     `MM      MM        MM   Y  , 
  MM        MM     ,M   MM   `Mb.   MM    ,dP' MM  Mb     dM      MM        MM     ,M 
.JMML.    .JMMmmmmMMM .JMML. .JMM..JMMmmmdP' .JMML.P"Ybmmd"     .JMML.    .JMMmmmmMMM 
_____________________________________________________________________________________
\n""")
                respuesta = input("\n ¿Quieres volver a jugar? Marca 1 si quieres o 0 para terminar: ")
                if respuesta == "1":
                    os.system("cls")
                    break
                    
                else:
                    #si el usuario no quiere volver a jugar se cierra el programa
                    quit()


    

if __name__ == "__main__":
    run()