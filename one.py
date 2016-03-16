#one
name = raw_input("Enter Name:\n")
print 'hello', name

#two and five
try:
    hours = float(raw_input('enter hours:\n'))
    try:
        rate = float(raw_input('enter rate\n'))
        if hours > 40:
            pay = 40 * rate + (hours - 40) * rate * 1.5
        else:
            pay = hours * rate
        print "Pay =", pay
    except Exception as e:
        print 'Error, please enter numeric input'
except Exception as e:
    print 'Error, please enter numeric input'

#three
width = 17
height = 12.0
print width/2
print width/2.0
print height/3
print 1 + 2 * 5

#four celsius to fahrenheit
cels = float(raw_input("Give me the temp in Celsius:"))
fahr = cels * 9/5 + 32
print "here's the real temp", fahr

#six
try:
    score = float(raw_input("Enter Score: \n"))
    if score < 0.0 or score > 1.0:
        print "Bad Score"
    elif score >= 0.9:
        print "A"
    elif score >= 0.8:
        print "B"
    elif score >= 0.7:
        print "C"
    elif score >= 0.6:
        print "D"
    else:
        print "F"
except Exception as e:
    print "Bad Score\n"
