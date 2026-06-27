import sys
path = 'd:\\Vibe Coding\\Professional Portfolio\\index.html'

with open(path, 'r', encoding='utf-8') as f:
    html = f.read()

start_str = '<div class="testimonials-marquee-wrapper">'
start_idx = html.find(start_str)
end_str = '</section>'
end_idx = html.find(end_str, start_idx)

cards = '''
                    <!-- Testimonial 1 -->
                    <div class="testimonial-card">
                        <div class="quote-icon">
                            <svg width="28" height="28" viewBox="0 0 24 24" fill="var(--accent-blue)" xmlns="http://www.w3.org/2000/svg">
                                <path d="M14.017 18L14.017 10.609C14.017 4.905 17.748 1.039 23 0L23.995 2.151C21.563 3.068 20 5.789 20 8H24V18H14.017ZM0 18V10.609C0 4.905 3.748 1.038 9 0L9.996 2.151C7.563 3.068 6 5.789 6 8H9.983L9.983 18L0 18Z"/>
                            </svg>
                        </div>
                        <div class="stars">?????</div>
                        <h3>Impressive Website Services</h3>
                        <p>"Talha has done an excellent job working with us to develop our website as we had imagined. From start to finish, Talha has been Patient, Detail-oriented, Professional, and Responsive. Highly recommended, thank you for giving your 100 percent."</p>
                        <div class="client-info">
                            <span class="client-name">MAHRUKH GUL & TEAM</span>
                            <span class="client-role">Director, Mahrukh Gull Collection</span>
                        </div>
                    </div>
                    <!-- Testimonial 2 -->
                    <div class="testimonial-card">
                        <div class="quote-icon">
                            <svg width="28" height="28" viewBox="0 0 24 24" fill="var(--accent-blue)" xmlns="http://www.w3.org/2000/svg">
                                <path d="M14.017 18L14.017 10.609C14.017 4.905 17.748 1.039 23 0L23.995 2.151C21.563 3.068 20 5.789 20 8H24V18H14.017ZM0 18V10.609C0 4.905 3.748 1.038 9 0L9.996 2.151C7.563 3.068 6 5.789 6 8H9.983L9.983 18L0 18Z"/>
                            </svg>
                        </div>
                        <div class="stars">?????</div>
                        <h3>Outstanding Experience</h3>
                        <p>"Working with TW Developers on my website was a delight, and they went above and beyond my expectations. Their team skillfully brought my ideas to life, resulting in a stunning and incredibly efficient website. I value their commitment to perfection."</p>
                        <div class="client-info">
                            <span class="client-name">Samiullah</span>
                            <span class="client-role">CEO, Tech-Max Computer Institute</span>
                        </div>
                    </div>
                    <!-- Testimonial 3 -->
                    <div class="testimonial-card">
                        <div class="quote-icon">
                            <svg width="28" height="28" viewBox="0 0 24 24" fill="var(--accent-blue)" xmlns="http://www.w3.org/2000/svg">
                                <path d="M14.017 18L14.017 10.609C14.017 4.905 17.748 1.039 23 0L23.995 2.151C21.563 3.068 20 5.789 20 8H24V18H14.017ZM0 18V10.609C0 4.905 3.748 1.038 9 0L9.996 2.151C7.563 3.068 6 5.789 6 8H9.983L9.983 18L0 18Z"/>
                            </svg>
                        </div>
                        <div class="stars">?????</div>
                        <h3>Top-Notch Services</h3>
                        <p>"I had the pleasure of working with TW Developers for my website, and they exceeded my expectations. Their team brilliantly captured my vision, creating a beautiful and highly functional website. I appreciate their dedication to excellence and ongoing support."</p>
                        <div class="client-info">
                            <span class="client-name">Samiullah</span>
                            <span class="client-role">CEO, Tech-Max Computer Institute</span>
                        </div>
                    </div>
                    <!-- Testimonial 4 -->
                    <div class="testimonial-card">
                        <div class="quote-icon">
                            <svg width="28" height="28" viewBox="0 0 24 24" fill="var(--accent-blue)" xmlns="http://www.w3.org/2000/svg">
                                <path d="M14.017 18L14.017 10.609C14.017 4.905 17.748 1.039 23 0L23.995 2.151C21.563 3.068 20 5.789 20 8H24V18H14.017ZM0 18V10.609C0 4.905 3.748 1.038 9 0L9.996 2.151C7.563 3.068 6 5.789 6 8H9.983L9.983 18L0 18Z"/>
                            </svg>
                        </div>
                        <div class="stars">?????</div>
                        <h3>Amazing Transformation</h3>
                        <p>"Talha works wonder on my WordPress site, transforming and modifying it into an attractive and engaging platform. His expertise and creativity shone through in every edit, greatly enhancing the user experience. I'm truly impressed with the results!"</p>
                        <div class="client-info">
                            <span class="client-name">M. Atif</span>
                            <span class="client-role">Happy Client</span>
                        </div>
                    </div>'''

new_block = f'''<div class="testimonials-marquee-wrapper">
                <div class="marquee-group">
{cards}
                </div>
                <div class="marquee-group" aria-hidden="true">
{cards}
                </div>
                <div class="marquee-group" aria-hidden="true">
{cards}
                </div>
                <div class="marquee-group" aria-hidden="true">
{cards}
                </div>
            </div>
        '''

if start_idx != -1 and end_idx != -1:
    new_html = html[:start_idx] + new_block + html[end_idx:]
    with open(path, 'w', encoding='utf-8') as f:
        f.write(new_html)
    print("Testimonials updated successfully!")
else:
    print("Could not find bounds.")

