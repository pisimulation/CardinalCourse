# export as JSON:
# $ scrapy crawl cs -o cs.json

import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.markup import remove_tags
from scrapy.selector import HtmlXPathSelector
import unicodedata


class CSSpider(scrapy.Spider):
    name = "cs"
    majors = ['ARAB','ARHA','ARST','CHIN','CCIV','CEAS','FILM','COL','DANC','ENGL','FREN','FSTR','GELT','GRST','GRK','HEBR','ITAL','ISTR','JAPN','KREA','LAT','LANG','MUSC','PORT','RUSS','RULE','SPAN','SSTR','THEA','AMST','ANTH','CSS','ECON','GOVT','HIST','PHIL','RELI','SOC','CADS','CEC','CES','CIM','CIR','CJS','CMES','CMB','CSCT','CSA','CSED','CWRC','ASTR','BIOL','CHEM','CIS','COMP','EES','MATH','MBB','NSB','PHYS','PSYC','XAFS','XAMS','XCHS','XDST','XHST','XPSC','XQST','XSER','XURS','AFAM','ARCP','CGST','CJST','CHUM','CSPL','ENVS','FGSS','LAST','MDST','QAC','REES','SISP','WRCT','PHED']
    def start_requests(self):
        for major in self.majors:
            yield scrapy.Request(url="https://iasext.wesleyan.edu/regprod/!wesmaps_page.html?subj_page=%s&term=1179" % major, callback=self.parse_sem)

    def parse_sem(self, response):
        nextPageFall = HtmlXPathSelector(response).select("//td/a[contains(text(),'Fall')]/@href").extract()
        nextPageFall = 'https://iasext.wesleyan.edu/regprod/' + unicodedata.normalize('NFKD', nextPageFall[0]).encode('ascii','ignore')
        nextPageSpring = HtmlXPathSelector(response).select("//td/a[contains(text(),'Spring')]/@href").extract()
        nextPageSpring = 'https://iasext.wesleyan.edu/regprod/' + unicodedata.normalize('NFKD', nextPageSpring[0]).encode('ascii','ignore')
        
        yield scrapy.Request(url=nextPageFall, callback=self.parse)
        yield scrapy.Request(url=nextPageSpring, callback=self.parse, )
        
    def parse(self, response):
        for major in self.majors:
            if major in response.url: 
                yield {
                    major : response.xpath("//td[contains(@width,'55%')]/text()").extract()
                }


# To run Scrapy from script
"""  
if __name__ == "__main__":
    process = CrawlerProcess({
        'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
    })

    process.crawl(MenuSpider)
    process.start()
"""
    