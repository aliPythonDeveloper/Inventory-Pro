var updateBtn = document.getElementsByClassName('update-filter');
console.log("updateBtn: "+updateBtn)
if (updateBtn) {
    updateBtn.addEventListener('click', function() {
        var actionId = this.dataset.action;
        if (user == 'AnonymousUser') {
            console.log('Not logged in');
        } else {
            updateFilter(actionId);
        }
    });
}

function updateFilter(actionId){
var url = ""
if(actionId == "low_to_high"){
url = "/product/list/?sort_by_price=price"
}

 fetch(url)
        .then(response => {
            if (!response.ok) {
                throw new Error('Failed to fetch products');
            }
            return response.json();
        })
        .then(data => {
            displayProducts(data);  // Update the product list
        })
        .catch(error => {
            console.error('Error fetching products:', error);
        });
}

function displayProducts(products) {
    const productsContainer = document.getElementById('products');
    productsContainer.innerHTML = '';  // Clear existing products

    // Loop through products and display them
    products.forEach(product => {
        const productDiv = document.createElement('div');
        productDiv.classList.add('product-item');
        productDiv.innerHTML = `
            <h3>${product.product_name}</h3>
            <p>${product.description}</p>
            <p>Price: $${product.price}</p>

        `;
        productsContainer.appendChild(productDiv);
    });
}