console.log('connected');

let cards = document.querySelectorAll('.card');

console.log(cards);
cards.forEach((card) => {
    card.addEventListener('click', function (event) {
        console.log(card.classList);
        card.classList.toggle('is-flipped');


        console.log('event id', event.target.id)
        let dataId = card.getAttribute('data-id')
        let confirm_buttons = document.querySelectorAll("[data-id]");
        confirm_buttons.forEach((button) => {
            if (button.getAttribute('data-id') === dataId) {
                button.classList.toggle('show');
            }
        })
    })
});

let count = 0;
let right_button_tally = document.querySelector('#right_button_tally')
let right_buttons = document.querySelectorAll('.confirm-buttons')
right_buttons.forEach((button) => {
    button.addEventListener('click', function (event) {
        console.log('clicked')
        count++
        right_button_tally.innerText = count
    })


});


