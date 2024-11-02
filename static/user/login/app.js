const startBtn = document.getElementById('start')
const screens = document.querySelectorAll('.screen')

startBtn.addEventListener('click', (event) => {
    event.preventDefault()
    screens[0].classList.add('up')
    fetch(ogrnUrl) // Укажите правильный URL для вашего API
        .then(response => {
            if (!response.ok) {
                throw new Error('Сеть ответила с ошибкой: ' + response.status);
            }
            return response.json(); // Предполагаем, что ответ в формате JSON
        })
        .then(data => {
            console.log(data); // Можно оставить для отладки, если нужно

            // Обработайте данные и отобразите их на странице
            const dataContainer = document.getElementById('sw_ogrns');
            dataContainer.innerHTML = ''; // Очищаем контейнер перед добавлением новых данных

            // Предполагаем, что data — это массив строк
            data.ogrn.forEach(item => {
                const link = document.createElement('a'); // Создаем элемент <a>
                link.className = 'sw_ogrn'; // Добавляем класс
                link.href = '#'; // Укажите URL или оставьте пустым
                link.textContent = item; // Устанавливаем текст элемента

                // Добавляем элемент <a> в контейнер
                dataContainer.appendChild(link);
            });
        })
        .catch(error => {
            console.error('Ошибка:', error);
        });
});
