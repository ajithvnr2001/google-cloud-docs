---
url: https://docs.cloud.google.com/data-studio/regex-example-dot-backslash/
title: Handling special characters: dot (.) and backslash () \u00a0|\u00a0 Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:20:13.890609+00:00
---

# Handling special characters: dot (.) and backslash ()  |  Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/regex-example-dot-backslash/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)



Send feedback 

#  Handling special characters: dot (.) and backslash () Stay organized with collections  Save and categorize content based on your preferences. 

When you use regular expressions in Data Studio for filtering or transformations, some characters, like the dot (.) or backslash (), have special meanings. Learn how to use the dot (.) to match any character and the backslash () to escape special characters in Data Studio regular expressions.

By default, the dot character (.) matches any single character. This can lead to unexpected results if you aim to match a literal dot. For example, a regular expression that attempts to match an IP address, like `0.0.0.0`, would incorrectly match `0102030` or `0a0b0c0` instead of the exact IP address.

To achieve precise pattern matching in your reports, you must "escape" these special characters. Escaping ensures that the regular expression engine interprets them as their literal selves, ensuring accurate data analysis in your Data Studio reports.

To match a literal dot in a regular expression, such as in an IP address, you must provide a signal instead of letting it match any character. The backslash () is that signal. When a regular expression encounters a backslash, it interprets the next character literally.

In the previous example, we would use the regular expression `0\.0\.0\.0` to indicate that the dots themselves should be matched.

You can also use the backslash to escape any special character and interpret it literally.

The following examples are common use cases for the backslash character in regular expressions:

  * `\\` (escapes the backslash)
  * `\[` (escapes the bracket)
  * `\{` (escapes the curly brace)
  * `\.` (escapes the dot)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
