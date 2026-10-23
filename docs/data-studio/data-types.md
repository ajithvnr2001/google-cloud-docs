---
url: https://docs.cloud.google.com/data-studio/data-types/
title: Data types \u00a0|\u00a0 Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:19:34.489260+00:00
---

# Data types  |  Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/data-types/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  Data types Stay organized with collections  Save and categorize content based on your preferences. 

A field's _data type_ specifies the kind of values the field can contain and determines how that field's data appears in your reports, as well as which operations are allowed for the field and which are not allowed. For example, you can't apply an arithmetic function to a **Text** type field, or use a **Number** type field as the date range dimension in a report.

The following table shows the supported field types, along with the kind of data expected as input, and examples of how that data might look in your reports.

Type  |  Expected data  |  Report examples   
---|---|---  
**Number** |  A floating point number.  |  1,234.56   
**Percent** |  A floating point number representing a ratio.  |  61.73%   
**Duration** |  An integer representing a length of time in seconds. This will be formatted into a standard time display (with hours, minutes, and seconds) in reports.  |  01:43:19   
**Currency** |  A floating point number representing a monetary value. This will be formatted to include the appropriate currency symbol in reports. 

> Changing the currency type doesn't convert to the new type or change the decimal and comma placement. It simply applies the specified currency symbol to the metric value. To change the decimal and comma placement, [ format the field ](https://docs.cloud.google.com/data-studio/format-fields-in-reports) with a default or custom value. For example, to apply a lakhs and crores format, use a custom formatting string such as the following: ` ##,##,##,##0.00; `

|  $1,234.56  173.9 €  ¥30,093   
**Text** |  Zero or more letters, numbers, characters, or symbols.  |  A1B2C3   
**Date & Time ** |  An actual calendar date, a calendar date with time, or an abstract date or time index. This will be formatted according to the locale.  Learn more about [ dates and times in Data Studio](https://docs.cloud.google.com/data-studio/dates-and-times).  |  2020-09-21  2020-09-21 12:35 PM  Q4 2020  Week 1   
**Boolean** |  A logical value. 

> If the dataset doesn't provide Boolean values, you can create a **Boolean** data type field by using a calculated field with a ` CASE ` statement:  ` CASE WHEN... THEN TRUE ELSE FALSE END ` Learn more about [ CASE statements ](https://docs.cloud.google.com/data-studio/case-searched). 

|  true  false   
**Geo** |  A value representing a geographic region, such as a country name, latitude and longitude, ISO code, or Google Ads criteria ID.  Learn more about [ visualizing geographic data ](https://docs.cloud.google.com/data-studio/geo-dimension-reference).  |  United Kingdom  51.5074,-0.1278  1006886   
**URL** |  An address of a web page.  |  https://datastudio.google.com/   
**Hyperlink** |  A clickable link to a URL. Hyperlink fields are created by the [ HYPERLINK ](https://docs.cloud.google.com/data-studio/hyperlinks-in-data) function.  |  [ See an example of Hyperlink fields ](https://datastudio.google.com/reporting/1tgcseoJ7-LLWNJqRu1thi5Ij8qmHfiEz/page/xGxK)  
**Image** |  An image. Image fields are created by the [ IMAGE ](https://docs.cloud.google.com/data-studio/image) function.  |  ![A Tyrannosaur stands in a primeval forest holding a computer tablet displaying data visualizations.](https://docs.cloud.google.com/static/data-studio/images/dino-bi-2024-06-04.png)  
**Image Link** |  A clickable image. Image Link fields are created by the HYPERLINK function.  |  [ See an example of Image Link fields ](https://datastudio.google.com/reporting/1zOZ2aPL8HYl4JIhjsMQKvj5BSWwcKRdv/page/xGxK)  
  
To change a field's data type, use the **Type** drop-down menu in the data source edit page. If the [field editing in reports](https://docs.cloud.google.com/data-studio/edit-fields-in-your-reports) option is enabled for the data source, you can also change a field's data type directly in reports based on this data source.

If the [field editing in reports](https://docs.cloud.google.com/data-studio/edit-fields-in-your-reports) option is enabled for the data source, you can also [apply custom value formatting](https://docs.cloud.google.com/data-studio/format-fields-in-reports) to **Number** and **Date & Time** type fields, without sending additional SQL queries to the database.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
