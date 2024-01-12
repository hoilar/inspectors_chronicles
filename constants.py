# Dictorionary of constants used in the game

profiles = {
    "adventurer": {"tooltip": (
        f"Move profile: 1AP\n\nVelocipede (0 AP): Resets AP to 2.\n\nLantern (1 AP): Add new random item to locker."
        ), "playitem": "bicycle", "handitem": "lantern"}, 
        
    "agent": {"tooltip": (
        "Move profile: 1AP\n\nPocket-watch (3 AP): Add 1 extra day.\n\nMagnifying glass: Add witness for 3 AP,\nif suspect is found add 1 Special AP."
        ), "playitem": "watch", "handitem": "magnifyingglass"},

    "archeolog": {"tooltip": (
        "Move profile: 1AP\n\nWheelbarrow: TODO\n\nMagnifying glass: Add witness for 3 AP,\nif suspect is found add 1 Special AP."
        ), "playitem": "wheelbarrow", "handitem": "magnifyingglass"},

    "barber": {"tooltip": (
        "Move profile: 1AP\n\nDagger: TODO\n\nGoggles (0 AP): Free to play."
        ), "playitem": "dagger", "handitem": "goggles"},

    "barkeeper": {"tooltip": (
        "Move profile: 1AP\n\nTeapot play: full hand, -1 random witness.\n\nTop-hat (X AP): TODO."
        ), "playitem": "teapot", "handitem": "tophat"},

    "butcher": {"tooltip": (
        "Move profile: 1AP\n\nDagger: TODO\n\nPipe (1 AP): Add witness-point,\nloose 1 profile in waiting room."
        ), "playitem": "dagger", "handitem": "pipe"},

    "coalworker": {"tooltip": (
        "Move profile: 1AP\n\nWheelbarrow: TODO\n\nGoggles (0 AP): Free to play."
        ), "playitem": "wheelbarrow", "handitem": "goggles"},

    "curator": {"tooltip": (
        "Move profile: 1AP\n\nTop-hat (X AP): TODO"
        ), "playitem": "tophat", "handitem": "wheelbarrow"},

    "detective": {"tooltip": (
        "Move profile: 1AP\n\nPipe (1 AP): Add witness-point,\nloose 1 profile in waiting room."
        ), "playitem": "pipe", "handitem": "whistle"},

    "doctor": {"tooltip": (
        "Move profile: 1AP\n\nGoggles (0 AP): Free to play.\n\nVelocipede (0 AP): Resets AP to 2."
        ), "playitem": "goggles", "handitem": "bicycle"},

    "fisherman": {"tooltip": (
        "Move profile: 1AP\n\nLantern (1 AP): Add new random item to locker."
        ), "playitem": "lantern", "handitem": "dagger"},

    "hobo": {"tooltip": (
        "Move profile: 1AP\n\nPipe (1 AP): Add witness-point,\nloose 1 profile in waiting room.\n\nBaton (1 AP): Add new random profile to waiting room."
        ), "playitem": "pipe", "handitem": "baton"},

    "housewife": {"tooltip": (
        "Move profile: 1AP\n\nTeapot: TODO"
        ), "playitem": "teapot", "handitem": "whistle"},

    "hunter": {"tooltip": (
        "Move profile: 1AP\n\nDagger: TODO\n\nLantern (1 AP): Add new random item to locker."
        ), "playitem": "dagger", "handitem": "lantern"},

    "inventor": {"tooltip": (
        "Move profile: 1AP\n\nMagnifyingglass (3 AP): Add witness-point.\n\nGoggles (0 AP): Free to play."
        ), "playitem": "magnifyingglass", "handitem": "goggles"},

    "magician": {"tooltip": (
    "Move profile: 1AP\n\nPocket-watch (3 AP): Add 1 extra day.\n\nLantern (1 AP): Add new random item to locker."
        ), "playitem": "watch", "handitem": "lantern"},

    "maid": {"tooltip": (
        "Move profile: 1AP\n\nWhistle: TODO"
        ), "playitem": "whistle", "handitem": "teapot"},

    "mayor": {"tooltip": (
        "Move profile: 1AP\n\nTop-hat (X AP): TODO"
        ), "playitem": "tophat", "handitem": "teapot"},

    "pi": {"tooltip": (
        "Move profile: 1AP\n\nMagnifyingglass (3 AP): Add witness-point.\n\nBaton (1 AP): Add new random profile to waiting room."
        ), "playitem": "magnifyingglass", "handitem": "baton"},

    "policeman": {"tooltip": (
        "Move profile: 1AP\n\nBaton: New profile to waiting room \nif room is not full.\n\nBaton (1 AP): Add new random profile to waiting room."
        ), "playitem": "baton", "handitem": "whistle"},
        
    "postman": {"tooltip": (
        "Move profile: 1AP\n\nLantern (1 AP): Add new random item to locker.\n\nVelocipede: Resets AP to 2." #OK
        ), "playitem": "lantern", "handitem": "bicycle"}, 

    "professor": {"tooltip": (
        "Move profile: 1AP\n\nPocket-watch (3 AP): Add 1 extra day.\n\nTop-hat (X AP): TODO"
        ), "playitem": "watch", "handitem": "tophat"},

    "scientist": {"tooltip": (
        "Move profile: 1AP\n\nGoggles (0 AP): Free to play.\n\nPocket-watch (3 AP): Add 1 extra day."
        ), "playitem": "goggles", "handitem": "watch"},
        
    "vodouisant": {"tooltip": (
        "Move profile: 1AP\n\nDagger: TODO\n\nPocket-watch (3 AP): Add 1 extra day."
        ), "playitem": "dagger", "handitem": "watch"},
}

player_items = {
    "baton": {"tooltip": "Match Baton, 1+AP", "type": "item"},
    "bicycle": {"tooltip": "Match Velocipede, 1+AP", "type": "item"},
    "dagger": {"tooltip": "Match Dagger, 1+AP", "type": "item"},
    "goggles": {"tooltip": "Match Goggles, 1+AP", "type": "item"},
    "lantern": {"tooltip": "Match Lantern, 1+AP", "type": "item"},
    "magnifyingglass": {"tooltip": "Match Mag.glass, 1+AP", "type": "item"},    
    "pipe": {"tooltip": "Match Pipe, 1+AP", "type": "item"},
    "teapot": {"tooltip": "Match Teapot, 1+AP", "type": "item"},
    "tophat": {"tooltip": "Match Tophat, 1+AP", "type": "item"},    
    "watch": {"tooltip": "Match Pocket-watch, 1+AP", "type": "item"},
    "wheelbarrow": {"tooltip": "Match Wheeelbarrow, 1+AP", "type": "item"}, 
    "whistle": {"tooltip": "Match Whistle, 1+AP", "type": "item"},

    "cab": {"tooltip": "Increase waiting-room-size to 5.\nDown to 2 if suspect uses Mask", "type": "special"},
    "cell": {"tooltip": "Days not counting down.\n Lose 5 days if suspect plays shovel", "type": "special"},
    "duster": {"tooltip": "gain 1 random profile to examination,\nbut empties if perpetrator uses gloves", "type": "special"},
    "fist": {"tooltip": "Perpetrator chance to play new item\nis set to 20%", "type": "special"},
    "gun": {"tooltip": r"50% chance to negate perpetrator item", "type": "special"},
    "hat": {"tooltip": "Macthing items for 2+ AP to\nWaiting-room profiles yellow items", "type": "special"},
    "mail": {"tooltip": "Macthing items for 2+ AP to\nExamination-room profiles yellow items", "type": "special"},
    "newspaper": {"tooltip": "Increase examination room-size to 5.\nDown to 2 if suspect uses Mask", "type": "special"},
    "note": {"tooltip": "Macthing items for 2+ AP to\nWaiting-room profiles green items", "type": "special"},
    "poster": {"tooltip": "Increase both room-sizes to 4.\n Both down to 2 if suspect plays Mask", "type": "special"},
    "safe": {"tooltip": "Gain 4 extra SP next day.\n Loose all if suspect plays Lockpick", "type": "special"},
    "telegram": {"tooltip": "Add 1 profile to waiting-room next day,\nEmpty waiting-room if suspect\n uses Cipher", "type": "special"},
    "whiskey": {"tooltip": "Yellow item is now profiles ability", "type": "special"},
}

enemy_items = {
    "bag": {"tooltip": "Removes one random profile from waiting-room\nas long as this item is in play", "type": "enemyitem"},
    "bribe": {"tooltip": "Removes one random profile from examination-room\nas long as this item is in play", "type": "enemyitem"},
    "cipher": {"tooltip": "If player item Telegram is active\nempty waiting-room.", "type": "enemyitem"},
    "gloves": {"tooltip": "If player item Duster is active\nempty examination-room.", "type": "enemyitem"},
    "ladder": {"tooltip": "Loose one extra day as long as\nitem is in play.", "type": "enemyitem"},
    "lockpick": {"tooltip": "If player item Safe is active\nloose all Special AP.", "type": "enemyitem"},
    "mask": {"tooltip": "If player item Cab, Newspaper or\nPoster is active loose 3 days.", "type": "enemyitem"},
    "shovel": {"tooltip": "If player item Cell is active\nloose 3 days.", "type": "enemyitem"}
}

# Delt profiles images update on mouse-hover 
card_images_d = {f"{name}_delt.png": f"images/profiles/{name}_delt.png" for name in profiles.keys()}
card_images_d.update({f"{name}_delt_hov.png": f"images/profiles/{name}_delt_hov.png" for name in profiles.keys()})
card_images_d.update({f"{name}_delt.png": f"images/profiles/{name}_delt.png" for name in profiles.keys()})

# Waiting room profiles images update on mouse-hover 
card_images_h = {f"{name}_hand.png": f"images/profiles/{name}_hand.png" for name in profiles.keys()}
card_images_h.update({f"{name}_hand_hov.png": f"images/profiles/{name}_hand_hov.png" for name in profiles.keys()})
card_images_h.update({f"{name}_hand.png": f"images/profiles/{name}_hand.png" for name in profiles.keys()})

# Examination profiles images update on mouse-hover 
card_images_p = {f"{name}_play.png": f"images/profiles/{name}_play.png" for name in profiles.keys()}
card_images_p.update({f"{name}_play_hov.png": f"images/profiles/{name}_play_hov.png" for name in profiles.keys()})
card_images_p.update({f"{name}_play.png": f"images/profiles/{name}_play.png" for name in profiles.keys()})

# Player items images update on mouse-hover 
card_images_i = {f"{name}.png": f"images/items/{name}.png" for name in player_items.keys()}
card_images_i.update({f"{name}_hov.png": f"images/items/{name}_hov.png" for name in player_items.keys()})
card_images_i.update({f"{name}.png": f"images/items/{name}.png" for name in player_items.keys()})

