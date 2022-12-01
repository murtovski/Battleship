![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome murtovski,

This is the Code Institute student template for deploying your third portfolio project, the Python command-line project. The last update to this file was: **August 17, 2021**

## Reminders

* Your code must be placed in the `run.py` file
* Your dependencies must be placed in the `requirements.txt` file
* Do not edit any of the other files or your code may not deploy properly

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

-----
Happy coding!

#Battleship

I have created my take on the classic Battleship game to be played on Command Line. I took the original size of an 8x8 game and reproduced it
to be played easily. The ships themselves are all a 1x1 where they will be sank after one direct hit.

Users will play against the computer, and will need to sink all 5 enemy battleships to win the game!

##How to play

Battleship is based on the original board game that most people will be familiar with.

In this version of the game, a user and computer board are generated with five ships for both boards.

The player's ships are visible to the player, but the computer's ships are concealed to the user.
The player's ships are displayed to the player using the "X", and will be randomly positioned around the board.
If the player or computer misses a shot, it will be displayed on the opponents side with a "-".
If the player or computer sink an enemy ship, it will be displayed using a "@".

The score will be displayed on every turn and once a player reaches a score of 5 then the enemy can no longer
battle!

