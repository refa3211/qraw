import win32com.client

outlook = win32com.client.Dispatch("outlook.application")
# olmailitem = 0x0  # size of the new email
mail = outlook.CreateItem(0x0)
mail.Subject = 'testsubject'
mail.To = 'refa3211@gmail.com'
mail.CC = 'refa3211@gmail.com'
mail.Body = 'Hello, this is a test email to showcase how to send emails from Python and Outlook.'
# attach='C:\\Users\\admin\\Desktop\\Python\\Sample.xlsx'
# newmail.Attachments.Add(attach)
# To display the mail before sending it
mail.Display()
mail.Send()
