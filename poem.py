import random
import string

hero = ["knight","wrestler","baseball player",
             "football player","racer","teacher","jedi master","pilot","inventor","boxer","dojo master","leader","superhero"]

beautiful = ["flower","butterfly",
             "ballerina","heart","child",
             "angel","star",
             "spark","sun"]


animal = ["gorilla","lion","bull",
          "hawk","eagle","fox","tiger","rhino","cheetah","panther","wasp","ram","snake"]

smart = ["light bulb","book","experiment",
          "genius","passing grade", "successor","enthusiast"]

life = ["childhood","adulthood","future",
          "world","lifehood"]

creator = ["brendon t. jones","brendon","brendon jones"]


line_1 = "YOU HAVE A STRIKING RESEMBLANCE OF A " + random.choice(hero).upper()
line_2 = "THE PASSION OF A " + random.choice(beautiful).upper()
line_3 = "THE STRENGTH OF A " + random.choice(animal).upper()
line_4 = "THE KNOWLEDGE OF A " + random.choice(smart).upper()
line_5 = "YOU'LL REACH FOR THE STAR TO HAVE A FUN " + random.choice(life).upper()
line_6 = "AN ORIGINAL POEM CREATED BY " + random.choice(creator).upper()

print(line_1)
print("\t" + line_2)
print("\t\t" + line_3)
print("\t\t\t" + line_4)
print("\t\t\t\t" + line_5)
print("\t\t\t\t\t" + line_6)
