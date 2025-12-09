# Professor Assistant — version 1.0

A small command-line helper to create exams from a plain text question bank.

## Files
- `2401509.py` — interactive Python script that reads a question bank and writes a generated exam file.
- `queation_bank.txt` — sample question/answer bank (alternating lines: question then answer).

## Requirements
- Python 3.x

## Run
From PowerShell (in the project folder or with full paths):

```powershell
py "d:\2401509\2401509.py"
# or
python "d:\2401509\2401509.py"
```

Follow the prompts:
- Enter your name
- Type `Yes` to create an exam
- Provide the path to the question bank (e.g. `d:\2401509\queation_bank.txt`)
- Enter how many question-answer pairs to include
- Provide an output path (e.g. `d:\2401509\midterm.txt`)

To run non-interactively, create an `input.txt` file with responses (one per line) and use:

```powershell
py "d:\2401509\2401509.py" < "d:\2401509\input.txt"
```

## Notes
- The question bank must be alternating lines: question line, then its answer line.
- The file `queation_bank.txt` in this repo is an example (note the filename typo).

If you'd like, I can also add a license or an example `input.txt` file.
