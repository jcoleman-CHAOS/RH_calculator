import numpy as np

def give_rh(t, g):
    index_of_rh = 0
    try:
        for index, i in enumerate(temp_air):
            if temp_air[index] > t:
                index_of_rh = index-1
                break
    except:
        return "not in range, try again"

    for i, k in enumerate(RH_psy):
        if air_g_0_exponent[index_of_rh][i] > g:
            return RH_psy[i-1]

print "\nPlease enter a Temperature (C) and g/Kg moisture\nSeparated by a space.\n"
print "Preparing look up tables..."

# These generate the Temp and RH
temp_air = np.arange(10, 35, .02)
RH_psy = np.arange(0,100,.2)
air_g_0_exponent = [[0 for x in range(len(RH_psy))] for x in range(len(temp_air))]
for i in range(len(temp_air)):
    for k in range(len(RH_psy)):
        air_g_0_exponent[i][k] = RH_psy[k]*10*0.62198*np.exp(77.345+0.0057*(temp_air[i]+273.15)-7235/(temp_air[i]+273.15))/(101325*np.power((temp_air[i]+273.15),8.2)-np.exp(77.345+0.0057*(temp_air[i]+273.15)-7235/(temp_air[i]+273.15)))
print "Done!\n"

while True:
    r = raw_input("\nEnter Temp. and RH: ").split()
    try:
        print "RH at " + r[0] + " with " + r[1] + " g/Kg water is: ",
        print give_rh(float(r[0]), float(r[1])),
        print " %"
    except:
        print "Error, please try again\n"
