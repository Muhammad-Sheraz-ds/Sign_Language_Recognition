document.addEventListener("DOMContentLoaded", function () {
    const imageInput = document.getElementById("imageInput");
    const previewImage = document.getElementById("previewImage");
    const predictButton = document.getElementById("predictButton");
    const resultDiv = document.getElementById("result");

    predictButton.disabled = true;

    imageInput.addEventListener("change", function () {
        const file = imageInput.files[0];
        if (file) {
            const reader = new FileReader();
            reader.onload = function (e) {
                previewImage.src = e.target.result;
                previewImage.style.display = "block";
            };
            reader.readAsDataURL(file);
            predictButton.disabled = false;
        } else {
            previewImage.src = "";
            previewImage.style.display = "none";
            predictButton.disabled = true;
        }
    });

    document.getElementById("uploadForm").addEventListener("submit", async function (event) {
        event.preventDefault();

        const file = imageInput.files[0];
        if (!file) {
            alert("Please select an image.");
            return;
        }

        const formData = new FormData();
        formData.append("file", file);

        try {
            const response = await fetch("http://127.0.0.1:5000/predict", {
                method: "POST",
                body: formData,
            });

            const data = await response.json();
            if (response.ok) {
                resultDiv.innerHTML = `Predicted Gesture: <span>${data.prediction}</span>`;
                resultDiv.style.color = "green";
            } else {
                resultDiv.innerHTML = `<span>Error: ${data.error}</span>`;
                resultDiv.style.color = "red";
            }
        } catch (error) {
            console.error("Error:", error);
            resultDiv.innerHTML = `<span class="text-danger">Failed to connect to the backend.</span>`;
        }
    });
});
