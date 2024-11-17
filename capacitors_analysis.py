import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

class CapacitorsAnalysis:
    RESISTANCE_OHMS = 1000
    VOLTAGE = 100
    CAPACITANCY_F = 100e-6

    def __init__(self, time: float):
        self.time = time
        self.tau = CapacitorsAnalysis.RESISTANCE_OHMS * CapacitorsAnalysis.CAPACITANCY_F
    
    def charging_equation_one(self):
        return CapacitorsAnalysis.VOLTAGE * (1 - np.exp(-self.time / self.tau))
    
    def charging_equation_two(self):
        return (CapacitorsAnalysis.VOLTAGE / CapacitorsAnalysis.RESISTANCE_OHMS) * np.exp(-self.time/self.tau)
    
    def discharging_equation_one(self):
        return CapacitorsAnalysis.VOLTAGE * np.exp(-self.time / self.tau)
    
    def discharging_equation_two(self):
        return -(CapacitorsAnalysis.VOLTAGE / CapacitorsAnalysis.RESISTANCE_OHMS) * np.exp(-self.time/self.tau)


    def graph(self):
        fig, ax = plt.subplots(nrows=2, ncols=2, figsize=(12, 8))

        plt.subplots_adjust(
            bottom=0.069,
            top=0.96,
            hspace=0.297,
            right=0.97
        )

        sns.lineplot(x=self.time, y = self.charging_equation_one(), ax=ax[0, 0])
        ax[0, 0].set_xlabel('Tempo (s)')
        ax[0, 0].set_ylabel('Tensão (V)')
        ax[0, 0].set_title('Carregamento do Capacitor (I)')
        ax[0, 0].grid(True)

        sns.lineplot(x=self.time, y=self.discharging_equation_one(), ax=ax[0, 1])
        ax[0, 1].set_xlabel('Tempo (s)')
        ax[0, 1].set_ylabel('Tensão (V)')
        ax[0, 1].set_title('Descarregamento do Capacitor (I)')
        ax[0, 1].grid(True)

        sns.lineplot(x=self.time, y=self.charging_equation_two(), ax=ax[1, 0])
        ax[1, 0].set_xlabel('Tempo (s)')
        ax[1, 0].set_ylabel('Intensdade da Corrente (A)')
        ax[1, 0].set_title('Carregamento do Capacitor (II)')
        ax[1, 0].grid(True)

        sns.lineplot(x=self.time, y=self.discharging_equation_two(), ax=ax[1, 1])
        ax[1, 1].set_xlabel('Tempo (s)')
        ax[1, 1].set_ylabel('Intesidade da corrente (A)')
        ax[1, 1].set_title('Descarregamento do Capacitor (II)')
        ax[1, 1].grid(True)

        plt.tight_layout()

        plt.show()

time = np.arange(0, 2, 0.005)

analysis = CapacitorsAnalysis(time)
analysis.graph()

df = pd.DataFrame(
    {
        'time': time,
        'charge voltage one': analysis.charging_equation_one(),
        'discharge voltage one': analysis.discharging_equation_one(),
        'charge voltage two': analysis.charging_equation_two(),
        'discharge voltage two': analysis.discharging_equation_two()
    }
)
