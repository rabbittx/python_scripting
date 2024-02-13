[read in persian](README.en.md)
<div dir='ltr'>

# GoogleSearch Scraper

## Description
This project is a Python script that uses Google to search for keywords and saves the results in a CSV file. For each search key, it extracts and stores relevant results from the Google Search Engine Results Page (SERP). With this tool, you can easily find Google's suggested keys for your own keywords.

## Features
- Uses a random User-Agent for requests
- Reads search keys from a text file
- Saves search results in a CSV file with two columns: `search key` and `result`
- Manages errors and logging

## Requirements
To run this script, you need to install the following libraries:
- requests
- beautifulsoup4
- fake-useragent

You can install all requirements by running the following command:

```bash
pip install -r requirements.txt
```
## Usage
To run the script, first prepare your input file containing the search keys. Remember to write each key you're interested in on a new line. Then, execute the script by specifying the path to the input file and the CSV output file from the command line:

```bash 
python google_offer_keys.py --input your_input_file.txt --output results.csv
```
## Configuration
You can configure the script settings by changing the command line arguments. The input file should be a text file with search keys separated by lines.

## Contribution
Contributions to improve this script are welcome. Please create a Pull Request to submit your changes.
</div>
