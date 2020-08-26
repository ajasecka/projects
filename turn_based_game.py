"""
This is a program that uses Reinforcement Learning to play a turn-based fighting game
"""

import requests
import json
import random
from random import *
import numpy as np


ROLL = [.85, 1.0]
ALPHA = .1
GAMMA = .9
ACTIONS = ['attack', 'heal']
ITERATION = 20000
HEALTH = 50


class Person:
    def __init__(self, name, health, atk, defense, speed):
        self.name = name
        self.max_health = health
        self.health = health
        self.atk = atk
        self.defense = defense
        self.spd = speed

    def attack(self, enemy):
        enemy.health -= int(self.atk * uniform(ROLL[0], ROLL[1]))
        if enemy.health <= 0:
            return True
        return False

    # heals 40% health
    def heal(self):
        self.health += int(self.max_health * .4)
        if self.health > self.max_health:
            self.health = self.max_health


def update_q(q_table, curr_s, next_s, curr_a):
    # reward determined by if enemy was defeated
    reward = 0
    if next_s[1] == 0:
        reward = 1
    elif next_s[0] == 0:
        reward = -1
    elif curr_s == next_s:
        reward = -.1

    # Bellman equation
    q_table[curr_s[0]][curr_s[1]][curr_a] += ALPHA * (reward + GAMMA * np.max(q_table[next_s[0]][next_s[0]]) - q_table[curr_s[0]][curr_s[1]][curr_a])


# performs whichever move was chosen for action
def make_move(p1, p2, action1, action2):
    first = choose_order(p1, p2)

    if first == p1.name:
        if action1 == 'attack':
            if p1.attack(p2):
                return p1.name
        elif action1 == 'heal':
            p1.heal()
        if action2 == 'attack':
            if p2.attack(p1):
                return p2.name
        elif action2 == 'heal':
            p2.heal()
    else:
        if action2 == 'attack':
            if p2.attack(p1):
                return p2.name
        elif action2 == 'heal':
            p2.heal()
        if action1 == 'attack':
            if p1.attack(p2):
                return p1.name
        elif action1 == 'heal':
            p1.heal()
    return False


# returns the state of p1 and p2
# TODO could add every single field
def get_state(p1, p2):
    # TODO CHANGE SO THAT IT IS THE COMPLETE EQUATION FOR ATTACK DAMAGE
    # THESE STATES SHOULD INCLUDE THE POTENTIAL DAMAGE EACH ATTACK CAN DO SO IT KNOWS THE NEXT STEP
    power = 70
    # WILL "ROLL" CAUSE A PROBLEM???
    modifier = 1 # crit, ROLL, etc
    # damage = np.floor((((42 * power * (p2.atk / p1.defense)) / 50) + 2) * modifier)

    p1_dis_health = int(np.ceil(HEALTH * p1.health / p1.max_health))
    p2_dis_health = int(np.ceil(HEALTH * p2.health / p2.max_health))
    # speed should be 1, -1, or 0 (equal)

    return [p1_dis_health, p2_dis_health]

# choosing order of who goes first
def choose_order(p1, p2):
    if p1.spd > p2.spd:
        return p1.name
    elif p2.spd > p1.spd:
        return p2.name
    else:
        return p1.name if randint(0, 1) else p2.name


def battle(q_table):
    p1 = Person('p1', 1000, 150, 100, 100)
    p2 = Person('p2', 2000, 200, 100, 150)
    rounds = 0
    wins = 0
    losses = 0
    # list of all attributes of fighters from p1's perspective (discrete values)
    curr_state1 = get_state(p1, p2)
    while rounds < 200:
        # TODO SWITCH ACTIONS, SHOULD NOT CHOOSE RANDOM ACTION
        # SHOULD BE CHOOSING MAX VALUE
        action1 = np.argmax(q_table[curr_state1[0]][curr_state1[1]])
        # action1 = randint(0, 1)

        winner = make_move(p1, p2, ACTIONS[action1], 'attack')

        # prevents infinite loop (will be able to remove this eventually once moves have limited number of actions)
        if curr_state1 != get_state(p1, p2):
            curr_state1 = get_state(p1, p2)
        else:
            p1.health = 0

        if winner:
            if winner == p1.name:
                wins += 1
            else:
                losses += 1

            p1 = Person('p1', 1000, 150, 100, 100)
            p2 = Person('p2', 2000, 200, 100, 150)
            rounds += 1
            # list of all attributes of fighters from p1's perspective (discrete values)
            curr_state1 = get_state(p1, p2)
    print(f'wins: {wins}\nlosses: {losses}')


def main():
    # Q table of current hp's and actions, but eventually all other stats
    # TODO INCLUDE TOTAL DAMAGE OUTPUT TAKING INTO ACCOUNT HEALTH AND USE THAT AS THE POSITION
    # Q table: p1.health, p2.health, p1 move choice
    q_table = np.random.uniform(-1, 1, (HEALTH + 1, HEALTH + 1, 2))

    print('Before training---------------------')
    battle(q_table)

    # training
    for i in range(ITERATION):
        print(f'Iteration: {i}/{ITERATION}') if (i % 1000 == 0) else None
        p1 = Person('p1', 1000, 150, 100, 100)
        p2 = Person('p2', 2000, 200, 100, 150)
        t = 0
        # list of all attributes of fighters from p1's perspective (discrete values)
        curr_state1 = get_state(p1, p2)
        winner = False
        while not winner:
            t += 1

            # probability the action will explore vs exploit
            exploit = i / ITERATION
            action1 = randint(0, 1) if (random() > exploit) else np.argmax(q_table[curr_state1[0]][curr_state1[1]])

            # TODO WILL NEED TO DO ALL OF THIS FOR P2 TO SIMULATE FIGHT BETWEEN ITSELF
            winner = make_move(p1, p2, ACTIONS[action1], 'attack')

            next_state1 = get_state(p1, p2)

            update_q(q_table, curr_state1, next_state1, action1)

            if winner:
                # print(f'The winner is: {winner}')
                break

            # print(f'{t}) {p1.health} {p2.health}')

            curr_state1 = next_state1

    # print(json.dumps(q_table))

    print('After training---------------------')
    battle(q_table)



if __name__ == '__main__':
    main()