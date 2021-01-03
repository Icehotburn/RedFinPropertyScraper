# This is a Python script to scrape a Rental Property listings for useful data.
#
# In it's current state this project scrapes a Redfin property listing search
# to find the listings with the best price to rental income ratio.
#
# The results are then stored in a csv file, and emailed to the desired recipient(s).

import yaml

from RentalPropertyScraper.Redfin.scrapeSite import scrape_redfin_search

from RentalPropertyScraper.Utils.sendEmail import send_email_with_attachment

if __name__ == '__main__':

    print("Running main.py")

    with open("config.yaml", "r") as ymlfile:
        cfg = yaml.full_load(ymlfile)
        redfin_cfg = cfg["redfin"]
        email_cfg = cfg["email"]

    RedfinResultsFilePath = scrape_redfin_search(redfin_cfg)

    print("Created Redfin results file: " + RedfinResultsFilePath)

    send_email_with_attachment(RedfinResultsFilePath, email_cfg)

    print("Emailed Redfin results file to: " + email_cfg["toEmail"]["address"])
