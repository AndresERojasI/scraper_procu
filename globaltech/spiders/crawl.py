# -*- coding: utf-8 -*-
import scrapy

class CrawlSpider(scrapy.Spider):
    name = 'procuraduria'
    allowed_domains = ['https://www.procuraduria.gov.co/CertWEB/Certificado.aspx?tpo=1']
    start_urls = ['https://www.procuraduria.gov.co/CertWEB/Certificado.aspx?tpo=1']

    def parse(self, response):
        form = '//*[@id="form1"]'
        token_csrf = response.xpath('//*[@id="__VIEWSTATE"]/@value').extract()

        return scrapy.FormRequest.from_response(
            response,
            formxpath=form,
            formdata={'__VIEWSTATE': token_csrf[0], 'ddlTipoID': '1', 'txtNumID': '1090038928093'},
            callback=self.after_query
        )

    def after_query(self, response):
        print('response::::', response)
