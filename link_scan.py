from typing import List
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.remote.webdriver import WebDriver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import urllib.error, urllib.request
import sys


def get_links(url):
    """Find all links on page at the given url.
    Returns:
        a list of all unique hyperlinks on the page,
        without page fragments or query parameters.
    """
    browser.get(url)
    link_list = browser.find_elements_by_tag_name("a")
    all_list = []
    for link in link_list:
        url = link.get_attribute('href')
        if url != None:
            if '#' in url:
                if url.split('#')[0] not in all_list:
                    all_list.append(url.split('#')[0])
            elif '?' in url:
                if url.split('?')[0] not in all_list:
                    all_list.append(url.split('?')[0])
            else:
                if url not in all_list:
                    all_list.append(url)
    return all_list


def is_valid_url(url: str) -> bool:
    """Check if the url is valid and reachable.
    Returns:
        True if the URL is OK, False otherwise.
    """
    try:
        urllib.request.urlopen(url)
    except urllib.error.HTTPError as error:
        if error.getcode() == 403:
            return True
        return False
    else:
        return True


def invalid_urls(urllist: List[str]) -> List[str]:
    """Validate the urls in urllist and return a new list containing
    the invalid or unreachable urls.
    Returns:
        A new list containing only the invalid or unreachable URLs from the parameter list.
    """
    new_list = []
    for url in urllist:
        if is_valid_url(url) == False:
            new_list.append(url)
    return new_list


if __name__ == "__main__":
    browser: WebDriver = webdriver.Chrome('C:/Program Files (x86)/chromedriver.exe')
    url = sys.argv[1]
    link_list = get_links(url)
    bad_link_list = invalid_urls(link_list)
    print('This is good link')
    for url in link_list:
        print(url)
    print('This is bad link')
    for url in bad_link_list:
        print(url)
    browser.quit()