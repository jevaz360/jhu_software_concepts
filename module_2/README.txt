Name: Janice Vaz JHED ID

Module 2: Webscraping The Grad Cafe Website

Approach: In this assignment, we were tasked with webscraping entries from The Grad Cafe, containing student statistics for their graduate school applications.
URLlib was used to get the website while BeautifulSoup was used to create a Soup object out of the web page. On The Grad Cafe website, each student entry was associated
with a <tr> html tag, which is what was used to parse the website and extract respective data. The data was stored according to each page's gathered entries.
Essentially, a list object stored all the entries, then the list was paired with a "key" according to the page number the entries were derived from, and put into
an outer dictionary. Finally, the outer dictionary of each page collectively was put into a list to export to a JSON file.

Known Bugs: