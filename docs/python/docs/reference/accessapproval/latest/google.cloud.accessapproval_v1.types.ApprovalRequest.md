---
url: https://docs.cloud.google.com/python/docs/reference/accessapproval/latest/google.cloud.accessapproval_v1.types.ApprovalRequest
title: Class ApprovalRequest (1.21.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:09:21.661479+00:00
---

# Class ApprovalRequest (1.21.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/accessapproval/latest/google.cloud.accessapproval_v1.types.ApprovalRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class ApprovalRequest (1.21.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.21.0 (latest)  1.20.0  1.19.0  1.18.0  1.17.0  1.16.2  1.15.0  1.14.1  1.13.5  1.12.0  1.11.3  1.10.1  1.9.1  1.8.0  1.7.5  1.6.1  1.5.1  1.4.1  1.3.5  1.2.0  1.1.1  1.0.0  0.2.2  0.1.0 
    
    
    ApprovalRequest(mapping=None, *, ignore_unknown_fields=False, **kwargs)

A request for the customer to approve access to a resource.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

## Attributes  
  
---  
**Name** | **Description**  
`name` |  `str`   
The resource name of the request. Format is "{projects|folders|organizations}/{id}/approvalRequests/{approval_request}".   
`requested_resource_name` |  `str`   
The resource for which approval is being requested. The format of the resource name is defined at https://cloud.google.com/apis/design/resource_names. The resource name here may either be a "full" resource name (e.g. "//library.googleapis.com/shelves/shelf1/books/book2") or a "relative" resource name (e.g. "shelves/shelf1/books/book2") as described in the resource name specification.   
`requested_resource_properties` |  `[google.cloud.accessapproval_v1.types.ResourceProperties](https://docs.cloud.google.com/python/docs/reference/accessapproval/latest/google.cloud.accessapproval_v1.types.ResourceProperties)`   
Properties related to the resource represented by requested_resource_name.   
`requested_reason` |  `[google.cloud.accessapproval_v1.types.AccessReason](https://docs.cloud.google.com/python/docs/reference/accessapproval/latest/google.cloud.accessapproval_v1.types.AccessReason)`   
The justification for which approval is being requested.   
`requested_locations` |  `[google.cloud.accessapproval_v1.types.AccessLocations](https://docs.cloud.google.com/python/docs/reference/accessapproval/latest/google.cloud.accessapproval_v1.types.AccessLocations)`   
The locations for which approval is being requested.   
`request_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
The time at which approval was requested.   
`requested_expiration` |  `google.protobuf.timestamp_pb2.Timestamp`   
The requested expiration for the approval. If the request is approved, access will be granted from the time of approval until the expiration time.   
`approve` |  `[google.cloud.accessapproval_v1.types.ApproveDecision](https://docs.cloud.google.com/python/docs/reference/accessapproval/latest/google.cloud.accessapproval_v1.types.ApproveDecision)`   
Access was approved. This field is a member of `oneof`_ `decision`.   
`dismiss` |  `[google.cloud.accessapproval_v1.types.DismissDecision](https://docs.cloud.google.com/python/docs/reference/accessapproval/latest/google.cloud.accessapproval_v1.types.DismissDecision)`   
The request was dismissed. This field is a member of `oneof`_ `decision`.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-04 UTC."],[],[]] 
