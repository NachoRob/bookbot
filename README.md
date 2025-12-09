# 🤖 BookBot

BookBot is my first [Boot.dev](https://www.boot.dev) project!

---

## 📚 About BookBot

BookBot is a simple command-line utility that **analyzes the text content** of any book file, providing a comprehensive report on the word count and the frequency of every alphabet character used. It's a quick way to gain basic statistical insights into a text file.

---

## 💻 Tech Stack

This project is built purely with **Python 3**. It focuses on core Python concepts, specifically:

* **Standard Library:** Utilizes the built-in `sys` module for handling command-line arguments (CLI).
* **Data Structures:** Heavy use of **dictionaries** for efficient character counting and **lists of dictionaries** for sorting and reporting results.
* **File I/O:** Reads text files directly using context managers (`with open(...)`).

## ✨ How to Run It

1.  **Clone the Repository** (assuming you have a repository).
2.  **Run the script** from your terminal, providing the path to a text file (e.g., a book):

```bash
python3 main.py books/frankenstein.txt
```

Example Output

```
============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found 158330 total words
--------- Character Count -------
e: 18788
t: 13355
a: 11843
o: 10839
i: 10609
...
============= END ===============
```

**Fun Fact**: The letter 'e' is almost always the most common character. If you run BookBot on any English book and 'e' doesn't top the list, you've found a truly unique piece of literature!