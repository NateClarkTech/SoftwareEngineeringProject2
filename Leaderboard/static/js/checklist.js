console.log("JavaScript file is linked!");

function sendUpdate() {
    fetch('/leaderboard/update_checklist/', {  
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
            'task5': document.getElementById('checkbox5').checked,
            'task6': document.getElementById('checkbox6').checked,
            'task7': document.getElementById('checkbox7').checked,
            'task8': document.getElementById('checkbox8').checked,
            'task9': document.getElementById('checkbox9').checked,
            'task10': document.getElementById('checkbox10').checked
        })
    });
}

var scalar = 2;
var unicorn = confetti.shapeFromText({ text: '🦄', scalar });

var defaults = {
  spread: 360,
  ticks: 60,
  gravity: 0,
  decay: 0.96,
  startVelocity: 20,
  shapes: [unicorn],
  scalar
};

function shoot() {
  confetti({
    ...defaults,
    particleCount: 30
  });

  confetti({
    ...defaults,
    particleCount: 5,
    flat: true
  });

  confetti({
    ...defaults,
    particleCount: 15,
    scalar: scalar / 2,
    shapes: ['circle']
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

        // If all checkboxes are checked, trigger a different confetti effect
        if (allChecked) {
            var end = Date.now() + (15 * 1000);

            // go Buckeyes!
            var colors = ['#FFBF3F',' 003087'];

            (function frame() {
              confetti({
                particleCount: 2,
                angle: 60,
                spread: 55,
                origin: { x: 0 },
                colors: colors
              });
              confetti({
                particleCount: 2,
                angle: 120,
                spread: 55,
                origin: { x: 1 },
                colors: colors
              });

              if (Date.now() < end) {
                requestAnimationFrame(frame);
              }
            }());
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
    for (let i = 1; i <= 10; i++) {
        let checkbox = document.getElementById('checkbox' + i);
        if (checkbox.checked) {
            checkbox.disabled = true;
        }
    }
};

document.getElementById('reset-button').addEventListener('click', function() {
    // Reset all checkboxes
    var checkboxes = document.querySelectorAll('input[type=checkbox]');
    for (var i = 0; i < checkboxes.length; i++) {
        checkboxes[i].checked = false;
    }

    // Send the update to the server
    sendUpdate();

    // Refresh page to undisable buttons
    location.reload();
});