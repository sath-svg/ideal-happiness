import datetime
import time
import pandas as pd
from selenium import webdriver


driver_path = r"C:\Temp\Chrome_Driver\chromedriver.exe"
driver = webdriver.Chrome(executable_path=driver_path)
# driver.get(r'https://members.myactivesg.com/bookfacility')
driver.get('https://members.myactivesg.com/auth')
driver.maximize_window()
time.sleep(1.8)

def main():
    # while True:
        email = driver.find_element_by_xpath('//*[contains(@id,"email")]')
        email.click()
        email.send_keys('S9870118D')
        time.sleep(0.1)
        password = driver.find_element_by_xpath('//*[contains(@id,"password")]')
        password.click()
        password.send_keys('Red7777777#')
        lgn = driver.find_element_by_xpath('//*[contains(@id,"btn-submit-login")]')
        lgn.click()
        time.sleep(0.5)
        now = datetime.datetime.now()
        print(f"Running booking script at {now}")
        book_date = datetime.date.today() + datetime.timedelta(days=15)
        print('Target Booking date: %s' % str(book_date))

        future_date = int(time.mktime(book_date.timetuple()))
        driver.get('https://members.myactivesg.com/facilities/view/activity/%d/venue/%d?time_from=%d' % (
            18, 1181, future_date))

        time.sleep(1)
        # try:
        #     for i in range(5):
        #         try:
        #             activity = driver.find_element_by_xpath('//*[contains(@id,"activity_filter_chosen")]')
        #             activity.click()
        #             activity = driver.find_element_by_xpath('//*[contains(@id,"activity_filter_chosen")]/div/div/input')
        #             activity.send_keys('Badminton')
        #             time.sleep(1)
        #             venue = driver.find_element_by_xpath('//*[contains(@id,"venue_filter_chosen")]')
        #             venue.click()
        #             venue = driver.find_element_by_xpath('//*[contains(@id,"venue_filter_chosen")]/div/div/input')
        #             venue.send_keys('Bukit Canberra Sport Hall')
        #             datey = driver.find_element_by_xpath('//*[contains(@id,"date_filter")]')
        #             future_date = now + datetime.timedelta(days=15)
        #             formatted_date = future_date.strftime('%a, %d %b %Y')
        #             datey.send_keys(formatted_date)
        #             search = driver.find_element_by_xpath('//*[contains(@id,"search")]')
        #             search.click()
        #             break
        #             #activity_drop = driver.find_element_by_xpath('//*[@id="activity_filter_chosen"]/div/div/input')
        #
        #         except Exception as ex_opportunities:
        #             print('cant load badminton courts')
        try:

            count = 0
            # Find all checkboxes inside the specified div
            checkbox_divs = driver.find_elements_by_xpath(
                '//div[@class="col-xs-4 col-sm-2 chkbox-grid"]')
            # Iterate over the checkboxes and select the first two for 7:00 AM and 8:00 AM
            for checkbox_div in checkbox_divs:
                checkbox = checkbox_div.find_element_by_xpath('.//input[@type="checkbox"]')
                label_text = checkbox.find_element_by_xpath('following-sibling::label').text
                print(label_text)
                if label_text in ["07:00 AM", "08:00 AM"]:
                    count+=1
                    print(count)
                    checkbox_div.click()
                    print(f"Checkbox for {label_text} selected.")
                    # Break after selecting the first two checkboxes
                    if count == 2:
                        break
                else:
                    continue


        except Exception as ex_opportunities:
            print(ex_opportunities)
            print('cant get slots')

        time.sleep(0.1)
        try:
            cart = driver.find_element_by_xpath('//*[contains(@id,"addtocartbtn")]')
            cart.click()



        # Your script logic goes here
        except Exception as ex_opportunities:
            print(f'Exception occurred - {ex_opportunities}')
            print('add to cart not found')
            # Sleep for a short duration before retrying
            time.sleep(1)

        # Sleep for a short duration (e.g., 5 minutes) before the next iteration


def run_script():
    now = datetime.datetime.now().time()
    start_time = datetime.time(7, 0)
    end_time = datetime.time(7, 5)

    if start_time <= now <= end_time:
        print("Running script at", now)
        main()
    else:
        print("Not within the specified time range. Current time is", now)

if __name__ == "__main__":
    #run_script()
    main()
