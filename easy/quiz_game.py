print('Bem-vindo')

playing = input("Você quer jogar: ")
score = 0

if playing.lower() != "sim":
    quit()

print("Ok, vamos jogar :) ")

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("Whats does GPU stand for? ") 
if answer.lower() == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("what does RAM stand for? ")
if answer.lower() == "random acess memory":
    print("Correct!")
    score += 1

else:
    print("Incorrect!")

answer = input("What does PSU stand for? ")
if answer.lower() == "power supply":
    print("Correct!")
    score += 1

else:
    print("Incorrect!")

print(f"você fez: {score}")
print(f"você fez: {(score / 4) * 100}%.")