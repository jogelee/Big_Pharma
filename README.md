# Big_Pharma

After seeing Kodak insider transactions surge right before it was announced they would be receiving a large federal loan to produce pharmaceutical ingredients, I thought maybe I could identify which pharmaceutical company had successfully developed a COVID-19 vaccine before they officially announced it (probably a pipe dream).

The idea is to look at the insider transactions of the executives of a few big name companies that are known to be working on a vaccine. Insider transactions are officially reported to the SEC and are available for anyone to view in their EDGAR database.

I manually searched for the executive teams of a few companies (Pfizer, Moderna, Inovio, Johnson & Johnson, Novavax), and added their names and SEC insider transactions URL to BIG_PHARMA.csv. The insiders.py script can then be run each day to web scrape each URL and find the most recent transactions for each company's executives.

Any records can be added to BIG_PHARMA.csv, so any company (pharm or no pharm) and its executives can be tracked.
