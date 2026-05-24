 📈 AlphaStock — Stock Portfolio Tracker

Welcome to AlphaStock, a lightweight, console-based investment tracking application built entirely in Python. 

This project was developed as part of my CodeAlpha Internship to master Python dictionaries, basic data arithmetic, error validation, and file handling.



 ✨ Features
 🏬 Built-in Market Database: Simulates stock market tracking using a predefined price dictionary.
 🛡️ Robust Input Protection: Includes error-handling ('try-except') to prevent crashes if a user accidentally enters letters for quantity or a stock that doesn't exist.
 🧮 Dynamic Math Processing: Automatically aggregates shares and multiplies them by market costs to generate real-time evaluations.
 💾 File Generation (UTF-8 Compliant): Offers the option to export your portfolio summary to a local text file ('portfolio_summary.txt') with universal emoji and character support!



 🛠️ Concepts Practiced
 📖 Dictionaries: Using 'key:value' pairs to instantly fetch stock prices by their ticker names.
 🚨 Exception Handling: Managing input errors seamlessly via 'try-except' blocks.
 💾 File I/O: Reading/writing text files safely using the 'with open()' statement and specifying proper 'utf-8' text encoding.


Sample System Database:
🍏 AAPL (Apple) — $180 / share
⚡ TSLA (Tesla) — $250 / share
🔍 GOOG (Google) — $150 / share
📦 AMZN (Amazon) — $175 / share
💻 MSFT (Microsoft) — $400 / share

Made with 💖 during my Python Programming learning journey!



 🚀 How to Run and Use

1. Ensure Python 3 is installed on your operating system.
2. Launch the script using your command prompt or terminal:
   '''bash
   python stockportfolio_tracker.py