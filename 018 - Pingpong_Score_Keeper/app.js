// alert("jfiewjao")

const p1Button = document.querySelector('#p1Button');
const p2Button = document.querySelector('#p2Button');
const p1Display = document.querySelector('#p1Display');
const p2Display = document.querySelector('#p2Display');
const resetButton = document.querySelector('#reset');
const winningScoreSelect = document.querySelector('#winningScoreSelect');



let p1Score = 0;
let p2Score = 0;
let isGameOver = false;

p1Button.addEventListener('click', function (e) {
    if (!isGameOver) {
        p1Score += 1;
        if (p1Score === winningScore) {
            isGameOver = true;
            p1Display.classList.add('has-text-success');
            p2Display.classList.add('has-text-danger');
            p1Button.disabled = true; // part of the Bulma event
            p2Button.disabled = true; // part of the Bulma event
        }
        p1Display.textContent = p1Score;
    }
});

p2Button.addEventListener('click', function (e) {
    if (!isGameOver) {
        p2Score += 1;
        if (p2Score === winningScore) {
            isGameOver = true;
            p1Display.classList.add('has-text-danger');
            p2Display.classList.add('has-text-success');
            p1Button.disabled = true; // part of the Bulma event
            p2Button.disabled = true; // part of the Bulma event
        }
        p2Display.textContent = p2Score;
    }
});

winningScoreSelect.addEventListener('change', function (e) {
    winningScore = parseInt(this.value);
    reset();
})

resetButton.addEventListener('click', reset);

function reset() {
    isGameOver = false;
    p1Score = 0;
    p2Score = 0;
    p1Display.textContent = 0;
    p2Display.textContent = 0;
    p1Display.classList.remove('has-text-success', 'has-text-danger');
    p2Display.classList.remove('has-text-success', 'has-text-danger');
    p1Button.disabled = false; // part of the Bulma event
    p2Button.disabled = false; // part of the Bulma event

}