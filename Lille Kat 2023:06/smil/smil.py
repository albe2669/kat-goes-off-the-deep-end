import re

for match in re.finditer(r'[:;]-?\)', input()):
    print(match.start())
