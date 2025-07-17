Project Overview
This repository demonstrates how to deploy a Large Language Model locally using Ollama, customize its behavior with a Modelfile, and build a fully-featured, menu-driven Python AI assistant. You’ll find step-by-step instructions for model creation, setup, and code usage—ideal for students, developers, and anyone exploring local AI solutions.

Table of Contents
Prerequisites

Step 1: Create a Custom Model with Ollama

Step 2: Build and Register Your Model

Step 3: Python Script – Local AI Assistant

How to Run the Assistant

Sample Interactions

Troubleshooting

Next Steps & Enhancements

1. Prerequisites
Ollama Installed: Download and install from Ollama’s official site.

Python 3.7+ Installed

Ollama Python Library: Install with
pip install ollama
At least one LLM Installed: Such as llama3.2, via
ollama pull llama3.2


Step 1: Create a Custom Model with Ollama
A. Make a Project Folder
Open File Explorer, navigate to your Documents or Desktop.
Right-click > New > Folder > Name it my-ollama-model.
B. Add the modelfile
Open the folder my-ollama-model.
and add the modelfile file in it 

3. Step 2: Build and Register Your Model
A. Open Command Prompt

Navigate to your model folder
cd C:\Users\<YourName>\Documents\my-ollama-model
(Replace <YourName> with your Windows username)

B. Build and Register the Model:

Run:
ollama create my-custom-model -f ./Modelfile
When successful, you’ll see a confirmation.

C. Verify Model Availability:

List models with:
ollama list
Confirm my-custom-model is on the list.

Step 3:  is the Python Script 
Step 4:
How to Run the Assistant
Ensure Ollama is running and your custom model is listed.

Open Command Prompt, navigate to the script’s directory.

Run:
python (name of the python script).py

Troubleshooting
ModuleNotFoundError: Ensure you ran pip install ollama.

AttributeError (no attribute 'generate'):

Do not name your script ollama.py.

Remove any duplicate files named ollama.py or ollama.pyc in the script’s folder.

Model Not Found: Verify your model name with ollama list and update MODEL_NAME in your script.

Ollama not running: Start Ollama via its desktop shortcut or by running ollama in a terminal.
