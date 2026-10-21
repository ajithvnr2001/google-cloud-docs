---
url: https://docs.cloud.google.com/chronicle/docs/preview/detection-engine/yara-l-2-0-functions/strings-extract_url_params/
title: Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T04:56:34.220417+00:00
---

# Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/preview/detection-engine/yara-l-2-0-functions/strings-extract_url_params/




Stay organized with collections  Save and categorize content based on your preferences. 

### strings.extract_url_params

Supported in:

[ Rules ](https://docs.cloud.google.com/chronicle/docs/detection/default-rules) [ Search ](https://docs.cloud.google.com/chronicle/docs/investigation/udm-search)
    
    
    strings.extract_url_params(url_string)
    

#### Description

Extracts the URL query parameters from a URL string and adds it to an array.

#### Param data types

`STRING`

#### Return type

`ARRAY_STRINGS`

#### Code samples

##### Example 1

The following example extracts the query parameter (`name`) from the URL.
    
    
    strings.extract_url_params("https://example.com/?name=Johnathan%20Smith") // yields this array of strings ["name:Johnathan Smith"]
    

##### Example 2

The following example yields an empty array as there are no query parameters in the URL.
    
    
    strings.extract_url_params("https://example.com/") // yields an empty array []
    

##### Example 3

The following example extracts the query parameter (`foo`) from the URL.
    
    
    strings.extract_url_params("     \t   !$5*^)&dahgsdfs;http://www.google.com/?foo=bar") // yields this array of strings ["foo:bar"]
    

##### Example 4

This example shows handling of URIs.
    
    
    strings.extract_url_params("mailto:?to=&subject=&body=") // yields an empty array []
    

##### Example 5

This example shows handling of non-ASCII characters.
    
    
    strings.extract_url_params("http://例子/?卷筒纸=中国") // yields this array of strings ["卷筒纸:中国"]
    

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
