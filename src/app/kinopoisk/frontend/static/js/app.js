import { getListMovies } from "./services/movies.js";
import { showMovies } from "./render.js";
import {show_search_movie_by_name} from "./features/search.js"
import { showPaginationMovies } from "./pagination.js";
import { showTop250Movies } from "./features/show_top_250_movies.js";
import {openModal} from "./features/modal.js"


// Отображение топ 250 фильмов на главной странице
await showTop250Movies(getListMovies, showMovies, openModal, showPaginationMovies)
// Поиск фильмов
show_search_movie_by_name(getListMovies, showMovies, openModal, showPaginationMovies)


