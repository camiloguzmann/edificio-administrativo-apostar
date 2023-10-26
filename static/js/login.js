function toggleUsuario(inputElement) {
    const usuarioHelper = document.querySelector('.inputGroup1 .helper1');

    if (inputElement.value.length > 0) {
        // Si el cuadro de entrada de usuario no está vacío, oculta el texto de ayuda
        usuarioHelper.style.display = 'none';
    } else {
        // Si el cuadro de entrada de usuario está vacío, muestra el texto de ayuda
        usuarioHelper.style.display = 'block';
    }
}
// Agregar un evento 'submit' al formulario para la redirección
document.getElementById('loginForm').addEventListener('submit', function (e) {
    e.preventDefault(); // Evitar que el formulario se envíe normalmente
    window.location.href = '/Portal.html'; // Redirigir a la página "Portal"
});
// function validateForm() {
// var user = document.getElementById("email").value;
// var password = document.getElementById("password").value;

// if (user === "" || password === "") {
//     alert("Por favor complete todos los campos");
//     return false;
// } else if (user === "1" && password === "1") {
//     window.location.href = "index.html";
//    alert("Bienvenido");                
// } else {
//     alert("Usuario o contraseña incorrectos");
//     return false;
// }
// }