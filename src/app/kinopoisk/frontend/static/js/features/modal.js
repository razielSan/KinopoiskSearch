import { getListMovies } from "../services/movies.js";
import { API } from "../api.js";
import { showErrors } from "../domain/errors.js";

const modelEl = document.querySelector(".modal");

/**
 * @param {number} film_id - ID фильма
 */
async function openModal(film_id) {
  // Отображает модальное окно
  modelEl.classList.add("modal--show");
  document.body.classList.add("stop-scrolling");

  const url = `${API.movie}?film_id=${film_id}`;
  // получаем данные о фильме
  const movieInfo = await getListMovies(url);

  if (!movieInfo.name) { // если произошла ошибка
    showErrors(movieInfo.message);
    return;
  }
  modelEl.innerHTML = `
    <div class="modal__card">
    <img src="${movieInfo.urlPoster}" onerror="this.src='/static/img/no-photo.png'" alt="" class="modal__movie-backdrop" />
    <h2>
      <span class="modal__movie-title">${movieInfo.name}</span>
      <span class="modal__movie-release-year">- ${movieInfo.year}</span>
    <h2>
    </h2>
    <ul class="modal__movie-info">
      <div class="loader"></div>
      <li class="modal__movie-genre">Жанр: ${movieInfo.genres}</li>
      <li class="modal__movie-runtime">Время: ${movieInfo.filmLength}</li>
      <li>Сайт: <a href="${movieInfo.site}" class="modal__movie-site">${movieInfo.site}</a></li>
      <li class="modal__movie-overview">Описание: ${movieInfo.description}</li>
    </ul>
    <button type="button" class="modal__button-close">Закрыть</button>
    </div>
    `;
  const buttonClose = document.querySelector(".modal__button-close");
  buttonClose.addEventListener("click", () => {
    closeModal();
  });
}

function closeModal() {
  modelEl.classList.remove("modal--show");
  document.body.classList.remove("stop-scrolling");
}

window.addEventListener("click", (e) => {
  if (e.target === modelEl) {
    closeModal();
  }
});

window.addEventListener("keydown", (e) => {
  if (e.key === "Escape") {
    closeModal();
  }
});

export { openModal };
