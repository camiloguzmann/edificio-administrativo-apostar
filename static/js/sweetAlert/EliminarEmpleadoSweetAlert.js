// En EliminarEmpleadoSweetAlert.js
document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('.eliminar-empleado').forEach(function(btn) {
      btn.addEventListener('click', function(event) {
        event.preventDefault(); // Evita el comportamiento predeterminado del enlace
  
        const empleadoId = this.getAttribute('data-empleado-id');
        DeleteSweet(empleadoId);
      });
    });
  });
  
  async function DeleteSweet(empleado_id) {
    const result = await Swal.fire({
      title: "¿Quieres eliminar este empleado?",
      showDenyButton: true,
      showCancelButton: true,
      confirmButtonText: "Eliminar",
      denyButtonText: "No eliminar"
    });
  
    if (result.isConfirmed) {
    //   const url = "{% url 'eliminar_empleado' empleado_id=0 %}".replace('0', empleado_id);
      const url = `/eliminar_empleado/${empleado_id}/`;

  
      fetch(url, {
        method: 'GET',  // o 'POST' si prefieres usar el método POST
      })
      .then(response => response.json())
      .then(data => {
        Swal.fire("Empleado eliminado correctamente.", "", "success");
        window.location.reload();
      })
      .catch(error => {
        console.error('Error:', error);
        Swal.fire("Hubo un error al intentar eliminar el empleado.", "", "error");
      });
    } else if (result.isDenied) {
      Swal.fire("No se eliminó el empleado.", "", "info");
    }
  }
  