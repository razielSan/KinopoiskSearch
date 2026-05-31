/**
 * @param {string} url - URL для запроса
 */
async function getListMovies(
  url,
) {
  const response = await fetch(url);
  const result = await response.json()
  console.log(result)
  return result
}


export { getListMovies }