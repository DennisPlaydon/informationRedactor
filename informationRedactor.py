#! python3
# informationRedactor.py - Finds phone numbers and email addresses on the clipboard

import pyperclip, re

redactRegex = re.compile(r'''(
    \d{4}
    (\s | -)?
    \d{4}
    (\s | -)?
    \d{4}
    (\s | -)?
    \d{4}
    )''', re.VERBOSE)
    
#text = '1111222233334444 yup yup yup 1234123412341234'

text = str(pyperclip.paste())

matches = []
for groups in redactRegex.findall(text):
    last_four = groups[0][-4:]
    matches.append('{0} {1} {2} {3}'.format('*'*4, '*'*4, '*'*4, last_four))
        
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No credit card numbers found.')


