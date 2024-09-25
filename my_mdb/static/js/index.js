/*jshint esversion: 6 */

//Query Selectors
const movieCardImgRef = document.querySelector('.movie-card-poster');
const dialogRef = document.querySelector("dialog");

//Event Click
movieCardImgRef.addEventListener("click", () => {
    dialogRef.showModal();
});