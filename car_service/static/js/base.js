function rotateCarCard(cardId, pk) {
    const card = document.querySelector(`.card-${pk}`)
    const cardBackContent = document.querySelector(`.${cardId} > .card > .card-back`)
    const cardFront = document.querySelector(`.${cardId} > .card > .card-front`)

    const url = `http://127.0.0.1:8000/api/car/${pk}/`

    fetch (url)
        .then(response => response.json())
        .then(data => present(data))

    
    function present(data) {
        cardBackContent.innerHTML = `
            <h2>Model: ${data.model}</h2>
            <p>Year: ${data.year}</p>
            <p>VIN: ${data.VIN}</p>
            <p>Kilometers: ${data.kilometers}</p>
            
            <a class="edit-btn" onclick="BackrotateCarCard('col-md-${pk}', ${pk});">Back</a>
            
        `
        if (data.have_history) {
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


function genereateInvoice(id) {
    const url = `http://127.0.0.1:8000/api/car/history/${id}/`
    const contentBox = document.getElementsByClassName("content")[0]
    const popup = document.getElementsByClassName("overlay")[0]

    contentBox.innerHTML = ""
    fetch (url)
        .then(response => response.json())
        .then(data => present(data))

    function present(data) {
        const parts = data.history['Changed parts']
        totalPrice = 0
        const invoice = document.createElement("section")
        invoice.setAttribute("class", "invoice")
        invoice.innerHTML = `
                <div class="invoice__header">
                <div id="logo">
                    <img class="invoice__header__logo" src="/static/images/new_logo.png" alt="company logo">
                </div>
                <h1 class="invoice__title" >INVOICE ${id}</h1>
            </div>
            <div class="invoice__summary">
                <table class="invoice__table">
                    <thead>
                    <tr>
                        <th>Part</th>
                        <th></th>
                        <th>PRICE</th>
                        <th>QTY</th>
                        <th>TOTAL</th>
                    </tr>
                    </thead>
                    <tbody class="table_body">
                    </tbody>
                    <tfoot class="table_footer">
                    </tfoot>
                </table>
            </div>
        `
        contentBox.appendChild(invoice)
        tableBody = document.getElementsByClassName("table_body")[0]
        tableFooter = document.getElementsByClassName("table_footer")[0]

        for (const part in parts) {
            const partName = part;
            const partPrice = parts[part];
            const totalPartPrice = partPrice * 1;
            
            totalPrice +=  partPrice    ;

            var newRow = document.createElement("tr");
            newRow.innerHTML = `
                <td class="td__center">${partName}</td>
                <td></td>
                <td class="td__center">${partPrice.toFixed(2)}</td>
                <td class="td__center">1</td>
                <td class="td__right">${totalPartPrice.toFixed(2)}</td>
            `;
            tableBody.appendChild(newRow);

            
        }
        tax = (totalPrice * 0.25);
        subTotal = (totalPrice - tax);

        tableFooter.innerHTML = `
            <tr class="td__right invoice__total">
                <td colspan="4">SUBTOTAL</td>
                <td class="subtotal">${subTotal.toFixed(2)}</td>
            </tr>
            <tr class="td__right">
                <td colspan="4">TAX 25%</td>
                <td class="tax">${tax.toFixed(2)}</td>
            </tr>
            <tr class="td__right">
                <td colspan="4" class="grand total">GRAND TOTAL</td>
                <td class="grand total">${totalPrice.toFixed(2)}</td>
            </tr>
        `;

        popup.style.cssText = `
            display: block;
        `;

        
        
    }
    
}


function closePopUp() {
    const popup = document.getElementsByClassName("overlay")[0]
    console.log(popup);

    popup.style.cssText = `
        display: none;
    `;
}