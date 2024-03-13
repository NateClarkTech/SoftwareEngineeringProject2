console.log("JavaScript file is linked!");

function sendUpdate() {
    let checkboxes = []

    for (let i = 1; i <= 51; i++) {
        checkboxes.push(document.getElementById('item-' + i).checked);
    }

    let params = new URLSearchParams();
    for (let i = 0; i < checkboxes.length; i++) {
        params.append('item-' + i, checkboxes[i]);
    }

    

    fetch('/shoppinglist/update_shoppinglist', {  // Update this line
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-CSRFToken': getCookie('csrftoken')
        },
        body: params
    });
}

var scalar = 2;
var money = confetti.shapeFromText({ text: '💸', scalar });

var defaults = {
  spread: 360,
  ticks: 60,
  gravity: 0,
  decay: 0.96,
  startVelocity: 20,
  shapes: [money],
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

for (let i = 1; i <= 51; i++) {
    let checkbox = document.getElementById('item-' + i);
    let itembox = document.getElementById('itembox-' + i);
    checkbox.addEventListener('change', function() {
        sendUpdate();  // Send the update to the server
        
        if (checkbox.checked) {
            // Trigger a custom confetti effect
            itembox.classList.remove('not-checked');
            itembox.classList.add('checked');
            setTimeout(shoot, 0);
            setTimeout(shoot, 100);
            setTimeout(shoot, 200);
        }
        else{
            itembox.classList.remove('checked');
            itembox.classList.add('not-checked');  
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

function printDiv(divId) {
    var content = document.getElementById(divId).cloneNode(true); // Clone the content to preserve the original
    var checkboxes = content.querySelectorAll('input[type="checkbox"]');

    // Disable checkboxes
    for (var i = 0; i < checkboxes.length; i++) {
        checkboxes[i].disabled = true;
    }

    var printWindow = window.open('', 'Shopping List', 'height=400,width=800'); // Specify the window title here
    printWindow.document.write('<html><head><title>Shopping List</title></head><body>');
    printWindow.document.write(content.innerHTML); // Write the updated content to the print window
    printWindow.document.write('</body></html>');
    printWindow.document.close();

    // Define a promise that resolves when the print window is fully loaded
    var printWindowLoaded = new Promise(function(resolve, reject) {
        printWindow.onload = function() {
            resolve();
        };
    });

    // Print and close the print window once it's loaded
    printWindowLoaded.then(function() {
        printWindow.print();
        printWindow.close(); // Optional: Close the print window after printing
    });
}