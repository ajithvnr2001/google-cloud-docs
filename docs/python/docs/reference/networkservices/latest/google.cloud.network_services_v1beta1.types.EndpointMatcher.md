---
url: https://docs.cloud.google.com/python/docs/reference/networkservices/latest/google.cloud.network_services_v1beta1.types.EndpointMatcher
title: Class EndpointMatcher (0.10.4) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:42:24.924137+00:00
---

# Class EndpointMatcher (0.10.4)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/networkservices/latest/google.cloud.network_services_v1beta1.types.EndpointMatcher

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class EndpointMatcher (0.10.4) Stay organized with collections  Save and categorize content based on your preferences. 

0.10.4 (latest)  0.10.3  0.9.0  0.8.0  0.7.0  0.6.0  0.5.24  0.4.1  0.3.0  0.2.2  0.1.1 
    
    
    EndpointMatcher(mapping=None, *, ignore_unknown_fields=False, **kwargs)

A definition of a matcher that selects endpoints to which the policies should be applied.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

## Attribute  
  
---  
**Name** | **Description**  
`metadata_label_matcher` |  `[google.cloud.network_services_v1beta1.types.EndpointMatcher.MetadataLabelMatcher](https://docs.cloud.google.com/python/docs/reference/networkservices/latest/google.cloud.network_services_v1beta1.types.EndpointMatcher.MetadataLabelMatcher)`   
The matcher is based on node metadata presented by xDS clients. This field is a member of `oneof`_ `matcher_type`.   
  
## Classes 

### MetadataLabelMatcher
    
    
    MetadataLabelMatcher(mapping=None, *, ignore_unknown_fields=False, **kwargs)

The matcher that is based on node metadata presented by xDS clients.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
