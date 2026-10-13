---
url: https://docs.cloud.google.com/python/docs/reference/networkservices/latest/google.cloud.network_services_v1beta1.types.ExtensionBinding.MatchCondition.To
title: Class To (0.10.4) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:18:58.833539+00:00
---

# Class To (0.10.4)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/networkservices/latest/google.cloud.network_services_v1beta1.types.ExtensionBinding.MatchCondition.To

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class To (0.10.4) Stay organized with collections  Save and categorize content based on your preferences. 

0.10.4 (latest)  0.10.3  0.9.0  0.8.0  0.7.0  0.6.0  0.5.24  0.4.1  0.3.0  0.2.2  0.1.1 
    
    
    To(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Describes properties of one or more destinations of a request.

## Attributes  
  
---  
**Name** | **Description**  
`destination` |  `[google.cloud.network_services_v1beta1.types.ExtensionBinding.MatchCondition.To.Destination](https://docs.cloud.google.com/python/docs/reference/networkservices/latest/google.cloud.network_services_v1beta1.types.ExtensionBinding.MatchCondition.To.Destination)`   
Optional. Describes properties of destination of a request. Within a destination, the match follows AND semantics across fields and OR semantics within a field, i.e. a match occurs when ANY path matches AND ANY header matches and ANY method matches. At least one of destination or not_destination must be specified.   
`not_destination` |  `[google.cloud.network_services_v1beta1.types.ExtensionBinding.MatchCondition.To.Destination](https://docs.cloud.google.com/python/docs/reference/networkservices/latest/google.cloud.network_services_v1beta1.types.ExtensionBinding.MatchCondition.To.Destination)`   
Optional. Describes the negated properties of the request destination. Extension will not be invoked on requests that match the criteria specified in this field. At least one of destination or not_destination must be specified.   
  
## Classes 

### Destination
    
    
    Destination(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Describes properties of a single destination.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
