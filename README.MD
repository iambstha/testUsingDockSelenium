# DOCK SELENIUM

## Python only

This is a startup directory to write the selenium scripts in python along with some customization.

### Steps.
1. Clone [this](https://github.com/iambstha/dockSelenium) repository.
2. Edit `test_script.py`. To make changes, write selenium scripts inside the run function defination.
3. Always bind any selenium script with `d` while writing test scripts. For example `driver.find_element()` should be written as `d.driver.find_element()`
4. Customize the webdriver wait-time as per your project requirements.
5. Customize the amount of retest by modifying the integer value in the `rerun` call.