CUPOS_MAXIMOS = 30

N = int(input("¿Cuántos vehículos se van a registrar hoy? "))

sabado_texto = input("¿Es sábado? (True/False): ")
if sabado_texto == "True" or sabado_texto == "true":
    es_sabado = True
if sabado_texto == "False" or sabado_texto == "false":
    print("ERROR: valor de 'es_sabado' inválido. Se asumirá que no es sábado o el valor ingresado no es correcto. Se asumirá que no es sábado.")
    es_sabado = False
vehiculos_registrados = 0
total_recaudado = 0.0
total_estudiantes = 0
total_docentes = 0
total_visitantes = 0
suma_horas = 0.0

contador = 0

while contador < N and vehiculos_registrados < CUPOS_MAXIMOS:
    contador = contador + 1
    print("\n--- Vehículo", contador, "de", N, "---")

    placa = input("Placa: ")
    tipo_usuario = input("Tipo de usuario (E/D/V): ")
    hora_entrada = int(input("Hora de entrada (0-23): "))
    horas_permanencia = float(input("Horas que permanecerá parqueado: "))

    if hora_entrada < 0 or hora_entrada > 23 or type(hora_entrada) not in [int, float]:
        print("ERROR: hora de entrada inválida. Este vehículo no se contará en las estadísticas.")
        continue

    if horas_permanencia <= 0 or type(horas_permanencia) not in [int, float]:
        print("ERROR: horas de permanencia inválidas (negativas o cero). Registro rechazado.")
        continue

    if tipo_usuario != "E" and tipo_usuario != "D" and tipo_usuario != "V":
        print("ADVERTENCIA: tipo de usuario no reconocido, se tratará como visitante por defecto.")
        tipo_usuario = "V"
    cobro = 0.0
    if tipo_usuario == "E":
        if horas_permanencia <= 2:
            cobro = 0.0
        else:
            horas_adicionales = horas_permanencia - 2
            cobro = horas_adicionales * 800
    elif tipo_usuario == "D":
        cobro = horas_permanencia * 500
    else:
        if horas_permanencia <= 1:
            cobro = 1500.0
        else:
            horas_adicionales = horas_permanencia - 1
            cobro = 1500 + horas_adicionales * 1200

    if es_sabado and tipo_usuario == "V":
        cobro = cobro * 0.8

    if (hora_entrada >= 19 or hora_entrada < 6) and not es_sabado:
        cobro = cobro * 0.9

    cobro = round(cobro, 2)
    vehiculos_registrados = vehiculos_registrados + 1
    total_recaudado = total_recaudado + cobro
    suma_horas = suma_horas + horas_permanencia

    if tipo_usuario == "E":
        total_estudiantes = total_estudiantes + 1
    elif tipo_usuario == "D":
        total_docentes = total_docentes + 1
    else:
        total_visitantes = total_visitantes + 1

    print("Cobro para este vehículo: $" + str(cobro))

    if vehiculos_registrados == CUPOS_MAXIMOS:
        print("\nPARQUEADERO LLENO")

if vehiculos_registrados > 0:
    promedio_horas = suma_horas / vehiculos_registrados
else:
    promedio_horas = 0.0
ocupacion = (vehiculos_registrados / CUPOS_MAXIMOS) * 100
print("\n====== RESUMEN DEL DIA ======")
print("Vehiculos registrados:", vehiculos_registrados, "/", CUPOS_MAXIMOS)
print("Ocupacion:", round(ocupacion, 1), "%")
print("Recaudo total: $" + str(round(total_recaudado, 2)))
print("Estudiantes:", total_estudiantes, "| Docentes:", total_docentes, "| Visitantes:", total_visitantes)
print("Promedio de permanencia:", round(promedio_horas, 2), "horas")
print("================================")



