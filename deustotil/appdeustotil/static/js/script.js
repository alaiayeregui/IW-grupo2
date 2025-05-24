document.addEventListener('DOMContentLoaded', () => {
    //inputs del formulario empleado
    const nombreInput = document.getElementById('id_nombre');
    const apellidosInput = document.getElementById('id_apellidos');
    const emailInput = document.getElementById('id_email');

    // inputs del formulario cliente
    const clienteNombreInput = document.getElementById('cliente_nombre');
    const clienteCIFInput = document.getElementById('cliente_CIF');
    const clienteDireccionInput = document.getElementById('cliente_direccion');
    const clientePersonaContactoInput = document.getElementById('cliente_persona_contacto');
    const clienteEmailContactoInput = document.getElementById('cliente_email_contacto');
    const clienteNumContactoInput = document.getElementById('cliente_num_contacto');

    function generarEmail() {
        const nombre = nombreInput.value.trim().toLowerCase();
        const apellido = apellidosInput.value.trim().split(" ")[0].toLowerCase();
        if (nombre && apellido) {
            emailInput.value = `${nombre}.${apellido}@deustotil.com`;
        }
    }

    if (nombreInput != null){
        nombreInput.addEventListener('input', generarEmail);
        apellidosInput.addEventListener('input', generarEmail);
    }

    function validarCliente(){
        let nombre = clienteNombreInput.value.trim();
        if (nombre != null && nombre != ""){
            // Expresión regular: una mayúscula seguida de solo letras minúsculas
            let regex = /^[A-Z][a-z]+$/;

            if (regex.test(nombre)) {
                //Comprobamos si no hay error, se podria comentar mas adelante
                console.log("Nombre válido");
            } else {
                alert("El nombre tiene que empezar por mayuscula y solo contener letras");
            }
        }
        let cif = clienteCIFInput.value.trim();
        if (cif != null && cif != ""){
            let regex = /^[A-Z][0-9]+$/;
            if (regex.test(cif)){
                 //Comprobamos si no hay error, se podria comentar mas adelante
                console.log("CIF válido");
            } else {
                alert("El CIF tiene que empezar por mayuscula y solo contener numeros despues");
            }
        }
        let direccion = clienteDireccionInput.value.trim().toLowerCase();
        //Tengo que mirarlo despacio
        let personaContacto = clientePersonaContactoInput.value;
        if (personaContacto != null && personaContacto != ""){
            let regex = /^[A-Z][a-z]+ [A-Z][a-z]+$/;

            if (personaContacto !== "") {
                if (regex.test(personaContacto)) {
                    console.log("Es valido");
                } else {
                    alert("Debe ingresar nombre y apellido con la primera letra en mayúscula.");
                }
            }
        }
        let emailContacto = clienteEmailContactoInput.value.toLowerCase();
        let emailSinEspacios = emailContacto.trim();
        if (emailContacto != null && emailContacto != ""){
            if (emailContacto == emailSinEspacios){
                if (emailContacto.endsWith(".es") || emailContacto.endsWith(".com")){
                        console.log("Es valido");
                } else {
                    alert("El correo no finaliza con .es o .com");
                }
            } else {
                alert("El email no debe contener espacios.");
            }
        }
        let numContacto = clienteNumContactoInput.value.trim().toLowerCase();
        if (numContacto != null && numContacto != ""){
            let regex = /^[0-9]+$/;
            if (regex.test(numContacto)){
                 //Comprobamos si no hay error, se podria comentar mas adelante
                console.log("El numero de contacto es válido");
            } else {
                alert("El numero del contacto debe contenes solo numeros");
            }
        }
    }

    //Variable para calcular el tiempo
    let debounceTimer;

    //Funcion para esperar 1 segundos antes de validar cada campo de cliente
    function debounceValidarCliente() {
        clearTimeout(debounceTimer);
        debounceTimer = setTimeout(validarCliente, 1000); //1000 ms = 1 segundos
    }

    if (clienteNombreInput != null){
        clienteNombreInput.addEventListener('input', debounceValidarCliente);
        clienteCIFInput.addEventListener('input', debounceValidarCliente);
        clienteDireccionInput.addEventListener('input', debounceValidarCliente);
        clientePersonaContactoInput.addEventListener('input', debounceValidarCliente);
        clienteEmailContactoInput.addEventListener('input', debounceValidarCliente);
        clienteNumContactoInput.addEventListener('input', debounceValidarCliente);
    }

    // accesibilidad: Click para editar tamaño del texto
    // selecciona el tamaño actual como escala (1), sumandole o restandole 0.1 según lo que indique el usuario
    let escala = 1;
    const paso = 0.1;
    const tamañosOriginales = new Map();
    let tamañosGuardados = false;

    const etiquetasTexto = [ 'p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'span', 'a', 'li', 'td', 'th', 'label', 'div', 'button',
    'form', 'input', 'textarea', 'select', 'option', 'fieldset'];

    // funcion que guarda el tamaño de fuente original de los elementos
    function guardarTamañosOriginales() {
        etiquetasTexto.forEach(tag => {
            document.querySelectorAll(tag).forEach(el => {
                if (!tamañosOriginales.has(el)) {
                    const tamañoBase = parseFloat(getComputedStyle(el).fontSize);
                    tamañosOriginales.set(el, tamañoBase);
                }
            });
        });
        tamañosGuardados = true;
    }

    // funcion que establece el nuevo tamaño del texto
    function aplicarEscala() {
        tamañosOriginales.forEach((tamañoOriginal, el) => {
            el.style.fontSize = (tamañoOriginal * escala) + 'px';
        });
    }

    // funcion que ejecuta las funciones anteriores una vez se pulsa uno de los botones
    function ajustarTamañoTexto(factor) {
        if (!tamañosGuardados) {
            guardarTamañosOriginales();
        }

        escala += factor;
        if (escala < 0.8) escala = 0.8;
        if (escala > 1.2) escala = 1.2;

        aplicarEscala();
    }

    // según el botón pulsado, señala a la función de aumento/reducción
    document.getElementById('btnAumentar')?.addEventListener('click', () => ajustarTamañoTexto(paso));
    document.getElementById('btnReducir')?.addEventListener('click', () => ajustarTamañoTexto(-paso));

});

// funcion para conseguir el token CSRF 
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (const cookie of cookies) {
            const trimmed = cookie.trim();
            if (trimmed.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(trimmed.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

//
document.addEventListener('DOMContentLoaded', () => {
    
    document.querySelectorAll('.estado-select').forEach(select => {
        
        select.addEventListener('change', () => {
            // obtiene la tarea y su nuevo estado
            const tareaId = select.dataset.tareaId;
            const nuevoEstado = select.value;

            // petición POST usando fetch 
            fetch(`/deustotil/tarea/${tareaId}/cambiar_estado/`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCookie('csrftoken'),
                },
                //envia el nuevo estado
                body: JSON.stringify({ nuevo_estado: nuevoEstado })
            })

            .then(response => response.json())
            .then(data => {
                // si se ha actualizado muestra mensaje de confirmación, sino error
                if (data.message) {
                    alert(data.message);
                } else {
                    alert('Error: ' + data.error);
                }
            })
            .catch(error => {
                alert('Error de red: ' + error);
            });
        });
    });
});

