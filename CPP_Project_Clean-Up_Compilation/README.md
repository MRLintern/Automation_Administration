### C++ Project Clean-Up and Compilation
---

Note: Please refer to the `testing` folder where the application was tested to ensure the folder name was changed and a json metadata file was generated.

Note: `C++_Compilation_Scipt.py` will compile the `calc.cpp` and produce an executable. However, a warning is produced by the shell telling the user that `calc` can't be found.

### Introduction
---

Task: 

  * The Python `main.py` script searchs through the `src` directory for subdirectories called `calc_app`.
  * Once this folder has been found, a new directory called `target` (or whatver you want to call it) is generated.
  * The new sub-directory of `target` is called `calc`.
  * Inside this sub-directory, a `C++` executable is generated which can be run at the command line.

### Requirements
---

  * Tested on `Ubuntu 20.04`.
  * `Python 3.8.10`.
  * Compiler: `g++ 9.4.0`.
  * Text Editor: Any will do. This project was develped using `Sublime Text`.

### Initial Project Structure
---

    src/
    
        calc_app/
        
            calc.cpp
            calc.hpp
            
     main.py
     test.py
     README.md
     
     
### Final Project Structure
---

      src/
      
          calc_app/
          
              calc.cpp
              calc.hpp
                     
       main.py
       README.md
       
       target/
       
           calc/
           
               calc.cpp
               calc.hpp
               calc
               
           metadata.json
                    
### Running the Application
---

  * `$ git clone https://github.com/MRLintern/Automation_Administration/CPP_Project_Clean-Up_Compilation.git`
  * This will download all projects within the `Automation_Administration` repo.
  * `$ cd CPP_Project_Clean-Up_Compilation`
  * `$ python3 main.py src target`
  
### TODO
---

As stated at the start, refer to the `testing` folder to run the application which will change the folder name and produce a metadata.json file.
The script will have to be develped to allow for compiling the `C++` file, `calc.cpp`. 
---
                


