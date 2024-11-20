const startBtn = document.getElementById('start')
const screens = document.querySelectorAll('.screen')

function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) {
        return parts.pop().split(';').shift();
    }
    return null;
}


document.getElementById('login_form').addEventListener('submit', (event) => {

    event.preventDefault()
    screens[0].classList.add('up')

    const htmlForm = document.getElementById('login_form')
    const dataForm = new FormData(htmlForm);

    fetch(loginUrl, {
        method: "POST",
        body: dataForm,
        headers: {
            "X-CSRFToken": dataForm.get('csrfmiddlewaretoken')
        }
    })
    .then(response => response.json());
    // .then(data => {
    //     if (data.status === "success") {
    //         // Обновите интерфейс или покажите сообщение о успешной аутентификации
    //         alert("Вы успешно вошли в систему!");
    //     } else {
    //         // Покажите ошибку
    //         alert(data.message);
    //     }
    // });

    fetch(ogrnUrl) // Укажите правильный URL для вашего API
        .then(response => {
            if (!response.ok) {
                throw new Error('Сеть ответила с ошибкой: ' + response.status);
            }
            return response.json(); // Предполагаем, что ответ в формате JSON
        })
        .then(data => {
            console.log(getCookie('csrftoken'))
            console.log(data); // Можно оставить для отладки, если нужно

            // Обработайте данные и отобразите их на странице
            const dataContainer = document.getElementById('sw_ogrns');
            dataContainer.innerHTML = ''; // Очищаем контейнер перед добавлением новых данных
            

            // Предполагаем, что data — это массив строк
            data.ogrn.forEach(item => {
                const link = document.createElement('div'); // Создаем элемент <a>
                link.className = 'sw_ogrn'; // Добавляем класс
                // link.href = '#'; // Укажите URL или оставьте пустым
                link.textContent = item; // Устанавливаем текст элемента

                // Добавляем элемент <a> в контейнер
                dataContainer.appendChild(link);
            });

            const listOgrn = document.querySelectorAll('.sw_ogrn') 
            listOgrn.forEach((item) => {
                item.addEventListener('click', (event) => {
                    // const data = {
                    //     csrfmiddlewaretoken: dataForm.get('csrfmiddlewaretoken'),
                    //     email: dataForm.get('email'),
                    //     password: dataForm.get('password'),
                    //     ogrn: item.textContent
                    // }
                    window.location.assign(homeUrl.slice(0, -1) + item.textContent)
                    // const formData = new FormData();
                    // formData.append('csrfmiddlewaretoken', dataForm.get('csrfmiddlewaretoken'));
                    // formData.append('email', dataForm.get('email'));
                    // formData.append('password', dataForm.get('password'));
                    // formData.append('ogrn', item.textContent);

                    // console.log(formData)

                    // fetch(loginUrl, {
                    //     method: 'POST',
                    //     headers: {
                    //         // 'Content-Type': 'application/x-www-form-urlencoded',
                    //         'X-CSRFToken': dataForm.get('csrfmiddlewaretoken'),
                    //     },
                    //     body: formData,
                    //   })
                    //     .then((response) => response.json())
                    //     .then((data) => {
                    //         if (data['status'] == 'ok') {
                    //             console.log('hello')
                    //             window.location.assign(homeUrl.slice(0, -1) + item.textContent)
                    //         } else {
                    //             // console.log()
                    //         }
                    //     })
                    //     .catch((error) => {
                    //       console.error('Error:', error);
                    //     });
                })
            })


        })
        .catch(error => {
            console.error('Ошибка:', error);
        });  
})


const addOGRN = document.getElementById('addOGRN')

const htmlOgrnForm = document.getElementById('ogrn_form')
const dataOgrnForm = new FormData(htmlOgrnForm);




addOGRN.addEventListener('click', (event) => {
    event.preventDefault();
    
    // Получаем значение из поля ввода
    const ogrnValue = document.getElementById('id_add_ogrn').value;
    console.log(ogrnValue);  // Проверяем в консоли, что получаем правильное значение

    // Отправляем запрос с данными в формате JSON
    fetch(ogrnUrl, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken'),
        },
        body: JSON.stringify({
            'ogrn': ogrnValue
        }),
    })
    .then((response) => response.text())
    .then((data) => { console.log(data); })  // Проверяем ответ от сервера
    .catch((error) => {
        console.error('Error:', error);
    });

    const link = document.createElement('div'); // Создаем элемент <a>
    link.className = 'sw_ogrn'; // Добавляем класс
    // link.href = '#'; // Укажите URL или оставьте пустым
    link.textContent = ogrnValue; // Устанавливаем текст элемента
    const dataContainer = document.getElementById('sw_ogrns');
    // Добавляем элемент <a> в контейнер
    dataContainer.appendChild(link);
})