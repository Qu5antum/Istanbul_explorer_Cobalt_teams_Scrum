import axios from "axios";

const API = axios.create({
    baseURL: "http://127.0.0.1:8000/api",
    headers: {
        "Content-Type": "application/json",
    },
});


// ======================
// REGISTER
// ======================

export const registerUser = async (userData) => {
    try {
        const response = await API.post("/user/register", userData);
        return response.data;
    } catch (error) {
        throw error.response?.data || error;
    }
};
import { registerUser } from "./api.js";

const form = document.querySelector("form");

form.addEventListener("submit", async (e) => {
    e.preventDefault();

    const username = document.querySelector("#username").value;
    const email = document.querySelector("#email").value;
    const password = document.querySelector("#password").value;

    const userData = {
        username,
        email,
        password,
    };

    try {
        const result = await registerUser(userData);

        alert("Kayıt başarılı!");

        window.location.href = "login.html";

    } catch (error) {
        console.log(error);

        alert("Kayıt başarısız!");
    }
});


// ======================
// LOGIN
// ======================

export const loginUser = async (username, password) => {
    try {
        const formData = new URLSearchParams();

        formData.append("username", username);
        formData.append("password", password);

        const response = await API.post(
            "/user/login",
            formData,
            {
                headers: {
                    "Content-Type": "application/x-www-form-urlencoded",
                },
            }
        );

        if (response.data.access_token) {
            localStorage.setItem(
                "access_token",
                response.data.access_token
            );
        }

        return response.data;
    } catch (error) {
        throw error.response?.data || error;
    }
};

import { loginUser } from "./api.js";

constform = document.querySelector("form");

form.addEventListener("submit", async (e) => {

    e.preventDefault();

    const username = document.querySelector("#username").value;

    const password = document.querySelector("#password").value;

    try {

        const result = await loginUser(username, password);

        console.log(result);

        alert("Giriş başarılı!");

        window.location.href = "index.html";

    } catch (error) {

        console.log(error);

        alert("Giriş başarısız!");
    }
});


// ======================
// AUTH HEADER
// ======================

export const getAuthHeader = () => {
    const token = localStorage.getItem("access_token");

    return {
        headers: {
            Authorization: `Bearer ${token}`,
        },
    };
};