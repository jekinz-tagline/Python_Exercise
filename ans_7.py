import re

emails = ['abc@gmail.com', '123$tt*@xyz.com', 'good@bad@uk.in', 'nasa@usa12.space', 'no-reply@domain.in', 'ramhanuman@saketa.lok', 'ruhi.mohan@exter123.123', 'fake@fake123.fakercom']

regex = r'\b[a-zA-Z0-9-_]+@+[a-zA-Z0-9]+\.+[a-zA-Z]{2,3}\b'

output_emails = []

for email in emails:
    if re.fullmatch(regex,email):
        output_emails.append(email)

print(output_emails)