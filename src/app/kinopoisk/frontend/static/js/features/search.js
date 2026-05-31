import { API } from "../api.js";
import { showErrors } from "../domain/errors.js";

/**
 *
 * @param {function} getListMovies - делает запрос по API
 * @param {function} showMovies  - отображает фильмы
 * @param {function} openModal  - отображает модальное окно
 * @param {funciton} showPaginationMovies - отображает пагинацию страницы
 */
function show_search_movie_by_name(
    getListMovies,
    showMovies,
    openModal,
    showPaginationMovies
) {
    const page = 1;
    const form = document.querySelector("form");
    const search = document.querySelector(".header_search");
    form.addEventListener("submit", async (el) => {
        el.preventDefault();
        const apiSearchUrl = `${API.search}?name=${search.value}&page=${page}`;
        if (search.value) {
            document.querySelector(".pagination").innerHTML = "";
            const dataSearch = await getListMovies(apiSearchUrl);
            if (!dataSearch.movies) { // Если произошла ошибка
                showErrors(dataSearch.message);
                return;
            }
            showMovies(dataSearch, openModal);
            showPaginationMovies(
                dataSearch,
                showMovies,
                openModal,
                getListMovies,
                search.value
            );
            search.value = "";
        }
    });
}

export { show_search_movie_by_name };
