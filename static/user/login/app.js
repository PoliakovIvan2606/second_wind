const startBtn = document.getElementById('start')
const screens = document.querySelectorAll('.screen')

startBtn.addEventListener('click', (event) => {
    event.preventDefault()
    console.log('asdasd')
    screens[0].classList.add('up')
})