---
url: https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.types.Asset
title: Class Asset (2.21.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:56:37.242033+00:00
---

# Class Asset (2.21.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.types.Asset

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class Asset (2.21.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.21.0 (latest)  2.20.0  2.19.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.2  2.9.0  2.8.0  2.7.1  2.6.0  2.5.0  2.4.0  2.3.1  2.2.2  2.1.0  2.0.1  1.13.0  1.12.3  1.11.0  1.10.0  1.9.0  1.8.1  1.7.0  1.6.2  1.5.1  1.4.3  1.3.0  1.2.0  1.1.3  1.0.1  0.2.1  0.1.0 
    
    
    Asset(mapping=None, *, ignore_unknown_fields=False, **kwargs)

An asset represents a cloud resource that is being managed within a lake as a member of a zone.

## Attributes  
  
---  
**Name** | **Description**  
`name` |  `str`   
Output only. The relative resource name of the asset, of the form: `projects/{project_number}/locations/{location_id}/lakes/{lake_id}/zones/{zone_id}/assets/{asset_id}`.   
`display_name` |  `str`   
Optional. User friendly display name.   
`uid` |  `str`   
Output only. System generated globally unique ID for the asset. This ID will be different if the asset is deleted and re-created with the same name.   
`create_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. The time when the asset was created.   
`update_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. The time when the asset was last updated.   
`labels` |  `MutableMapping[str, str]`   
Optional. User defined labels for the asset.   
`description` |  `str`   
Optional. Description of the asset.   
`state` |  `[google.cloud.dataplex_v1.types.State](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.types.State)`   
Output only. Current state of the asset.   
`resource_spec` |  `[google.cloud.dataplex_v1.types.Asset.ResourceSpec](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.types.Asset.ResourceSpec)`   
Required. Specification of the resource that is referenced by this asset.   
`resource_status` |  `[google.cloud.dataplex_v1.types.Asset.ResourceStatus](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.types.Asset.ResourceStatus)`   
Output only. Status of the resource referenced by this asset.   
`security_status` |  `[google.cloud.dataplex_v1.types.Asset.SecurityStatus](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.types.Asset.SecurityStatus)`   
Output only. Status of the security policy applied to resource referenced by this asset.   
`discovery_spec` |  `[google.cloud.dataplex_v1.types.Asset.DiscoverySpec](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.types.Asset.DiscoverySpec)`   
Optional. Specification of the discovery feature applied to data referenced by this asset. When this spec is left unset, the asset will use the spec set on the parent zone.   
`discovery_status` |  `[google.cloud.dataplex_v1.types.Asset.DiscoveryStatus](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.types.Asset.DiscoveryStatus)`   
Output only. Status of the discovery feature applied to data referenced by this asset.   
  
## Classes 

### DiscoverySpec
    
    
    DiscoverySpec(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Settings to manage the metadata discovery and publishing for an asset.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### DiscoveryStatus
    
    
    DiscoveryStatus(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Status of discovery for an asset.

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
  
### ResourceSpec
    
    
    ResourceSpec(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Identifies the cloud resource that is referenced by this asset.

### ResourceStatus
    
    
    ResourceStatus(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Status of the resource referenced by an asset.

### SecurityStatus
    
    
    SecurityStatus(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Security policy status of the asset. Data security policy, i.e., readers, writers & owners, should be specified in the lake/zone/asset IAM policy.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
