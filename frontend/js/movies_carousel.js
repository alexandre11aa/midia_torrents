document.addEventListener('DOMContentLoaded', () => {
    const movieBar = document.querySelector('.movie-bar');
    const movieItemsContainer = document.querySelector('.movie-items-container');

    // Defina o tempo de rotação (em milissegundos)
    const scrollDuration = 120000; // 40 segundos

    movieItemsContainer.style.animation = `scroll ${scrollDuration}ms linear infinite`;

    movieBar.addEventListener('mouseenter', () => {
        movieItemsContainer.style.animationPlayState = 'paused';
    });

    movieBar.addEventListener('mouseleave', () => {
        movieItemsContainer.style.animationPlayState = 'running';
    });
});