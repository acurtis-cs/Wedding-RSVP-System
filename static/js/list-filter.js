

document.querySelectorAll(".filterable-table").forEach(table => {

    // Get all guest rows with associated data
    const rows = table.querySelectorAll("tbody tr");
    // Get the dropdown element into a variable
    const dropdown = table.querySelector(".filter-by-value");

    // Retrieve all values from the second column of the table
    const values = Array.from(rows, row =>
        row.cells[1].textContent.trim()
    );
    // Remove duplicate values collected above and sort alphabetically
    const options = [...new Set(values)].sort();

    // Add each unique value to the dropdown
    options.forEach(value => {
        // Create a new option element for each unique value
        const option = document.createElement("option");
        // Set the text content of the option element to the unique value
        option.value = value;
        // Set the value of the option element to the unique value
        option.textContent = value;
        
        // Add the option element to the dropdown
        dropdown.appendChild(option);
    });

    // Filter records when dropdown selection changes
    dropdown.addEventListener("change", function() {
        // Loop through each row in the table
        rows.forEach(row => {
            // Get the value from the second column of the current row
            const value = row.cells[1].textContent.trim();
            
            // Show the row if no filter is selected or the value matches the selected filter
            if (dropdown.value === "" || dropdown.value === value) {
                row.style.display = "";
            } else {
                row.style.display = "none";
            }
        });
    });
});
