# Importing the Ollama library to interact with the locally running LLM
import ollama  # type: ignore

# Define the name of your local Ollama model (must be already created)
MODEL_NAME = 'my-ollama-model'

# Function for handling a single question-and-answer interaction
def single_prompt():
    prompt = input("Enter your question: ")  # Ask user for input
    response = ollama.generate(model=MODEL_NAME, prompt=prompt)  # Call the model
    print("\nModel response:\n", response['response'])  # Display the result

# Function to run an interactive chatbot loop
def interactive_chatbot():
    print("\nType 'exit' or 'quit' to end the chat.")
    while True:
        prompt = input("You: ")  # Get user input
        if prompt.lower() in ['exit', 'quit']:  # Exit condition
            print("Chat ended.\n")
            break
        response = ollama.generate(model=MODEL_NAME, prompt=prompt)  # Generate response
        print("Ollama:", response['response'])  # Display model response

# Function to handle multiple questions at once (batch processing)
def batch_qa():
    print("\nEnter your questions one by one. Type 'done' when finished.")
    questions = []
    while True:
        q = input("Question: ")  # Take questions one by one
        if q.lower() == 'done':  # End input collection
            break
        questions.append(q)  # Add question to list
    
    # Process each question using the model
    print("\nBatch Q&A Results:")
    for q in questions:
        response = ollama.generate(model=MODEL_NAME, prompt=q)
        print(f"Q: {q}\nA: {response['response']}\n")  # Display Q&A

# Function to summarize a block of text provided by the user
def summarize_text():
    print("\nPaste the text you want summarized. Type 'end' on a new line to finish.")
    lines = []
    while True:
        line = input()  # Read each line of text
        if line.strip().lower() == 'end':  # Stop if user types 'end'
            break
        lines.append(line)  # Add line to text list
    text = "\n".join(lines)  # Join all lines into a single string
    prompt = f"Summarize the following text:\n{text}"  # Create summarization prompt
    response = ollama.generate(model=MODEL_NAME, prompt=prompt)  # Call model
    print("\nSummary:\n", response['response'])  # Display summary

# Main menu to select between functionalities
def main():
    while True:
        # Display menu
        print("\n--- Local AI Assistant ---")
        print("1. Single Q&A")
        print("2. Interactive Chat")
        print("3. Batch Q&A")
        print("4. Summarization")
        print("5. Exit")
        choice = input("Choose an option (1-5): ")  # Get user choice

        # Route to appropriate function based on input
        if choice == '1':
            single_prompt()
        elif choice == '2':
            interactive_chatbot()
        elif choice == '3':
            batch_qa()
        elif choice == '4':
            summarize_text()
        elif choice == '5':
            print("Goodbye!")  # Exit program
            break

# Run the program if executed directly
if __name__ == "__main__":
    main()
