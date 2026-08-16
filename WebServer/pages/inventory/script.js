const backButton = document.getElementById("backButton");
backButton.addEventListener("click", () => {
    console.log("back clicked");
	window.location.href = "/";
});

const loadButton = document.getElementById("loadButton");
loadButton.addEventListener("click", loadProducts);

const searchButton = document.getElementById("searchButton");
searchButton.addEventListener("click", () => {
    const searchText = document.getElementById("productSearch").value;
    searchProducts(searchText);

});


async function loadProducts(){

	const response = await fetch("/api/products");

	const products = await response.json();
	const container = document.getElementById("products");

	container.innerHTML = "";

	products.forEach(product => {
		container.innerHTML += `
            <p>
                ${product.id} |
                ${product.name} |
                Stock: ${product.stock}
            </p>
        `;

    });

}

async function searchProducts(name){

	const response = await fetch(`/api/products/search?name=${name}`);

	const products = await response.json();

	const container = document.getElementById("products");

	container.innerHTML = "";

	products.forEach(product => {
		container.innerHTML += `
            <p>
                ${product.id} |
                ${product.name} |
                Stock: ${product.stock}
            </p>
        `;

    });

}