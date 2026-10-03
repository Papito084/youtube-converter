async function convertVideo() {
    const urlInput = document.getElementById('urlInput');
    const convertBtn = document.getElementById('convertBtn');
    const loader = document.getElementById('loader');
    const result = document.getElementById('result');
    const error = document.getElementById('error');
    const errorMsg = document.getElementById('errorMsg');
    const videoTitle = document.getElementById('videoTitle');
    const downloadLink = document.getElementById('downloadLink');

    const url = urlInput.value.trim();
    const format = document.querySelector('input[name="format"]:checked').value;

    if (!url) {
        showError('Please enter a valid YouTube URL');
        return;
    }

    // Reset UI
    error.classList.add('hidden');
    result.classList.add('hidden');
    loader.classList.remove('hidden');
    document.getElementById('statusArea').classList.remove('hidden');
    convertBtn.disabled = true;
    convertBtn.style.opacity = '0.7';

    try {
        const response = await fetch('/convert', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ url: url, format: format }),
        });

        const data = await response.json();

        if (response.ok) {
            videoTitle.textContent = data.title;
            downloadLink.href = `/download/${encodeURIComponent(data.filename)}`;
            result.classList.remove('hidden');
        } else {
            showError(data.error || 'An error occurred during conversion');
        }
    } catch (err) {
        showError('Failed to connect to the server');
        console.error(err);
    } finally {
        loader.classList.add('hidden');
        convertBtn.disabled = false;
        convertBtn.style.opacity = '1';
    }
}

function showError(message) {
    const error = document.getElementById('error');
    const errorMsg = document.getElementById('errorMsg');
    const statusArea = document.getElementById('statusArea');

    errorMsg.textContent = message;
    error.classList.remove('hidden');
    statusArea.classList.remove('hidden');
}

// Allow Enter key to submit
document.getElementById('urlInput').addEventListener('keypress', function (e) {
    if (e.key === 'Enter') {
        convertVideo();
    }
});
