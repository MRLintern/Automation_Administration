### Testing the Application: No C++ Compilation

This part of the project looks at simply changing the folder name where the C++ source files exist and generating a json metadata file
which will tell us the name of the new folder and the number of folders that have been changed.

### Project Structure (Initial)

        main_folder.py
        
        src/
        
            calc_app/
            
                calc.cpp
                calc.hpp
                
                
### Project Structure (After)
   
   
         main_folder.py
        
         src/
        
             calc_app/
            
                calc.cpp
                calc.hpp
                
          target/
          
              calc/
              
                 calc.cpp
                 calc.hpp
                 
              metadata.json
              
          
### Running the Application

`$ python3 main_folder.py src target`
              
              
             
   
   
          `
                
                
