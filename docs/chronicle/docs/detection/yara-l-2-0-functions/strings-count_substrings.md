---
url: https://docs.cloud.google.com/chronicle/docs/detection/yara-l-2-0-functions/strings-count_substrings/
title: Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T11:30:48.558149+00:00
---

# Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/detection/yara-l-2-0-functions/strings-count_substrings/




Stay organized with collections  Save and categorize content based on your preferences. 

### strings.count_substrings

Supported in:

[ Rules ](https://docs.cloud.google.com/chronicle/docs/detection/default-rules) [ Search ](https://docs.cloud.google.com/chronicle/docs/investigation/udm-search)
    
    
    strings.count_substrings(string_to_search_in, substring_to_count)
    

#### Description

When given a string and a substring, returns an int64 of the count of non-overlapping occurrences of the substring within the string.

#### Param data types

`STRING`, `STRING`

#### Return type

`INT`

#### Code samples

This section contains examples that calculate the number of times a substring appears in a given string.

##### Example 1

This example uses a non-null string and a non-null single substring character.
    
    
    strings.count_substrings("this`string`has`four`backticks", "`") = 4
    

##### Example 2

This example uses a non-null string and a non-null substring greater than one character.
    
    
    strings.count_substrings("str", "str") = 1
    

##### Example 3

This example uses a non-null string and an empty substring.
    
    
    strings.count_substrings("str", "") = 0
    

##### Example 4

This example uses an empty string and a non-null substring greater than one character.
    
    
    strings.count_substrings("", "str") = 0
    

##### Example 5

This example uses an empty string and an empty substring.
    
    
    strings.count_substrings("", "") = 0
    

##### Example 6

This example uses a non-null string and a non-null substring that is greater than one character and greater than one occurrence.
    
    
    strings.count_substrings("fooABAbarABAbazABA", "AB") = 3
    

##### Example 7

This example uses a non-null string and a non-null substring that is greater than one character and greater than one occurrence. It highlights the limitation with overlapping substring occurrences
    
    
    strings.count_substrings("ABABABA", "ABA") = 2
    

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
