var cat = document.getElementById('menes')
var but = document.getElementById('butones');

but.addEventListener('click', function() {
    if (cat.style.display === 'block') {
        cat.style.display = 'none';
    } else {
        cat.style.display = 'block';
    }
});