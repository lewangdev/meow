import json
import os
import sys

from urllib.parse import quote


if __name__ == '__main__':

    if len(sys.argv) != 6:
        print("python labels.py owner repo user passwd action[create/update/get/delete]")
        exit(1)

    owner = sys.argv[1]
    repo = sys.argv[2]
    user = sys.argv[3]
    passwd = sys.argv[4]
    action = sys.argv[5]

    labels = None
    with open('labels.json', 'r') as f:
        labels = map(lambda l: dict(name=l['name'], color=l['color'], description=l['description']), json.loads(f.read()))

    for label in labels:
        data = json.dumps(label, ensure_ascii=False)

        cmd = None
        if 'create' == action:
            cmd = 'curl -u {0}:{1} \
                    -H "Accept: application/vnd.github.symmetra-preview+json" \
                    -d \'{4}\' \
                    https://api.github.com/repos/{2}/{3}/labels'.format(user, passwd, owner, repo, data)
        elif 'update' == action:
            cmd = 'curl -u {0}:{1} \
                    -H "Accept: application/vnd.github.symmetra-preview+json" \
                    -d \'{4}\' \
                    -X PATCH \
                    https://api.github.com/repos/{2}/{3}/labels/{5}'.format(user, passwd, owner, repo, data, quote(label['name']))
        elif 'get' == action:
            cmd = 'curl -u {0}:{1} \
                    -H "Accept: application/vnd.github.symmetra-preview+json" \
                    https://api.github.com/repos/{2}/{3}/labels > labels.json'.format(user, passwd, owner, repo)
            print(cmd)
            #os.system(cmd)
            break
        elif 'delete' == action:
            cmd = 'curl -u {0}:{1} \
                    -H "Accept: application/vnd.github.symmetra-preview+json" \
                    -d \'{4}\' \
                    -X DELETE\
                    https://api.github.com/repos/{2}/{3}/labels/{5}'.format(user, passwd, owner, repo, data, quote(label['name']))

        if cmd is not None:
           print(cmd)
           os.system(cmd)

