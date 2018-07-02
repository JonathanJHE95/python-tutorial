############################
### Expresiones Regulares ##
############################
# \d - Salto de linea
# \s - Espacio
# \t - Tabulador
# \e - Escape
# \r - carriage return
# \f - form feed

import re

xx = 'Jonathan, deep learning'
r1 = re.findall(r'^\w+',xx)
print(r1)

print((re.split(r'\s','we are split this words')))
print((re.split(r's','split the words')))

############## MATCH

fruta = ["gera gero", "ganzana ganzo", "guva givo", "gimon gamon"]

for element in fruta:
    z = re.match('(g\w+)\W(g\w+)', element)

    if z:
        print((z.groups()))

############## SEARCH

patterns = ['software testing', 'guru99']
text = 'software testing is fun'

for patter in patterns:
    print('Looking for "%s" in "%s" ->' % (patter, text), end=' ')

    if re.search(patter, text):
        print('found a match')
    else:
        print('no match')

############## FINDALL

abc = 'guru99@google.com, careerguru99@hotmail.com, users@yahoomail.com'

emails = re.findall(r'[\w\.-]+@[\w\.-]+', abc)

for email in emails:
    print(email)

############## FLAGS

# Syntax for Regex Flags	What does this flag do
# [re.M]	Make begin/end consider each line - Multiline Flags
# [re.I]	It ignores case
# [re.S]	Make [ . ]
# [re.U]	Make { \w,\W,\b,\B} follows Unicode rules
# [re.L]	Make {\w,\W,\b,\B} follow locale
# [re.X]	Allow comment in Regex

xx = '''guru99
careerguru99
selenium'''

k1 = re.findall(r'^\w', xx)
k2 = re.findall(r'^\w', xx, re.MULTILINE)

print(k1)
print(k2)








