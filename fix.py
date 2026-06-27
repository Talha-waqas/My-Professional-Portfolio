import sys
path = 'd:\\Vibe Coding\\Professional Portfolio\\index.html'
with open(path, 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the track class
html = html.replace('<div class="testimonials-marquee-track">', '<div class="marquee-group">')

# Split the groups
split_marker = '                    <!-- DUPLICATE FOR INFINITE SCROLL -->'
replacement = '                </div>\n                <div class="marquee-group" aria-hidden="true">\n                    <!-- DUPLICATE FOR INFINITE SCROLL -->'
html = html.replace(split_marker, replacement)

# Now we need to add 2 more groups at the end of the wrapper to be perfectly safe on ultrawide monitors
# The wrapper ends at </div> \n        </section>
# Let us extract the block of 4 cards first.
start_str = '<!-- Testimonial 1 -->'
end_str = '                    <!-- DUPLICATE FOR INFINITE SCROLL -->'
start_idx = html.find(start_str)
end_idx = html.find(end_str)
cards_block = html[start_idx:end_idx]

# We append 2 more marquee-groups before the end of the wrapper
wrapper_end = '                </div>\n        </section>'
new_groups = '                </div>\n                <div class="marquee-group" aria-hidden="true">\n                    ' + cards_block + '                </div>\n                <div class="marquee-group" aria-hidden="true">\n                    ' + cards_block + wrapper_end
html = html.replace(wrapper_end, new_groups)

with open(path, 'w', encoding='utf-8') as f:
    f.write(html)
