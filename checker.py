import json
import os


def main():
    print(
        "This program gives you a list of accounts that follow you but you don't follow them "
        "back")
    if not foundFiles():
        print("\nOne or more file is missing in current directory/folder. Program is exiting")
        exit(-1)
    followers = getFollowers()
    print(len(followers))


def foundFiles() -> bool:
    found1 = False
    found2 = False
    print("\nChecking for presence of the required files: ")
    if os.path.exists('followers_1.json'):
        found1 = True
        print("\tfollowers_1.json: found")
    else:
        print("\tfollowers_1.json: not found")
    if os.path.exists('following.json'):
        found2 = True
        print('\tfollowing.json: found')
    else:
        print('\tfollowing.json: not found')

    return found1 & found2


def getFollowers() -> list:
    followers = []
    with open('followers_1.json', 'r') as file_obj:
        followerData = json.load(file_obj)
        for follower in followerData:
            currFollower = follower['string_list_data'][0]['value']
            followers.append(currFollower)

    return followers


if __name__ == "__main__":
    main()
