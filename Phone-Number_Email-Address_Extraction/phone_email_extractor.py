
#!/usr/bin/python

import pyperclip, re

#create a Regex for phone numbers

phoneRegex = re.compile(r'''(

	(\d{3}|\(\d{3}\))?               #area code
	(\s|-|\.)?						 #separator
	(\d{3})							 #1st 3 digits
	(\s|-|\.)						 #separator
	(\d{4})							 #last 4 digits
	(\s*(ext|x|ext.)\s*(\d{2,5}))?   #extension
	)''',re.VERBOSE)

#create a Regex for email addresses

emailRegex = re.compile(r'''(

	[a-zA-Z0-9._%+-]+		#username; any characters
	@						# @ symbol
	[a-zA-Z0-9.-]+			#domain name
	(\.[a-zA-Z]{2,4})
	)''', re.VERBOSE)



#find matches in clipboard text

#Note: group 0 matches the entire regular expression

text = str(pyperclip.paste())

matches = [] #store all matches found

"""

create a variable which consists of the different groups of the matched text.

Note: phone regex

group[1] = area code
group[3] = first 3 digits
group[5] = last 4 digits
group[8] = last 4 digits


"""

for groups in phoneRegex.findall(text):

	phoneNum = '-'.join([groups[1], groups[3], groups[5]])

	if groups[8] != '':

		phoneNum += ' x' + groups[8]

	matches.append(phoneNum)

#group 0 is appended to each match
for groups in emailRegex.findall(text):

	matches.append(groups[0])


#copy results to the clipboard
if len(matches) > 0:

	pyperclip.copy('\n'.join(matches))

	print('Copied to clipboard:')
	print('\n'.join(matches))

else:

	print('No phone numbers or email addresses found.')


