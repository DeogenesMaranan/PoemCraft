import random


def generate_love_poem():
    word_banks = [
        {
            "placeholder0": ["beautiful", "enchanting", "captivating", "breathtaking", "mesmerizing"],
            "placeholder1": ["gentle", "tender", "warm", "loving", "kind"],
            "placeholder2": ["forever", "eternally", "endlessly", "always", "perpetually"],
            "placeholder3": ["heart", "soul", "mind", "dream", "desire"],
            "placeholder4": ["adore", "cherish", "love", "treasure", "worship"],
            "placeholder5": ["love", "affection", "devotion", "sentiment", "feeling", "adoration"],
            "placeholder6": ["best", "greatest", "finest", "purest", "most wonderful"],
            "placeholder7": ["grateful", "thankful", "proud", "content", "amazed", "honored"],
            "placeholder8": ["best", "greatest", "finest", "purest", "most wonderful"]
        },
        {
            "placeholder0": ["stunning", "radiant", "alluring", "spellbinding", "irresistible"],
            "placeholder1": ["tender", "gentle", "warm", "loving", "kind"],
            "placeholder2": ["always", "eternally", "forever", "endlessly", "perpetually"],
            "placeholder3": ["heart", "soul", "mind", "dream", "desire"],
            "placeholder4": ["adore", "cherish", "love", "treasure", "worship"],
            "placeholder5": ["love", "affection", "devotion", "sentiment", "feeling", "adoration"],
            "placeholder6": ["greatest", "finest", "purest", "most wonderful", "irreplaceable"],
            "placeholder7": ["grateful", "thankful", "proud", "content", "amazed", "honored"],
            "placeholder8": ["best", "greatest", "finest", "purest", "most wonderful"]
        },
        {
            "placeholder0": ["exquisite", "dazzling", "enamoring", "heavenly", "astonishing"],
            "placeholder1": ["tender", "gentle", "warm", "loving", "kind"],
            "placeholder2": ["forever", "eternally", "endlessly", "always", "perpetually"],
            "placeholder3": ["heart", "soul", "mind", "dream", "desire"],
            "placeholder4": ["adore", "cherish", "love", "treasure", "worship"],
            "placeholder5": ["love", "affection", "devotion", "sentiment", "feeling", "adoration"],
            "placeholder6": ["best", "greatest", "finest", "purest", "most wonderful"],
            "placeholder7": ["grateful", "thankful", "proud", "content", "amazed", "honored"],
            "placeholder8": ["best", "greatest", "finest", "purest", "most wonderful"]
        }
    ]

    poem_structures = [
        [
            "Your {placeholder0} eyes are a work of art.",
            "Your {placeholder1} smile warms my {placeholder2} {placeholder3}.",
            "I {placeholder4} you deeply, it's the {placeholder6} {placeholder5}.",
            "You're the {placeholder8} of all, I'm {placeholder7}.",
            "Having you in my life is a fresh start."
        ],
        [
            "In your {placeholder0} presence, my heart takes flight.",
            "Your {placeholder1} touch sets everything right.",
            "I {placeholder4} you, a love so {placeholder6},",
            "With you, life's a {placeholder7} dream, not just a dream.",
            "In your arms, I find my eternal light."
        ],
        [
            "You are the {placeholder0} star in my night sky.",
            "With your {placeholder1} embrace, I'll never say goodbye.",
            "I {placeholder4} you, my {placeholder6} devotion so pure.",
            "In your love, I'm {placeholder7} forevermore.",
            "You and I, a love that will never die."
        ]
    ]

    def generate_random_poem():
        poem_structure_index = random.randint(0, len(poem_structures) - 1)
        poem_structure = poem_structures[poem_structure_index]
        selected_values = {}
        for key, value_list in word_banks[poem_structure_index].items():
            selected_values[key] = random.choice(value_list)
        poem = [line.format(**selected_values) for line in poem_structure]
        return "\n".join(poem)

    poem = generate_random_poem()

    return poem


def generate_birthday_poem():
    word_banks = [
        {
            "placeholder0": ["beautiful", "enchanting", "gorgeous", "radiant", "lovely"],
            "placeholder1": ["sweet", "charming", "dear", "precious", "beloved"],
            "placeholder2": ["today", "on this special day", "as you celebrate", "on your birthday", "with joy"],
            "placeholder3": ["heart", "soul", "life", "world", "dream"],
            "placeholder4": ["adore", "cherish", "love", "treasure", "worship"],
            "placeholder5": ["smile", "laugh", "happiness", "joy", "delight"],
            "placeholder6": ["best", "greatest", "finest", "purest", "most wonderful"],
            "placeholder7": ["grateful", "thankful", "blessed", "fortunate", "happy"],
            "placeholder8": ["wishing you", "sending you", "hoping for", "dreaming of", "celebrating with"],
            "placeholder9": ["more love", "endless joy", "countless blessings", "dreams come true", "a future bright"]
        },
        {
            "placeholder0": ["mesmerizing", "captivating", "elegant", "dazzling", "alluring"],
            "placeholder1": ["dearest", "loving", "treasured", "cherished", "special"],
            "placeholder2": ["on this day of joy", "as you turn a year older", "celebrating with delight", "on your special day", "with love in the air"],
            "placeholder3": ["life", "journey", "path", "adventure", "dream"],
            "placeholder4": ["adore", "cherish", "love", "treasure", "worship"],
            "placeholder5": ["laughter", "happiness", "bliss", "joy", "delight"],
            "placeholder6": ["brightest", "most wonderful", "fullest", "loveliest", "happiest"],
            "placeholder7": ["grateful", "thankful", "blessed", "fortunate", "joyful"],
            "placeholder8": ["wishing you", "sending you", "hoping for", "dreaming of", "celebrating with"],
            "placeholder9": ["more love", "endless joy", "countless blessings", "dreams come true", "a future bright"]
        },
        {
            "placeholder0": ["radiant", "exquisite", "charming", "divine", "adorable"],
            "placeholder1": ["beloved", "precious", "darling", "loving", "treasured"],
            "placeholder2": ["on this special day", "as you grow a year older", "celebrating with delight", "on your birthday", "in the company of friends and family"],
            "placeholder3": ["life", "journey", "path", "adventure", "dream"],
            "placeholder4": ["adore", "cherish", "love", "treasure", "worship"],
            "placeholder5": ["laughter", "happiness", "bliss", "joy", "delight"],
            "placeholder6": ["brightest", "most wonderful", "fullest", "loveliest", "happiest"],
            "placeholder7": ["grateful", "thankful", "blessed", "fortunate", "joyful"],
            "placeholder8": ["wishing you", "sending you", "hoping for", "dreaming of", "celebrating with"],
            "placeholder9": ["more love", "endless joy", "countless blessings", "dreams come true", "a future bright"]
        }
    ]

    poem_structures = [
        [
            "To my {placeholder1}, {placeholder2},",
            "Your {placeholder0} presence lights up my {placeholder3}.",
            "I {placeholder4} you more than words can say,",
            "Your {placeholder5} is a gift in every way.",
            "You're the {placeholder6} girlfriend, and I'm {placeholder7} every day.",
            "On your special day, I'm {placeholder8} you {placeholder9}."
        ],
        [
            "On this day, {placeholder2},",
            "Your {placeholder0} grace leaves me in awe,",
            "I {placeholder4} you with a heart full of {placeholder5},",
            "You're the {placeholder6} and I'm {placeholder7}.",
            "Wishing you {placeholder8} {placeholder9} and more."
        ],
        [
            "Today, as you celebrate {placeholder2},",
            "Your {placeholder0} spirit shines so bright,",
            "I {placeholder4} you more than words can convey,",
            "You make every day a pure delight.",
            "With you, life is the {placeholder6}, and I'm {placeholder7},",
            "Wishing you {placeholder8} {placeholder9} this birthday night."
        ]
    ]

    def generate_random_poem():
        poem_structure_index = random.randint(0, len(poem_structures) - 1)
        poem_structure = poem_structures[poem_structure_index]
        selected_values = {}
        for key, value_list in word_banks[poem_structure_index].items():
            selected_values[key] = random.choice(value_list)
        poem = [line.format(**selected_values) for line in poem_structure]
        return "\n".join(poem)

    poem = generate_random_poem()

    return poem


def generate_christmas_poem():
    word_banks = [
        {
            "placeholder0": ["joyful", "merry", "festive", "cheerful", "magical"],
            "placeholder1": ["season", "time", "holiday", "moment", "celebration"],
            "placeholder2": ["hearts", "souls", "spirits", "homes", "dreams"],
            "placeholder3": ["twinkle", "glow", "shine", "gleam", "radiate"],
            "placeholder4": ["laughter", "love", "warmth", "happiness", "delight"],
            "placeholder5": ["family", "friends", "loved ones", "dear ones", "near ones"],
            "placeholder6": ["blessed", "grateful", "happy", "content", "joyful"],
            "placeholder7": ["together", "united", "connected", "gathered", "rejoiced"],
            "placeholder8": ["blessings", "joy", "peace", "love", "wishes"],
            "placeholder9": ["throughout the year", "for all days", "forevermore", "in every way", "today and always"]
        },
        {
            "placeholder0": ["magical", "enchanting", "whimsical", "gleeful", "radiant"],
            "placeholder1": ["season", "time", "holiday", "moment", "celebration"],
            "placeholder2": ["hearts", "souls", "spirits", "homes", "dreams"],
            "placeholder3": ["twinkle", "glow", "shine", "gleam", "radiate"],
            "placeholder4": ["laughter", "love", "warmth", "happiness", "delight"],
            "placeholder5": ["family", "friends", "loved ones", "dear ones", "near ones"],
            "placeholder6": ["blessed", "grateful", "joyful", "content", "happy"],
            "placeholder7": ["together", "united", "connected", "gathered", "rejoiced"],
            "placeholder8": ["blessings", "joy", "peace", "love", "wishes"],
            "placeholder9": ["throughout the year", "for all days", "forevermore", "in every way", "today and always"]
        },
        {
            "placeholder0": ["festive", "wholesome", "heartwarming", "radiant", "glorious"],
            "placeholder1": ["season", "time", "holiday", "moment", "celebration"],
            "placeholder2": ["hearts", "souls", "spirits", "homes", "dreams"],
            "placeholder3": ["twinkle", "glow", "shine", "gleam", "radiate"],
            "placeholder4": ["laughter", "love", "warmth", "happiness", "delight"],
            "placeholder5": ["family", "friends", "loved ones", "dear ones", "near ones"],
            "placeholder6": ["blessed", "grateful", "content", "joyful", "happy"],
            "placeholder7": ["together", "united", "connected", "gathered", "rejoiced"],
            "placeholder8": ["blessings", "joy", "peace", "love", "wishes"],
            "placeholder9": ["throughout the year", "for all days", "forevermore", "in every way", "today and always"]
        }
    ]

    poem_structures = [
        [
            "In this {placeholder0} {placeholder1}, our {placeholder2} {placeholder3},",
            "Fills with {placeholder4} as we gather 'round the tree.",
            "With {placeholder5} by our side, we're truly {placeholder6}.",
            "On this day, we're {placeholder7}, it's a time to be carefree.",
            "Sending you {placeholder8}, {placeholder9}."
        ],
        [
            "The {placeholder0} {placeholder1} is here, our {placeholder2} {placeholder3} bright.",
            "Our {placeholder4} multiplies, and the world seems just right.",
            "With {placeholder5} near, our hearts are {placeholder6}.",
            "On this day, we're {placeholder7}, and the stars alight.",
            "Wishing you {placeholder8}, {placeholder9} tonight."
        ],
        [
            "This {placeholder0} {placeholder1} is a time of {placeholder2} {placeholder3},",
            "Our {placeholder4} and warmth, the ultimate degree.",
            "With {placeholder5} close, our spirits are {placeholder6}.",
            "On this day, we're {placeholder7}, and our hearts are free.",
            "Sending you {placeholder8}, {placeholder9} to be."
        ]
    ]

    def generate_random_poem():
        poem_structure_index = random.randint(0, len(poem_structures) - 1)
        poem_structure = poem_structures[poem_structure_index]
        selected_values = {}
        for key, value_list in word_banks[poem_structure_index].items():
            selected_values[key] = random.choice(value_list)
        poem = [line.format(**selected_values) for line in poem_structure]
        return "\n".join(poem)

    poem = generate_random_poem()

    return poem


def generate_new_year_poem():
    word_banks = [
        {
            "placeholder0": ["fresh", "brand new", "promising", "exciting", "vibrant"],
            "placeholder1": ["year", "chapter", "adventure", "beginning", "journey"],
            "placeholder2": ["hope", "joy", "dreams", "success", "adventures"],
            "placeholder3": ["unfolds", "awaits", "beckons", "calls", "greets"],
            "placeholder4": ["laughter", "love", "happiness", "peace", "prosperity"],
            "placeholder5": ["friends", "family", "loved ones", "dear ones", "near ones"],
            "placeholder6": ["blessed", "grateful", "content", "joyful", "happy"],
            "placeholder7": ["together", "united", "connected", "gathered", "celebrating"],
            "placeholder8": ["hopes", "dreams", "achievements", "success", "prosperity"],
            "placeholder9": ["throughout the year", "for all days", "forevermore", "in every way", "now and always"]
        },
        {
            "placeholder0": ["new", "bright", "limitless", "majestic", "splendid"],
            "placeholder1": ["year", "chapter", "adventure", "beginning", "journey"],
            "placeholder2": ["hope", "joy", "dreams", "success", "adventures"],
            "placeholder3": ["unfolds", "awaits", "beckons", "calls", "greets"],
            "placeholder4": ["laughter", "love", "happiness", "peace", "prosperity"],
            "placeholder5": ["friends", "family", "loved ones", "dear ones", "near ones"],
            "placeholder6": ["blessed", "grateful", "joyful", "content", "happy"],
            "placeholder7": ["together", "united", "connected", "gathered", "celebrating"],
            "placeholder8": ["hopes", "dreams", "achievements", "success", "prosperity"],
            "placeholder9": ["throughout the year", "for all days", "forevermore", "in every way", "now and always"]
        },
        {
            "placeholder0": ["fresh", "promising", "exciting", "bright", "radiant"],
            "placeholder1": ["year", "chapter", "adventure", "beginning", "journey"],
            "placeholder2": ["hope", "joy", "dreams", "success", "adventures"],
            "placeholder3": ["unfolds", "awaits", "beckons", "calls", "greets"],
            "placeholder4": ["laughter", "love", "happiness", "peace", "prosperity"],
            "placeholder5": ["friends", "family", "loved ones", "dear ones", "near ones"],
            "placeholder6": ["blessed", "grateful", "joyful", "content", "happy"],
            "placeholder7": ["together", "united", "connected", "gathered", "celebrating"],
            "placeholder8": ["hopes", "dreams", "achievements", "success", "prosperity"],
            "placeholder9": ["throughout the year", "for all days", "forevermore", "in every way", "now and always"]
        }
    ]

    poem_structures = [
        [
            "As the {placeholder0} {placeholder1} {placeholder3},",
            "May it bring you {placeholder2} beyond your dreams.",
            "With {placeholder4} and warmth, we're {placeholder7},",
            "Embracing {placeholder8} and what life redeems.",
            "Wishing you joy {placeholder9}, it seems."
        ],
        [
            "A {placeholder0} {placeholder1} {placeholder3} before us,",
            "Filled with {placeholder2}, and endless delight.",
            "With {placeholder4} and loved ones, we're {placeholder7},",
            "Embracing {placeholder8}, from morning to night.",
            "Wishing you happiness and light {placeholder9}."
        ],
        [
            "In this {placeholder0} {placeholder1} that {placeholder3} anew,",
            "May it be filled with {placeholder2}, each day for you.",
            "With {placeholder4} and togetherness, we're {placeholder7},",
            "Embracing {placeholder8} that will remain true.",
            "Wishing you a year that's {placeholder9}."
        ]
    ]

    def generate_random_poem():
        poem_structure_index = random.randint(0, len(poem_structures) - 1)
        poem_structure = poem_structures[poem_structure_index]
        selected_values = {}
        for key, value_list in word_banks[poem_structure_index].items():
            selected_values[key] = random.choice(value_list)
        poem = [line.format(**selected_values) for line in poem_structure]
        return "\n".join(poem)

    poem = generate_random_poem()

    return poem


def generate_miss_you_poem():
    word_banks = [
        {
            "placeholder0": ["lonely", "empty", "alone", "lost", "sorrowful"],
            "placeholder1": ["moments", "times", "hours", "nights", "days"],
            "placeholder2": ["longing", "yearning", "aching", "missing", "craving"],
            "placeholder3": ["warmth", "embrace", "presence", "smile", "touch"],
            "placeholder4": ["heart", "soul", "world", "life", "mind"],
            "placeholder5": ["aches", "cries", "calls", "whispers", "mourns"],
            "placeholder6": ["come back", "return to me", "be near", "rejoin", "embrace me"],
            "placeholder7": ["fill", "mend", "heal", "soothe", "calm"],
            "placeholder8": ["dreaming", "wishing", "hoping", "praying", "waiting"],
            "placeholder9": ["until you're here", "with each passing day", "in every moment", "for eternity", "until you're back"]
        },
        {
            "placeholder0": ["empty", "aching", "longing", "yearning", "desolate"],
            "placeholder1": ["moments", "times", "hours", "nights", "days"],
            "placeholder2": ["craving", "missing", "aching", "needing", "longing for"],
            "placeholder3": ["warmth", "embrace", "presence", "smile", "touch"],
            "placeholder4": ["heart", "soul", "world", "life", "mind"],
            "placeholder5": ["aches", "cries", "calls", "whispers", "mourns"],
            "placeholder6": ["come back", "return to me", "be near", "rejoin", "embrace me"],
            "placeholder7": ["fill", "mend", "heal", "soothe", "calm"],
            "placeholder8": ["dreaming", "wishing", "hoping", "praying", "waiting"],
            "placeholder9": ["until you're here", "with each passing day", "in every moment", "for eternity", "until you're back"]
        },
        {
            "placeholder0": ["lonely", "empty", "alone", "lost", "sorrowful"],
            "placeholder1": ["moments", "times", "hours", "nights", "days"],
            "placeholder2": ["longing", "yearning", "aching", "missing", "craving"],
            "placeholder3": ["warmth", "embrace", "presence", "smile", "touch"],
            "placeholder4": ["heart", "soul", "world", "life", "mind"],
            "placeholder5": ["aches", "cries", "calls", "whispers", "mourns"],
            "placeholder6": ["come back", "return to me", "be near", "rejoin", "embrace me"],
            "placeholder7": ["fill", "mend", "heal", "soothe", "calm"],
            "placeholder8": ["dreaming", "wishing", "hoping", "praying", "waiting"],
            "placeholder9": ["until you're here", "with each passing day", "in every moment", "for eternity", "until you're back"]
        }
    ]

    poem_structures = [
        [
            "In these {placeholder0} {placeholder1}, my {placeholder4} {placeholder2} for your {placeholder3}.",
            "My {placeholder4} {placeholder5} for your return, for the day when you'll {placeholder6}.",
            "Your absence leaves my {placeholder4} in pain, and I {placeholder7} it with thoughts of you.",
            "I'm {placeholder8} for the moment {placeholder9}.",
        ],
        [
            "These {placeholder0} {placeholder1}, my {placeholder4} {placeholder2} for your {placeholder3}.",
            "My {placeholder4} {placeholder5} for your embrace, for the day when you'll {placeholder6}.",
            "Your absence leaves my {placeholder4} in pain, and I {placeholder7} it with thoughts of you.",
            "I'm {placeholder8} for the moment {placeholder9}.",
        ],
        [
            "During these {placeholder0} {placeholder1}, my {placeholder4} {placeholder2} for your {placeholder3}.",
            "My {placeholder4} {placeholder5} for your presence, for the day when you'll {placeholder6}.",
            "Your absence leaves my {placeholder4} in pain, and I {placeholder7} it with thoughts of you.",
            "I'm {placeholder8} for the moment {placeholder9}.",
        ]
    ]

    def generate_random_poem():
        poem_structure_index = random.randint(0, len(poem_structures) - 1)
        poem_structure = poem_structures[poem_structure_index]
        selected_values = {}
        for key, value_list in word_banks[poem_structure_index].items():
            selected_values[key] = random.choice(value_list)
        poem = [line.format(**selected_values) for line in poem_structure]
        return "\n".join(poem)

    poem = generate_random_poem()

    return poem
