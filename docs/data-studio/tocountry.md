---
url: https://docs.cloud.google.com/data-studio/tocountry/
title: TOCOUNTRY \u00a0|\u00a0 Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:44:53.864189+00:00
---

# TOCOUNTRY  |  Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/tocountry/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  TOCOUNTRY Stay organized with collections  Save and categorize content based on your preferences. 

Returns the country name for the specified geolocation.

## Sample usage

`TOCOUNTRY(Country Code)`

## Syntax

`TOCOUNTRY(X [,input_format])`

### Parameters

  * `X` \- A text field or expression, or a geo field or expression.
  * `input_format` \- format for text field `X`. Optional if `X` is correctly configured as a geo field.



## Input format

`TOCOUNTRY` accepts the following input formats if `X` is a text field:

  * [COUNTRY_ISO_CODE](http://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)
  * [REGION_ISO_CODE](http://en.wikipedia.org/wiki/ISO_3166-2)



## Examples

Example formula | Input | Output  
---|---|---  
` TOCOUNTRY(Country Code) ` |  PE  |  Peru   
` TOCOUNTRY(Region ID,'REGION_ISO_CODE') ` |  US-CA  |  United States   
  
## Related resources

  * [Calculated fields](https://docs.cloud.google.com/data-studio/about-calculated-fields)
  * [Data Studio function list](https://docs.cloud.google.com/data-studio/function-list)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
