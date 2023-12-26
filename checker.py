import json
import os


def main():
    print(
        "This program gives you a list of accounts that you follow but they don't follow you "
        "back")
    if not foundFiles():
        print("\nOne or more file is missing in current directory/folder. Program is exiting")
        exit(-1)
    followers = getFollowers()
    following = getFollowing()
    nonFollowing = checkNonFollowing(followers, following)
    printSummary(nonFollowing, following, followers)


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


def getFollowing() -> list:
    following = []
    with open('following.json', 'r') as file_obj:
        followingData = json.load(file_obj)
        for account in followingData["relationships_following"]:
            currFollowing = account['string_list_data'][0]['value']
            following.append(currFollowing)
    return following


def checkNonFollowing(followers, following) -> list:
    followers1 = set(followers)
    following1 = set(following)

    nonFollowing = following1 - followers1

    return list(nonFollowing)


def printSummary(nonFollowing, following, followers):
    print("\nHere are your accounts stats:")
    print(f"\tfollowing: {len(following)}")
    print(f"\tfollowers: {len(followers)}")
    if len(following) > len(followers):
        print(f"\t% of non-followers: "
              f"{round(((len(nonFollowing) / len(following)) * 100), 2)}%")
        print(f"\n{len(following) - len(followers)} do not follow you back.\nHere is the "
              f"list:")
        for nonFollower in nonFollowing:
            print(f"\t{nonFollower}")


if __name__ == "__main__":
    main()
