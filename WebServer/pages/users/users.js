console.log("NEW CREATE USER SCRIPT LOADED");

const form = document.getElementById("create_user_form");
const result = document.getElementById("result");

form.addEventListener("submit", async (event) => {

    event.preventDefault();

    const username = document.getElementById("username").value;
    const access_level = document.getElementById("access_level").value;
    const password = document.getElementById("password").value;

    const transaction = {
        username: username,
        access_level: Number(access_level),
        password: password
    };

    try {

    const response = await fetch("/api/users/create", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            username: username,
            access_level: Number(access_level),
            password: password
        })
    });

    console.log("HTTP status:", response.status);
    console.log(
        "Content-Type:",
        response.headers.get("content-type")
    );

    const responseText = await response.text();

    console.log("Raw response:", responseText);

    try {

        const data = JSON.parse(responseText);

        if (response.ok) {
            result.textContent = "User created successfully.";
        } else {
            result.textContent =
                data.detail || "Error creating user.";
        }

    } catch (error) {

        console.error("Response was not valid JSON:", error);
        result.textContent = "Server returned an invalid response.";
    }

} catch (error) {

    console.error("Request failed:", error);
    result.textContent = "Could not reach the API.";

}
});