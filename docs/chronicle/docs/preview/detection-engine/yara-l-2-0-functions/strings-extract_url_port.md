---
url: https://docs.cloud.google.com/chronicle/docs/preview/detection-engine/yara-l-2-0-functions/strings-extract_url_port/
title: Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:47:55.244545+00:00
---

# Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/preview/detection-engine/yara-l-2-0-functions/strings-extract_url_port/




Stay organized with collections  Save and categorize content based on your preferences. 

### strings.extract_url_port

Supported in:

[ Rules ](https://docs.cloud.google.com/chronicle/docs/detection/default-rules) [ Search ](https://docs.cloud.google.com/chronicle/docs/investigation/udm-search)
    
    
    strings.extract_url_port(url_string)
    

#### Description

Extracts the port (explicit or inferred) from a URL string. If the port is set in the URL, return it. Otherwise, return one of the default ports or -1 if a port cannot be found or inferred from the URL.

#### Param data types

`STRING`

#### Return type

`INT`

#### Code samples

##### Example 1

This example returns -1 when you enter an empty string.
    
    
    strings.extract_url_port("") = -1
    

##### Example 2

This example returns the port when the string includes a port.
    
    
    strings.extract_url_port("ftp://example.com:221/svn/Repos/") = 221
    

##### Example 3

This example returns the default port when the string doesn't include a port.
    
    
    strings.extract_url_port("ftp://example.com/svn/Repos/") = 21
    

##### Example 4

This example returns the default HTTP port when the string is a URL.
    
    
    strings.extract_url_port("http://example.com/svn/Repos/") = 80
    

##### Example 5

This example returns the default HTTP port when the string doesn't include a port.
    
    
    strings.extract_url_port("https://example.com/svn/Repos/") = 443
    

##### Example 6

This example returns the default web server port when the URL doesn't include the port.
    
    
    strings.extract_url_port("ws://example.com/svn/Repos/") = 80
    

##### Example 7

This example returns the default WSS port when the URL doesn't include the port.
    
    
    strings.extract_url_port("wss://example.com/svn/Repos/") = 443
    

##### Example 8

This example returns -1 when the string isn't a network connection.
    
    
    strings.extract_url_port("file:///ada/Analytical%20Engine/README.md") = -1
    

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
