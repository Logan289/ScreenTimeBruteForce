# iOS Restriction Passcode Crack [![Codacy Badge](https://api.codacy.com/project/badge/Grade/017319df2b8d4a588c0c92d5730b7811)](https://www.codacy.com/app/thehappydinoa/ios_Restriction_PassCode_Crack---Python-version?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=thehappydinoa/ios_Restriction_PassCode_Crack---Python-version&amp;utm_campaign=Badge_Grade)


## Overview 

This version of the application is written with Python programming language,which is used to crack the Restriction PassCode of iphone/ipad.

### Brute Force

1. Get the Base64 key and salt from the backup file in Computer.

2. Decode the Base64 key and salt.

3. Try from 1 to 9999 to with the pbkdf2-hmac-sha1 hash with passlib
(passlib moudle need to be installed before:easy_install passlib)


### How to Use
1. Make sure to use Itunes to back up the ios device to Computer

2. Run ioscrack.py
```python 
python ioscrack.py
```

### Source Code
```python
  ioscrack.py : main process
```
