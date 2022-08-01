import argparse

parser = argparse.ArgumentParser(description="Username Permutator")
parser.add_argument('usernames', help="List of usernames")

args = parser.parse_args()

usersFile = open(args.usernames, 'r')

for user in usersFile:
    username = user.rstrip('\n')
    first, last = username.split(" ")
    first = first.lower()
    last = last.lower()

    # first
    print(first)

    # flast
    print(first[0] + last)

    # first.last
    print(first + "." + last)

    # firstl
    print(first + last[0])
