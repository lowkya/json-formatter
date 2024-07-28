# JSON Formatter V1

## Overview

Welcome to the JSON Formatter project! This tool is designed to convert JSON strings into a well-formatted, human-readable format. It handles various JSON structures, including nested dictionaries and lists, and provides clear and organized output.

## Features

- **Readable Output**: Formats JSON data with proper indentation and structure.
- **Handles Nested Structures**: Supports nested dictionaries and lists for comprehensive formatting.
- **Error Handling**: Provides basic error handling for invalid JSON input.

## Getting Started

To use the JSON Formatter, follow these steps:

1. **Clone the Repository**
   ```
   git clone https://github.com/yourusername/json-formatter.git
   ```
2. **Navigate to the Project Directory**
   ```
   cd json-formatter
   ```
4. Install Dependencies
   This project requires Python 3.8 or later. No additional dependencies are required.
5. Run the Formatter
   You can run the formatter script directly:
   ```
   python main.py
   ```
You’ll be prompted to enter a JSON string to parse. The formatted output will be displayed in the console.

## Usage

Here’s a brief overview of how the formatter works:

Input: A JSON string entered by the user.
Processing: The formatter parses and formats the JSON string.
Output: The formatted JSON is displayed with proper indentation.

## Example
```{"key1": true,"key2": false,"key3": null,"key4": "value","key5": 101}```

```
{
 key1 : True
 key2 : False
 key3 : None
 key4 : value
 key5 : 101
}
```

