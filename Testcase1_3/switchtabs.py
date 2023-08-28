# Necessary webdrivers need to be imported
from selenium import webdriver

# This is for Firefox. Similarly, if
# chrome is needed , then it has to be specified
webBrowser = webdriver.Firefox()

# first tab. Open google.com in the first tab
webBrowser.get('http://google.com')

# second tab
# execute_script->Executes JavaScript snippet.
# Here the snippet is window.open that means, it
# opens in a new browser tab
webBrowser.execute_script("window.open('about:blank','secondtab');")

# It is switching to second tab now
webBrowser.switch_to.window("secondtab")

# In the second tab, it opens geeksforgeeks
webBrowser.get('https://opensource-demo.orangehrmlive.com/')
