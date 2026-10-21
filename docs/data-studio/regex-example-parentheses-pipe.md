---
url: https://docs.cloud.google.com/data-studio/regex-example-parentheses-pipe/
title: Parentheses ( ) and pipe | \u00a0|\u00a0 Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T17:04:45.772126+00:00
---

# Parentheses ( ) and pipe |  |  Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/regex-example-parentheses-pipe/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)



Send feedback 

#  Parentheses ( ) and pipe | Stay organized with collections  Save and categorize content based on your preferences. 

## Parentheses ( )

Use parentheses to group parts of an expression together.

For example, if you need to match a set of characters that appear in a number of different product SKUs, then you can group those characters together in parentheses. In this scenario, you have a beach sandal that you sell for men and women, and your product SKUs look like this:

  * MN**BS** 010212 (men's beach sandal, style 01, color 02, size 12)
  * WM**BS** 020208 (women's beach sandal, style 02, color 02, size 08)



You could create the following regular expression to capture all beach-sandal SKUs:

`\D+(BS)\d+`

  * `\D` (non-numeric character)
  * `+` (one or more times)
  * `(BS)` (character code for beach sandal)
  * `\d` (numeric character)
  * `+` (one or more times)



## Pipe |

Use the pipe to create an OR condition in an expression.

For example, here's a way to create an expression to match your beach-sandal SKUs:

`(MN|WM)BS\d+`

  * `(MN OR WM)`
  * `BS` (character code for beach sandals)
  * `\d` (numeric character)
  * `+` (one or more times)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-14 UTC."],[],[]] 
