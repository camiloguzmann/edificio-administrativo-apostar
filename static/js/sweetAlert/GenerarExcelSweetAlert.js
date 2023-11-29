function validarCampos() {
    // Obtén los valores de los campos
    var tipo = document.getElementById('tipo').value;
    var EFI = document.getElementById('EFI').value;
    var EFF = document.getElementById('EFF').value;

    // Verifica si todos los campos están llenos
    if (tipo === '' || EFI === '' || EFF === '') {
        // Si falta algún dato, muestra el Sweet Alert
        Swal.fire({
            title: "Error",
            text: "Por favor, completa todos los campos.",
            icon: "error"
        });
        // Devuelve falso para evitar que se ejecute ExcelSweet()
        return false;
    }

    return true;
}

function ExcelSweet() {
    if (validarCampos()) {
        Swal.fire({
            title: "Felicitaciones",
            text: "Generaste El reporte de salidas de excel!",
            icon: "success"
        });
    }
}
