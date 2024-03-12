window.onload = function() {
    for (let i = 1; i <= 10; i++) {
        let checkbox = document.getElementById('checkbox' + i);
        if (checkbox.checked) {
            checkbox.disabled = true;
        }
    }
};