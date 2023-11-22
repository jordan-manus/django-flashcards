console.log('connected');

let cards = document.querySelectorAll('.card');

console.log(cards);
cards.forEach((card) => {
    card.addEventListener('click', function (event) {
        console.log(card.classList);
        card.classList.toggle('is-flipped');

        // allows me to add classes to question and answer elems
        let question = card.childNodes[1].classList;
        question.toggle('hide-question');
        console.log('question: ', question);
        let answer = card.childNodes[3].classList;
        console.log('answer: ', answer);
        answer.toggle('show-answer');
        console.log('answer after toggle: ', answer);


        // get access the congrats button to tally correct guesses
        console.log('event id', event.target.id);
        let dataId = card.getAttribute('data-id');
        let confirm_buttons = document.querySelectorAll("[data-id]");
        confirm_buttons.forEach((button) => {
            let nodes = button.childNodes
            console.log('button nodes: ', nodes)
            if (button.getAttribute('data-id') === dataId) {
                button.classList.toggle('show');
            }
        });
    })
});

// counts correct guesses once button is pushed
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
