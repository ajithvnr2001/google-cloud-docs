---
url: https://docs.cloud.google.com/data-studio/regex-example-brackets/
title: Square brackets [ ] and the hyphen - \u00a0|\u00a0 Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:42:06.043315+00:00
---

# Square brackets [ ] and the hyphen -  |  Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/regex-example-brackets/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)



Send feedback 

#  Square brackets [ ] and the hyphen - Stay organized with collections  Save and categorize content based on your preferences. 

## Square brackets [ ]

Use square brackets to create a set of characters to match.

When you include a series of characters in brackets, your expression matches one of those characters.

For example, the expression `PART[123]` matches the following:

  * PART1
  * PART2
  * PART3



The expression doesn't match the following:

  * PART12
  * PART23
  * PART123



## Hyphen -

Use the hyphen along with the brackets to create a range of characters to match.

For example, if you need to match any uppercase letter, you can specify `[A-Z]`.

If you need to match any digit, you can specify `[0-9]`.

If you needed to match all of the part numbers, you could use the following expression:

`[A-Z]+[0-9]+`

  * `[A-Z]` (matches any uppercase letter).
  * `+` (one or more times).
  * `[0-9]` (matches any digit).
  * `+` (one or more times).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
