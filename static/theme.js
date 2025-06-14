document.addEventListener('DOMContentLoaded', function() {
    const toggle = document.getElementById('theme-toggle');
    const body = document.body;

    // Load saved theme
    if (localStorage.getItem('theme') === 'dark') {
        body.classList.add('dark-mode');
    }

    if (toggle) {
        toggle.addEventListener('click', function() {
            body.classList.toggle('dark-mode');
            // Save preference
            if (body.classList.contains('dark-mode')) {
                localStorage.setItem('theme', 'dark');
            } else {
                localStorage.setItem('theme', 'light');
            }
        });
    }
});

