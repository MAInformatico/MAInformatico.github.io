python3 -c "
from pathlib import Path
import re
d = Path('src/content/blog')
for f in d.glob('*.md'):
    nuevo = re.sub(r'^\d{4}-\d{2}-\d{2}-', '', f.name)
    if nuevo != f.name:
        f.rename(d / nuevo)
        print(f'{f.name} -> {nuevo}')
"
