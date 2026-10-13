---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.InterconnectGroupConfiguredTopologyCapabilityIntendedCapabilityBlockers
title: Class InterconnectGroupConfiguredTopologyCapabilityIntendedCapabilityBlockers (0.12.7) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:40:42.971642+00:00
---

# Class InterconnectGroupConfiguredTopologyCapabilityIntendedCapabilityBlockers (0.12.7)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.InterconnectGroupConfiguredTopologyCapabilityIntendedCapabilityBlockers

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class InterconnectGroupConfiguredTopologyCapabilityIntendedCapabilityBlockers (0.12.7) Stay organized with collections  Save and categorize content based on your preferences. 

0.12.7 (latest)  0.12.6  0.11.0  0.4.0  0.3.0  0.2.0  0.1.8 
    
    
    InterconnectGroupConfiguredTopologyCapabilityIntendedCapabilityBlockers(
        mapping=None, *, ignore_unknown_fields=False, **kwargs
    )

[Output Only] Reasons why configuration.topologyCapability.sla differs from intent.topologyCapability. This list is empty if and only if those are the same.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

## Attributes  
  
---  
**Name** | **Description**  
`blocker_type` |  `str`   
Check the BlockerType enum for the list of possible values. This field is a member of `oneof`_ `_blocker_type`.   
`documentation_link` |  `str`   
Output only. [Output Only] The url of Google Cloud public documentation explaining this requirement. This is set for every type of requirement. This field is a member of `oneof`_ `_documentation_link`.   
`explanation` |  `str`   
Output only. [Output Only] A human-readable explanation of this requirement and why it's not met. This is set for every type of requirement. This field is a member of `oneof`_ `_explanation`.   
`facilities` |  `MutableSequence[str]`   
Output only. [Output Only] Facilities used to explain this blocker in more detail. Like physicalStructure.metros.facilities.facility, this is a numeric string like "5467".   
`interconnects` |  `MutableSequence[str]`   
Output only. [Output Only] Interconnects used to explain this blocker in more detail.   
`metros` |  `MutableSequence[str]`   
Output only. [Output Only] Metros used to explain this blocker in more detail. These are three-letter lowercase strings like "iad". A blocker like INCOMPATIBLE_METROS will specify the problematic metros in this field.   
`zones` |  `MutableSequence[str]`   
Output only. [Output Only] Zones used to explain this blocker in more detail. Zone names are "zone1" and/or "zone2".   
  
## Classes 

### BlockerType
    
    
    BlockerType(value)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
