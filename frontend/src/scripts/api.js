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

export async function getPlaceById(
    placeId,
    lat,
    lng
) {
    return request(`/place/${placeId}`, {
        method: "POST",
        headers: {
            ...getHeaders(null),
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            lat,
            lng
        })
    });
}

/* =========================
   COMMENTS
========================= */

export async function getPlaceComments(placeId) {
    return request(`/place/${placeId}/comment/`, {
        headers: getHeaders(null)
    });
}

export async function createComment(placeId, title) {
    return request(`/place/${placeId}/comment/create/`, {
        method: "POST",
        headers: getHeaders(),
        body: JSON.stringify({
            title
        })
    });
}

/* =========================
   FAVORITES
========================= */

export async function addPlaceToFavorites(placeId) {
    return request(`/place/${placeId}/favorite`, {
        method: "POST",
        headers: getHeaders(null)
    });
}

/* =========================
   FAVORITES
========================= */

export async function getFavoritePlaces() {
    return request("/user/favorites", {
        headers: getHeaders(null)
    });
}

export async function removeFavoritePlace(placeId) {
    return request(`/place/${placeId}/favorite`, {
        method: "DELETE",
        headers: getHeaders(null)
    });
}

/* =========================
   NEARBY PLACES
========================= */
export async function getNearbyPlaces(lat, lng) {
    return request("/place/nearby", {
        method: "POST",
        headers: getHeaders(),
        body: JSON.stringify({
            lat: lat,
            lng: lng
        })
    });
}

/* =========================
   NEARBY BY CATEGORY
========================= */

export async function getNearbyPlacesByCategory(
    categoryId,
    lat,
    lng
) {
    return request(
        `/place/nearby/category/${categoryId}`,
        {
            method: "POST",
            headers: getHeaders(),
            body: JSON.stringify({
                lat: lat,
                lng: lng
            })
        }
    );
}

/* Place Rating */

export async function ratePlace(placeId, rating) {
    return request(`/place/${placeId}/rate`, {
        method: "POST",
        headers: getHeaders(),
        body: JSON.stringify({ rating })
    });
}

export async function getPlaceRating(placeId) {
    return request(`/place/${placeId}/rating`, {headers: getHeaders(null)});
}


/* =========================
   GET ALL ROUTES
========================= */
export async function getRoutes() {
    return request(
        "/route/all",
        {
            method: "GET",
            headers: getHeaders()
        }
    );
}

/* =========================
   GET ROUTE PLACES
========================= */

export async function getRoutePlaces(
    routeId
) {
    return request(
        `/route/${routeId}/route_places`,
        {
            method: "GET",
            headers: getHeaders()
        }
    );
}

/* =========================
   GENERATE ROUTE
========================= */

export async function generateRoute(data) {

    return request("/route/generate", {
        method: "POST",
        headers: getHeaders(),
        body: JSON.stringify(data)
    });
}

/* delete route */
export async function deleteRoute(routeId) {
    return request(`/route/${routeId}/delete`, {
        method: "DELETE",
        headers: getHeaders()
    });
}

export async function getSharedRoute(routeToken) {
    return request(`/route/${routeToken}/shared`, {
        headers: getHeaders()
    });
}