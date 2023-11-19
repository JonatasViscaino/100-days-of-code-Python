# Day 17 - Object-Oriented Quiz Game

This Python project is a simple Quiz Game that tests your knowledge with a set of questions. The game utilizes two key modules:

**Question Model**: The question_model module defines a Question class, providing a blueprint for creating question objects with associated correct answers.

**Quiz Brain**: The quiz_brain module contains a QuizBrain class responsible for managing the quiz flow. It handles the sequence of questions, user responses, and calculates the final score.

**Usage**:
1. Questions are loaded from the question_data module, which contains a list of dictionaries specifying questions and correct answers.  
2. The QuizBrain class is initialized with the question bank, creating an instance of the quiz.  
3. Users progress through the quiz using the next_question() method until there are no more questions.  
4. The game concludes with a summary, displaying the user's final score and the total number of questions answered.