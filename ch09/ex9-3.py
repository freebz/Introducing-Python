# 9.3 웹 서비스와 자동화

# 9.3.1 webbrowser 모듈

import antigravity


import webbrowser
url = 'http://www.python.org/'
webbrowser.open(url)
# True


webbrowser.open_new(url)
# True


webbrowser.open_new_tab('http://www.python.org/')
# True


# 9.3.2 웹 API와 REST

# 9.3.3 JSON

# 9.3.4 크롤링과 스크래핑

# 9.3.5 HTML 스크랩하기: BeautifulSoup

def get_links(url):
    import requests
    from bs4 import BeautifulSoup as soup

    result = requests.get(url)
    page = result.text
    doc = soup(page)
    links = [element.get('href') for element in doc.find_all('a')]
    return links

if __name__ == '__main__':
    import sys
    for url in sys.argv[1:]:
        print('Links in', url)
        for num, link in enumerate(get_links(url), start=1):
            print(num, link)
        print()
