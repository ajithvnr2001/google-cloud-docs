---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.TargetGrpcProxy
title: Class TargetGrpcProxy (0.12.7) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:15:07.428985+00:00
---

# Class TargetGrpcProxy (0.12.7)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.TargetGrpcProxy

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class TargetGrpcProxy (0.12.7) Stay organized with collections  Save and categorize content based on your preferences. 

0.12.7 (latest)  0.12.6  0.11.0  0.4.0  0.3.0  0.2.0  0.1.8 
    
    
    TargetGrpcProxy(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Represents a Target gRPC Proxy resource.

A target gRPC proxy is a component of load balancers intended for load balancing gRPC traffic. Only global forwarding rules with load balancing scheme INTERNAL_SELF_MANAGED can reference a target gRPC proxy. The target gRPC Proxy references a URL map that specifies how traffic is routed to gRPC backend services.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

## Attributes  
  
---  
**Name** | **Description**  
`creation_timestamp` |  `str`   
Output only. [Output Only] Creation timestamp inRFC3339 text format. This field is a member of `oneof`_ `_creation_timestamp`.   
`description` |  `str`   
An optional description of this resource. Provide this property when you create the resource. This field is a member of `oneof`_ `_description`.   
`fingerprint` |  `str`   
Fingerprint of this resource. A hash of the contents stored in this object. This field is used in optimistic locking. This field will be ignored when inserting a TargetGrpcProxy. An up-to-date fingerprint must be provided in order to patch/update the TargetGrpcProxy; otherwise, the request will fail with error 412 conditionNotMet. To see the latest fingerprint, make a get() request to retrieve the TargetGrpcProxy. This field is a member of `oneof`_ `_fingerprint`.   
`id` |  `int`   
Output only. [Output Only] The unique identifier for the resource type. The server generates this identifier. This field is a member of `oneof`_ `_id`.   
`kind` |  `str`   
Output only. [Output Only] Type of the resource. Alwayscompute#targetGrpcProxy for target grpc proxies. This field is a member of `oneof`_ `_kind`.   
`name` |  `str`   
Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply withRFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash. This field is a member of `oneof`_ `_name`.   
`self_link` |  `str`   
Output only. [Output Only] Server-defined URL for the resource. This field is a member of `oneof`_ `_self_link`.   
`self_link_with_id` |  `str`   
Output only. [Output Only] Server-defined URL with id for the resource. This field is a member of `oneof`_ `_self_link_with_id`.   
`url_map` |  `str`   
URL to the UrlMap resource that defines the mapping from URL to the BackendService. The protocol field in the BackendService must be set to GRPC. This field is a member of `oneof`_ `_url_map`.   
`validate_for_proxyless` |  `bool`   
If true, indicates that the BackendServices referenced by the urlMap may be accessed by gRPC applications without using a sidecar proxy. This will enable configuration checks on urlMap and its referenced BackendServices to not allow unsupported features. A gRPC application must use "xds:///" scheme in the target URI of the service it is connecting to. If false, indicates that the BackendServices referenced by the urlMap will be accessed by gRPC applications via a sidecar proxy. In this case, a gRPC application must not use "xds:///" scheme in the target URI of the service it is connecting to This field is a member of `oneof`_ `_validate_for_proxyless`.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
