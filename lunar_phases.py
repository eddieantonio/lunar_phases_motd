import time
import math
from textwrap import dedent

# Constants
SECONDS_IN_DAY = 86400
JULIAN_DATE_UNIX_EPOCH = 2440587.5
JULIAN_DATE_MARCH_NEW_MOON = 2461118.3097222
LUNAR_PHASE_LENGTH = 29.53
LUNAR_PHASE_HALFPOINT = 14.765


def lunar_phase():
    """
    Calculates where today falls inside a lunar phase.
    """
    current_julian_date = time.time() / SECONDS_IN_DAY + JULIAN_DATE_UNIX_EPOCH
    phase_calculation = (
        current_julian_date - JULIAN_DATE_MARCH_NEW_MOON
    ) % LUNAR_PHASE_LENGTH
    return phase_calculation


class MoonPhase:
    """
    Superclass for all phases of the moon. This super-class:
     - automatically determines the name of the phase of the moon
     - extracts the ASCII art from the docstring
     - stores all phases of the moon in a SORTED array
     - provides a few defaults that are useful for printing the message
    """

    PHASES = []

    # Default attributes for all phases of the moon:
    today_is = "normal"
    countdown = None

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        cls.name = camel_case_to_capitalized_string(cls.__name__)
        cls.ascii_art = dedent(cls.__doc__)
        cls.PHASES.append(cls)


def camel_case_to_capitalized_string(name):
    for i, c in enumerate(name[1:]):
        if "A" <= c <= "Z":
            # Account for chopping of the first number of this loop:
            split_pos = i + 1
            break
    return name[:split_pos] + " " + name[split_pos:]


# == Phases of the moon =====================================================


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

    today_is = "special"


def days_plural(number):
    word = "day" if number == 1 else "days"
    return f"{number} {word}"


def print_motd(phase=None):
    if phase is None:
        phase = lunar_phase()

    # Figure out the phase of the moon using a binary search.
    # This is a special case of binary search where:
    #  - there are exact 2**3 == 8 options
    #  - we can't fail (we will always whittle down 8 options to one)
    # We will always get an answer in EXACTLY three iterations.  Due to MATH it also
    # means we just need to keep track of is the lower-bound, which we adjust by
    # precomputed constants in each iteration.
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
