console.log("JavaScript file is linked!");

function sendUpdate() {
    fetch('/leaderboard/update_checklist/', {  // Update this line
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-CSRFToken': getCookie('csrftoken')
        },
        body: new URLSearchParams({
            'task1': document.getElementById('checkbox1').checked,
            'task2': document.getElementById('checkbox2').checked,
            'task3': document.getElementById('checkbox3').checked,
            'task4': document.getElementById('checkbox4').checked,
            'task5': document.getElementById('checkbox5').checked
        })
    });
}

for (let i = 1; i <= 5; i++) {
    let checkbox = document.getElementById('checkbox' + i);
    checkbox.addEventListener('change', function() {
        var card = document.getElementById('card' + i);
        if (this.checked) {
            card.classList.add('bg-primary');
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
        sendUpdate();  // Send the update to the server
    });
}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        let cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            let cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

window.onload = function() {
    for (let i = 1; i <= 5; i++) {
        let checkbox = document.getElementById('checkbox' + i);
        let card = document.getElementById('card' + i);
        if (checkbox.checked) {
            card.classList.add('bg-primary');
            checkbox.disabled = true;
        }
    }
};