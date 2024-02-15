# Day 57 - Flask with Jinja

This project is a simple web application built with Flask and Jinja, a lightweight web framework in Python.  
The application has three main functionalities:

## Overview: 

![Screenshot 2024-02-15 at 12 08 02](https://github.com/JonatasViscaino/100-days-of-code-Python/assets/121301717/1c81bbec-d333-4272-bdc7-d12a518c8b56)

### Blog Display:

The home route ("/") displays a list of blog posts fetched from an external API (https://api.npoint.io/c790b4d5cab58020d391).
The blog posts are rendered on the index.html template using Jinja templating, providing a clean and dynamic layout for users to browse through.

### Individual Blog Post:

Clicking on the "Read" link for each blog post directs the user to an individual post view ("/post/int:index").
The get_post route retrieves the specific blog post based on the provided index and renders it on the post.html template.

### Name Guessing Game:

The application includes a fun name guessing game ("/guess/<name>") utilizing external APIs for age and gender prediction.
The guess_game route fetches information about the provided name from Agify and Genderize APIs, displaying the estimated age and gender on the guess_name.html template.

## Project Structure:

server.py contains the Flask application setup, routes, and interactions with external APIs.
HTML templates (index.html, post.html, guess_name.html) use Jinja templating to dynamically display content and create a cohesive user interface.

## Note:

Make sure to install the required packages (Flask and other dependencies) before running the application.
Enjoy exploring the blog and have fun with the name guessing game! 🚀

Feel free to customize the description further based on additional features or functionalities you might want to highlight!
