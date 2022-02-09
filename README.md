🔴🟠🟢

# Board paper

## Useful Links

Test Plan

https://efrei365net-my.sharepoint.com/:x:/g/personal/maxence_chambrin_efrei_net/EQZq64HNTrpEtA3d5zU8TXUBKTDWapDiwypr0BkL4UajTw?rtime=wgyna9Lr2Ug

Bug Tracker 

https://github.com/louminod/f.hr.dmerej.info/projects/1

## *18/01/2022*

Objective of the day :
- Make the test plan 🟢
- Do the first run 🟢
- Put first run bugs in tracker 🟢

### Make the test plan
Each website functionalities seen had been put in the test plan.
We detected "logical" uses and created the appropriate tests

### Do the first run
First run had been executed.
Result had been written down on the excel.
We found lot of bugs.

### Put first run bugs in tracker
Bugs had been reported to the bug tracker

### Conclusion
Lot of bugs had been founded.
Some of them are minor (syntax) but the others are pretty criticals (stack trace, wrong redirects)

## *26/01/2022*

Objective of the day :
- Run the test plan for the second time 🟢
- Put second run bugs in tracker & update olders 🟢
- Automate the tests 🟠

### Run the test plan for the second time
We ran the test plan on the version **1.0.2** of the website to look for patched bugs.

### Put second run bugs in tracker & update olders
We updated the status of the current reported bugs and added the new ones.

### Automate the tests
We setup playwright and started to automate tests.
We already have at least one test working.

## *09/02/2022*

Objective of the day :
- Continue automating the tests using playwright
- setup the project with the full website backend
- create direct database tests inside the source code

### Continue automating the tests using playwright
We continue from where we left off last time, by writing more playwright tests.
We've added a few more, with different levels of complexity.

### setup the project with the full website backend
Following the guidelines given on the main project page, we setup the django local server to start using the site source code.

### create direct database tests inside the source code
Using our different tests, we check how the code is, add tests and see what can be enhanced and how.

## Conclusion
There are still some bugs we could test, but we're lacking time.
To make the most of our time, we split out team up on the work on hand, but we might have not given enough focus on certain points.


### White-box testing
While we're now in possession of the source code, writing tests for it is still not an easy job.
We need to first understand how it is written, then write the tests checking for the functionnalities we expect the application to fulfill.
After that, there still is a risk of us not understanding how the code works, making our tests possibly redundant, or incorrect.

### Other ideas to reduce the bugs in the application

### Our opinion on the different testing strategies used in the 4 sequences, and their pros and cons

*Manual Testing*

Pros :
- Clear user result
- Work easily split among the team members

Cons :
- Slow
- Repetitive
- Prone to human error
- Impossible to do every kind of tests easily 

*Automatic on Black-box*

Pros :
- A lot of different kinds of tests are possible
- Easy to setup

Cons :
- Cannot access deep parts of the site
- requires smart thinkering to achieve tests easily done through white-box

*Automatic on White-box*

Pros :
- Total access to the code and functionnalities
- Most efficient, and fastest to run
- Can be run without affecting a production server
- Can be automated before serving production

Cons :
- Requires comprehension of the code and language used for the project
- Requires access to the source code
- Requires setting up the project development envirronment correctly

