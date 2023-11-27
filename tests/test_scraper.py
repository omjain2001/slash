from bs4 import BeautifulSoup
from src import scraper
import pytest
import requests


def test_searchWalmart(mocker):
    page = {
        "content": '''<div class="pv3 overflow-x-auto w-90-m w-80">
<div class="flex flex-row" data-testid="products">
<div class="flex-grow-1 ph4 w-20-l w-50-m w-35">
<div class="sans-serif mid-gray relative flex flex-column w-100" data-item-id="518977383" role="group">
<div class="flex items-center flex-column">
<div class="absolute top-0 left-0 w-100 z-1 h-100">
<a class="absolute w-100 h-100 z-1 hide-sibling-opacity" href="https://wrd.walmart.com/track?bt=1&;eventST=click&;plmt=sb-search-top~desktop~&;pos=2&;tax=3944_1089430_3951_8835131_1737838&;rdf=1&;rd=https%3A%2F%2Fwww.walmart.com%2Fip%2FHP-Chromebook-X360-14-HD-Touchscreen-2-in-1-Laptop-Intel-Celeron-N4020-4GB-RAM-64GB-eMMC-Teal-14a-ca0130wm%2F518977383%3FadsRedirect%3Dtrue&;adUid=33e5a076-162f-428a-bcd1-29ee564fe36a&;mloc=sb-search-top&;pltfm=desktop&;pgId=laptops&;pt=search&;spQs=T4ky7SJGaU6bRFLThT-z6o2Zbo3F9KrziHssJciU08KGDJLKmC0_hyChPulrXPlVoKrtTzYv6oVQBeJ82Pst0_0s-lJh1AgfzOAYZXIecsc0JogOK-WnpPcgQiSllenn-1nlzo2IMQMlZL7TGICG02I70Grcgpt7MGKhNt9AhGYCnoPTcfEyGrl_61-QoMrfMscYV0pVRDnIIgsh8PDXeA&;storeId=5292&;couponState=na&;bkt=2977&;/ip/HP-Chromebook-X360-14-HD-Touchscreen-2-in-1-Laptop-Intel-Celeron-N4020-4GB-RAM-64GB-eMMC-Teal-14a-ca0130wm/518977383" link-identifier="518977383" target="">
<span class="w_iUH7">
                          HP Chromebook X360 14" HD Touchscreen 2-in-1 Laptop, Intel Celeron N4020, 4GB RAM, 64GB eMMC, Teal, 14a-ca0130wm
                         </span>
</a>
</div>
<div class="pr3 relative mb4-m">
<img alt="" class="mw-none" height="150" loading="eager" src="https://i5.walmartimages.com/seo/HP-Chromebook-X360-14-HD-Touchscreen-2-in-1-Laptop-Intel-Celeron-N4020-4GB-RAM-64GB-eMMC-Teal-14a-ca0130wm_33dec549-bf1a-4d1c-9165-7e1d3bd62a71.92e69b79b60021aa2a983207475f8a39.jpeg?odnHeight=150&;odnWidth=150&;odnBg=FFFFFF" width="150"/>
<div class="z-2 absolute bottom--2 dn db-l mb3 left--1">
<div class="relative dib" data-id="518977383">
<button aria-label='Add to cart - HP Chromebook X360 14" HD Touchscreen 2-in-1 Laptop, Intel Celeron N4020, 4GB RAM, 64GB eMMC, Teal, 14a-ca0130wm' class="w_hhLG w_8nsR w_jDfj pointer bn sans-serif b ph2 flex items-center justify-center w-auto shadow-1" data-automation-id="add-to-cart" data-pcss-hide="true" type="button">
<i class="ld ld-Plus" style="font-size:1.5rem;vertical-align:-0.25em;width:1.5rem;height:1.5rem;box-sizing:content-box" title="add to cart">
</i>
<span class="mr2">
                            Add
                           </span>
</button>
</div>
</div>
</div>
<div class="flex flex-column">
<div class="flex flex-wrap justify-start items-center lh-title" data-automation-id="product-price">
<div aria-hidden="true" class="mr1 mr2-xl b black green lh-copy f5 f4-l">
                          Now $199.00
                         </div>
<span class="w_iUH7">
                          current price Now $199.00
                         </span>
<div aria-hidden="true" class="gray mr1 strike f7 f6-l">
                          $329.00
                         </div>
<span class="w_iUH7">
                          Was $329.00
                         </span>
</div>
<span class="f6 f5-m">
<span class="w_V_DM" style="-webkit-line-clamp:2;padding-bottom:0em;margin-bottom:-0em">
                          HP Chromebook X360 14" HD Touchscreen 2-in-1 Laptop, Intel Celeron N4020, 4GB RAM, 64GB eMMC, Teal, 14a-ca0130wm
                         </span>
</span>
<div class="flex items-center mt2">
<span class="black inline-flex mr1">
<i aria-hidden="true" class="ld ld-StarFill" style="font-size:12px;vertical-align:-0.175em;width:12px;height:12px;box-sizing:content-box">
</i>
<i aria-hidden="true" class="ld ld-StarFill" style="font-size:12px;vertical-align:-0.175em;width:12px;height:12px;box-sizing:content-box">
</i>
<i aria-hidden="true" class="ld ld-StarFill" style="font-size:12px;vertical-align:-0.175em;width:12px;height:12px;box-sizing:content-box">
</i>
<i aria-hidden="true" class="ld ld-StarFill" style="font-size:12px;vertical-align:-0.175em;width:12px;height:12px;box-sizing:content-box">
</i>
<i aria-hidden="true" class="ld ld-StarHalf" style="font-size:12px;vertical-align:-0.175em;width:12px;height:12px;box-sizing:content-box">
</i>
</span>
<span aria-hidden="true" class="sans-serif gray f7">
                          464
                         </span>
<span class="w_iUH7">
                          4.3 out of 5 Stars. 464 reviews
                         </span>
</div>
<div>
</div>
</div>
</div>
</div>
</div>'''
    }

    soup = BeautifulSoup(page['content'], "html.parser")
    searchResult = BeautifulSoup(soup.prettify(), "html.parser")

    httpsGetMock = mocker.patch('src.scraper.httpsGet')
    httpsGetMock.return_value = searchResult

    query = "laptops"

    product = scraper.searchWalmart(query, 0, None)[0]

    httpsGetMock.assert_called_once_with(
        "https://www.walmart.com/search?q=laptops")

    print(product)

    ans = {
        "title": 'HP Chromebook X360 14" HD Touchscreen 2-in-1 Laptop, Intel Celeron N4020, 4GB RAM, 64GB eMMC, Teal, 14a-ca0130wm',
        "price": 'Now $199.00',
        "link": 'www.walmart.comhttps://wrd.walmart.com/track?bt=1&;eventST=click&;plmt=sb-search-top~desktop~&;pos=2&;tax=3944_1089430_3951_8835131_1737838&;rdf=1&;rd=https%3A%2F%2Fwww.walmart.com%2Fip%2FHP-Chromebook-X360-14-HD-Touchscreen-2-in-1-Laptop-Intel-Celeron-N4020-4GB-RAM-64GB-eMMC-Teal-14a-ca0130wm%2F518977383%3FadsRedirect%3Dtrue&;adUid=33e5a076-162f-428a-bcd1-29ee564fe36a&;mloc=sb-search-top&;pltfm=desktop&;pgId=laptops&;pt=search&;spQs=T4ky7SJGaU6bRFLThT-z6o2Zbo3F9KrziHssJciU08KGDJLKmC0_hyChPulrXPlVoKrtTzYv6oVQBeJ82Pst0_0s-lJh1AgfzOAYZXIecsc0JogOK-WnpPcgQiSllenn-1nlzo2IMQMlZL7TGICG02I70Grcgpt7MGKhNt9AhGYCnoPTcfEyGrl_61-QoMrfMscYV0pVRDnIIgsh8PDXeA&;storeId=5292&;couponState=na&;bkt=2977&;/ip/HP-Chromebook-X360-14-HD-Touchscreen-2-in-1-Laptop-Intel-Celeron-N4020-4GB-RAM-64GB-eMMC-Teal-14a-ca0130wm/518977383',
        "website": "walmart",
        "rating": 4.3,
        "no of ratings": 464,
        "paymentMode": 'flat'
    }

    assert (product["title"] == (ans["title"]
            if len(product["title"]) > 0 else ""))
    assert (product["price"] == ans["price"])
    assert (product["link"] == ans["link"])
    assert (product["website"] == ans["website"])
    assert (product["rating"] == ans["rating"])
    assert (product["no of ratings"] == ans["no of ratings"])
    assert (product["paymentMode"] == ans["paymentMode"])

    httpsGetMock.stopAll()
