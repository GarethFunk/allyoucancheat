"""
Master file for running the entire project
"""

# Read in file
f = open('input/it_essay.txt', mode='r')
essay = f.read()
f.close()
# Split into sentences
sentences = essay.split('.')

