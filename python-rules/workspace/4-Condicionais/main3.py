salario = float(input ("Digite aqui o valor do seu sálario:"))

if salario <= 1000:
    print("Você receberá o valor de um estagiario!")
elif salario > 1000 and salario <= 3000:
    print("Você receberá o valor de um programador júnior")
elif salario > 3000 and salario <= 6000:
    print ("Você receberá o valor de um programador pleno")
elif salario > 6000 and salario <= 15000:
    print ("Meu fi recebe que nem um senior!")
else:
    print("Meu fi é gerente de projetos")