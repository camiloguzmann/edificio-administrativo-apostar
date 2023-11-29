// // Función para ir a la siguiente página
// function nextPage() {
//   var currentPage = parseInt(getParameterByName('page')) || 1;
//   var nextPage = currentPage + 1;

//   // Verificar si la siguiente página no excede el límite (en este caso, 5)
//   if (nextPage <= 15) {
//     window.location.href = '?page=' + nextPage;
//   }
// };

// // Función para ir a la página anterior
// function previousPage() {
//   var currentPage = parseInt(getParameterByName('page')) || 1;
//   var nextPage = currentPage - 1;

//   // Verificar si la página anterior no es menor que 1
//   if (nextPage >= 1) {
//     window.location.href = '?page=' + nextPage;
//   }
// };

// // Función para obtener el valor de un parámetro en la URL
// function getParameterByName(name) {
//   var url = window.location.href;
//   name = name.replace(/[\[\]]/g, "\\$&");
//   var regex = new RegExp("[?&]" + name + "(=([^&#]*)|&|#|$)"),
//       results = regex.exec(url);
//   if (!results) return null;
//   if (!results[2]) return '';
//   return decodeURIComponent(results[2].replace(/\+/g, ' '));
// };

// // Cuando se carga el contenido del DOM
// document.addEventListener('DOMContentLoaded', function () {
//   // Obtener la página actual
//   var currentPage = parseInt(getParameterByName('page')) || 1;

//   // Obtener todos los elementos de paginación
//   var paginationLinks = document.querySelectorAll('.pagination li');

//   // Remover la clase "active" de todos los elementos de paginación
//   paginationLinks.forEach(function (link) {
//     link.classList.remove('active');
//   });

//   paginationLinks[currentPage].classList.add('active');

//   var previousLink = document.getElementById('previousPage');
//   if (currentPage === 1) {
//     previousLink.classList.add('disabled');
//   } else {
//     previousLink.classList.remove('disabled');
//   };

  
//   // var nextPageLink = document.getElementById('nextPage');
//   // if (currentPage === 5) {
//   //   nextPageLink.classList.add('disabled');
//   // } else {
//   //   nextPageLink.classList.remove('disabled');
//   // }
// });

// Ejemplo de uso básico
Swal.fire('Hello World!');

// Puedes personalizar los botones y el comportamiento
$("#crear").on("click", function() {
  Swal.fire({
    title: '¿Estás seguro?',
    text: '¡No podrás revertir esto!',
    icon: 'warning',
    showCancelButton: true,
    confirmButtonText: 'Sí, eliminarlo',
    cancelButtonText: 'No, cancelar',
  }).then((result) => {
    if (result.isConfirmed) {
      // Aquí puedes hacer la acción que desees después de confirmar
      $("#visitante").submit();
    }
  });
});