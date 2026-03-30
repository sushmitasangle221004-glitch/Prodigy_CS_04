# Prodigy_CS_04
# ⌨️ Simple Keylogger

A simple **Python Keylogger** built using the `pynput` library that records keystrokes and saves them into a log file with timestamps.

---

## 📌 Project Description

This project captures keyboard inputs in real-time and logs them into a file named **`keylog.txt`** along with the exact date and time each key was pressed.

It is designed for **educational purposes** to understand how keyboard event listeners work in Python.

---

## 🚀 Features

* ⌨️ Records all key presses
* 🕒 Adds timestamps to each keystroke
* 📁 Saves logs into a file (`keylog.txt`)
* 🛑 Stops logging when **ESC key** is pressed
* ⚡ Lightweight and easy to run

---

## 🛠️ Technologies Used

* Python 3
* `pynput` library
* Built-in modules:

  * `datetime`
  * `os`

---

## ⚙️ Requirements

Install the required library before running:

```bash id="k2d9x1"
pip install pynput
```

---

## ▶️ How to Run

### Step 1: Clone the Repository

```bash id="p8s3n2"
git clone https://github.com/your-username/keylogger-python.git
```

### Step 2: Navigate to Project Folder

```bash id="x7f2l0"
cd keylogger-python
```

### Step 3: Run the Script

```bash id="m4v9q8"
python prodigy_cs_04.py
```

---

## 🧪 How It Works

1. The program starts a keyboard listener.
2. Every key press is recorded with a timestamp.
3. Data is stored in `keylog.txt`.
4. Press **ESC** to stop the keylogger.

---

## 🖥️ Sample Log Output

```id="n3b7k5"
Keylogger started at 2026-03-30 10:15:23
[2026-03-30 10:15:25] h
[2026-03-30 10:15:26] e
[2026-03-30 10:15:26] l
[2026-03-30 10:15:27] l
[2026-03-30 10:15:27] o
[2026-03-30 10:15:28] Key.space
```



## 👨‍💻 Author

**Sushmita Suryakant Sangle**
Task 4 : Simple Keylogger - Completed


---

