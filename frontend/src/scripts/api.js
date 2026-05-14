const API_URL = "http://127.0.0.1:8000/api";

function getToken() {
    return localStorage.getItem("token");
}

function getHeaders(contentType = "application/json") {
    const headers = {};

    if (contentType) {
        headers["Content-Type"] = contentType;
    }

    const token = getToken();

    if (token) {
        headers["Authorization"] = `Bearer ${token}`;
    }

    return headers;
}

async function request(endpoint, options = {}) {
    const response = await fetch(`${API_URL}${endpoint}`, options);

    const data = await response.json();

    if (!response.ok) {
        throw new Error(data.detail || "Bir hata oluştu");
    }

    return data;
}

/* =========================
   AUTH
========================= */

export async function registerUser(userData) {
    return request("/user/register", {
        method: "POST",
        headers: getHeaders(),
        body: JSON.stringify(userData)
    });
}

export async function loginUser(username, password) {
    const formData = new URLSearchParams();

    formData.append("username", username);
    formData.append("password", password);

    const data = await request("/user/login", {
        method: "POST",
        headers: getHeaders("application/x-www-form-urlencoded"),
        body: formData
    });

    if (data.access_token) {
        localStorage.setItem("token", data.access_token);
    }

    return data;
}

/* =========================
   CATEGORY
========================= */

export async function getCategories() {
    return request("/category", {
        headers: getHeaders(null)
    });
}

/* =========================
   PLACES
========================= */

export async function getAllPlaces() {
    return request("/place/all", {
        headers: getHeaders(null)
    });
}

export async function getPlacesByCategory(categoryId) {
    return request(`/category/${categoryId}`, {
        headers: getHeaders(null)
    });
}

export async function searchPlace(title) {
    return request(`/search/${encodeURIComponent(title)}`, {
        headers: getHeaders(null)
    });
}

export async function getPlaceById(placeId) {
    return request(`/place/${placeId}`, {
        headers: getHeaders(null)
    });
}