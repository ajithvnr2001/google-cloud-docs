---
url: https://docs.cloud.google.com/data-studio/convert-text-and-numbers-to-date-and-date--time/
title: Convert text and numbers to date and time \u00a0|\u00a0 Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:24:29.834369+00:00
---

# Convert text and numbers to date and time  |  Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/convert-text-and-numbers-to-date-and-date--time/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  Convert text and numbers to date and time Stay organized with collections  Save and categorize content based on your preferences. 

You can convert text and numeric fields in your data source into valid Date or Date & Time fields in Data Studio using calculated fields. This helps you parse ambiguous date formats so you can accurately sort, filter, and visualize time-based data in your reports.

Sometimes, though, the data is ambiguous, making it difficult for Data Studio to know how to handle it. For example:

  * 20201210 could represent a number or currency value: $20,201,210.
  * 12/10/2020 could represent Dec 10, 2020 or Oct 12, 2020.



## Can't convert to date

If you connect to data that contains ambiguous dates or times, you may see a message saying "Data Studio can't convert [field] to a date". To resolve this, do one of the following:

### Change the underlying data

If you can edit the dataset, consider changing the format of your date field to a full year, month, and day format. You may also be able to set the field's data type to date or date and time. This is the recommended approach, especially if you'll be creating multiple data sources from this dataset.

### Convert to date using a calculated field

To create a valid Date or Date & Time field from your original unrecognized field, create a new calculated field and use the [PARSE_DATE](https://docs.cloud.google.com/data-studio/parsedate) or [PARSE_DATETIME](https://docs.cloud.google.com/data-studio/parsedatetime) function. See the following examples, replacing `field` with the name of the original (unrecognized) field.

#### Example formulas

Following are examples of how to convert text fields to Date fields:

Format | Formula  
---|---  
2020-03-18 | PARSE_DATE("%Y-%m-%d", `field`)  
2020/03/18 | PARSE_DATE("%Y/%m/%d", `field`)  
20200318 | PARSE_DATE("%Y%m%d", `field`)  
3/18/2020 | PARSE_DATE("%m/%d/%Y", `field`)  
18/3/2020 | PARSE_DATE("%d/%m/%Y", `field`)  
Mar 18, 2020 | PARSE_DATE("%b %d, %Y", `field`)  
Wed, Mar 18, 2020 | PARSE_DATE("%a, %b %d, %Y", `field`)  
March 18, 2020 | PARSE_DATE("%B %d, %Y", `field`)  
Wednesday, March 18, 2020 | PARSE_DATE("%A, %B %d, %Y", `field`)  
  
Following are examples of how to convert text fields to Date & Time fields:

Format | Formula  
---|---  
2020-03-18 16:45:00.000000 | PARSE_DATETIME("%Y-%m-%d %H:%M:%E*S", `field`)  
2020-03-18T16:45:00.000000 | PARSE_DATETIME("%Y-%m-%dT%H:%M:%E*S", `field`)  
  
Following is an example of how to convert a numeric field to a Date field:

Format | Formula  
---|---  
20200318 | PARSE_DATE("%Y%m%d", CAST(`field` AS TEXT))  
  
## Related resources

  * [About calculated fields](https://docs.cloud.google.com/data-studio/about-calculated-fields)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
