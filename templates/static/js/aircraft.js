document.addEventListener('DOMContentLoaded', function() {
    console.log("JavaScript is running..."); // Debugging
    fetch('/aircraft/api/aircraft-list-datatable/')
        .then(response => response.json())
        .then(data => {
            console.log("Fetched data:", data);
            const tableBody = document.getElementById('aircraft-list-body');
            if (!tableBody) {
                console.error("Error: #aircraft-list-body not found!");
                return;
            }
            tableBody.innerHTML = '';

            data.data.forEach(row => {
                console.log("Processing row:", row);
                const tableRow = document.createElement('tr');
                tableRow.innerHTML = `
                    <td>${row[0]}</td>  <!-- Aircraft Name -->
                    <td>${row[1]}</td>  <!-- Assembled By -->
                    <td>${row[2]}</td>  <!-- Parts List -->
                `;
                tableBody.appendChild(tableRow);
            });
        })
        .catch(error => console.error('Error fetching assembled aircrafts:', error));
});