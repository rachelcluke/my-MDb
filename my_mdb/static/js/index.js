/*jshint esversion: 6 */

//Query Selectors
const movieCardImgRef = document.querySelector('.movie-card-poster');
const dialogRef = document.querySelector("dialog");
const closeDialogBtnRef = document.querySelector("#close-dialog-btn-div");

//Event Click
movieCardImgRef.addEventListener("click", () => {
    dialogRef.showModal();
});

closeDialogBtnRef.addEventListener("click", () => {
    dialogRef.close();
  });