
// Wczytaj zapisany motyw przy starcie
(function () {
    const saved = localStorage.getItem('theme') || 'light';
    document.documentElement.setAttribute('data-theme', saved);
})();

function setTheme(theme) {
    document.documentElement.setAttribute('data-theme', theme);
    localStorage.setItem('theme', theme);
    updateButtons(theme);
}

function updateButtons(theme) {
    document.querySelectorAll('.theme-btn').forEach(btn => {
        btn.classList.toggle('active', btn.dataset.theme === theme);
    });
}

document.addEventListener('DOMContentLoaded', function () {
    const current = localStorage.getItem('theme') || 'light';
    updateButtons(current);
});
