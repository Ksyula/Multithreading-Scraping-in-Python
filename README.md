### Parallel web scraping
The project is a training task for web scraping using python multithreading and a real-time-updated list of available proxy servers.

#### Goal
The script extracts names and prices of the Top-100 crypto coins and stores the data into a db. 

#### Disclaimer
The task is quite contrived and serves mainly for study purpose. There are innumerous of mature sources containing both real-time and historical cryptocurrency data.

### Solved problems within the project
* Multiple pages with single-level nesting have been scraped. Propagation is handled by collecting internal links from the main page and iterating through them.
* To prevent bans from the remote server, a proxy management mechanism was implemented.
* Since free public proxy servers are often unreliable, the following approach was used to address this issue:
  - A separate scraping script extracts a list of free public proxy servers from a website.
  - With each script execution, the list of 10 proxy servers is updated with currently available ones.
  - During execution, some proxies may become unavailable. Each scraping request cycles through the list to find an active proxy before proceeding.
* To accelerate the scraping of all 101 web pages, multithreading was utilized. The workload is distributed across four threads running concurrently.
* The extracted data is written directly to a database.
