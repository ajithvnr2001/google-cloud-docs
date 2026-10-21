---
url: https://docs.cloud.google.com/chronicle/docs/preview/detection-engine/yara-l-2-0-functions/strings-count_subdomains/
title: Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T13:44:36.337943+00:00
---

# Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/preview/detection-engine/yara-l-2-0-functions/strings-count_subdomains/




Stay organized with collections  Save and categorize content based on your preferences. 

### strings.count_subdomains

Supported in:

[ Rules ](https://docs.cloud.google.com/chronicle/docs/detection/default-rules) [ Search ](https://docs.cloud.google.com/chronicle/docs/investigation/udm-search)
    
    
    strings.count_subdomains(url_string)
    

#### Description

Returns the count of all the subdomains that are found in a URL string.

#### Param data types

`STRING`

#### Return type

`INT`

#### Code samples

##### Example 1

This example shows the count of subdomains in a URL string.
    
    
    strings.count_subdomains("www.sub1.sub2.google.com") = 3
    

##### Example 2

This example shows the count of subdomains in a non ASCII URL string.
    
    
    strings.count_subdomains("http://例子.卷筒纸.中国") = 1
    

##### Example 3

This example shows the handling in case the URL is not valid.
    
    
    strings.count_subdomains("three nine four") = 0
    

##### Example 4

This example shows the handling in case the URL is not a registered domain.
    
    
    strings.count_subdomains("http://localhost:80") = 0
    

##### Example 5

This example shows the handling in case the URL has multipart suffix.
    
    
    strings.count_subdomains("    www.Example.Co.UK    ") = 1
    

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
