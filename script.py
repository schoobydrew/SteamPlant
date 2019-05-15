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
    return data
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
