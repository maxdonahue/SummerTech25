unit = input("Farenheit or Celcuis ")
tempature = int(input("What tempature would you like to convert? "))
     
def farenheittocelcius(x):
    print(f"{((x - 32) * 5/9):.2f}","celcius")
def celciustofarenheit(y):
    print(f"{((y * 9/5) + 32):.2f}","farenheit")

if unit == "farenheit":
    farenheittocelcius(tempature)
elif unit == "celcius":
    celciustofarenheit(tempature)
