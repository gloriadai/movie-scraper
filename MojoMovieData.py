from lxml import html
import requests

# data extraction example from movie title: the a-team

page = requests.get('http://www.boxofficemojo.com/movies/?page=main&id=ateam.htm')
tree = html.fromstring(page.text)

# Domestic Total Gross
print tree.xpath('//*[@id="body"]//font[starts-with(normalize-space(.),"Domestic Total Gross:")]/b/text()')
# Genre
print tree.xpath('//*[@id="body"]//td[starts-with(normalize-space(.),"Genre:")]/b/text()')
# Production Budget
print tree.xpath('//*[@id="body"]//td[starts-with(normalize-space(.),"Production Budget:")]/b/text()')
# MPAA Rating
print tree.xpath('//*[@id="body"]//td[starts-with(normalize-space(.),"MPAA Rating:")]/b/text()')
# Distributor
print tree.xpath('//*[@id="body"]//td[starts-with(normalize-space(.),"Distributor:")]/b/a/text()')
# Release Date
print tree.xpath('//*[@id="body"]//td[starts-with(normalize-space(.),"Release Date:")]/b/nobr/a/text()')
# Movie Title
print tree.xpath('/html/head/title/text()')

# Work around &nbsp; issue
tree = html.fromstring(page.text.replace("&nbsp;", ""))
# Foreign Box Office
print tree.xpath('//*[@class="mp_box_content"]//a[starts-with(normalize-space(.),"Foreign:")]/../following-sibling::*[1][name()="td"]/text()')
# Opening Weekend
print tree.xpath('//*[@class="mp_box_content"]//a[starts-with(normalize-space(.),"OpeningWeekend:")]/../following-sibling::*/text()')
# Widest Release
print tree.xpath('//*[@class="mp_box_content"]//td[starts-with(normalize-space(.),"WidestRelease:")]/following-sibling::*/text()')
# Close Date
print tree.xpath('//*[@class="mp_box_content"]//td[starts-with(normalize-space(.),"CloseDate:")]/following-sibling::*/text()')
# In Release
print tree.xpath('//*[@class="mp_box_content"]//td[starts-with(normalize-space(.),"In Release:")]/following-sibling::*/text()')

