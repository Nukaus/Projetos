faturamento = [67836.43, 36678.66, 29229.88, 27165.48, 19849.53]
estados = ["SP", "RJ", "MG", "ES", "Outros"]
faturamento_total = sum(faturamento)
valor_arredondado = round(faturamento_total, 2)

for i in range (len(faturamento)):
    percentual = (faturamento[i]/valor_arredondado)*100
    print(f"{estados[i]}: {round(percentual, 2)}%")


    
