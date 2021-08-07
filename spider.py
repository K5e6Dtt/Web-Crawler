import requests,re,argparse
from urllib.parse import urljoin

class Spider:
    def __init__(self,target_url):
        self.target_url = target_url
        self.stored_urls = []
        self.crawl(target_url)

    def extract_links(self,url):
        response = requests.get(url)
        href_links = re.findall('(?:href=")(.*?)"',response.content.decode(errors="ignore"))
        #If you want to ignore byte decoding errors like 0x10 something just say errors="ignore"
        return href_links

    def crawl(self,url):
        href_links = self.extract_links(url)
        for link in href_links:
            link = urljoin(url,link)

            if '#' in link:
                link = link.split('#')[0]

            if self.target_url in link and link not in self.stored_urls:
                self.stored_urls.append(link)
                print(link)
                self.crawl(link)



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="This is a simple spider, type -h fpr help")
    parser.add_argument("--url",help="The url of the target website")
    option = parser.parse_args()
    Spider(option.url)
    


