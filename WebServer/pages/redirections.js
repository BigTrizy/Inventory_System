const toProductsListing = document.getElementById("toProductsListing");

toProductsListing.addEventListener("click", () => {
	window.location.href = "/inventory/productslisting.html";
})

const toUpdateProduct = document.getElementById("toUpdateProduct");

toUpdateProduct.addEventListener("click", () => {
	window.location.href = "/update/product.html";
})

const toUserCreate = document.getElementById("toUserCreate");

toUserCreate.addEventListener("click", () => {
	window.location.href = "/users/create.html";
})