"""
python list comprehension

Where to use?- In order to create new sequence form another sequence
Did you used? = yes, after got the DB result, we used to change the some values.
why you can change in SQL?  = it used VIEW,
in order to change to view we have to get permission for other Up steam and down stream application owners.
"""

l1 = [i*i for i in range(1,11)]

print(l1)

t1 = (10,20,30)
t2 = (10,40,50)
t3= t1+t2
print(t3)
t4 = t3*2
print(t4)
print(len(t4))
print(t4.count(10))
print(t4.index(5))

