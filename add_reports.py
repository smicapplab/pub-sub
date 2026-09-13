import os
import glob

reports_link = """        <a href="03-campaign-report.html" class="flex items-center gap-3 px-3 py-2 rounded-xl text-xs font-medium text-zinc-500 hover:bg-zinc-100 transition-colors">
          <svg class="w-4 h-4 shrink-0" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path stroke-linecap="round" stroke-linejoin="round" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z"/></svg>
          <span>Reports</span>
        </a>"""

for filepath in glob.glob('/Users/steve/Projects/Araneta/pub-sub/engage/*.html'):
    with open(filepath, 'r') as f:
        content = f.read()
    
    # Insert after Templates
    if '<span>Templates</span>' in content:
        # split at Templates</a> and insert
        parts = content.split('<span>Templates</span>\n        </a>')
        if len(parts) == 2:
            new_content = parts[0] + '<span>Templates</span>\n        </a>\n' + reports_link + parts[1]
            with open(filepath, 'w') as f:
                f.write(new_content)

print("done")
