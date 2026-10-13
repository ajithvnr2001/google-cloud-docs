---
url: https://docs.cloud.google.com/python/docs/reference/cloudtrace/latest/google.cloud.trace_v2.types.Span.Links
title: Class Links (1.21.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:16:25.817608+00:00
---

# Class Links (1.21.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/cloudtrace/latest/google.cloud.trace_v2.types.Span.Links

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class Links (1.21.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.21.0 (latest)  1.20.0  1.19.0  1.18.0  1.17.0  1.16.2  1.15.0  1.14.1  1.13.5  1.12.0  1.11.3  1.10.0  1.9.1  1.8.0  1.7.3  1.6.2  1.5.1  1.4.0  1.3.4  1.2.0  1.1.0  1.0.0  0.24.2  0.23.0  0.22.1 
    
    
    Links(mapping=None, *, ignore_unknown_fields=False, **kwargs)

A collection of links, which are references from this span to a span in the same or different trace.

## Attributes  
  
---  
**Name** | **Description**  
`link` |  `MutableSequence[google.cloud.trace_v2.types.Span.Link]`   
A collection of links.   
`dropped_links_count` |  `int`   
The number of dropped links after the maximum size was enforced. If this value is 0, then no links were dropped.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-04 UTC."],[],[]] 
