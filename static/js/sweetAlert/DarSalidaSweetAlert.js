document.addEventListener("DOMContentLoaded", function () {
  // Selecciona los formularios por su clase
  const forms = document.querySelectorAll(".salida-form");

  forms.forEach((form) => {
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
          // Muestra el SweetAlert según la información proporcionada en la respuesta
          if (response.success) {
            Swal.fire({
              title: response.title,
              text: response.text,
              icon: response.icon,
              showCancelButton: response.showCancelButton || false,
              confirmButtonColor: response.confirmButtonColor || "#d33",
              cancelButtonColor: response.cancelButtonColor || "#3085d6",
              confirmButtonText: response.confirmButtonText || "OK",
              cancelButtonText: response.cancelButtonText || "Cancelar",
            }).then(() => {
              // Puedes agregar acciones adicionales después de cerrar el SweetAlert
              window.location.reload(); // Recarga la página después de cerrar
            });
          } else {
            // Muestra un SweetAlert de advertencia si success es False
            Swal.fire({
              title: response.title,
              text: response.text,
              icon: response.icon,
            });
          }
        },
        error: function (error) {
          // Maneja el error si es necesario
          console.error(error);
        },
      });
    });
  });
});
