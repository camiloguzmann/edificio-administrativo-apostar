// En EliminarEmpleadoSweetAlert.js
document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('.eliminar-usuario').forEach(function(btn) {
      btn.addEventListener('click', function(event) {
        event.preventDefault(); // Evita el comportamiento predeterminado del enlace
  
        const usuarioId = this.getAttribute('data-usuario-id');
        DeleteSweet(usuarioId);
      });
    });
  });
  
  async function DeleteSweet(usuario_id) {
    const result = await Swal.fire({
      title: "¿Quieres eliminar este usuario?",
      showDenyButton: true,
      showCancelButton: true,
      confirmButtonText: "Eliminar",
      denyButtonText: "No eliminar"
    });
  
    if (result.isConfirmed) {
    //   const url = "{% url 'eliminar_usuario' usuario_id=0 %}".replace('0', usuario_id);
      const url = `/eliminar_usuario/${usuario_id}/`;

  
      fetch(url, {
        method: 'GET',  // o 'POST' si prefieres usar el método POST
      })
      .then(response => response.json())
      .then(data => {
        Swal.fire("Usuario eliminado correctamente.", "", "success");
        window.location.reload();
      })
      .catch(error => {
        console.error('Error:', error);
        Swal.fire("Hubo un error al intentar eliminar el usuario.", "", "error");
      });
    } else if (result.isDenied) {
      Swal.fire("No se eliminó el Usuario.", "", "info");
    }
  }
  