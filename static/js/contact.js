document.getElementById("contactForm").addEventListener("submit", function (e) {
    e.preventDefault();
    const subject = document.getElementById("subject");
    const message = document.getElementById("message");
    const mailtoLink = `mailto:${receiverEmail}?subject=${encodeURIComponent(
        subject.value
    )}&body=${encodeURIComponent(message.value)}`;
    window.location.href = mailtoLink;
    setTimeout(() => {
        subject.value = "";
        message.value = "";
    }, 1000);
});
