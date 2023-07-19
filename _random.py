import random

# result = random.random()   # 0-1 arasında random sayı 

result =int(random.uniform(1,10))
result = random.random() * 100
result = random.randint(1,10)               #random tam sayi


names = ['serdar','alara', 'ipek' ,'pelin']
greetings = 'hello there'

result = names[random.randint(0,len(names)-1)]

result=random.choice(names)  # direkt içinden birini random seçer

result=random.choice(greetings)

liste =  list(range(10))
random.shuffle(liste)               # belirtilen listeyi rastgele karistir

liste= range(100)
result= random.sample(liste,4)    # belirtilen adresten 2 rastgele eleman al
result= random.sample(names,2)


print(result)