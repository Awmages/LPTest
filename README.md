# LPTest
The LPTest project is an example of what Junior Software Engineers are expected to achieve in order to be considered for employment at LP Technologies.

main.py queries a MySQL database, retrieves a BLOB of hex values, converts to signed decimal, then graphing the data in a plot similar to a spectrum analyzer screen.  main.py is also designed to loop continually, and as such the connection is not closed until the program is terminated.

## Getting Started
The readme is written for Windows OS, adjust for Linux where necessary.


### Requirements
main.py was written in Python 3.6, and has the following dependecies:

|Package|Description|Version|Install|
|-----|-----|-----|-----|
|matplotlib|Graphing library|3.0.3|pip install matplotlib|
|mysql-connector|Python's MySQL driver to access MySQL database|2.1.6|pip install mysql-connector|

### Installing
Included in the project is a pip freeze of the needed libraries.
To install requirements using pip freeze
`````
1. Open Command Line
2. cd to where LPTest project is cloned
3. Enter "pip install -r lptest_pip_freeze.txt
`````
### Database Credentials
Database credentials are found starting on line 5 under the config variable

|Variable|Default|
|-----|-----|
|user|"root"|
|password|"lptech"|
|host|"127.0.0.1"|
|database|"test"|


## Execution
To run main.py enter
`````
python main.py
`````
