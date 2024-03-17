console.log("JavaScript file is linked!");

 /**
 * Gets each shopping list item and pushes their checkbox state
 * then takes the state of the checkboxes and updates the database
 * 
 * @returns {void}
 */
function sendUpdate() {
    //make an array for the checkboxes
    let checkboxes = []

    //get every single item's checkbox on the page
    let i = 1;
    while (document.getElementById('item-' + i).checked) {
        checkboxes.push(document.getElementById('item-' + i).checked);
    }

    //add the checkboxes to 
    let params = new URLSearchParams();
    for (let i = 0; i < checkboxes.length; i++) {
        params.append('item-' + i, checkboxes[i]);
    }

    //send request to server to update database.
    fetch('/shoppinglist/update_shoppinglist', {
        method: 'POST', //request is type POST

        //details of the request
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-CSRFToken': getCookie('csrftoken')
        },

        //data being sent to the server
        body: params
    });
}


//properties for the confetti
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

/**
 * Shoots confetti on the screen using the confetti package
 * 
 * package used:  https://www.kirilv.com/canvas-confetti/
 * @returns {void}
 */
function shoot() {

    //Shoots money coneftti
    confetti({
        ...defaults,
        particleCount: 30
    });

    //Shoots money confetti that doesn't spin
    confetti({
        ...defaults,
        particleCount: 5,
        flat: true
    });

    //Shoots circle confetti
    confetti({
        ...defaults,
        particleCount: 15,
        scalar: scalar / 2,
        shapes: ['circle']
    });
}

/**
 * Gets every shopping list item on the page and adds javascript
 * so that when a checkbox is clicked the database is updated
 * and confetti shoots when a checkbox is marked bought
 */
let i = 1;
while (document.getElementById('itembox-' + i)) {
    
    //get the current shopping list item
    let itembox = document.getElementById('itembox-' + i);
    let checkbox = document.getElementById('item-' + i);
   
    //add an event listener so that when a shopping item's state is changed this code executes
    checkbox.addEventListener('change', function() {
        
        //update the database
        sendUpdate(); 
        
        //if the checkbox is checked
        if (checkbox.checked) {
            // update the class so stylization changes
            itembox.classList.remove('not-checked');
            itembox.classList.add('checked');

            //shoot confetti
            setTimeout(shoot, 0);
            setTimeout(shoot, 100);
            setTimeout(shoot, 200);
        }
        //if the checkbox is not checked
        else{
            // update the class so stylization changes
            itembox.classList.remove('checked');
            itembox.classList.add('not-checked');  
        }
    });
}
 
/**
 * Gets every shopping list item on the page and adds javascript
 * so that when a checkbox is clicked the database is updated
 * 
 * @param {string} name 
 * @return {string} cookie
 */
function getCookie(name) {

    //If a cookie excists
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        //split the cookie into parts
        let cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            let cookie = cookies[i].trim();

            //Find the cookie that matches the name give
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }

    //return the cookie
    return cookieValue;
}

/**
 * Gets the contents of a div to print
 * Will lock the page till the print window is closed
 * 
 * @param {string} divId the id of the div that we want to rpint
 */
function printDiv(divId) {
    //get a copy of the dic we want to print
    var content = document.getElementById(divId).cloneNode(true);
    var checkboxes = content.querySelectorAll('input[type="checkbox"]');

    // Disable checkboxes
    for (var i = 0; i < checkboxes.length; i++) {
        checkboxes[i].disabled = true;
    }

    //make the print window
    var printWindow = window.open('', '', 'height=400,width=800');
    printWindow.document.write('<html><head><title>Shopping List</title>');

    // Include CSS stylesheets
    var stylesheets = document.querySelectorAll('link[rel="stylesheet"]');
    for (var i = 0; i < stylesheets.length; i++) {
        printWindow.document.write(stylesheets[i].outerHTML);
    }

    //add the contents of the div to the print window
    printWindow.document.write('</head><body>');
    printWindow.document.write(content.innerHTML);
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
        printWindow.close();
    });
}
