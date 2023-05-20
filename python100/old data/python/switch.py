sub = 2400
likes = 200
'''
print(sub,likes)
temp=sub
sub=likes
likes=temp
print(sub,likes)
'''

print(sub,likes)
sub, likes = likes, sub
print(sub,likes)