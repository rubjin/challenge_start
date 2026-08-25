import os
import re

dir_path = 'c:/Users/rubji/challenge_start/src/html'
classes = set()
for root, _, files in os.walk(dir_path):
    for f in files:
        if f.endswith('.html'):
            content = open(os.path.join(root, f), 'r', encoding='utf-8').read()
            for match in re.findall(r'class=["\']([^"\']+)["\']', content):
                for cls in match.split():
                    if '-' in cls or '_' in cls:
                        classes.add(cls)

print('HTML Classes:', sorted(list(classes)))
