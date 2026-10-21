---
url: https://docs.cloud.google.com/chronicle/docs/detection/yara-l-2-0-functions/strings-extract_domain/
title: Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T20:14:07.814894+00:00
---

# Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/detection/yara-l-2-0-functions/strings-extract_domain/




Stay organized with collections  Save and categorize content based on your preferences. 

### strings.extract_domain

Supported in:

[ Rules ](https://docs.cloud.google.com/chronicle/docs/detection/default-rules) [ Search ](https://docs.cloud.google.com/chronicle/docs/investigation/udm-search)
    
    
    strings.extract_domain(url_string)
    

#### Description

Extracts the domain from a string.

**Note:** The function does not perform Unicode normalization.**Note:** The public suffix data at publicsuffix.org also contains private domains. This function does not treat a private domain as a public suffix. For example, if us.com is a private domain in the public suffix data, ("foo.us.com") returns us.com (the public suffix com plus the preceding label us) rather than foo.us.com (the private domain us.com plus the preceding label foo).**Note:** The public suffix data might change over time. Consequently, input that produces default empty value now may produce a non-empty value in the future.

#### Param data types

`STRING`

#### Return type

`STRING`

#### Code samples

##### Example 1

This example shows an empty string
    
    
    strings.extract_domain("") = ""
    

##### Example 2

random string, not a URL
    
    
    strings.extract_domain("1234") = ""
    

##### Example 3

multiple backslaches
    
    
    strings.extract_domain("\\\\") = ""
    

##### Example 4

non-alphabet characters handled gracefully
    
    
    strings.extract_domain("http://例子.卷筒纸.中国") = "卷筒纸.中国"
    

##### Example 5

handling URIs
    
    
    strings.extract_domain("mailto:?to=&subject=&body=") = ""
    

##### Example 6

multiple characters before actual URL
    
    
    strings.extract_domain("     \t   !$5*^)&dahgsdfs;http://www.google.com") = "google.com"
    

##### Example 7

special characters in URI `#`
    
    
    strings.extract_domain("test#@google.com") = ""
    

##### Example 8

special characters in URL `#`
    
    
    strings.extract_domain("https://test#@google.com") = ""
    

##### Example 9

positive test case
    
    
    strings.extract_domain("https://google.co.in") = "google.co.in"
    

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
