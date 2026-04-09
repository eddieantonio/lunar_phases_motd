import time 
import math

SECONDS_IN_DAY = 86400
JULIAN_DATE_UNIX_EPOCH = 2440587.5
JULIAN_DATE_MARCH_NEW_MOON = 2461118.3097222
LUNAR_PHASE_LENGTH = 29.53
LUNAR_PHASE_HALFPOINT = 14.765

def lunar_phase():
    """Function calculates where today falls inside a lunar phase."""
    current_julian_date = time.time() / SECONDS_IN_DAY + JULIAN_DATE_UNIX_EPOCH 
    phase_calculation = (current_julian_date - JULIAN_DATE_MARCH_NEW_MOON) % LUNAR_PHASE_LENGTH
    return phase_calculation


phases_dict = {
"NEW MOON" : 
"""
       _..._     
     .'     `.    
    :         :    
    :         :  
    `.       .'  
jgs   `-...-'  
""", 
"WAXING CRESCENT" : 
"""
       _..._     
     .'   `::.    
    :       :::    
    :       :::  
    `.     .::'  
jgs   `-..:'' 
""", 
"FIRST QUARTER" : 
"""
       _..._     
     .'  ::::.    
    :    ::::::    
    :    ::::::  
    `.   :::::'  
jgs   `-.::''   
""", 
"WAXING GIBBOUS" : 
""" 
       _..._     
     .' .::::.    
    :  ::::::::    
    :  ::::::::  
    `. '::::::'  
jgs   `-.::''  
""", 
"FULL MOON" : 
"""    
       _..._     
     .:::::::.    
    :::::::::::   
    ::::::::::: 
    `:::::::::'  
jgs   `':::'' 
""", 
"WANING GIBBOUS" : 
""" 
       _..._     
     .::::. `.    
    :::::::.  :    
    ::::::::  :  
    `::::::' .'  
jgs   `'::'-'
 """, 
 "THIRD QUARTER" : 
 """
       _..._     
     .::::  `.    
    ::::::    :    
    ::::::    :  
    `:::::   .'  
jgs   `'::.-'   
""", 
"WANING CRESCENT" : 
"""  
       _..._     
     .::'   `.    
    :::       :    
    :::       :  
    `::.     .'  
jgs   `':..-'
"""
}

# boundary points for lunar phase
"""
Waxing crescent: 0-6.375
First quarter: 6.375-7.375
Waxing gibbous: 7.375-13.75
Full moon: 13.75-14.75
Waning Gibbous: 14.75 - 21.125
Last quarter: 21.125-22.125
Waning crescent: 22.125-28.5
New moon: 28.5-29.5
"""

# Calculate today's lunar phase
phase = lunar_phase()

# Calculating days to next full/new moon
cntdwn = math.floor(LUNAR_PHASE_HALFPOINT - phase)
cntdwn2 = math.floor(LUNAR_PHASE_LENGTH - phase)

# Assigning variable 'day' for propper grammar
day = "day" if cntdwn == 1 else "days"
day2 = "day" if cntdwn2 == 1 else "days"


# Remove the # if you want to print the output of the function above
# print(phase)

# Assigning a physical phase to the calculated date 
# printing ASCII, phase name, and countdown to next new/full moon
if phase <= 6.375 :
    print(phases_dict["WAXING CRESCENT"])
    print("Today the moon is a WAXING CRESCENT")
    print(f"{cntdwn} {day} until next Full Moon")
elif phase <= 7.375 :
    print(phases_dict["FIRST QUARTER"])
    print("Today the moon is starting its FIRST QUARTER")
    print(f"{cntdwn} {day} until next Full Moon")
elif phase <= 13.75 :
    print(phases_dict["WAXING GIBBOUS"])
    print("Today the moon is a WAXING GIBBOUS")
    print(f"{cntdwn} {day} until next Full Moon")
elif phase <= 14.75 :
    print(phases_dict["FULL MOON"])
    print("Today is the FULL MOON!")
elif phase <= 21.125 :
    print(phases_dict["WANING GIBBOUS"])
    print("Today the moon is a WANING GIBBOUS")
    print(f"{cntdwn2} {day2} until next New Moon")
elif phase <= 22.125 :
    print(phases_dict["LAST QUARTER"])
    print("Today the moon is starting its LAST QUARTER")
    print(f"{cntdwn2} {day2} until next New Moon")
elif phase <= 28.5 :
    print(phases_dict["WANING CRESCENT"])
    print("Today the moon is a WANING CRESCENT")
    print(f"{cntdwn2} {day2} until next New Moon")
else:
    print(phases_dict["NEW MOON"])
    print("Today is the NEW MOON!")
