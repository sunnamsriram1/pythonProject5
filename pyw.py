# importing the module
import pywhatkit as kit

# using Exception Handling to avoid
# unprecedented errors
try:

# sending message to receiver
# using pywhatkit
pywhatkit.sendwhatmsg("+918688655324","Hello from GeeksforGeeks",22, 28)
print("Successfully Sent!")

except:

# handling exception
# and printing error message
print("An Unexpected Error!")
