# Multi-agent_SARSA

## Goal of the project is to analyze the behaviour of multiple machine learning agent when they all are assign to complete one single task.

In this project agent_A and agent_B is assign to catch one enemy. agent_A can move with 2x speed while agent_B can only move with 1x speed.

SARSA Machine learning algorithm is used to train the model.

## Agent Actions

Both agent can perform 4 actions left, right, up and down.

## Reward logic

if agent_A catch enemy = +10
if agent_B catch enemy = +10
if agent collide with each other = -10
step penalty = -1
if both agent catch the enemy at same time = +500


![]()
