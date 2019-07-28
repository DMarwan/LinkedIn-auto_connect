##It may fail sometimes. Feel free to adapt to your own need.
## @author {DARWISH Marwan, https://github.com/DMarwan, https://www.linkedin.com/in/dmarwan/}

def auto_connector(mail, password, job):
    
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    import time
    from random import uniform
    
    browser = webdriver.Chrome('/usr/bin/chromedriver')
    browser.get('https://www.linkedin.com/login?trk=guest_homepage-basic_nav-header-signin')
    login = browser.find_element_by_xpath('//*[@id="username"]').send_keys(mail)
    pwd = browser.find_element_by_xpath('//*[@id="password"]').send_keys(password)
    validation_1 = browser.find_element_by_xpath('//*[@id="app__container"]/main/div/form/div[3]/button').send_keys(Keys.ENTER)
    time.sleep(1.5)
    search = browser.find_element_by_class_name("search-global-typeahead__input")
    search.send_keys(job)
    search.send_keys(Keys.ENTER)
    time.sleep(2)
    people = browser.find_element_by_xpath('//button[@aria-label="View only People results"]').click()
    time.sleep(2)
    connections = browser.find_element_by_xpath('//button[@aria-label="Connections filter. Clicking this button displays all Connections filter options."]').click()
    second = browser.find_element_by_xpath('//label[@for="network-S"]').click()
    time.sleep(1)
    third = browser.find_element_by_xpath('//label[@for="network-O"]').click()
    time.sleep(1)
    apply = browser.find_element_by_xpath('//button[@data-control-name="filter_pill_apply"]').click()
    
    time.sleep(2)
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
   
    next_page = browser.find_element_by_xpath('//button[@class="artdeco-pagination__button artdeco-pagination__button--next artdeco-button artdeco-button--muted artdeco-button--icon-right artdeco-button--1 artdeco-button--tertiary ember-view"]')
    time.sleep(1)
    i = 0
    
    #let's go 
    
    while True:  
        try:
            browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")   
            time.sleep(1.5)
    
            to_connect = browser.find_elements_by_xpath("//button[starts-with(@aria-label, 'Connect with')]")
            time.sleep(1)
            for connect in to_connect:
                time.sleep(uniform(1.5,2.5))
                browser.execute_script("arguments[0].scrollIntoView();", connect)
                time.sleep(1.5)
                browser.execute_script("arguments[0].click();", connect)
                i += 1
                time.sleep(uniform(0.8,1.8))
                browser.find_element_by_xpath('//button[@class="artdeco-button artdeco-button--3 ml1"]').click()
            
            time.sleep(1)    
            
            browser.execute_script("arguments[0].scrollIntoView();", next_page)
            next_page.click()
            time.sleep(1)
            browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            next_page = browser.find_element_by_xpath('//button[@class="artdeco-pagination__button artdeco-pagination__button--next artdeco-button artdeco-button--muted artdeco-button--icon-right artdeco-button--1 artdeco-button--tertiary ember-view"]')
        except:
            print(f'Job finished. {i} invitations sent.')
            
