/*jshint esversion: 6 */

//Query Selectors
const movieCardImgRef = document.querySelectorAll('.movie-card-poster');
const warningCancelDialogRef = document.querySelector('#warning-cancel-dialog');
const warningDeleteDialogRef = document.querySelector('#warning-delete-dialog');
const closeDialogBtnsRef = document.querySelectorAll('.close-dialog-btn');
const deleteMovieBtnsRef = document.querySelectorAll('.delete-dialog-btn');
const cancelBtnRef = document.querySelector('#cancel-btn');
const closeCancelDialogBtnRef = document.querySelector('#close-cancel-warning-dialog-btn');
const closeDeleteDialogBtnsRef = document.querySelectorAll('.close-delete-dialog-btn'); 
const cardMovieNameRef = document.querySelector(".movie-card-name");
const dialogMovieNameRef = document.querySelector("#dialog-movie-name");
const dialogMovieDateRef = document.querySelector("#dialog-movie-date");
const dialogMovieReviewRef = document.querySelector("#dialog-movie-review");
const dialogMovieIdRef = document.querySelector("#dialog-movie-id");
const formDateFieldRef = document.querySelector("#datefield");

const currentUrl = window.location.href;
let currentMovieName;
let currentMovieDate;
let currentMovieReview;
let currentMovieId;
let movieCardDialogRef;

let today = new Date();
let dd = today.getDate();
let mm = today.getMonth() + 1;
let yyyy = today.getFullYear();

//Functions
function getMovieDataforDialog(obj) {

    currentMovieName = obj.dataset.movieName;
    currentMovieDate = obj.dataset.movieDate;
    currentMovieReview = obj.dataset.movieReview;
    currentMovieId =  obj.dataset.movieId;
    movieCardDialogRef = document.querySelector(`.movie-card-dialog-${currentMovieId}`);
    setMovieDataforDialog();
    movieCardDialogRef.showModal();

    closeDialogBtnsRef.forEach(button => {
        button.addEventListener("click", (event) => {
            const movieId = event.target.dataset.movieId;
            const dialogRef = document.querySelector(`#movieCardDialog-${movieId}`);
    
            if (dialogRef) {
                dialogRef.close(); 
            } else {
                console.error(`Dialog not found for movie id: ${movieId}`);
            }
        });
    });

    deleteMovieBtnsRef.forEach(button => {
        button.addEventListener("click", (event) => {
            const movieId = event.target.dataset.movieId;
            const deleteDialogRef = document.querySelector(`#warningDeleteDialog-${movieId}`);
    
            if (deleteDialogRef) {
                deleteDialogRef.showModal(); 
            } else {
                console.error(`Dialog not found for movie id: ${movieId}`);
            }
        });
    });

    closeDeleteDialogBtnsRef.forEach(button => {
        button.addEventListener("click", (event) => {
            const movieId = event.target.dataset.movieId;
            const deleteDialogRef = document.querySelector(`#warningDeleteDialog-${movieId}`);
    
            if (deleteDialogRef) {
                deleteDialogRef.close(); 
            } else {
                console.error(`Dialog not found for movie id: ${movieId}`);
            }
        });
    });
}

function setMovieDataforDialog() {
    dialogMovieNameRef.textContent = currentMovieName;
    dialogMovieDateRef.textContent = currentMovieDate;
    dialogMovieReviewRef.textContent = currentMovieReview;
    dialogMovieIdRef.textContent = currentMovieId;
}

function formatDateField() {
    if (dd < 10) {
        dd = '0' + dd;
     }
     
     if (mm < 10) {
        mm = '0' + mm;
     } 
         
     today = yyyy + '-' + mm + '-' + dd;
     formDateFieldRef.setAttribute("max", today);
}

document.addEventListener("DOMContentLoaded", () => {

    cancelBtnRef?.addEventListener("click",  () => {
        warningCancelDialogRef.showModal();
    });

    closeCancelDialogBtnRef?.addEventListener("click",  () => {
        warningCancelDialogRef.close();
    });

});