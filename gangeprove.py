## Copyright Sigurd Rage 2020
import random
import time

questions = []
answers = []
questions_rand = []
answers_rand = []

for x in range (1,11):
    for y in range (1,11):
        q = str(x) + " * " + str(y)
        questions.append(q)
        answers.append(str(x * y))

for i in range (0,len(questions)):
    num = random.randrange(0,len(questions))
    q = questions.pop(num)
    questions_rand.append(q)
    a = answers.pop(num)
    answers_rand.append(a)

questions.clear()
answers.clear()
score=0

print("Velkommen til Sigurds gangetest. - (c) Sigurd Rage 2020\n\nDu får nå alle gangestykkene i den lille gangetabelle i tilfeldig rekkefølge.\nNår du er ferdig får du vite hvor mange pojeng du fikk!")
print("Da får du også prøve om igjen de gangestykkene du ikke fikk til.\n")

invalid_input = True
antall_int=0

while invalid_input:
    antall = input("Hvor mange gangestykker vil du ha på testen? (0-100):")
    if antall == "":
        antall_int=100
        print("Du får 100 oppgaver.\n")
        invalid_input = False
    elif int(antall) < 0 or int(antall) > 100:
        print("Skriv et tall mellom 0 og 100\n")
    else:
        print("OK, du får " + antall + " oppgaver.\n")
        antall_int = int(antall)
        invalid_input = False

start = round(time.time(),1)

for i in range(0, antall_int):
    answered = input(questions_rand[i] + " = ")
    if answered == answers_rand[i]:
        score += 1
        print("Riktig!" + " Du har: " + str (antall_int -1 - i) + " spørsmål igjen!")
    else:
        print("Feil!" + " Du har: " + str (antall_int - 1 - i) + " spørsmål igjen!")
        questions.append(questions_rand[i])
        answers.append(answers_rand[i])

print("\nDu fikk " + str(score) + " pojeng av " + str(antall_int) + " mulige!")

if score == antall_int:
    print("Bra jobba! Alt rett!")
    stop = round(time.time(),1)
    print("Du brukte ", stop-start, " sekunder!")
else :
    print("\nDu må gjøre disse gangestykkene om igjen")
    for i in range(0, len(questions)):
        answered = input(questions[i] + " = ")
        if answered == answers[i]:
            print("Riktig!")
            score += 1
        else:
            print("Feil!")

    print("\n Nå fikk du " + str(score) + " pojeng")
    stop = round(time.time(),1)
    print("Du brukte ", stop - start, " sekunder!")

time.sleep(3)

