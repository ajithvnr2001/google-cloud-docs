---
url: https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/searchAllResources/
title: Method: searchAllResources \u00a0|\u00a0 Cloud Asset Inventory \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:30:04.750962+00:00
---

# Method: searchAllResources  |  Cloud Asset Inventory  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/searchAllResources/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Cloud Asset Inventory ](https://docs.cloud.google.com/asset-inventory/docs)
  * [ Reference ](https://docs.cloud.google.com/asset-inventory/docs/asset-types)



Send feedback 

#  Method: searchAllResources Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * ResourceSearchResult
    * JSON representation
  * VersionedResource
    * JSON representation
  * AttachedResource
    * JSON representation
  * RelatedResources
    * JSON representation
  * RelatedResource
    * JSON representation
  * AssetEnrichment
    * JSON representation
  * ResourceOwners
    * JSON representation
  * Try it!



Searches all Google Cloud resources within the specified scope, such as a project, folder, or organization. The caller must be granted the `cloudasset.assets.searchAllResources` permission on the desired scope, otherwise the request will be rejected.

### HTTP request

`GET https://cloudasset.googleapis.com/v1/{scope=*/*}:searchAllResources`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`scope` |  `string` Required. A scope can be a project, a folder, or an organization. The search is limited to the resources within the `scope`. The caller must be granted the [`cloudasset.assets.searchAllResources`](https://cloud.google.com/asset-inventory/docs/access-control#required_permissions) permission on the desired scope.The allowed values are:

  * projects/{PROJECT_ID} (e.g., "projects/foo-bar")
  * projects/{PROJECT_NUMBER} (e.g., "projects/12345678")
  * folders/{FOLDER_NUMBER} (e.g., "folders/1234567")
  * organizations/{ORGANIZATION_NUMBER} (e.g., "organizations/123456")

Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `scope`:

  * `cloudasset.assets.searchAllResources`

  
  
### Query parameters

Parameters  
---  
`query` |  `string` Optional. The query statement. See [how to construct a query](https://cloud.google.com/asset-inventory/docs/searching-resources#how_to_construct_a_query) for more information. If not specified or empty, it will search all the resources within the specified `scope`.Examples:

  * `name:Important` to find Google Cloud resources whose name contains `Important` as a word.
  * `name=Important` to find the Google Cloud resource whose name is exactly `Important`.
  * `displayName:Impor*` to find Google Cloud resources whose display name contains `Impor` as a prefix of any word in the field.
  * `location:us-west*` to find Google Cloud resources whose location contains both `us` and `west` as prefixes.
  * `labels:prod` to find Google Cloud resources whose labels contain `prod` as a key or value.
  * `labels.env:prod` to find Google Cloud resources that have a label `env` and its value is `prod`.
  * `labels.env:*` to find Google Cloud resources that have a label `env`.
  * `tagKeys:env` to find Google Cloud resources that have directly attached tags where the [`TagKey.namespacedName`](https://cloud.google.com/resource-manager/reference/rest/v3/tagKeys#resource:-tagkey) contains `env`.
  * `tagValues:prod*` to find Google Cloud resources that have directly attached tags where the [`TagValue.namespacedName`](https://cloud.google.com/resource-manager/reference/rest/v3/tagValues#resource:-tagvalue) contains a word prefixed by `prod`.
  * `tagValueIds=tagValues/123` to find Google Cloud resources that have directly attached tags where the [`TagValue.name`](https://cloud.google.com/resource-manager/reference/rest/v3/tagValues#resource:-tagvalue) is exactly `tagValues/123`.
  * `effectiveTagKeys:env` to find Google Cloud resources that have directly attached or inherited tags where the [`TagKey.namespacedName`](https://cloud.google.com/resource-manager/reference/rest/v3/tagKeys#resource:-tagkey) contains `env`.
  * `effectiveTagValues:prod*` to find Google Cloud resources that have directly attached or inherited tags where the [`TagValue.namespacedName`](https://cloud.google.com/resource-manager/reference/rest/v3/tagValues#resource:-tagvalue) contains a word prefixed by `prod`.
  * `effectiveTagValueIds=tagValues/123` to find Google Cloud resources that have directly attached or inherited tags where the [`TagValue.name`](https://cloud.google.com/resource-manager/reference/rest/v3/tagValues#resource:-tagvalue) is exactly `tagValues/123`.
  * `kmsKey:key` to find Google Cloud resources encrypted with a customer-managed encryption key whose name contains `key` as a word. This field is deprecated. Use the `kmsKeys` field to retrieve Cloud KMS key information.
  * `kmsKeys:key` to find Google Cloud resources encrypted with customer-managed encryption keys whose name contains the word `key`.
  * `relationships:instance-group-1` to find Google Cloud resources that have relationships with `instance-group-1` in the related resource name.
  * `relationships:INSTANCE_TO_INSTANCEGROUP` to find Compute Engine instances that have relationships of type `INSTANCE_TO_INSTANCEGROUP`.
  * `relationships.INSTANCE_TO_INSTANCEGROUP:instance-group-1` to find Compute Engine instances that have relationships with `instance-group-1` in the Compute Engine instance group resource name, for relationship type `INSTANCE_TO_INSTANCEGROUP`.
  * `sccSecurityMarks.key=value` to find Cloud resources that are attached with security marks whose key is `key` and value is `value`.
  * `sccSecurityMarks.key:*` to find Cloud resources that are attached with security marks whose key is `key`.
  * `state:ACTIVE` to find Google Cloud resources whose state contains `ACTIVE` as a word.
  * `NOT state:ACTIVE` to find Google Cloud resources whose state doesn't contain `ACTIVE` as a word.
  * `createTime<1609459200` to find Google Cloud resources that were created before `2021-01-01 00:00:00 UTC`. `1609459200` is the epoch timestamp of `2021-01-01 00:00:00 UTC` in seconds.
  * `updateTime>1609459200` to find Google Cloud resources that were updated after `2021-01-01 00:00:00 UTC`. `1609459200` is the epoch timestamp of `2021-01-01 00:00:00 UTC` in seconds.
  * `Important` to find Google Cloud resources that contain `Important` as a word in any of the searchable fields.
  * `Impor*` to find Google Cloud resources that contain `Impor` as a prefix of any word in any of the searchable fields.
  * `Important location:(us-west1 OR global)` to find Google Cloud resources that contain `Important` as a word in any of the searchable fields and are also located in the `us-west1` region or the `global` location.

  
`assetTypes[]` |  `string` Optional. A list of asset types that this request searches for. If empty, it will search all the asset types [supported by search APIs](https://cloud.google.com/asset-inventory/docs/supported-asset-types).Regular expressions are also supported. For example:

  * "compute.googleapis.com.*" snapshots resources whose asset type starts with "compute.googleapis.com".
  * ".*Instance" snapshots resources whose asset type ends with "Instance".
  * ".*Instance.*" snapshots resources whose asset type contains "Instance".

See [RE2](https://github.com/google/re2/wiki/Syntax) for all supported regular expression syntax. If the regular expression does not match any supported asset type, an INVALID_ARGUMENT error will be returned.  
`pageSize` |  `integer` Optional. The page size for search result pagination. Page size is capped at 500 even if a larger value is given. If set to zero or a negative value, server will pick an appropriate default. Returned results may be fewer than requested. When this happens, there could be more results as long as `nextPageToken` is returned.  
`pageToken` |  `string` Optional. If present, then retrieve the next batch of results from the preceding call to this method. `pageToken` must be the value of `nextPageToken` from the previous response. The values of all other method parameters, must be identical to those in the previous call.  
`orderBy` |  `string` Optional. A comma-separated list of fields specifying the sorting order of the results. The default order is ascending. Add " DESC" after the field name to indicate descending order. Redundant space characters are ignored. Example: "location DESC, name". Only the following fields in the response are sortable:

  * name
  * assetType
  * project
  * displayName
  * description
  * location
  * createTime
  * updateTime
  * state
  * parentFullResourceName
  * parentAssetType

  
`readMask` |  `string (`[FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` format)` Optional. A comma-separated list of fields that you want returned in the results. The following fields are returned by default if not specified:

  * `name`
  * `assetType`
  * `project`
  * `folders`
  * `organization`
  * `displayName`
  * `description`
  * `location`
  * `labels`
  * `tags`
  * `effectiveTags`
  * `networkTags`
  * `kmsKeys`
  * `createTime`
  * `updateTime`
  * `state`
  * `additionalAttributes`
  * `parentFullResourceName`
  * `parentAssetType`

Some fields of large size, such as `versionedResources`, `attachedResources`, `effectiveTags` etc., are not returned by default, but you can specify them in the `readMask` parameter if you want to include them. If `"*"` is specified, all [available fields](https://cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/searchAllResources#resourcesearchresult) are returned. Examples: `"name,location"`, `"name,versionedResources"`, `"*"`. Any invalid field path will trigger INVALID_ARGUMENT error.This is a comma-separated list of fully qualified names of fields. Example: `"user.displayName,photo"`.  
  
### Request body

The request body must be empty.

### Response body

Search all resources response.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "results": [
        {
          object ([ResourceSearchResult](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/searchAllResources#ResourceSearchResult))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`results[]` |  `object (`[ResourceSearchResult](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/searchAllResources#ResourceSearchResult)`)` A list of Resources that match the search query. It contains the resource standard metadata information.  
`nextPageToken` |  `string` If there are more results than those appearing in this response, then `nextPageToken` is included. To get the next set of results, call this method again using the value of `nextPageToken` as `pageToken`.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

## ResourceSearchResult

A result of Resource Search, containing information of a cloud resource.

JSON representation  
---  
      
    
    {
      "name": string,
      "assetType": string,
      "project": string,
      "folders": [
        string
      ],
      "organization": string,
      "displayName": string,
      "description": string,
      "location": string,
      "labels": {
        string: string,
        ...
      },
      "networkTags": [
        string
      ],
      "kmsKey": string,
      "kmsKeys": [
        string
      ],
      "createTime": string,
      "updateTime": string,
      "state": string,
      "additionalAttributes": {
        object
      },
      "parentFullResourceName": string,
      "versionedResources": [
        {
          object ([VersionedResource](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/searchAllResources#VersionedResource))
        }
      ],
      "attachedResources": [
        {
          object ([AttachedResource](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/searchAllResources#AttachedResource))
        }
      ],
      "relationships": {
        string: {
          object ([RelatedResources](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/searchAllResources#RelatedResources))
        },
        ...
      },
      "tagKeys": [
        string
      ],
      "tagValues": [
        string
      ],
      "tagValueIds": [
        string
      ],
      "tags": [
        {
          object ([Tag](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Tag))
        }
      ],
      "effectiveTags": [
        {
          object ([EffectiveTagDetails](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/EffectiveTagDetails))
        }
      ],
      "enrichments": [
        {
          object ([AssetEnrichment](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/searchAllResources#AssetEnrichment))
        }
      ],
      "parentAssetType": string,
      "sccSecurityMarks": {
        string: string,
        ...
      }
    }  
  
Fields  
---  
`name` |  `string` The full resource name of this resource. Example: `//compute.googleapis.com/projects/my_project_123/zones/zone1/instances/instance1`. See [Cloud Asset Inventory Resource Name Format](https://cloud.google.com/asset-inventory/docs/resource-name-format) for more information.To search against the `name`:

  * Use a field query. Example: `name:instance1`
  * Use a free text query. Example: `instance1`

  
`assetType` |  `string` The type of this resource. Example: `compute.googleapis.com/Disk`.To search against the `assetType`:

  * Specify the `assetType` field in your search request.

  
`project` |  `string` The project that this resource belongs to, in the form of projects/{PROJECT_NUMBER}. This field is available when the resource belongs to a project.To search against `project`:

  * Use a field query. Example: `project:12345`
  * Use a free text query. Example: `12345`
  * Specify the `scope` field as this project in your search request.

  
`folders[]` |  `string` The folder(s) that this resource belongs to, in the form of folders/{FOLDER_NUMBER}. This field is available when the resource belongs to one or more folders.To search against `folders`:

  * Use a field query. Example: `folders:(123 OR 456)`
  * Use a free text query. Example: `123`
  * Specify the `scope` field as this folder in your search request.

  
`organization` |  `string` The organization that this resource belongs to, in the form of organizations/{ORGANIZATION_NUMBER}. This field is available when the resource belongs to an organization.To search against `organization`:

  * Use a field query. Example: `organization:123`
  * Use a free text query. Example: `123`
  * Specify the `scope` field as this organization in your search request.

  
`displayName` |  `string` The display name of this resource. This field is available only when the resource's Protobuf contains it.To search against the `displayName`:

  * Use a field query. Example: `displayName:"My Instance"`
  * Use a free text query. Example: `"My Instance"`

  
`description` |  `string` One or more paragraphs of text description of this resource. Maximum length could be up to 1M bytes. This field is available only when the resource's Protobuf contains it.To search against the `description`:

  * Use a field query. Example: `description:"important instance"`
  * Use a free text query. Example: `"important instance"`

  
`location` |  `string` Location can be `global`, regional like `us-east1`, or zonal like `us-west1-b`. This field is available only when the resource's Protobuf contains it.To search against the `location`:

  * Use a field query. Example: `location:us-west*`
  * Use a free text query. Example: `us-west*`

  
`labels` |  `map (key: string, value: string)` User labels associated with this resource. See [Labelling and grouping Google Cloud resources](https://cloud.google.com/blog/products/gcp/labelling-and-grouping-your-google-cloud-platform-resources) for more information. This field is available only when the resource's Protobuf contains it.To search against the `labels`:

  * Use a field query: 
    * query on any label's key or value. Example: `labels:prod`
    * query by a given label. Example: `labels.env:prod`
    * query by a given label's existence. Example: `labels.env:*`
  * Use a free text query. Example: `prod`

An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`networkTags[]` |  `string` Network tags associated with this resource. Like labels, network tags are a type of annotations used to group Google Cloud resources. See [Labelling Google Cloud resources](https://cloud.google.com/blog/products/gcp/labelling-and-grouping-your-google-cloud-platform-resources) for more information. This field is available only when the resource's Protobuf contains it.To search against the `networkTags`:

  * Use a field query. Example: `networkTags:internal`
  * Use a free text query. Example: `internal`

  
`kmsKey  
**(deprecated)**` |  `string` This item is deprecated!The Cloud KMS [CryptoKey](https://cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys) name or [CryptoKeyVersion](https://cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions) name.This field only presents for the purpose of backward compatibility. Use the `kmsKeys` field to retrieve Cloud KMS key information. This field is available only when the resource's Protobuf contains it and will only be populated for [these resource types](https://cloud.google.com/asset-inventory/docs/legacy-field-names#resource_types_with_the_to_be_deprecated_kmskey_field) for backward compatible purposes.To search against the `kmsKey`:

  * Use a field query. Example: `kmsKey:key`
  * Use a free text query. Example: `key`

  
`kmsKeys[]` |  `string` The Cloud KMS [CryptoKey](https://cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys) names or [CryptoKeyVersion](https://cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions) names. This field is available only when the resource's Protobuf contains it.To search against the `kmsKeys`:

  * Use a field query. Example: `kmsKeys:key`
  * Use a free text query. Example: `key`

  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The create timestamp of this resource, at which the resource was created. The granularity is in seconds. Timestamp.nanos will always be 0. This field is available only when the resource's Protobuf contains it.To search against `createTime`:

  * Use a field query. 
    * value in seconds since unix epoch. Example: `createTime > 1609459200`
    * value in date string. Example: `createTime > 2021-01-01`
    * value in date-time string (must be quoted). Example: `createTime > "2021-01-01T00:00:00"`

Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The last update timestamp of this resource, at which the resource was last modified or deleted. The granularity is in seconds. Timestamp.nanos will always be 0. This field is available only when the resource's Protobuf contains it.To search against `updateTime`:

  * Use a field query. 
    * value in seconds since unix epoch. Example: `updateTime < 1609459200`
    * value in date string. Example: `updateTime < 2021-01-01`
    * value in date-time string (must be quoted). Example: `updateTime < "2021-01-01T00:00:00"`

Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`state` |  `string` The state of this resource. Different resources types have different state definitions that are mapped from various fields of different resource types. This field is available only when the resource's Protobuf contains it.Example: If the resource is an instance provided by Compute Engine, its state will include PROVISIONING, STAGING, RUNNING, STOPPING, SUSPENDING, SUSPENDED, REPAIRING, and TERMINATED. See `status` definition in [API Reference](https://cloud.google.com/compute/docs/reference/rest/v1/instances). If the resource is a project provided by Resource Manager, its state will include LIFECYCLE_STATE_UNSPECIFIED, ACTIVE, DELETE_REQUESTED and DELETE_IN_PROGRESS. See `lifecycleState` definition in [API Reference](https://cloud.google.com/resource-manager/reference/rest/v1/projects).To search against the `state`:

  * Use a field query. Example: `state:RUNNING`
  * Use a free text query. Example: `RUNNING`

  
`additionalAttributes` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` The additional searchable attributes of this resource. The attributes may vary from one resource type to another. Examples: `projectId` for Project, `dnsName` for DNS ManagedZone. This field contains a subset of the resource metadata fields that are returned by the List or Get APIs provided by the corresponding Google Cloud service (e.g., Compute Engine). see [API references and supported searchable attributes](https://cloud.google.com/asset-inventory/docs/supported-asset-types) to see which fields are included.You can search values of these fields through free text search. However, you should not consume the field programically as the field names and values may change as the Google Cloud service updates to a new incompatible API version.To search against the `additionalAttributes`:

  * Use a free text query to match the attributes values. Example: to search `additionalAttributes = { dnsName: "foobar" }`, you can issue a query `foobar`.

  
`parentFullResourceName` |  `string` The full resource name of this resource's parent, if it has one. To search against the `parentFullResourceName`:

  * Use a field query. Example: `parentFullResourceName:"project-name"`
  * Use a free text query. Example: `project-name`

  
`versionedResources[]` |  `object (`[VersionedResource](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/searchAllResources#VersionedResource)`)` Versioned resource representations of this resource. This is repeated because there could be multiple versions of resource representations during version migration.This `versionedResources` field is not searchable. Some attributes of the resource representations are exposed in `additionalAttributes` field, so as to allow users to search on them.  
`attachedResources[]` |  `object (`[AttachedResource](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/searchAllResources#AttachedResource)`)` Attached resources of this resource. For example, an OSConfig Inventory is an attached resource of a Compute Instance. This field is repeated because a resource could have multiple attached resources.This `attachedResources` field is not searchable. Some attributes of the attached resources are exposed in `additionalAttributes` field, so as to allow users to search on them.  
`relationships` |  `map (key: string, value: object (`[RelatedResources](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/searchAllResources#RelatedResources)`))` A map of related resources of this resource, keyed by the relationship type. A relationship type is in the format of {SourceType}_{ACTION}_{DestType}. Example: `DISK_TO_INSTANCE`, `DISK_TO_NETWORK`, `INSTANCE_TO_INSTANCEGROUP`. See [supported relationship types](https://cloud.google.com/asset-inventory/docs/supported-asset-types#supported_relationship_types).An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`tagKeys[]  
**(deprecated)**` |  `string` This item is deprecated!This field is only present for the purpose of backward compatibility. Use the `tags` field instead.TagKey namespaced names, in the format of {ORG_ID}/{TAG_KEY_SHORT_NAME}. To search against the `tagKeys`:

  * Use a field query. Example:
    * `tagKeys:"123456789/env*"`
    * `tagKeys="123456789/env"`
    * `tagKeys:"env"`
  * Use a free text query. Example:
    * `env`

  
`tagValues[]  
**(deprecated)**` |  `string` This item is deprecated!This field is only present for the purpose of backward compatibility. Use the `tags` field instead.TagValue namespaced names, in the format of {ORG_ID}/{TAG_KEY_SHORT_NAME}/{TAG_VALUE_SHORT_NAME}. To search against the `tagValues`:

  * Use a field query. Example:
    * `tagValues:"env"`
    * `tagValues:"env/prod"`
    * `tagValues:"123456789/env/prod*"`
    * `tagValues="123456789/env/prod"`
  * Use a free text query. Example:
    * `prod`

  
`tagValueIds[]  
**(deprecated)**` |  `string` This item is deprecated!This field is only present for the purpose of backward compatibility. Use the `tags` field instead.TagValue IDs, in the format of tagValues/{TAG_VALUE_ID}. To search against the `tagValueIds`:

  * Use a field query. Example:
    * `tagValueIds="tagValues/456"`
  * Use a free text query. Example:
    * `456`

  
`tags[]` |  `object (`[Tag](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Tag)`)` The tags directly attached to this resource.To search against the `tags`:

  * Use a field query. Example:
    * `tagKeys:"123456789/env*"`
    * `tagKeys="123456789/env"`
    * `tagKeys:"env"`
    * `tagKeyIds="tagKeys/123"`
    * `tagValues:"env"`
    * `tagValues:"env/prod"`
    * `tagValues:"123456789/env/prod*"`
    * `tagValues="123456789/env/prod"`
    * `tagValueIds="tagValues/456"`
  * Use a free text query. Example:
    * `env/prod`

  
`effectiveTags[]` |  `object (`[EffectiveTagDetails](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/EffectiveTagDetails)`)` The effective tags on this resource. All of the tags that are both attached to and inherited by a resource are collectively called the effective tags. For more information, see [tag inheritance](https://cloud.google.com/resource-manager/docs/tags/tags-overview#inheritance).To search against the `effectiveTags`:

  * Use a field query. Example: 
    * `effectiveTagKeys:"123456789/env*"`
    * `effectiveTagKeys="123456789/env"`
    * `effectiveTagKeys:"env"`
    * `effectiveTagKeyIds="tagKeys/123"`
    * `effectiveTagValues:"env"`
    * `effectiveTagValues:"env/prod"`
    * `effectiveTagValues:"123456789/env/prod*"`
    * `effectiveTagValues="123456789/env/prod"`
    * `effectiveTagValueIds="tagValues/456"`

  
`enrichments[]` |  `object (`[AssetEnrichment](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/searchAllResources#AssetEnrichment)`)` Enrichments of the asset. Currently supported enrichment types with v1.searchAllResources API:

  * RESOURCE_OWNERS

The corresponding read masks in order to get the enrichment:

  * enrichments.resource_owners

The corresponding required permissions:

  * cloudasset.assets.searchEnrichmentResourceOwners

Example query to get resource owner enrichment:
    
    
      scope: "projects/my-project"
      query: "name: my-project"
      assetTypes: "cloudresourcemanager.googleapis.com/Project"
      readMask: {
         paths: "assetType"
         paths: "name"
         paths: "enrichments.resource_owners"
      }
      
  
`parentAssetType` |  `string` The type of this resource's immediate parent, if there is one.To search against the `parentAssetType`:

  * Use a field query. Example: `parentAssetType:"cloudresourcemanager.googleapis.com/Project"`
  * Use a free text query. Example: `cloudresourcemanager.googleapis.com/Project`

  
`sccSecurityMarks` |  `map (key: string, value: string)` The actual content of Security Command Center security marks associated with the asset.To search against SCC SecurityMarks field:

  * Use a field query: 
    * query by a given key value pair. Example: `sccSecurityMarks.foo=bar`
    * query by a given key's existence. Example: `sccSecurityMarks.foo:*`

An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
  
## VersionedResource

Resource representation as defined by the corresponding service providing the resource for a given API version.

JSON representation  
---  
      
    
    {
      "version": string,
      "resource": {
        object
      },
      "assetExceptions": [
        {
          object ([AssetException](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/AssetException))
        }
      ]
    }  
  
Fields  
---  
`version` |  `string` API version of the resource.Example: If the resource is an instance provided by Compute Engine v1 API as defined in `https://cloud.google.com/compute/docs/reference/rest/v1/instances`, version will be "v1".  
`resource` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` JSON representation of the resource as defined by the corresponding service providing this resource.Example: If the resource is an instance provided by Compute Engine, this field will contain the JSON representation of the instance as defined by Compute Engine: `https://cloud.google.com/compute/docs/reference/rest/v1/instances`.You can find the resource definition for each supported resource type in this table: `https://cloud.google.com/asset-inventory/docs/supported-asset-types`  
`assetExceptions[]` |  `object (`[AssetException](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/AssetException)`)` The exceptions of a resource.  
  
## AttachedResource

Attached resource representation, which is defined by the corresponding service provider. It represents an attached resource's payload.

JSON representation  
---  
      
    
    {
      "assetType": string,
      "versionedResources": [
        {
          object ([VersionedResource](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/searchAllResources#VersionedResource))
        }
      ]
    }  
  
Fields  
---  
`assetType` |  `string` The type of this attached resource.Example: `osconfig.googleapis.com/Inventory`You can find the supported attached asset types of each resource in this table: `https://cloud.google.com/asset-inventory/docs/supported-asset-types`  
`versionedResources[]` |  `object (`[VersionedResource](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/searchAllResources#VersionedResource)`)` Versioned resource representations of this attached resource. This is repeated because there could be multiple versions of the attached resource representations during version migration.  
  
## RelatedResources

The related resources of the primary resource.

JSON representation  
---  
      
    
    {
      "relatedResources": [
        {
          object ([RelatedResource](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/searchAllResources#RelatedResource))
        }
      ]
    }  
  
Fields  
---  
`relatedResources[]` |  `object (`[RelatedResource](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/searchAllResources#RelatedResource)`)` The detailed related resources of the primary resource.  
  
## RelatedResource

The detailed related resource.

JSON representation  
---  
      
    
    {
      "assetType": string,
      "fullResourceName": string
    }  
  
Fields  
---  
`assetType` |  `string` The type of the asset. Example: `compute.googleapis.com/Instance`  
`fullResourceName` |  `string` The full resource name of the related resource. Example: `//compute.googleapis.com/projects/my_proj_123/zones/instance/instance123`  
  
## AssetEnrichment

The enhanced metadata information for a resource.

JSON representation  
---  
      
    
    {
    
      // Union field EnrichmentData can be only one of the following:
      "resourceOwners": {
        object ([ResourceOwners](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/searchAllResources#ResourceOwners))
      }
      // End of list of possible types for union field EnrichmentData.
    }  
  
Fields  
---  
Union field `EnrichmentData`.`EnrichmentData` can be only one of the following:  
`resourceOwners` |  `object (`[ResourceOwners](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/searchAllResources#ResourceOwners)`)` The resource owners for a resource.Note that this field only contains the members that have "roles/owner" role in the resource's IAM Policy.  
  
## ResourceOwners

The resource owners information.

JSON representation  
---  
      
    
    {
      "resourceOwners": [
        string
      ]
    }  
  
Fields  
---  
`resourceOwners[]` |  `string` List of resource owners.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-11-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-11-12 UTC."],[],[]] 
