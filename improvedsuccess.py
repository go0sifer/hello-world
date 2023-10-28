def success(dedication, persistence):
    passion = dedication > 0 and persistence > 0

    if passion:
        magic = dedication + persistence
        return f"You have a magic rating of {magic}"
    else:
        return "You have no magic. Dedicate yourself and be Persistent. This shows Passion and combined will grant you magic."

# love it. learn it. make mistakes. keep learning.

# Example usage:
# dedication = 0
# persistence = 0
# result = success(dedication, persistence)


RESULT = success(4, 20)
RESULT2 = success(0, 0)
RESULT3 = success(0, 1)
print(RESULT)
print(RESULT2)
print(RESULT3)
