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

