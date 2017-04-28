from bs4 import BeautifulSoup as bs
from engine import SynEngine

soup = bs(open("./test/lexsub_test.xml"), "xml")

with open('best.out', 'w') as best:
    with open('bo10.out', 'w') as bo10:
        for l in soup.find_all('lexelt'):
            word = l['item']
            for i in l.find_all('instance'):
                iid = i['id']
                c = list(i.context.strings)
                phrase = c[0]
                w = c[1]
                if len(c) > 2 :
                    phrase += c[2]
                en = SynEngine(phrase, w)
                synonym = [i[0] for i in en.getSyn()]
                ans = word + " " + str(iid) + " :: "
                if len(synonym) > 0:
                    best.write(ans + synonym[0] + "\n")
                    for i in synonym[:10]:
                        ans += i + " "
                    bo10.write(ans + "\n")
                else:
                    best.write(ans + "\n")
                    bo10.write(ans + "\n")