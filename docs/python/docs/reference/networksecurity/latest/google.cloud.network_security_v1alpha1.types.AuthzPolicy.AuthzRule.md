---
url: https://docs.cloud.google.com/python/docs/reference/networksecurity/latest/google.cloud.network_security_v1alpha1.types.AuthzPolicy.AuthzRule
title: Class AuthzRule (0.13.4) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:58:52.791513+00:00
---

# Class AuthzRule (0.13.4)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/networksecurity/latest/google.cloud.network_security_v1alpha1.types.AuthzPolicy.AuthzRule

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class AuthzRule (0.13.4) Stay organized with collections  Save and categorize content based on your preferences. 

0.13.4 (latest)  0.13.3  0.12.0  0.11.0  0.10.0  0.9.21  0.8.0  0.7.2  0.6.1  0.5.0  0.4.2  0.3.2  0.2.0  0.1.5 
    
    
    AuthzRule(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Conditions to match against the incoming request.

## Attributes  
  
---  
**Name** | **Description**  
`from_` |  `[google.cloud.network_security_v1alpha1.types.AuthzPolicy.AuthzRule.From](https://docs.cloud.google.com/python/docs/reference/networksecurity/latest/google.cloud.network_security_v1alpha1.types.AuthzPolicy.AuthzRule.From)`   
Optional. Describes properties of a source of a request.   
`to` |  `[google.cloud.network_security_v1alpha1.types.AuthzPolicy.AuthzRule.To](https://docs.cloud.google.com/python/docs/reference/networksecurity/latest/google.cloud.network_security_v1alpha1.types.AuthzPolicy.AuthzRule.To)`   
Optional. Describes properties of a target of a request.   
`when` |  `str`   
Optional. CEL expression that describes the conditions to be satisfied for the action. The result of the CEL expression is ANDed with the from and to. Refer to the CEL language reference for a list of available attributes.   
  
## Classes 

### From
    
    
    From(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Describes properties of one or more sources of a request.

### HeaderMatch
    
    
    HeaderMatch(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Determines how a HTTP header should be matched.

### IpBlock
    
    
    IpBlock(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Represents a range of IP Addresses.

### Principal
    
    
    Principal(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Describes the properties of a principal to be matched against.

### RequestResource
    
    
    RequestResource(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Describes the properties of a client VM resource accessing the internal application load balancers.

### StringMatch
    
    
    StringMatch(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Determines how a string value should be matched.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### To
    
    
    To(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Describes properties of one or more targets of a request.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
