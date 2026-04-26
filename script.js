const API_URL = "http://127.0.0.1:8001/products";

// Load all products
async function fetchProducts() {
    const res = await fetch(API_URL);
    const data = await res.json();

    const tableBody = document.querySelector("#productTable tbody");
    tableBody.innerHTML = "";

    data.forEach(product => {
        const row = `
            <tr>
                <td>${product.id}</td>
                <td>${product.name}</td>
                <td>${product.brand}</td>
                <td>${product.description}</td>
                <td>${product.price}</td>
                <td>${product.quantity}</td>
                <td>
                    <button class="edit-btn" onclick="editProduct(${product.id})">Edit</button>
                    <button class="delete-btn" onclick="deleteProduct(${product.id})">Delete</button>
                </td>
            </tr>
        `;
        tableBody.innerHTML += row;
    });
}

// Add Product
document.getElementById("productForm").addEventListener("submit", async (e) => {
    e.preventDefault();

    const product = {
        id: parseInt(document.getElementById("id").value),
        name: document.getElementById("name").value,
        brand: document.getElementById("brand").value,
        description: document.getElementById("description").value,
        price: parseFloat(document.getElementById("price").value),
        quantity: parseInt(document.getElementById("quantity").value)
    };

    await fetch(API_URL, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(product)
    });

    alert("Product Added!");
    fetchProducts();
});

// Delete Product
async function deleteProduct(id) {
    await fetch(`${API_URL}/${id}`, {
        method: "DELETE"
    });

    alert("Deleted!");
    fetchProducts();
}

// Edit Product
async function editProduct(id) {
    const res = await fetch(`${API_URL}/${id}`);
    const product = await res.json();

    document.getElementById("id").value = product.id;
    document.getElementById("name").value = product.name;
    document.getElementById("brand").value = product.brand;
    document.getElementById("description").value = product.description;
    document.getElementById("price").value = product.price;
    document.getElementById("quantity").value = product.quantity;

    // Change form behavior to update
    const form = document.getElementById("productForm");
    form.onsubmit = async (e) => {
        e.preventDefault();

        await fetch(`${API_URL}/${id}`, {
            method: "PUT",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                id: id,
                name: document.getElementById("name").value,
                brand: document.getElementById("brand").value,
                description: document.getElementById("description").value,
                price: parseFloat(document.getElementById("price").value),
                quantity: parseInt(document.getElementById("quantity").value)
            })
        });

        alert("Updated!");
        form.reset();
        fetchProducts();
    };
}

// Initial Load
fetchProducts();


// Search


// Load
fetchProducts();