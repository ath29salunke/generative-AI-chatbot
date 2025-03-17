async function sendMessage() {
    let userInput = document.getElementById("user-input").value;
    if (!userInput.trim()) return;

    let chatBox = document.getElementById("chat-box");
    chatBox.innerHTML += `<p><strong>You:</strong> ${userInput}</p>`;

    document.getElementById("user-input").value = "";

    let response = await fetch("http://127.0.0.1:5000/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: userInput }),
    });

    let data = await response.json();
    chatBox.innerHTML += `<p><strong>Bot:</strong> ${data.response}</p>`;
    chatBox.scrollTop = chatBox.scrollHeight;
}
