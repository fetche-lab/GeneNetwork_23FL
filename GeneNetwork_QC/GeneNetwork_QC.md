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
### The followng is the link to the repository containing the source code and test files of the app 
` https://gitlab.com/fredmanglis/gnqc_py `
### This app runs as a `command line interface (CLI)` and as a `web app`, under `flask` application, a pyhon framework used for web development 

### The `etc/` directory contains configuration files for system-wide settings and parameters 

### The 'qc_app/` directory contains 2 subdirectories and 7 python modules 
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

### 
