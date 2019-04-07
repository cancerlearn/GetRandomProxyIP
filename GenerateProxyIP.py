from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import random as rnd


def getAllProxyIPs():
    """
    This method returns a list of proxy IPs gathered from a table on the page "https://free-proxy-list.net/".
    Note: A chrome browser used by selenium will open during runtime. 
    """

    #List of proxy IPs to be returned
    proxyIP_List = []

    #webpage where generated proxy IPs are taken from
    url = "https://free-proxy-list.net/"

    CHROMEDRIVER_PATH = "selenium/chromedriver.exe"

    #making browser headless (no ui pops up)
    chromeOptions = Options()
    chromeOptions.headless = True
    
    #selenium driver for browser used
    driver = webdriver.Chrome(CHROMEDRIVER_PATH, options= chromeOptions)

    driver.get(url)

    #CSS selector for 'next' button to move to next table list of proxy IPs
    nextBtn_cssSelector = "section#list>div.container>div.table-responsive>div#proxylisttable_wrapper>div.row>div.col-sm-7>div.dataTables_paginate>ul.pagination>li.next>a"
    
    #CSS selector for disabled 'next' button
    #This button is disabled only when the list of proxy IPs in the table are exhausted
    disablednextBtn_cssSelector = "section#list>div.container>div.table-responsive>div#proxylisttable_wrapper>div.row>div.col-sm-7>div.dataTables_paginate>ul.pagination>li.next.disabled>a"

    nextProxyIP_btn = driver.find_element_by_css_selector(nextBtn_cssSelector)
    
    #while button is still 'clickable'
    while not nextProxyIP_btn.click():
        
        #Since the element 'driver.find_element_by_css_selector(testcssSelector).text' does not exist until the 'next' button is disabled
        #Placing this code in a try/except block will allow for the program to end when the element exist, thus when the list of proxy IPs are exhausted
        try:
            driver.find_element_by_css_selector(disablednextBtn_cssSelector).text
            #If element exists,
            break
        except:
            #else,
            pass

        #Find button in new div
        nextProxyIP_btn = driver.find_element_by_css_selector(nextBtn_cssSelector)

        #Retrieve data in table of proxy IPs
        table_UserAgents = driver.find_elements_by_css_selector("table.dataTable>tbody>tr")

        #Go thtough rows of data to store proxy IPs appropriately
        for row in table_UserAgents:
            
            #Add 'https://' to proxyIP if proxyIP is https
            if row.text.split(" ")[4] == "yes": proxyIP_List.append("https://" + row.text.split(" ")[0] + ":" + row.text.split(" ")[1])
            #Otherwise, add 'http://'
            else: proxyIP_List.append("http://" + row.text.split(" ")[0] + ":" + row.text.split(" ")[1])

    driver.close()

    return proxyIP_List


def getRandomProxyIP():
    """
    This method returns a random proxy IP from the list returned by getAllProxyIPs()
    """

    proxyIPList = getAllProxyIPs()
    
    randomSelection = rnd.randint(0, len(proxyIPList)-1)

    randomProxyIP = proxyIPList[randomSelection]

    return randomProxyIP


def getRandomProxyIPDict():
    """
    Using the protocol passed as an argument, this method returns a proxy IP with the respective protocol
    """

    proxyDict = {}

    proxyIPList = getAllProxyIPs()

    for proxyIP in proxyIPList:

        protocol = proxyIP.split("://")[0]

        #Adding proxyIP to proxyIP list if it does not exist
        try:
            proxyDict[protocol]
        except KeyError:
            proxyDict[protocol] = proxyIP

    return proxyDict