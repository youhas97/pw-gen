import secrets, json, math
seed = secrets.SystemRandom()

fillers = "!@#$%&/',.?;:<>|"

with open("words_dictionary.json", "r") as f:
    #filter out words shorter than 4 characters.
    words = list(filter(lambda word: len(word) >= 4, json.load(f).keys()))


n = int(input("How many words do you want in your password? ").split()[0])

pw = words[(math.floor(seed.random()*len(words)))].capitalize()
for i in range(n-1):
    pw += fillers[math.floor(seed.random()*(len(fillers)-1))]
    pw += words[(math.floor(seed.random()*len(words)))].capitalize()

print(pw)
