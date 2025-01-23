var updateBtns = document.querySelectorAll('.update-filter');

if (updateBtns) {
    updateBtns.forEach(function (btn) {
        btn.addEventListener('click', function() {
            var actionId = this.dataset.action;
            if (user == 'AnonymousUser') {
                console.log('Not logged in');
            } else {
                updateFilter(actionId);
            }
        });
    });
}
function updateFilter(actionId) {
var urlParams = new URLSearchParams(window.location.search);
var url = "/product/filters/?" + urlParams + "&";
console.log("actionID" + actionId);

if (actionId == "low_to_high") {
    url = url + "sort_by=price";
} else if (actionId == "high_to_low") {
    url = url + "sort_by=price_desc";
}else if (actionId == "a_to_z") {
    url = url + "sort_by=name_asc";
}
else if (actionId == "z_to_a") {
    url = url + "sort_by=name_desc";
}
 else {
    // Handle other cases here
    console.log('Invalid action ID');
    return;  // Exit function if no valid action
}

    fetch(url)
        .then(response => {
            if (!response.ok) {
                throw new Error('Failed to fetch products');
            }
            return response.json();
        })
        .then(data => {
            console.log("displayProducts: "+JSON.stringify(data))
            displayProducts(data);  // Update the product list
        })
        .catch(error => {
            console.error('Error fetching products:', error);
        });
}

//
//function displayProducts(data) {
//    const productsContainer = document.getElementById('products');
//    productsContainer.innerHTML = '';  // Clear existing products
//
//    // Loop through products and display them
//    data.results.forEach(product => {  // Using 'data.results' as your product list
//        const productDiv = document.createElement('div');
//        productDiv.classList.add('product-item');
//        productDiv.innerHTML = `
//            <h3>${product.product_name}</h3>
//            <p>${product.description}</p>
//            <p>Price: $${product.price}</p>
//        `;
//        productsContainer.appendChild(productDiv);
//    });
//}


//
function displayProducts(data) {
    const productsContainer = document.getElementById('products');
    productsContainer.innerHTML = '';  // Clear existing products

    // Loop through products and display them
    data.results.forEach(product => {  // Using 'data.results' as your product list
        const productDiv = document.createElement('div');
        productDiv.classList.add('prod-items', 'section-items');

        // Get the first image (if available)
        const firstImage = product.products_image.length > 0 ? product.products_image[0].category_image : '';

        // Construct the product HTML
        productDiv.innerHTML = `
    <div class="prodlist-i">
        ${firstImage ? `<a class="prodlist-i-img" href="product.html"><img src="${firstImage}" alt="${product.product_name}"></a>` : ''}
        <div class="prodlist-i-cont">
            <h3><a href="#">${product.product_name}</a></h3>
            <div class="prodlist-i-txt">${product.description}</div>
            <div class="prodlist-i-skuwrap">
                <div class="prodlist-i-skuitem">
                    <p class="prodlist-i-skuttl">Color</p>
                    <ul class="prodlist-i-skucolor">
                                ${product.color_variant.map(color => `
                                    <li>
                                        <img src="${color.image}" alt="${color.color_name}">
                                    </li>
                                `).join('')}
                            </ul>
                </div>
                <div class="prodlist-i-skuitem">
                    <p class="prodlist-i-skuttl">Clothes sizes</p>
                    <div class="offer-props-select">
                        <p>XS</p>
                        <ul>
                            <li><a href="#">S</a></li>
                            <li><a href="#">M</a></li>
                            <li><a href="#">L</a></li>
                            <li class="active"><a href="#">XS</a></li>
                            <li><a href="#">XL</a></li>
                            <li><a href="#">XXL</a></li>
                            <li><a href="#">XXXL</a></li>
                        </ul>
                    </div>
                </div>
            </div>
            <div class="prodlist-i-action">
                <p class="prodlist-i-qnt">
                    <input value="1" type="text">
                    <a href="#" class="prodlist-i-plus"><i class="fa fa-angle-up"></i></a>
                    <a href="#" class="prodlist-i-minus"><i class="fa fa-angle-down"></i></a>
                </p>
                <p class="prodlist-i-addwrap">
                    <a href="#" class="prodlist-i-add">Add to cart</a>
                </p>
                <span class="prodlist-i-price"><b>$${product.price}</b></span>
            </div>
            <p class="prodlist-i-info">
                <a href="#" class="prodlist-i-favorites"><i class="fa fa-heart"></i> Add to wishlist</a>
                <a href="#" class="qview-btn prodlist-i-qview"><i class="fa fa-search"></i> Quick view</a>
                <a class="prodlist-i-compare" href="#"><i class="fa fa-bar-chart"></i> Compare</a>
            </p>
        </div>
<div class="prodlist-i-props-wrap">
						<ul class="prodlist-i-props">
							<li><b>Exterior</b> Silt Pocket</li>
							<li><b>Material</b> PU</li>
							<li><b>Occasion</b> Versatile</li>
							<li><b>Shape</b> Casual Tote</li>
							<li><b>Pattern Type</b> Solid</li>
							<li><b>Style</b> American Style</li>
							<li><b>Hardness</b> Soft</li>
							<li><b>Decoration</b> None</li>
							<li><b>Closure Type</b> Zipper</li>
						</ul>
					</div>
    </div>
`;


        productsContainer.appendChild(productDiv);
    });
}

