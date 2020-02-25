### Parallel web scraping
The project is a training task for web scraping using python multithreading and a real-time-updated list of available proxy servers.

#### Goal
The script extracts names and prices of the Top-100 crypto coins and stores the data into a db. 

#### Disclaimer
The task is quite contrived and serves mainly for study purpose. There are innumerous of mature sources containing both real-time and historical cryptocurrency data.

### Solved problems within the project
1. Multiple pages with one level nesting have been scraped. The propagation has been implemented by gathering internal links from the main page followed by looping on them.
2. To avoid getting banned from the remote server, a mechanism dealing with proxy servers was implemented.
3. A free public proxy server is commonly assumed as unreliable in terms of availability. To overcome this issue:
    - another scraping script extracts a list of free public proxy servers from a web site.
    - with each launch of the script, the list of 10 proxy servers gets updated by currently available proxy servers.
    - during the script execution, some proxy servers get unavailable. Thus, each scraping query goes through this list and searches for an alive proxy server to execute a query.
4. To speed up the scraping of the total 101 web pages multithreading is involved. The work is divided among 4 threads running almost simultaneously.
5. The extracted data is being written directly to a DataBase.
