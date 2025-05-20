document.addEventListener('DOMContentLoaded', () => {
    //inputs del formulario empleado
    const nombreInput = document.getElementById('id_nombre');
    const apellidosInput = document.getElementById('id_apellidos');
    const emailInput = document.getElementById('id_email');

    // inputs del formulario proyecto
    const proyectoNomInput = document.getElementById('proyecto_nombre');
    const proyectoFechaInput = document.getElementById('proyecto_fecha_inicio');
    const proyectoCodigoInput = document.getElementById('proyecto_codigo');

    function generarEmail() {
        const nombre = nombreInput.value.trim().toLowerCase();
        const apellido = apellidosInput.value.trim().split(" ")[0].toLowerCase();
        if (nombre && apellido) {
            emailInput.value = `${nombre}.${apellido}@deustotil.com`;
        }
    }

    function generarCodigoProyecto() {
        const nombreProyecto = proyectoNomInput.value.trim().toUpperCase();
        var fecha = proyectoFechaInput.value;
        fecha = fecha.replace('-', '/');

        if (nombreProyecto && fecha) {
            proyectoCodigoInput.value = `${nombreProyecto}_${fecha}`;
        }
    }

    nombreInput.addEventListener('input', generarEmail);
    apellidosInput.addEventListener('input', generarEmail);
    proyectoNomInput.addEventListener('input', generarCodigoProyecto);
    proyectoFechaInput.addEventListener('input', generarCodigoProyecto);

    function cambiarEstado(tareaId) {
        fetch('/cambiar_estado/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken') 
            },
            body: JSON.stringify({
                id: tareaId,
                estado: 'completado'
            })
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                document.getElementById('estado-' + tareaId).textContent = data.estado;
            } else {
            alert('Error al actualizar estado');
            }
        });
    }
    const estadoButton = document.getElementById('boton-estado');
    estadoButton.addEventListener('click', cambiarEstado);

    
});
