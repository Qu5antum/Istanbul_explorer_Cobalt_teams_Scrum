const categories = [
  {
    id: 1,
    title: "all",
  },
  {
    id: 2,
    title: "park",
  },
  {
    id: 3,
    title: "museum",
  },
  {
    id: 4,
    title: "mosque",
  },
];

const places = [
  {
    id: 1,
    title: "Hagia Sophia",
    category: "mosque",
    price: "1400-1800₺",
    latitude: 41.008,
    longitude: 28.98,
    description: "İstanbul’un en önemli tarihi yapılarından biri.",
    address: "Fatih / İstanbul",
    image:
      "https://images.unsplash.com/photo-1634720433737-8f57f2f23d64?q=80&w=1200&auto=format&fit=crop",
    link: "https://maps.google.com",
  },

  {
    id: 2,
    title: "Gülhane Parkı",
    category: "park",
    price: "Ücretsiz",
    latitude: 41.012,
    longitude: 28.981,
    description: "Şehir merkezinde doğa ile iç içe park.",
    address: "Fatih / İstanbul",
    image:
      "https://images.unsplash.com/photo-1506744038136-46273834b3fb?q=80&w=1200&auto=format&fit=crop",
    link: "https://maps.google.com",
  },

  {
    id: 3,
    title: "Topkapı Sarayı",
    category: "museum",
    price: "950₺",
    latitude: 41.011,
    longitude: 28.983,
    description: "Osmanlı döneminden tarihi saray.",
    address: "Fatih / İstanbul",
    image:
      "https://images.unsplash.com/photo-1544735716-392fe2489ffa?q=80&w=1200&auto=format&fit=crop",
    link: "https://maps.google.com",
  },
];

const cardsContainer = document.getElementById("cards");
const categoriesContainer = document.getElementById("categories");
const searchInput = document.getElementById("searchInput");

function renderCategories() {
  categoriesContainer.innerHTML = "";

  categories.forEach((category) => {
    const button = document.createElement("button");

    button.className = "category-btn";

    button.innerText = category.title;

    if (category.title === "all") {
      button.classList.add("active");
    }

    button.addEventListener("click", () => {
      document
        .querySelectorAll(".category-btn")
        .forEach((btn) => btn.classList.remove("active"));

      button.classList.add("active");

      if (category.title === "all") {
        renderPlaces(places);
      } else {
        const filtered = places.filter(
          (place) => place.category === category.title,
        );

        renderPlaces(filtered);
      }
    });

    categoriesContainer.appendChild(button);
  });
}

function renderPlaces(data) {
  cardsContainer.innerHTML = "";

  data.forEach((place) => {
    const card = document.createElement("div");

    card.className = "card";

    card.innerHTML = `
    
      <div class="card-image">

        <img src="${place.image}" />

        <div class="tag">
          ${place.category}
        </div>

        <div class="price">
          ${place.price}
        </div>

        <button class="save-btn">
          ❤
        </button>

      </div>


      <div class="card-content">

        <div class="location">
          📍 ${place.address}
        </div>

        <div class="card-title">
          ${place.title}
        </div>

        <div class="description">
          ${place.description}
        </div>

        <div class="card-footer">

          <div>
            ${place.latitude}
            <br>
            ${place.longitude}
          </div>

          <button
            class="go-btn"
            onclick="window.open('${place.link}')"
          >
            →
          </button>

        </div>

      </div>

    `;

    cardsContainer.appendChild(card);
  });
}

searchInput.addEventListener("keyup", (e) => {
  const value = e.target.value.toLowerCase();

  const filtered = places.filter(
    (place) =>
      place.title.toLowerCase().includes(value) ||
      place.category.toLowerCase().includes(value),
  );

  renderPlaces(filtered);
});

renderCategories();
renderPlaces(places);
