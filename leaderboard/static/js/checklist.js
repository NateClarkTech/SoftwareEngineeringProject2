console.log("JavaScript file is linked!");

for (let i = 1; i <= 5; i++) {
    let checkbox = document.getElementById('checkbox' + i);
    checkbox.addEventListener('change', function() {
        var card = document.getElementById('card' + i);
        if (this.checked) {
            card.classList.add('bg-primary');
            console.log("Making color PRIMARY");
            this.disabled = true;  // Disable the checkbox
            var toastElList = [].slice.call(document.querySelectorAll('.toast'))
            var toastList = toastElList.map(function (toastEl) {
                return new bootstrap.Toast(toastEl, {
                    autohide: false  // Make the toast stay until the user closes it
                })
            });
            toastList.forEach(toast => toast.show());  // Show the toast
        } else {
            card.classList.remove('bg-primary');
        }
    });
}