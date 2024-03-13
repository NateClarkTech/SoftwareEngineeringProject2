function printDiv(divId) {
    var content = document.getElementById(divId).cloneNode(true); // Clone the content to preserve the original
    var checkboxes = content.querySelectorAll('input[type="checkbox"]');

    // Disable checkboxes
    for (var i = 0; i < checkboxes.length; i++) {
        checkboxes[i].disabled = true;
    }

    var printWindow = window.open('', '', 'height=400,width=800');
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