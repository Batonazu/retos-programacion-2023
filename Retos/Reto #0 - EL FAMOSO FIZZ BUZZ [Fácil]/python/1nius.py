numeros = int(input("Cuantos numeros quieres calcular?"))

for i in range (1,numeros):
    if (i%15==0):
        print('fizzbuzz')
    elif(i%3==0):
        print('fizz')
    elif(i%5==0):
        print('buzz')
    else:
        print(i)
