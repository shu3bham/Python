sub = 2400
likes = 200
comment = 56

#if sub>2000 or likes < 25 or comment == 6:
 #   print("awesome article")

condition = [sub>2000 , likes < 25 , comment == 6]
if any(condition) :
    print("awesome article")
