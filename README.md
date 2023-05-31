<h1>CookBook Project: What to eat in Ireland</h1>

<p>The "CookBook Project: What to eat in Ireland" is a culinary exploration aimed at showcasing the rich and diverse traditional Irish cuisine. The project will compile a comprehensive cookbook that highlights authentic Irish dishes, including beloved classics and lesser-known regional specialties, while also delving into the cultural and historical significance of each recipe. Through this project, food enthusiasts and travelers alike will be able to discover and savor the flavors of Ireland's gastronomic heritage.</p>

## **[Live site](https://cookbook-igor.herokuapp.com//)**

---

## **[Repository](https://github.com/Sergutin/CookBook)**

## Table of contents

* [Technologies Used](#technologies-used)
  * [HTML](#html)
  * [CSS](#css)
  * [JavaScript](#javascript)
  * [Python](#python)
  * [Django](#django)
  * [Bootstrap 5](#bootstrap-5)
  * [Cloudinary](#cloudinary)
  * [Heroku PostgreSQL](#heroku-postgresql)
* [UX Design](#ux-design)
  * [Overview](#overview)
  * [Design](#design)
  * [Website User](#website-user)
  * [Main goals](#main-goals)
* [Agile methodology](#agile-methodology)
* [User Stories](#user-stories)
* [Features](#features)
* [Testing](#testing)



  * [HTML](#html)
  * [CSS](#css)
  * [JSHint](#jshint)
  * [Lighthouse](#lighthouse)
  * [Manual Testing](#manual-testing)
  * [Fixed Bugs](#fixed-bugs)
  * [Unfixed Bugs](#unfixed-bugs)
* [Deployment](#deployment)
  * [Cloning and forking](#cloning-and-forking)
* [Media](#media)


## UX Design
<p>Responsive on all device sizes</p>
<p>Interactive elements</p>

  ### Overview
<p>The main idea of the game is immediately evident to users, i.e. the landing page shows the image of the child playing cards with two matching cards in his hand.</p>
<p>This section provides a brief explanation of the game and allows users to easily start the game from the main page just clicking the "Let's Start the Game" button.</p>

<img src="assets/images/readme/main.jpg" width=600px height=auto>

  ### Design 
<p>After clicking "Let's Start the Game" button users are getting moved to the next (game) page where they can pick the level of the game: "easy" (2x2 cards) or "normal" (4x4).</p>

<img src="assets/images/readme/levels.jpg" width=600px height=auto>

  ### Website User
<p>The "home" button is located at the bottom of the game page, allowing users to open the main page of the game.</p>

<img src="assets/images/readme/home.jpg" width=200px height=auto>

  ### Main goals
<p>After clicking the "Easy Game" button users see the card game field 2x2 cards with car image on the back side.</p>
<p>Player clicks on the cards to flip them over. If the two cards have the same image (car logo), then player continues with the next cards, otherwise the cards turn face down.</p>

<img src="assets/images/readme/easy.jpg" width=600px height=auto>
<br>
<img src="assets/images/readme/easy2.jpg" width=600px height=auto>


## Agile methodology


## User Stories

 1. [USER STORY: Registration](https://github.com/Sergutin/CookBook/issues/7)
 2. [USER STORY: Log in](https://github.com/Sergutin/CookBook/issues/8)
 3. [USER STORY: Log out](https://github.com/Sergutin/CookBook/issues/5)
 4. [USER STORY: Site pagination](https://github.com/Sergutin/CookBook/issues/9)
 5. [USER STORY: Create recipe](https://github.com/Sergutin/CookBook/issues/10)
 6. [USER STORY: Edit recipe](https://github.com/Sergutin/CookBook/issues/3)
 7. [USER STORY: Delete recipe](https://github.com/Sergutin/CookBook/issues/4)
 8. [USER STORY: Rate / review recipes](https://github.com/Sergutin/CookBook/issues/11)
 9. [USER STORY: Comment](https://github.com/Sergutin/CookBook/issues/2)
 10. [USER STORY: Like and unlike recipes](https://github.com/Sergutin/CookBook/issues/1)

  ### HTML 
<p>No errors were returned when passing through the official W3C validator testing</p>

<img src="assets/images/readme/html-test1.jpg" width=600px height=auto>
<img src="assets/images/readme/html-test2.jpg" width=600px height=auto>

  ### CSS 
<p>No errors were found when passing through the official (Jigsaw) CSS validator</p>

<img src="assets/images/readme/css-test1.jpg" width=600px height=auto>
<img src="assets/images/readme/css-test2.jpg" width=600px height=auto>

  ### JSHint 
<p>No errors were found when passing through the official (JSHint) JavaScript validator.
Two unused variables "startEasyGame" and "startNormalGame" are being called using "button onclick" event from the Game page.</p>

<img src="assets/images/readme/jshint.jpg" width=600px height=auto>

  ### Lighthouse
<p>The website was measured using Lighthouse tool, performance 100% was calculated for desktop device and 100% for mobile device:</p>

<img src="assets/images/readme/lhm.jpg" width=600px height=auto>
<br>
<img src="assets/images/readme/lhd.jpg" width=600px height=auto>

  ### Manual testing
<p>Responsiveness was tested in different browsers:</p>
<li>Chrome</li>
<img src="assets/images/readme/chrome.jpg" width=600px height=auto>
<li>Safari</li>
<img src="assets/images/readme/safari.jpg" width=600px height=auto>
<li>Firefox</li>
<img src="assets/images/readme/firefox.jpg" width=600px height=auto>

<p>Tests were completed in following browsers from mobile device (iOS):</p>
<li>Chrome</li>
<img src="assets/images/readme/chromem.jpg" width=600px height=auto>
<li>Safari</li>
<img src="assets/images/readme/safarim.jpg" width=600px height=auto>

<p>No broken links found, everything works as expected.</p>

  ### Fixed Bugs
<p>During the project there were a few bugs and errors that have been fixed.</p>
<ul>
<li>Bug Number One: "You Win" window appeared every time after 2 matching pairs (for "easy" and for "normal" game as well, while for "normal" game it supposed to appear after 8 matching pairs rather than 2).</li>
<p>Solution: JavaScript function matchCards was amended from:</p>
<img src="assets/images/readme/bug1.jpg" width=300px height=auto>
<p>to:</p>
<img src="assets/images/readme/bug1fix.jpg" width=300px height=auto>
<p>Additionally a global variable "level" was added with a default value of "null". It helped to solve the issue.</p>
<li>Bug Number Two: Shuffle function didn't work properly for easy game, it was taking random cards from the whole array (8 cards) rather than from the first two cards.</li>
<p>Solution: "shuffleCard" function was moved from "matchCard" function to the very beginning of the game, when users decide which game to play (easy / normal). Code with a bug:</p>
<img src="assets/images/readme/bug2.jpg" width=300px height=auto>
<p>Code after the fix:</p>
<img src="assets/images/readme/bug2fix.jpg" width=300px height=auto>
<li>Bug Number Three: Last four images in Normal game were not visible, just alt description was available.</li>
<img src="assets/images/readme/bug3.jpg" width=500px height=auto>
<p>Solution: forEach function (within shuffleCard function) was trying to run through all the cards, including the ones were hidden (when "Normal" game is being played, "Easy" game cards are being hidden). Another function "shuffleEasyCard" was implemented to separate cards for "normal" game and the ones for "easy" game. It solved the issue.</p>
</ul>

  ### Unfixed Bugs
<p>There are no known unfixed bugs in the code</p>

## Deployment
<p>The site is deployed using GitHub Pages.</p>
<p>To deploy the site using GitHub Pages:</p>
<ol>
<li>Login or signup to Github.</li>
<li>Go to the repository for this project, https://github.com/Sergutin/CardMemoryGame</li>
<li>At the top of the repository, locate the "Settings" button on the menu.</li>
<li>Select "Pages" section in the left hand menu.</li>
<li>From the "Source" dropdown select "Deploy from a Branch". Press "Save".</li>
<li>The site has now been deployed, please note that the process may take a few minutes before the site goes live.</li>
</ol>

  ### Cloning and forking
<p>Forking a repository creates a copy of the original repository on GitHub account.
To fork a repository in GitHub:</p>
<ol>
<li>On GitHub.com, navigate to the repository.</li>
<li>In the top-right corner of the page, click Fork.</li>
<img src="assets/images/readme/fork.jpg" width=200px height=auto>
<li>Select an owner for the forked repository.</li>
<li>By default, forks are named the same as their parent repositories. You can change the name of the fork to distinguish it further.</li>
<li>Optionally, add a description of your fork.</li>
<li>Choose whether to copy only the default branch or all branches to the new fork. For many forking scenarios, such as contributing to open-source projects, you only need to copy the default branch. By default, only the default branch is copied.</li>
<li>Click Create fork.</li>
</ol>

<p>Cloning a repository creates a copy of the original repository on our local machine.
To clone a repository in GitHub:</p>
<ol>
<li>On GitHub.com, navigate to your fork of the repository.</li>
<li>Above the list of files, click  Code.</li>
<img src="assets/images/readme/code.jpg" width=350px height=auto>
<li>Copy the URL for the repository.</li>
<ul>
    <li>To clone the repository using HTTPS, click the "Copy" icon on the right of "HTTPS".</li>
<img src="assets/images/readme/clone.jpg" width=500px height=auto>
<li>To clone the repository using an SSH key, including a certificate issued by your organization's SSH certificate authority, click SSH, then click the icon on the right to copy it.</li>
  <li>To clone a repository using GitHub CLI, click GitHub CLI, then click the "Copy" icon on the right.</li>
</ul>
</ol>

## Media
<p>The main page image was taken from https://sightwords.com/images/memory/memory.jpg</p>
<p>The back card image of the car was adapted from https://pictures.dealer.com/c/currychevroletscarsdale/1429/5f5b6bc6d929fb8039c58ab125c0f7a7x.jpg?impolicy=downsize&w=568</p>
<p>Car logos were taken from https://similarpng.com/</p>
<p>"You Win" image was taken from https://pbs.twimg.com/media/Fg48ZrfXgAAiPR0?format=jpg&name=large</p>