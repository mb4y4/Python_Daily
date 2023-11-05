#file manipulation(creating as 'w', writting and appending)

# sample_emails = [
#     'john.doe@example.com',
#     'jane.smith@example.com',
#     'bob.johnson@example.com',
#     'alice.wilson@example.com',
# ]

# # Create the 'emails.txt' file and populate it with sample email addresses

# with open('ourmails.txt', 'w') as emails_file:
#     for email in sample_emails:
#         emails_file.write(email + '\n')

# #dispay written results on terminal

# with open('ourmails.txt', 'r') as emails:
#     results = emails.read()
    
#     print(results)

# create a new txt file(emails.txt) to perform different operations on

# with open('emails.txt', 'w') as emails_file:
#     emails_file.write('for trial'+ '\n')

with open('emails.txt', 'r') as emails:
    results = emails.read()

email_list = results.split('\n')  # Assuming each email is on a separate line
print(email_list)

search_email = 'd.sommy@gmail.com'  # Replace with the email you want to search for
if search_email in results:
    print(f"The email '{search_email}' was found in the file.")
else:
    print(f"The email '{search_email}' was not found in the file.")

splitted = results.split()
target = 'd.sommy@gmail.com'
for i in range(len(splitted)):
     if splitted[i] == target:
        print(target, "Found at index", i + 1)
        break

# count number of emails
mail_list = results.split('\n')  # Split the content into a list of emails
email_count = len(email_list)
print(f"Number of email addresses: {email_count}")

#Process the email addresses in some way (e.g., extract domains):
email_list = results.split('\n')  # Split the content into a list of emails

# Extract email domains, handling potential format issues
email_domains = []
for email in email_list:
    if '@' in email:
        email_domain = email.split('@')[1]
        email_domains.append(email_domain)
    else:
        print(f"Invalid email format: {email}")

print(email_domains)

# Write the email addresses to a new file:
email_list = results.split('\n')  # Split the content into a list of emails

# Write the email addresses to a new file
with open('clean_emails.txt', 'w') as clean_emails:
    for email in email_list:
        clean_emails.write(email + '\n')