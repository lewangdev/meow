import json
import os
import sys


if __name__ == '__main__':

    if len(sys.argv) != 5:
        print("python labels.py owner repo user passwd")
        exit(1)

    owner = sys.argv[1]
    repo = sys.argv[2]
    user = sys.argv[3]
    passwd = sys.argv[4]

    labels = None
    with open('labels.json', 'r') as f:
        labels = json.loads(f.read())

    for label in labels:
        data = json.dumps(label, ensure_ascii=False)
        cmd = 'curl -u {0}:{1} -d \'{4}\' https://api.github.com/repos/{2}/{3}/labels'.format(user, passwd, owner, repo, data)
        print(cmd)
        os.system(cmd)

