import re

email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}" 
phone_number_pattern = r"\+234 \d{3} \d{3} \d{4}"
    
with open("review.txt", "r") as f:
    content = f.read()
    emails = re.findall(email_pattern, content)
    
    with open("emails.txt", "w") as f:
            f.write("\n".join(emails))

    phone_number = re.findall(phone_number_pattern, content)
    with open("phone_number.txt", "w") as f:
            f.write("\n".join(phone_number))


with open("emails.txt", "r") as f:
        content = f.read()
        print(content)