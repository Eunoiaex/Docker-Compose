function togglePasswordVisibility() {
    var passwordInput = document.getElementById("password");
    var toggleButton = document.querySelector(".toggle-password");

    if (passwordInput.type === "password") {
        passwordInput.type = "text";
        toggleButton.innerHTML = "&#x1f440;"; // Eye icon closed
    } else {
        passwordInput.type = "password";
        toggleButton.innerHTML = "&#x1f441;"; // Eye icon open
    }
}