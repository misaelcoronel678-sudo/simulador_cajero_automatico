"""Simulador de Cajero Automatico"""

#le pedimos al usuario la cantidad de dinero que tiene
saldo = int(input('ingresa la cantidad de saldo que tienes: '))
print ('-'*30)
#le pedimos al usuario que ingrese el monto a retirar
retiro = int(input('ingresa la cantidad de dinero a retirar: '))
print ('-'*30)
#el cajero tiene dinero?
cajero_tiene_dinero = True

#si el retiro es menor que el saldo y el cajero si tiene dinero entonces
if retiro < saldo and cajero_tiene_dinero:
	#restamos el saldo y el retiro
	saldo_restante = saldo - retiro
	#y le decimos al usuario que el retiro fue exitoso y cuanto dinero le queda
	print (f'El retiro se concreto Exitosamente y quedan {saldo_restante:,.0f} Gs')
	print ('-'*30)

#si esto no se cumple entonces	
else:
	#si el cajero no tiene dinero entonces
	if not cajero_tiene_dinero:
			#le decimos al usuario que el retiro no fue posible porque el cajero esta fuera de servicio
			print ('No fue posible hacer el retiro el cajero esta fuera de Servicio')
			print ('-'*30)
	
	#si esto otro tampoco se cumple entonces 
	elif retiro > saldo or retiro < 0:
			#le decimos al usuario que el retiro no fue posible porque no tiene el dinero suficiente
			print ('No fue posible hacer el retiro Fondos Insuficientes o ingresaste numeros Negativos')	
			print ('-'*30)	
