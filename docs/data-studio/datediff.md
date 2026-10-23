---
url: https://docs.cloud.google.com/data-studio/datediff/
title: Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:20:10.213985+00:00
---

# Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/datediff/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# DATE_DIFF

Calculates the number of days between two compatibility mode dates.

**Important:** This function supports only compatibility mode dates. We recommend upgrading any older date fields in your data sources to the new Date or Date & Time types and using the [DATETIME_DIFF](https://docs.cloud.google.com/data-studio/datetimediff) function instead. [Learn more](https://docs.cloud.google.com/data-studio/dates-and-times).

## Sample usage

```DATE_DIFF(End Date, Start Date)```

## Syntax

```DATE_DIFF( X, Y )```

### Parameters

  * `X` \- a date field or date expression.
  * `Y` \- a date field or date expression.



## Notes

```DATE_DIFF``` calculates `X` \- `Y`. If `X` > `Y`, the result is positive, otherwise the result is negative.

## Examples

Example formula | Input | Output  
---|---|---  
` DATE_DIFF(End Date, Start Date) ` | 

  * **End Date** : Sep 28 2019 
  * **Start Date** : Sep 10 2019 

|  18   
` DATE_DIFF(End Date, Start Date) ` | 

  * **End Date** : Sep 9 2019 
  * **Start Date** : Sep 10 2019 

|  -1   
  
## Related resources

  * [Dates and times](https://docs.cloud.google.com/data-studio/dates-and-times)
  * [Calculated fields](https://docs.cloud.google.com/data-studio/about-calculated-fields)
  * [Data Studio function list](https://docs.cloud.google.com/data-studio/function-list)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
