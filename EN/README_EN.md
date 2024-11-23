# LogsColor
**Logscolor** is a lightweight and easy-to-use open-source library for creating logs with customizable colors in Python. Ideal for developers looking to simplify tracking and debugging in their projects.
- Colored log messages.
- Different log levels (`INFO`, `WARNING`, `ERROR`, `TRACE`).
- Optional: Display the line of code where the message was generated.

## Installation
To install `logscolor`, simply run the following command:

```bash
pip install logscolor
```
Then, in your project, import the logging functions:
```python
from logscolor.logscl import info, error, trace, warning, infoL, errorL, traceL, warningL
```
With this, you'll be able to use the different logging levels in your code.

## Basic Usage
Import SimpleLogs into your project:
```python
from logscolor.logscl import info, warning, error, trace

info("Information message")
warning("Warning message")
error("Error message")
trace("Debug message")
```

If you want to include information about the line where the message was generated, use the functions with the L suffix:

```python
from simpleLogs import infoL, warningL, errorL, traceL

infoL("Information with line number")
```

## Features
- Customizable colors: Each log level has a unique color for easier visual identification.
- Enriched format: Displays the date, time, and optionally the line of origin.
- Lightweight and easy to integrate: Ideal for both large and small projects.
- Support for advanced levels: Includes traceability (trace) for detailed debugging.
- Easy integration: Designed to be a quick and simple replacement for print().

## Supported Log Levels
SimpleLogs supports the following log levels, each with custom colors for better visibility:

| Level      | Description                              | Variants               |
|------------|------------------------------------------|-------------------------|
| **INFO**   | Informational messages.                  | `info`, `infoL`         |
| **WARNING**| Warnings about potential issues.   | `warning`, `warningL`   |
| **ERROR**  | Critical error messages.             | `error`, `errorL`       |
| **TRACE**  | Detailed debugging messages.      | `trace`, `traceL`       |

## Images
![alt text](/examples/example_terminal.png)

### Real Examples
![alt text](/examples/real_ex.png)

## Requirements
- Python 3.7 or higher
- colorama

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Contact
Created by Pablo Vega Castro. If you have any questions or suggestions, feel free to contact me at pablovegac.93@gmail.com.