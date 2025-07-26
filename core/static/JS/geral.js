dpd = document.getElementById('dpd');

document.getElementById('mobi').addEventListener('click', function() {
    if (dpd.style.display === 'block') {
        dpd.style.display = 'none';
    } else {
        dpd.style.display = 'block';
    }
});

