console.log("JavaScript file is linked!");

function sendUpdate(items) {
    fetch('/leaderboard/update_checklist/', {  // Update this line
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-CSRFToken': getCookie('csrftoken')
        },
        body: new URLSearchParams({
            'task1': document.getElementById('').checked,
            'task2': document.getElementById('checkbox2').checked,
            'task3': document.getElementById('checkbox3').checked,
            'task4': document.getElementById('checkbox4').checked,
            'task5': document.getElementById('checkbox5').checked,
            'task6': document.getElementById('checkbox6').checked,
            'task7': document.getElementById('checkbox7').checked,
            'task8': document.getElementById('checkbox8').checked,
            'task9': document.getElementById('checkbox9').checked,
            'task10': document.getElementById('checkbox10').checked
        })

        for item in items
    });
}


for (let i = 1; i <= 10; i++) {
    let checkbox = document.getElementById('checkbox' + i);
    checkbox.addEventListener('change', function() {
        this.disabled = true;  // Disable the checkbox
        sendUpdate();  // Send the update to the server

        // Trigger a custom confetti effect
        setTimeout(shoot, 0);
        setTimeout(shoot, 100);
        setTimeout(shoot, 200);

        let allChecked = true;
        for (let j = 1; j <= 10; j++) {
            if (!document.getElementById('checkbox' + j).checked) {
                allChecked = false;
                break;
            }
        }
        
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