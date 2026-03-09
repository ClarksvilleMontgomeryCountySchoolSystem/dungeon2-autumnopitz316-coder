good = r"""

    _____________
   /      _      \
   [] :: (_) :: []
   [] ::::::::: []
   [] ::::::::: []
   [] ::::::::: []
   [] ::::::::: []
   [_____________]
       I     I
       I_   _I
        /   \
        \   /
        (   )   -cfbd-
        /   \
        \___/
    Ignition Key
"""
bad = r"""
            __________
           |  __  __  |
           | |  ||  | |
           | |  ||  | |
           | |__||__| |
           |  __  __()|
           | |  ||  | |
           | |  ||  | |
           | |  ||  | |
           | |  ||  | |
           | |__||__| |
ejm        |__________|
"""
has_key = True
if not has_key:
    outcome = "Doom: How are we going to open the dore?"
    print(bad)
else:
    outcome = "Click: Yay! The dore opened!!"
    print(good)
print(outcome)