1.	Enable less secure app with below link
https://www.google.com/settings/security/lesssecureapps

2.	Disable captcha
https://accounts.google.com/DisplayUnlockCaptcha
 
Click continue button

3. Place xls file with below format
eg.
email,name, subject, marks, total
xyz@gmail.com,first last name, English, 9,10

4. execute the script
python3 mail.py -f xls_file_name -u email_address -p passmepass
