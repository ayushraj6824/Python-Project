import random

subjects = [
    "Shah Rukh Khan",
    "Virat Kohli",
    "A group of monkeys",
    "A school of fish",
    "Elon Musk",
    "The Eiffel Tower",
    "A pride of lions",
    "Cristiano Ronaldo",
    "A flock of birds",
    "A team of firefighters",
    "Narendra Modi",
    "A basket of fruits",
    "A colony of ants",
    "Taylor Swift",
    "A herd of elephants",
    "The Great Wall of China",
    "A swarm of bees",
    "Barack Obama",
    "A classroom of students",
    "A choir of singers",
    "A parliament of owls",
    "A galaxy of stars",
    "A band of musicians",
    "Amitabh Bachchan",
    "A pack of wolves",
    "A bouquet of flowers",
    "A constellation of satellites",
    "A bunch of balloons",
    "A litter of puppies",
    "A troop of dancers"
]



actions = [
    "is dancing", "is running", "is sleeping", "is eating", "is singing",
    "is talking", "is jumping", "is reading a book", "is playing cricket", "is cooking food",
    "is watching a movie", "is climbing a tree", "is writing a letter", "is painting a picture", "is swimming in the pool",
    "is flying a kite", "is riding a bicycle", "is washing clothes", "is walking in the park", "is planting a tree",
    "is studying for exams", "is cleaning the room", "is feeding the dog", "is fixing the car", "is drawing a sketch",
    "is drinking water", "is typing on a laptop", "is brushing teeth", "is listening to music", "is shopping for groceries"
]

places_or_things = [
    "in Mumbai",
    "on the moon",
    "at the Taj Mahal",
    "inside a haunted house",
    "near the White House",
    "at a cricket stadium",
    "on a moving train",
    "inside a submarine",
    "at a secret island",
    "on top of Mount Everest",
    "in a jungle",
    "inside a volcano",
    "in a spaceship",
    "in the middle of the desert",
    "at a pizza shop",
    "inside a video game",
    "at the airport",
    "in a zoo",
    "in a classroom",
    "at a music festival",
    "in a time machine",
    "on a flying carpet",
    "at a robot factory",
    "in a parallel universe",
    "inside a treasure chest",
    "at the bottom of the ocean",
    "on a cloud",
    "at a hacker conference",
    "inside a chocolate factory",
    "on a pirate ship"
]


# The headline generation loop 
while True:
    subject=random.choice(subjects)
    action=random.choice(actions)
    place_or_thing=random.choice(places_or_things)


    headline=f" Breaking News : {subject} {action} {place_or_thing} "
    print(("\n"+headline))

    user_input=input("\n Do you want another headline?(Yes/No)").strip().lower()
    if user_input == "no":
        break

print("\n Thanks for using the fake News Headline Generator.have a fun day")