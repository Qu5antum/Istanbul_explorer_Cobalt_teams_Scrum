import { loginUser, registerUser } from "./api.js";

/* ======================
   LOGIN
====================== */
const loginForm = document.querySelector("#loginForm");

if (loginForm) {
    loginForm.addEventListener("submit", async (e) => {
        e.preventDefault();

        const username = document.querySelector("#username").value;
        const password = document.querySelector("#password").value;

        try {
            await loginUser(username, password);
            alert("Giriş başarılı!");
            window.location.href = "index.html";
        } catch (err) {
            console.log(err);
            alert("Giriş başarısız!");
        }
    });
}

/* ======================
   REGISTER
====================== */
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

            alert("Kayıt başarılı!");
            window.location.href = "login.html";

        } catch (err) {
            console.log(err);
            alert("Kayıt başarısız!");
        }
    });
}