// Добавляем класс show после загрузки страницы для всех постов
window.addEventListener('load', function() {
    const posts = document.querySelectorAll('.post-preview, .post-detail');
    posts.forEach((post, index) => {
        setTimeout(() => {
            post.classList.add('show'); // Добавляем класс для плавного появления
        }, index * 200); // Задержка для каждого элемента
    });
});
