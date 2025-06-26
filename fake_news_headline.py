import random

subjects = [
    "Shah Rukh Khan",
    "Salman Khan",
    "Motu Patlu",
    "Narendra Modi",
    "A group of drunk monkeys",
    "A mysterious AI",
    "An angry toaster",
    "A time-traveling cat",
    "A dancing robot",
    "An invisible man"
]

actions = [
    "declares war on gravity",
    "buys the moon",
    "eats 50 ice creams in 10 minutes",
    "challenges Elon Musk to a dance battle",
    "gets arrested for teleporting into a zoo",
    "wins a Nobel Prize for sleeping",
    "launches a new cryptocurrency called 'BananaCoin'",
    "hosts a tea party for aliens",
    "becomes the CEO of Mars",
    "accidentally opens a portal to another dimension"
]

places_or_things = [
    "on live TV 📺",    
    "in a haunted mansion 👻",
    "during a cricket match 🏏",
    "at a wedding in space 🚀",
    "inside a video game 🎮",
    "while riding a unicorn 🦄",
    "in a secret underground bunker 🕳️",
    "at the top of Mount Everest 🏔️",
    "in a Bollywood movie 🎬",
    "in a swimming pool full of noodles 🍜"
]

headline_templates = [
    "🚨 Breaking News: {subject} {action} {place}",
    "🗞️ You won't believe this: {subject} just {action} {place}",
    "🔥 Trending Now: {subject} {action} {place}",
    "😱 OMG! {subject} {action} {place}",
    "📢 Shocking: {subject} {action} {place}"
]

while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    place_or_thing = random.choice(places_or_things)
    template = random.choice(headline_templates)

    headline = template.format(subject=subject, action=action, place=place_or_thing)
    print("\n" + headline)

    user_input = input("Press Enter to generate another headline or type 'exit' to quit: ").strip().lower()
    if user_input == 'exit':
        break

print("📰 Thanks for using the Fake News Headline Generator. Stay weird!")
