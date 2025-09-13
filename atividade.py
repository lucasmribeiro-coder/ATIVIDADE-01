# Recebe o salário como float
salario = float(input("Insira por favor seu salário: "))

# Inicializa a variável para armazenar o imposto total
imposto_total = 0.0

#Verifica a isenção de impostos
if salario <= 2000.00:
    print("Isento")
else:
    # Cria uma cópia do salário para subtrair os valores já processados
    salario_restante = salario
    
    salario_restante -= 2000.00
    
    # Calcula a faixa de "até 3000"
    if salario_restante > 0:
        
        valor_na_faixa_1 = min(salario_restante, 1000.00)
        imposto_total += valor_na_faixa_1 * 0.08
        salario_restante -= valor_na_faixa_1
        
    # Calcula a faixa de "até 4500"
    if salario_restante > 0:
        valor_na_faixa_2 = min(salario_restante, 1500.00)
        imposto_total += valor_na_faixa_2 * 0.18
        salario_restante -= valor_na_faixa_2
        
    #Calcula a faixa de  "acima de R$ 4500.00"
    if salario_restante > 0:
        # O que sobrar entra nesta faixa
        valor_na_faixa_3 = salario_restante
        imposto_total += valor_na_faixa_3 * 0.28
        
    # Imprime o resultado formatado
    print(f"R$ {imposto_total:.2f}")