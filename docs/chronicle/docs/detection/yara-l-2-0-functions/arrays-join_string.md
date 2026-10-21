---
url: https://docs.cloud.google.com/chronicle/docs/detection/yara-l-2-0-functions/arrays-join_string/
title: Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:43:23.872491+00:00
---

# Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/detection/yara-l-2-0-functions/arrays-join_string/




Stay organized with collections  Save and categorize content based on your preferences. 

### arrays.join_string

Supported in:

[ Rules ](https://docs.cloud.google.com/chronicle/docs/detection/default-rules) [ Search ](https://docs.cloud.google.com/chronicle/docs/investigation/udm-search)
    
    
    arrays.join_string(array_of_strings, optional_delimiter)
    

#### Description

Converts an array of strings into a single string separated by the optional parameter. If no delimiter is provided, the empty string is used.

#### Param data types

`ARRAY_STRINGS`, `STRING`

#### Return type

`STRING`

#### Code samples

Here are some examples of how to use the function:

##### Example 1

This example joins an array with non-null elements and a delimiter.
    
    
    arrays.join_string(["foo", "bar"], ",") = "foo,bar"
    

##### Example 2

This example joins an array with a null element and a delimiter.
    
    
    arrays.join_string(["foo", NULL, "bar"], ",") = "foo,bar"
    

##### Example 3

This example joins an array with non-null elements and no delimiter.
    
    
    arrays.join_string(["foo", "bar"]) = "foobar"
    

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
