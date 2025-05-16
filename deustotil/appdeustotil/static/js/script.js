document.addEventListener('DOMContentLoaded', () => {
    const nombreInput = document.getElementById('id_nombre');
    const apellidosInput = document.getElementById('id_apellidos');
    const emailInput = document.getElementById('id_email');

    function generarEmail() {
        const nombre = nombreInput.value.trim().toLowerCase();
        const apellido = apellidosInput.value.trim().split(" ")[0].toLowerCase();
        if (nombre && apellido) {
            emailInput.value = `${nombre}.${apellido}@deustotil.com`;
        }
    }

    nombreInput.addEventListener('input', generarEmail);
    apellidosInput.addEventListener('input', generarEmail);
});

