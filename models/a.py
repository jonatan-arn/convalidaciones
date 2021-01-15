import random,string
aux = ''.join(random.choice( string.ascii_letters  ) for x in range(5))+''.join(random.choice( string.digits  ) for x in range(5))
aux = ''.join(random.sample(aux,len(aux)))
print(aux)