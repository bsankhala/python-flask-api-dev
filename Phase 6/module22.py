import re

# text = "You can reach me at 123-456-7890 or my office at 987-654-3210. In case of emergency, call 555-555-5555."

# pattern = r"\d{3}-\d{3}-\d{4}"
# result= re.findall(pattern,text)

# print("The found numbers are: ")
# for num in result:
#     print(num)


text = """
Hello   user_01!!!

My primary email is   sample.user_99@gmail.com and my backup is support_team@company.org.
You can also contact admin_123@service.co.in   for technical issues.

For urgent matters, call me at 123-456-7890 or my manager at 987-654-3210.
If those fail, try the old office line: 555-666-7777.

Hi   again!!!
Please   do not   hesitate   to   contact   us.
Thank    you!!!
"""

greeting_match = re.match(r"^(Hello|Hi)", text.strip())
if greeting_match:
    print("Text starts with a greeting:", greeting_match.group())

emails = re.findall(r"\b[\w._%+-]+@[\w.-]+\.[a-zA-Z]{2,}\b", text)
print("\nEmails found:")
for email in emails:
    print(email)

phone_numbers = re.findall(r"\d{3}-\d{3}-\d{4}", text)
print("\nPhone numbers found:")
for number in phone_numbers:
    print(number)

usernames = re.findall(r"\b\w+\b", text)
print("\nUsernames/words found:")
print(usernames)

clean_text = re.sub(r"\s+", " ", text)
print("\nCleaned text with single spaces:")
print(clean_text)
