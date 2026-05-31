/**
 * @param {object} data - Данные с запроса
 * @param {function} openModal - Функция для отображения модального окна
 */
async function showMovies(data, openModal) {
  // Отрисовывает изображения фильмов на экране


  // оцищаем предыдущие фильмы
  document.querySelector(".movies").innerHTML = "";


  let movieData = data.movies;
  const moviesEl = document.querySelector(".movies");
  movieData.forEach((element) => {
    const movieElemintRating =
      element.rating !== null
        ? `<div class="movie_average movie_average--${element.ratingColor}">${element.rating}</div>`
        : "";
    const movie = document.createElement("div");
    movie.classList.add("movie");
    movie.innerHTML = `
                        <div class="movie_cover-inner">
                        <img
                        src="${element.urlPoster}"
                        onerror="this.src='static/img/no-photo.png'"
                        alt="movie_img"
                        class="movie_cover"
                        />
                        <div class="movie_cover--darkned"></div>
                    </div>
                    <div class="movie_info">
                        <div class="movie_title">${element.name}</div>
                        <div class="movie_category">${element.genres}</div>
                        ${movieElemintRating}
                    </div>       
                    `;
    movie.addEventListener("click", () => openModal(element.kinopoiskId)); // реакция на клик мыши
    moviesEl.appendChild(movie);
  });
}

export { showMovies };
