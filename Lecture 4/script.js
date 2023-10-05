const main = document.querySelector('main');
const button = document.createElement('button');
button.textContent = 'Change Color';
button.addEventListener('click', () => {
    const randomColor = '#' + Math.floor(Math.random()*16777215).toString(16);
    main.style.backgroundColor = randomColor;
});
main.appendChild(button);

// This is my function, it does things!
const myfunc = () => {

}
