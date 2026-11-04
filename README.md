# Random Small Projects 1

A collection of small Python projects I built in September 2026 to practice and experiment. Each project is a single script (except the 2048 game), so they are easy to read and run on their own.

## Projects

| # | Project | Description |
|---|---------|-------------|
| 1 | [Currency Converter](Currency_Converter.py) | Converts an amount from one currency to another. |
| 2 | [Calculator](Calculator.py) | A simple calculator for basic arithmetic. |
| 3 | [Dice Roll](Dice_Roll.py) | Simulates rolling a dice. |
| 4 | [Number Guess](Number_Guess.py) | Guess the secret number in as few tries as possible. |
| 5 | [Rock Paper Scissors](R_P_S.py) | Play rock, paper, scissors against the computer. |
| 6 | [Word Guess](Word_Guess.py) | Guess the hidden word. |
| 7 | [Hangman Game](Hangman_Game.py) | The classic Hangman word game. |
| 8 | [Comparing Two PDFs](Comparing_Two_PDFs.py) | Compares two PDF files (samples: `f1.pdf`, `f2.pdf`). |
| 9 | [Convert Emoji](Convert_emoji.py) | Converts text into emojis. |
| 10 | [Voice Recorder](Voice_Recorder.py) | Records audio from the microphone. |
| 11 | [Screen Recorder](Screen_Recorder.py) | Records the screen to a video file. |
| 12 | [Mastermind Game](Mastermind_Game.py) | Crack the secret code in a limited number of guesses. |
| 13 | [2048 Game](2048_Game/) | The 2048 puzzle game (`2048.py` + `logic.py`). |
| 14 | [Pokemon Training](Pokemon_Training.py) | A small Pokemon training game. |
| 15 | [Taking Screenshot](Taking_Screenshot.py) | Takes a screenshot of the screen and saves it. |

## Getting Started

### Requirements

- Python 3.8 or newer

Some scripts need extra libraries. Install what you need with pip, for example:

```bash
pip install pyautogui opencv-python numpy
```

Check the `import` lines at the top of each script to see what it needs.

### Run a project

```bash
git clone https://github.com/YOUR_USERNAME/Random_Small_Projects_1.git
cd Random_Small_Projects_1
python Calculator.py
```

Replace `Calculator.py` with any script you want to run. For the 2048 game:

```bash
cd 2048_Game
python 2048.py
```

## Notes

- The screen and voice recorders save their output files in the folder you run them from.
- Press `q` in the preview window to stop the screen recorder.
- `f1.pdf` and `f2.pdf` are sample files used by the PDF comparison script.

## License

Free to use for learning and experimenting.
