# Day 29 and 30 - GUI Password Manager

This Python script implements a simple password manager with a graphical user interface (GUI) built using Tkinter. The program allows users to store and retrieve login details for various websites securely.

## Libraries Used:
- **Tkinter**: The standard GUI library for creating graphical interfaces.
- **pyperclip**: Enables copying generated passwords to the clipboard for easy use.
- **json**: Handles reading and writing data in JSON format for persistent storage.

## Features:
- **Add Data**: Easily add website details, including email and password, which are then saved in a JSON file ("data.json").
- **Generate Password**: Generate strong, random passwords with a mix of letters, symbols, and numbers.
- **Search Data**: Retrieve stored login details for a specific website.
- **Exception Handling**: The script incorporates robust exception handling, addressing FileNotFoundError by creating a new data file ("data.json") and employing general exception handling to prevent unexpected crashes.

## Usage:
1. Run the script.
2. Enter website details, including email and password.
3. Optionally, generate a secure password.
4. Save the data or search for existing details.

![GUI Password Manager](https://github.com/JonatasViscaino/100-days-of-code-Python/assets/121301717/a94356b3-a31e-428a-b50f-f9e90ace8618)

Feel free to customize and enhance this password manager to suit your needs!
