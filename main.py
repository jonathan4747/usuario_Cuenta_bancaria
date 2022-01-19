from Cuenta import Usuario
from Cuenta import Cuenta

Persona=Usuario("Jonathan")
Cuenta1=Persona.cuenta=Cuenta(200)
Cuenta2=Persona.cuenta=Cuenta(300)
Persona.deposito_usuario(200).retiro_usuario(20).imprimir_usuario()
Persona.deposito_usuario(200).retiro_usuario(20).imprimir_usuario()



