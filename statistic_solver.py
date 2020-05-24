import numpy as np

confirmed = [35120.47403822038, 39142.75526423077, 41861.51942625632,44692.013622337705, 47894.94126527191, 50055.05525701823, 53779.389725546374, 57094.04740253642, 60594.92180295287,63835.09279057236, 67559.4272591005, 70352.6781104966, 73034.19892783687, 76609.56001762388, 80780.8146223754,84430.66240153299, 89086.08048719316, 93964.95864096502, 98620.37672662521, 103871.68832724988, 108527.10641291006,112623.87432829101, 117242.04906926591, 120817.41015905293]
deaths = [906.2043399113949, 987.5279736100833, 1080.549391072327,1135.966973970448, 1226.6114445035673, 1265.1767407468863,1367.1183860105623, 1464.012357458458, 1563.069617684545,1651.7644575904053, 1736.373085359681, 1797.5861456018465,1838.0476579346914, 1924.4990872557603, 2037.9248581320592,2152.712699720553, 2256.6306828803545, 2364.688292714474,2464.359820124492, 2535.4011553095534, 2656.9192286524208,2778.0901075000234, 2904.9229273473375, 2983.1485178575044]
days = [53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76]

for i in range(len(days)):
	print("\\textbf{" + str(days[i]) + "}" + " & " + str(round(confirmed[i], 0)) + " & " + str(round(deaths[i], 0)) + "\\\\\n\\hline")

 
