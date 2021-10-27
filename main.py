import statistics

n1 = int(input("Ingrese primer dato númerico :"))
n2 = int(input("Ingrese el segundo dato númerico :"))
n3 = int(input("Ingrese el tercer dato númerico :"))
list = [n1, n2, n3]

mean = statistics.mean(list)
print("El valor medio es :" + str(mean))

median = statistics.median(list)
print("El valor de la mediana es :" + str(median))

variance = statistics.variance(list)
print("El valor de la variante es :" + str(variance))
