## Ideas worth noting on modifying the GeneNetwork Uploader (Originally written by Fred) 

### After going through the uploader repo, perusing and studying each each of the files in the directories, the following are a few suggestions I would have added from what I understood so far on the functionality of this Uploader 

### User Options
#### 01 File format 
- The expected file format for this uploader to accept a file is TSV (Tab Separated Format). So, wouldn't it be wise to add an option for the user to be able to convert the file format into a TSV format?
- In this way, the uploader accepts TSV files and also provides an option to convert any other file into the TSV format 
##### How to go about this:
- I would use the available libraries written in Python, specifically for file format conversion, or even write a custom Python script (APIs) to meet the functionality needs.

#### 02 Modify file contents 
In addition to the specific requirements, which were highlighted in the Uploader brief description, I would also add the option for the user to be able to modify the file content, in this case, filling the empty cells, 
modify the spurious values in the cells as well as decimal values as required by the uploader. However, the challenge to this would be to ensure that the modified data is not corrupted by the user.

### Rewriting the whole uploader in Rust or integrating rust functionality with the Uploader 
I thought of this idea due to the following reasons:
  - Rust, being one of the most widely used general-purpose programming languages, has several advantages over Python.
     - Error handling;
        - Python usually throws exceptions and errors during runtime, which, in one way or another, affects the general performance in terms of speed and completion. On the other hand, 
          Rust checks for errors during compile time, not runtime. In addition, it returns a value and suggests for possible ways to solve the error(s)
     - User base scalability;
        - With most web development projects, scability is one of the important factors to put into consideration. Python is not well designed for program scalability. However, there are embedded features
          related to infrastucture scaling (horizonral or verical scaling), but this comes with a lot of production costs. On the other hand, Rust is designed of high system performance, as it contains most
          system based features found in C++, which is one of the well known low level programming languages used in systems development, therefore it is much easier to build scalable web services with Rust.

     - Higher speed of execution in Rust
        - The speed of execution is reflected by level of performance a particular language has. Due to the fact that python uses an interpreter to convert its code to the machine code, and inefficient
          memory management (handling garbage collection which is the automatic memory management) during runtime, makes it relatively low in performance.
        - Rust on the other hand, does not perform garbage collection during runtime, and the its code is directly compiled in machine code, therefore making it an inherently high-performance language
   
  So, I would not say that rust is all perfect of a language as compared to python, but I think integrating some features in Rust to a web application built in python, such as in this case, Fred's 
  uploader, would greatly improve the performance and scalability of the uploader, especially due to the growing number of our users, companies and their needs expected in the web service app. 


### Few questions I had from going through Fred's Uploader Web service
- I still did not fully understand the general aspect as to why we focus on the average files and standard error files?
- I also would like to understand more on the guix package as used in the context of this project? 


