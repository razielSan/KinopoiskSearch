import { API } from "../api.js";
import {showErrors} from "../domain/errors.js"

/**
 * 
 * @param {function} getListMovies - делает запрос по API
 * @param {function} showMovies  - отображает фильмы
 * @param {function} openModal  - отображает модальное окно
 * @param {funciton} showPaginationMovies - отображает пагинацию страницы
 */
async function showTop250Movies(
    getListMovies,
    showMovies,
    openModal,
    showPaginationMovies
) {
    const page = 1;
    const dataMovie = await getListMovies(`${API.top250}?page=${page}`);
    if (!dataMovie.movies) {
        showErrors(dataMovie.message)
        return;
    } // Если произошла ошибка

    await showMovies(dataMovie, openModal);

    await showPaginationMovies(dataMovie, showMovies, openModal, getListMovies);
}

export { showTop250Movies };
