text = input("Enter a String:") 
unique_string = "" 
for ch in text:
    if ch not in unique_string:
        unique_string +=ch 
print(unique_string)
