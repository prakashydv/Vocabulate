## Add sentence usage
## Add synonyms
## Add choice of vocab list
## Add type of word (noun/adj/etc.)

import random

"""
names = open('names.txt', 'r')
definitions = open('defs.txt', 'r')
db = {}
for word in names:
    db[word] = definitions.readline()

names.close()
definitions.close()
"""

db = {}
vocab = open('vocab.txt', 'r')
for line in vocab:
    if len(line) < 5: continue
    name = line[:line.find(' ')]
    line = line[line.find(' ')+1:]
    type = line[:line.find(' ')]
    line = line[line.find(' ')+1:]
    defn = line
    if type not in ['n.', 'ad.', 'conj.', 'inter.', 'interj.', 'prep.', 'v.', 'adj.', 'adv.'] or len(defn) < 4: continue
    db[name] = defn
vocab.close()

## Get the highscore
score = open('data', 'rb')
high_score = score.readline()
score.close()

def write_highscore(new_score):
    score = open('data', 'wb')
    score.write(str(high_score))
    score.close()

def guess(word, multiple):
    score = 0
    round_no = 0
    limit = 1
    if multiple:
        limit = 4
    while round_no < 10:
        ## Disallow same words in the ten rounds?
        definitions = []
        term = random.sample(db.keys(), limit)
        for question_word in term:
            definitions.append(db[question_word])
        if word:
            q = term
            a = definitions
        else:
            a = term
            q = definitions
        print "Q: " + q[0]
        print
        poss = a[:]
        random.shuffle(poss)
        if multiple:
            print "Options"
            for ind, option in enumerate(poss):
                print ind+1, 
                print option
            print "Enter answer number"
            ans = input()
            if poss[ans-1] == a[0]:
                print "CORRECT"
                score+=1
            else:
                print "WRONG!" + " The correct answer was: " + a[0]
        else:
            ans = raw_input()
            print a[0]
            print "Did you get it right? (1 - Yes, 0 - No)"
            ans = input()
            score+=ans
        print "SCORE: " + str(score)
        print 
        round_no+=1
    print "Your score was: ", score
    if score > int(high_score):
        print "You achieved a new high_score!"
    write_highscore(score)

def run_game(choice):
    if choice == 1:
        guess(True, False)
    elif choice == 2:
        guess(False, False)
    elif choice == 3:
        guess(True, True)
    elif choice == 4:
        guess(False, True)
    elif choice == 5:
        print "Your high score is ", high_score

choice = 2
while choice < 10:
    print "1. Guess what the word means"
    print "2. Guess what word the definition corresponds to"
    print "3. Match (Given: word)"
    print "4. Match (Given: definition)"
    print "5. Check high score"
    print "10. Exit"

    choice = input()
    run_game(choice)

