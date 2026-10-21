---
url: https://docs.cloud.google.com/data-studio/geo-dimension-reference/
title: Geo dimension reference \u00a0|\u00a0 Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:31:03.495421+00:00
---

# Geo dimension reference  |  Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/geo-dimension-reference/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  Geo dimension reference Stay organized with collections  Save and categorize content based on your preferences. 

Geographic fields help you visualize your data in maps. The type of geographic dimension selected for a chart determines how your data will be plotted on the map. For example, to plot your data by city, select a dimension containing city names or valid city codes. To see your data plotted by country, select a dimension containing country names or codes. The actual values used to encode the geographic information must conform to the relevant standard used for that dimension, if any. Some geographic types are only supported in Google Maps and are not available in Geo charts.

This page defines the geo dimension types supported by Data Studio, along with notes for how to use these in Geo charts and Google Maps.

##  Continent 

  * **Available in:** Geo charts, Google Maps 
  * **Encoding:** [ 3-digit continent hierarchy code ](https://developers.google.com/chart/interactive/docs/gallery/geochart#Continent_Hierarchy) (for example, 001) or specify [ continent name ](https://developers.google.com/chart/interactive/docs/gallery/geochart#continent-hierarchy-and-codes) (for example, "Africa") 



###  Usage notes 

Setting a field to type Geo > Continent in non-Google Analytics data source types will cause Geo charts using that field to display the error message, **"Specified data cannot be rendered."**

####  **Geo chart zoom areas supported**

World 

##  Subcontinent 

  * **Available in:** Geo charts, Google Maps 
  * **Encoding:** [ 3-digit continent hierarchy code ](https://developers.google.com/chart/interactive/docs/gallery/geochart#Continent_Hierarchy) (for example, "011" for Western Africa) or specify [ continent name ](https://developers.google.com/chart/interactive/docs/gallery/geochart#continent-hierarchy-and-codes) (for example, "Western Africa") 



###  Usage notes 

Subcontinent is only available in Google Analytics data sources for Geo charts. Setting a field to type Geo > Subcontinent in other data source types will cause Geo charts using that field to display the error message, **"Specified data cannot be rendered."**

####  **Geo chart zoom areas supported**

World 

##  Country 

  * **Available in:** Geo charts, Google Maps 
  * **Encoding:** [ ISO 3166-1 alpha-2 code ](http://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) (for example, "AU" for Australia), [ ISO-3166-1 alpha-3 code ](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3) (for example, "AUS" for Australia), [ 3-digit country code ](https://unstats.un.org/unsd/methodology/m49/) (for example, "036" for Australia), or specify country by name (for example, "France") 



###  Usage notes 

####  **Geo chart zoom areas supported**

World, Continent, Subcontinent 

##  Country subdivision (1st level) 

  * **Available in:** Geo charts, Google Maps 
  * **Encoding:** [ ISO-3166-2 code ](https://en.wikipedia.org/wiki/ISO_3166-2) (for example, "US-AL" for Alabama, "BR-RJ" for Rio de Janeiro), [ US state FIPS code ](https://en.wikipedia.org/wiki/Federal_Information_Processing_Standard_state_code) (for example, "01" for Alabama), [ UK NUTS 1 code ](https://en.wikipedia.org/wiki/NUTS_statistical_regions_of_the_United_Kingdom) (for example, "UKF" for East Midlands), or specify country subdivision name (for example, "Alabama") 



###  Usage notes 

Country subdivision (1st level) corresponds, for example, to US states, Canadian provinces, French regions, Spanish autonomous communities, and Japanese prefectures. Geo chart don't support FIPS or NUTS codes. 

####  **Geo chart zoom areas supported**

Country 

> Country subdivision (1st level) is not available for the following countries: 
> 
> ####  Country subdivision (1st level) excluded countries 
> 
>   * AC 
>   * AI 
>   * AQ 
>   * AS 
>   * AW 
>   * AX 
>   * BL 
>   * BM 
>   * BV 
>   * CC 
>   * CK 
>   * CP 
>   * CW 
>   * CX 
>   * DG 
>   * EA 
>   * EH 
>   * FK 
>   * FO 
>   * GF 
>   * GG 
>   * GI 
>   * GP 
>   * GS 
>   * GU 
>   * HK 
>   * HM 
>   * IC 
>   * IM 
>   * IO 
>   * JE 
>   * KE 
>   * KY 
>   * MC 
>   * MF 
>   * MO 
>   * MP 
>   * MQ 
>   * MS 
>   * MT 
>   * NC 
>   * NF 
>   * NU 
>   * PF 
>   * PM 
>   * PN 
>   * PR 
>   * PS 
>   * RE 
>   * SG 
>   * SJ 
>   * SX 
>   * TA 
>   * TC 
>   * TF 
>   * TK 
>   * TW 
>   * UM 
>   * VA 
>   * VG 
>   * VI 
>   * WF 
>   * WS 
>   * XK 
>   * YT 
> 


##  Country subdivision (2nd level) 

  * **Available in:** Google Maps 
  * **Encoding:** [ ISO-3166-2 code ](https://en.wikipedia.org/wiki/ISO_3166-2) (for example, "FR-75" for Paris), [ US county FIPS code ](https://en.wikipedia.org/wiki/List_of_United_States_FIPS_codes_by_county) (for example, "01049" for De Kalb County), or specify country subdivision name (for example, De Kalb County) 



###  Usage notes 

Country subdivision (2nd level) corresponds, for example, to US counties, French departments, and Italian and Spanish provinces. 

> Country subdivision (2nd level) is not available for the following countries: 
> 
> ####  Country subdivision (2nd level) excluded countries 
> 
>   * AC 
>   * AI 
>   * AQ 
>   * AS 
>   * AW 
>   * AX 
>   * BL 
>   * BM 
>   * BV 
>   * CC 
>   * CK 
>   * CP 
>   * CW 
>   * CX 
>   * DG 
>   * EA 
>   * EH 
>   * FK 
>   * FO 
>   * GF 
>   * GG 
>   * GI 
>   * GP 
>   * GS 
>   * GU 
>   * HK 
>   * HM 
>   * IC 
>   * IM 
>   * IO 
>   * JE 
>   * KE 
>   * KY 
>   * MC 
>   * MF 
>   * MO 
>   * MP 
>   * MQ 
>   * MS 
>   * MT 
>   * NC 
>   * NF 
>   * NU 
>   * PF 
>   * PM 
>   * PN 
>   * PR 
>   * PS 
>   * RE 
>   * SG 
>   * SJ 
>   * SX 
>   * TA 
>   * TC 
>   * TF 
>   * TK 
>   * TW 
>   * UM 
>   * VA 
>   * VG 
>   * VI 
>   * WF 
>   * WS 
>   * XK 
>   * YT 
> 


##  Designated market area 

  * **Available in:** Geo charts, Google Maps 
  * **Encoding:** [ Geographical targeting criteria ID ](https://developers.google.com/analytics/devguides/collection/protocol/v1/geoid) (for example, 200807), DMA name (for example, San Francisco-Oakland-San Jose CA) 



###  Usage notes 

Designated market area is only available in Google Analytics data sources for Geo charts. Setting a field to type Geo > Designated market area in other data source types will cause Geo charts using that field to display the error message, **"Specified data cannot be rendered."**

Designated market areas are used to plot [ media markets ](https://en.wikipedia.org/wiki/Media_market). These geo field types are only available for the United States. 

####  **Geo chart zoom areas supported**

Country, Region 

##  City 

  * **Available in:** Geo charts, Google Maps 
  * **Encoding:** [ Geographical targeting criteria ID ](https://developers.google.com/google-ads/api/data/geotargets) (for example, 1006886), or specify the city by name (for example, "Paris"). 



###  Usage notes 

Geo charts plot the _City_ field types with map markers, rather than shaded regions, with larger markers representing greater metric values than smaller markers as shown in the following image.

![A United States geo chart with various sized city markers in shades of gray indicates the number of web sessions, and a gray gradient scale from light to dark gray represents a range of values from 11 to 589.](https://docs.cloud.google.com/static/data-studio/images/geo-map-example-city-2016-10-17.png)

####  Geo chart zoom areas supported 

World, Continent, Subcontinent, Country, Region 

Because city names are not unique, you should use the Geo charts zoom area to narrow down the map area and avoid duplication. 

##  Postal Code 

  * **Available in:** Google Maps 
  * **Encoding:** n/a 



###  Usage notes 

For bubble maps, Postal Code can be a US ZIP code (for example, 94043) or an international postal code (example: L4L 9H8). For filled area maps Postal Code can be a US ZIP code. 

##  Address 

  * **Available in:** Google Maps (bubble map only) 
  * **Encoding:** n/a 



###  Usage notes 

For accuracy, addresses should be complete, for example: 1600 Amphitheatre Pkwy, Mountain View, CA 94043. For a partial address ("1600 Amphitheatre Pkwy"), Google Maps might not be able to resolve the city, region, or country. 

##  Latitude Longitude 

  * **Available in:** Geo charts, Google Maps (bubble map only) 
  * **Encoding:** Comma separated latitude and longitude decimal values (for example, "51.5074,-0.1278" specifies to London, England) 



###  Usage notes 

####  **Geo chart zoom areas supported**

World, Continent, Subcontinent, Country, Region 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
