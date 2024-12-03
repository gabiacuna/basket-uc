document.getElementById('id-form').addEventListener('submit', function (e) {
    // console.log('Form submitted');
    // console.log(document.getElementById('id-form')); // Check if form exists
    // console.log(document.getElementById('rut_request')); // Check if input exists
    // console.log(document.getElementById('status-msg')); // Check if status message exists

    e.preventDefault();  // Prevent form submission
    // clear status message
    document.getElementById('status-msg').textContent = 'Validando...';
    document.getElementById('status-msg').className = 'empty';
    
    const userRut = document.getElementById('rut_request').value;
    console.log(userRut);

    const data = {
        rut: userRut,
    };

    const {GoogleAuth} = require('google-auth-library');
    const auth = new GoogleAuth();
    
    fetch('/app/check_id/', {
        method: 'POST',
        body: JSON.stringify(data),
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken'),  // Django CSRF token
            'Authorization': `Bearer ${auth.idToken}`,
        },
    })
    .then(response => response.json())
    .then(data => {
        // console.log(data.status);
        // console.log(data);
        if (data.status === 'valid') {
            document.getElementById('status-msg').textContent = `RUT Valido! Bienvenid@ ${data.name} ${data.last_name}, Tipo de socio: ${data.member_type}`;
            // document.getElementById('status-msg').style.color = 'green';
            document.getElementById('status-msg').className = 'valid';
        } else {
            document.getElementById('status-msg').textContent = `Invalido: No pasa la validación`;
            // document.getElementById('status-msg').style.color = 'red';
            document.getElementById('status-msg').className = 'invalid';
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


// QR Code Scanning

function onScanSuccess(decodedText, decodedResult) {
    // handle the scanned code as you like, for example:
    // console.log(`Code matched = ${decodedText}`, decodedResult);
    // text example: https://portal.sidiv.registrocivil.cl/docstatus?RUN=20677154-2&type=CEDULA&serial=527692739&mrz=527692739601040453104046

    userRut = decodedText.split('=')[1].split('-');
    userRut = userRut[0] + '-' + userRut[1][0];
    
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
        console.log(data.status);
        // console.log(data);
        console.log(data.name);
        console.log(data.member_type);
        if (data.status === 'valid') {
            document.getElementById('status-msg').textContent = `RUT Valido! Bienvenid@ ${data.name} ${data.last_name}, Tipo de socio: ${data.member_type}`;
            // document.getElementById('status-msg').style.color = 'green';
            // document.getElementById('status-msg').style.background = 'green';
            document.getElementById('status-msg').className = 'valid';
        } else {    
            document.getElementById('status-msg').textContent = `Invalido: No pasa la validación`;
            // document.getElementById('status-msg').style.color = 'red';
            document.getElementById('status-msg').className = 'invalid';
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
}

function onScanFailure(error) {
    // if (error != 'QR code parse error') {
    //     console.warn(`Code scan error = ${error}`);
    // }
}

let html5QrcodeScanner = new Html5QrcodeScanner(
    "reader",
    { fps: 10, qrbox: {width: 250, height: 250} },
    /* verbose= */ false);
html5QrcodeScanner.render(onScanSuccess, onScanFailure);