let nextCursor = null;

async function loadCategories() {

    const response = await fetch("/categories");
    const data = await response.json();

    const select = document.getElementById("category");

    select.innerHTML =
        "<option value=''>All Categories</option>";

    data.categories.forEach(category => {

        select.innerHTML +=
            `<option value="${category}">${category}</option>`;

    });

}

async function loadProducts(cursor = null) {

    const category =
        document.getElementById("category").value;

    let url = "/products?limit=20";

    if (category) {
        url += "&category=" + encodeURIComponent(category);
    }

    if (cursor) {
        url +=
            `&cursor_updated_at=${encodeURIComponent(cursor.cursor_updated_at)}`
            + `&cursor_id=${cursor.cursor_id}`;
    }

    const response = await fetch(url);
    const data = await response.json();

    nextCursor = data.next_cursor;

    const tbody =
        document.getElementById("productTable");

    tbody.innerHTML = "";

    data.items.forEach(product => {

        tbody.innerHTML += `
        <tr>
            <td>${product.id}</td>
            <td>${product.name}</td>
            <td>${product.category}</td>
            <td>₹ ${Number(product.price).toFixed(2)}</td>
        </tr>
        `;

    });

}

function resetFilter() {

    document.getElementById("category").value = "";

    nextCursor = null;

    loadProducts();

}

document
    .getElementById("nextBtn")
    .addEventListener("click", () => {

        if (nextCursor) {

            loadProducts(nextCursor);

        }

    });

loadCategories();
loadProducts();