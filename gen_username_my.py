import sys
import collections


User = collections.namedtuple('User', 'username forename middlename surname id')
ID, FORENAME, SURNAME, MIDDLENAME, DEPARTMENT = range(5)


def main():
    if len(sys.argv) == 1 or sys.argv[1] in {'-h', '--help'}:
        print("usage: {} file1 file2...file'n'".format(sys.argv[0]))
        sys.exit()

    usernames = set()
    users = {}
    for filename in sys.argv[1:]:
        for line in open(filename, encoding='utf8'):
            line = line.rstrip()
            if line:
                user = process_line(line, usernames)
                # print('======\n\n', user)
                users[(user.surname.lower(), user.forename.lower(), user.id)] = user

    for each in users:
        print(each,'\n', users[each])


def process_line(line, usernames):
    fields = line.split(':')
    # print(fields)
    username = generate_username(fields, usernames)
    user = User(username, fields[FORENAME], fields[MIDDLENAME], fields[SURNAME], fields[ID])
    # print(user)
    return user


def generate_username(fields, usernames):
    username = ((fields[FORENAME][0] + fields[MIDDLENAME][:1] +
    fields[SURNAME]).replace("-", "").replace("'", ""))
    username = original_name = username[:8].lower()
    count = 1

    while username in usernames:
        username = "{0}{1}".format(original_name, count)
        count += 1

    usernames.add(username)
    return username

main()
