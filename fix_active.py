filepath = '/Users/steve/Projects/Araneta/pub-sub/engage/03-campaign-report.html'
with open(filepath, 'r') as f:
    content = f.read()

# Make Campaigns inactive
content = content.replace(
    '<a href="01-campaigns-list.html" class="flex items-center gap-3 px-3 py-2 rounded-xl text-xs font-semibold bg-brand-primary/10 text-brand-primary">',
    '<a href="01-campaigns-list.html" class="flex items-center gap-3 px-3 py-2 rounded-xl text-xs font-medium text-zinc-500 hover:bg-zinc-100 transition-colors">'
)

# Make Reports active
content = content.replace(
    '<a href="03-campaign-report.html" class="flex items-center gap-3 px-3 py-2 rounded-xl text-xs font-medium text-zinc-500 hover:bg-zinc-100 transition-colors">',
    '<a href="03-campaign-report.html" class="flex items-center gap-3 px-3 py-2 rounded-xl text-xs font-semibold bg-brand-primary/10 text-brand-primary">'
)

with open(filepath, 'w') as f:
    f.write(content)
print("fixed")
