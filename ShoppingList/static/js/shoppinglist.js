console.log("JavaScript file is linked!");

function sendUpdate() {
    fetch('/leaderboard/update_checklist/', {  // Update this line
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-CSRFToken': getCookie('csrftoken')
        },
        body: new URLSearchParams({
            //put code for the checkboxes here.
        })
    });
}


for (let i = 1; i <= 51; i++) {
    let checkbox = document.getElementById('item-' + i);
    checkbox.addEventListener('change', function() {
        this.disabled = true;  // Disable the checkbox
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
    for (let i = 1; i <= 51; i++) {
        let checkbox = document.getElementById('item-' + i);
        if (checkbox.checked) {
            checkbox.disabled = true;
        }
    }
};