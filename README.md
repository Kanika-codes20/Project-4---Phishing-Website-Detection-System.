# Phishing Website Detection System 

A beginner-friendly Python cybersecurity project that analyzes website URLs for characteristics commonly associated with phishing websites.

The project uses several URL-based indicators to calculate a risk score and classify the URL as **LOW**, **MEDIUM**, or **HIGH** risk.

## About the Project

Phishing websites are designed to trick users into providing sensitive information or interacting with malicious content.

This project provides a simple way to examine a URL for suspicious characteristics.

Instead of relying on a single indicator, the system checks multiple characteristics and combines them into a risk score.

## Features

- Accepts a website URL as user input
- Analyzes the URL for multiple suspicious indicators
- Uses regular expressions to detect certain URL patterns
- Checks for suspicious characters such as `@`
- Checks for IP addresses used as hostnames
- Checks for suspicious words in the URL
- Analyzes the URL hostname
- Calculates a risk score based on detected indicators
- Provides reasons for the assigned score
- Classifies the URL into LOW, MEDIUM, or HIGH risk

## URL Indicators

The system checks for several characteristics that can contribute to the risk score.

### Suspicious `@` Character

The project checks whether the URL contains an `@` character, which can be used in deceptive URLs.

### IP Address

The system checks whether the hostname is an IP address rather than a normal domain name.

### Suspicious Words

The project checks the URL for words that may appear in suspicious or deceptive links.

### Hostname Analysis

The hostname is analyzed for characteristics that may contribute to the risk score.

Each detected indicator can add points to the overall risk score.

## 📊 Risk Scoring

After analyzing the URL, the system calculates a risk score based on the indicators it detects.

The score is then used to assign a risk level:

```text
LOW
MEDIUM
HIGH
```

The system also displays the reasons that contributed to the score so that the result is easier to understand.

## Technologies Used

- Python
- Regular Expressions (`re`)
- URL parsing (`urllib.parse`)
- String processing

## Python Concepts Practiced

This project helped me practice:

- Variables
- User input
- Strings
- `.lower()`
- `.strip()`
- `if`, `elif`, and `else`
- Functions
- Lists
- Loops
- Regular expressions
- Modules and imports
- URL parsing
- Conditional risk scoring

## What I Learned

While building this project, I learned how Python can be used to analyze URLs and identify patterns that may be associated with phishing.

I also learned how multiple indicators can be combined into a simple risk-scoring system instead of relying on only one condition.

The project helped me connect Python programming concepts with practical cybersecurity ideas.

## How to Run

1. Make sure Python is installed on your computer.
2. Clone or download this repository.
3. Open the project in PyCharm or another Python IDE.
4. Run the main Python file.
5. Enter a website URL when prompted.
6. Review the risk score, risk level, and detected indicators.

## Example

```text
Enter the website URL: http://example.com

Risk Score: 0
Risk Level: LOW
```

A URL containing multiple suspicious indicators may produce a higher score and display the reasons that contributed to the result.

## Limitations

This project is a **basic educational URL analyzer**, not a complete phishing-detection or website-security system.

A URL can contain suspicious characteristics without actually being malicious, and a phishing URL may not trigger the indicators used by this project.

The system does not visit or interact with websites to determine whether they are malicious.

Therefore, the risk level should be treated as an educational indicator rather than a definitive determination that a website is safe or malicious.

## Project Context

This project was created as part of my beginner cybersecurity and Python learning journey.

The goal was to understand how URL characteristics can be analyzed programmatically and how simple cybersecurity detection logic can be implemented using Python.

## Future Improvements

Possible future improvements could include:

- Adding more URL indicators
- Improving the risk-scoring system
- Adding additional URL parsing checks
- Creating a graphical user interface
- Integrating trusted external threat-intelligence sources

---

**Educational cybersecurity project built with Python. 🐍🛡️**
