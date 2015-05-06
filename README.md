# Welcome to Datamation.nyc 

What if we had a way to save PDF as open-data? What if we had links back to the actual machine-readable data?

Our big idea is to combine the power of Github's collaborative framework and open-source tools to provide direct access to city agency data. We hope to streamline the process of publishing data and automate tasks when possible. This project is designed to explore a model for scraping, parsing and publishing using the CROW [City Record Online] project as our first target dataset.

With the support of legislators and civic hackers, Datamation wants to change the way the city releases it's data, too often within semi-transparent PDFs. The format simply does not conform to the core attribute of open data: machine readability. Needed is a way to aggregate these documents, apply metadata along with contributed open-source scrapers, parsers and API’s, to once and for all liberate the embedded data.

Since all content is data, Datamation hopes to work with motivated legislators and civic hackers within an open-by-design, collaborative ecosystem.

A salient question is "do PDFs really suck?" Well, yes and no...Back in the early days of Web 1.0, as a contract developer for the Greater New York Hospital Associations, I was tasked with publishing their bi-weekly newsletter and reports. PDF, with postscript printer drivers and cross platform readers was chosen as a least painful way to publish information to the widest possible audience. Creating structured web pages was the ultimate goal however this often lagged given the lack of decent document conversion tools. Sound familiar? The worst mistake however was that no thought was ever given to maintaining links to the original embedded tabular data.

It's now 20 years later and the city is still publishing a lot of it's data in guess what PDF. There is often little or no structured metadata associated with the PDF unless maybe buried as scrapable  text within the document and no links back to the original structured data sources.

Datamation will give legislators and civic hackers a repository of tools to crawl, scrape, and parse PDF documents. The platform will be a model for city agencies and departments to publish their machine-readable data and engage with, legislators and the civic open data community. 

As background, City Record is the daily broadsheet of city business: the procurement of goods and services, contracts & awards, meetings, and legal notices.
A city councilmember may be getting numerous complaints from constituents concerned about rumors of impending alterations within their historic landmark district. City Record provides info of proposed Landmarks Preservation Commission certificates and meetings. A civic technologist will find this data useful to build apps that track trends in gentrification, useful for urban planners, small businesses or neighborhood associations.

The purpose behind Datamation is to engage both legislators and the broader civic tech community to join in the policy making process of government. The hope is city agencies and departments will be encouraged and adopt this approach to further their goals.

Datamation's core infrastructure will be modeled on three principles:

* A repository of code. Crawlers, scrapers & parsers (oh my) to filter and clean data with APIs to lower the barrier for a more sustainable data flow.
* A data chain of custody. Codebooks, schema and metadata remain though personnel and administrations change.
* A supportive, machine-readable data culture. Open-source tools and a rich source of metadata!

Please join us!

<!--
### Jekyllized gulp.js
* doctor (checks _config)
* check (js csslint hint)
* build (run gulpfile)
* publish (seems to be required for deploy => github)
* deploy (the world is your erster)

There will also be some parcers and scrapers under development
-->

TODO

* /dcas/spiders/dcas_spider.py PDF links & title parcer
	- remove empty values
	- create rows for 2008 & 2009 links & titles 

* Order by year