# Day 34 - Quizzler - A Simple Quiz Application

## Overview:
Quizzler is a basic quiz application built in Python, featuring a graphical user interface created using Tkinter.  
The application fetches a set of True/False questions from the Open Trivia Database API, and the user can answer them interactively.

## Components:
1. **Main Module (main.py):**
- Imports question data, creates question objects, and initializes the quiz engine.
- Utilizes the QuizBrain class to manage quiz logic.
- Initializes the graphical user interface using the QuizInterface class.
2. **User Interface Module (ui.py):**
- Defines the QuizInterface class responsible for the graphical user interface.
- Displays the current score, question text, and True/False buttons.
- Dynamically updates UI elements based on user input and quiz progress.
3. **Quiz Logic Module (quiz_brain.py):**
- Implements the QuizBrain class, managing the state of the quiz.
- Tracks the question number, score, and the current question.
- Checks user answers and provides feedback.
4. **Data Retrieval Module (data.py):**
- Fetches True/False questions from the Open Trivia Database API using requests.
- Parses the response to extract question data for the quiz.

## Usage:
1. Run the main.py file to start the quiz application.
2. Answer True/False questions using the provided buttons.
3. Receive instant feedback on your answers and see your score.
4. The quiz ends when all questions are answered.

## Technologies Used:
- Tkinter (for GUI)
- Open Trivia Database API
- Requests (for API communication)

**App Preview:**  
![Quizzler App](https://github.com/JonatasViscaino/100-days-of-code-Python/assets/121301717/aa7b410d-f755-435e-b6b6-c1fa64799521)

Feel free to explore, modify, and use this code as a starting point for your own projects or learning endeavors.
