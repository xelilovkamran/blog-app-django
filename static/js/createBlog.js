function showToast(message) {
    Toastify({
        text: message,
        duration: 3000,
        close: true,
        gravity: "top",
        position: "right",
        stopOnFocus: true,
        avatar: avatarURL,
        style: {
            background: "#fff",
            color: "red",
        },
        oldestFirst: false,
    }).showToast();
}

if (error) showToast(error);
