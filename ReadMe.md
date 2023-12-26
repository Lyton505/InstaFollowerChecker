## Why

When my account was still set to a public account, a stream of bot and scamming accounts 
followed me so that they could send me links to malicious links since only my followers can 
send me messages. I noticed however that I never followed these accounts back; hence I can 
easily identify them by checking which accounts I do not follow back. **This program gives you 
a list of accounts that follow you but you don't follow them back**

## What you need

- two files that you would've downloaded from your account profile(go to Accounts center in 
  Settings -> Your info and permission -> Download info --- download as json)
  - unzip and look for the files: followers_1.json, and following.json
- python3

### Expected format - Python

1. followers_1.json
   - list of dictionaries
   - each dictionary contains 3 keys, one of which is _string_list_data_
   - _string_list_data_ has a corresponding value that is a list nesting one dictionary
   - the nested dictionary has 3 keys one of which is _value_ ---> this is the username of a 
     follower


2. following.json
    - dictionary with the key _relationships_following_
    - _relationships_following_ has the value of a list with dictionaries
    - each dictionary contains 3 keys, one of which is _string_list_data_
   - _string_list_data_ has a corresponding value that is a list nesting one dictionary
   - the nested dictionary has 3 keys one of which is _value_ ---> this is the username of an 
     account you are following

n.b: Without the format above, this program will fail