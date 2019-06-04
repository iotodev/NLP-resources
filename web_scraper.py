from bs4 import BeautifulSoup
import re
import requests


def download_html_page(parliament_session, page_number):
    # TODO: make arguments optional (eg. download_html_page(parliament_session=41, page_number=70))

    # ParlSes=All for all publications
    url = 'https://www.ourcommons.ca/Parliamentarians/en/publicationsearch?View=D&Item=' \
          '&ParlSes=' + str(parliament_session) + \
          '&oob=' \
          '&Topic=' \
          '&Proc=' \
          '&Per=' \
          '&Prov=' \
          '&Cauc=' \
          '&Text=' \
          '&RPP=15' \
          '&order=' \
          '&targetLang=' \
          '&SBS=0' \
          '&MRR=150000' \
          '&Page=' + str(page_number) + \
          '&PubType=37'

    res = requests.get(url)
    html_page = res.content
    return html_page


def beautiful_soup(html_page):
    soup = BeautifulSoup(html_page, 'html.parser')

    # get all text from html page:
    # text = soup.find_all(text=True)

    paragraphs = soup.findAll("div", {"class": ["para", "PersonSpeakingName"]})  # get person speaking, speech
    tags = soup.findAll("a", {"class": "index"})  # get speech tags # TODO: group with paragraphs output
    # TODO: also get date of speech; to set date range for finding topic ("talked about x this week")

    # findall <a> elements where href "contains 'members'"; gives mp names (+ some junk):
    # mps = soup.findAll("a", {"href": re.compile("members")})

    # view all elements in html page (for creating blacklist):
    # print(set([t.parent.name for t in text]))

    output = ''
    tag_output = ''

    blacklist = [  # entire list of html page elements; comment out what to keep
        'i',
        'span',
        'title',
        'script',
        'b',
        'option',
        'button',
        'ul',
        'meta',
        'style',
        'nav',
        # 'a',
        'header',
        'label',
        '[document]',
        # 'div',
        'form',
        'html',
        'head',
        'body',
        'select',
        'h5',
        'footer',
        'input',
        'li'
    ]

    for t in paragraphs:  # see above for paragraphs definition
        if t.parent.name not in blacklist:
            output += '{}\n'.format(t)

    for t in tags:  # see above for tags definition
        if t.parent.name not in blacklist:
            tag_output += '{} '.format(t)

    # output all text:
    # for t in text:
    #     if t.parent.name not in blacklist:
    #         output += '{} '.format(t)

    output = re.sub("^\s+|\s+$", "", output, flags=re.UNICODE)  # remove all whitespace

    # print WITH html tags (for easier reinsertion into an html page); also see below (output text to txt file):
    # print(output)

    # remove all whitespace (not even in sentences); will probably never need this
    # output = ''.join(output.split())

    print(BeautifulSoup(output, features='html.parser').get_text())  # without html tags
    print(tag_output)

    # output to txt file, formatted for easy insert into HTML page (I think)
    # with open('new.txt', 'w') as f:
    #     f.write(soup.prettify())


def main():
    mp_publications_html_page = download_html_page(41, 70)
    beautiful_soup(mp_publications_html_page)


if __name__ == '__main__':
    main()
