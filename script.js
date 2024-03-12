function generateAndDisplayID() {
    // Generate a unique 10-digit Cell ID
    const cellID = Math.random().toString().slice(2,12);
    document.getElementById('display-area').innerHTML = `Cell ID: ${cellID} <br> Barcode: [Simulated Barcode for ${cellID}]`;
    
    // Display the uploaded image
    const imageUpload = document.getElementById('imageUpload');
    if (imageUpload.files.length > 0) {
        const reader = new FileReader();
        reader.onload = function(e) {
            const img = document.createElement('img');
            img.src = e.target.result;
            img.style.width = '200px'; // Example width, adjust as needed
            document.getElementById('display-area').appendChild(img);
        }
        reader.readAsDataURL(imageUpload.files[0]);
    }
}
