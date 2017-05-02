# CardinalCourse

Wesleyan course review site for Wesleyan students to post ratings and reviews of courses they took

## Installation

In terminal, run

`npm run dev`

Then, go to `http://localhost:3000/` in your browser.

## Status
I am reviving a hackathon project from the WesHack 2015. This project is still incomplete. I am currently working on the back end. A user can now search for courses using department names, e.g. COMP, math. List of courses will appear. Each course has reviews and the user can add their own review which will be added to database.

## Tool Used

### Python, Scrapy web crawling framework

With Scrapy, course names are scraped from [WesMaps 2017-2018](https://iasext.wesleyan.edu/regprod/!wesmaps_page.html?term=1181) and exported as JSON by running

`scrapy crawl cs -o cs.json`

### NodeJS, ExpressJS, jQuery

Course reviews are stored in MongoDB database. List of dependencies can be found in package.json

### Bootstrap

Bootstrap forms, buttons, collapse divs, etc.