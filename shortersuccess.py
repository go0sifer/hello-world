def success(dedication, persistence, passion):
    if dedication > 0 and persistence > 0 and passion:
        magic = dedication + persistence
        return f"You have magic of {magic}" if magic > 0 else "You have no magic."
    else:
        return "You have no magic."

# Example usage:
# dedication = 0
# persistence = 0
# passion = True
# result = success(dedication, persistence, passion)


result = success(4, 20, True)
print(result)
