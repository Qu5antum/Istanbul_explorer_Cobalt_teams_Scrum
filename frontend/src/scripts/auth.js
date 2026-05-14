import { loginUser, registerUser } from "./api.js";

const loginForm = document.querySelector("#loginForm");
if (loginForm) {
    loginForm.addEventListener("submit", async (e) => {
        e.preventDefault();
        const username = document.querySelector("#username").value;
        const password = document.querySelector("#password").value;
        try {
            await loginUser(username, password);
            window.location.href = "main_page.html";
        } catch (err) {
            console.log(err);
            alert("Giriş başarısız!");
        }
    });
}

const registerForm = document.querySelector("#registerForm");
if (registerForm) {
    registerForm.addEventListener("submit", async (e) => {
        e.preventDefault();
        const email = document.querySelector("#email").value;
        const phone = document.querySelector("#phone").value;
        const password = document.querySelector("#password").value;
        try {
            await registerUser({
                username: email,
                phone_number: phone,
                password: password
            });
            window.location.href = "login.html";
        } catch (err) {
            console.log(err);
            alert("Kayıt başarısız!");
        }
    });
}