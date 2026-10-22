---
url: https://docs.cloud.google.com/data-studio/filter-examples/
title: Filter examples \u00a0|\u00a0 Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:44:19.353350+00:00
---

# Filter examples  |  Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/filter-examples/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  Filter examples Stay organized with collections  Save and categorize content based on your preferences. 

####  Include only United States, Canada, or Mexico 

Suppose you want to limit a chart's information to just data coming from the United States, Mexico, or Canada. Select the chart and add the following filter: 

  1. Include/Exclude: **Include**
  2. Dimension: _Country_
  3. Match Type: **IN**
  4. Value: ` United States, Canada, Mexico `



![The Edit Filter dialog for a filter called Country filter, with the settings Include In United States, Canada, Mexico for the field Country.](https://docs.cloud.google.com/static/data-studio/images/filter-example-country-in-2020-06-12.png)

> You could also do this using 3 OR clauses. But it's easier to use IN with a list. 

####  Exclude "(not set)" 

To exclude "(not set)" values from your charts, use an Exclude filter. For example: 

  1. Include/Exclude: **Exclude**
  2. Dimension: _Campaign_
  3. Match Type: **Equals**
  4. Value: ` (not set) `



![The Edit Filter dialog for a filter called Exclude not set filter with the settings Exclude Equal to \(=\) \(not set\) for the field Campaign.](https://docs.cloud.google.com/static/data-studio/images/filter-example-exclude-not-set-2020-06-12.png)

####  Find data at the end of a value 

The RegExp Match and RegExp Contains operators let you perform more complex matches. For example, to filter data that contains a value at the end of the data, you can use the end-of-line marker $: 

  1. Include/Exclude: **Include**
  2. Dimension: _Medium_
  3. Match Type:: **RegExp Match**
  4. Value:. ` *c$ `



![The Edit Filter dialog for a filter called Include c at end of data with the settings Include RegExp Match.*c$ for the field Medium.](https://docs.cloud.google.com/static/data-studio/images/filter-example-include-c-2020-06-12.png)

When applied to the Analytics _Medium_ dimension, you'd include values like "organic" and "cpc." 

###  Understanding the regular expression: .`*c$`

> `.* ` means "match anything" (including nothing), 
> 
> then the literal letter "c" 
> 
> ` $ ` means the "end of line" character. (To match the beginning of the string, use ^.) 

Here's another example: 

` ^c.*k.*$ ` matches text that begins with the letter c, followed by anything, followed by the letter k, followed by anything until the end of the string. This would match values like "cook", "cookie" and "cake". 

####  Exclude data that doesn't begin with an alphabetic character 

Regular expression character classes are a powerful shortcut for matching types characters. For example: 

  1. Include/Exclude: **Exclude**
  2. Match Type:: **RegExp Match**
  3. Value: ` ^[[:^alpha:]].* `



![The Edit Filter dialog for a filter called Exclude non-alpha characters, with the settings Exclude RegExp Match ^\[\[](https://docs.cloud.google.com/static/data-studio/images/filter-example-exclude-non-alpha-2020-06-12.png)

This will filter out non-alphabetic characters, such as Japanese kanji or Korean Hangul. 

###  Understanding the regular expression: ` ^[[:^alpha:]].* `

> ` ^ ` means "beginning of string" 
> 
> ` [[:alpha:]] ` is the alphabetic [A-Za-z] character class. [[:^alpha:]] negates the class ("not alphabetic") 
> 
> `.* ` means "match anything" 

## Related resources

[Google RE2 regular expression syntax](https://github.com/google/re2/wiki/Syntax).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
