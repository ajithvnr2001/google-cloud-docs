---
url: https://docs.cloud.google.com/data-studio/regex-example-caret/
title: Caret (^) \u00a0|\u00a0 Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:17:28.137837+00:00
---

# Caret (^)  |  Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/regex-example-caret/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)



Send feedback 

#  Caret (^) Stay organized with collections  Save and categorize content based on your preferences. 

Use the caret to match the following adjacent characters at the beginning of a string.

For example, `^St` matches the following:

  * **St** art here
  * **St** and here
  * **St** op here



However, `^St` doesn't match the following:

  * 1 Start here
  * 2 Stand here
  * 3 Stop here



The preceding three lines start with a digit and a space, not with the letters "St".

Use this type of regular expression to create segments, filters, or goal steps that match a URI. For example, if you need to isolate data for a particular directory of pages, you can use expressions such as the following:

  * `^/mens/` (matches www.example.com**/mens/**)
  * `^/womens/` (matches www.example.com**/womens/**)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
