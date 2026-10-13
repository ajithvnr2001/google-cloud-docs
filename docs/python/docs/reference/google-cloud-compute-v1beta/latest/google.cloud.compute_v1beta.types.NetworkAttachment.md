---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.NetworkAttachment
title: Class NetworkAttachment (0.12.7) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:12:16.460705+00:00
---

# Class NetworkAttachment (0.12.7)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.NetworkAttachment

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class NetworkAttachment (0.12.7) Stay organized with collections  Save and categorize content based on your preferences. 

0.12.7 (latest)  0.12.6  0.11.0  0.4.0  0.3.0  0.2.0  0.1.8 
    
    
    NetworkAttachment(mapping=None, *, ignore_unknown_fields=False, **kwargs)

NetworkAttachments A network attachment resource ...

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

## Attributes  
  
---  
**Name** | **Description**  
`connection_endpoints` |  `MutableSequence[[google.cloud.compute_v1beta.types.NetworkAttachmentConnectedEndpoint](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.NetworkAttachmentConnectedEndpoint)]`   
Output only. [Output Only] An array of connections for all the producers connected to this network attachment.   
`connection_preference` |  `str`   
Check the ConnectionPreference enum for the list of possible values. This field is a member of `oneof`_ `_connection_preference`.   
`creation_timestamp` |  `str`   
Output only. [Output Only] Creation timestamp inRFC3339 text format. This field is a member of `oneof`_ `_creation_timestamp`.   
`description` |  `str`   
An optional description of this resource. Provide this property when you create the resource. This field is a member of `oneof`_ `_description`.   
`fingerprint` |  `str`   
Fingerprint of this resource. A hash of the contents stored in this object. This field is used in optimistic locking. An up-to-date fingerprint must be provided in order to patch. This field is a member of `oneof`_ `_fingerprint`.   
`id` |  `int`   
Output only. [Output Only] The unique identifier for the resource type. The server generates this identifier. This field is a member of `oneof`_ `_id`.   
`kind` |  `str`   
Output only. [Output Only] Type of the resource. This field is a member of `oneof`_ `_kind`.   
`name` |  `str`   
Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply withRFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash. This field is a member of `oneof`_ `_name`.   
`network` |  `str`   
Output only. [Output Only] The URL of the network which the Network Attachment belongs to. Practically it is inferred by fetching the network of the first subnetwork associated. Because it is required that all the subnetworks must be from the same network, it is assured that the Network Attachment belongs to the same network as all the subnetworks. This field is a member of `oneof`_ `_network`.   
`producer_accept_lists` |  `MutableSequence[str]`   
Projects or service class ids that are allowed to connect to this network attachment. The project can be specified using its id or number. Service class id can be specified as "serviceclasses/{service_class_id}".   
`producer_reject_lists` |  `MutableSequence[str]`   
Projects or service class ids that are not allowed to connect to this network attachment. The project can be specified using its id or number. Service class id can be specified as "serviceclasses/{service_class_id}".   
`region` |  `str`   
Output only. [Output Only] URL of the region where the network attachment resides. This field applies only to the region resource. You must specify this field as part of the HTTP request URL. It is not settable as a field in the request body. This field is a member of `oneof`_ `_region`.   
`self_link` |  `str`   
Output only. [Output Only] Server-defined URL for the resource. This field is a member of `oneof`_ `_self_link`.   
`self_link_with_id` |  `str`   
Output only. [Output Only] Server-defined URL for this resource's resource id. This field is a member of `oneof`_ `_self_link_with_id`.   
`subnetworks` |  `MutableSequence[str]`   
An array of URLs where each entry is the URL of a subnet provided by the service consumer to use for endpoints in the producers that connect to this network attachment.   
  
## Classes 

### ConnectionPreference
    
    
    ConnectionPreference(value)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
