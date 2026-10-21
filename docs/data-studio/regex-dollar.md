---
url: https://docs.cloud.google.com/data-studio/regex-dollar/
title: Dollar sign ($) \u00a0|\u00a0 Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:04:59.634242+00:00
---

# Dollar sign ($)  |  Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/regex-dollar/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)



Send feedback 

#  Dollar sign ($) Stay organized with collections  Save and categorize content based on your preferences. 

Use the dollar sign to match the preceding, adjacent characters at the end of a string.

For example, `end$` matches the following:

  * Temporarily susp**end**
  * We're going off the deep **end**
  * Match the characters that prep**end**



However, `end$` doesn't match the following:

  * Temporarily suspend.
  * We're going off the deep end.
  * Match the characters that prepend.



The preceding three lines all end with **nd.** rather than the **end** characters that you're matching with the regular expression.

Use this type of regular expression to create segments, filters, or goal steps that match a URI. For example, if you're testing the efficacy of a new HTM version of a page versus an older HTML version, you can identify the versions separately by using regular expressions such as the following:

  * email-signup\\.htm$
  * email-signup\\.html$



Use [the backslash](https://docs.cloud.google.com/data-studio/regex-example-dot-backslash) to escape the dot and ensure that it is interpreted literally.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
