# celcius to fahrenheit convert

def cwltofah(celcius):
    return (celcius*9/5)+32

celciusvalue=int(input("Enter celcius: "))    
fahrenheitvalue=cwltofah(celciusvalue)
print(fahrenheitvalue)