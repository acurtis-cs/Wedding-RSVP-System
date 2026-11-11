
// Enable alphabetical sorting for tables with the sortable-table class
document.querySelectorAll(".sortable-table").forEach(table => {
    // Get the table body
    const tbody = table.querySelector("tbody");
    // Store the original rows in their initial order (important for restoring the original order)
    const originalRows = Array.from(tbody.querySelectorAll("tr"));
    // Get the sort button and its symbol element
    const button = table.querySelector(".sort-by-name");
    const symbol = button.querySelector("span");

    // 0 = Original order, 1 = A-Z, 2 = Z-A
    let sortState = 0;

    button.addEventListener("click", function() {

        // Cycle through three sorting states using %3 to wrap around back to 0 after Z-A
        sortState = (sortState + 1) % 3;
        // Start with the original rows
        let rows = [...originalRows];

        // Sort alphabetically by first name
        if (sortState === 1) {
            rows.sort((a, b) =>
                a.dataset.firstName.localeCompare(b.dataset.firstName, undefined, { sensitivity: "base" })
            );
        }

        // Sort reverse alphabetically by first name
        else if (sortState === 2) {
            rows.sort((a, b) =>
                b.dataset.firstName.localeCompare(a.dataset.firstName, undefined, { sensitivity: "base" })
            );
        }

        // Display the rows in the selected order
        tbody.append(...rows);
        // Update the sorting symbol
        symbol.textContent = ["-", "↑", "↓"][sortState];
    });
});
