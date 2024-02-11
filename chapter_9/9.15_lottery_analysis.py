"""Modules"""
from random import choice


pool = [1,2,3,4,5,6,7,8,9,0]
my_ticket =[1,3,6,9]
w_ticket = []
attempt = 0
flag = True

while flag:
    for i in range(1,5):
        w_ticket.append(choice(pool))
    print(w_ticket)
    if w_ticket == my_ticket:
        flag = False
        print(attempt)
    else:
        attempt += 1 
        w_ticket = []
