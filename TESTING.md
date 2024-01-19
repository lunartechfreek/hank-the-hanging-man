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
| Iphone 15 ProMax | Physical | ![Iphone 15 ProMax screenshot]() |  |
| Iphone 14 Plus | Physical | ![Iphone 14 Plus screenshot]() |  |
|  |  | ![screenshot]() |  |
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
| Home | ![Desktop screenshot](documentation/lighthouse-desktop.png) | ![Mobile screenshot](documentation/lighthouse-mobile.png) |

### Notable Errors

After running my lighthouse report there was only one notable error. This was on the desktop report under the SEO section. The error was regarding the template provided to me by the [Code Institute](https://www.codeinstitute.net/). In the layout.html file there was no meta description in the head of the document summarising the content of the page. This would be added as a future development to change the SEO score from amber to green.

