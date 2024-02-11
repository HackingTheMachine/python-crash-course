from random import choice
pool = (1,2,3,4,5,6,7,8,9,0,"A","B","C","D","E")
w_ticket = []
for i in range(1,5):
    
    w_ticket.append(choice(pool))
print(f"Any ticket matching this is a winning ticket: {w_ticket}")
