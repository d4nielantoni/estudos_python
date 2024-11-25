class ConversorTemperatura:
    def celsius_para_fahrenheit(self, celsius):
        return (celsius * 9/5) + 32

celsius = float(input())

conversor = ConversorTemperatura()

fahrenheit = conversor.celsius_para_fahrenheit(celsius)
print(fahrenheit)
