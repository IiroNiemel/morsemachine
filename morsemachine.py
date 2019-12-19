import winsound
import time

def changeFreq(frq):
    newFreq = input("Type new freq, it must be between 37 and 32000")
    if newFreq > 37 and newFreq < 32000:
        print("Success")
        return frq
    else:
        print("Invalid, go home")

def goToMorse(word, Frequency):
    try:
        frequency = int(Frequency)
    except (ValueError):
        print("Faulty frequency format!!\n")
        main()
    alphabets = { 'a' : '.-', 'b' : '-...',
               'c' : '-.-.', 'd' : '-..',
               'e' : '.', 'f' : '..-.',
               'g' : '--.', 'h' : '....',
               'i' : '..', 'j' : '.---',
               'k' : '-.-', 'l' : '.-..',
               'm' : '--', 'n' : '-.',
               'o' : '---', 'p' : '.--.',
               'q' : '--.-', 'q' : '--.-',
               'r' : '.-.', 's' : '...',
               't' : '-', 'u' : '..--',
               'v' : '...-', 'x' : '-..-',
               'y' : '-.--', 'z' : '--..',
               '1' : '.----', '2' : '..---',
               '3' : '...--', '4' : '....-',
               '5' : '.....', '6' : '-....',
               '7' : '--...', '8' : '---..',
               '9' : '----.', '0' : '-----', ' ' : '/'}

    translate = ""
    try:
        for i in range(0,len(word)): 
            translate = translate + alphabets[word[i]]+"/"

        print("Same as morse: ", translate)
    except (KeyError):
        print("All letters from","'" ,word,"'" , "are not coded")

    for i in translate:
        if i == ".":
            duration = 200  # set duration, 1000 ms == 1 second
            winsound.Beep(frequency, duration)
            time.sleep(0.200)
        elif i == "-":
            duration = 400  # set duration, 1000 ms == 1 second
            winsound.Beep(frequency, duration)
            time.sleep(0.200)
        elif i == "/":
            time.sleep(0.200)
        else:
            print("Something went wrong")
            
def main():
    frequency = 1000
    input_1 = input ("Give me something to morse: ")
    goToMorse(input_1, frequency)

if __name__ == '__main__':
    main()