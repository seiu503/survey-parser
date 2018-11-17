from bs4 import BeautifulSoup
with open("html/AtEase.html") as fp:
    soup = BeautifulSoup(fp, 'html.parser')

p_classes = ["s11", "s36", "s17", "s37", "s54", "s16", "s57", "s55", "s103", "s123", "s16"]
ol_ids = ["l14", "l16", "l17", "l18", "l21"]

def check_if_in_list(element, collection: iter):
    return element in collection

def els_to_return(tag):
    try:
        if tag['class']:
            classname = tag['class'][0]
            return check_if_in_list(classname, p_classes) or check_if_in_list(tag.id, ol_ids)
    except KeyError:
        pass

els = soup.find_all(els_to_return)
print(els)

for el in els:
    # if p.string:
        print(el.get_text())
