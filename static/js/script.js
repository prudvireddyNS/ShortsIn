document.getElementById('generate-form').addEventListener('submit', function(event) {
    event.preventDefault();

    const topic = document.getElementById('topic').value;
    const messageDiv = document.getElementById('message');
    const downloadLink = document.getElementById('download-link');
    const downloadAnchor = document.getElementById('download');

    messageDiv.textContent = 'Generating... Please wait.';
    downloadLink.style.display = 'none';

    fetch('/generate_short', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ topic: topic }),
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            messageDiv.textContent = `Error: ${data.error}`;
        } else {
            messageDiv.textContent = 'Short generated successfully!';
            // Assuming the generated video file is named 'final_output_video_0.mp4'
            downloadAnchor.href = '/download/video.mp4';
            downloadLink.style.display = 'block';
        }
    })
    .catch(error => {
        console.error('Error:', error);
        messageDiv.textContent = 'An error occurred while generating the short.';
    });
});
