// @vitest-environment jsdom
import { test, expect, vi } from "vitest";


// a sample table for testing so I don't have to render Flask or use Playwright. This structure matches the table used in the application.
// While the table is not rendered by Flask, it allows us to test the JavaScript functionality in isolation. 
// Ensuring my tests match the actual table structure helps verify that the JavaScript for sorting and filtering works correctly with the application's HTML.
async function setupTable(heading, guests) {

    document.body.innerHTML = `
        <table class="sortable-table filterable-table">
            <thead>
                <tr>
                    <th><button class="sort-by-name">Guest Name <span>-</span></button></th>
                    <th><select class="filter-by-value"><option value="">${heading}</option></select></th>
                </tr>
            </thead>
            <tbody>
                ${guests.map(guest => `
                    <tr data-first-name="${guest[0]}">
                        <td>${guest[0]}</td>
                        <td>${guest[1]}</td>
                    </tr>
                `).join("")}
            </tbody>
        </table>
    `;

    // Pulling our actual JavaScript code for each test
    vi.resetModules();
    await import("../static/js/list-sort.js");
    await import("../static/js/list-filter.js");
}

// Get names in the current table order
function getNames() {
    return Array.from(document.querySelectorAll("tbody tr"))
        .map(row => row.dataset.firstName);
}

// Get names that are currently visible
function getVisibleNames() {
    return Array.from(document.querySelectorAll("tbody tr"))
        .filter(row => row.style.display !== "none")
        .map(row => row.dataset.firstName);
}

// Test 1: RSVP Sorting
test("RSVP sorting cycles through all three states", async () => {

    await setupTable("RSVP Status", [
        ["Mary", "Attending"],
        ["Alex", "Not Attending"],
        ["Bob", "Not Responded"]
    ]);
    // Get the sort button
    const button = document.querySelector(".sort-by-name");
    // Check the initial order
    expect(getNames()).toEqual(["Mary", "Alex", "Bob"]);

    button.click(); // A-Z
    expect(getNames()).toEqual(["Alex", "Bob", "Mary"]);
    expect(button.querySelector("span").textContent).toBe("↑");

    button.click(); // Z-A
    expect(getNames()).toEqual(["Mary", "Bob", "Alex"]);
    expect(button.querySelector("span").textContent).toBe("↓");

    button.click(); // Original
    expect(getNames()).toEqual(["Mary", "Alex", "Bob"]);
    expect(button.querySelector("span").textContent).toBe("-");
});


// Test 2: RSVP Filtering
test("RSVP filtering shows only matching guests", async () => {

    await setupTable("RSVP Status", [
        ["Mary", "Attending"],
        ["Alex", "Not Attending"],
        ["John", "Attending"]
    ]);

    const dropdown = document.querySelector(".filter-by-value");
    // Set the filter to "Attending"
    dropdown.value = "Attending";
    dropdown.dispatchEvent(new Event("change"));

    // Check that only matching guests are visible
    expect(getVisibleNames()).toEqual(["Mary", "John"]);

    dropdown.value = ""; // Reset filter
    dropdown.dispatchEvent(new Event("change"));
    // Check that all guests are visible after resetting the filter (should be 3)
    expect(getVisibleNames()).toHaveLength(3);
});


// Test 3: Meal List Sorting and Filtering
test("Meal List sorting and filtering works", async () => {

    await setupTable("Meal Selection", [
        ["Zoe", "Chicken"],
        ["Amy", "Vegetarian"],
        ["Mike", "Chicken"]
    ]);

    const button = document.querySelector(".sort-by-name");
    const dropdown = document.querySelector(".filter-by-value");

    // Check meal options were created
    expect(dropdown.options.length).toBe(3);

    button.click(); // A-Z
    expect(getNames()).toEqual(["Amy", "Mike", "Zoe"]);
    expect(button.querySelector("span").textContent).toBe("↑");

    // Set the filter to "Chicken"
    dropdown.value = "Chicken";
    dropdown.dispatchEvent(new Event("change"));
    // Check that only matching meals are visible
    expect(getVisibleNames()).toEqual(["Mike", "Zoe"]);
    // Click the sort button to reverse the order
    button.click(); // Z-A
    expect(getVisibleNames()).toEqual(["Zoe", "Mike"]);
    expect(button.querySelector("span").textContent).toBe("↓");
});


// Test 4: Empty Table
test("Empty table works without errors", async () => {
    // Set up an empty table
    await setupTable("RSVP Status", []);
    // Get references to the sort button and filter dropdown
    const button = document.querySelector(".sort-by-name");
    const dropdown = document.querySelector(".filter-by-value");
    // Click the sort button multiple times to cycle through sort states
    button.click();
    button.click();
    button.click();

    // Dispatch a change event on the filter dropdown
    dropdown.dispatchEvent(new Event("change"));
    // Check that the table remains empty and the dropdown has only the default option
    expect(getNames()).toEqual([]);
    expect(dropdown.options.length).toBe(1);
});
