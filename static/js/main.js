const cambiarTitulo = () => {
    titulo = document.getElementById('nuevoTitulo').value
    document.getElementById("titulo").innerHTML = titulo
}

const mostrarNombre = (check) => {
    console.log(check.checked);
    id_jugador = parseInt(check.id.split('jugadorPago')[1]);

    // Get the output text
    jugador = document.getElementById(`jugador${id_jugador}`);
    if (check.checked == true){
        label_jugador = document.getElementById(`jugadorLabel${id_jugador}`).innerHTML = jugador.value
        label_pago = document.getElementById(`labelPago${id_jugador}`)
        jugador.style.display = "none"
        // label_pago.style.display = "none"
    } else {
        label_jugador = document.getElementById(`jugadorLabel${id_jugador}`).innerHTML = ""
        jugador.style.display = "block"
        // label_pago.style.display = "inline-block"
    }
    id_jugador = null
    
}


const sorteo = () => {
    numerosSorteo = document.getElementById("sorteo").value
    converted = JSON.parse(numerosSorteo)

    numerosCartas = document.getElementById("sorteo").value
    convertedCartas = JSON.parse(numerosSorteo)

    almacenados = []
    i = 0

    let temporizador = setInterval(() => {
        
        key = document.getElementById(`key-${converted[i]}`)
        key.classList.add("bg-success")
        key.classList.remove("bg-primary")
        document.getElementById("num-sorteado").innerHTML = converted[i];
        i++
        if (i == 96) {
            clearInterval(temporizador)
        }
    }, 500)

    
}