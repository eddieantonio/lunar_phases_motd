import time 
import math

SECONDS_IN_DAY = 86400
JULIAN_DATE_UNIX_EPOCH = 2440587.5
JULIAN_DATE_MARCH_NEW_MOON = 2461118.3097222
LUNAR_PHASE_LENGTH = 29.53
LUNAR_PHASE_HALFPOINT = 14.765

def lunar_phase():
    current_julian_date = time.time() / SECONDS_IN_DAY + JULIAN_DATE_UNIX_EPOCH 
    phase_calculation = (current_julian_date - JULIAN_DATE_MARCH_NEW_MOON) % LUNAR_PHASE_LENGTH
    """Function calculates where today falls inside a lunar phase."""
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
 "LAST QUARTER" : 
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

def no_countdown(phase):
    pass # do nothing

def countdown_to_full(phase):
    cntdwn = math.floor(LUNAR_PHASE_HALFPOINT - phase)
    print(f"{days_plural(cntdwn)} until next Full Moon")


def countdown_to_new(phase):
    cntdwn2 = math.floor(LUNAR_PHASE_LENGTH - phase)
    print(f"{days_plural(cntdwn2)} until next New Moon")


class Phase:
    def __init__(self, name, upper_boundary, countdown=no_countdown):
        self.name = name
        self.upper_boundary = upper_boundary
        self._countdown = countdown

    def print_ascii_art(self):
        print(phases_dict[self.name])

    def print_today_is(self):
        print(f"Today the moon is a {self.name}")

    def print_countdown(self, phase):
        self._countdown(phase)


class QuarterMoon(Phase):
    def print_today_is(self):
        print(f"Today the moon is starting its {self.name}")


class SpecialMoon(Phase):
    def print_today_is(self):
        print(f"Today is the {self.name}!")


PHASE_INFO = [
    Phase("WAXING CRESCENT", 6.375, countdown=countdown_to_full),
    QuarterMoon("FIRST QUARTER", 7.375, countdown=countdown_to_full),
    Phase("WAXING GIBBOUS", 13.75, countdown=countdown_to_full),
    SpecialMoon("FULL MOON", 14.75),
    Phase("WANING GIBBOUS", 21.125, countdown=countdown_to_new),
    QuarterMoon("LAST QUARTER", 22.125, countdown=countdown_to_new),
    Phase("WANING CRESCENT", 28.5, countdown=countdown_to_new),
    SpecialMoon("NEW MOON", LUNAR_PHASE_LENGTH),
]

def days_plural(number):
    word = "day" if number == 1 else "days"
    return f"{number} {word}"


# Remove the # if you want to print the output of the function above
# print(phase)

def print_motd(phase=None):
    if phase is None:
        phase = lunar_phase()

    # Assigning a physical phase to the calculated date 
    lo = 0
    lo += phase >= PHASE_INFO[lo + 3].upper_boundary and 4
    lo += phase >= PHASE_INFO[lo + 1].upper_boundary and 2
    lo += phase >= PHASE_INFO[lo + 0].upper_boundary and 1
    info = PHASE_INFO[lo]

    # printing ASCII, phase name, and countdown to next new/full moon
    info.print_ascii_art()
    info.print_today_is()
    info.print_countdown(phase)


if __name__ == "__main__":
    print_motd()
