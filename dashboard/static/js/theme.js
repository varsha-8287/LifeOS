const button =
document.getElementById(
'theme-toggle'
);

button.onclick = () => {

document.body.classList.toggle(
'dark-mode'
);

}