navigator.mediaDevices.getUserMedia({ video: { width: 900, height: 500 } })

    .then(function (stream) {
        // Mostrar el flujo de la cámara en el elemento de video
        var cameraFeed = document.getElementById('camera-feed');
        cameraFeed.srcObject = stream;
    })
    .catch(function (error) {
        console.error('Error al acceder a la cámara:', error);
    });

// Capturar una imagen al hacer clic en el botón
    var captureButton = document.getElementById('capture-button');
    captureButton.addEventListener('click', function () {
    var cameraFeed = document.getElementById('camera-feed');
    var capturedImage = document.getElementById('captured-image');
    var context = capturedImage.getContext('2d');

    // Configurar el tamaño del lienzo para que coincida con el tamaño de la imagen de la cámara
    capturedImage.width = cameraFeed.videoWidth;
    capturedImage.height = cameraFeed.videoHeight;

    // Dibujar la imagen de la cámara en el lienzo
    context.drawImage(cameraFeed, 0, 0, capturedImage.width, capturedImage.height);

});



// Obtén el token CSRF de la página
var csrfToken = document.querySelector('input[name=csrfmiddlewaretoken]').value;


document.getElementById('capture-button').addEventListener('click', function () {
    var cameraFeed = document.getElementById('camera-feed');
    var capturedImage = document.getElementById('captured-image');
    var context = capturedImage.getContext('2d');

    capturedImage.width = cameraFeed.videoWidth;
    capturedImage.height = cameraFeed.videoHeight;

    context.drawImage(cameraFeed, 0, 0, capturedImage.width, capturedImage.height);

    capturedImage.toBlob(function(blob) {
        var formData = new FormData();
        formData.append('image', blob);
        formData.append('csrfmiddlewaretoken', csrfToken);

        var xhr = new XMLHttpRequest();
        xhr.open('POST', '/cedula/', true);
        xhr.onreadystatechange = function() {
            if (xhr.readyState === 4) {
                if (xhr.status === 200) {
                    var responseText = xhr.responseText;

                    // Parsea la respuesta JSON
                    var responseJson = JSON.parse(responseText);

                    if (responseJson && responseJson.cedula) {
                        // Llena el campo "identificacion" con el número de cédula extraído
                        var identificacionInput = document.getElementById('identificacion').value = responseJson.cedula;
                        if (identificacionInput) {
                            identificacionInput.value = responseJson.cedula;
                        }
                    } else {
                        alert('No se pudo extraer el número de cédula.');
                    }

                    if (responseJson && responseJson.nombres) {
                        // Llena el campo "nombres" con los nombres extraídos
                        var nombresInput = document.getElementById('nombres');
                        if (nombresInput) {
                            nombresInput.value = responseJson.nombres;
                            
                        }
                    } else {
                        console.log('No se pudieron extraer los nombres.');
                    }

                    if (responseJson && responseJson.apellidos) {
                        // Llena el campo "apellidos" con los apellidos extraídos
                        var apellidosInput = document.getElementById('apellidos');
                        if (apellidosInput) {
                            apellidosInput.value = responseJson.apellidos;
                        }
                    } else {
                        console.log('No se pudieron extraer los apellidos.');
                    }
                } else {
                    console.log('Error al procesar la imagen en el servidor.');
                }
            }
        };
        xhr.send(formData);
    }, 'image/jpeg', 0.9);
});


document.getElementById('area_id').addEventListener('change', function () {
    var selectedAreaId = this.value;
    var empleadoDropdown = document.getElementById('id_empleado_id');

    // Si no se selecciona un área, oculta todas las opciones del segundo desplegable y sale del evento
    if (!selectedAreaId) {
        for (var i = 0; i < empleadoDropdown.options.length; i++) {
            empleadoDropdown.options[i].style.display = 'none';
        }
        return;
    }

    // Si se selecciona un área, muestra solo las opciones correspondientes al área seleccionada
    for (var i = 0; i < empleadoDropdown.options.length; i++) {
        var empleadoAreaId = empleadoDropdown.options[i].getAttribute('data-area-id');
        if (empleadoAreaId === selectedAreaId) {
            empleadoDropdown.options[i].style.display = 'block';
        } else {
            empleadoDropdown.options[i].style.display = 'none';
        }
    }
});

// Oculta todas las opciones del segundo desplegable al cargar la página
document.addEventListener('DOMContentLoaded', function () {
    var empleadoDropdown = document.getElementById('id_empleado_id');
    for (var i = 0; i < empleadoDropdown.options.length; i++) {
        empleadoDropdown.options[i].style.display = 'none';
    }
});


