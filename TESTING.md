# Testing

Return back to the [README.md](README.md) file.

## Code Validation

### Python

I have used the recommended [PEP8 CI Python Linter](https://pep8ci.herokuapp.com) to validate all of my Python files.

| File | CI URL | Passed Screenshot | Errors Screenshot | Notes |
| --- | --- | --- | --- | --- |
| run.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/lunartechfreek/hank-the-hanging-man/main/run.py) | ![Main screenshot](documentation/testing-files/validation/validation-main-fixed.png) | ![Main errors screenshot](documentation/testing-files/validation/validation-main-errors.png) | Passed: Fixed all errors |
| story.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/lunartechfreek/hank-the-hanging-man/main/story.py) | ![Story screenshot](documentation/testing-files/validation/validation-story-fixed.png) | ![Story errors screenshot](documentation/testing-files/validation/validation-story-errors.png) | Passed: Fixed all errors |
| words.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/lunartechfreek/hank-the-hanging-man/main/words.py) | ![Words screenshot](documentation/testing-files/validation/validation-words-fixed.png) | ![Words errors screenshot](documentation/testing-files/validation/validation-words-errors.png) | Passed: Fixed all errors |

## Manual Testing 

### Browser Compatibility

I've tested my deployed project on multiple browsers to check for compatibility issues. To make this as thorough as possible I tested the browsers on a variety of operating systems and devices.

As well as testing on real world devices I wanted to test on other devices that I could not access. For this i used [BrowserStack](https://www.browserstack.com/).

#### Desktop

| Browser | macOS | Windows 11 | Notes |
| --- | --- | --- | --- |
| Chrome | ![Mac chrome screenshot](documentation/testing-files/browser-testing/testing-mac-chrome.png) | ![Windows chrome screenshot](documentation/testing-files/browser-testing/testing-windows-chrome.png) | No issues encountered |
| Edge | ![Mac edge screenshot](documentation/testing-files/browser-testing/testing-mac-edge.png) | ![Windows edge screenshot](documentation/testing-files/browser-testing/testing-windows-edge.png) | No issues encountered |
| Firefox | ![Mac firefox screenshot](documentation/testing-files/browser-testing/testing-mac-firefox-error.png) | ![Windows firefox screenshot](documentation/testing-files/browser-testing/testing-windows-firefox-error.png) | Bug: When displaying an emoji, it splits it in half |
| Opera | ![Mac opera screenshot](documentation/testing-files/browser-testing/testing-mac-opera.png) | ![Windows opera screenshot](documentation/testing-files/browser-testing/testing-windows-opera-.png) | No issues encountered |
| Safari | ![Mac safari screenshot](documentation/testing-files/browser-testing/testing-mac-safari-error.png) | ![Windows safari screenshot](documentation/testing-files/browser-testing/testing-windows-safari-error.png) | macOS: Can not type in terminal. Windows11: Can not show page (very old browser v5.1) |
| Yandex | N/A | ![Windows yandex screenshot](documentation/testing-files/browser-testing/testing-windows-yandex-error.png) | Bug: Emoji not displaying |

#### Mobile

With the application being deployed on [Heroku](https://www.heroku.com/) in a terminal designed by the [Code Institute](https://www.codeinstitute.net/) there are some issues with how the game is displayed on mobile screens. For the purpose of this section I have disregarded these issues and focused on how the game itself behaves on different devices and different browsers.

| Device | Browser | Screenshot | Notes |
| --- | --- | --- | --- |
| Samsung Galaxy s23 | Chrome | ![Galaxy chrome screenshot](documentation/testing-files/browser-testing/testing-mobile-galaxy-s23-chrome.png) | No issues encountered |
| Iphone 14 Pro | Safari | ![Iphone safari screenshot](documentation/testing-files/browser-testing/testing-mobile-iphone14-pro-safari-error.png) | Bug: Not able to type so not able to play game |
| Iphone 15 plus | Chrome | ![Iphone chrome screenshot](documentation/testing-files/browser-testing/testing-mobile-iphone15-plus-chrome-error.png) | Bug: Input not displaying so not able to play game |
| Oneplus 11R | Chrome | ![Oneplus chrome screenshot](documentation/testing-files/browser-testing/testing-mobile-oneplus-11r-chrome.png) | No issues encountered |
| Google Pixel 8 | Edge | ![Pixel edge screenshot](documentation/testing-files/browser-testing/testing-mobile-pixel8-pro-edge.png) | No issues encountered |


#### Tablet

| Device | Browser | Screenshot | Notes |
| --- | --- | --- | --- |
| Samsung Galaxy Tab 9 | Chrome | ![Galaxy tab chrome screenshot](documentation/testing-files/browser-testing/testing-tablet-galaxy-tab-s9-chrome.png) | No issues encountered |
| Samsung Galaxy Tab 9 | Edge | ![Galaxy tab edge screenshot](documentation/testing-files/browser-testing/testing-tablet-galaxy-tab-s9-edge.png) | No issues encountered |
| Ipad 10th Gen | Chrome | ![Ipad chrome screenshot](documentation/testing-files/browser-testing/testing-tablet-ipad-chrome-error.png) | Bug: Unable to type, not able to play game |
| Ipad 10th Gen | Safari | ![Ipad safari screenshot](documentation/testing-files/browser-testing/testing-tablet-ipad-safari-error.png) | Bug: When displaying an emoji, it splits it in half |

### Responsiveness

I've tested my deployed project on multiple devices to check for responsiveness issues.

| Device | Test Type | Screenshot | Notes |
| --- | --- | --- | --- |
| Macbook Pro | Physical | ![Macbook Pro screenshot](documentation/testing-files/responsiveness-testing/responsiveness-macbook-pro.png) | No issues |
| Iphone 15 ProMax | Physical | ![Iphone 15 ProMax screenshot](documentation/testing-files/responsiveness-testing/responsiveness-mobile-iphone-15-pro-max.png) | Content does not fit screen |
| Desktop | Virtual | ![Desktop screenshot](documentation/testing-files/browser-testing/testing-windows-edge.png) | No issues |
| Galaxy S23 | Virtual | ![Galaxy S23 screenshot](documentation/testing-files/browser-testing/testing-mobile-galaxy-s23-chrome.png) | Content does not fit screen |
| Oneplus 11R | Virtual | ![Oneplus 11R screenshot](documentation/testing-files/browser-testing/testing-mobile-oneplus-11r-chrome.png) | Content does not fit screen |
| Pixel 8 | Virtual | ![Pixel 8 screenshot](documentation/testing-files/browser-testing/testing-mobile-pixel8-pro-edge.png) | Content does not fit screen |
| Galaxy Tab 9 | Virtual | ![Galaxy Tab 9 screenshot](documentation/testing-files/browser-testing/testing-tablet-galaxy-tab-s9-chrome.png) | No issues |
| Ipad 10th Gen | Virtual | ![Ipad 10th Gen screenshot](documentation/testing-files/browser-testing/testing-tablet-ipad-safari-error.png) | No issues |
| Galaxy Fold | Devtools | ![Galaxy Fold screenshot](documentation/testing-files/responsiveness-testing/responsiveness-galaxy-fold.png) | Content does not fit screen |
| Galaxy Surface Duo | Devtools | ![Galaxy Surface Duo screenshot](documentation/testing-files/responsiveness-testing/responsiveness-surface-duo.png) | Content does not fit screen |
| Galaxy Surface Pro | Devtools | ![Galaxy Surface Pro screenshot](documentation/testing-files/responsiveness-testing/responsiveness-surface-pro-7.png) | Content does not fit screen |



## Lighthouse Audit

I've tested my deployed project using the Lighthouse Audit tool to check for any major issues.

| Page | Desktop | Mobile |
| --- | --- | --- |
| Home | ![Desktop screenshot](documentation/testing-files/lighthouse/lighthouse-desktop.png) | ![Mobile screenshot](documentation/testing-files/lighthouse/lighthouse-mobile.png) |

### Notable Errors

After running my lighthouse report there was only one notable error. This was on the desktop report under the SEO section. The error was regarding the template provided to me by the [Code Institute](https://www.codeinstitute.net/). In the layout.html file there was no meta description in the head of the document summarising the content of the page. This would be added as a future development to change the SEO score from amber to green.

![Lighthouse error screenshot](documentation/testing-files/lighthouse/lighthouse-warning.png)

## Defensive Programming

Defensive programming was manually tested with the below user acceptance testing:

| Feature | Expectation | Test | Result | Screenshot |
| --- | --- | --- | --- | --- |
| Game Start |  |  |  |  |
|  | Game loaded on page load | Load webpage application is hosted on | Passed: Game loaded | ![Game load screenshot](documentation/testing-files/defensive-programming/defensive-load.png) |
| Name Input |  |  |  |  |
|  | If a valid name is entered, how to play will be displayed | Enter valid name | Passed: How to play displayed | ![How to screenshot](documentation/testing-files/defensive-programming/defensive-how-to.png) |
|  | If a number is entered, invalid entry message will display and return the number entered | Type number | Passed: Invalid message displayed | ![Invalid number screenshot](documentation/testing-files/defensive-programming/defensive-name-input-number.png) |
|  | If a special character is entered, invalid entry message will display and return the character entered | Type special character | Passed: Invalid message displayed | ![Invalid character screenshot](documentation/testing-files/defensive-programming/defensive-name-input-special.png) |
|  | If a space is entered, invalid entry message will display and return spacebar was pressed | Press spacebar | Passed: Invalid message displayed | ![Invalid space screenshot](documentation/testing-files/defensive-programming/defensive-name-input-space.png) |
|  | If the user presses enter, invalid entry message will display and return enter was pressed | Press enter | Passed: Invalid message displayed | ![Invalid enter screenshot](documentation/testing-files/defensive-programming/defensive-name-input-enter.png) |
| How To Play |  |  |  |  |
|  | If 'Y' is entered on how to play input, the instructions will be displayed | Enter 'Y' | Passed: Instructions displayed | ![Instructions screenshot](documentation/testing-files/defensive-programming/defensive-instructions.png) |
|  | If 'N' is entered on how to play input, the introduction will be displayed | Enter 'N' | Passed: Introduction displayed | ![Introduction screenshot](documentation/testing-files/defensive-programming/defensive-intro.png) |
|  | If an incorrect letter is entered, invalid entry message will display and return the letter entered | Type incorrect letter | Passed: Invalid message displayed | ![Invalid letter screenshot](documentation/testing-files/defensive-programming/defensive-how-to-incorrect-letter.png) |
|  | If a number is entered, invalid entry message will display and return the number entered | Type number | Passed: Invalid message displayed | ![Invalid number screenshot](documentation/testing-files/defensive-programming/defensive-how-to-number.png) |
|  | If a special character is entered, invalid entry message will display and return the character entered | Type special character | Passed: Invalid message displayed | ![Invalid character screenshot](documentation/testing-files/defensive-programming/defensive-how-to-special.png) |
|  | If a space is entered, invalid entry message will display and return spacebar was pressed | Press spacebar | Passed: Invalid message displayed | ![Invalid space screenshot](documentation/testing-files/defensive-programming/defensive-how-to-space.png) |
|  | If the user presses enter, invalid entry message will display and return enter was pressed | Press enter | Passed: Invalid message displayed | ![Invalid enter screenshot](documentation/testing-files/defensive-programming/defensive-how-to-enter.png) |
| Instructions |  |  |  |  |
|  | If 'Y' is entered on instructions input, the introduction will be displayed | Enter 'Y' | Passed: Introduction displayed | ![Introduction screenshot](documentation/testing-files/defensive-programming/defensive-intro.png) |
|  | If an incorrect letter is entered, invalid entry message will display and return the letter entered | Type incorrect letter | Passed: Invalid message displayed | ![Invalid letter screenshot](documentation/testing-files/defensive-programming/defensive-instructions-incorrect-letter.png) |
|  | If a number is entered, invalid entry message will display and return the number entered | Type number | Passed: Invalid message displayed | ![Invalid number screenshot](documentation/testing-files/defensive-programming/defensive-instructions-number.png) |
|  | If a special character is entered, invalid entry message will display and return the character entered | Type special character | Passed: Invalid message displayed | ![Invalid character screenshot](documentation/testing-files/defensive-programming/defensive-instructions-special.png) |
|  | If a space is entered, invalid entry message will display and return spacebar was pressed | Press spacebar | Passed: Invalid message displayed | ![Invalid space screenshot](documentation/testing-files/defensive-programming/defensive-instructions-space.png) |
|  | If the user presses enter, invalid entry message will display and return enter was pressed | Press enter | Passed: Invalid message displayed | ![Invalid enter screenshot](documentation/testing-files/defensive-programming/defensive-instructions-enter.png) |
| Introduction |  |  |  |  |
|  | If 'Y' is entered on introduction input, the select difficulty will be displayed | Enter 'Y' | Passed: Select difficulty displayed | ![Select difficulty screenshot](documentation/testing-files/defensive-programming/defensive-select-difficulty.png) |
|  | If 'N' is entered on introduction input, the application will quit | Enter 'N' | Passed: Goodbye message displayed | ![Goodbye screenshot](documentation/testing-files/defensive-programming/defensive-intro-type-n.png) |
|  | If an incorrect letter is entered, invalid entry message will display and return the letter entered | Type incorrect letter | Passed: Invalid message displayed | ![Invalid letter screenshot](documentation/testing-files/defensive-programming/defensive-intro-incorrect-letter.png) |
|  | If a number is entered, invalid entry message will display and return the number entered | Type number | Passed: Invalid message displayed | ![Invalid number screenshot](documentation/testing-files/defensive-programming/defensive-intro-number.png) |
|  | If a special character is entered, invalid entry message will display and return the character entered | Type special character | Passed: Invalid message displayed | ![Invalid character screenshot](documentation/testing-files/defensive-programming/defensive-intro-special.png) |
|  | If a space is entered, invalid entry message will display and return spacebar was pressed | Press spacebar | Passed: Invalid message displayed | ![Invalid space screenshot](documentation/testing-files/defensive-programming/defensive-intro-space.png) |
|  | If the user presses enter, invalid entry message will display and return enter was pressed | Press enter | Passed: Invalid message displayed | ![Invalid enter screenshot](documentation/testing-files/defensive-programming/defensive-intro-enter.png) |
| Select Difficulty |  |  |  |  |
|  | If 'E' is entered on select difficulty input, game starts with easy difficulty | Enter 'Y' | Passed: Easy difficulty displayed | ![Easy difficulty screenshot](documentation/testing-files/defensive-programming/defensive-game-easy.png) |
|  | If 'M' is entered on select difficulty input, game starts with medium difficulty | Enter 'N' | Passed: Medium difficulty displayed | ![Medium difficulty screenshot](documentation/testing-files/defensive-programming/defensive-game-medium.png) |
|  | If 'H' is entered on select difficulty input, game starts with hard difficulty | Enter 'Y' | Passed: Hard difficulty displayed | ![Hard difficulty screenshot](documentation/testing-files/defensive-programming/defensive-game-hard.png) |
|  | If 'Q' is entered on select difficulty input, the application will quit | Enter 'Q' | Passed: Goodbye message displayed | ![Goodbye message screenshot](documentation/testing-files/defensive-programming/defensive-difficulty-type-q.png) |
|  | If an incorrect letter is entered, invalid entry message will display and return the letter entered | Type incorrect letter | Passed: Invalid message displayed | ![Invalid letter screenshot](documentation/testing-files/defensive-programming/defensive-difficulty-incorrect-letter.png) |
|  | If a number is entered, invalid entry message will display and return the number entered | Type number | Passed: Invalid message displayed | ![Invalid number screenshot](documentation/testing-files/defensive-programming/defensive-difficulty-number.png) |
|  | If a special character is entered, invalid entry message will display and return the character entered | Type special character | Passed: Invalid message displayed | ![Invalid character screenshot](documentation/testing-files/defensive-programming/defensive-difficulty-special.png) |
|  | If a space is entered, invalid entry message will display and return spacebar was pressed | Press spacebar | Passed: Invalid message displayed | ![Invalid space screenshot](documentation/testing-files/defensive-programming/defensive-difficulty-space.png) |
|  | If the user presses enter, invalid entry message will display and return enter was pressed | Press enter | Passed: Invalid message displayed | ![Invalid enter screenshot](documentation/testing-files/defensive-programming/defensive-difficulty-enter.png) |
| Game |  |  |  |  |
|  | If a letter is entered on game input, the letter appears in 'Guessed letters' | Guess letter | Passed: Letter in 'Guessed letters' | ![Guessed letters screenshot](documentation/testing-files/defensive-programming/defensive-game-guessed-letters.png) |
|  | If a correct letter is entered on game input, a well done message is displayed | Guess correct letter | Passed: Well done displayed | ![Letter correct screenshot](documentation/testing-files/defensive-programming/defensive-game-letter-correct.png) |
|  | If an incorrect letter is entered on game input, an incorrect message is displayed and hangman image updated | Guess incorrect letter | Passed: Incorrect message displayed and hangman image updated | ![Letter incorrect screenshot](documentation/testing-files/defensive-programming/defensive-game-letter-incorrect.png) |
|  | If a correct word is entered on game input, a well done message is displayed and replay question appears | Guess correct word | Passed: Well done and replay question displayed | ![Correct word screenshot](documentation/testing-files/defensive-programming/defensive-game-word-correct.png) |
|  | If an incorrect word is entered on game input, an incorrect message is displayed and hangman image updated | Guess incorrect word | Passed: Incorrect message displayed and hangman image updated | ![Word incorrect screenshot](documentation/testing-files/defensive-programming/defensive-game-word-incorrect.png) |
|  | If an incorrect length word is entered on game input while playing on easy, an incorrect length message is displayed and no lives lost | Guess incorrect length word | Passed: Incorrect length message displayed and prompt of letter length | ![Incorrect length easy mode screenshot](documentation/testing-files/defensive-programming/defensive-game-easy-word-guess.png) |
|  | If an incorrect length word is entered on game input while playing on medium, an incorrect message is displayed and hangman image updated | Guess incorrect length word | Passed: Incorrect message displayed and hangman image updated | ![Incorrect length medium mode screenshot](documentation/testing-files/defensive-programming/defensive-game-medium-word-guess.png) |
|  | If an incorrect length word is entered on game input while playing on hard, an incorrect message is displayed and hangman image updated | Guess incorrect length word | Passed: Incorrect message displayed and hangman image updated | ![Incorrect length hard mode screenshot](documentation/testing-files/defensive-programming/defensive-game-hard-word-guess.png) |
|  | If a number is entered, invalid entry message will display and return the number entered | Type number | Passed: Invalid message displayed | ![Invalid number screenshot](documentation/testing-files/defensive-programming/defensive-game-number.png) |
|  | If a special character is entered, invalid entry message will display and return the character entered | Type special character | Passed: Invalid message displayed | ![Invalid character screenshot](documentation/testing-files/defensive-programming/defensive-game-special.png) |
|  | If a space is entered, invalid entry message will display and return spacebar was pressed | Press spacebar | Passed: Invalid message displayed | ![Invalid space screenshot](documentation/testing-files/defensive-programming/defensive-game-space.png) |
|  | If the user presses enter, invalid entry message will display and return enter was pressed | Press enter | Passed: Invalid message displayed | ![Invalid enter screenshot](documentation/testing-files/defensive-programming/defensive-game-enter.png) |
| Game End |  |  |  |  |
|  | If 'Y' is entered on game end input, the game will restart and select difficulty will be displayed | Enter 'Y' | Passed: Select difficulty displayed | ![Select difficulty screenshot](documentation/testing-files/defensive-programming/defensive-select-difficulty.png) |
|  | If 'N' is entered on game end input, the game will quit and goodbye message will be displayed | Enter 'N' | Passed: Goodbye message displayed | ![Goodbye message screenshot](documentation/testing-files/defensive-programming/defensive-game-end-type-n.png) |
|  | If an incorrect letter is entered, invalid entry message will display and return the letter entered | Type incorrect letter | Passed: Invalid message displayed | ![Invalid letter screenshot](documentation/testing-files/defensive-programming/defensive-replay-incorrect-letter.png) |
|  | If a number is entered, invalid entry message will display and return the number entered | Type number | Passed: Invalid message displayed | ![Invalid number screenshot](documentation/testing-files/defensive-programming/defensive-replay-number.png) |
|  | If a special character is entered, invalid entry message will display and return the character entered | Type special character | Passed: Invalid message displayed | ![Invalid character screenshot](documentation/testing-files/defensive-programming/defensive-replay-special.png) |
|  | If a space is entered, invalid entry message will display and return spacebar was pressed | Press spacebar | Passed: Invalid message displayed | ![Invalid space screenshot](documentation/testing-files/defensive-programming/defensive-replay-space.png) |
|  | If the user presses enter, invalid entry message will display and return enter was pressed | Press enter | Passed: Invalid message displayed | ![Invalid enter screenshot](documentation/testing-files/defensive-programming/defensive-replay-enter.png) |

## Bugs

I encountered many bugs throughout my project, the most notable ones are as follows:

- Hangman image displaying incorrectly.

    ![Display hangman bug screenshot](documentation/testing-files/bugs/bug-display-hangman.png)

    - To fix this I added an extra `\` to the arm and leg so that the program would read it as a literal backslash and not as an escape character. I found this fix to my bug on [Chat GPT](https://chat.openai.com/).

- If a correct letter was guessed by the user, it was not replacing the `_` with the letter and its position inside the hidden game word.

    ![Update word letters bug screenshot](documentation/testing-files/bugs/bug-update-word-letter.png)

    - To fix this I adjusted my `letter_guess()` function by first assigning the `update_word()` function to the `word_completion` variable rather than just calling the `update_word()` function. And then finally returning the result of the `update_word()` function.

- If an incorrect letter was guessed by the user the hangman image was not updating.  

    ![Update hangman bug screenshot](documentation/testing-files/bugs/bug-update-hangman.png)

    - To fix this I by changed the variable `tries` to a global variable. This was needed to be done because the value of `tries` was being modified inside a function that it was not declared in so needed to be changed to a global scope. 

- When the correct word was guessed it did not end the game and congratulate the user for winning. 

    ![Word guess bug screenshot one](documentation/testing-files/bugs/bug-word-guess.png)
    ![Word guess bug screenshot two](documentation/testing-files/bugs/bug-word-guess-two.png)

    - To fix this I changed the variable `guessed` to a global variable. This was needed to be done because the value of `guessed` was being modified inside a function that it was not declared in so needed to be changed to a global scope to update the value to true when the word was correctly guessed, and run the `game_end()` function. 

- When the user guessed a word that was a different length to the word it was showing an invalid entry error. 

    ![Invalid word length bug screenshot](documentation/testing-files/bugs/bug-invalid-word-length.png)

    - To fix this I changed the if statement to stop checking if the guess length was equal to the word length,  and instead check that the length of the guess was over one. I then went further into this and changed my `word_guess()` function to check if the game was being played in easy mode. If it was then the user would receive an error message saying that the guess was the wrong length. I did this to make easy mode slightly easier. If the user was playing medium or hard mode then the user would lose a life if the word guess was incorrect regardless of the length. 

## Unfixed Bugs

- The first unfixed bug that I know of is regarding the responsiveness tests on mobile devices. The terminal provided does not fit the screen correctly. This is a known issue with the [Code Institute](https://www.codeinstitute.net/) template that I am required to use for this project.

    - | Galaxy Fold | Galaxy S23 | Oneplus 11R
      | --- | --- | --- |
      | ![Galaxy Fold screenshot](documentation/testing-files/responsiveness-testing/responsiveness-galaxy-fold.png) | ![Galaxy S23 screenshot](documentation/testing-files/browser-testing/testing-mobile-galaxy-s23-chrome.png) |![Oneplus 11R screenshot](documentation/testing-files/browser-testing/testing-mobile-oneplus-11r-chrome.png) |

- The second unfixed bug was found during my browser testing. This was that the program did not run correctly on Safari because you could not enter anything into the first input. Without the use of the input feature, this game would be unplayable on this browser. This bug is again a known issue with the template provided by the [Code Institute](https://www.codeinstitute.net/).

    - ![Safari error screenshot](documentation/testing-files/browser-testing/testing-mac-safari-error.png)

- The third unfixed bug I found was that emojis do not display correctly on some browsers. The two I found on desktop browsers are Firefox and Yondex. On Firefox it only shows half the emoji, and on Yondex it replaces it with a 0. Interestingly the iPad 10th Gen on safari also shows only half the emoji but all other macOS and iOS products do not have this exact issue. 

- | Firefox | Yandex | Safari (iPad)
  | --- | --- | --- |
  | ![Firefox screenshot](documentation/testing-files/browser-testing/testing-mac-firefox-error.png) | ![Yandex screenshot](documentation/testing-files/browser-testing/testing-windows-yandex-error.png) | ![Safari (iPad) screenshot](documentation/testing-files/browser-testing/testing-tablet-ipad-safari-error.png) |

There are no remaining bugs that I am aware of.
