/*jshint esversion: 6 */

//Query Selectors
const navMainLinkRef = document.querySelector('#nav-main-link');
const navCommunityLinkRef = document.querySelector('#nav-community-link');
const movieCardImgRef = document.querySelector('.movie-card-poster');
const dialogRef = document.querySelector('dialog');
const closeDialogBtnRef = document.querySelector('#close-dialog-btn-div');

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
    dialogRef.showModal();
});

closeDialogBtnRef.addEventListener("click", () => {
    dialogRef.close();
  });