# VCF Contact Generator

**VCF Contact Generator** is a simple Python package that allows generating VCF (vCard) files containing contacts.

## 📌 Features

- Create a single contact in `.vcf` format.
- Create a contact library and save it to a `.vcf` file.

## 📦 Installation

To install the package, use:

```sh
pip install -r requirements.txt
```

## 🚀 Usage

### 1. Creating a Single Contact

```python
from contacts import create_single_contact

create_single_contact("contacts.vcf", "John Doe", "+1234567890")
```

### 2. Creating a Contact Library

```python
from contacts import create_library

contacts = [
    ("Alice Smith", "+1122334455"),
    ("Bob Johnson", "+2233445566")
]

create_library("contacts.vcf", contacts)
```

## 🧪 Testing

To run unit tests, use:

```sh
pytest test.py
```

## 🛠 Requirements

- Python 3.8+
- `pytest` (optional, for testing)

## 📄 License

This project is available under the MIT license. You are free to use and modify it.

---
✉️ If you have any questions or suggestions, feel free to contact me via GitHub! 😊

