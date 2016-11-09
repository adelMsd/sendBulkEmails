This python script used to send any number of emails using gmail account with activated feature, check this link to activate it: https://www.google.com/settings/security/lesssecureapps

It is very easy to send emails using this,

1- create a txt file that contains a list of emails you want to email, line by line.

2- I you want to attach a file then put in the same folder.(for multiple files try to compress them, since the script accepts just one file) 

3- Edit the Subject and the Text(body of msg) to what ever you want in sendMSG-v-2.0.py

4- excute the script by running:

        I- Without attached files:

            -$ python sendMsg-v-2.0.py YourEmailAddress@gmail.com emails_list.txt 

        II- with attaching a file:
            
            -$ python sendMsg-v-2.0.py YourEmailAddress@gmail.com emails_list.txt filenameOfTheattached(CV.pdf)



PS: for other email servers you need to get their smtp server, like smtp.live.com for hotmail email accounts and change it in the python file.


I hope you use it for good purposes ;)
