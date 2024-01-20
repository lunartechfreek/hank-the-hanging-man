# Hank The Hanging Man

![screenshot](documentation/readme-files/preview.png)

[Click here to view the live project](https://hank-the-hanging-man-8f469cffdce1.herokuapp.com)

## Introduction

Hank The Hanging Man is a game made for educational purposes for my third portfolio project in software development that I am studying with the [Code Institute](https://www.codeinstitute.net/). It is aimed at people who want to have fun, test their knowledge, and also train their brain.

The project is generally a game of hangman but to make the game more interesting and appealing than the typical game of hangman people are used to playing, I added a story narrative to enhance the users experience. While designing this game I wanted my target audience to be users of all levels of intelligence so I added three different difficulty levels so that every user could have an enjoyable experience without finding the game either too challenging, or too easy. I wanted to also create a game that the user would want to return to, and play again so I designed it in a way that some of the statements would change every time the game is played to avoid repetition. 

I have applied the the technologies I have learnt so far in python to create my game. Other technologies used are listed in the technologies used section further down the page.

## UX

I wanted to make a game of hangman which will be played on the command line. I wanted to try to make the game a bit more interesting that the average hangman game by creating a story narrative to engage the user. This story consists of an introduction, and various messages that are displayed at certain points through the game depending on how many lives the user has left. These messages are taken from a list in a separate file and consist of multiple messages and only one is displayed at random to the user. I did this so the messages would vary each time the game is played so the user will not find the messages repetitive and will make the game more repayable. To further make the game more repayable I also added three different difficulties each consisting of 50 words. I added an extra feature to the easy difficulty which means the user will not lose a life if they guess a word of an incorrect length just to make the easy difficulty a lot easier than the other two.

I designed the game to consist of various sections which are displayed in a certain order to the user. After the user enters the desired input the terminal clears before displaying the next section. I did this so the terminal would not get cluttered and only display the relevant content for each section without the content from the last section still being displayed above. 

### Colour Palette

With this being a command line game, the main game area consisted of black and white. The template provided to me by [Code Institute](https://www.codeinstitute.net/) placed this game area on a white background and added a orange run program button at the top of the game. 

To make my game more visually appealing I installed the external module [Colorama](https://pypi.org/project/colorama/) to add colour to my print statements. I wanted to do this to help the user have a more enjoyable experience than they would on the standard black and white terminal.  I also did this to emphasise to the user whether the answer they gave was correct or incorrect. 

I used the colour green to highlight various parts of my correct statements including the letter or word guessed, and the users name. By also highlighting the name I felt that it was directly congratulating them to engage them. 

For my incorrect statements I used red to highlight the letter or word guessed and the users name. Again by highlighting their name in red I felt It was more engaging and directly emphasising that they were wrong. I also used the colour red for my invalid statements to emphasise that the input entered was not correct. 

I also added colour to the difficulty narratives. I used green for easy, cyan for medium, and red for hard. 

I used [Coolers](https://coolors.co/ffffff-2ed1d1-83d932-e84610-ed2828-000000) to use their colour pick tool to create a palette of the various colours used throughout the game, and also the colours used in the template provided to me by the [Code Institute](https://www.codeinstitute.net/).

![Colour Palette](documentation/readme-files/colour-palette.png)

### Contrast Grid

I used [Contrast Grid Eight Shapes](https://contrast-grid.eightshapes.com/?version=1.1.0&background-colors=&foreground-colors=%2383D932%0D%0A%23ED2828%0D%0A%23E84610%0D%0A%232ED1D1%0D%0A%23000000%0D%0A%23FFFFFF&es-color-form__tile-size=compact&es-color-form__show-contrast=aaa&es-color-form__show-contrast=aa&es-color-form__show-contrast=aa18&es-color-form__show-contrast=dnp) to check that all of the colours I had chosen from the [Colorama](https://pypi.org/project/colorama/) module were a good contrast to the black game background. 

![Contrast Grid](documentation/readme-files/contrast-grid.png)

