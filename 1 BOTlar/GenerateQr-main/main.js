async function postData() {
    const form = document.getElementById("apiForm");
    const formData = new FormData(form);

    const response = await fetch('http://omonullo.uz:8081/qr/', {
        method: 'POST',
        body: JSON.stringify(Object.fromEntries(formData.entries())),
        headers: {
            'Content-Type': 'application/json'
        }
    });

    const responseData = await response.json();
    document.getElementById("response").innerHTML = `<img src="${responseData['url']}" alt="QR Code"> <button id="downloadButton" onclick="downloadQR('${responseData['url']}')">Download QR Code</button>`;
}

async function downloadQR(url) {
    const filename = document.getElementById("text_prompt").value;
    const response = await fetch(url);
    const blob = await response.blob();
    const downloadUrl = window.URL.createObjectURL(blob);

    const a = document.createElement("a");
    a.href = downloadUrl;
    a.download = filename + ".jpg";
    document.body.appendChild(a);
    a.click();
    window.URL.revokeObjectURL(downloadUrl);
}

