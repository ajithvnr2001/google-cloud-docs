---
url: https://docs.cloud.google.com/chronicle/docs/detection/yara-l-2-0-functions/re-regex/
title: Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:11:28.733428+00:00
---

# Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/detection/yara-l-2-0-functions/re-regex/




Stay organized with collections  Save and categorize content based on your preferences. 

### re.regex

Supported in:

[ Rules ](https://docs.cloud.google.com/chronicle/docs/detection/default-rules) [ Search ](https://docs.cloud.google.com/chronicle/docs/investigation/udm-search)

You can define regular expression matching in YARA-L 2.0 using either of the following syntax:

  * Using YARA-L syntax — Related to events. The following is a generic representation of this syntax:
        
        $e.field = /regex/
        

  * Using YARA-L syntax — As a function taking in the following parameters:

    * Field the regular expression is applied to.
    * Regular expression specified as a string.

The following is a generic representation of this syntax:
    
    re.regex($e.field, `regex`)
    




#### Description

This function returns `true` if the string contains a substring that matches the regular expression provided. It is unnecessary to add `.*` to the beginning or at the end of the regular expression.

The `re.regex` function uses the RE2 regular expression engine.

**Note:** For predictable performance, the RE2 engine intentionally omits certain advanced features, such as lookahead and lookbehind assertions. For more information, see [RE2 syntax](https://github.com/google/re2/wiki/Syntax).

##### Notes

  * To match the exact string or only a prefix or suffix, include the `^` (starting) and `$` (ending) anchor characters in the regular expression. For example, `/^full$/` matches `"full"` exactly, while `/full/` could match `"fullest"`, `"lawfull"`, and `"joyfully"`.
  * If the UDM field includes newline characters, the `regexp` only matches the first line of the UDM field. To enforce full UDM field matching, add a `(?s)` to the regular expression. For example, replace `/.*allUDM.*/` with `/(?s).*allUDM.*/`.
  * You can use the `nocase` modifier after strings to indicate that the search should ignore capitalization.



#### Param data types

`STRING`, `STRING`

#### Param expression types

`ANY`, `ANY`

#### Return type

`BOOL`

#### Code samples

##### Example 1
    
    
    // Equivalent to $e.principal.hostname = /google/
    re.regex($e.principal.hostname, "google")
    

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
