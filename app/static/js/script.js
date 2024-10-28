document.getElementById('id-form').addEventListener('submit', function (e) {
    // console.log('Form submitted');
    // console.log(document.getElementById('id-form')); // Check if form exists
    // console.log(document.getElementById('rut_request')); // Check if input exists
    // console.log(document.getElementById('status-msg')); // Check if status message exists

    e.preventDefault();  // Prevent form submission

    const userRut = document.getElementById('rut_request').value;
    // console.log(userRut);

    const data = {
        rut: userRut,
    };
    
    fetch('/app/check_id/', {
        method: 'POST',
        body: JSON.stringify(data),
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken')  // Django CSRF token
        },
    })
    .then(response => response.json())
    .then(data => {
        // console.log(data.status);
        // console.log(data);
        if (data.status === 'valid') {
            document.getElementById('status-msg').textContent = `Status: ${data.status}, Member Type: ${data.member_type}`;
        } else {
            document.getElementById('status-msg').textContent = `Status: ${data.status}`;
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
});

// Get CSRF Token Function
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}


// QR Code Scanning (optional)
navigator.mediaDevices.getUserMedia({ video: { facingMode: "environment" } }).then(function (stream) {
    const video = document.getElementById('preview');
    video.srcObject = stream;
    video.setAttribute("playsinline", true);  // iOS compatibility
    video.play();
});
