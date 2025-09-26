# Deep Learning Class: Perceptron Logic Gates and Adders (Python)

This repository contains simple perceptron-based implementations of basic logic gates and their compositions into a half/full adder and a 4‑bit ripple-carry adder. It is intended for educational purposes to illustrate how neural units (perceptrons) can emulate boolean logic.

## Contents

- `and_gate.py`: Perceptron implementation of AND
- `or_gate.py`: Perceptron implementation of OR
- `nand_gate.py`: Perceptron implementation of NAND
- `xor_gate.py`: XOR built from NAND, OR, and AND
- `full_adder.py`: 1‑bit full adder built from gates
- `full_adder_4bit.py`: 4‑bit ripple-carry adder built from the 1‑bit full adder

## Requirements

- Python 3.8+ (earlier versions may work, but are untested)
- `numpy`

Install dependencies into a virtual environment (recommended):

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install numpy
```

## Quickstart

Run any module directly to print its truth table or demo output:

```bash
python and_gate.py
python or_gate.py
python nand_gate.py
python xor_gate.py
python full_adder.py
python full_adder_4bit.py
```

## Usage in Python

Each gate function expects binary inputs `0` or `1` and returns `0` or `1`.

```python
from and_gate import AND
from or_gate import OR
from nand_gate import NAND
from xor_gate import XOR

print(AND(1, 1))   # 1
print(OR(0, 0))    # 0
print(NAND(1, 1))  # 0
print(XOR(1, 0))   # 1
```

Full adder (sum and carry) and 4‑bit ripple-carry adder:

```python
from full_adder import FA
from full_adder_4bit import FA_4b

S, C = FA(1, 1, 0)       # S: sum bit, C: carry out
print(S, C)               # -> 0 1

carry_out, sum_bits = FA_4b((1,0,1,0), (0,1,0,1), 1)
print(carry_out, sum_bits)
```

## Notes

- These gates are implemented using simple weighted sums with a bias (perceptron) and step activation.
- Inputs must be integers `0` or `1`.
- Numpy is used only for concise vector math; no training is involved.

## Contributing

Issues and pull requests are welcome. For significant changes, please open an issue first to discuss what you would like to change.

## Author

`@kuoyaoming`

## License

No license specified.
