// Función para mostrar una alerta básica

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

// Código anterior para la captura de cédula...

$(document).ready(function() {
    $('#capture-button').click(function() {
        // Lógica para obtener los datos del visitante
        obtenerDatosVisitante();
    });
});

function obtenerDatosVisitante() {
    var cedula = $('#identificacion').val();
    

    // Verificar si la cédula ya existe
    $.get('/obtener_datos_visitante/' + cedula + '/', function(data) {
        // Comprobar si se encontraron datos
        if (data && data.existe) {
            // Rellenar los campos con los datos existentes
            $('#nombres').val(data.nombres);
            $('#apellidos').val(data.apellidos);
            $('#celular').val(data.celular);
            // Puedes agregar más campos según tus necesidades

            console.log('Datos del visitante encontrados:', data);
        } else {
            // Si no hay datos existentes, realizar la solicitud AJAX normalmente
            // Puedes utilizar la información capturada de la cámara u otros datos relevantes
            $.ajax({
                url: '/edificio/visitantes/',  // Reemplaza con la URL correcta de tu backend
                method: 'POST',
                data: {
                    imagen: $('#imagen').val(),  // Puedes enviar la imagen u otros datos necesarios
                    // Agrega más campos según tus necesidades
                },
                success: function(response) {
                    // Manejar la respuesta del servidor (puede ser un JSON con los datos del visitante)
                    console.log(response);
                    // Aquí puedes actualizar la interfaz de usuario con los datos obtenidos
                    // Por ejemplo, puedes mostrar la información en algún lugar de tu página
                },
                error: function(jqXHR, textStatus, errorThrown) {
                    console.error('Error al obtener datos del visitante:', textStatus, errorThrown);
                }
            });
        }
    }).fail(function(jqXHR, textStatus, errorThrown) {
        console.error('Error en la solicitud de datos del visitante:', textStatus, errorThrown);
    });
}


var csrfToken = document.querySelector('input[name=csrfmiddlewaretoken]').value;

// Función para la captura de cédula y obtención de datos del visitante
function capturarYObtenerDatosVisitante() {
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
                        return;  // Detén la ejecución si no se puede extraer la cédula
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

                    // Ahora, llama a la función para obtener datos del visitante
                    obtenerDatosVisitante();
                } else {
                    console.log('Error al procesar la imagen en el servidor.');
                }
            }
        };
        xhr.send(formData);
    }, 'image/jpeg', 0.9);
}

// Agrega el evento de clic al botón de captura
document.getElementById('capture-button').addEventListener('click', function () {
    capturarYObtenerDatosVisitante();
});

