/*jshint esversion: 6 */

//Query Selectors
const navMainLinkRef = document.querySelector('#nav-main-link');
const navCommunityLinkRef = document.querySelector('#nav-community-link');
const movieCardImgRef = document.querySelectorAll('.movie-card-poster');
const movieCardDialogRef = document.querySelector('.movie-card-dialog');
const warningCancelDialogRef = document.querySelector('#warning-cancel-dialog');
const warningDeleteDialogRef = document.querySelector('#warning-delete-dialog');
const closeDialogBtnRef = document.querySelector('#close-dialog-btn-div');
const deleteMovieBtnRef = document.querySelector('#div-delete-btn');
const cancelBtnRef = document.querySelector('#cancel-btn');
const closeCancelDialogBtnRef = document.querySelector('#close-cancel-warning-dialog-btn');
const closeDeleteDialogBtnRef = document.querySelector('#close-delete-warning-dialog-btn');
const cardMovieNameRef = document.querySelector(".movie-card-name");
const dialogMovieNameRef = document.querySelector("#dialog-movie-name");
const dialogMovieDateRef = document.querySelector("#dialog-movie-date");
const dialogMovieReviewRef = document.querySelector("#dialog-movie-review");

//CONSTANTS
const currentUrl = window.location.href;

//Variables
let currentMovieName;
let currentMovieDate;
let currentMovieReview;

//Functions
function getMovieDataforDialog(obj) {
    currentMovieName = obj.dataset.movieName;
    currentMovieDate = obj.dataset.movieDate;
    currentMovieReview = obj.dataset.movieReview;
}

function setMovieDataforDialog() {
    dialogMovieNameRef.textContent = currentMovieName;
    dialogMovieDateRef.textContent = currentMovieDate;
    dialogMovieReviewRef.textContent = currentMovieReview;
}

/*
const formatHeader = () => {
    console.log(currentUrl);
    //TODO - add check for which page is active

    //if on Main page
    navMainLinkRef.classList.add("nav-is-active");
    navCommunityLinkRef.classList.remove("nav-is-active");

    //if on Community Page
    navMainLinkRef.classList.remove("nav-is-active");
    navCommunityLinkRef.classList.add("nav-is-active");
    

*/

//Event Click
document.addEventListener("DOMContentLoaded", () => {

    /*movieCardImgRef?.addEventListener("click",  () => {
        movieCardDialogRef.showModal();
    });*/

    for( var i=0; i<movieCardImgRef.length; i++){
        movieCardImgRef[i].addEventListener("click", () => { 
            setMovieDataforDialog();
            movieCardDialogRef.showModal();
        });
    }

    closeDialogBtnRef?.addEventListener("click",  () => {
        movieCardDialogRef.close();
    });

    cancelBtnRef?.addEventListener("click",  () => {
        warningCancelDialogRef.showModal();
    });

    closeCancelDialogBtnRef?.addEventListener("click",  () => {
        warningCancelDialogRef.close();
    });

    deleteMovieBtnRef?.addEventListener("click",  () => {
        warningDeleteDialogRef.showModal();
    });

    closeDeleteDialogBtnRef?.addEventListener("click",  () => {
        warningDeleteDialogRef.close();
    });

});

