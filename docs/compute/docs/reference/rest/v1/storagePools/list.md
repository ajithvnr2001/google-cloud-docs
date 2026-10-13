---
url: https://docs.cloud.google.com/compute/docs/reference/rest/v1/storagePools/list/
title: Method: storagePools.list \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:56:59.796480+00:00
---

# Method: storagePools.list  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/reference/rest/v1/storagePools/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ APIs & Reference ](https://docs.cloud.google.com/compute/docs/apis)



Send feedback 

#  Method: storagePools.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
      * JSON representation
      * JSON representation
      * JSON representation
      * JSON representation
      * JSON representation
      * JSON representation
  * Authorization scopes
  * IAM Permissions
  * Try it!



Retrieves a list of storage pools contained within the specified zone.

### HTTP request

Choose an endpoint:

globalafrica-south1asia-east1asia-east2asia-northeast1asia-northeast2asia-northeast3asia-south1asia-south2asia-southeast1asia-southeast2asia-southeast3australia-southeast1australia-southeast2europe-central2europe-north1europe-north2europe-southwest1europe-west1europe-west10europe-west12europe-west2europe-west3europe-west4europe-west6europe-west8europe-west9me-central1me-central2me-west1northamerica-northeast1northamerica-northeast2northamerica-south1southamerica-east1southamerica-west1us-central1us-east1us-east4us-east5us-south1us-west1us-west2us-west3us-west4

  
`GET https://compute.googleapis.com/compute/v1/projects/{project}/zones/{zone}/storagePools`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`project` |  `string` Project ID for this request.  
`zone` |  `string` The name of the zone for this request.  
  
### Query parameters

Parameters  
---  
`maxResults` |  `integer ([uint32](https://developers.google.com/discovery/v1/type-format) format)` The maximum number of results per page that should be returned. If the number of available results is larger than `maxResults`, Compute Engine returns a `nextPageToken` that can be used to get the next page of results in subsequent list requests. Acceptable values are `0` to `500`, inclusive. (Default: `500`)  
`pageToken` |  `string` Specifies a page token to use. Set `pageToken` to the `nextPageToken` returned by a previous list request to get the next page of results.  
`filter` |  `string` A filter expression that filters resources listed in the response. Most Compute resources support two types of filter expressions: expressions that support regular expressions and expressions that follow API improvement proposal [AIP-160](https://google.aip.dev/160). These two types of filter expressions cannot be mixed in one request.If you want to use AIP-160, your expression must specify the field name, an operator, and the value that you want to use for filtering. The value must be a string, a number, or a boolean. The operator must be either `=`, `!=`, `>`, `<`, `<=`, `>=` or `:`.For example, if you are filtering Compute Engine instances, you can exclude instances named `example-instance` by specifying `name != example-instance`.The `:*` comparison can be used to test whether a key has been defined. For example, to find all objects with `owner` label use:
    
    
    labels.owner:*
    

You can also filter nested fields. For example, you could specify `scheduling.automaticRestart = false` to include instances only if they are not scheduled for automatic restarts. You can use filtering on nested fields to filter based on [resource labels](https://docs.cloud.google.com/compute/docs/labeling-resources).To filter on multiple expressions, provide each separate expression within parentheses. For example:
    
    
    (scheduling.automaticRestart = true)
    (cpuPlatform = "Intel Skylake")
    

By default, each expression is an `AND` expression. However, you can include `AND` and `OR` expressions explicitly. For example:
    
    
    (cpuPlatform = "Intel Skylake") OR
    (cpuPlatform = "Intel Broadwell") AND
    (scheduling.automaticRestart = true)
    

If you want to use a regular expression, use the `eq` (equal) or `ne` (not equal) operator against a single un-parenthesized expression with or without quotes or against multiple parenthesized expressions. Examples:`fieldname eq unquoted literal` `fieldname eq 'single quoted literal'` `fieldname eq "double quoted literal"` `(fieldname1 eq literal) (fieldname2 ne "literal")`The literal value is interpreted as a regular expression using Google [RE2](https://github.com/google/re2/wiki/Syntax) library syntax. The literal value must match the entire field.For example, to filter for instances that do not end with name "instance", you would use `name ne .*instance`.You cannot combine constraints on multiple fields using regular expressions.  
`orderBy` |  `string` Sorts list results by a certain order. By default, results are returned in alphanumerical order based on the resource name.You can also sort results in descending order based on the creation timestamp using `orderBy="creationTimestamp desc"`. This sorts results based on the `creationTimestamp` field in reverse chronological order (newest result first). Use this to sort resources like operations so that the newest operation is returned first.Currently, only sorting by `name` or `creationTimestamp desc` is supported.  
`returnPartialSuccess` |  `boolean` Opt-in for partial success behavior which provides partial results in case of failure. The default value is false.For example, when partial success behavior is enabled, aggregatedList for a single zone scope either returns all resources in the zone or no resources, with an error code.  
  
### Request body

The request body must be empty.

### Response body

A list of StoragePool resources.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "kind": string,
      "id": string,
      "items": [
        {
          "kind": string,
          "id": string,
          "creationTimestamp": string,
          "name": string,
          "description": string,
          "poolProvisionedCapacityGb": string,
          "poolProvisionedIops": string,
          "poolProvisionedThroughput": string,
          "zone": string,
          "state": enum,
          "selfLink": string,
          "selfLinkWithId": string,
          "labels": {
            string: string,
            ...
          },
          "labelFingerprint": string,
          "resourceStatus": {
            "lastResizeTimestamp": string,
            "diskCount": string,
            "poolUsedCapacityBytes": string,
            "poolUserWrittenBytes": string,
            "totalProvisionedDiskCapacityGb": string,
            "maxTotalProvisionedDiskCapacityGb": string,
            "poolUsedIops": string,
            "totalProvisionedDiskIops": string,
            "poolUsedThroughput": string,
            "totalProvisionedDiskThroughput": string,
            "exapoolMaxReadIops": string,
            "exapoolMaxWriteIops": string,
            "exapoolMaxReadThroughput": string,
            "exapoolMaxWriteThroughput": string
          },
          "storagePoolType": string,
          "status": {
            "lastResizeTimestamp": string,
            "diskCount": string,
            "poolUsedCapacityBytes": string,
            "poolUserWrittenBytes": string,
            "totalProvisionedDiskCapacityGb": string,
            "maxTotalProvisionedDiskCapacityGb": string,
            "poolUsedIops": string,
            "totalProvisionedDiskIops": string,
            "poolUsedThroughput": string,
            "totalProvisionedDiskThroughput": string,
            "exapoolMaxReadIops": string,
            "exapoolMaxWriteIops": string,
            "exapoolMaxReadThroughput": string,
            "exapoolMaxWriteThroughput": string
          },
          "capacityProvisioningType": enum,
          "performanceProvisioningType": enum,
          "exapoolProvisionedCapacityGb": {
            "writeOptimized": string,
            "readOptimized": string,
            "capacityOptimized": string
          },
          "shareSettings": {
            "projectMap": {
              string: {
                "projectId": string
              },
              ...
            }
          },
          "params": {
            "resourceManagerTags": {
              string: string,
              ...
            }
          }
        }
      ],
      "nextPageToken": string,
      "selfLink": string,
      "warning": {
        "code": enum,
        "message": string,
        "data": [
          {
            "key": string,
            "value": string
          }
        ]
      },
      "etag": string,
      "unreachables": [
        string
      ]
    }  
  
Fields  
---  
`kind` |  `string` Output only. Type of resource. Always `compute#storagePoolList` for lists of storagePools.  
`id` |  `string` Output only. Unique identifier for the resource; defined by the server.  
`items[]` |  `object` A list of StoragePool resources.  
`items[].kind` |  `string` Output only. Type of the resource. Always `compute#storagePool` for storage pools.  
`items[].id` |  `string ([uint64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The unique identifier for the resource. This identifier is defined by the server.  
`items[].creationTimestamp` |  `string` Output only. Creation timestamp in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format.  
`items[].name` |  `string` Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with [RFC1035](https://www.ietf.org/rfc/rfc1035.txt). Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.  
`items[].description` |  `string` An optional description of this resource. Provide this property when you create the resource.  
`items[].poolProvisionedCapacityGb` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Size of the storage pool in GiB. For more information about the size limits, see <https://cloud.google.com/compute/docs/disks/storage-pools>.  
`items[].poolProvisionedIops` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Provisioned IOPS of the storage pool. Only relevant if the storage pool type is hyperdisk-balanced.  
`items[].poolProvisionedThroughput` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Provisioned throughput of the storage pool in MiB/s. Only relevant if the storage pool type is hyperdisk-balanced or hyperdisk-throughput.  
`items[].zone` |  `string` Output only. URL of the zone where the storage pool resides. You must specify this field as part of the HTTP request URL. It is not settable as a field in the request body.  
`items[].state` |  `enum` Output only. The status of storage pool creation. 

  * `CREATING`: Storage pool is provisioning.
storagePool. 
  * `FAILED`: Storage pool creation failed.
  * `READY`: Storage pool is ready for use.
  * `DELETING`: Storage pool is deleting.

  
`items[].selfLink` |  `string` Output only. Server-defined fully-qualified URL for this resource.  
`items[].selfLinkWithId` |  `string` Output only. Server-defined URL for this resource's resource id.  
`items[].labels` |  `map (key: string, value: string)` Labels to apply to this storage pool. These can be later modified by the `setLabels` method.  
`items[].labelFingerprint` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` A fingerprint for the labels being applied to this storage pool, which is essentially a hash of the labels set used for optimistic locking. The fingerprint is initially generated by Compute Engine and changes after every request to modify or update labels. You must always provide an up-to-date fingerprint hash in order to update or change labels, otherwise the request will fail with error `412 conditionNotMet`.To see the latest fingerprint, make a `get()` request to retrieve a storage pool.A base64-encoded string.  
`items[].resourceStatus` |  `object` Output only. Status information for the storage pool resource.  
`items[].resourceStatus.lastResizeTimestamp` |  `string` Output only. Timestamp of the last successful resize in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format.  
`items[].resourceStatus.diskCount` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. Number of disks used.  
`items[].resourceStatus.poolUsedCapacityBytes` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. Space used by data stored in disks within the storage pool (in bytes). This will reflect the total number of bytes written to the disks in the pool, in contrast to the capacity of those disks.  
`items[].resourceStatus.poolUserWrittenBytes` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. Amount of data written into the pool, before it is compacted.  
`items[].resourceStatus.totalProvisionedDiskCapacityGb` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. Sum of all the disks' provisioned capacity (in GiB) in this storage pool. A disk's provisioned capacity is the same as its total capacity.  
`items[].resourceStatus.maxTotalProvisionedDiskCapacityGb` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. Maximum allowed aggregate disk size in GiB.  
`items[].resourceStatus.poolUsedIops` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. Sum of all the disks' provisioned IOPS, minus some amount that is allowed per disk that is not counted towards pool's IOPS capacity. For more information, see <https://cloud.google.com/compute/docs/disks/storage-pools>.  
`items[].resourceStatus.totalProvisionedDiskIops` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. Sum of all the disks' provisioned IOPS.  
`items[].resourceStatus.poolUsedThroughput` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. Sum of all the disks' provisioned throughput in MiB/s.  
`items[].resourceStatus.totalProvisionedDiskThroughput` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. Sum of all the disks' provisioned throughput in MiB/s, minus some amount that is allowed per disk that is not counted towards pool's throughput capacity.  
`items[].resourceStatus.exapoolMaxReadIops` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. Maximum allowed read IOPS for this Exapool.  
`items[].resourceStatus.exapoolMaxWriteIops` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. Maximum allowed write IOPS for this Exapool.  
`items[].resourceStatus.exapoolMaxReadThroughput` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. Maximum allowed read throughput in MiB/s for this Exapool.  
`items[].resourceStatus.exapoolMaxWriteThroughput` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. Maximum allowed write throughput in MiB/s for this Exapool.  
`items[].storagePoolType` |  `string` Type of the storage pool.  
`items[].status` |  `object` Output only. Status information for the storage pool resource.  
`items[].status.lastResizeTimestamp` |  `string` Output only. Timestamp of the last successful resize in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format.  
`items[].status.diskCount` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. Number of disks used.  
`items[].status.poolUsedCapacityBytes` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. Space used by data stored in disks within the storage pool (in bytes). This will reflect the total number of bytes written to the disks in the pool, in contrast to the capacity of those disks.  
`items[].status.poolUserWrittenBytes` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. Amount of data written into the pool, before it is compacted.  
`items[].status.totalProvisionedDiskCapacityGb` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. Sum of all the disks' provisioned capacity (in GiB) in this storage pool. A disk's provisioned capacity is the same as its total capacity.  
`items[].status.maxTotalProvisionedDiskCapacityGb` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. Maximum allowed aggregate disk size in GiB.  
`items[].status.poolUsedIops` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. Sum of all the disks' provisioned IOPS, minus some amount that is allowed per disk that is not counted towards pool's IOPS capacity. For more information, see <https://cloud.google.com/compute/docs/disks/storage-pools>.  
`items[].status.totalProvisionedDiskIops` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. Sum of all the disks' provisioned IOPS.  
`items[].status.poolUsedThroughput` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. Sum of all the disks' provisioned throughput in MiB/s.  
`items[].status.totalProvisionedDiskThroughput` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. Sum of all the disks' provisioned throughput in MiB/s, minus some amount that is allowed per disk that is not counted towards pool's throughput capacity.  
`items[].status.exapoolMaxReadIops` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. Maximum allowed read IOPS for this Exapool.  
`items[].status.exapoolMaxWriteIops` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. Maximum allowed write IOPS for this Exapool.  
`items[].status.exapoolMaxReadThroughput` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. Maximum allowed read throughput in MiB/s for this Exapool.  
`items[].status.exapoolMaxWriteThroughput` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. Maximum allowed write throughput in MiB/s for this Exapool.  
`items[].capacityProvisioningType` |  `enum` Provisioning type of the byte capacity of the pool.  
`items[].performanceProvisioningType` |  `enum` Provisioning type of the performance-related parameters of the pool, such as throughput and IOPS.  
`items[].exapoolProvisionedCapacityGb` |  `object` Provisioned capacities for each SKU for this Exapool in GiB  
`items[].exapoolProvisionedCapacityGb.writeOptimized` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Size, in GiB, of provisioned write-optimized capacity for this Exapool  
`items[].exapoolProvisionedCapacityGb.readOptimized` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Size, in GiB, of provisioned read-optimized capacity for this Exapool  
`items[].exapoolProvisionedCapacityGb.capacityOptimized` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Size, in GiB, of provisioned capacity-optimized capacity for this Exapool  
`items[].shareSettings` |  `object` Share settings for the storage pool.  
`items[].shareSettings.projectMap[]` |  `map (key: string, value: object)` A map of project id and project config.  
`items[].shareSettings.projectMap[].projectId` |  `string` The project ID, should be same as the key of this project config in the parent map.  
`items[].params` |  `object` Input only. Additional params passed with the request, but not persisted as part of resource payload.  
`items[].params.resourceManagerTags` |  `map (key: string, value: string)` Input only. Resource manager tags to be bound to the storage pool. Tag keys and values have the same definition as [resource manager tags](https://cloud.google.com/resource-manager/docs/tags/tags-overview). Keys and values can be either in numeric format, such as `tagKeys/{tag_key_id}` and `tagValues/{tag_value_id}` or in namespaced format such as `{org_id|projectId}/{tag_key_short_name}` and `{tag_value_short_name}`. The field is ignored (both PUT & PATCH) when empty.  
`nextPageToken` |  `string` Output only. This token allows you to get the next page of results for list requests. If the number of results is larger than `maxResults`, use the `nextPageToken` as a value for the query parameter `pageToken` in the next list request. Subsequent list requests will have their own `nextPageToken` to continue paging through the results.  
`selfLink` |  `string` Output only. Server-defined URL for this resource.  
`warning` |  `object` Output only. Informational warning message.  
`warning.code` |  `enum` Output only. A warning code, if applicable. For example, Compute Engine returns `NO_RESULTS_ON_PAGE` if there are no results in the response.  
`warning.message` |  `string` Output only. A human-readable description of the warning code.  
`warning.data[]` |  `object` Output only. Metadata about this warning in `key: value` format. For example: 
    
    
    "data": [  {  "key": "scope",  "value": "zones/us-east1-d"  }]  
  
`warning.data[].key` |  `string` Output only. A key that provides more detail on the warning being returned. For example, for warnings where there are no results in a list request for a particular zone, this key might be `scope` and the key value might be the zone name. Other examples might be a key indicating a deprecated resource and a suggested replacement, or a warning about invalid network settings (for example, if an instance attempts to perform IP forwarding but is not enabled for IP forwarding).  
`warning.data[].value` |  `string` Output only. A warning data value corresponding to the key.  
`etag` |  `string`  
`unreachables[]` |  `string` Output only. Unreachable resources. end_interface: MixerListResponseWithEtagBuilder  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/compute.readonly`
  * ` https://www.googleapis.com/auth/compute`
  * ` https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

In addition to any permissions specified on the fields above, authorization requires one or more of the following [IAM](https://cloud.google.com/iam/docs/) permissions:

  * `compute.storagePools.list`



To find predefined roles that contain those permissions, see [Compute Engine IAM Roles](https://docs.cloud.google.com/compute/docs/access/iam).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-28 UTC."],[],[]] 
