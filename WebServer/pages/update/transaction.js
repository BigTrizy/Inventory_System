
const backButton = document.getElementById("backButton");
backButton.addEventListener("click", () => {
    console.log("back clicked");
	window.location.href = "/";
});

const form = document.getElementById("transactionForm");
const result = document.getElementById("result");

form.addEventListener("submit", async (event) => {

    event.preventDefault();

    const productId = document.getElementById("productId").value;
    const quantity = document.getElementById("quantity").value;
    const user = document.getElementById("user").value;
    const reason = document.getElementById("reason").value;

    const transaction = {
        id: Number(productId),
        qty: Number(quantity),
        user: user,
        reason: reason
    };

    try {

        const response = await fetch("/api/products/update", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(transaction)
        });

        const data = await response.json();
        console.log("Status:", response.status);
        console.log("Response:", data);

        result.textContent = data;

        result.textContent = JSON.stringify(data, null, 2);

    } catch (error) {

        result.textContent = "Error submitting transaction.";

        console.error(error);
    }

});