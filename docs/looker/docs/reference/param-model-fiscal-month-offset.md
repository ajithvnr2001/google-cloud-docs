---
url: https://docs.cloud.google.com/looker/docs/reference/param-model-fiscal-month-offset/
title: fiscal_month_offset \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:40:18.846595+00:00
---

# fiscal_month_offset  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/param-model-fiscal-month-offset/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ LookML Reference ](https://docs.cloud.google.com/looker/docs/reference/lookml-quick-reference)



Send feedback 

#  fiscal_month_offset Stay organized with collections  Save and categorize content based on your preferences. 

## Usage
    
    
    
    fiscal_month_offset: 3
    

Hierarchy [Model File](https://docs.cloud.google.com/looker/docs/reference/param-model) `fiscal_month_offset` |  Default Value 0 Accepts An integer   
---|---  
  
## Definition

If you don't use the calendar year for your fiscal year, you can specify when your fiscal year begins for each model. Use `fiscal_month_offset` to declare the number of months your fiscal year is offset from the calendar year. For example, `fiscal_month_offset: 1` will specify that the fiscal year starts in February.

Although `fiscal_month_offset` is typically set to a positive integer between 0 and 11 (inclusive), `fiscal_month_offset` accepts any integer as a value, including negative integers. In the case of a negative integer, your fiscal year is set to the past. For example, `fiscal_month_offset: -3` causes Q1 of fiscal year 2018 to start in October of 2017. In the case of an integer greater than 11, your fiscal year starts a year or more into the future. For example, `fiscal_month_offset: 15` causes Q1 of fiscal year 2018 to start in April of 2019.

Setting `fiscal_month_offset` specifies the year start of all fiscal timeframes used in [dimension_groups](https://docs.cloud.google.com/looker/docs/reference/param-field-dimension-group) and in [advanced matches](https://docs.cloud.google.com/looker/docs/filtering-and-limiting#advanced_matches_filters) filter settings.

  * fiscal_year
  * fiscal_quarter
  * fiscal_month_num
  * fiscal_quarter_of_year



Any fiscal timeframes you create can be selected in the field picker and used to [specify values for filters](https://docs.cloud.google.com/looker/docs/filtering-and-limiting#filtering_data).

![](https://docs.cloud.google.com/static/looker/docs/images/explore-fiscal-quarter-basic-with-field-picker-48.png)

For [advanced matches filter expressions](https://docs.cloud.google.com/looker/docs/filter-expressions#date_&_time), you can refer to fiscal years and quarters as absolute dates or relative dates.

  * When using relative dates for fiscal years, insert the word `fiscal` in your filter expression for the quarter(s) or year(s). For example: `2 fiscal quarters`.

![](https://docs.cloud.google.com/static/looker/docs/images/explore-fiscal-relative-year-adv-match-48.png)

  * When using absolute dates for fiscal years, add `FY` in front of the year. For example: `FY2016`.

![](https://docs.cloud.google.com/static/looker/docs/images/explore-fiscal-year-adv-match-48.png)

  * When using absolute dates for a fiscal quarter, use the format `FY<YEAR>-<QUARTER>`. For example:`FY2016-Q1`.

![](https://docs.cloud.google.com/static/looker/docs/images/explore-fiscal-qtr-adv-match-48.png)




You also can use fiscal date references in [individual date types](https://docs.cloud.google.com/looker/docs/reference/param-dimension-filter-parameter-types#individual_time_and_date_types) for dimensions and filters. Typically, however, using [dimension_groups](https://docs.cloud.google.com/looker/docs/reference/param-field-dimension-group) is the better practice.

## Examples

To set your fiscal year to start in April, add the `fiscal_month_offset` to your model file:
    
    
    connection: thelook
     ### INCLUDES ###
    include: '*.view.lkml'
    include: '*.dashboard.lookml'
    fiscal_month_offset: 3
    

In this example, the fiscal year will begin in April and the first quarter will include April, May, and June.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-22 UTC."],[],[]] 
