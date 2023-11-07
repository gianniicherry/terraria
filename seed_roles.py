from app import db, Role

def seed_roles():
    roles = [
        Role(name='Warrior', description='A strong and fearless warrior.'),
        Role(name='Wizard', description='A wise and powerful wizard.'),
        # Add more roles as needed
    ]

    for role in roles:
        db.session.add(role)

    db.session.commit()

if __name__ == '__main__':
    seed_roles()
