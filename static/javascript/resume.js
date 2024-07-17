document.addEventListener('DOMContentLoaded', function() {
    const fetchButton = document.getElementById('fetchButton');
    const download = document.getElementById('download');
    const downloadButton = document.getElementById('downloadButton');
    const closeModal = document.getElementsByClassName('close')[0];

    fetchButton.addEventListener('click', function() {
        fetch('/static/resume.pdf')
            .then(response => response.blob())
            .then(blob => {
                const url = window.URL.createObjectURL(blob);

                // Open the download
                download.style.display = "block";

                // Set the download button URL
                downloadButton.onclick = function() {
                    const a = document.createElement('a');
                    a.href = url;
                    a.download = 'resume.pdf'; 
                    document.body.appendChild(a);
                    a.click();
                    document.body.removeChild(a);
                };
            })
            .catch(error => console.error('Error fetching the file:', error));
    });

    // When the user clicks on <span> (x), close the download
    closeModal.onclick = function() {
        download.style.display = "none";
    }

    // When the user clicks anywhere outside of the download, close it
    window.onclick = function(event) {
        if (event.target == download) {
            download.style.display = "none";
        }
    }
});
