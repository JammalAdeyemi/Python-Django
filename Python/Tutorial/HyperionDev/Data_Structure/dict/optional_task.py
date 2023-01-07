# You are going to write a program that will give you the meaning of a given abbreviation.

# Create a dictionary that contains some abbreviations and their meanings. Let the abbreviation be the key and the meaning of the abbreviation be the value (e.g. ADSL: Asymmetric Digital Subscriber Line).
abbreviations = {
    'ADSL': 'Asymmetric Digital Subscriber Line',
    'CD': 'Compact Disc',
    'DVD': 'Digital Versatile Disc',
    'FTP': 'File Transfer Protocol',
    'IDE': 'Integrated Development Environment'}

# After you have created your dictionary, add 2 more abbreviations and their meanings to it.
updated_abbreviations = abbreviations.update({'CPU': 'Central Processing Unit', 'RAM': 'Random Access Memory'})

# Now ask the user to enter an abbreviation and check if that abbreviation is in your dictionary.
user = input('Enter an abbreviation: ')
# If it is, print out the abbreviation and its meaning.
if user in abbreviations:
    print(abbreviations[user])
# If it is not in the dictionary, print out "Abbreviation not found"
else:
    print('Abbreviation not found')