# 🕹️ Hangman Game in Python

A simple and interactive command-line Hangman game written in Python.

## 🚀 Overview

Hangman is a word-guessing game where you must guess a hidden word one letter at a time. You have **6 lives**, and each wrong guess brings the hangman closer to being complete. Can you guess the word before it's too late?

## 📌 Features

- Random word selection from a predefined list
- Real-time feedback on correct/incorrect guesses
- Visual stages for incorrect guesses (ASCII art)
- Tracks previously guessed letters to avoid repetition
- Win/Lose message at the end of the game

## 🧠 How It Works

1. A word is selected at random from a list.
2. The word is masked with underscores `_ _ _ _` (one for each letter).
3. You guess one letter per turn.
4. If the letter is in the word:
    - It replaces the corresponding blank(s).
5. If the letter is **not** in the word:
    - You lose a life (starts with 6).
6. The game ends when:
    - You guess the word (Win)
    - You run out of lives (Lose)

## 🛠️ Technologies Used

- Python 3
- ASCII Art for visual feedback

## 📁 Project Structure

Day6_Hangman/  
│
├── Day6_Hangman_main.py # Main game logic  
├── Day6_Hangman_words.py # Word list used for random selection  
└── Day6_Hangman_Stages.py # ASCII art stages and game logo  

## 📷 Sample Output
Welcome to Hangman!
_ _ _ _ _

You have 6/6 lives left  
Guess a letter: a  
You chose 'a', which is wrong. You lose a life!  
You have 5/6 lives left  

_ _ _ _ a 
...

## ✨ Future Improvements
Add support for full word guesses

Add difficulty levels (Easy, Medium, Hard)

Score tracking system

GUI version using Tkinter or PyQt

## 👨‍💻 Author
Arghyajyoti Samui

GitHub: @Arghyajyoti007




