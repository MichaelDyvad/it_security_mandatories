# Find out how to fix/mitigate the command injection vulnerability we saw in class and modify the Python script nslookup.py accordingly.
# Explain what change(s) you did to the code and why is that addressing the vulnerability.

import subprocess

input = input("Enter the domain name: ")

approved_domains = (".dk", ".com", ".org")
approved_www = ("www.")
blacklist_symbols = [";", "&", "<", ">", "'"] 

#Checks for the symbols if they appear terminate
for symbols in blacklist_symbols:
        if symbols in input:
            print("Symbols not allowed")
            quit()

if input.endswith(approved_domains) & input.startswith(approved_www):
    command = "nslookup {}".format(input)
    response = subprocess.check_output(command, shell=True, encoding="UTF-8")
    print(response)
else:
    print("Error - not allowed")