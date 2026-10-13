---
url: https://docs.cloud.google.com/python/docs/reference/networksecurity/latest/google.cloud.network_security_v1alpha1.types.PartnerSSERealm
title: Class PartnerSSERealm (0.13.4) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:42:49.403077+00:00
---

# Class PartnerSSERealm (0.13.4)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/networksecurity/latest/google.cloud.network_security_v1alpha1.types.PartnerSSERealm

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class PartnerSSERealm (0.13.4) Stay organized with collections  Save and categorize content based on your preferences. 

0.13.4 (latest)  0.13.3  0.12.0  0.11.0  0.10.0  0.9.21  0.8.0  0.7.2  0.6.1  0.5.0  0.4.2  0.3.2  0.2.0  0.1.5 
    
    
    PartnerSSERealm(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Message describing PartnerSSERealm object

## Attributes  
  
---  
**Name** | **Description**  
`name` |  `str`   
name of resource   
`create_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. Create time stamp   
`update_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. Update time stamp   
`labels` |  `MutableMapping[str, str]`   
Labels as key value pairs   
`pairing_key` |  `str`   
Required. value of the key to establish global handshake from SSERealm   
`partner_vpc` |  `str`   
Optional. VPC owned by the partner to be peered with CDEN sse_vpc in sse_project This field is deprecated. Use partner_network instead.   
`sse_vpc` |  `str`   
Output only. CDEN owned VPC to be peered with partner_vpc This field is deprecated. Use sse_network instead.   
`sse_project` |  `str`   
Output only. CDEN owned project owning sse_vpc. It stores project id in the TTM flow, but project number in the NCCGW flow. This field will be deprecated after the partner migrates from using sse_project to using sse_project_number.   
`state` |  `[google.cloud.network_security_v1alpha1.types.PartnerSSERealm.State](https://docs.cloud.google.com/python/docs/reference/networksecurity/latest/google.cloud.network_security_v1alpha1.types.PartnerSSERealm.State)`   
Output only. State of the realm. It can be either CUSTOMER_ATTACHED or CUSTOMER_DETACHED.   
`partner_network` |  `str`   
Optional. Partner-owned network to be peered with CDEN's sse_network in sse_project   
`sse_network` |  `str`   
Output only. CDEN-owned network to be peered with partner_network   
`pan_options` |  `[google.cloud.network_security_v1alpha1.types.PartnerSSERealm.PartnerSSERealmPanOptions](https://docs.cloud.google.com/python/docs/reference/networksecurity/latest/google.cloud.network_security_v1alpha1.types.PartnerSSERealm.PartnerSSERealmPanOptions)`   
Optional. Required only for PAN.   
`sse_project_number` |  `int`   
Output only. CDEN owned project owning sse_vpc   
  
## Classes 

### LabelsEntry
    
    
    LabelsEntry(mapping=None, *, ignore_unknown_fields=False, **kwargs)

The abstract base class for a message.

**Parameters**  
---  
**Name** | **Description**  
`kwargs` |  `dict`   
Keys and values corresponding to the fields of the message.  
`mapping` |  `Union[dict, `.Message`]`   
A dictionary or message to be used to determine the values for this message.  
`ignore_unknown_fields` |  `Optional(bool)`   
If True, do not raise errors for unknown fields. Only applied if `mapping` is a mapping type or there are keyword parameters.  
  
### PartnerSSERealmPanOptions
    
    
    PartnerSSERealmPanOptions(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Fields specific to PAN realms.

### State
    
    
    State(value)

State of the realm

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
