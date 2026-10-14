// ============================================
// CodeAlpha E-commerce Store - Main JavaScript
// ============================================

document.addEventListener('DOMContentLoaded', function() {

    // --- Navbar scroll effect ---
    const navbar = document.querySelector('.navbar');
    if (navbar) {
        window.addEventListener('scroll', function() {
            if (window.scrollY > 50) {
                navbar.classList.add('navbar-scrolled');
            } else {
                navbar.classList.remove('navbar-scrolled');
            }
        });
    }

    // --- Auto-dismiss alerts after 5 seconds ---
    const alerts = document.querySelectorAll('.alert:not(.alert-permanent)');
    alerts.forEach(function(alert) {
        setTimeout(function() {
            const bsAlert = new bootstrap.Alert(alert);
            bsAlert.close();
        }, 5000);
    });

    // --- Quantity increment/decrement buttons ---
    document.querySelectorAll('.qty-btn').forEach(function(btn) {
        btn.addEventListener('click', function() {
            const input = this.closest('.quantity-controls').querySelector('.qty-input');
            const currentVal = parseInt(input.value) || 1;
            const max = parseInt(input.max) || 99;
            const min = parseInt(input.min) || 1;
            
            if (this.dataset.action === 'increase' && currentVal < max) {
                input.value = currentVal + 1;
            } else if (this.dataset.action === 'decrease' && currentVal > min) {
                input.value = currentVal - 1;
            }
        });
    });

    // --- Animate elements on scroll ---
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver(function(entries) {
        entries.forEach(function(entry) {
            if (entry.isIntersecting) {
                entry.target.classList.add('animate-visible');
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    document.querySelectorAll('.animate-on-scroll').forEach(function(el) {
        observer.observe(el);
    });

    // --- Confirm before removing cart item ---
    document.querySelectorAll('.remove-item-form').forEach(function(form) {
        form.addEventListener('submit', function(e) {
            if (!confirm('Remove this item from your cart?')) {
                e.preventDefault();
            }
        });
    });

    // --- Smooth scroll for anchor links ---
    document.querySelectorAll('a[href^="#"]').forEach(function(anchor) {
        anchor.addEventListener('click', function(e) {
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                e.preventDefault();
                target.scrollIntoView({ behavior: 'smooth', block: 'start' });
            }
        });
    });

    // --- Add loading state to forms on submit ---
    document.querySelectorAll('form.loading-form').forEach(function(form) {
        form.addEventListener('submit', function() {
            const btn = this.querySelector('button[type="submit"]');
            if (btn) {
                btn.disabled = true;
                btn.innerHTML = '<span class="spinner-border spinner-border-sm me-2"></span>Processing...';
            }
        });
    });

    // --- Search bar focus effect ---
    const searchInput = document.querySelector('.search-input');
    if (searchInput) {
        searchInput.addEventListener('focus', function() {
            this.closest('.search-form').classList.add('search-focused');
        });
        searchInput.addEventListener('blur', function() {
            this.closest('.search-form').classList.remove('search-focused');
        });
    }

    // --- Back to top button ---
    const backToTop = document.getElementById('backToTop');
    if (backToTop) {
        window.addEventListener('scroll', function() {
            if (window.scrollY > 300) {
                backToTop.classList.add('show');
            } else {
                backToTop.classList.remove('show');
            }
        });
        backToTop.addEventListener('click', function() {
            window.scrollTo({ top: 0, behavior: 'smooth' });
        });
    }

    // --- Tooltip initialization ---
    var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    tooltipTriggerList.map(function (tooltipTriggerEl) {
        if (typeof bootstrap !== 'undefined') {
            return new bootstrap.Tooltip(tooltipTriggerEl);
        }
    });

});
