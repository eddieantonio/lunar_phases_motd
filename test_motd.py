"""
Not automated testing. Just visual testing :)
"""

from io import StringIO
from contextlib import redirect_stdout

from lunar_phases import print_motd

MAX_WIDTH = 180


# Get all of them:
outputs = []
for probe in [0, 7, 10, 14, 15, 22, 28, 29]:
    fake_file = StringIO()
    with redirect_stdout(fake_file):
        print_motd(float(probe))

    outputs.append(fake_file.getvalue())
    # lol whoops
    # print(outputs[-1])

screens = []
for output in outputs:
    lines = output.split("\n")

    max_width = max(len(line) for line in lines)
    padded_lines = [line + " " * (max_width - len(line)) for line in lines]
    screens.append(padded_lines)

buffer = []
current_width = 0
spacing = "      "
for screen in screens:
    width = len(screen[0])
    num_spaces = len(buffer) * len(spacing)
    if current_width + width + num_spaces >= MAX_WIDTH:
        # Print the buffer
        for line in zip(*buffer):
            print(*line, sep=spacing)
        print()
        # Reset:
        current_width = 0
        buffer = []

    buffer.append(screen)
    current_width += width

if buffer:
    for line in zip(*buffer):
        print(*line)
    print()
