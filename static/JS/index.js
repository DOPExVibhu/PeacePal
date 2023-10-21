function sendMessage() {
    var userMessage = document.getElementById("user-input").value;
    var chatBox = document.getElementById("chat-box");

    // Display the user's message in the chat
    var userMessageDiv = document.createElement("div");
    userMessageDiv.className = "chat-message user-message";
    userMessageDiv.textContent = userMessage;
    chatBox.appendChild(userMessageDiv);

    // Make an AJAX request to get the bot's response
    fetch("/chat", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ user_input: userMessage }),
    })
    .then(response => {
        if (!response.ok) {
            throw new Error("Network response was not ok");
        }
        return response.json();
    })
    .then(data => {
        var botResponseDiv = document.createElement("div");
        botResponseDiv.className = "chat-message bot-message";
        botResponseDiv.textContent = data.response;
        chatBox.appendChild(botResponseDiv);
    })
    .catch(error => {
        console.error("Error fetching the chatbot response:", error);
        var errorResponseDiv = document.createElement("div");
        errorResponseDiv.className = "chat-message bot-message";
        errorResponseDiv.textContent = "Sorry, there was an error. Please try again later.";
        chatBox.appendChild(errorResponseDiv);
    });

    // Clear the user input field
    document.getElementById("user-input").value = "";
}

// Remove the reference to the regenerateResponse() since it's not defined
