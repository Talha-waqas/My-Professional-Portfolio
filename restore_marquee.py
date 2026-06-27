import sys
path = 'd:\\Vibe Coding\\Professional Portfolio\\index.html'
with open(path, 'r', encoding='utf-8') as f:
    html = f.read()

start_str = '<div class="testimonials-slider">'
end_str = '</section>'
start_idx = html.find(start_str)
end_idx = html.find(end_str, start_idx)

# Extract the 4 cards from inside the track
track_start = '<div class="testimonials-track">'
track_start_idx = html.find(track_start, start_idx) + len(track_start)
track_end_idx = html.rfind('</div>', track_start_idx, end_idx) # finds the closing div of testimonials-track
# Wait, actually track_end_idx is just before the two closing divs: </div> </div>

# Let's be precise.
start_card_str = '<!-- Testimonial 1 -->'
end_card_str = '<!-- New Premium Services Section -->'
# Let's extract between Testimonial 1 and the end of the 4th card
start_card_idx = html.find(start_card_str, start_idx)
# The 4th card ends before the closing div of the track.
cards_block = html[start_card_idx:track_end_idx].strip()
if cards_block.endswith('</div>'):
    # remove the closing div of the track if it was caught
    cards_block = cards_block[:-6].strip()

new_html_block = f'''<div class="testimonials-marquee-wrapper">
                <div class="marquee-group">
                    {cards_block}
                </div>
                <div class="marquee-group" aria-hidden="true">
                    {cards_block}
                </div>
                <div class="marquee-group" aria-hidden="true">
                    {cards_block}
                </div>
                <div class="marquee-group" aria-hidden="true">
                    {cards_block}
                </div>
            </div>
        '''

# Replace from <div class="testimonials-slider"> up to but not including </section>
# Actually, up to end_idx.
# But wait, end_idx is the </section>. So we replace html[start_idx:end_idx] with new_html_block.
# Wait, html[end_idx] is '<'. If we replace up to end_idx, it will preserve </section>.

new_html = html[:start_idx] + new_html_block + html[end_idx:]

with open(path, 'w', encoding='utf-8') as f:
    f.write(new_html)
