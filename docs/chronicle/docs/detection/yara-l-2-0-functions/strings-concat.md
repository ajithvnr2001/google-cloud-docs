---
url: https://docs.cloud.google.com/chronicle/docs/detection/yara-l-2-0-functions/strings-concat/
title: Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:50:57.938096+00:00
---

# Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/detection/yara-l-2-0-functions/strings-concat/




Stay organized with collections  Save and categorize content based on your preferences. 

### strings.concat

Supported in:

[ Rules ](https://docs.cloud.google.com/chronicle/docs/detection/default-rules) [ Search ](https://docs.cloud.google.com/chronicle/docs/investigation/udm-search)
    
    
    strings.concat(a, b, c, ...)
    

#### Description

Returns the concatenation of an unlimited number of items, each of which can be a string, integer, or float.

If any arguments are event fields, the attributes must be from the same event.

#### Param data types

`STRING`, `FLOAT`, `INT`

#### Return type

`STRING`

#### Code samples

##### Example 1

The following example includes a string variable and integer variable as arguments. Both `principal.hostname` and `principal.port` are from the same event, `$e`, and are concatenated to return a string.
    
    
    "google:80" = strings.concat($e.principal.hostname, ":", $e.principal.port)
    

##### Example 2

The following example includes a string variable and string literal as arguments.
    
    
    "google-test" = strings.concat($e.principal.hostname, "-test") // Matches the event when $e.principal.hostname = "google"
    

##### Example 3

The following example includes a string variable and float literal as arguments. When represented as strings, floats that are whole numbers are formatted without the decimal point (for example, 1.0 is represented as "1"). Additionally, floats that exceed sixteen decimal digits are truncated to the sixteenth decimal place.
    
    
    "google2.5" = strings.concat($e.principal.hostname, 2.5)
    

##### Example 4

The following example includes a string variable, string literal, integer variable, and float literal as arguments. All variables are from the same event, `$e`, and are concatenated with the literals to return a string.
    
    
    "google-test802.5" = strings.concat($e.principal.hostname, "-test", $e.principal.port, 2.5)
    

##### Example 5

The following example attempts to concatenate principal.port from event `$e1`, with `principal.hostname` from event `$e2`. It will return a compiler error because the arguments are different event variables.
    
    
    // Will not compile
    "test" = strings.concat($e1.principal.port, $e2.principal.hostname)
    

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
