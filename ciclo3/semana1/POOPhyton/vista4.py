import ejercicioclase3 as ec

tiempoHoras = int(input("Ingrese el tiempo transcurrido en horas: "))
tiempoMinutos = int(input("Ingrese el tiempo transcurrido en minutos: "))

cliente = ec.Cliente(tiempoHoras, tiempoMinutos)
print(f'{cliente.getTiempoHoras()} h {cliente.getTiempoMinutos()} min')
print("El total a pagar es:", cliente.pagoEstacionamiento())