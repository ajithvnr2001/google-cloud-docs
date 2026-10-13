---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.SdpFilterResult
title: Class SdpFilterResult (0.7.2) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:19:03.191310+00:00
---

# Class SdpFilterResult (0.7.2)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.SdpFilterResult

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class SdpFilterResult (0.7.2) Stay organized with collections  Save and categorize content based on your preferences. 

0.7.2 (latest)  0.7.1  0.6.0  0.5.0  0.4.0  0.3.0  0.2.8  0.1.1 
    
    
    SdpFilterResult(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Sensitive Data Protection filter result.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

## Attributes  
  
---  
**Name** | **Description**  
`inspect_result` |  `[google.cloud.modelarmor_v1.types.SdpInspectResult](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.SdpInspectResult)`   
Sensitive Data Protection Inspection result if inspection is performed. This field is a member of `oneof`_ `result`.   
`deidentify_result` |  `[google.cloud.modelarmor_v1.types.SdpDeidentifyResult](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.SdpDeidentifyResult)`   
Sensitive Data Protection Deidentification result if deidentification is performed. This field is a member of `oneof`_ `result`.   
`redact_result` |  `[google.cloud.modelarmor_v1.types.SdpRedactResult](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.SdpRedactResult)`   
Sensitive Data Protection Redaction result if redaction is performed. This is primarily used for image redaction. This field is a member of `oneof`_ `result`.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
