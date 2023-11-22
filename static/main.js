console.log('connected');

let cards = document.querySelectorAll('.card');

console.log(cards);
cards.forEach((card) => {
    card.addEventListener('click', function (event) {
        // console.log('clicked');
        console.log(card.classList);
        card.classList.toggle('is-flipped');
        // console.log(card.classList);

        console.log('event id', event.target.id)
        let dataId = card.getAttribute('data-id')
        // console.log('data id', dataId)
        let confirm_buttons = document.querySelectorAll("[data-id]");
        // console.log('confirm buttons', confirm_buttons)
        // confirm_buttons.classList.toggle('.show');
        // console.log('confirm buttons', confirm_buttons.classList)
        confirm_buttons.forEach((button) => {
            // console.log('before if statement')
            if (button.getAttribute('data-id') === dataId) {
                // console.log('inside the if statement for button')
                button.classList.toggle('show');
            }
            // console.log('outside of if statment')
            // console.log('button class list: ', button.classList)

            // add pop up to tell user they got it right and record data
            // show user how many they got correct at the end
        })
        
        
    })
    
    let count = 0;
    let right_button_tally = document.querySelector('#right_button_tally')
    let right_buttons = document.querySelectorAll('.show')
    right_buttons.forEach((button) => {
        button.addEventListener('click', function (event) {
            console.log('clicked')
            count ++
            right_button_tally.innerText = count

        })
        // function calculateResults() {

        // }


    });
});


