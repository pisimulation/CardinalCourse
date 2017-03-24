# CardinalCourse

Wesleyan course review site for Wesleyan students to post ratings and reviews of courses they took

## Status
I am reviving a hackathon project from the WesHack 2015. This project is still incomplete. I am currently working on the front end.

## Tool Used

### Python, Scrapy web crawling framework

With Scrapy, course names are scraped from [WesMaps 2017-2018](https://iasext.wesleyan.edu/regprod/!wesmaps_page.html?term=1181) and exported as JSON by running
`scrapy crawl cs -o cs.json`

### HTML, JavaScript

With the HTML DOM, JavaScript accesses the index.html document and fills in course names of all departments, programs, certificates.
