from bs4 import BeautifulSoup as bs
from selenium import webdriver
import requests as rs
import random as rnd


def getAllProxyIPs():
    """
    This method returns a list of proxy IPs
    """

    #List of proxy IPs to be returned
    proxyIP_List = []

    #webpage where generated proxy IPs are taken from
    url = "https://free-proxy-list.net/"
    
    #selenium driver for browser used
    driver = webdriver.Chrome()

    driver.get(url)

    #Retrieve data in table of proxy IPs
    table_UserAgents = driver.find_elements_by_css_selector("table.dataTable>tbody>tr")

    for row in table_UserAgents:

        proxyIP_List.append(row.text.split(" ")[0])

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
