---
url: https://docs.cloud.google.com/data-studio/regex-example-question-plus-asterisk/
title: Question mark (?), plus sign (+), asterisk (*) \u00a0|\u00a0 Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:43:58.628872+00:00
---

# Question mark (?), plus sign (+), asterisk (*)  |  Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/regex-example-question-plus-asterisk/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)



Send feedback 

#  Question mark (?), plus sign (+), asterisk (*) Stay organized with collections  Save and categorize content based on your preferences. 

You can use the regular expression special characters question mark (?), plus sign (+), and asterisk (*). These characters help you define patterns to transform and analyze text in your Data Studio reports and dashboards. With these patterns, you can match diverse text structures to refine your data, improving its visualization and presentation.

## Question mark (?)

The question mark (?) matches the preceding character zero or one times.

For example, `10?` matches the following:

  * 1
  * 10



### Example

Match an IP address with one or two digits in the last section.

For example, `216.239.32.\d\d?` matches the following:

  * 216.239.32.2
  * 216.239.32.34



This example uses the [backslash](https://docs.cloud.google.com/data-studio/regex-example-dot-backslash) to escape the decimal, and it uses `\d` to match any digit.

## Plus sign (+)

The plus sign (+) matches the preceding character one or more times.

For example, `10+` matches the following:

  * 10
  * 100
  * 1000
  * etc.



### Example

Match an IP address with one or more digits in the last section.

For example, `216.239.32.\d+` matches the following:

  * 216.239.32.2
  * 216.239.32.34
  * 216.239.32.567



This example uses the [backslash](https://docs.cloud.google.com/data-studio/regex-example-dot-backslash) to escape the decimal, and it uses `\d` to match any digit.

## Asterisk (*)

The asterisk or star matches the preceding character zero or more times.

For example, `10*` matches the following:

  * 1
  * 10
  * 100
  * 1000
  * etc.



### Example

Match an IP address with zero or more digits in the last section.

For example, `216.239.32.\d*` matches the following:

  * 216.239.32.
  * 216.239.32.2
  * 216.239.32.34
  * 216.239.32.567



This example uses the [backslash](https://docs.cloud.google.com/data-studio/regex-example-dot-backslash) to escape the decimal, and it uses `\d` to match any digit.

If you need to match more than just the preceding item, you can combine the asterisk (`__`) with the[dot (`.`)](https://docs.cloud.google.com/data-studio/regex-example-dot-backslash). The dot matches any preceding item, and then the asterisk matches that item zero or more times, which lets you match things like all URIs that begin and end with the same characters, regardless of how many characters are in between. For example, `/mens/.*html` matches the following:

  * /mens/shirts/oxford.html
  * /mens/shirts/oxford/shortsleeve.html



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
