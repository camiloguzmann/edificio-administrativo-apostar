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
                        var identificacionInput = document.getElementById('identificacion');
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

$(document).ready(function () {
    $('#id_dependencia_id').change(function () {
        var dependenciaId = $(this).val();
        $.ajax({
            url: '/visitantes/create/' + dependenciaId + '/',
            success: function (data) {
                $('#id_empleado_id').html(data);
            }
        });
    });
});