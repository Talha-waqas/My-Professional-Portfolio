import sys
path = 'd:\\Vibe Coding\\Professional Portfolio\\index.html'
with open(path, 'r', encoding='utf-8') as f:
    html = f.read()

start_str = '<!-- New Premium Services Section -->'
first_idx = html.find(start_str)
second_idx = html.find(start_str, first_idx + len(start_str))

end_str = '<!-- Proven Formula (My Expertise) -->'
end_idx = html.find(end_str)

# We want to keep everything up to second_idx, and everything from end_idx onwards.
# But second_idx is exactly where the duplication starts!
# Let's check what's immediately before second_idx.
# It should be the end of the Testimonials section.

if second_idx != -1 and end_idx != -1 and second_idx < end_idx:
    new_html = html[:second_idx] + html[end_idx:]
    with open(path, 'w', encoding='utf-8') as f:
        f.write(new_html)
    print("Fixed duplication!")
else:
    print("Could not find indices properly.")
