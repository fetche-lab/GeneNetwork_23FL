## QUALITY CONTROL OF FILE UPLOADS AND DATA IN GENENETWORK QC APP 

## The following documentation provides the overview of the qc app used in GeneNetwork to inspect the kinds of data uploaded and stored. 

### In summary, the following are the requirements considered:
```markdown 
1 File format - tab separated (TSV)

2 Data values

  - no empty cells

  - the average files (to have exactly 3 decimal values) and standard error files (to have three to six decimal values),

    and both values to the right hand side, and a number to the left side of the dot

  - The line endings to be in Unix type and not DOS

  - The headers to match trusted sources
```
### The following is the link to the repository containing the source code and test files of the app 
` https://gitlab.com/fredmanglis/gnqc_py `
### This app runs as a `command line interface (CLI)` and as a `web app`, under `flask` application, a pyhon framework used for web development 

### The `etc/` directory contains configuration files for system-wide settings and parameters 

### The `qc_app/` directory contains 2 subdirectories and 7 python modules 
```markdown
1 static/ and templates/ - Frontend and web server access for the user (user - client architecture), / {js and css}
2 python modules;

 - In summary, these modules do the following:

    - Provide entry point for web application to run on flask framework (_init_.py)

    - Ensures secure connection of the app to the database server (MySQL) and Redis server by providing right access to them (check_connection.py, db_utils.py)

    - Ability to retrieve information from the database and handle file uploads to the qc app via flask (dbinsert.py, entry.py)

    - Handling the background processing of the app, ensuring no interference with program execution (jobs.py)

    - Handling the uploaded data, converting the dataset into a format that can be manipulated by the app, (such as to inpect the synthax and the necessary quality checks required) (parsing.py)
```

### After the files are uploaded, the processing of testing and checking for the validity and correctness of the data begins. The `quality_control` directory contains Python code for this functionality 

 ```markdown
 1 __init__.py 
 This module contains a string of a brief description of the data curation process in the uploaded files
```
```markdown 
 2 average.py
 This Python script checks for data validity and error handling in uploaded average files.

 - 3 Python modules imported (typing,.utils,.errors), with utils and errors found within the program

    - Union class from `typing` module provides type hints for the function `invalid_value` which takes 3 arguments; {line_number(int), column_number(int), val(string)}

 - Ideally, the function returns `InvalidValue` (from `.errors` module) if any of the arguments are not as defined, and `None` if they are valid, as defined by "Union[InvalidValue, None]"

 - And if the values do not adhere to the provided regex {r"^([0-9]+\.[0-9]{3}|[0-9]+\.?0*)$"}, cell_error class from `.utils` module returns an error message, which explains the expected format to be

   numbers with exactly three decimal places to the right, as well as at least one number to the left of the integer value. 
```

```markdown
3 errors.py
This Python script provides a structured way of storing and accessing information about errors that occur during quality control checks

- imports `namedtuple` function from `collections` module

  - namedtuple creates a subclass of tuples with named files, in this case 3 (`InvalidValue`, `DuplicateHeading`, and

   `InconsistentColumns`), and they store information about the specific types of errors that can occur during QC checks

    - `InvalidValue` stores information about a value that is invalid, in this case (line number, column number, value and error message)

    - `DuplicateHeading` stores information about the duplicated heading in the file's (line number, column number, value and error

       message)

    - `InconsistentColumns` stores information about the inconsistent columns, including (line numbers, header count, contents count, and

       error message)
```

```markdown
4 file_utils.py 
This Python script provides access to necessary tools to open files (in this case zipped files and those in tsv format)

 - It consists of a function called `open_file` which checks for zipped files to decompress, before opening them; otherwise, it continues to open the file

   - Uses `is_zipfile` to check if the file is zipped, and `ZipFile` to open the zipped file: both from `zipfile` module

   - Uses `Union` from `typing` module and `Path` from `pathlib` module to indicate the filepath to contain string and the path as identified by the python function to navigate and open files in

     specified location

```

```markdown
5 headers.py
This Python script validates the column headers of the data in the upload files

- There are three functions defined; `invalid_header`, `invalid_headings`, and `duplicate_headings`

- The `invalid_header` function ensures the headers are a sequence of strings and returns InvalidValue or None (using `Sequence` and `Union` classes from `typing` module). If the number of columns in

  headers is less than two, it returns an error message

- The `invalid_headings` function ensures the first column contains line numbers (integers), then inspects each of the columns to see if the headers are valid; otherwise, it returns error message

- The `duplicate_headings` function checks for the column headers that have been replicated, then uses the `reduce` function from the `functiontools` module to deal with the duplication

- The `InvalidValue` and `DuplicateHeadings` tuples return error messages and they are imported from `quality_control.errors` module, which is custom made as part of this application 

```
```markdown
6 standard_errors.py
  This Python script inspects the values in the standard error files

  - Checks for the line number and column numbers to be integers, then values to be strings. Uses `Union` class from `typing` module to return InvalidValue for errors or None for no errors

  - Then, it checks for the number of decimal values to be at least six. Returns the `cell_error` function from `.errors` custom module, indicating the values to be at least six, as reflected by the

following regex ( r"^([0-9]+\.[0-9]{6,}|[0-9]+\.?0*)$") 
```
```markdown
7 parsing.py
This Python script provides tools and functions to parse uploaded files (converting data in files from one format to another). Ideally,

it goes through each of the uploaded file and inspects if the data is valid and correct

- The following modules are used in this python script

  - `colletions` module for data collections
  - `Enum` from `enum` module for creating an enumeration class
  - `partial` from `functools` module for partial function application (useful in function simplification)
  - `Tuple`, `Union`, `Iterable`, `Generator`, `Callable`, `Optional` from `typing` module, for type hints (usually for annotation   
     purposes and static programming, providing what type of values to work with)
  - `average`, `file_utils`, `standard_error`, `errors`, and `headers` from quality_control module, which is custom to the project. 
  -  An enumeration class called FileType is created with `AVERAGE` and `STANDARD_ERROR` (this helps simplify the representation of the 
     filetype to be handled in this code)

- The Functions and their purpose in this script;

  - `strain_names(filepath)`; This function retrieves strain names from a given file
  - `headers_errors(line_number, fields, strains)`; This function collects errors related to the header rows of a file
  - `empty_value(line_number, column_number, value)`; This function for an empty field value in a line
  - `average_errors(line_number, fields)`; This function collects errors for a line in a file of averages
  - `se_errors(line_number, fields)`; This function collects errors for a line in a file of standard errors
  - `make_column_consistency_checker(header_row)`; A function that builds a function, `__checker__(line_number, contents_row)`, to   
     check for column consistency based on the header 
  - `collect_errors(filepath, filetype, strains, update_progress, user_aborted)`; This function runs checks against an uploaded file 
     and collects all the errors as indicated in the arguments, as a generator
    - The arguments;
      - `filepath`; path of the file to be processed
      - `filetype`; type of the file to be processed (`FileType.AVERAGE` or `FileType.STANDARD_ERROR`)
      - `strains`; a list of strains
      - `update_progress`; a function to update progress (optional)
      - `user_aborted`; a function to check if the user has aborted the process
    - How it operates;
      - Opens the file, goes through the lines, and processes them based on their line numbers and file type
      - Then calls appropriate error checkers(`__process_errors__`) for header validation, column consistency, and error accumulation
      - If an error is found, it yields error, and also, updates progress if `update_progress` is provided

  - `take(iterable, num)`; This function takes at most `num` items from an iterable and returns a list

```
```markdown
8 utils.py
This python code mainly deals with calculating and tracking progress and handling cell errors when the application is examining the quality of the data in uploaded files 
```
