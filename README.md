# iOS Restriction Passcode Brute Force [![Codacy Badge](https://api.codacy.com/project/badge/Grade/5c343edc44b8436588b1a2fc153a98d4)](https://www.codacy.com/app/thehappydinoa/iOS-Restriction-Crack?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=thehappydinoa/iOS-Restriction-Crack&amp;utm_campaign=Badge_Grade) [![Codacy Badge](https://api.codacy.com/project/badge/Coverage/5c343edc44b8436588b1a2fc153a98d4)](https://www.codacy.com/app/thehappydinoa/iOS-Restriction-Crack?utm_source=github.com&utm_medium=referral&utm_content=thehappydinoa/iOS-Restriction-Crack&utm_campaign=Badge_Coverage)


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

## DEPENDENCIES

This has been tested with Python 2.6 and 2.7.

## LICENSE

MIT License
