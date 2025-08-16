# main.py

from src.single_play import single_play
from src.expert_help import expert_help

def main():
    print("Welcome to Twenty Four Points!")
    user_input = "single play"
    while True:
        if user_input.lower() in ('quit', 'exit'):
            print("Goodbye!")
            break
        elif user_input.lower() in ('help', 'expert'):
            print("Type 'help' or 'expert' for expert help, 'quit' or 'exit' to quit;")
            print("Let's get help from expert...")
            user_input = expert_help()
        else:
            print("Type 'help' or 'expert' for expert help, 'quit' or 'exit' to quit;")
            print("Let's start single play.")
            user_input = single_play()

if __name__ == "__main__":
    main()