email = input("Enter your company email: ")

if email.endswith("@company.com"):
    if email.startswith("admin"):
        print("Admin email detected!")
    else:
        print("Valid company email")
else:
    print("External email detected!")

file_name = input("Enter file name: ")

if file_name.endswith((".pdf", ".docx")):
    print("Document accepted")
else:
    print("Unsupported file format")
