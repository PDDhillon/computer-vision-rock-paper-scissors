# Computer Vision RPS

# Milestone 2 
Teachable machine is a google application that allows you to create machine learning models, without having to write any code. I was able to utilise this application to create a machine learning model that will play the game rock paper scissors.

I trained this model on 900 images of me showing the three different states that are present in the game. The high amount of images meant that it would be more accurate at being able to detect the correct outcome. After completing, I exported the model and pushed the two susbsequent files to git. These files will now help to complete the implementation of rock paper scissors.

![alt text](https://github.com/pddhillon/computer-vision-rock-paper-scissors/blob/main/teachable_machine.png?raw=true)

# Milestone 3
Dependency management is an important aspect of programming in python. When working on multiple projects, it could become an issue if many of our imported modules and dependencies begin to clash with one another. For example, one project may require version A of module A. Another project may require a Module B which required version B of module A. This would create an issue when moving between projects.

To manage this, we can utilise conda and pip. Conda was utilised in this project in order to create our own virtual environment. These virtual environments allow me to be able to keep my modules/dependencies local to that environment. This means if I create another environment, there would be no conflicts. We used Pip as our dependency manager in order to install all the prerequisite modules for the Rock-Paper-Scissors game. (opencv-python, tensorflow, ipykernel)

# Milestone 4
A simple python script was created to play a game of Rock-Paper-Scissors through the terminal. I used the OOP principle of Abstraction in order to create reusable functions to play the game. A function to get a random choice to be used as the computers input. A terminal input from the user to be used as our user input in a get user input function. Subsequentyl, a get winner function was used to evaluate these two inputs and determine who wins. Finally, a play function was used to utilise these three functions and play one singular game of Rock-Paper-Scissors

![alt text](https://github.com/pddhillon/computer-vision-rock-paper-scissors/blob/main/code_fragment.png?raw=true)

# Milestone 5
This milestone was the culmination of all the work performed in previous milestones. The camera takes the current frame after a 3 second countdown (CV2 module). This frame is then normalised and Tensorflow runs my model created in teachable machine, in order to return a prediction on what the frame shows. I created a module called RPS that housed all the components needed to play a game of RPS. This allowed me to utilise all that i'd learned in the prerequisities. An abstract class "Player" is inherited by "User" and "Computer". The "Player" also inherits from "GetChoiceMixin". This mixin was created similar to how we have Interfaces in C#. It allowed me to force all concrete classes to implement their own version of a get_choice method. Finally a "Game" class is used to keep track of all information to do with the game. These classes are then instantiated and utilised to play the RPS game. The result is printed in the terminal for each round.

![alt text](https://github.com/pddhillon/computer-vision-rock-paper-scissors/blob/main/example.png?raw=true)

There are many improvements that I would make, in order to improve this game.

- First, I would use a larger dataset of images in order to make my game playable by anyone. Currently, I have to wear the same clothes, same lighting etc, in order to get reliable results
- I would also use the capabilities of the CV2 library to have a much more intuitive visual experience, rather than relying on the terminal.
