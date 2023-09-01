console.log('scripts.js loaded');

document.getElementById("file-input").addEventListener("change", function () {
    const fileNameDisplay = document.getElementById("file-name-display");
    const fileName = this.files[0].name;
    fileNameDisplay.textContent = `Selected file: ${fileName}`;
});