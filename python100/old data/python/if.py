sub = 2400
likes = 200
comment = 56

#if sub>2000 and likes < 250 and comment == 56:
 #   print("awesome article")

condition = [sub>2000,likes < 250,comment == 56]
if all(condition) :
    print("awesome article")


