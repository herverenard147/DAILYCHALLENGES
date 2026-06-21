
#     Ask the user for their birthdate (specify the format, for example: DD/MM/YYYY).
#     Display a little cake as seen below:

birthdate = input("Enter your birthdate (DD/MM/YYYY): ")
day, month, year = map(int, birthdate.split('/'))
age = 2023 - year
candles = age % 100
if candles == 0:
    candles = 100
print("___iiiii___")
print("|:H:a:p:p:y:|")
print("|:B:i:r:t:h:d:a:y:|")        
print(f"~{'~' * candles}~") 