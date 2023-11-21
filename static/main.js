console.log('connected');

let cards = document.querySelectorAll('.card');
console.log(cards);
cards.forEach((card) => {
    card.addEventListener('click', function () {
        console.log('clicked');
        console.log(card.classList);
        card.classList.toggle('is-flipped');

        console.log(card.classList);
    });
});

// card.addEventListener('click', (event) => {
//     console.log("card value:", card.value)
//     console.log(card.src)
//     card.src = card.dataset.cardFront;
//     console.log(card.src)
// })

