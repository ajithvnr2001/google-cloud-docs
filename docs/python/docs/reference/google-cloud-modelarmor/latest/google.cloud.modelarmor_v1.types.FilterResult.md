---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.FilterResult
title: Class FilterResult (0.7.2) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:18:56.172190+00:00
---

# Class FilterResult (0.7.2)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.FilterResult

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class FilterResult (0.7.2) Stay organized with collections  Save and categorize content based on your preferences. 

0.7.2 (latest)  0.7.1  0.6.0  0.5.0  0.4.0  0.3.0  0.2.8  0.1.1 
    
    
    FilterResult(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Filter Result obtained after Sanitization operations.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

## Attributes  
  
---  
**Name** | **Description**  
`rai_filter_result` |  `[google.cloud.modelarmor_v1.types.RaiFilterResult](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.RaiFilterResult)`   
Responsible AI filter results. This field is a member of `oneof`_ `filter_result`.   
`sdp_filter_result` |  `[google.cloud.modelarmor_v1.types.SdpFilterResult](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.SdpFilterResult)`   
Sensitive Data Protection results. This field is a member of `oneof`_ `filter_result`.   
`pi_and_jailbreak_filter_result` |  `[google.cloud.modelarmor_v1.types.PiAndJailbreakFilterResult](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.PiAndJailbreakFilterResult)`   
Prompt injection and Jailbreak filter results. This field is a member of `oneof`_ `filter_result`.   
`malicious_uri_filter_result` |  `[google.cloud.modelarmor_v1.types.MaliciousUriFilterResult](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.MaliciousUriFilterResult)`   
Malicious URI filter results. This field is a member of `oneof`_ `filter_result`.   
`csam_filter_filter_result` |  `[google.cloud.modelarmor_v1.types.CsamFilterResult](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.CsamFilterResult)`   
CSAM filter results. This field is a member of `oneof`_ `filter_result`.   
`virus_scan_filter_result` |  `[google.cloud.modelarmor_v1.types.VirusScanFilterResult](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.VirusScanFilterResult)`   
Virus scan results. This field is a member of `oneof`_ `filter_result`.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
