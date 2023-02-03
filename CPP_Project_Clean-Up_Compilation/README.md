### C++ Project Clean-Up and Compilation

### Introduction

Task: 

  * The Python `main.py` script searchs through the `src` directory for subdirectories called `calculator_test` and `multiply`.
  * Once these have been found, a new directory called `target` (or whatver you want to call it.
  * The new sub-directories now have the names `calculator` and `multiply`.
  * Inside these new sub-directories C++ files are compilied and readuy to be run.

### Requirements

  * Tested on `Ubuntu 20.04`.
  * `Python 3.8.10`.
  * Compiler: `g++ 9.4.0`.
  * Text Editor: Any will do. This project was develped using `Sublime Text`.

### Initial Project Structure

    src/
    
        calculator_test/
        
            calc.cpp
            
        multiply_test/
        
            calc_2.cpp
             
     main.py
     test.py
     README.md
     
     
### Final Project Structure (No C++ File Compilation yet)

      src/
      
          calculator_test/
          
              calc.cpp
                
          multiply_test/
          
              calc_2.cpp
               
       main.py
       test.py
       README.md
       
       target/
       
           calculator/
           
               calc.cpp
               calc
               
           multiply/
           
               calc_2.cpp
               calc_2
               
         
### Running the Application

  * `$ git clone https://github.com/MRLintern/Automation_Administration/CPP_Project_Clean-Up_Compilation.git`
  * `$ python3 main.py src target`
  * Note: for the test case, replace `main.py` with `test.py`

### Testing and TODO

The process of compiling the C++ files is yet to be achived. With this in mind, a script called `test.py` has been developed to create the `target`
directory and sub-directories. That is, changing the names of the sub-directories. However, `main.py` is included. 
                  
                


