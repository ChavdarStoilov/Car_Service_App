function rotateCarCard(cardId, pk) {
    const card = document.querySelector(`.card-${pk}`)
    const cardBackContent = document.querySelector(`.${cardId} > .card > .card-back`)
    const cardFront = document.querySelector(`.${cardId} > .card > .card-front`)

    const url = `http://127.0.0.1:8000/api/car/${pk}/`

    fetch (url)
        .then(response => response.json()) // convert response to json
        .then(data => present(data)) // function for present data

    
    function present(data) {
        cardBackContent.innerHTML = `
            <h2>Model: ${data.model}</h2>
            <p>Year: ${data.year}</p>
            <p>VIN: ${data.VIN}</p>
            <p>Kilometers: ${data.kilometers}</p>
            
            <a class="edit-btn" onclick="BackrotateCarCard('col-md-${pk}', ${pk});">Back</a>
            
        `
        if (data.history_id != null) {
            cardBackContent.innerHTML += `
                <a class="edit-btn" href="/garage/history/${pk}">History</a>
            `
        }
    }

    card.style.cssText = `
        transform: rotateY(-180deg);
    `

    cardFront.style.cssText = `
        display: none;
    `

    cardBackContent.style.cssText = `
        transform: rotateY(180deg);
        display: block;
    `

}


function BackrotateCarCard(cardId, pk) {
    const card = document.querySelector(`.card-${pk}`)
    const cardBackContent = document.querySelector(`.${cardId} > .card > .card-back`)
    const cardFront = document.querySelector(`.${cardId} > .card > .card-front`)

    card.style.cssText = `
        transform: none;
    `


    cardBackContent.style.cssText = `
        display: none;
        transform: none;
    `
    
    cardFront.style.cssText = `
        display: block;
    `
}



function carQueue(pk) {
    console.log(pk);
    // active
    // <i class="fas fa-check"></i>
    // active-bar
}