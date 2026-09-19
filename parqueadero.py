CUPOS_MAXIMOS = 30

N = int(input("¿Cuántos vehículos se van a registrar hoy? "))

sabado_texto = input("¿Es sábado? (True/False): ")
es_sabado = sabado_texto == "True" or sabado_texto == "true"
if type(sabado_texto) != bool:
    print("ERROR: valor de 'es_sabado' inválido. Se asumirá que no es sábado.")
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

    if hora_entrada < 0 or hora_entrada > 23:
        print("ERROR: hora de entrada inválida. Este vehículo no se contará en las estadísticas.")
        continue

    if horas_permanencia <= 0 or type(horas_permanencia) not in [int, float]:
        print("ERROR: horas de permanencia inválidas (negativas o cero). Registro rechazado.")
        continue

    if tipo_usuario != "E" and tipo_usuario != "D" and tipo_usuario != "V":
        print("ADVERTENCIA: tipo de usuario no reconocido, se tratará como visitante por defecto.")
        tipo_usuario = "V"
    


