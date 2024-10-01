import skfuzzy
from skfuzzy import control
import numpy as np

# parametros de entarda (controle)
TC = control.Antecedent(np.arange(0, 100, 1), 'TC')
AC = control.Antecedent(np.arange(0, 10, 1), 'AC')
AD = control.Antecedent(np.arange(0, 100, 1), 'AD')

rinse = control.Consequent(np.arange(0, 60, 1), 'rinse')
wash = control.Consequent(np.arange(0, 50, 1), 'wash')
spin = control.Consequent(np.arange(0, 180, 1), 'spin')

TC['thin'] = skfuzzy.trimf(TC.universe, [-50, 0, 50])
TC['thick'] = skfuzzy.trimf(TC.universe, [20, 50, 80])
TC['jean'] = skfuzzy.trimf(TC.universe, [50, 100, 150])

AC['little'] = skfuzzy.trimf(AC.universe, [-5, 0, 5])
AC['normal'] = skfuzzy.trimf(AC.universe, [2, 5, 8])
AC['large'] = skfuzzy.trimf(AC.universe, [5, 10, 15])

AD['small'] = skfuzzy.trimf(AD.universe, [-50, 0, 50])
AD['normal'] = skfuzzy.trimf(AD.universe, [20, 50, 80])
AD['large'] = skfuzzy.trimf(AD.universe, [50, 100, 150])

rinse['very_small'] = skfuzzy.trimf(rinse.universe, [-12.5, 0, 12.5])
rinse['small'] = skfuzzy.trimf(rinse.universe, [0, 12.5, 25])
rinse['normal'] = skfuzzy.trimf(rinse.universe, [15, 25, 35])
rinse['long'] = skfuzzy.trimf(rinse.universe, [25, 35, 45])
rinse['very_long'] = skfuzzy.trimf(rinse.universe, [40, 60, 80])

wash['small'] = skfuzzy.trimf(wash.universe, [-20, 0, 20])
wash['normal'] = skfuzzy.trimf(wash.universe, [10, 25, 40])
wash['large'] = skfuzzy.trimf(wash.universe, [35, 50, 50])

spin['very_small'] = skfuzzy.trimf(spin.universe, [0, 0, 40])
spin['small'] = skfuzzy.trimf(spin.universe, [30, 52.5, 75])
spin['normal'] = skfuzzy.trimf(spin.universe, [50, 75, 100])
spin['large'] = skfuzzy.trimf(spin.universe, [75, 107.5, 140])
spin['very_large'] = skfuzzy.trimf(spin.universe, [120, 180, 480])

TC.view()
AC.view()
AD.view()
rinse.view()
wash.view()
spin.view()

regra1 = control.Rule(AC['large'] & AD['large'], rinse['long'])
regra2 = control.Rule(AC['little'] & AD['small'], rinse['very_small'])
regra3 = control.Rule(AC['normal'] & AD['normal'], rinse['normal'])
regra4 = control.Rule(AC['normal'] & AD['small'], rinse['small'])
regra5 = control.Rule(AC['large'] & AD['normal'], rinse['long'])
regra6 = control.Rule(AC['normal'] & AD['large'], rinse['very_long'])
regra7 = control.Rule(AC['large'] & AD['small'], rinse['long'])
regra8 = control.Rule(AC['little'] & AD['large'], rinse['long'])

regra9 = control.Rule(AC['little'] & AD['small'], wash['small'])
regra10 = control.Rule(AC['normal'] & AD['small'], wash['small'])
regra11 = control.Rule(AC['large'] & AD['small'], wash['normal'])
regra12 = control.Rule(AC['little'] & AD['normal'], wash['small'])
regra13 = control.Rule(AC['normal'] & AD['normal'], wash['normal'])
regra14 = control.Rule(AC['large'] & AD['normal'], wash['large'])
regra15 = control.Rule(AC['little'] & AD['large'], wash['normal'])
regra16 = control.Rule(AC['normal'] & AD['large'], wash['large'])
regra17 = control.Rule(AC['large'] & AD['large'], wash['large'])

regra18 = control.Rule(TC['thin'] & AC['little'], spin['very_small'])
regra19 = control.Rule(TC['jean'] & AC['large'], spin['very_large'])
regra20 = control.Rule(TC['thin'] & AC['normal'], spin['small'])
regra21 = control.Rule(TC['thick'] & AC['normal'], spin['large'])
regra22 = control.Rule(TC['thick'] & AC['little'], spin['normal'])
regra23 = control.Rule(TC['thick'] & AC['large'], spin['large'])
regra24 = control.Rule(TC['thin'] & AC['large'], spin['normal'])
regra25 = control.Rule(TC['jean'] & AC['normal'], spin['large'])
regra26 = control.Rule(TC['jean'] & AC['little'], spin['normal'])

regras = control.ControlSystem([regra1, regra2, regra3, regra4, regra5, regra6, regra7, regra8,
                                regra9, regra10, regra11, regra12, regra13, regra14, regra15,
                                regra16, regra17, regra18, regra19, regra20, regra21, regra22,
                                regra23, regra24, regra25, regra26])

resultado = control.ControlSystemSimulation(regras)

resultado.input['TC'] = 50
resultado.input['AC'] = 5
resultado.input['AD'] = 50

resultado.compute()

print(resultado.output['rinse'])
print(resultado.output['wash'])
print(resultado.output['spin'])

wash.view(sim=resultado)
rinse.view(sim=resultado)
spin.view(sim=resultado)

input()
