from scrapy.spiders import Spider
from scrapy.selector import Selector
from tutorial.items import Website


class DmozSpider(Spider):
    name = "amazon"
    allowed_domains = ["amazon.com"]
    start_urls = [
        "https://www.amazon.com/s/ref=lp_2649513011_nr_p_n_format_browse-bi_2?fst=as%3Aoff&rh=n%3A2625373011%2Cn%3A%212625374011%2Cn%3A2649513011%2Cp_n_format_browse-bin%3A2650304011&bbn=2649513011&ie=UTF8&qid=1464841011&rnid=2650303011",
        "https://www.amazon.com/s/ref=lp_2650363011_nr_p_n_format_browse-bi_1?fst=as%3Aoff&rh=n%3A2625373011%2Cp_n_theme_browse-bin%3A2650363011%2Cp_n_format_browse-bin%3A2650305011&bbn=2650363011&ie=UTF8&qid=1464841835&rnid=2650303011",
    ]

    def parse(self, response):
        """
        The lines below is a spider contract. For more info see:
        http://doc.scrapy.org/en/latest/topics/contracts.html
        @url http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/
        @scrapes name
        """
        sel = Selector(response)
        sites = sel.xpath('//ul[@id="s-results-list-atf"]//li')
        items = []

        for site in sites:
            item = Website()
            item['name'] = site.xpath('//h2/text()').extract()
            item['url'] = site.xpath('//div[@class="a-row a-spacing-small"]//a[@class="a-link-normal s-access-detail-page  a-text-normal"]/@href').extract()
            item['description'] = site.xpath('//title').extract()
            items.append(item)

        return items

    #div[@class="site-descr"/text()
    #For all the titles of the page.
    #//ul[@id="s-results-list-atf"]//li//div[@class="a-row a-spacing-small"]//a[@class="a-link-normal s-access-detail-page  a-text-normal"]