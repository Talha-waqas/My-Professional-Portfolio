import sys
path = 'd:\\Vibe Coding\\Professional Portfolio\\index.html'
with open(path, 'r', encoding='utf-8') as f:
    html = f.read()

# We need to replace the entire marquee wrapper with a simple scrollable slider
start_str = '<div class="testimonials-marquee-wrapper">'
end_str = '</section>'
start_idx = html.find(start_str)
end_idx = html.find(end_str)

# The first 4 cards are in the first marquee-group
group_start_str = '<div class="marquee-group">'
group_end_str = '</div>\n                <div class="marquee-group" aria-hidden="true">'
group_start_idx = html.find(group_start_str, start_idx) + len(group_start_str)
group_end_idx = html.find(group_end_str, group_start_idx)

original_cards = html[group_start_idx:group_end_idx]

new_slider = f'''<div class="testimonials-slider">
                <div class="testimonials-track">
{original_cards}                </div>
            </div>
        '''

html = html[:start_idx] + new_slider + html[end_idx:]

with open(path, 'w', encoding='utf-8') as f:
    f.write(html)
