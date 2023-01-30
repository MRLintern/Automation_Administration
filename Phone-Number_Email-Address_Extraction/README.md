
### Project: phone number and email address extractor

Script looks through a long document or web page for a phone number or email address.
you won't be using CTRL+F.

script requires the `pyperclip.py` module for copy/paste strings

### More Detail

1. use pyperclip module to copy and paste strings; you need to install this module
2. create 2 regexes, 1 for matching phone numbers and 1 for email addresses
3. find all matches for both regexes
4. neatly format the matched strings into a single string to paste
5. display some kind of message if no matches were found in the text

### Requirements

Application tested on `Windows 10` and `Ubuntu 20.04`.
'Python 3.8`.
A text editor. `Sublime Text` was used. An IDE can also be used too.
`pyperclip` module for copy/paste functionality.

### Running the application

`$ git clone https://github.com/MRLintern/Automation_Administration/edit/main/Phone-Number_Email-Address_Extraction.git`
Go to a web page with phone numbers (US) and email addresses.
Press CTRL+A & CTRL+C.
`$ python3 phone_email_extractor.py`
