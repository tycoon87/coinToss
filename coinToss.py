#import random
#x = random.random()
##x_rounded = round(x)
#heads = 0
#tails = 0
#for i in 5000:
#    print "Attempt #{}: Throwing a coin...".format(i)
#    x_rounded = round(x)
#    if x_rounded >= 0.5:
#        heads =+ 1
#        print "It's a head! ..."
#    elif x_rounded =< 0.49
#        tails =+ 1
#    print "You Got {} head(s) so far and {} tail(s) so far".format(heads,tails)
#    **************************************************
#impot random function
import random
#define the function for the coin toss (reps is a place holder)
def toss(reps):
    # print new_toss
    attempt_count = 1
    head_count = 0
    tail_count = 0
    result = ""
    result_string_complete = ""
#    start for loop with 2 peramaders
    for x in range(1, reps):
#        set the new toss to a random number between 0 and 1
        new_toss = random.randint(0,1)
#        if the new toss is 1
        if new_toss == 1:
#            add one to head count
            head_count += 1
#            set result to head
            result = "head"
#            than print the following
            print "Attempt #", attempt_count, ": Throwing a coin... It's a ", result, "! Got ", head_count, "head(s) so far and", tail_count, "tail(s) so far"
#            outherwise 
        else:
#            add 1 to tails count
            tail_count += 1
#            set the result to tail
            result = "tail"
#            print the following
            print "Attempt #", attempt_count, ": Throwing a coin... It's a ", result, "! Got ", head_count, "head(s) so far and", tail_count, "tail(s) so far"
#        add one to attempt count 
        attempt_count += 1
#toss coin 5000 times, dose not run 5001
toss(5001)