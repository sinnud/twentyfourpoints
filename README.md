# Twenty Four Points

## Overview
This project is a Python game where you draw 4 random playing cards and try to use their numbers (with +, -, *, /) to make 24. J=11, Q=12, K=13.

## Getting Started

### Prerequisites
Make sure you have Python installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

### Installation
1. Clone the repository:
   ```
   git clone <repository-url>
   ```
2. Navigate into the project directory:
   ```
   cd twentyfourpoints
   ```
3. (Optional) Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate
   ```
4. Install the required dependencies (if any):
   ```
   pip install -r requirements.txt
   ```

### Running the Application
To run the application, execute:
```
python main.py
```
If you encounter import errors, try:
```
PYTHONPATH=. python main.py
```

## Game Modes
- **Single Play:** Try to solve for 24 with randomly drawn cards.
- **Expert Help:** Type `help` or `expert` to input your own numbers and get a solution.

## Contributing
If you would like to contribute to this project, please fork the repository and submit a pull request.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.