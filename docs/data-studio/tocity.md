---
url: https://docs.cloud.google.com/data-studio/tocity/
title: TOCITY \u00a0|\u00a0 Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:24:39.635833+00:00
---

# TOCITY  |  Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/tocity/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  TOCITY Stay organized with collections  Save and categorize content based on your preferences. 

Returns the city name of the specified Google Ads criteria ID.

## Sample usage

```TOCITY(Criteria ID)```

## Syntax

```TOCITY( X )```

### Parameters

  * _`X`_ \- A field that provides a valid Google Ads criteria ID for a city



## Examples

Example formula | Input | Output  
---|---|---  
` TOCITY(City Code) ` |  1023191  |  New York   
**Important:** **Note** : passing a non-existent or incorrect `criteria_ID` may result in an error in your charts. For example, passing a `criteria_ID` for a country or neighborhood instead of a city will break your chart.

## Related resources

  * [Google Ads API > Geo targets](https://developers.google.com/google-ads/api/data/geotargets)
  * [Calculated fields](https://docs.cloud.google.com/data-studio/about-calculated-fields)
  * [Data Studio function list](https://docs.cloud.google.com/data-studio/function-list)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
