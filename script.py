
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
# temp.clear()
# temp = readFile("20MPA.csv")
# pressures[20] = temp
###
pump = readFile("pump_data.csv")
boiler = readFile("boiler_data.csv")
fuel = readFile("fuel_data.csv")
turbine = readFile("turbine_data.csv")
###
# print pump
# print boiler
# print fuel
# print turbine
# print pressures
def interpolate(opTemp):
    low = "0"
    high = "10000"
    for i in pressures[15]:
        if ((opTemp > int(i)) and (int(i) > int(low))):
            low = i
        if ((opTemp < int(i)) and (int(i) < int(high))):
            high = i
    h_low = pressures[15][low][2]
    h_high = pressures[15][high][2]
    s_low = pressures[15][low][3]
    s_high = pressures[15][high][3]
    h = ((h_high-h_low)/(int(high)-int(low)))*(opTemp - int(low)) + (h_low)
    s = ((s_high-s_low)/(int(high)-int(low)))*(opTemp - int(low)) + (s_low)
    return h, s

def getTableData(opTemp):
    if str(int(opTemp)) in pressures[15]:
        h = pressures[15][str(int(opTemp))][2]
        s = pressures[15][str(int(opTemp))][3]
    else:
        h, s = interpolate(opTemp)
    return h, s
def solve():
    n = pump[p][1]
    W = .001043*(15450-100)
    W_p_in = W/n
    h_pumpO = W_p_in + 417.51
    ###
    n = turbine[t][2]
    Temp = turbine[t][1]
    P_1 = 15000
    h_1, s_1 = getTableData(Temp)
    h_turbineI = h_1
    x_4 = (s_1-1.3028)/(6.0562)
    h_2s = 417.51 + (x_4)*2257.5
    h_2a = (h_1) - n*(h_1-h_2s)
    h_turbineO = h_2a
    ###
    h_1 = h_turbineI
    h_2 = h_turbineO
    W_out = 25000
    m_w = W_out/(h_1-h_2-W_p_in)
    ###
    h_1 = h_pumpO*.97
    h_2 = h_turbineI/.97
    hv = fuel[f][0]
    he = boiler[b][boil]
    m_c = m_w*(h_2-h_1)/(hv*he)
    ###
    h_1 = h_turbineO
    h_2 = 417.51
    T2 = 300.15
    cp = 4.18
    T1 = T2-(h_2-h_1)/cp
    l_p = m_w*cp*(T2-T1)/(-500000)
    return 5.1*m_w + 8.8*m_c + 2.1*l_p
for p in pump:
    for t in turbine:
        for f in fuel:
            if (f == "Coal"):
                boil = 0
            if (f == "Ngas"):
                boil = 1
            if (f == "Gasoline"):
                boil = 2
            for b in boiler:
                HR = solve()
                print "{}, {}, {}, {}, {}".format(p, t, f, b, HR)
