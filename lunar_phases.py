import time
import math
from textwrap import dedent

SECONDS_IN_DAY = 86400
JULIAN_DATE_UNIX_EPOCH = 2440587.5
JULIAN_DATE_MARCH_NEW_MOON = 2461118.3097222
LUNAR_PHASE_LENGTH = 29.53
LUNAR_PHASE_HALFPOINT = 14.765


def lunar_phase():
    current_julian_date = time.time() / SECONDS_IN_DAY + JULIAN_DATE_UNIX_EPOCH
    phase_calculation = (
        current_julian_date - JULIAN_DATE_MARCH_NEW_MOON
    ) % LUNAR_PHASE_LENGTH
    """Function calculates where today falls inside a lunar phase."""
    return phase_calculation


class MoonPhase:
    PHASES = []

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        cls.name = camel_case_to_capitalized_string(cls.__name__)
        cls.ascii_art = dedent(cls.__doc__)
        cls.today_is = "normal"
        cls.countdown = None
        cls.PHASES.append(cls)


def camel_case_to_capitalized_string(name):
    for i, c in enumerate(name[1:]):
        if "A" <= c <= "Z":
            # Account for chopping of the first number of this loop:
            split_pos = i + 1
            break
    return name[:split_pos] + " " + name[split_pos:]


class WaxingCrescent(MoonPhase):
    """
           _..._
         .'   `::.
        :       :::
        :       :::
        `.     .::'
    jgs   `-..:''
    """

    upper_boundary = 6.375
    countdown = "to-full-moon"


class FirstQuarter(MoonPhase):
    """
           _..._
         .'  ::::.
        :    ::::::
        :    ::::::
        `.   :::::'
    jgs   `-.::''
    """

    upper_boundary = 7.375
    countdown = "to-full-moon"
    today_is = "quarter"


class WaxingGibbous(MoonPhase):
    """
           _..._
         .' .::::.
        :  ::::::::
        :  ::::::::
        `. '::::::'
    jgs   `-.::''
    """

    upper_boundary = 13.75
    countdown = "to-full-moon"


class FullMoon(MoonPhase):
    """
           _..._
         .:::::::.
        :::::::::::
        :::::::::::
        `:::::::::'
    jgs   `':::''
    """

    upper_boundary = 14.75
    action = "full-moon"
    today_is = "special"


class WaningGibbous(MoonPhase):
    """
           _..._
         .::::. `.
        :::::::.  :
        ::::::::  :
        `::::::' .'
    jgs   `'::'-'
    """

    upper_boundary = 21.125
    countdown = "to-new-moon"


class LastQuarter(MoonPhase):
    """
           _..._
         .::::  `.
        ::::::    :
        ::::::    :
        `:::::   .'
    jgs   `'::.-'
    """

    upper_boundary = 22.125
    countdown = "to-new-moon"
    today_is = "quarter"


class WaningCrescent(MoonPhase):
    """
           _..._
         .::'   `.
        :::       :
        :::       :
        `::.     .'
    jgs   `':..-'
    """

    upper_boundary = 28.5
    countdown = "to-new-moon"


class NewMoon(MoonPhase):
    """
           _..._
         .'     `.
        :         :
        :         :
        `.       .'
    jgs   `-...-'
    """

    countdown = "new-moon"
    today_is = "special"


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


def days_plural(number):
    word = "day" if number == 1 else "days"
    return f"{number} {word}"


# Remove the # if you want to print the output of the function above
# print(phase)


def print_motd(phase=None):
    if phase is None:
        phase = lunar_phase()

    # Assigning a physical phase to the calculated date
    PHASES = MoonPhase.PHASES
    lo = 0
    lo += 4 if phase >= PHASES[lo + 3].upper_boundary else 0
    lo += 2 if phase >= PHASES[lo + 1].upper_boundary else 0
    lo += 1 if phase >= PHASES[lo + 0].upper_boundary else 0
    moon = PHASES[lo]

    # Print the moon!
    print(moon.ascii_art)

    # Print the first line of the message:
    if moon.today_is == "normal":
        print(f"Today the moon is a {moon.name}")
    elif moon.today_is == "quarter":
        print(f"Today the moon is starting its {moon.name}")
    elif moon.today_is == "special":
        print(f"Today is the {moon.name}!")

    # Print the countdown (if present)
    if moon.countdown == "to-full-moon":
        # Calculating days to next full/new moon
        cntdwn = math.floor(LUNAR_PHASE_HALFPOINT - phase)
        print(f"{days_plural(cntdwn)} until next Full Moon")
    elif moon.countdown == "to-new-moon":
        cntdwn2 = math.floor(LUNAR_PHASE_LENGTH - phase)
        print(f"{days_plural(cntdwn2)} until next New Moon")


if __name__ == "__main__":
    print_motd()
