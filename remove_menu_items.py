import os
import glob
import re

for filepath in glob.glob('/Users/steve/Projects/Araneta/pub-sub/engage/*.html'):
    with open(filepath, 'r') as f:
        content = f.read()
    
    # Remove Reports block
    content = re.sub(r'<a href="[^"]*" class="flex items-center gap-3 px-3 py-2 rounded-xl text-xs font-medium text-zinc-500 hover:bg-zinc-100 transition-colors">\s*<svg[^>]*>.*?<\/svg>\s*<span>Reports<\/span>\s*<\/a>', '', content, flags=re.DOTALL)
    
    # Remove Stores block
    content = re.sub(r'<a href="[^"]*" class="flex items-center gap-3 px-3 py-2 rounded-xl text-xs font-medium text-zinc-500 hover:bg-zinc-100 transition-colors">\s*<svg[^>]*>.*?<\/svg>\s*<span>Stores<\/span>\s*<\/a>', '', content, flags=re.DOTALL)
    
    # Remove Whitespace Radar block
    content = re.sub(r'<a href="[^"]*" class="flex items-center gap-3 px-3 py-2 rounded-xl text-xs font-medium text-zinc-500 hover:bg-zinc-100 transition-colors">\s*<svg[^>]*>.*?<\/svg>\s*<span>Whitespace Radar<\/span>\s*<\/a>', '', content, flags=re.DOTALL)
    
    with open(filepath, 'w') as f:
        f.write(content)

print("done")
