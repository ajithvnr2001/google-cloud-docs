---
url: https://docs.cloud.google.com/chronicle/docs/detection/yara-l-2-0-functions/strings-starts_with/
title: Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T06:23:20.929908+00:00
---

# Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/detection/yara-l-2-0-functions/strings-starts_with/




Stay organized with collections  Save and categorize content based on your preferences. 

### strings.starts_with

Supported in:

[ Rules ](https://docs.cloud.google.com/chronicle/docs/detection/default-rules) [ Search ](https://docs.cloud.google.com/chronicle/docs/investigation/udm-search)
    
    
    strings.starts_with(value, suffix)
    

#### Description

Function takes two strings `(value, suffix)`. Returns true if the suffix is non-empty and at start-of-value.

#### Param data types

`STRING`, `STRING`

#### Return type

`BOOL`

#### Code samples

The following code samples illustrate some of the ways you might use the `strings.starts_with` function.

##### Example: returns true

Returns true when the prefix is found at start-of-value.
    
    
    strings.starts_with(target.hostname, "www") = true
    

##### Example: returns false

Returns false when the prefix isn't at start-of-value.
    
    
    strings.starts_with(target.hostname, "www") = false
    

##### Example: returns true when identical

Returns true when prefix and value are identical.
    
    
    target.hostname != "example.com"
    strings.starts_with("str", "str") = true
    

##### Example: returns false when suffix empty

Returns false when prefix is an empty string.
    
    
    target.hostname != "example.com"
    strings.starts_with("", "str") = false
    

##### Example: returns false when value empty

Returns false when value is an empty string.
    
    
    target.hostname != "example.com"
    strings.starts_with("str", "") = false
    

##### Example: returns false when prefix and value are empty

Returns false when prefix and value are empty strings.
    
    
    target.hostname != "example.com"
    strings.starts_with("", "") = false
    

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
