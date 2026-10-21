---
url: https://docs.cloud.google.com/chronicle/docs/preview/detection-engine/yara-l-2-0-functions/strings-extract_url_path/
title: Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T01:20:17.611046+00:00
---

# Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/preview/detection-engine/yara-l-2-0-functions/strings-extract_url_path/




Stay organized with collections  Save and categorize content based on your preferences. 

### strings.extract_url_path

Supported in:

[ Rules ](https://docs.cloud.google.com/chronicle/docs/detection/default-rules) [ Search ](https://docs.cloud.google.com/chronicle/docs/investigation/udm-search)
    
    
    strings.extract_url_path(url_string)
    

#### Description

Extracts the path behind the domain in a URL but before the parameters.

#### Param data types

`STRING`

#### Return type

`STRING`

#### Code samples

##### Example 1

This example shows that nothing is returned when you enter an empty string.
    
    
    strings.extract_url_path("") = ""
    

##### Example 2

This example shows the path that is returned when you provide a valid URL.
    
    
    strings.extract_url_path("https://developer.test_company.org/en-US/docs/Web/API/URL/pathname?q=value") = "/en-US/docs/Web/API/URL/pathname"
    

##### Example 3

This example shows that nothing is returned when you provide a random string that isn't a URL.
    
    
    strings.extract_url_path("1234") = ""
    

##### Example 4

This example shows support for non ASCII characters in a URL.
    
    
    strings.extract_url_path("http://例子/卷筒纸/中国") = "/卷筒纸/中国"
    

##### Example 5

This example shows that an empty string is returned when a URI is provided.
    
    
    strings.extract_url_path("mailto:?to=&subject=&body=") = ""
    

##### Example 6

This example shows the path that is returned when you provide multiple characters before a URL.
    
    
    strings.extract_url_path("     \t   !$5*^)&dahgsdfs;http://www.google.com/foo/bar") = "/foo/bar"
    

##### Example 7

This example shows that an empty string is returned when you provide special characters (for example, `#`) in a URL.
    
    
    strings.extract_url_path("test#@google.com") = ""
    

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
