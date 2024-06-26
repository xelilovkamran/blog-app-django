async function getTemperature(cityName, API_KEY) {
    try {
        const URL = `https://api.openweathermap.org/data/2.5/weather?q=${cityName}&appid=${API_KEY}&units=metric`;
        const response = await fetch(URL);
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        const data = await response.json();
        return data;
    } catch (error) {
        window.alert(error.message);
    }
}

document.addEventListener("DOMContentLoaded", async () => {
    const navList = document.querySelector(".nav-right");
    const temperatureData = await getTemperature(
        "Baku",
        "eeb9d0aadd6bdfd0f0194aba3c64ed29"
    );
    const li = document.createElement("li");
    li.classList.add("nav-item", "fw-bold");
    li.innerHTML = `<a class="nav-link" href="#">${temperatureData.main.temp}°C</a>`;
    navList.insertBefore(li, navList.firstChild);
});
