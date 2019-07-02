# getTopStories.py

import os,json
from bs4 import BeautifulSoup
from collections import defaultdict

ourFiles = ['brett kavanaugh.html', 'christine blasey ford.html', 'delay the vote.html', 'kavanaugh confirmation.html', 'kavanaugh fbi investigation.html', 'kavanaugh hearing.html', 'kavanaugh vote.html', 'kavanaugh.html', 'mark judge.html', 'supreme court.html', 'survivors rally.html']

def has_top_stories(soup):
    titles = []
    # Find sections with header
    for el in soup.find_all("g-section-with-header"):
        title = el.find('h3')
        if title:
            titles.append(title.get_text())
    if 'Top stories' in titles:
        return True
    return False

def find_top_story_index(soup):
    """It's going to count the ads too."""
    sections = soup.find_all(class_ = "bkWMgd")
    posCount = 1
    for i, sec in enumerate(sections):
        g = sec.find_all(class_ = "g")
        posCount += len(g)
        allText = sec.text
        if allText.find('Top stories') != -1:
            return posCount

def get_top_stories(soup):
    """Given a parsed DOM, extract the content of top stories.
    This does the extraction for both cards with images and the
    ones without. The only difference seem to be the class name
    for the time element, "8 hours ago".
    """
    gSect = soup.findAll("g-section-with-header")
    for sec in gSect:
        h3 = sec.find('h3')
        if 'Top stories' in h3:
            cards = sec.findAll('g-inner-card')
            stories = []
            if cards:
                for card in cards:             
                    url = card.find('a')['href']
                    title = card.find('a').text
                    #print(title)
                    try:
                        source = card.find('cite').text
                    except:
                        source = card.find('span').text
                    try:
                        time = card.find(class_='f').text
                    except:
                        time = card.find(class_='uaCsqe').text
                    stories.append({'title': title, 'url': url, 
                                    'source': source, 'time': time})
                return stories

def get_top_stories_type2(soup):
    """
    """
    stories = []
    divs = soup.findAll(class_='dbsr')
    if divs:
        for div in divs:
            url = div.find('a')['href']
            try: 
                title = div.find(class_='y9oXvf').text
            except:
                title = div.find(class_='rrBdId').text
            try:
                source = div.find('cite').text
            except:
                source = div.find('span').text
            try:
                time = div.find(class_='f').text
            except:
                time = div.find(class_='FGlSad').text
            stories.append({'title': title, 'url': url,
                            'source': source, 'time': time})
        return stories


def get_top_stories_type3(soup):
    """
    """
    stories = []
    divs = soup.findAll(class_='dbsr')
    if divs:
        for div in divs:
            url = div.find('a')['href']
            try: 
                title = div.find(class_='fn6bCb').text
            except:
                title = div.find('a').text
            try:
                source = div.find('cite').text
            except:
                source = div.find('span').text
            try:
                time = div.find(class_='f').text
            except:
                time = div.find(class_='uaCsqe').text
            stories.append({'title': title, 'url': url,
                            'source': source, 'time': time})
        return stories


if __name__ == '__main__':
  path = '/Users/yueyang/Downloads/2020-candidates/'
  folders = [f for f in os.listdir(path) if os.path.isdir(os.path.join(path, f))]
  print(len(folders)) #result = 147

#female candidates
  female_candidates = ['Elizabeth Warren', 'Kamala Harris', 'Amy Klobuchar', 'Kirsten Gillebrand', 'Marianne Willimson','Tulsi Gabbard']
#--getting top stories
  storiesPerFile = defaultdict(dict)
  for fld in folders:
    fldPath = os.path.join(path, fld)
    files = os.listdir(fldPath)
    female_candidates = ['Elizabeth Warren', 'Kamala Harris', 'Amy Klobuchar', 'Kirsten Gillebrand', 'Marianne Willimson','Tulsi Gabbard']
    female_candidates_files = ['{}.html'.format(c) for c in female_candidates]
    toread = [f for f in files if f in female_candidates_files]
    for fl in toread:
        #getting the soup
        with open(os.path.join(fldPath, fl)) as fp:
            html_doc = fp.read()
            soup = BeautifulSoup(html_doc, 'html5lib')
            hasTop = has_top_stories(soup)
            #if has top stories
            if hasTop:
                index = find_top_story_index(soup)
                try:
                    stories = get_top_stories(soup)
                    if stories:
                        storiesPerFile[fld][fl] = stories
                    else:
                        print('ELSE', index, fld+'/'+fl)
                except:
                    print(index, fld+"/"+fl)
  print(len(storiesPerFile))
  cnt = 0
  for dt in storiesPerFile:
    files = storiesPerFile[dt]
    for f in files:
        cnt += len(storiesPerFile[dt][f])
  print(cnt)
  json.dump(storiesPerFile, open('processed-top-stories.json', 'w'))
  

#Elizabeth Warren, Kamala Harris, Amy Klobuchar, Kirsten Gillebrand, Marianne Willimson, and Tulsi Gabbard