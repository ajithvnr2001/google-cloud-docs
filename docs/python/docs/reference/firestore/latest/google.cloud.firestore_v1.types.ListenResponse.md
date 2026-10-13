---
url: https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.types.ListenResponse
title: Class ListenResponse (2.34.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:07:47.914863+00:00
---

# Class ListenResponse (2.34.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.types.ListenResponse

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class ListenResponse (2.34.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.34.0 (latest)  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.1  2.27.0  2.26.0  2.23.0  2.22.0  2.21.0  2.20.2  2.19.0  2.18.0  2.17.2  2.16.1  2.15.0  2.14.0  2.13.1  2.12.0  2.11.1  2.10.1  2.9.1  2.8.0  2.7.3  2.6.1  2.5.3  2.4.0  2.3.4  2.2.0  2.1.3  2.0.2  1.9.2  1.8.1  1.7.0  1.6.2  1.5.0  1.4.0  1.3.0 
    
    
    ListenResponse(mapping=None, *, ignore_unknown_fields=False, **kwargs)

The response for `Firestore.Listen][google.firestore.v1.Firestore.Listen]`.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

## Attributes  
  
---  
**Name** | **Description**  
`target_change` |  `[google.cloud.firestore_v1.types.TargetChange](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.types.TargetChange)`   
Targets have changed. This field is a member of `oneof`_ `response_type`.   
`document_change` |  `[google.cloud.firestore_v1.types.DocumentChange](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.types.DocumentChange)`   
A `Document][google.firestore.v1.Document]` has changed. This field is a member of `oneof`_ `response_type`.   
`document_delete` |  `[google.cloud.firestore_v1.types.DocumentDelete](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.types.DocumentDelete)`   
A `Document][google.firestore.v1.Document]` has been deleted. This field is a member of `oneof`_ `response_type`.   
`document_remove` |  `[google.cloud.firestore_v1.types.DocumentRemove](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.types.DocumentRemove)`   
A `Document][google.firestore.v1.Document]` has been removed from a target (because it is no longer relevant to that target). This field is a member of `oneof`_ `response_type`.   
`filter` |  `[google.cloud.firestore_v1.types.ExistenceFilter](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.types.ExistenceFilter)`   
A filter to apply to the set of documents previously returned for the given target. Returned when documents may have been removed from the given target, but the exact documents are unknown. This field is a member of `oneof`_ `response_type`.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
