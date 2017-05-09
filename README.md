# CardinalCourse

Wesleyan course review site for Wesleyan students to post ratings and reviews of courses they took

## Installation

The project is now deployed on heroku. Check it out here:

https://cardinalcourse.herokuapp.com

To run locally, download the repo, and in terminal, run

`npm run dev`

Then, go to `http://localhost:3000` in your browser.

## Features

Users can search courses by department abbreviation (e.g. russ, hist, comp), add their reviews, rate courses, upvote and downvote reviews. This project is originally started during the WesHack 2015.

## Tool Used

### Python, Scrapy web crawling framework

With Scrapy, course names are scraped from [WesMaps 2017-2018](https://iasext.wesleyan.edu/regprod/!wesmaps_page.html?term=1181) and exported as JSON by running

`scrapy crawl cs -o cs.json`

### NodeJS, ExpressJS, jQuery, local storage

Course reviews are stored in MongoDB database. List of dependencies can be found in package.json. Local storage is used to store what courses a user has already reviewed or rated and what reviews a user has already upvoted or downvoted.

### Bootstrap

Bootstrap forms, buttons, collapse divs, etc.