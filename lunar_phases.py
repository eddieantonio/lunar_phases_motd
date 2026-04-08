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

phase = lunar_phase()

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

PHASE_INFO = [
    {
        "name": "WAXING CRESCENT",
        "upper_boundary": 6.375,
        "countdown": "to-full-moon",
    },
    {
        "name": "FIRST QUARTER",
        "upper_boundary": 7.375,
        "countdown": "count-to-full-moon",
        "today_is": "quarter"
    },
    {
        "name": "WAXING GIBBOUS",
        "upper_boundary": 13.75,
        "countdown": "count-to-full-moon",
    },
    {
        "name": "FULL MOON",
        "upper_boundary": 14.75,
        "action": "full-moon",
        "today_is": "special"
    },
    {
        "name": "WANING GIBBOUS",
        "upper_boundary": 21.125,
        "countdown": "count-to-new-moon",
    },
    {
        "name": "LAST QUARTER",
        "upper_boundary": 22.125,
        "countdown": "count-to-new-moon",
        "today_is": "quarter"
    },
    {
        "name": "WANING CRESCENT",
        "upper_boundary": 28.5,
        "countdown": "count-to-new-moon",
    },
    {
        "name": "NEW MOON",
        "upper_boundary": LUNAR_PHASE_LENGTH,
        "countdown": "new-moon",
        "today_is": "special"
    },
]

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
today_is_style = "normal"
countdown = None
if 0 < phase <= 6.375 :
    phase_idx = 0
elif 6.375 < phase <= 7.375 :
    phase_idx = 1
    name = "FIRST QUARTER"
elif 7.375 < phase <= 13.75 :
    phase_idx = 2
elif 13.75 < phase <= 14.75 :
    phase_idx = 3
elif 14.75 < phase <= 21.125 :
    phase_idx = 4
elif 21.125 < phase <= 22.125 :
    phase_idx = 5
elif 22.125 < phase <= 28.5 :
    phase_idx = 6
else:
    phase_idx = 7

info = PHASE_INFO[phase_idx]
name = info["name"]

# Print the moon!
ascii_art = phases_dict[name]
print(ascii_art)

# Print the first line of the message:
today_is_style = info.get("today_is", "normal")
if today_is_style == "normal":
    print(f"Today the moon is a {name}")
elif today_is_style == "quarter":
    print(f"Today the moon is starting its {name}")
elif today_is_style == "special":
    print(f"Today is the {name}!")

# Print the countdown (if present)
countdown = info.get("countdown")
if countdown == "to-full-moon":
    print(f"{cntdwn} {day} until next Full Moon")
elif countdown == "to-new-moon":
    print(f"{cntdwn2} {day2} until next New Moon")
