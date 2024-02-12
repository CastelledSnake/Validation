# Validation

Cours Validation @ ENSTA Bretagne.

## Installation

- Python 3.10

1. Clone the repo :

```bash
git clone git@github.com:CastelledSnake/Validation
```

2. (optional) Create and activate a python virtual environment for the project

For `conda` users :

- Create the environment

```bash
conda create -n ensta_validation python=3.10
```

- Activate the environment

```bash
conda activate ensta_validation
```

For `venv` users :

- Create the environment

```bash
python3 -m venv venv
```

- Activate the environment

```bash
source venv/bin/activate
```

3. Install the dependencies

```bash
pip install .
```

4. Run the `main.py` file or the tests

```bash
python3 main.py
pytest
```

## Authors

- Vincent C. (@CastelledSnake)
- Mathis U. (@LBF38)

## Notes

Date limite du rendu du projet: **Lundi 12/02/2024, 8h00**

TODO before final release:

- [ ] Finish implementation of the different types of validation
  - [ ] Implementation of AliceBob V1 (ou 0) (for @LBF38)
    - [ ] graph
    - [X] semantics
    - [ ] soup
  - [ ] Implementation of AliceBob V2 & 3 (for @CastelledSnake)
    - [ ] graph
    - [X] semantics
    - [ ] soup
- [x] Finish tests
- [x] Add documentation (some comments on the implementation)
- [x] Add [comments for improvements on the course](./Comments%20on%20the%20course.md)
