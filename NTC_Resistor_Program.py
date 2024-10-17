import numpy as np
from scipy.constants import zero_Celsius
import matplotlib.pyplot as plt
import seaborn as sns

class NTC_Resistance:
    TERMISTOR_CONSTANT_KELVIN = 3450
    AMBIENT_RESISTANCE = 1
    AMBIENT_TEMPERATURE_KELVIN = 298.15

    def __init__(self, temperature):
        self.temperature = temperature
    
    def NTC_resistance_algorithm(self):
        final_temperature_converted = self.temperature + zero_Celsius

        inside_exp = NTC_Resistance.TERMISTOR_CONSTANT_KELVIN * (1/final_temperature_converted - 
                                                                 1/NTC_Resistance.AMBIENT_TEMPERATURE_KELVIN)

        resistance = NTC_Resistance.AMBIENT_RESISTANCE * np.exp(inside_exp)

        return resistance

    def show_numeric_result(self):
        index = 0

        for i in self.NTC_resistance_algorithm():
            print('#'*22)
            print(f'Temperature: {self.temperature[index]} °C\nResistance: {i:.3f} Ohm')

            index += 1
    
    def show_visual_result(self):
        fig = plt.figure(figsize=(5.5, 4.5))
        sns.lineplot(x=self.temperature, y=self.NTC_resistance_algorithm())
        plt.xlabel('Temperature (Celsius)')
        plt.ylabel('Resistance (Ohms)')
        plt.grid(True)
        plt.title('Variação da Resistência de um NTC')
        plt.show()

my_temperature = np.array([10, 20, 40, 60, 80, 100, 120])

main = NTC_Resistance(my_temperature)

main.show_numeric_result()
main.show_visual_result()