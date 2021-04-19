#!/usr/bin/env python
import re
import os

name = os.getenv('NAME_TO_VALIDATE')


def check_upper():
    if name is not None:
        if any(s.isupper() for s in name):
            print('Branch name {} contains an uppercase character.'.format(name))
            return True
        else:
            return False
    else:
        print('Branch name is empty')
        return False


def check_str():
    regex = re.compile("[@_!#$%^&*()<>?|\}{~:]")
    if name is not None:
        if regex.search(name) is not None:
            print('Branch name {} contains non dns compliant characters.'.format(name))
            return True
        else:
            return False
    else:
        print('Branch name is empty')
        return False


def check_length():
    if name is not None:
        if len(name) > 52:
            print("The {} name to use as namespace in k8s, must be less or equal to 52 characters, "
                  "please rename it\n".format(name))
            return True
        else:
            return False
    else:
        print('Branch name is empty')
        return False


if __name__ == '__main__':
    if name is not None:
        if check_upper() == False and check_str() == False and check_length() == False:
            exit(0)
        else:
            exit(1)
    else:
        print('Branch name is empty')
        exit(1)
