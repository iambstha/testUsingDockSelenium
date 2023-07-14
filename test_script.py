import dock.dock as d

# Url is dynamically input in the terminal
getUrl = input("Enter the URL: ")
d.driver.get(getUrl)

# Run Function
def run():
    # Your script goes here
    try:
        search_u_field = d.driver.find_element(by=d.By.XPATH, value="//input[@id='username']")
        search_p_field = d.driver.find_element(by=d.By.XPATH, value="//input[@id='password']")
        submit_field = d.driver.find_element(by=d.By.XPATH, value="//button[@name='login']")
        if search_u_field:
            print("Username field found.")
        if search_p_field:
            search_p_field_type = d.driver.find_element(by=d.By.XPATH, value="//input[@id='password'][@type='password']")
            if search_p_field_type:
                print("Password field found & is hidden.")
            else:
                print("Alert: Password is not hidden.")
        if submit_field:
            print("Submit button found.")
    except:
        print("Error: Username, password or submit field not found.")

    def askInfo():
        username = input("Username: ")
        password = input("Password: ")
        findComponents(username,password)

    def findComponents(username,password): 

        try:
            # u_text_box = d.driver.find_element(by=d.By.XPATH, value=u_xpath)
            u_text_box = search_u_field
            if u_text_box:
                # print('Username field found.')
                u_text_box.send_keys(username)
        except d.NoSuchElementException:
            print('Username field not found.')

        try:
            # p_text_box = d.driver.find_element(by=d.By.XPATH, value=p_xpath)
            p_text_box = search_p_field
            if p_text_box:
                # print('Password field found.')
                p_text_box.send_keys(password)
        except d.NoSuchElementException:
            print('Password field not found.')

        try:
            # submit_button = d.driver.find_element(by=d.By.XPATH, value=submit_xpath)
            submit_button = submit_field
            if submit_button:
                submit_button.click()
                print('Submit clicked.')
        except d.NoSuchElementException:
            print('Submit button not found.')

        try:
            check_login_status = d.driver.find_element(by=d.By.XPATH, value="/html/body/div/div[1]/div[2]/form/button")
            if check_login_status.text == 'Log out':
                d.driver.save_screenshot("screenshot.png")
                print("Successfully logged in.") 
                check_login_status.click()
        except d.NoSuchElementException:
            print('Error: Username or password doesnot match!!!')
        # finally:
        #     d.driver.quit()

    askInfo()




i = d.Driver(d.driver)
i.rerun(3, lambda: run())