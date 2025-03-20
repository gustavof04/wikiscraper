# 🕷️ Wikiscraper

Simple web scraping done in Python using the **requests** library to send a GET request to the Wikipedia URL where I performed the scraping, and **Beautiful Soup** for selecting and formatting the HTML of two paragraphs from the following article:

> Project Status: ✔️ (completed)

https://pt.wikipedia.org/wiki/Python

The paragraphs present:
* What the Python language is;
* The origin of the Python language name.

Wikiscraper creates a .txt file as soon as it is executed, displaying the two paragraphs formatted with utf-8 standard and two functions with regex for better readability.

## Technologies used
Python V.: 3.11.1 || Beautiful Soup 4 V.: 4.12.2 || requests V.: 2.31.0

NOTE: Manual installation of Python in the version mentioned above is required to create the virtual environment and install the project dependencies.

- Windows 8+

https://www.python.org/ftp/python/3.11.1/python-3.11.1-amd64.exe

- macOS 10.9+

https://www.python.org/ftp/python/3.11.1/python-3.11.1-macos11.pkg

## Setting up the virtual environment
* In your terminal, navigate to the project's root folder and run the following command to create a virtual environment:

  ```bash
  python -m venv name_of_virtualenv
  ```

* Run the command according to your system to activate your virtual environment:

  **Windows**
  ```bash
  .\name_of_virtualenv\Scripts\activate
  ```

  **Linux or macOS**
  ```bash
  source name_of_virtualenv/bin/activate
  ``` 

## Installing dependencies
* With the virtual environment **activated**, install the project dependencies with the following command:

   ```bash
  pip install -r requirements.txt
  ```

## Running the web scraping
* Execute the main file as follows:

  ```bash
  python wikiscraper.py
  ```
