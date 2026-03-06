# AI Error Explainer

AI Error Explainer is a simple Python tool that helps programmers understand coding errors more easily.  
Instead of searching online or reading long documentation, users can paste an error message and get a clear explanation along with possible fixes.

This project uses a **local AI model (Mistral via Ollama)** to analyze and explain errors in a structured way.

---

## Features

- Explains programming errors in simple language
- Identifies the programming language when possible
- Provides the meaning of the error
- Explains why the error happens
- Suggests ways to fix the issue
- Gives example corrected code

---

## Tech Stack

- Python
- Ollama
- Mistral LLM
- Requests library

---

## How It Works

1. The user enters a programming error.
2. The Python script sends the error to a local AI model.
3. The AI analyzes the error and generates a structured explanation.
4. The explanation is displayed in the terminal.

---

## Example

Input:

```
TypeError: can only concatenate str (not "int") to str
```

Output:

```
Programming Language: Python

Meaning:
You tried to combine a string with an integer.

Why it happens:
Python cannot automatically convert integers into strings.

Fix:
Convert the integer into a string before concatenating.

Correct Code Example:
print("Age: " + str(age))
```

---

## Installation

1. Install Python
2. Install Ollama

Download from: https://ollama.com

3. Pull the Mistral model

```
ollama run mistral
```

4. Install required Python package

```
pip install requests
```

---

## Running the Project

```
python error_explainer.py
```

Then enter the error you want explained.

---

## Purpose

This project was built as a learning exercise while experimenting with **AI integration in Python applications** and exploring how local LLMs can help developers understand coding errors faster.

---

## Future Improvements

- Support multiple programming languages
- Detect errors from full code snippets
- Add a graphical interface
- Build a web version of the tool
