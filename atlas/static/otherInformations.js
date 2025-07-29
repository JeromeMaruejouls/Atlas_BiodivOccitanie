/* Permet de compacter les listes d'observateurs et de communes */

document.addEventListener('DOMContentLoaded', function () {
    const btn = document.getElementById('toggle-observers-btn');
    const more = document.getElementById('more-observers');
    let expanded = false;
    if (btn && more) {
        btn.addEventListener('click', function () {
            expanded = !expanded;
            more.classList.toggle('d-none');
            btn.textContent = expanded ? 'Afficher moins' : 'Afficher plus';
        });
    }
});