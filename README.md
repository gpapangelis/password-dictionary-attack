# password-dictionary-attack


In order to execute the specific project you have to run the scripts in specific order.

First, hashing.py is reading the username and the password from the console. The file users.txt contain some users so you can run only the second script.
```
 python hasing.py -i users.txt
```

The second script cracks the password, for each user from a specific file by comparing them with a known password list.
```
 python get_pass.py -i users.txt -p passwords_list.txt
 ```
