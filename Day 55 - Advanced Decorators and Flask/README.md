# Day 55 - Flask Web Guess the Number with Advanced Decorators

## Introduction

This repository showcases a simple web application built with Flask, a Python web framework, and includes examples of advanced decorators in a separate module.

### Advanced Decorators

#### `advanced_decorator.py`

This module illustrates the application of advanced decorators using two examples:

1. **Authentication Decorator (`is_authenticated_decorator`):**
    - Defines a `User` class with a decorator to check if the user is authenticated.
    - Demonstrates the usage of the decorator with a `create_blog_post` function.

2. **Logging Decorator (`logging_decorator`):**
    - Implements a decorator to log the details of function calls and their return values.
    - Provides an example with the `a_function` function.

## Flask Web Application

#### `server.py`

This file contains a basic Flask web application with two routes:

1. **Root Route ("/"):**
    - Displays an initial page with an instruction to guess a number between 0 and 9.
    - Generates a random number each time the page is loaded.

2. **Guess Route ("/<int:number>"):**
    - Handles user guesses for the randomly generated number.
    - Returns feedback and an image based on whether the guess is correct, too high, or too low.

Feel free to explore and modify the code to better understand Flask and advanced decorators in Python.
