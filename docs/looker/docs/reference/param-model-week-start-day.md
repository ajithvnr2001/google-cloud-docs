---
url: https://docs.cloud.google.com/looker/docs/reference/param-model-week-start-day/
title: week_start_day \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:40:19.524554+00:00
---

# week_start_day  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/param-model-week-start-day/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ LookML Reference ](https://docs.cloud.google.com/looker/docs/reference/lookml-quick-reference)



Send feedback 

#  week_start_day Stay organized with collections  Save and categorize content based on your preferences. 

## Usage
    
    
    week_start_day: monday
    

Hierarchy [Model File](https://docs.cloud.google.com/looker/docs/reference/param-model) `week_start_day` |  Default Value `monday` Accepts A day of the week (`monday`, `tuesday`, `wednesday`, `thursday`, `friday`, `saturday`, or `sunday`)   
---|---  
  
## Definition

You can adjust the day that Looker considers to be the start of a week with the `week_start_day` parameter. Using `week_start_day` affects:

  * The way that data appears in your tables
  * The sort order of the tables
  * The operation of filters



The `week_start_day` parameter works with three of the four week-related [`timeframes`](https://docs.cloud.google.com/looker/docs/reference/param-field-dimension-group#timeframes):

timeframe | Works with `week_start_day`?  
---|---  
`day_of_week_index` | Yes  
`week` | Yes  
`day_of_week` | Yes  
`week_of_year` | No  
  
`week_start_day` does not work with `week_of_year` because that timeframe is based on the ISO standard, which uses Monday weeks.

## Examples

Adjust weeks to start on Sunday instead of Monday:
    
    
    week_start_day: sunday
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-22 UTC."],[],[]] 
