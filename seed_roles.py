from app import app, db, Role

# Use the app context
with app.app_context():
    roles = [
        # Your role objects here
        Role(name='Warrior', description='A fearless and battle-hardened gladiator, the Warrior excels in close combat, wielding heavy weapons and armor to protect their allies and crush their foes on the front lines of epic quests.'),
        Role(name='Wizard', description='Masters of arcane magic, Wizards harness the mystical forces of the universe to cast powerful spells, conjure elements, and manipulate reality itself, using their intellect and knowledge to unlock the secrets of the arcane.'),
        Role(name='Assassin', description='Silent shadows in the night, Assassins are deadly experts in stealth and subterfuge. They specialize in precise strikes and covert tactics, eliminating targets with precision and cunning, often working from the shadows to complete their missions.'),
        Role(name='Ranger', description='Guardians of the natural world, Rangers are skilled archers and wilderness experts. They navigate forests, deserts, and mountains, forming deep connections with the animals and elements, and using their knowledge to protect the land and its inhabitants.'),
        Role(name='Templar', description='Devoted to a divine cause, Templars are holy warriors who wield faith and courage as their weapons. They defend against the forces of darkness, wielding divine magic and righteous zeal in service of their sacred order.'),
        Role(name='Wicken', description='Wicken are practitioners of ancient nature-based magic, drawing their power from the earth and the spirits that inhabit it. They work in harmony with the natural world, using herbs, rituals, and incantations to heal, protect, and commune with the forces of nature.'),
    ]

    for role in roles:
        db.session.add(role)

    db.session.commit()

