const API_URL = "http://127.0.0.1:8000/api";

export async function registerUser(data) {
    const res = await fetch(`${API_URL}/user/register`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
    });

    if (!res.ok) throw await res.json();

    return res.json();
}

export async function loginUser(username, password) {
    const formData = new URLSearchParams();
    formData.append("username", username);
    formData.append("password", password);

    const res = await fetch(`${API_URL}/user/login`, {
        method: "POST",
        headers: {
            "Content-Type": "application/x-www-form-urlencoded"
        },
        body: formData
    });

    const data = await res.json();

    if (!res.ok) throw data;

    if (data.access_token) {
        localStorage.setItem("token", data.access_token);
    }

    return data;
}
