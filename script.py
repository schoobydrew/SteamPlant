pump = {}
boiler = {}
fuel = {}
turbine = {}
###
def readFile(fileName):
    f = open(fileName)
    line = f.readline().strip()
    data = {}
    x = []
    while (line != ""):
        x = line.split(",")
        data[x[0]] = [float(i) for i in x[1:]]
        line = f.readline().strip()
    f.close()
    return data
###
temp = {}
pressures = {}
temp = readFile("15MPA.csv")
pressures[15] = temp
temp.clear()
temp = readFile("20MPA.csv")
pressures[20] = temp
###
pump = readFile("pump_data.csv")
boiler = readFile("boiler_data.csv")
fuel = readFile("fuel_data.csv")
turbine = readFile("turbine_data.csv")
###
print pump
print boiler
print fuel
print turbine
print pressures
