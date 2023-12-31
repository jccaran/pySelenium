# The Ask

Setup an automation environment on your local machine using Selenium
Automate any cases that you would think are good to test the functionality of validating logging into hudl.com ( http://hudl.com/ ).

Ignore social logins (Facebook, Google, Apple, etc.) and account creation. Automate only functionality around using credentials.
Push your tests to a GitHub repository (a public repo is fine) and share the link (please do not include any passwords in a public repo).We are expecting you to automate scenarios that you deem critical to validate the functionality of credentialed login to hudl.com ( http://hudl.com/ ).

This project is an opportunity to showcase your organization structure, approach to automation, and ability to effectively write new automated test cases.We will be looking for well-established best practices and patterns. Lastly, we will run your automation suite against the site, so please write it in a way that allows us to do so.
 
This isn't a timed test, however, we estimate this exercise to take you around 2-3 hours to complete. To allow us to continue to move through this process quickly, we ask that you return this project to us in 4 days. If you need more time for whatever reason, we ask that you please let us know, so we can properly set expectations with our project reviewers.
 
## Tips
 
If you're unfamiliar with Selenium the best place to start is with the below readings:
https://www.seleniumhq.org/projects/webdriver/
https://gist.github.com/huangzhichong/3284966
Once you have completed your project and pushed it to GitHub, please use the link at the bottom of this email to share the URL to the public repo.

## Overview

I haven't touched Selenium in a few years, so the first part of this was just re-familiarizing myself. Also, I know you all use a lot of Python in your testing, so I challenged myself to do it in Python. I definitely have some areas I would like to refactor, but I wanted to make sure I got this submitted in a working state on time rather than in a perfect state. 

Monday morning, 8/28/23, the main landing page went down while I was doing some testing and refactoring. Slight delay here, but not super impactful.

### Setup
* Make sure you have Python3 installed in your system.
* Install the necessary libraries and modules by typing `pip install -r requirements.txt` (My system is using `pip3`, so use the correct one for you)
* I provided a **testdata.json.sample** file instead of using environment variables, that way you can run this without having to add anything to your system settings. **testdata.json** is git ignored, so just create your own with your own credentials based on the sample template.

### Testing Approach:
* I focused on UI navigation and availability, along with some basic functionality concerns.
* Exercising any login-specific functionality outside of UI concerns is probably best handled via API tests instead of trying to hammer everything with Selenium.
  * Specifically I'd like to verify that the UI field and the API contract match in input requirements.
* Same goes with security testing - I had considered implementing some OWASP-style tests around sanitizing inputs and SQL injections, but that is best discussed with the security team before jumping in there.
* I got a real-time example of the failover to the mobile landing page with the incident above - it worked with a slight delay, which is great by the way, but I don't know if there is an easier way to test that. Might be worth a conversation.

### Open Issues:
* pages/base_page.py **wait_element_text** function isn't working properly. It was not my highest priority to debug this since I had a workaround, but I'd like to get that working - I think it's a more elegant way to handle waiting for the text to appear in error situations.
