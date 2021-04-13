import re
import os

name = os.getenv('BRANCH_NAME')


def check_upper():
    if any(s.isupper() for s in name):
        print('Branch name {} contains an uppercase character.'.format(name))
        exit(1)
    else:
        return True


def check_str():
    regex = re.compile("[@_!#$%^&*()<>?|\}{~:]")
    if regex.search(name) is not None:
        print('Branch name {} contains non dns compliant characters.'.format(name))
        exit(1)
    else:
        return True


def check_length():
    if len(name) > 52:
        print("The {} name to use as namespace in k8s, must be less or equal to 52 characters, "
              "please rename it\n".format(name))
        exit(1)
    else:
        return True


if __name__ == '__main__':
    if check_upper() and check_str() and check_length():
        exit(0)
    else:
        exit(1)


