import random


class entity:
    def __init__(self, hp, defence, atk, name):
        self.hp = hp
        self.name = name
        self.defence = defence
        self.atk = atk
        self.init_hp = hp

    def is_alive(self):
        return self.hp > 0

    def damage(self, hp):
        # print(f'{self.name} took {hp} damage!')
        self.hp -= hp

    def rand_ev(self, chns):
        return random.randint(0, 101) < chns

    def attack(self, entity):
        atk = self.atk - entity.defence
        if atk < 0:
            atk = 0
        entity.damage(atk)

    def reset(self):
        self.hp = self.init_hp


class Knight(entity):
    def __init__(self, hp, defence, atk, dodge_chns, krit_chns, name):
        super().__init__(hp, defence, atk, name)
        self.dodge = dodge_chns
        self.krit = krit_chns

    def damage(self, hp):
        if self.rand_ev(self.dodge):
            # print(f'{self.name} dodged {hp} damage!')
            return
        else:
            # print(f'{self.name} took {hp} damage!')
            self.hp -= hp

    def attack(self, entity):
        if self.rand_ev(self.krit):
            atk = self.atk * 3 - entity.defence
            # print(f'{self.name} attack: CRIT {self.atk*3} damage!')
        else:
            atk = self.atk - entity.defence
            # print(f'{self.name} attack: {self.atk} damage!')
        entity.damage(atk)


class Dragon(entity):
    def __init__(self, hp, defence, atk, insta_kill_chns, dodge_chns, name):
        super().__init__(hp, defence, atk, name)
        self.insta_kill = insta_kill_chns
        self.dodge = dodge_chns

    def attack(self, entity):
        if self.rand_ev(self.insta_kill):
            atk = entity.hp * 10
            # print(f'{self.name} INSTA KILL ATTACK!: {atk} damage!')
            entity.damage(atk)
        else:
            # print(f'{self.name} attack: {self.atk} damage!')
            atk = self.atk - entity.defence
            entity.damage(atk)


class Arena:
    def __init__(self, wariors: list):
        self.wariors = wariors
        self.winrate = {warior: 0 for warior in self.wariors}

    def fight(self):
        local_wariors = self.wariors.copy()
        for w in local_wariors:
            w.reset()
        while len(local_wariors) > 1:
            # print(local_wariors)
            warior = random.choice(local_wariors)
            targets = local_wariors.copy()
            targets.remove(warior)
            target = random.choice(targets)  # type: entity
            if not target.is_alive():
                # print(f'{target.name} died.')
                local_wariors.remove(target)
            else:
                warior.attack(target)
            # print('\n=========STATS==========')
            for warior in self.wariors:
                pass
                # print(f'{warior.name}: {warior.hp} hp')

            # print('========================\n')

        # print(f"{local_wariors[0].name} - won!")
        self.winrate[local_wariors[0]] += 1


if __name__ == '__main__':
    knight = Knight(300, 30, 80, 90, 33, "Dillinor__")
    dragon = Dragon(1500, 60, 120, 25, 0, 'Dragon')
    arena = Arena([knight, dragon])
    for _ in range(1_000_000):
        arena.fight()
    print('\n============SCORE BOARD============')
    for warior, winrate in arena.winrate.items():
        print(f'{warior.name}: {winrate}\n')
    print('=====================================\n')
