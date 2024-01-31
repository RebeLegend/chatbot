// Event listener for DOM content load
document.addEventListener('DOMContentLoaded', function() {
    // Set a default welcome message
    document.getElementById('response').innerText = 'Hello! Ask me a cybersecurity question.';
});

// Function to send user message to the Flask server and handle the response
function sendMessage() {
    var userMessage = document.getElementById('user_input').value;
    fetch('/get_response', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ message: userMessage }),
    })
    .then(response => response.json())
    .then(data => {
        // Display the response
        document.getElementById('response').innerText = data.response;
    })
    .catch((error) => {
        // Error handling
        console.error('Error:', error);
        document.getElementById('response').innerText = 'Error: Could not retrieve response';
    });
}
