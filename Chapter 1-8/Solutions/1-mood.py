"""
Basic solution for the mood-checker
"""

mood = input("What's your mood today? ")

if mood == "happy":
    print("It is great to see you happy!")
elif mood == "nervous":
    print("Take a deep breath 3 times.")
elif mood == "sad":
    print("Keep your head up!")
elif mood == "excited":
    print("Easy now, don't go too crazy...")
elif mood == "relaxed":
    print("Don't get too comfortable...")
else:
    print("What mood is that!?")
