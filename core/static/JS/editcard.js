var cat = document.getElementById('menes')
var cat2 = document.getElementById('menes2')
var but = document.getElementById('butones');
var but2 = document.getElementById('butonestwo');

but.addEventListener('click', function() {
    if (cat.style.display == 'block') {
        cat.style.display = 'none';
    } else {
        cat.style.display = 'block';
    }

    console.log('Easter Egg!')
});

but2.addEventListener('click', function() {
    if (cat2.style.display == 'block') {
        cat2.style.display = 'none';
    } else {
        cat2.style.display = 'block';
    }

    console.log('Easter Egg!')
});