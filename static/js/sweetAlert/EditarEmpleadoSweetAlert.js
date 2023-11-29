document.addEventListener("DOMContentLoaded", function () {
    // Selecciona el formulario por su ID
    const form = document.getElementById("demo-form2");
  
    // Agrega un evento al formulario cuando se envía
    form.addEventListener("submit", function (event) {
      event.preventDefault(); // Previene el envío del formulario por defecto
  
      // Configura los datos del formulario para la petición AJAX
      const formData = new FormData(form);
  
      // Realiza la petición AJAX
      $.ajax({
        url: form.action,
        type: form.method,
        data: formData,
        processData: false,
        contentType: false,
        success: function (response) {
          // Muestra un SweetAlert con la respuesta del servidor
          Swal.fire({
            title: response.title,
            text: response.message,
            icon: response.icon,
          }).then(() => {
            // Puedes agregar acciones adicionales después de cerrar el SweetAlert
            if (response.success && response.redirect_url) {
              window.location.href = response.redirect_url;
            } else {
              window.location.reload(); // Recarga la página después de cerrar
            }
          });
        },
        error: function (error) {
          // Maneja el error si es necesario
          console.error(error);
        },
      });
    });
  });
  
  