---
url: https://docs.cloud.google.com/looker/docs/time-formatting-for-charts/
title: Time formatting for charts \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:34:22.381312+00:00
---

# Time formatting for charts  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/time-formatting-for-charts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Time formatting for charts Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** This page is part of the [Retrieve and chart data](https://docs.cloud.google.com/looker/docs/retrieve-and-chart-data) learning series.

If your chart has a time dimension on the x-axis, you can change the formatting of the x-axis label by using the **Time Label Format** setting in the **X** tab of the visualization options.

![](https://docs.cloud.google.com/static/looker/docs/images/time-label-format-258.png)

## Time label expressions

You can format time values in Looker charts by using the syntax in the following table.

Format Type | Description | Expression  
---|---|---  
**Time**  
Time | Milliseconds as a decimal number: 000 to 999 | `%L`  
Time | Second as a two-digit number: 00 to 59 | `%S`  
Time | Minute as a two-digit number: 00 to 59 | `%M`  
Time | Hour as a decimal number (24-hour clock): 00 to 23 | `%H`  
Time | Hour as a decimal number (12-hour clock): 01 to 12 | `%I`  
Time | Either AM or PM | `%p`  
**Date**  
Date | Day of the year as a decimal number: 001 to 366 | `%j`  
Date | Zero-padded day of the month: 01 to 31 | `%d`  
Date | Space-padded day of the month (equivalent to `%_d`): 1 to 31 | `%e`  
Date | Full weekday name: Monday, Tuesday, Wednesday | `%A`  
Date | Abbreviated weekday name (3-letter): Mon, Tue, Wed | `%a`  
Date | Weekday as a decimal number (Sunday as the first day of the week): 0 to 6 | `%w`  
**Week**  
Week | Week number of the year (Sunday as the first day of the week) as a two-digit number: 00 to 53 **Note** : `%U` uses the [ISO week date](https://en.wikipedia.org/wiki/ISO_week_date) standard offset by one day. | `%U`  
Week | Week number of the year (Monday as the first day of the week) as a two-digit number: 00 to 53 **Note** : `%W` uses the [ISO week date](https://en.wikipedia.org/wiki/ISO_week_date) standard. | `%W`  
**Month**  
Month | Two-digit month: 01 through 12 (1-12 format not supported) | `%m`  
Month | Abbreviated month name: Jan, Feb, Mar  | `%b`  
Month | Full month name: January, February, March  | `%B`  
**Year**  
Year | Two-digit year: 00 to 99 | `%y`  
Year | Four-digit year: 2000, 2001, 2002 | `%Y`  
**Combination**  
Combination | Full time, of the form "%H:%M:%S": 23:56:12 | `%X`  
Combination | Full date, of the form "%m/%d/%Y": 01/27/2014 | `%x`  
Combination | Datetime format with the following: "%a %b %e %H:%M:%S %Y": Mon Jan 1 23:56:04 2014 | `%c`  
**Note:** Quarter time formatting is not supported. Consider including a quarter timeframe in your date [dimension_group](https://docs.cloud.google.com/looker/docs/reference/param-field-dimension-group) and selecting that quarter timeframe in the visualization to display and filter data by quarters.

## Examples

You can combine expressions together to create custom time formats, such as in the examples in the following table.

Input | Time Label Format | Output  
---|---|---  
August 14, 2014 10:31 PM | `%b '%y, %H:%M` | Aug '14, 22:31  
August 14, 2014 10:31 PM | `%B %Y, %I:%M %p` | August 2014, 10:31 PM  
August 14, 2014 10:31 PM | `%x %X` | 08/14/2014 22:31:00  
August 14, 2014 10:31 PM | `%I:%M:%S %p` | 10:31:00 PM  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
