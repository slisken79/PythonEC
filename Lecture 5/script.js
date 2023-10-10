// const button = document.createElement('button');
//button.textContent = 'Press me to change color';

setTimeout(function() {
    // Vi gör allt inom denna settimeout för att elementen så som button ska hinnas ladda in innan javascripten körs! Naiv lösning men funkar :) 
    const button = document.querySelector(".myButton")
    const main = document.querySelector('main');
    console.log("hello")
    console.log(button)
    button.addEventListener('click', function() {
        const randomColor = '#' + Math.floor(Math.random()*16777215).toString(16);
        main.style.backgroundColor = randomColor;
    });
}, 3000)
//main.appendChild(button);

// This is my function, it does things!
const myfunc = () => {
    console.log("hello world")
}
