password = "elmermenjivar"


password_usuario = input("Digite la contrasena para iniciar sesion: ")
if password_usuario == "":
    print("Por favor escriba una contrasena")

elif password_usuario == password:
    print("Contrasena Correcta!")

else:
    print("Contrasena Incorrecta!")    