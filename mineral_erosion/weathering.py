'''
Created on Jan 19, 2014
Python 2.7, in Eclipse with PyDev plugin

This script creates data for use in modelling the dissapearence of minerals in a
theoretical granitoid cube, and aggradation of solutes into groundwater.

completed for Problem Set 1 for EES 411 at Lehigh University

@author: Andrew Moodie
'''

'''
TO DO:
add in the production of kaolinite for feldspars                      v
add annite weathering to biotite and iron                             v
change rates of weathering to be for 2.75m^2                          v  
mole diff b/w feld and kaolinite                                      v
check on rate for tremolite (is it acid mechanism or neutral)?        v
reduce s.a. each time individually for each mineral                   v   
solutes estalished for:                                               -
Plag                                                                  v
Quartz                                                                v
Annite
Tremolite                                                             v
K-feld                                                                v
'''

'''
LIST OF ASSUMPTIONS:
assume no loss of minerals in flux b/w dissolution and product
assume stoichiometry of reactant to product:
    i.e. that 1 annite creates 0.5 FeOOH and 0.5 Kaolinite
    i.e. that 1 tremolite = 5Mg, 2Ca, 8Sa
check assumption on dissolution and solutes of tremolite stoich
assumption made for Annite solute production is just BS and wrong
'''

'''
############################################################################

module functions are defined below

############################################################################
'''

def print_moles():
    print "Moles of each mineral remaining:"
    print Pf_mol 
    print Qz_mol
    print An_mol
    print Tr_mol
    print Kf_mol
    print Ka_mol
    print Fe_mol
    print Sa_mol
    print Ca_mol
    print Na_mol
    print Mg_mol
    print Po_mol
    print ""
    
def print_moles_labeled():
    print "Moles of each mineral remaining:"
    print "Pf: " + str(Pf_mol) 
    print "Qz: " + str(Qz_mol)
    print "An: " + str(An_mol)
    print "Tr: " + str(Tr_mol)
    print "Kf: " + str(Kf_mol)
    print "Ka: " + str(Ka_mol)
    print "Fe: " + str(Fe_mol)
    print "Sa: " + str(Sa_mol)
    print "Ca: " + str(Ca_mol)
    print "Na: " + str(Na_mol)
    print "Mg: " + str(Mg_mol)
    print "Po: " + str(Po_mol)
    print ""

def weather_Pf(step):
    global Pf_mol
    global Ka_mol
    global Pf_sa
    global Ca_mol
    global Na_mol
    raw_to_tenth = -11.6
    raw_weather_rate = 10 ** raw_to_tenth 
    if step == 'sec':
        weather_rate = raw_weather_rate # mol/m^2 s .0000000000012589
    elif step == 'day':
        weather_rate = raw_weather_rate * 60 * 60 * 24 # mol/m^2 d - .00000010877116
    elif step == 'year':
        weather_rate = raw_weather_rate * 60 * 60 * 24 * 365 # mol/m^2 yr .0000397014
    weather_mol_Pf = weather_rate * Pf_sa
#    if Pf_mol <= set_zero:
#        Pf_mol = 0
    if weather_mol_Pf > Pf_mol and Pf_mol != 0:
        gram_Pf = Pf_mol * Pf_mw
        gram_Ka = gram_Pf
        add_mol_Ka = (gram_Ka / Ka_mw)
        Ka_mol += add_mol_Ka
        Pf_mol = Pf_mol - (Pf_mol)
        add_mol_Ca = Pf_mol * 0.6
        add_mol_Na = Pf_mol * 0.4
        Ca_mol += add_mol_Ca
        Na_mol += add_mol_Na
    elif Pf_mol == 0:
        Pf_mol = Pf_mol
    else:
        gram_Pf = weather_mol_Pf * Pf_mw
        gram_Ka = gram_Pf
        add_mol_Ka = (gram_Ka / Ka_mw)
        Pf_mol -= weather_mol_Pf
        Ka_mol += add_mol_Ka
        add_mol_Ca = weather_mol_Pf * 0.6
        add_mol_Na = weather_mol_Pf * 0.4
        Ca_mol += add_mol_Ca
        Na_mol += add_mol_Na
    Pf_sa = (Pf_mol * Pf_mw) * 1 #m2/g

def weather_Qz(step):
    global Qz_mol
    global Qz_sa
    global Sa_mol
    raw_to_tenth = -12.9
    raw_weather_rate = 10 ** raw_to_tenth
    if step == 'sec':
        weather_rate = raw_weather_rate # mol / m^2 s - .00000000000012589 
    elif step == 'day':
        weather_rate = raw_weather_rate * 60 * 60 * 24 # mol/m^2 d - .000000010877116 
    elif step == 'year':
        weather_rate = raw_weather_rate * 60 * 60 * 24 * 365 # mol/m^2 yr - .00000397014 
    weather_mol_Qz = weather_rate * Qz_sa
#    if Qz_mol <= set_zero:
#        Qz_mol = 0
    if weather_mol_Qz > Qz_mol and Qz_mol != 0:
        add_mol_Sa = Qz_mol
        Sa_mol += add_mol_Sa
        Qz_mol = Qz_mol - (Qz_mol)
    elif Qz_mol == 0:
        Qz_mol = Qz_mol
    else:
        add_mol_Sa = weather_mol_Qz
        Sa_mol += add_mol_Sa
        Qz_mol -= weather_mol_Qz
    Qz_sa = (Qz_mol * Qz_mw) * 1 #m2/g
        
def weather_An(step):
    global An_mol
    global Ka_mol
    global Fe_mol
    global An_sa
    global Po_mol
    raw_to_tenth = -11.35
    raw_weather_rate = 10 ** raw_to_tenth
    if step == 'sec':
        weather_rate = raw_weather_rate # mol / m^2 s -  .000000000031622
    elif step == 'day':
        weather_rate = raw_weather_rate * 60 * 60 * 24 # mol/m^2 d - .0000027322078 
    elif step == 'year':
        weather_rate = raw_weather_rate * 60 * 60 * 24 * 365 # mol/m^2 yr - .00099725589 
    weather_mol_An = weather_rate * An_sa
#    if An_mol <= set_zero:
#        An_mol = 0
    if weather_mol_An > An_mol and An_mol != 0:
        gram_An = An_mol * An_mw
        #I am making a wild assumption here about stoichiometry of annite dissolution
        gram_Ka = 0.5 * gram_An
        gram_Fe = 0.5 * gram_An
        add_mol_Ka = (gram_Ka / Ka_mw)
        add_mol_Fe = (gram_Fe / Fe_mw)
        Ka_mol += add_mol_Ka
        Fe_mol += add_mol_Fe
        An_mol = An_mol - (An_mol)
        add_mol_Po = An_mol * 1
        Po_mol += add_mol_Po
    elif An_mol == 0:
        An_mol = An_mol
    else:
        gram_An = weather_mol_An * An_mw
        #I am making a wild assumption here about stoichiometry of annite dissolution
        gram_Ka = 0.5 * gram_An
        gram_Fe = 0.5 * gram_An
        add_mol_Ka = (gram_Ka / Ka_mw)
        add_mol_Fe = (gram_Fe / Fe_mw)
        An_mol -= weather_mol_An
        Ka_mol += add_mol_Ka
        Fe_mol += add_mol_Fe
        add_mol_Po = weather_mol_An * 1
        Po_mol += add_mol_Po
    An_sa = (An_mol * An_mw) * 1 #m2/g
    
def weather_Tr(step):
    global Tr_mol
    global Tr_sa
    global Ca_mol
    global Mg_mol
    global Sa_mol
    raw_to_tenth = -11.9
    raw_weather_rate = 10 ** raw_to_tenth
    if step == 'sec':
        weather_rate = raw_weather_rate # mol / m^2 s -  .0000000000251188
    elif step == 'day':
        weather_rate = raw_weather_rate * 60 * 60 * 24 # mol/m^2 d - .00000217027 
    elif step == 'year':
        weather_rate = raw_weather_rate * 60 * 60 * 24 * 365 # mol/m^2 yr - .000792149 
    weather_mol_Tr = weather_rate * Tr_sa
#    if Tr_mol <= set_zero:
#        Tr_mol = 0
    if weather_mol_Tr > Tr_mol and Tr_mol != 0:
        add_mol_Ca = Tr_mol * 2 
        add_mol_Mg = Tr_mol * 5
        add_mol_Sa = Tr_mol * 8
        Ca_mol += add_mol_Ca
        Na_mol += add_mol_Mg
        Sa_mol += add_mol_Sa
        Tr_mol = Tr_mol -(Tr_mol)
    elif Tr_mol == 0:
        Tr_mol = Tr_mol
    else:
        Tr_mol -= weather_mol_Tr
        add_mol_Ca = weather_mol_Tr * 2 
        add_mol_Mg = weather_mol_Tr * 5
        add_mol_Sa = weather_mol_Tr * 8
        Ca_mol += add_mol_Ca
        Mg_mol += add_mol_Mg
        Sa_mol += add_mol_Sa
    Tr_sa = (Tr_mol * Tr_mw) * 1 #m2/g
    
def weather_Kf(step):
    global Kf_mol
    global Ka_mol
    global Kf_sa
    global Po_mol
    global Sa_mol
    raw_to_tenth = -12.5
    raw_weather_rate = 10 ** raw_to_tenth
    if step == 'sec':
        weather_rate = raw_weather_rate # mol / m^2 s -  .000000002238721
    elif step == 'day':
        weather_rate = raw_weather_rate * 60 * 60 * 24 # mol/m^2 d - .0001934255 
    elif step == 'year':
        weather_rate = raw_weather_rate * 60 * 60 * 24 * 365 # mol/m^2 yr - .0706003 
    weather_mol_Kf = weather_rate * Kf_sa
#    if Kf_mol <= set_zero:
#        Kf_mol = 0
    if weather_mol_Kf > Kf_mol and Kf_mol != 0:
        gram_Kf = Kf_mol * Kf_mw
        gram_Ka = gram_Kf
        add_mol_Ka = (gram_Ka / Ka_mw)
        Ka_mol += add_mol_Ka
        Kf_mol = Kf_mol - (Kf_mol)
        add_mol_Po = Kf_mol * 1
        add_mol_Sa = Kf_mol * 2
        Po_mol += add_mol_Po
        Sa_mol += add_mol_Sa
    elif Kf_mol == 0:
        Kf_mol = Kf_mol
    else:
        gram_Kf = weather_mol_Kf * Kf_mw
        gram_Ka = gram_Kf
        add_mol_Ka = (gram_Ka / Ka_mw)
        Kf_mol -= weather_mol_Kf
        Ka_mol += add_mol_Ka
        add_mol_Po = weather_mol_Kf * 1
        add_mol_Sa = weather_mol_Kf * 2
        Po_mol += add_mol_Po
        Sa_mol += add_mol_Sa
    Kf_sa = (Kf_mol * Kf_mw) * 1 #m2/g

def reduce_sa():
    global sa_cube
    curr_total_mol = (Pf_mol + Qz_mol + An_mol + Tr_mol + Kf_mol)
    sa_cube = ((curr_total_mol / init_total_mol) * 2.75)

def timestep():
    global time
    if time < 10:
        for t in range(1): # 18000  is 5 hours, 43200 is 12hr
            weather_Pf('year')
            weather_Qz('year')
            weather_An('year')
            weather_Tr('year')
            weather_Kf('year')
            sa_cube = Pf_sa + Qz_sa + An_sa + Tr_sa + Kf_sa
            time += 1
    elif time >= 10 and time < 100:
        for t in range(10): # 18000  is 5 hours, 43200 is 12hr
            weather_Pf('year')
            weather_Qz('year')
            weather_An('year')
            weather_Tr('year')
            weather_Kf('year')
            sa_cube = Pf_sa + Qz_sa + An_sa + Tr_sa + Kf_sa
            time += 1
    elif time >= 100 and time < 1000:
        for t in range(100): # 18000  is 5 hours, 43200 is 12hr
            weather_Pf('year')
            weather_Qz('year')
            weather_An('year')
            weather_Tr('year')
            weather_Kf('year')
            sa_cube = Pf_sa + Qz_sa + An_sa + Tr_sa + Kf_sa
            time += 1
    elif time >= 1000 and time < 10000:
        for t in range(1000): # 18000  is 5 hours, 43200 is 12hr
            weather_Pf('year')
            weather_Qz('year')
            weather_An('year')
            weather_Tr('year')
            weather_Kf('year')
            sa_cube = Pf_sa + Qz_sa + An_sa + Tr_sa + Kf_sa
            time += 1
    elif time >= 10000 and time <= 100000:
        for t in range(10000): # 18000  is 5 hours, 43200 is 12hr
            weather_Pf('year')
            weather_Qz('year')
            weather_An('year')
            weather_Tr('year')
            weather_Kf('year')
            sa_cube = Pf_sa + Qz_sa + An_sa + Tr_sa + Kf_sa
            time += 1
    print "Time is: (time = " + str((time)) + ") years"
#    print "Surface area is: (sa_cube = " + str(sa_cube) + ")"
    

'''
############################################################################

initial conditions for the script are defined below

############################################################################
'''

cube_mass = 2.75 # grams

Pf_mw = 271.81 # g/mol
Qz_mw = 60.083 # g/mol
An_mw = 512.88 # g/mol
Tr_mw = 812.37 # g/mol
Kf_mw = 278.33 # g/mol
Ka_mw = 258.16 # g/mol
Fe_mw = 88.85 # g/mol

'''find the mass by weight of each mineral'''
Pf_mass = cube_mass * 0.50      # 50% mass by weight
Qz_mass = cube_mass * 0.25      # 25% mass by weight
An_mass = cube_mass * 0.10      # 10% mass by weight
Tr_mass = cube_mass * 0.10      # 10% mass by weight
Kf_mass = cube_mass * 0.05      # 05% mass by weight

'''find the surface area of each mineral'''
Pf_sa = Pf_mass * 1 # m2/g
Qz_sa = Qz_mass * 1
An_sa = An_mass * 1
Tr_sa = Tr_mass * 1
Kf_sa = Kf_mass * 1

'''find or define the moles of each mineral'''
Pf_mol = Pf_mass / Pf_mw        # moles of Plag feldspar
Qz_mol = Qz_mass / Qz_mw        # moles of Quartz
An_mol = An_mass / An_mw        # moles of Annite
Tr_mol = Tr_mass / Tr_mw        # moles of Tremolite
Kf_mol = Kf_mass / Kf_mw        # moles of K-feldspar
Ka_mol = 0                      # moles of Kaolinite
Fe_mol = 0                      # moles of Iron Oxide
Sa_mol = 0                      # moles of Silicic Acid
Ca_mol = 0                      # moles of Ca ion
Na_mol = 0                      # moles of Na ion
Mg_mol = 0                      # moles of Mg ion
Po_mol = 0                      # moles of potassium ion

'''find the value of a few variables useful for debugging'''
init_total_mol = (Pf_mol + Qz_mol + An_mol + Tr_mol + Kf_mol)
sa_cube = Pf_sa + Qz_sa + An_sa + Tr_sa + Kf_sa
set_zero = .00001
'''
############################################################################

set up and run the model for a series of timesteps

############################################################################
'''



'''set the start time to 0 and print the initial variable values'''
time = 0
print "At start of script (time = " + str(time) + "):"
print "Surface area is: (sa_cube = " + str(sa_cube) + ")"
print_moles()

'''begin weathering'''
timestep()
print_moles() 
timestep()
print_moles() 
timestep()
print_moles() 
timestep()
print_moles() 
timestep()
print_moles() 
timestep()
print_moles() 
timestep()
print_moles() 
timestep()
print_moles() 
timestep()
print_moles() 
timestep()
print_moles() 
timestep()
print_moles() 
timestep()
print_moles() 
timestep()
print_moles() 
timestep()
print_moles() 
timestep()
print_moles() 
timestep()
print_moles() 
timestep()
print_moles() 
timestep()
print_moles() 
timestep()
print_moles() 
timestep()
print_moles() 
timestep()
print_moles() 
timestep()
print_moles() 
timestep()
print_moles()
timestep()
print_moles() 
timestep()
print_moles() 
timestep()
print_moles() 
timestep()
print_moles() 
timestep()
print_moles() 
timestep()
print_moles() 
timestep()
print_moles() 
timestep()
print_moles() 
timestep()
print_moles() 
timestep()
print_moles() 
timestep()
print_moles() 
timestep()
print_moles() 
timestep()
print_moles() 
timestep()
print_moles() 
timestep()
print_moles() 
timestep()
print_moles() 
timestep()
print_moles() 
timestep()
print_moles() 
timestep()
print_moles() 
timestep()
print_moles() 
timestep()
print_moles() 
timestep()
print_moles() 
timestep()
print_moles() 
timestep()
print_moles() 
timestep()
print_moles() 
timestep()
print_moles() 
timestep()
print_moles() 
timestep()
print_moles() 
timestep()
print_moles() 
timestep()
print_moles() 
timestep()
print_moles() 
timestep()
print_moles() 
timestep()
print_moles() 
timestep()
print_moles() 
timestep()
print_moles() 
timestep()
print_moles() 
timestep()
print_moles()
timestep()
print_moles() 
timestep()
print_moles() 
timestep()
print_moles() 
timestep()
print_moles() 
timestep()
print_moles() 
timestep()
print_moles() 
timestep()
print_moles() 
timestep()
print_moles() 
timestep()
print_moles() 
timestep()
print_moles() 
timestep()
print_moles() 
timestep()
print_moles() 
timestep()
print_moles() 
timestep()
print_moles() 
timestep()
print_moles() 
timestep()
print_moles() 
timestep()
print_moles() 
timestep()
print_moles() 
timestep()
print_moles() 
timestep()
print_moles() 
timestep()
print_moles() 
timestep()
print_moles() 





