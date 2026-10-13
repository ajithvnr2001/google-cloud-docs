---
url: https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.ResourceSearchResult
title: Class ResourceSearchResult (4.5.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:35:35.375965+00:00
---

# Class ResourceSearchResult (4.5.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.ResourceSearchResult

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class ResourceSearchResult (4.5.0) Stay organized with collections  Save and categorize content based on your preferences. 

4.5.0 (latest)  4.4.0  4.3.0  4.2.0  4.1.0  4.0.0  3.30.1  3.29.2  3.28.0  3.27.1  3.26.4  3.25.1  3.24.3  3.23.0  3.22.0  3.21.0  3.20.1  3.19.1  3.18.1  3.17.1  3.16.0  3.15.0  3.14.2  3.13.1  3.12.0  3.11.0  3.10.0  3.9.1  3.8.1  3.7.1  3.6.1  3.5.0  3.4.0  3.3.0  3.2.1  3.1.0  2.2.2  2.1.0  2.0.0  1.3.2  1.2.0  1.1.0  1.0.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.1  0.3.0 
    
    
    ResourceSearchResult(mapping=None, *, ignore_unknown_fields=False, **kwargs)

A result of Resource Search, containing information of a cloud resource.

## Attributes  
  
---  
**Name** | **Description**  
`name` |  `str`   
The full resource name of this resource. Example: `//compute.googleapis.com/projects/my_project_123/zones/zone1/instances/instance1`. See `Cloud Asset Inventory Resource Name Format   
`asset_type` |  `str`   
The type of this resource. Example: `compute.googleapis.com/Disk`. To search against the `asset_type`: \- Specify the `asset_type` field in your search request.   
`project` |  `str`   
The project that this resource belongs to, in the form of projects/{PROJECT_NUMBER}. This field is available when the resource belongs to a project. To search against `project`: \- Use a field query. Example: `project:12345` \- Use a free text query. Example: `12345` \- Specify the `scope` field as this project in your search request.   
`folders` |  `MutableSequence[str]`   
The folder(s) that this resource belongs to, in the form of folders/{FOLDER_NUMBER}. This field is available when the resource belongs to one or more folders. To search against `folders`: \- Use a field query. Example: `folders:(123 OR 456)` \- Use a free text query. Example: `123` \- Specify the `scope` field as this folder in your search request.   
`organization` |  `str`   
The organization that this resource belongs to, in the form of organizations/{ORGANIZATION_NUMBER}. This field is available when the resource belongs to an organization. To search against `organization`: \- Use a field query. Example: `organization:123` \- Use a free text query. Example: `123` \- Specify the `scope` field as this organization in your search request.   
`display_name` |  `str`   
The display name of this resource. This field is available only when the resource's Protobuf contains it. To search against the `display_name`: \- Use a field query. Example: `displayName:"My Instance"` \- Use a free text query. Example: `"My Instance"`  
`description` |  `str`   
One or more paragraphs of text description of this resource. Maximum length could be up to 1M bytes. This field is available only when the resource's Protobuf contains it. To search against the `description`: \- Use a field query. Example: `description:"important instance"` \- Use a free text query. Example: `"important instance"`  
`location` |  `str`   
Location can be `global`, regional like `us-east1`, or zonal like `us-west1-b`. This field is available only when the resource's Protobuf contains it. To search against the `location`: \- Use a field query. Example: `location:us-west*` \- Use a free text query. Example: `us-west*`  
`labels` |  `MutableMapping[str, str]`   
User labels associated with this resource. See `Labelling and grouping Google Cloud resources   
`network_tags` |  `MutableSequence[str]`   
Network tags associated with this resource. Like labels, network tags are a type of annotations used to group Google Cloud resources. See `Labelling Google Cloud resources   
`kms_key` |  `str`   
The Cloud KMS `CryptoKey `__ name or `CryptoKeyVersion `__ name. This field only presents for the purpose of backward compatibility. Use the `kms_keys` field to retrieve Cloud KMS key information. This field is available only when the resource's Protobuf contains it and will only be populated for `these resource types   
`kms_keys` |  `MutableSequence[str]`   
The Cloud KMS `CryptoKey `__ names or `CryptoKeyVersion `__ names. This field is available only when the resource's Protobuf contains it. To search against the `kms_keys`: \- Use a field query. Example: `kmsKeys:key` \- Use a free text query. Example: `key`  
`create_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
The create timestamp of this resource, at which the resource was created. The granularity is in seconds. Timestamp.nanos will always be 0. This field is available only when the resource's Protobuf contains it. To search against `create_time`: \- Use a field query. \- value in seconds since unix epoch. Example: `createTime > 1609459200` \- value in date string. Example: `createTime > 2021-01-01` \- value in date-time string (must be quoted). Example: `createTime > "2021-01-01T00:00:00"`  
`update_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
The last update timestamp of this resource, at which the resource was last modified or deleted. The granularity is in seconds. Timestamp.nanos will always be 0. This field is available only when the resource's Protobuf contains it. To search against `update_time`: \- Use a field query. \- value in seconds since unix epoch. Example: `updateTime <>` \- value in date string. Example: `updateTime <>` \- value in date-time string (must be quoted). Example: `updateTime <>`  
`state` |  `str`   
The state of this resource. Different resources types have different state definitions that are mapped from various fields of different resource types. This field is available only when the resource's Protobuf contains it. Example: If the resource is an instance provided by Compute Engine, its state will include PROVISIONING, STAGING, RUNNING, STOPPING, SUSPENDING, SUSPENDED, REPAIRING, and TERMINATED. See `status` definition in `API Reference   
`additional_attributes` |  `google.protobuf.struct_pb2.Struct`   
The additional searchable attributes of this resource. The attributes may vary from one resource type to another. Examples: `projectId` for Project, `dnsName` for DNS ManagedZone. This field contains a subset of the resource metadata fields that are returned by the List or Get APIs provided by the corresponding Google Cloud service (e.g., Compute Engine). see `API references and supported searchable attributes   
`parent_full_resource_name` |  `str`   
The full resource name of this resource's parent, if it has one. To search against the `parent_full_resource_name`: \- Use a field query. Example: `parentFullResourceName:"project-name"` \- Use a free text query. Example: `project-name`  
`versioned_resources` |  `MutableSequence[[google.cloud.asset_v1.types.VersionedResource](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.VersionedResource)]`   
Versioned resource representations of this resource. This is repeated because there could be multiple versions of resource representations during version migration. This `versioned_resources` field is not searchable. Some attributes of the resource representations are exposed in `additional_attributes` field, so as to allow users to search on them.   
`attached_resources` |  `MutableSequence[[google.cloud.asset_v1.types.AttachedResource](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.AttachedResource)]`   
Attached resources of this resource. For example, an OSConfig Inventory is an attached resource of a Compute Instance. This field is repeated because a resource could have multiple attached resources. This `attached_resources` field is not searchable. Some attributes of the attached resources are exposed in `additional_attributes` field, so as to allow users to search on them.   
`relationships` |  `MutableMapping[str, [google.cloud.asset_v1.types.RelatedResources](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.RelatedResources)]`   
A map of related resources of this resource, keyed by the relationship type. A relationship type is in the format of {SourceType}\ *{ACTION}*\ {DestType}. Example: `DISK_TO_INSTANCE`, `DISK_TO_NETWORK`, `INSTANCE_TO_INSTANCEGROUP`. See `supported relationship types   
`tag_keys` |  `MutableSequence[str]`   
This field is only present for the purpose of backward compatibility. Use the `tags` field instead. TagKey namespaced names, in the format of {ORG_ID}/{TAG_KEY_SHORT_NAME}. To search against the `tagKeys`: \- Use a field query. Example: \- `tagKeys:"123456789/env*"` \- `tagKeys="123456789/env"` \- `tagKeys:"env"` \- Use a free text query. Example: \- `env`  
`tag_values` |  `MutableSequence[str]`   
This field is only present for the purpose of backward compatibility. Use the `tags` field instead. TagValue namespaced names, in the format of {ORG_ID}/{TAG_KEY_SHORT_NAME}/{TAG_VALUE_SHORT_NAME}. To search against the `tagValues`: \- Use a field query. Example: \- `tagValues:"env"` \- `tagValues:"env/prod"` \- `tagValues:"123456789/env/prod*"` \- `tagValues="123456789/env/prod"` \- Use a free text query. Example: \- `prod`  
`tag_value_ids` |  `MutableSequence[str]`   
This field is only present for the purpose of backward compatibility. Use the `tags` field instead. TagValue IDs, in the format of tagValues/{TAG_VALUE_ID}. To search against the `tagValueIds`: \- Use a field query. Example: \- `tagValueIds="tagValues/456"` \- Use a free text query. Example: \- `456`  
`tags` |  `MutableSequence[[google.cloud.asset_v1.types.Tag](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.Tag)]`   
The tags directly attached to this resource. To search against the `tags`: \- Use a field query. Example: \- `tagKeys:"123456789/env*"` \- `tagKeys="123456789/env"` \- `tagKeys:"env"` \- `tagKeyIds="tagKeys/123"` \- `tagValues:"env"` \- `tagValues:"env/prod"` \- `tagValues:"123456789/env/prod*"` \- `tagValues="123456789/env/prod"` \- `tagValueIds="tagValues/456"` \- Use a free text query. Example: \- `env/prod`  
`effective_tags` |  `MutableSequence[[google.cloud.asset_v1.types.EffectiveTagDetails](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.EffectiveTagDetails)]`   
The effective tags on this resource. All of the tags that are both attached to and inherited by a resource are collectively called the effective tags. For more information, see `tag inheritance   
`enrichments` |  `MutableSequence[[google.cloud.asset_v1.types.AssetEnrichment](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.AssetEnrichment)]`   
Enrichments of the asset. Currently supported enrichment types with SearchAllResources API: \- RESOURCE_OWNERS The corresponding read masks in order to get the enrichment: \- enrichments.resource_owners The corresponding required permissions: \- cloudasset.assets.searchEnrichmentResourceOwners Example query to get resource owner enrichment: :: scope: "projects/my-project" query: "name: my-project" assetTypes: "cloudresourcemanager.googleapis.com/Project" readMask: { paths: "asset_type" paths: "name" paths: "enrichments.resource_owners" }   
`parent_asset_type` |  `str`   
The type of this resource's immediate parent, if there is one. To search against the `parent_asset_type`: \- Use a field query. Example: `parentAssetType:"cloudresourcemanager.googleapis.com/Project"` \- Use a free text query. Example: `cloudresourcemanager.googleapis.com/Project`  
`scc_security_marks` |  `MutableMapping[str, str]`   
The actual content of Security Command Center security marks associated with the asset. To search against SCC SecurityMarks field: \- Use a field query: \- query by a given key value pair. Example: `sccSecurityMarks.foo=bar` \- query by a given key's existence. Example: `sccSecurityMarks.foo:*`  
  
## Classes 

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
  
### RelationshipsEntry
    
    
    RelationshipsEntry(mapping=None, *, ignore_unknown_fields=False, **kwargs)

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
  
### SccSecurityMarksEntry
    
    
    SccSecurityMarksEntry(mapping=None, *, ignore_unknown_fields=False, **kwargs)

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

Last updated 2026-10-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-04 UTC."],[],[]] 
