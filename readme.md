This is Gmail bruteforce program.

BRUTEFORCE is a hacking technique where hacker use a list of different passwords to try to log into a system.

Before running the program successfully, please read the instruction carefully.

Instruction:
    . Make sure you have installed python in your pc.
    . For better experience, I recommend you to use visual code editor to clone and run the program.
    . In password_generator.py:
        + line 3: set the minimun length of your password
        + line 4: set the maximum length of your password
        + line 6: input any information about your password. Example:
                    - character = "hello" , it will start to shuffle the word hello and get "hello, elloh, llohe, lohel, ..."
                    - character = ["hello", "apple", "1"] , it will shuffle these words and get "helloapple1, applehello1, ..."
                    * Note: the way it shuffles depends on the max and min that u set above 
        + line 11: input a path for your password list into the syntax. Sample:
                    - file_open = open("C:/Password_list.txt', 'w')
                    * Note: You should name your password file without any space or number, it might error the program.
        * Then run password_generator.py
        * If you follow the steps correctly, you now should have a password list in form of txt file, which we will use it to bruteforce a gmail account
    . In bruteForce_Gmail.py:
        + open a new terminal then type: pip install goto-statement
        + line 5: input your target. Sample:
            - target = "fakehacker@gmail.com"
        + line 6: input the path to your password list. Sample:
            - passlist = "C:/Password_list.txt"
        * Then run the bruteForce_Gmail.py

**Note: Use this at your own risk.
References:
    . https://www.youtube.com/watch?v=omHZtBbc0Hc&t=25s
    . https://www.youtube.com/watch?v=k2BkdnlHnII&t=166s
