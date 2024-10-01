/*jshint esversion: 6 */

//Query Selectors
const navMainLinkRef = document.querySelector('#nav-main-link');
const navCommunityLinkRef = document.querySelector('#nav-community-link');
const movieCardImgRef = document.querySelector('.movie-card-poster');
const movieCardDialogRef = document.querySelector('#movie-card-dialog');
const warningCancelDialogRef = document.querySelector('#warning-cancel-dialog');
const closeDialogBtnRef = document.querySelector('#close-dialog-btn-div');
const deleteMovieBtnRef = document.querySelector('#div-delete-btn');
const cancelBtnRef = document.querySelector('#cancel-btn');
const closeWarningDialogBtnRef = document.querySelector('#close-warning-dialog-btn');

//CONSTANTS
const currentUrl = window.location.href;

//Functions
const formatHeader = () => {
    console.log(currentUrl);
    //TODO - add check for which page is active
    /*
    //if on Main page
    navMainLinkRef.classList.add("nav-is-active");
    navCommunityLinkRef.classList.remove("nav-is-active");

    //if on Community Page
    navMainLinkRef.classList.remove("nav-is-active");
    navCommunityLinkRef.classList.add("nav-is-active");
    */

};


//Event Click
movieCardImgRef.addEventListener("click", () => {
    movieCardDialogRef.showModal();
});

closeDialogBtnRef.addEventListener("click", () => {
    movieCardDialogRef.close();
  });

deleteMovieBtnRef.addEventListener("click", () => {
    warningDialogRef.showModal();
  });

cancelBtnRef.addEventListener("click", () => {
    warningCancelDialogRef.showModal();
});

closeWarningDialogBtnRef.addEventListener("click", () => {
    warningCancelDialogRef.close();
});
