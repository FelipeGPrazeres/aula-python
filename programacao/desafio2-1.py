def farenheintParaCelcius(temperatura):
    """
    Faz o cálculo da conversão de celcius para farenheit
    """
    return (temperatura - 32) * (5/9)

def celsiusParaFarenheint(temperatura):
    """
    Faz o cálculo da conversão de farenheit para celcius
    """
    return (temperatura * 1.8 + 32)


def main():
    """
    Lida com os inputs para definir os parâmetros de temperatura e tipo de temperatura, chamando as funções para calcular as devidas conversões
    """
    temperatura = float(input("Quantos graus? "))
    tipoTemperatura = input("Qual o tipo da temperatura? (F/C) ")

    if tipoTemperatura.upper() == "F":
        print(f"Em Celsius {farenheintParaCelcius(temperatura):.2f}, Em Farenheit {temperatura:.2f}")

    if tipoTemperatura.upper() == "C":
        print(f"A temperatura em Celsius é {temperatura} e em Farenheit {celsiusParaFarenheint(temperatura)}")
main()