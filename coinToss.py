import random
x = random.random()
#x_rounded = round(x)
heads = 0
tails = 0
for i in 5000:
    print "Attempt #{}: Throwing a coin...".format(i)
    x_rounded = round(x)
    if x_rounded >= 0.5:
        heads =+ 1
        print "It's a head! ..."
    elif x_rounded =< 0.49
        tails =+ 1
    print "You Got {} head(s) so far and {} tail(s) so far".format(heads,tails)