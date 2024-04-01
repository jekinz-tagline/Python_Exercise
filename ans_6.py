import re

string = "PQRQRQRQ"
sub_str = "QRQ"

length = len(re.findall(f'(?=({sub_str}))',string))
print(length)