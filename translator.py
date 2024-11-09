import random

emoji = {"love": ["❤️", "💗", "😍"],
         "cool": ["😎"],
         "think": ["🤔", "🧠"],
         "I don't know": ["🤷‍♀️", "😖"],
         "happy": ["😊", "☺️"],
         "funny": ["😂", "🤣", "💀"],
         "dog": ["🐕", "🐶"],
         "nerd": ["🤓"],
         "mad": ["😡", "🤬", "😠", "😠", "😾"],
         "evil": ["👿", "😈", "👹", "👺"],
         "animal": ["🐱", "🐈", "🐐", "🐄", "🐃", "🐎","🐸", "🐝", "🐗"],
         "insect": ["🦋", "🐞", "🐜", "🦗", "🪰", "🪲", "🪳", "🕷️"],
         "annoyed": ["🙄", "😩", "😑", "😤", "😒"],
         "sad": ["😢", "😕", "☹️"]}

while True: 
    inp = input("Give me a sentence: ")
    for word in emoji.keys():
        inp = inp.replace(word, random.choice(emoji[word]))
    print(inp)

    # if "cool" in inp:
    #     replacement = inp.replace("cool", random.choice(emoji["cool"]))
    #     print(replacement)
    # elif "love" in inp:
    #     replacement = inp.replace("love", random.choice(emoji["love"]))
    #     print(replacement)
    # elif "think" in inp:
    #     replacement = inp.replace("think", random.choice(emoji["think"]))
    #     print(replacement)
    # elif "I don't know" in inp:
    #     replacement = inp.replace("i don't know", random.choice(emoji["i don't know"]))
    #     print(replacement)
    # elif "Happy" in inp:
    #     replacement = inp.replace("happy", random.choice(emoji["happy"]))
    #     print(replacement)
    # elif "funny" in inp:
    #     replacement = inp.replace("funny", random.choice(emoji["funny"]))
    #     print(replacement)
    # elif "dog" in inp:
    #     replacement = inp.replace("dog", random.choice(emoji["dog"]))
    #     print(replacement)
    # else: 
    #     print("No emoji found to use in sentence ")


        

    






