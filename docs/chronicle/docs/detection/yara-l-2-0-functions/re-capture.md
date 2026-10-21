---
url: https://docs.cloud.google.com/chronicle/docs/detection/yara-l-2-0-functions/re-capture/
title: Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T12:00:48.959062+00:00
---

# Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/detection/yara-l-2-0-functions/re-capture/




Stay organized with collections  Save and categorize content based on your preferences. 

### re.capture

Supported in:

[ Rules ](https://docs.cloud.google.com/chronicle/docs/detection/default-rules) [ Search ](https://docs.cloud.google.com/chronicle/docs/investigation/udm-search)
    
    
    re.capture(stringText, regex)
    

#### Description

Captures (extracts) data from a string using the regular expression pattern provided in the argument.

This function takes two arguments:

  * `stringText`: the original string to search.
  * `regex`: the regular expression indicating the pattern to search for.



The regular expression can contain 0 or 1 capture groups in parentheses. If the regular expression contains 0 capture groups, the function returns the first entire matching substring. If the regular expression contains 1 capture group, it returns the first matching substring for the capture group. Defining two or more capture groups returns a compiler error.

#### Param data types

`STRING`, `STRING`

#### Return type

`STRING`

#### Code samples

##### Example 1

In this example, if `$e.principal.hostname` contains "aaa1bbaa2" the following would be true, because the function returns the first instance. This example has no capture groups.
    
    
    "aaa1" = re.capture($e.principal.hostname, "a+[1-9]")
    

##### Example 2

This example captures everything after the @ symbol in an email. If the `$e.network.email.from` field is `test@google.com`, the example returns `google.com`. The following example contains one capture group.
    
    
    "google.com" = re.capture($e.network.email.from , "@(.*)")
    

##### Example 3

If the regular expression does not match any substring in the text, the function returns an empty string. You can omit events where no match occurs by excluding the empty string, which is especially important when you are using `re.capture()` with an inequality:
    
    
    // Exclude the empty string to omit events where no match occurs.
    "" != re.capture($e.network.email.from , "@(.*)")
    
    // Exclude a specific string with an inequality.
    "google.com" != re.capture($e.network.email.from , "@(.*)")
    

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
