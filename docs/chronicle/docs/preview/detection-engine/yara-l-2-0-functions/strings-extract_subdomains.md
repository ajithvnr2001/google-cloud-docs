---
url: https://docs.cloud.google.com/chronicle/docs/preview/detection-engine/yara-l-2-0-functions/strings-extract_subdomains/
title: Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:58:54.596871+00:00
---

# Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/preview/detection-engine/yara-l-2-0-functions/strings-extract_subdomains/




Stay organized with collections  Save and categorize content based on your preferences. 

### strings.extract_subdomains

Supported in:

[ Rules ](https://docs.cloud.google.com/chronicle/docs/detection/default-rules) [ Search ](https://docs.cloud.google.com/chronicle/docs/investigation/udm-search)
    
    
    strings.extract_subdomains(url_string)
    

#### Description

Extracts all subdomains found in a URL string.

#### Param data types

`STRING`

#### Return type

`ARRAY_STRINGS`

#### Code samples

##### Example 1

This example shows how to extract the subdomains from a URL string.
    
    
    strings.extract_subdomains("www.sub1.sub2.google.com") = ["www", "sub1", "sub2"]
    

##### Example 2

This example shows how to extract subdomains when using non ASCII characters.
    
    
    strings.extract_subdomains("http://例子.卷筒纸.中国") = ["例子"]
    

##### Example 3

This example shows handling of a non URL string.
    
    
    strings.extract_subdomains("three nine four") = []
    

##### Example 4

This example shows handling of an unregistered domain.
    
    
    strings.extract_subdomains("http://localhost:80") = []
    

##### Example 5

This example shows handling of a multi part suffix.
    
    
    strings.extract_subdomains("    www.Example.Co.UK    ") = ["www"]
    

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
