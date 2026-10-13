---
url: https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1p7beta1/TopLevel/exportAssets/
title: Method: exportAssets \u00a0|\u00a0 Cloud Asset Inventory \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:30:08.313002+00:00
---

# Method: exportAssets  |  Cloud Asset Inventory  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1p7beta1/TopLevel/exportAssets/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Cloud Asset Inventory ](https://docs.cloud.google.com/asset-inventory/docs)
  * [ Reference ](https://docs.cloud.google.com/asset-inventory/docs/asset-types)



Send feedback 

#  Method: exportAssets Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
  * Authorization scopes
  * ContentType
  * OutputConfig
    * JSON representation
  * GcsDestination
    * JSON representation
  * BigQueryDestination
    * JSON representation
  * PartitionSpec
    * JSON representation
  * PartitionKey
  * Try it!



Exports assets with time and resource types to a given Cloud Storage location/BigQuery table. For Cloud Storage location destinations, the output format is newline-delimited JSON. Each line represents a `google.cloud.asset.v1p7beta1.Asset` in the JSON format; for BigQuery table destinations, the output table stores the fields in asset proto as columns. This API implements the `[google.longrunning.Operation](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/Shared.Types/Operation)` API , which allows you to keep track of the export. We recommend intervals of at least 2 seconds with exponential retry to poll the export operation result. For regular-size resource parent, the export operation usually finishes within 5 minutes.

### HTTP request

`POST https://cloudasset.googleapis.com/v1p7beta1/{parent=*/*}:exportAssets`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The relative name of the root asset. This can only be an organization number (such as "organizations/123"), a project ID (such as "projects/my-project-id"), or a project number (such as "projects/12345"), or a folder number (such as "folders/123"). Authorization requires one or more of the following [IAM](https://cloud.google.com/iam/docs/) permissions on the specified resource `parent`:

  * `cloudasset.assets.exportResource`
  * `cloudasset.assets.exportIamPolicy`

  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "readTime": string,
      "assetTypes": [
        string
      ],
      "contentType": enum ([ContentType](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1p7beta1/TopLevel/exportAssets#ContentType)),
      "outputConfig": {
        object ([OutputConfig](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1p7beta1/TopLevel/exportAssets#OutputConfig))
      },
      "relationshipTypes": [
        string
      ]
    }  
  
Fields  
---  
`readTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Timestamp to take an asset snapshot. This can only be set to a timestamp between the current time and the current time minus 35 days (inclusive). If not specified, the current time will be used. Due to delays in resource data collection and indexing, there is a volatile window during which running the same query may get different results.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`assetTypes[]` |  `string` A list of asset types to take a snapshot for. For example: "compute.googleapis.com/Disk".Regular expressions are also supported. For example:

  * "compute.googleapis.com.*" snapshots resources whose asset type starts with "compute.googleapis.com".
  * ".*Instance" snapshots resources whose asset type ends with "Instance".
  * ".*Instance.*" snapshots resources whose asset type contains "Instance".

See [RE2](https://github.com/google/re2/wiki/Syntax) for all supported regular expression syntax. If the regular expression does not match any supported asset type, an INVALID_ARGUMENT error will be returned.If specified, only matching assets will be returned, otherwise, it will snapshot all asset types. See [Introduction to Cloud Asset Inventory](https://cloud.google.com/asset-inventory/docs/overview) for all supported asset types.  
`contentType` |  `enum (`[ContentType](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1p7beta1/TopLevel/exportAssets#ContentType)`)` Asset content type. If not specified, no content but the asset name will be returned.  
`outputConfig` |  `object (`[OutputConfig](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1p7beta1/TopLevel/exportAssets#OutputConfig)`)` Required. Output configuration indicating where the results will be output to.  
`relationshipTypes[]` |  `string` A list of relationship types to export, for example: `INSTANCE_TO_INSTANCEGROUP`. This field should only be specified if contentType=RELATIONSHIP. If specified, it will snapshot [assetTypes]' specified relationships, or give errors if any relationshipTypes' supported types are not in [assetTypes]. If not specified, it will snapshot all [assetTypes]' supported relationships. An unspecified [assetTypes] field means all supported assetTypes. See [Introduction to Cloud Asset Inventory](https://cloud.google.com/asset-inventory/docs/overview) for all supported asset types and relationship types.  
  
### Response body

If successful, the response body contains an instance of `[Operation](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/Shared.Types/Operation)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

## ContentType

Asset content type.

Enums  
---  
`CONTENT_TYPE_UNSPECIFIED` | Unspecified content type.  
`RESOURCE` | Resource metadata.  
`IAM_POLICY` | The actual IAM policy set on a resource.  
`ORG_POLICY` | The organization policy set on an asset.  
`ACCESS_POLICY` | The Access Context Manager policy set on an asset.  
`RELATIONSHIP` | The related resources.  
  
## OutputConfig

Output configuration for export assets destination.

JSON representation  
---  
      
    
    {
    
      // Union field destination can be only one of the following:
      "gcsDestination": {
        object ([GcsDestination](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1p7beta1/TopLevel/exportAssets#GcsDestination))
      },
      "bigqueryDestination": {
        object ([BigQueryDestination](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1p7beta1/TopLevel/exportAssets#BigQueryDestination))
      }
      // End of list of possible types for union field destination.
    }  
  
Fields  
---  
Union field `destination`. Asset export destination. `destination` can be only one of the following:  
`gcsDestination` |  `object (`[GcsDestination](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1p7beta1/TopLevel/exportAssets#GcsDestination)`)` Destination on Cloud Storage.  
`bigqueryDestination` |  `object (`[BigQueryDestination](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1p7beta1/TopLevel/exportAssets#BigQueryDestination)`)` Destination on BigQuery. The output table stores the fields in asset proto as columns in BigQuery.  
  
## GcsDestination

A Cloud Storage location.

JSON representation  
---  
      
    
    {
    
      // Union field object_uri can be only one of the following:
      "uri": string,
      "uriPrefix": string
      // End of list of possible types for union field object_uri.
    }  
  
Fields  
---  
Union field `object_uri`. Required. `object_uri` can be only one of the following:  
`uri` |  `string` The URI of the Cloud Storage object. It's the same URI that is used by gcloud storage. Example: "gs://bucket_name/object_name". See [Viewing and Editing Object Metadata](https://cloud.google.com/storage/docs/viewing-editing-metadata) for more information.  
`uriPrefix` |  `string` The URI prefix of all generated Cloud Storage objects. Example: "gs://bucket_name/object_name_prefix". Each object URI is in format: "gs://bucket_name/object_name_prefix/{ASSET_TYPE}/{SHARD_NUMBER} and only contains assets for that type.  starts from 0. Example: "gs://bucket_name/object_name_prefix/compute.googleapis.com/Disk/0" is the first shard of output objects containing all compute.googleapis.com/Disk assets. An INVALID_ARGUMENT error will be returned if file with the same name "gs://bucket_name/object_name_prefix" already exists.  
  
## BigQueryDestination

A BigQuery destination for exporting assets to.

JSON representation  
---  
      
    
    {
      "dataset": string,
      "table": string,
      "force": boolean,
      "partitionSpec": {
        object ([PartitionSpec](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1p7beta1/TopLevel/exportAssets#PartitionSpec))
      },
      "separateTablesPerAssetType": boolean
    }  
  
Fields  
---  
`dataset` |  `string` Required. The BigQuery dataset in format "projects/projectId/datasets/datasetId", to which the snapshot result should be exported. If this dataset does not exist, the export call returns an INVALID_ARGUMENT error.  
`table` |  `string` Required. The BigQuery table to which the snapshot result should be written. If this table does not exist, a new table with the given name will be created.  
`force` |  `boolean` If the destination table already exists and this flag is `TRUE`, the table will be overwritten by the contents of assets snapshot. If the flag is `FALSE` or unset and the destination table already exists, the export call returns an INVALID_ARGUMENT error.  
`partitionSpec` |  `object (`[PartitionSpec](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1p7beta1/TopLevel/exportAssets#PartitionSpec)`)` [partitionSpec] determines whether to export to partitioned table(s) and how to partition the data.If [partitionSpec] is unset or [partitionSpec.partition_key] is unset or `PARTITION_KEY_UNSPECIFIED`, the snapshot results will be exported to non-partitioned table(s). [force] will decide whether to overwrite existing table(s).If [partitionSpec] is specified. First, the snapshot results will be written to partitioned table(s) with two additional timestamp columns, readTime and requestTime, one of which will be the partition key. Secondly, in the case when any destination table already exists, it will first try to update existing table's schema as necessary by appending additional columns. Then, if [force] is `TRUE`, the corresponding partition will be overwritten by the snapshot results (data in different partitions will remain intact); if [force] is unset or `FALSE`, it will append the data. An error will be returned if the schema update or data appension fails.  
`separateTablesPerAssetType` |  `boolean` If this flag is `TRUE`, the snapshot results will be written to one or multiple tables, each of which contains results of one asset type. The [force] and [partitionSpec] fields will apply to each of them.Field [table] will be concatenated with "_" and the asset type names (see <https://cloud.google.com/asset-inventory/docs/supported-asset-types> for supported asset types) to construct per-asset-type table names, in which all non-alphanumeric characters like "." and "/" will be substituted by "_". Example: if field [table] is "mytable" and snapshot results contain "storage.googleapis.com/Bucket" assets, the corresponding table name will be "mytable_storage_googleapis_com_Bucket". If any of these tables does not exist, a new table with the concatenated name will be created.When [contentType] in the ExportAssetsRequest is `RESOURCE`, the schema of each table will include RECORD-type columns mapped to the nested fields in the Asset.resource.data field of that asset type (up to the 15 nested level BigQuery supports (<https://cloud.google.com/bigquery/docs/nested-repeated#limitations))>. The fields in >15 nested levels will be stored in JSON format string as a child column of its parent RECORD column.If error occurs when exporting to any table, the whole export call will return an error but the export results that already succeed will persist. Example: if exporting to table_type_A succeeds when exporting to table_type_B fails during one export call, the results in table_type_A will persist and there will not be partial results persisting in a table.  
  
## PartitionSpec

Specifications of BigQuery partitioned table as export destination.

JSON representation  
---  
      
    
    {
      "partitionKey": enum ([PartitionKey](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1p7beta1/TopLevel/exportAssets#PartitionKey))
    }  
  
Fields  
---  
`partitionKey` |  `enum (`[PartitionKey](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1p7beta1/TopLevel/exportAssets#PartitionKey)`)` The partition key for BigQuery partitioned table.  
  
## PartitionKey

This enum is used to determine the partition key column when exporting assets to BigQuery partitioned table(s). Note that, if the partition key is a timestamp column, the actual partition is based on its date value (expressed in UTC. see details in <https://cloud.google.com/bigquery/docs/partitioned-tables#date_timestamp_partitioned_tables)>.

Enums  
---  
`PARTITION_KEY_UNSPECIFIED` | Unspecified partition key. If used, it means using non-partitioned table.  
`READ_TIME` | The time when the snapshot is taken. If specified as partition key, the result table(s) is partitioned by the additional timestamp column, readTime. If [readTime] in ExportAssetsRequest is specified, the readTime column's value will be the same as it. Otherwise, its value will be the current time that is used to take the snapshot.  
`REQUEST_TIME` | The time when the request is received and started to be processed. If specified as partition key, the result table(s) is partitioned by the requestTime column, an additional timestamp column representing when the request was received.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-24 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-24 UTC."],[],[]] 
