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