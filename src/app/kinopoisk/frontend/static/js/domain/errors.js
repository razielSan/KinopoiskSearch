/**
 * 
 * @param {string} message - сообщение об ошибке
 */
function showErrors(message) {
    const errorBox = document.getElementById("error-message")
    errorBox.textContent = `An error has occurred  -  ${message}`
    errorBox.style.display = "block";
}

export {showErrors}