from django.shortcuts import render
from playsound import playsound
import time
import pyttsx3 as pyttsx

# Create your views here.
def home(request):
    marks = [1,2,4,4,5,6,6,5,6,7,6,67,98]
    context = {
        'marks' : marks,
        'name' : "Arnab"
    }
    return render(request, 'form.html', context)




MORSE_CODE_DICT = { ' ':'/', 'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.', 'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-', 'L':'.-..', 'M':'--', 'N':'-.','O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-','U':'..-', 'V':'...-', 'W':'.--','X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--','4':'....-', '5':'.....', '6':'-....','7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-','?':'..--..', '/':'-..-.', '-':'-....-','(':'-.--.', ')':'-.--.-'}


def add(request):
    num1 = request.GET["num1"]
    num2 = request.GET["num2"]
    if int(num1) == 1:
        code = [MORSE_CODE_DICT[i.upper()] + ' ' for i in num2 if i.upper() in MORSE_CODE_DICT.keys()]
        morse=''.join(code)
        for m in morse:
            if m=='.':
                playsound('C:\\Users\\ARNAB\\Desktop\\morse\\morsecode\\myapp\\dit.wav')
            elif m=='-':
                playsound('C:\\Users\\ARNAB\\Desktop\\morse\\morsecode\\myapp\\dah.wav')
            else:
                time.sleep(0.5)
        return render(request,'res.html',{"result":morse})
    elif int(num1) == 2:    
        code = [k for i in num2.split() for k,v in MORSE_CODE_DICT.items() if i==v]
        newtxt = ''.join(code)
        engine = pyttsx.init()
        engine.say(newtxt)
        engine.runAndWait()
        return render(request,'result.html',{"result":newtxt}) 