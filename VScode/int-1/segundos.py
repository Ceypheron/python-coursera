segundos = int(input("Por favor, entre com o número de segundos que deseja converter: "))
dia = segundos // 86400
resto_dia = segundos % 86400
hora = resto_dia // 3600
seg_restante = segundos % 3600
minutos = seg_restante // 60
segundos_finais = seg_restante % 60
print(dia,"dias,",hora,"horas,",minutos,"minutos e",segundos_finais,"segundos.")