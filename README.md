# CardinalCourse

Wesleyan course review site for Wesleyan students to post ratings and reviews of courses they took

## Installation

The project is now deployed on heroku. Check it out here:

https://sheltered-bayou-66104.herokuapp.com/

To run locally, download the repo, and in terminal, run

`npm run dev`

Then, go to `http://localhost:3000/` in your browser.

## Features

Users can search courses by department abbreviation (e.g. russ, hist, comp), add their reviews, and rate courses. This project is originally started during the WesHack 2015.

## Tool Used

### Python, Scrapy web crawling framework

With Scrapy, course names are scraped from [WesMaps 2017-2018](https://iasext.wesleyan.edu/regprod/!wesmaps_page.html?term=1181) and exported as JSON by running

`scrapy crawl cs -o cs.json`

### NodeJS, ExpressJS, jQuery

Course reviews are stored in MongoDB database. List of dependencies can be found in package.json

### Bootstrap

Bootstrap forms, buttons, collapse divs, etc.