import {
  API
} from "./api.js";

/**
 * 
 * @param {*} pageData 
 * @param {object} showMovies 
 * @param {*} openModal 
 * @param {*} getListMovies 
 * @param {*} search 
 */
async function showPaginationMovies(
  pageData,
  showMovies,
  openModal,
  getListMovies,
  search = null
) {
  let currentPage = 1;
  const quantityMovie = 20;
/**
 * 
 * @param {object} data - содержит данные об общем количестве фильмов
 * @param {number} quantityMovie - количество фильмов на странице
 */
  async function displayPagination(data, quantityMovie) {
    const countMovies = data.total;
    const paginationEl = document.querySelector(".pagination");
    const pagesCount = Math.ceil(countMovies / quantityMovie);
    const ulEl = document.createElement("ul");
    ulEl.classList.add("pagination__list");
    for (let i = 0; i < pagesCount; i++) {
      const liEl = await displayPaginationBtn(i + 1);
      ulEl.appendChild(liEl);
    }
    paginationEl.appendChild(ulEl);
  }

  /**
   * 
   * @param {number} page - номер страницы
   * @returns html элемент
   */
  async function displayPaginationBtn(page) {
    const liEl = document.createElement("li");
    liEl.classList.add("pagination__item");
    liEl.innerText = page;
    if (currentPage === page) {
      liEl.classList.add("pagination__item--active");
    }

    liEl.addEventListener("click", async () => {
      let dataListMovies = "";
      if (search) {
        dataListMovies = await getListMovies(
          `${API.search}?name=${search}&page=${page}`,
        );
      } else {
        dataListMovies = await getListMovies(
          `${API.top250}?page=${page}`,
        );
      }

      showMovies(dataListMovies, openModal);
      document
        .querySelector(".pagination__item--active")
        .classList.remove("pagination__item--active");
      liEl.classList.add("pagination__item--active");
    });
    return liEl;
  }

  displayPagination(pageData, quantityMovie);
}

export { showPaginationMovies };
