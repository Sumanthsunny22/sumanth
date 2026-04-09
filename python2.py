minutes = int(input("Enter minutes: "))

hours = minutes // 60
mins = minutes % 60

if hours > 0:
    print(hours, "hrs", mins, "minutes")
else:
    print(mins, "minutes")
