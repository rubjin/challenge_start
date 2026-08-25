import os
import re

dir_path = 'c:/Users/rubji/challenge_start/src'

def to_camel(match):
    text = match.group(0)
    parts = [p for p in re.split(r'[-_]+', text) if p]
    if len(parts) <= 1:
        return text
    return parts[0] + ''.join(p.capitalize() for p in parts[1:])

# Include all the specific custom identifiers we saw:
prefixes = r'\b(?:ch|guide|is|sv|section)[-_][a-zA-Z0-9-_]+\b'
specific_words = r'\b(?:code-block|rabbit-wrap|rule-list|stock-view)\b'

pattern = re.compile(f'({prefixes}|{specific_words})')

for root, _, files in os.walk(dir_path):
    for f in files:
        if f.endswith('.html') or f.endswith('.scss') or f.endswith('.css'):
            path = os.path.join(root, f)
            with open(path, 'r', encoding='utf-8') as file:
                content = file.read()
            
            new_content = pattern.sub(to_camel, content)
            
            if new_content != content:
                with open(path, 'w', encoding='utf-8') as file:
                    file.write(new_content)
                print(f"Updated {path}")
