const form = document.getElementById("search_form");
const clearButton = document.getElementById("clear_button");
const table = document.getElementById("transaction_table");
const result = document.getElementById("result");


async function loadTransactions() {

    const product = document.getElementById("product").value;
    const date = document.getElementById("date").value;
    const time = document.getElementById("time").value;

    const params = new URLSearchParams();


    if (product) {
        params.append("product", product);
    }

    if (date) {
        params.append("date", date);
    }

    if (time) {
        params.append("time", time);
    }


    try {

        const response = await fetch(
            `/api/transactions?${params.toString()}`
        );

        console.log("HTTP status:", response.status);

        const responseText = await response.text();

        console.log("Raw API response:", responseText);


        let data;

        try {

            data = JSON.parse(responseText);

        } catch (error) {

            console.error(
                "API returned invalid JSON:",
                error
            );

            result.textContent =
                "The API returned an invalid response.";

            return;
        }


        if (!response.ok) {

            result.textContent =
                data.detail || "Error loading transactions.";

            return;
        }


        table.innerHTML = "";


        if (data.length === 0) {

            table.innerHTML = `
                <tr>
                    <td colspan="9">
                        No transactions found.
                    </td>
                </tr>
            `;

            return;
        }


        for (const transaction of data) {

            const row = document.createElement("tr");


            /*
             * PostgreSQL timestamptz is returned with timezone
             * information.
             *
             * JavaScript converts the timestamp to the browser's
             * local timezone automatically.
             */

            const transactionDate =
                new Date(transaction.created_at);


            const formattedDate =
                transactionDate.toLocaleString();


            row.innerHTML = `

                <td>
                    ${transaction.id}
                </td>

                <td>
                    ${formattedDate}
                </td>

                <td>
                    ${transaction.item_id}
                </td>

                <td>
                    ${transaction.item_quantity_changed}
                </td>

                <td>
                    ${transaction.item_stock_before_transaction}
                </td>

                <td>
                    ${transaction.item_stock_after_transaction}
                </td>

                <td>
                    ${transaction.transaction_type}
                </td>

                <td>
                    ${transaction.by_user}
                </td>

                <td>
                    ${transaction.reason}
                </td>

            `;

            table.appendChild(row);
        }


    } catch (error) {

        console.error(
            "Request failed:",
            error
        );

        result.textContent =
            "Could not connect to the API.";
    }
}


/*
 * Search
 */

form.addEventListener(
    "submit",
    function(event) {

        event.preventDefault();

        loadTransactions();
    }
);


/*
 * Clear filters
 */

clearButton.addEventListener(
    "click",
    function() {

        document.getElementById("product").value = "";
        document.getElementById("date").value = "";
        document.getElementById("time").value = "";

        result.textContent = "";

        loadTransactions();
    }
);


/*
 * Load all transactions when the page opens.
 */

loadTransactions();