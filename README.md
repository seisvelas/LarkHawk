Checks for available students in Lark and emails you if there are any.

## Usage

The script depends on three environmental variables, your Lark username (USER), password (PASS), and an 
email address to send updates to (EMAIL).

Then, install a cron job that runs larkhawk every so often! Viola!

## How?

Lark is surprisingly unfriendly to scrape. If you try to just do an HTTP request to log in and check Lark for available students, you'll be disappointed to find that none of the info is there in the raw HTTP response body. Instead, it's a big Javascript object. A huge, obfuscated Javascript file (client.js) then populates the page dynamically. So the only way to scrape this is if you can render JS to a DOM, in other words you need a web browser. Since we're running this from a script on a server, that pretty much limits us to Selenium.

**checkStudents.py** - Runs selenium via Python to login to Lark and print out the number of available students.

**sendAlert.rkt** - Opens sendmail via Racket and sends an alert that an available student has been found.

I wanted to do the whole thing in Lisp but Racket doesn't support Selenium, and, well, Python does. 
