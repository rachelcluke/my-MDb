#myMDB (Movie Tracker) Website

<!--[Am I responsive - myMDB](docs/XXX "Am I responsive")-->

# Project Overview

Welcome,

This is myMDb ("my MDb") website, a full-stack site for movie enthusiasts to search, track and review movies they have watched. They will also be able to view what movies other members have been watching. This is Rachel Luke's submission for Code Institute's Backend Development Milestone.

The following are high-level details of this project:

-  This is a relational database backed Flask project for a web application that allows users to store and manipulate data records on movies they have watched.
- The main technologies used are HTML, CSS, JavaScript, Python+Flask and PostgreSQL.
- The project demonstrates backend development web design.
- User functionality is intuitive to users (to create, locate, display, edit and delete records).
- The site has a main navigation in the header and a structured layout.
- Git & GitHub are used for version control.
- Any external code sources used in the project are clearly identified in the code itself and in this README.md file
- The final version has been deployed via GitHub Pages.
- There are no passwords or secret keys in the project repository. 


The last update to this file was: **October 20th, 2024**

# Table of Contents

- [My MDb](#my-mdb)
- [Project Overview](#project-overview)
- [Table of Contents](#table-of-contents)
- [UX](#ux)
  - [User Goals](#user-goals)
  - [User Stories](#user-stories)
  - [Site Owners Goals](#site-owners-goals)
    - [Requirements](#requirements)
    - [Expectations](#expectations)
- [UI / Design Choices](#ui-design-choices)
  - [Moodboard](#moodboard)
  - [Fonts](#fonts)
  - [Icons](#icons)
  - [Colours](#colours)
  - [Media Queries](#media-queries)
  - [Wireframes](#wireframes)
  - [Mockups](#mockups)
- [Features](#features)
  - [Existing Features](#existing-features)
   - [Future actions - Features to be Implemented](#future-actions)
- [Technologies used](#technologies-used)
  - [Languages](#languages)
  - [IDE](#ide)
  - [Libraries & Framework](#libraries-framework)
  - [Tools](#tools)
- [Validating](#validating)
- [Testing](#testing)
- [Deployment](#deployment)
- [Credits](#credits)


# UX

## User Goals

1. Upload and track movies watched.
2. Edit and delete movie listings/ reviews.
3. Easily navigate around website.
4. Log in/sign up account.
5. View other users' listed movies.

## User Stories

1. As a user, I want to find this art quiz website aesthetic and appealing. 
2. As a user, I want to be able to choose the difficulty of the quiz.
3. As a user, I want to be able to easily navigate through the website.
4. As a user, I want to be able to know if my chosen quiz answers are correct.
5. As a user, I want to know what my final quiz score is.

## Site Owners Goals

1. Upload their own watched movies and view other users' tracked movies.
2. Increase the number of online foot traffic.
3. Increase rankings on search engines.

### Requirements

1. Easy to navigate on various screen sizes.
2. Clear information on what the website offers (a movie tracker).
3. Functioning CRUD website to track own movies and view other users' watched movies.
4. Working backend and database management.
5. Visually inviting so users engage longer on the website.
  
### Expectations

1. I expect to be able to login or sign up for an account if I do not have an existing one.
2. I expect to be able to CRUD (create, read, update and delete) my movie trackings.
3. I expect to be able to view other users' movie trackings.
4. I expect screen size not to affect the quality of the website.
5. I expect all information to be correct and accurate.

\
&nbsp;
[Back to Top](#table-of-contents)
\
&nbsp;

# UI / Design Choices

## Moodboard

One of the first milestones of this project was to create a moodboard to help envision the overall house style of the webiite and ensure that all of the sections and elements are cohesive. The software I used to create the moodboard for this website is [Mila Note](https://milanote.com/ "Mila Note").
Below, is the moodboard:
![Moodboard](docs/moodboard.png)

## Fonts

## Icons

## Colours

The colour scheme of the website is inspired by the moodboard (previously depicted). I have used [Coolers](https://coolors.co/ "coolers") to retrieve the desired colour codes and generate the colour palette.

Below, is the color palette:
![Colour Palette](docs/colour-palette.png)

## Media Queries

As a starting point, I have designed this website with a mobile first mindset using the iPhone 5/SE (320px) as the smallest screen size for styling to look good on. Then I created 3 additional media queries for largers devices listed below.

| Screen Size |  Breakpoint |
| ----------- | ----------- | 
| mobile      |  <320px     |
| tablet      |  => 768px   |
| laptop      |  => 1920px  |
| desktop     |  => 2560px  |

\
&nbsp;
[Back to Top](#table-of-contents)
\
&nbsp;


## Wireframes

I have used [Balsamiq](https://balsamiq.com/wireframes/ "Balsamiq") to develop my wireframes for my website. I initially created the mobile version and then the wireframes and then scaled it up for desktop. The website has 3 pages that are all scrollable and displays/hides sections with logic in lieu of having even more HTML pages to decrease inconvenient reloading of entire website.

The wireframes are below:

[Landing Page - Mobile & Desktop Wireframes](docs/wireframes/wireframe-landing-page-mobile-desktop.png "home mobile and desktop wireframes")

[Login Page - Mobile & Desktop Wireframes](docs/wireframes/wireframe-login-page-mobile-desktop.png "login mobile and desktop wireframes")

[Main Page - Mobile & Desktop Wireframes](docs/wireframes/wireframe-landing-page-mobile-desktop.png "main mobile and desktop wireframes")

[Community Page - Mobile & Desktop Wireframes](docs/wireframes/wireframe-community-page-mobile-desktop.png "community mobile and desktop wireframes")

\
&nbsp;
[Back to Top](#table-of-contents)
\
&nbsp;

## Mockups
Based on the wireframes, I created mockups using [Figma](https://www.figma.com/ "Figma") to help me plan the interface design. Mockups for both mobile and desktop have been created as part of the website design phase, and can be viewed via this link [Mockups](https://www.figma.com/design/9iYeCSMx1ZhPTEsWesTW6V/Project-3?node-id=0-1&t=h3CqbXc5uzz9nmsm-1 "Mockups").


\
&nbsp;
[Back to Top](#table-of-contents)
\
&nbsp;

# Features 

## Existing Features

## Future Actions 

\
&nbsp;
[Back to Top](#table-of-contents)
\
&nbsp;

# Technologies used

## Languages

- [HTML](https://en.wikipedia.org/wiki/HTML "HTML")
  
- [CSS](https://en.wikipedia.org/wiki/CSS "CSS")

- [JavaScript](https://en.wikipedia.org/wiki/JavaScript "JavaScript")

- [Python](https://en.wikipedia.org/wiki/Python_(programming_language) "Python")

## IDE

- [Codeanywhere](https://codeanywhere.com/ "Codeanywhere")

- [GitPod](https://www.gitpod.io/ "GitPod")

## Libraries & Framework

- [Google Fonts](https://fonts.google.com/ "Google Fonts")
  
- [Font Awesome library](https://fontawesome.com/ "Font Awesome")

- [Favicon](https://favicon.io/ "Favicon")

- [Flask](https://flask.palletsprojects.com/en/2.3.x/templating/ "Flask")

## Tools

- [Mila Note](https://milanote.com/ "Mila Note")
  
- [Balsamiq](https://balsamiq.com/wireframes/ "Balsamiq")

- [CI Full Template](https://github.com/Code-Institute-Org/ci-full-template "CI Full Template")
  
- [Coolers](https://coolors.co/ "coolers")
  
- [Am I Responsive](https://ui.dev/amiresponsive "Am I Responsive")

- [W3C HTML Validation Service](https://validator.w3.org/ "W3C HTML")
  
- [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/ "W3C CSS")

- [W3C JS Validation Service](https://jshint.com "JSHint JS") 

- [Snyk Python Check Service](https://snyk.io/code-checker/python/ "Snyk Python")

\
&nbsp;
[Back to Top](#table-of-contents)
\
&nbsp;