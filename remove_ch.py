import os
import re

dir_path = 'c:/Users/rubji/challenge_start'

def remove_ch(match):
    text = match.group(1)
    return text[0].lower() + text[1:]

pattern = re.compile(r'\bch([A-Z][a-zA-Z0-9]*)\b')

for root, _, files in os.walk(dir_path):
    if '.git' in root or '.gemini' in root:
        continue
    for f in files:
        if f.endswith(('.html', '.scss', '.css')):
            path = os.path.join(root, f)
            with open(path, 'r', encoding='utf-8') as file:
                content = file.read()
            
            new_content = pattern.sub(remove_ch, content)
            
            # Additional cleanup for convention.html text that specifically mentions ch-
            new_content = new_content.replace('<code>ch-</code>', '<code>(제거됨)</code>')
            
            if new_content != content:
                with open(path, 'w', encoding='utf-8') as file:
                    file.write(new_content)
                print(f"Updated {path}")
