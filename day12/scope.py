boom = 1

def isboom():
    global boom
    #kolan intorie ke baes mishe on var ke biron az in box tarahi shode ghabele estefade beshe.
    boom = 2
    print(f"this is inside the jar{boom}")

isboom()
print(f"this is outside the jar{boom}")

# scope is like a box that your stuff is in there.
# when you put more stuff inside a small box,
# only the ppl who can open the box can use the stuff.
# if sb is out of the box they cant use the stuff in there.

# Global constant: is the cvar that you don't wanna change it, at all
# like the pi number
# Global Constant are normally declared in ALL CAPS with a _ in between

PI = 3.14159
# GOOGLE_URL = "https://www.google.com"

