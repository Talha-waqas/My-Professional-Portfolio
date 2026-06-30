document.addEventListener('DOMContentLoaded', () => {
    // --- Header Scroll Animation ---
    const header = document.querySelector('.header');
    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            header.classList.add('scrolled');
        } else {
            header.classList.remove('scrolled');
        }
    });

    // --- Smooth Scrolling ---
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            const targetId = this.getAttribute('href');
            if (targetId === '#') return;

            const targetElement = document.querySelector(targetId);
            if (targetElement) {
                e.preventDefault();
                const headerOffset = document.querySelector('.header').offsetHeight;
                const elementPosition = targetElement.getBoundingClientRect().top;
                const offsetPosition = elementPosition + window.pageYOffset - headerOffset;
                
                window.scrollTo({
                    top: offsetPosition,
                    behavior: 'smooth'
                });
            }
        });
    });

    // --- Mobile Menu Toggle ---
    const menuToggle = document.querySelector('.mobile-menu-toggle');
    const desktopNav = document.querySelector('.desktop-nav');
    
    if (menuToggle && desktopNav) {
        menuToggle.addEventListener('click', () => {
            menuToggle.classList.toggle('active');
            desktopNav.classList.toggle('active');
        });

        // Close menu when a link is clicked
        const navLinks = desktopNav.querySelectorAll('a');
        navLinks.forEach(link => {
            link.addEventListener('click', () => {
                menuToggle.classList.remove('active');
                desktopNav.classList.remove('active');
            });
        });
    }

    // --- Add subtle reveal animations on scroll (Optional enhancement) ---
    const observerOptions = {
        threshold: 0.1,
        rootMargin: "0px 0px -50px 0px"
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    // Apply animation to major sections and footer columns
    const animateElements = document.querySelectorAll('.portfolio-card, .software-card, .benefit-item, .testimonial-card, .footer-col');

    animateElements.forEach(el => {
        el.style.opacity = '0';
        el.style.transform = 'translateY(20px)';
        el.style.transition = 'opacity 0.6s ease-out, transform 0.6s ease-out';
        observer.observe(el);
    });

    // --- Portfolio Filtering Logic ---
    const filterBtns = document.querySelectorAll('.filter-btn');
    const modernCards = document.querySelectorAll('.modern-card');

    filterBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            // Remove active class from all buttons
            filterBtns.forEach(b => b.classList.remove('active'));
            // Add active class to clicked button
            btn.classList.add('active');

            const filterValue = btn.getAttribute('data-filter');

            modernCards.forEach(card => {
                const categories = card.getAttribute('data-category') || "";
                if (filterValue === 'all' || categories.includes(filterValue)) {
                    card.style.display = 'flex';
                } else {
                    card.style.display = 'none';
                }
            });
        });
    });
});

// --- Multi-Step Form Logic ---
window.nextStep = function(currentStep) {
    const currentStepEl = document.getElementById(`step-${currentStep}`);
    if (!currentStepEl) return;

    // Validate required fields
    const requiredInputs = currentStepEl.querySelectorAll('[required]');
    let isValid = true;
    
    requiredInputs.forEach(input => {
        if (!input.value.trim() || (input.type === 'email' && !input.value.includes('@'))) {
            isValid = false;
            input.style.borderColor = 'red';
        } else {
            input.style.borderColor = 'rgba(255, 255, 255, 0.15)';
        }
    });

    if (!isValid) return;

    // Hide current step, show next
    currentStepEl.style.display = 'none';
    currentStepEl.classList.remove('active');
    
    const nextStepEl = document.getElementById(`step-${currentStep + 1}`);
    if (nextStepEl) {
        nextStepEl.style.display = 'block';
        setTimeout(() => nextStepEl.classList.add('active'), 10);
        updateProgressBar(currentStep + 1);
    }
};

window.prevStep = function(currentStep) {
    const currentStepEl = document.getElementById(`step-${currentStep}`);
    if (!currentStepEl) return;
    
    currentStepEl.style.display = 'none';
    currentStepEl.classList.remove('active');
    
    const prevStepEl = document.getElementById(`step-${currentStep - 1}`);
    if (prevStepEl) {
        prevStepEl.style.display = 'block';
        setTimeout(() => prevStepEl.classList.add('active'), 10);
        updateProgressBar(currentStep - 1);
    }
};

function updateProgressBar(stepIndex) {
    const steps = document.querySelectorAll('.form-progress .step');
    const lines = document.querySelectorAll('.form-progress .step-line');
    
    steps.forEach((step, idx) => {
        if (idx < stepIndex) {
            step.classList.add('active');
        } else {
            step.classList.remove('active');
        }
    });
    
    lines.forEach((line, idx) => {
        if (idx < stepIndex - 1) {
            line.classList.add('active-line');
        } else {
            line.classList.remove('active-line');
        }
    });
}

// --- Form Submission via AJAX ---
const contactForm = document.getElementById('contactForm');
if (contactForm) {
    contactForm.addEventListener('submit', function(e) {
        e.preventDefault();
        
        const submitBtn = contactForm.querySelector('button[type="submit"]');
        const originalBtnText = submitBtn.innerText;
        submitBtn.innerText = 'Submitting...';
        submitBtn.disabled = true;

        const formData = new FormData(contactForm);
        
        fetch("https://formsubmit.co/ajax/talhawaqasofficial@gmail.com", {
            method: "POST",
            headers: { 
                'Accept': 'application/json'
            },
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            if (data.success === 'true' || data.success === true || data.success) {
                alert("Thank you! Your message has been sent successfully.");
                contactForm.reset();
                
                // Reset form steps
                document.querySelectorAll('.form-step').forEach(step => {
                    step.style.display = 'none';
                    step.classList.remove('active');
                });
                const step1 = document.getElementById('step-1');
                if (step1) {
                    step1.style.display = 'block';
                    setTimeout(() => step1.classList.add('active'), 10);
                }
                updateProgressBar(1);
            } else {
                alert("Oops! Something went wrong. Please try again.");
            }
        })
        .catch(error => {
            alert("Oops! Something went wrong. Please try again.");
            console.error(error);
        })
        .finally(() => {
            submitBtn.innerText = originalBtnText;
            submitBtn.disabled = false;
        });
    });
}
