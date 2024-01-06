document.addEventListener('DOMContentLoaded', function () {
    var ajaxButton = document.getElementById('ajaxButton');

    function makeAjaxRequest() {
        var xhr = new XMLHttpRequest();
        xhr.open('GET', '/ajax_endpoint/', true);

        xhr.onreadystatechange = function() {
            if (xhr.readyState === 4 && xhr.status === 200) {
                var responseData = JSON.parse(xhr.responseText);
                console.log('AJAX request successful:', responseData);
                // Обновите DOM или выполните другие действия
            }
        };

        xhr.send();
    }

    ajaxButton.addEventListener('click', makeAjaxRequest);

    // Запускаем AJAX-запрос каждые 10 секунд
    setInterval(makeAjaxRequest, 10000);
});