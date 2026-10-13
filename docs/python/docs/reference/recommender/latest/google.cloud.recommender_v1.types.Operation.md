---
url: https://docs.cloud.google.com/python/docs/reference/recommender/latest/google.cloud.recommender_v1.types.Operation
title: Class Operation (2.23.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:12:38.526370+00:00
---

# Class Operation (2.23.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/recommender/latest/google.cloud.recommender_v1.types.Operation

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class Operation (2.23.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.23.0 (latest)  2.22.0  2.21.0  2.20.0  2.19.0  2.18.2  2.17.0  2.16.1  2.15.5  2.14.0  2.13.0  2.12.0  2.11.2  2.10.1  2.9.0  2.8.3  2.7.4  2.6.0  2.5.1  2.4.0  2.3.4  2.2.0  2.1.0  2.0.0  1.1.3  1.0.0  0.3.0  0.2.0  0.1.0 
    
    
    Operation(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Contains an operation for a resource loosely based on the JSON-PATCH format with support for:

  * Custom filters for describing partial array patch.
  * Extended path values for describing nested arrays.
  * Custom fields for describing the resource for which the operation is being described.
  * Allows extension to custom operations not natively supported by RFC6902. See <https://tools.ietf.org/html/rfc6902> for details on the original RFC.



This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

## Attributes  
  
---  
**Name** | **Description**  
`action` |  `str`   
Type of this operation. Contains one of 'add', 'remove', 'replace', 'move', 'copy', 'test' and custom operations. This field is case-insensitive and always populated.   
`resource_type` |  `str`   
Type of GCP resource being modified/tested. This field is always populated. Example: cloudresourcemanager.googleapis.com/Project, compute.googleapis.com/Instance   
`resource` |  `str`   
Contains the fully qualified resource name. This field is always populated. ex: //cloudresourcemanager.googleapis.com/projects/foo.   
`path` |  `str`   
Path to the target field being operated on. If the operation is at the resource level, then path should be "/". This field is always populated.   
`source_resource` |  `str`   
Can be set with action 'copy' to copy resource configuration across different resources of the same type. Example: A resource clone can be done via action = 'copy', path = "/", from = "/", source_resource = and resource_name = . This field is empty for all other values of `action`.   
`source_path` |  `str`   
Can be set with action 'copy' or 'move' to indicate the source field within resource or source_resource, ignored if provided for other operation types.   
`value` |  `google.protobuf.struct_pb2.Value`   
Value for the `path` field. Will be set for actions:'add'/'replace'. Maybe set for action: 'test'. Either this or `value_matcher` will be set for 'test' operation. An exact match must be performed. This field is a member of `oneof`_ `path_value`.   
`value_matcher` |  `[google.cloud.recommender_v1.types.ValueMatcher](https://docs.cloud.google.com/python/docs/reference/recommender/latest/google.cloud.recommender_v1.types.ValueMatcher)`   
Can be set for action 'test' for advanced matching for the value of 'path' field. Either this or `value` will be set for 'test' operation. This field is a member of `oneof`_ `path_value`.   
`path_filters` |  `MutableMapping[str, google.protobuf.struct_pb2.Value]`   
Set of filters to apply if `path` refers to array elements or nested array elements in order to narrow down to a single unique element that is being tested/modified. This is intended to be an exact match per filter. To perform advanced matching, use path_value_matchers. \- Example: :: { "/versions/*/name" : "it-123" "/versions/*/targetSize/percent": 20 } \- Example: :: { "/bindings/*/role": "roles/owner" "/bindings/*/condition" : null } \- Example: :: { "/bindings/*/role": "roles/owner" "/bindings/*/members/*" : ["x@example.com", "y@example.com"] } When both path_filters and path_value_matchers are set, an implicit AND must be performed.   
`path_value_matchers` |  `MutableMapping[str, [google.cloud.recommender_v1.types.ValueMatcher](https://docs.cloud.google.com/python/docs/reference/recommender/latest/google.cloud.recommender_v1.types.ValueMatcher)]`   
Similar to path_filters, this contains set of filters to apply if `path` field refers to array elements. This is meant to support value matching beyond exact match. To perform exact match, use path_filters. When both path_filters and path_value_matchers are set, an implicit AND must be performed.   
  
## Classes 

### PathFiltersEntry
    
    
    PathFiltersEntry(mapping=None, *, ignore_unknown_fields=False, **kwargs)

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
  
### PathValueMatchersEntry
    
    
    PathValueMatchersEntry(mapping=None, *, ignore_unknown_fields=False, **kwargs)

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
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
