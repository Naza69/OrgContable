//Ejercicio de permutacion con cliente ftp

//Datos extraidos del input
let entry = []

const form = document.getElementById("formApermutar")

const botonSend = document.getElementById("botonEnviar")

botonSend.addEventListener("click", (e) => {
    e.preventDefault()
    entry = [document.getElementById("contra").value,
        document.getElementById("usuario").value]
})

function matchPass(pass) {
    const characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
    for(let i = 0; i<entry[0].length; i++){
        for(let j = 0; j<characters.length; j++ ){
            if(entry[0][i] == characters[j]){
                pass = pass+characters[j]
                break;
            }
        }
    }
    return pass
}

const botonHacking = document.getElementById("botonHack").addEventListener("click", () => {

    let pass = ""
    let passForm = matchPass(pass)

    const passContainer = document.getElementById("contenedorPassword")

    passContainer.innerHTML = `
    
    <div class="passContainer">Su contraseña es: ${passForm}</div>
    `
})