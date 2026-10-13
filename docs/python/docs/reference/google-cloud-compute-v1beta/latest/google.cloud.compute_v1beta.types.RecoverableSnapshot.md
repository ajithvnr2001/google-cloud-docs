---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.RecoverableSnapshot
title: Class RecoverableSnapshot (0.12.7) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:27:51.239000+00:00
---

# Class RecoverableSnapshot (0.12.7)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.RecoverableSnapshot

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class RecoverableSnapshot (0.12.7) Stay organized with collections  Save and categorize content based on your preferences. 

0.12.7 (latest)  0.12.6  0.11.0  0.4.0  0.3.0  0.2.0  0.1.8 
    
    
    RecoverableSnapshot(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Represents a RecoverableSnapshot resource.

A RecoverableSnapshot represents a snapshot in recycle bin.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

## Attributes  
  
---  
**Name** | **Description**  
`creation_timestamp` |  `str`   
Output only. [Output Only] Creation timestamp inRFC3339 text format. This field is a member of `oneof`_ `_creation_timestamp`.   
`description` |  `str`   
Optional. An optional description of this resource. This field is a member of `oneof`_ `_description`.   
`id` |  `int`   
Output only. [Output Only] The unique identifier for the resource. This identifier is defined by the server. This field is a member of `oneof`_ `_id`.   
`kind` |  `str`   
Output only. [Output Only] Type of the resource. Alwayscompute#recoverableSnapshot for RecoverableSnapshot resources. This field is a member of `oneof`_ `_kind`.   
`name` |  `str`   
Output only. Identifier. Name of the recoverable snapshot generated on the deletion of the snapshot. The name will be 1-63 characters long, and comply withRFC1035. Specifically, the name will be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character will be a lowercase letter, and all following characters can be a dash, lowercase letter, or digit, except the last character, which cannot be a dash. This field is a member of `oneof`_ `_name`.   
`original_resource` |  `[google.cloud.compute_v1beta.types.RecoverableSnapshotOriginalSnapshot](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.RecoverableSnapshotOriginalSnapshot)`   
Output only. Output Only] The original snapshot resource. This field is a member of `oneof`_ `_original_resource`.   
`purge_timestamp` |  `str`   
Output only. [Output Only] Purge timestamp of recoverable snapshot inRFC3339 text format. This field is a member of `oneof`_ `_purge_timestamp`.   
`satisfies_pzi` |  `bool`   
Output only. [Output Only] Reserved for future use. This field is a member of `oneof`_ `_satisfies_pzi`.   
`satisfies_pzs` |  `bool`   
Output only. [Output Only] Reserved for future use. This field is a member of `oneof`_ `_satisfies_pzs`.   
`self_link` |  `str`   
Output only. [Output Only] Server-defined URL for the resource. This field is a member of `oneof`_ `_self_link`.   
`self_link_with_id` |  `str`   
Output only. [Output Only] Server-defined URL for this resource's resource id. This field is a member of `oneof`_ `_self_link_with_id`.   
`status` |  `str`   
Output only. [Output Only] Status of the recoverable snapshot. Check the Status enum for the list of possible values. This field is a member of `oneof`_ `_status`.   
  
## Classes 

### Status
    
    
    Status(value)

Output only. [Output Only] Status of the recoverable snapshot.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
