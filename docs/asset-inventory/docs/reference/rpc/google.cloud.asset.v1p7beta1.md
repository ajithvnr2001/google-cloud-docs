---
url: https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1p7beta1
title: Package google.cloud.asset.v1p7beta1 \u00a0|\u00a0 Cloud Asset Inventory \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:30:10.498893+00:00
---

# Package google.cloud.asset.v1p7beta1  |  Cloud Asset Inventory  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1p7beta1

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Cloud Asset Inventory ](https://docs.cloud.google.com/asset-inventory/docs)
  * [ Reference ](https://docs.cloud.google.com/asset-inventory/docs/asset-types)



Send feedback 

#  Package google.cloud.asset.v1p7beta1 Stay organized with collections  Save and categorize content based on your preferences. 

## Index

  * `[AssetService](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1p7beta1#google.cloud.asset.v1p7beta1.AssetService)` (interface)
  * `[Asset](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1p7beta1#google.cloud.asset.v1p7beta1.Asset)` (message)
  * `[BigQueryDestination](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1p7beta1#google.cloud.asset.v1p7beta1.BigQueryDestination)` (message)
  * `[ContentType](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1p7beta1#google.cloud.asset.v1p7beta1.ContentType)` (enum)
  * `[ExportAssetsRequest](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1p7beta1#google.cloud.asset.v1p7beta1.ExportAssetsRequest)` (message)
  * `[ExportAssetsResponse](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1p7beta1#google.cloud.asset.v1p7beta1.ExportAssetsResponse)` (message)
  * `[GcsDestination](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1p7beta1#google.cloud.asset.v1p7beta1.GcsDestination)` (message)
  * `[GcsOutputResult](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1p7beta1#google.cloud.asset.v1p7beta1.GcsOutputResult)` (message)
  * `[OutputConfig](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1p7beta1#google.cloud.asset.v1p7beta1.OutputConfig)` (message)
  * `[OutputResult](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1p7beta1#google.cloud.asset.v1p7beta1.OutputResult)` (message)
  * `[PartitionSpec](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1p7beta1#google.cloud.asset.v1p7beta1.PartitionSpec)` (message)
  * `[PartitionSpec.PartitionKey](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1p7beta1#google.cloud.asset.v1p7beta1.PartitionSpec.PartitionKey)` (enum)
  * `[RelatedAsset](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1p7beta1#google.cloud.asset.v1p7beta1.RelatedAsset)` (message)
  * `[RelatedAssets](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1p7beta1#google.cloud.asset.v1p7beta1.RelatedAssets)` (message)
  * `[RelationshipAttributes](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1p7beta1#google.cloud.asset.v1p7beta1.RelationshipAttributes)` (message)
  * `[Resource](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1p7beta1#google.cloud.asset.v1p7beta1.Resource)` (message)



## AssetService

Asset service definition.

ExportAssets  
---  
` rpc ExportAssets(`[ExportAssetsRequest](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1p7beta1#google.cloud.asset.v1p7beta1.ExportAssetsRequest)`) returns (`[Operation](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.longrunning#google.longrunning.Operation)`) ` Exports assets with time and resource types to a given Cloud Storage location/BigQuery table. For Cloud Storage location destinations, the output format is newline-delimited JSON. Each line represents a `[google.cloud.asset.v1p7beta1.Asset](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1p7beta1#google.cloud.asset.v1p7beta1.Asset)` in the JSON format; for BigQuery table destinations, the output table stores the fields in asset proto as columns. This API implements the `[google.longrunning.Operation](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.longrunning#google.longrunning.Operation)` API , which allows you to keep track of the export. We recommend intervals of at least 2 seconds with exponential retry to poll the export operation result. For regular-size resource parent, the export operation usually finishes within 5 minutes.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
  
## Asset

An asset in Google Cloud. An asset can be any resource in the Google Cloud [resource hierarchy](https://cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy), a resource outside the Google Cloud resource hierarchy (such as Google Kubernetes Engine clusters and objects), or a policy (e.g. IAM policy). See [Supported asset types](https://cloud.google.com/asset-inventory/docs/supported-asset-types) for more information.

Fields  
---  
`update_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` The last update timestamp of an asset. update_time is updated when create/update/delete operation is performed.  
`name` |  `string` The full name of the asset. Example: `//compute.googleapis.com/projects/my_project_123/zones/zone1/instances/instance1`See [Resource names](https://cloud.google.com/apis/design/resource_names#full_resource_name) for more information.  
`asset_type` |  `string` The type of the asset. Example: `compute.googleapis.com/Disk`See [Supported asset types](https://cloud.google.com/asset-inventory/docs/supported-asset-types) for more information.  
`resource` |  `[Resource](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1p7beta1#google.cloud.asset.v1p7beta1.Resource)` A representation of the resource.  
`iam_policy` |  `[Policy](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.iam.v1#google.iam.v1.Policy)` A representation of the IAM policy set on a Google Cloud resource. There can be a maximum of one IAM policy set on any given resource. In addition, IAM policies inherit their granted access scope from any policies set on parent resources in the resource hierarchy. Therefore, the effectively policy is the union of both the policy set on this resource and each policy set on all of the resource's ancestry resource levels in the hierarchy. See [this topic](https://cloud.google.com/iam/help/allow-policies/inheritance) for more information.  
`org_policy[]` |  `[Policy](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.orgpolicy.v1#google.cloud.orgpolicy.v1.Policy)` A representation of an [organization policy](https://cloud.google.com/resource-manager/docs/organization-policy/overview#organization_policy). There can be more than one organization policy with different constraints set on a given resource.  
`related_assets` |  `[RelatedAssets](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1p7beta1#google.cloud.asset.v1p7beta1.RelatedAssets)` The related assets of the asset of one relationship type. One asset only represents one type of relationship.  
`ancestors[]` |  `string` The ancestry path of an asset in Google Cloud [resource hierarchy](https://cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy), represented as a list of relative resource names. An ancestry path starts with the closest ancestor in the hierarchy and ends at root. If the asset is a project, folder, or organization, the ancestry path starts from the asset itself.Example: `["projects/123456789", "folders/5432", "organizations/1234"]`  
Union field `access_context_policy`. A representation of an [access policy](https://cloud.google.com/access-context-manager/docs/overview#access-policies). `access_context_policy` can be only one of the following:  
`access_policy` |  `[AccessPolicy](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.identity.accesscontextmanager.v1#google.identity.accesscontextmanager.v1.AccessPolicy)` Please also refer to the [access policy user guide](https://cloud.google.com/access-context-manager/docs/overview#access-policies).  
`access_level` |  `[AccessLevel](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.identity.accesscontextmanager.v1#google.identity.accesscontextmanager.v1.AccessLevel)` Please also refer to the [access level user guide](https://cloud.google.com/access-context-manager/docs/overview#access-levels).  
`service_perimeter` |  `[ServicePerimeter](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.identity.accesscontextmanager.v1#google.identity.accesscontextmanager.v1.ServicePerimeter)` Please also refer to the [service perimeter user guide](https://cloud.google.com/vpc-service-controls/docs/overview).  
  
## BigQueryDestination

A BigQuery destination for exporting assets to.

Fields  
---  
`dataset` |  `string` Required. The BigQuery dataset in format "projects/projectId/datasets/datasetId", to which the snapshot result should be exported. If this dataset does not exist, the export call returns an INVALID_ARGUMENT error.  
`table` |  `string` Required. The BigQuery table to which the snapshot result should be written. If this table does not exist, a new table with the given name will be created.  
`force` |  `bool` If the destination table already exists and this flag is `TRUE`, the table will be overwritten by the contents of assets snapshot. If the flag is `FALSE` or unset and the destination table already exists, the export call returns an INVALID_ARGUMENT error.  
`partition_spec` |  `[PartitionSpec](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1p7beta1#google.cloud.asset.v1p7beta1.PartitionSpec)` [partition_spec] determines whether to export to partitioned table(s) and how to partition the data.If [partition_spec] is unset or [partition_spec.partition_key] is unset or `PARTITION_KEY_UNSPECIFIED`, the snapshot results will be exported to non-partitioned table(s). [force] will decide whether to overwrite existing table(s).If [partition_spec] is specified. First, the snapshot results will be written to partitioned table(s) with two additional timestamp columns, readTime and requestTime, one of which will be the partition key. Secondly, in the case when any destination table already exists, it will first try to update existing table's schema as necessary by appending additional columns. Then, if [force] is `TRUE`, the corresponding partition will be overwritten by the snapshot results (data in different partitions will remain intact); if [force] is unset or `FALSE`, it will append the data. An error will be returned if the schema update or data appension fails.  
`separate_tables_per_asset_type` |  `bool` If this flag is `TRUE`, the snapshot results will be written to one or multiple tables, each of which contains results of one asset type. The [force] and [partition_spec] fields will apply to each of them.Field [table] will be concatenated with "_" and the asset type names (see <https://cloud.google.com/asset-inventory/docs/supported-asset-types> for supported asset types) to construct per-asset-type table names, in which all non-alphanumeric characters like "." and "/" will be substituted by "_". Example: if field [table] is "mytable" and snapshot results contain "storage.googleapis.com/Bucket" assets, the corresponding table name will be "mytable_storage_googleapis_com_Bucket". If any of these tables does not exist, a new table with the concatenated name will be created.When [content_type] in the ExportAssetsRequest is `RESOURCE`, the schema of each table will include RECORD-type columns mapped to the nested fields in the Asset.resource.data field of that asset type (up to the 15 nested level BigQuery supports (<https://cloud.google.com/bigquery/docs/nested-repeated#limitations))>. The fields in >15 nested levels will be stored in JSON format string as a child column of its parent RECORD column.If error occurs when exporting to any table, the whole export call will return an error but the export results that already succeed will persist. Example: if exporting to table_type_A succeeds when exporting to table_type_B fails during one export call, the results in table_type_A will persist and there will not be partial results persisting in a table.  
  
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
  
## ExportAssetsRequest

Export asset request.

Fields  
---  
`parent` |  `string` Required. The relative name of the root asset. This can only be an organization number (such as "organizations/123"), a project ID (such as "projects/my-project-id"), or a project number (such as "projects/12345"), or a folder number (such as "folders/123"). Authorization requires one or more of the following [IAM](https://cloud.google.com/iam/docs/) permissions on the specified resource `parent`:

  * `cloudasset.assets.exportResource`
  * `cloudasset.assets.exportIamPolicy`

  
`read_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Timestamp to take an asset snapshot. This can only be set to a timestamp between the current time and the current time minus 35 days (inclusive). If not specified, the current time will be used. Due to delays in resource data collection and indexing, there is a volatile window during which running the same query may get different results.  
`asset_types[]` |  `string` A list of asset types to take a snapshot for. For example: "compute.googleapis.com/Disk".Regular expressions are also supported. For example:

  * "compute.googleapis.com.*" snapshots resources whose asset type starts with "compute.googleapis.com".
  * ".*Instance" snapshots resources whose asset type ends with "Instance".
  * ".*Instance.*" snapshots resources whose asset type contains "Instance".

See [RE2](https://github.com/google/re2/wiki/Syntax) for all supported regular expression syntax. If the regular expression does not match any supported asset type, an INVALID_ARGUMENT error will be returned.If specified, only matching assets will be returned, otherwise, it will snapshot all asset types. See [Introduction to Cloud Asset Inventory](https://cloud.google.com/asset-inventory/docs/overview) for all supported asset types.  
`content_type` |  `[ContentType](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1p7beta1#google.cloud.asset.v1p7beta1.ContentType)` Asset content type. If not specified, no content but the asset name will be returned.  
`output_config` |  `[OutputConfig](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1p7beta1#google.cloud.asset.v1p7beta1.OutputConfig)` Required. Output configuration indicating where the results will be output to.  
`relationship_types[]` |  `string` A list of relationship types to export, for example: `INSTANCE_TO_INSTANCEGROUP`. This field should only be specified if content_type=RELATIONSHIP. If specified, it will snapshot [asset_types]' specified relationships, or give errors if any relationship_types' supported types are not in [asset_types]. If not specified, it will snapshot all [asset_types]' supported relationships. An unspecified [asset_types] field means all supported asset_types. See [Introduction to Cloud Asset Inventory](https://cloud.google.com/asset-inventory/docs/overview) for all supported asset types and relationship types.  
  
## ExportAssetsResponse

The export asset response. This message is returned by the `[google.longrunning.Operations.GetOperation](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.longrunning#google.longrunning.Operations.GetOperation)` method in the returned `[google.longrunning.Operation.response](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.longrunning#google.longrunning.Operation.FIELDS.google.protobuf.Any.google.longrunning.Operation.response)` field.

Fields  
---  
`read_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Time the snapshot was taken.  
`output_config` |  `[OutputConfig](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1p7beta1#google.cloud.asset.v1p7beta1.OutputConfig)` Output configuration indicating where the results were output to.  
`output_result` |  `[OutputResult](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1p7beta1#google.cloud.asset.v1p7beta1.OutputResult)` Output result indicating where the assets were exported to. For example, a set of actual Cloud Storage object URIs where the assets are exported to. The URIs can be different from what [output_config] has specified, as the service will split the output object into multiple ones once it exceeds a single Cloud Storage object limit.  
  
## GcsDestination

A Cloud Storage location.

Fields  
---  
Union field `object_uri`. Required. `object_uri` can be only one of the following:  
`uri` |  `string` The URI of the Cloud Storage object. It's the same URI that is used by gcloud storage. Example: "gs://bucket_name/object_name". See [Viewing and Editing Object Metadata](https://cloud.google.com/storage/docs/viewing-editing-metadata) for more information.  
`uri_prefix` |  `string` The URI prefix of all generated Cloud Storage objects. Example: "gs://bucket_name/object_name_prefix". Each object URI is in format: "gs://bucket_name/object_name_prefix/{ASSET_TYPE}/{SHARD_NUMBER} and only contains assets for that type.  starts from 0. Example: "gs://bucket_name/object_name_prefix/compute.googleapis.com/Disk/0" is the first shard of output objects containing all compute.googleapis.com/Disk assets. An INVALID_ARGUMENT error will be returned if file with the same name "gs://bucket_name/object_name_prefix" already exists.  
  
## GcsOutputResult

A Cloud Storage output result.

Fields  
---  
`uris[]` |  `string` List of URIs of the Cloud Storage objects. Example: "gs://bucket_name/object_name".  
  
## OutputConfig

Output configuration for export assets destination.

Fields  
---  
Union field `destination`. Asset export destination. `destination` can be only one of the following:  
`gcs_destination` |  `[GcsDestination](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1p7beta1#google.cloud.asset.v1p7beta1.GcsDestination)` Destination on Cloud Storage.  
`bigquery_destination` |  `[BigQueryDestination](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1p7beta1#google.cloud.asset.v1p7beta1.BigQueryDestination)` Destination on BigQuery. The output table stores the fields in asset proto as columns in BigQuery.  
  
## OutputResult

Output result of export assets.

Fields  
---  
Union field `result`. Asset export result. `result` can be only one of the following:  
`gcs_result` |  `[GcsOutputResult](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1p7beta1#google.cloud.asset.v1p7beta1.GcsOutputResult)` Export result on Cloud Storage.  
  
## PartitionSpec

Specifications of BigQuery partitioned table as export destination.

Fields  
---  
`partition_key` |  `[PartitionKey](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1p7beta1#google.cloud.asset.v1p7beta1.PartitionSpec.PartitionKey)` The partition key for BigQuery partitioned table.  
  
## PartitionKey

This enum is used to determine the partition key column when exporting assets to BigQuery partitioned table(s). Note that, if the partition key is a timestamp column, the actual partition is based on its date value (expressed in UTC. see details in <https://cloud.google.com/bigquery/docs/partitioned-tables#date_timestamp_partitioned_tables)>.

Enums  
---  
`PARTITION_KEY_UNSPECIFIED` | Unspecified partition key. If used, it means using non-partitioned table.  
`READ_TIME` | The time when the snapshot is taken. If specified as partition key, the result table(s) is partitioned by the additional timestamp column, readTime. If [read_time] in ExportAssetsRequest is specified, the readTime column's value will be the same as it. Otherwise, its value will be the current time that is used to take the snapshot.  
`REQUEST_TIME` | The time when the request is received and started to be processed. If specified as partition key, the result table(s) is partitioned by the requestTime column, an additional timestamp column representing when the request was received.  
  
## RelatedAsset

An asset identify in Google Cloud which contains its name, type and ancestors. An asset can be any resource in the Google Cloud [resource hierarchy](https://cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy), a resource outside the Google Cloud resource hierarchy (such as Google Kubernetes Engine clusters and objects), or a policy (e.g. IAM policy). See [Supported asset types](https://cloud.google.com/asset-inventory/docs/supported-asset-types) for more information.

Fields  
---  
`asset` |  `string` The full name of the asset. Example: `//compute.googleapis.com/projects/my_project_123/zones/zone1/instances/instance1`See [Resource names](https://cloud.google.com/apis/design/resource_names#full_resource_name) for more information.  
`asset_type` |  `string` The type of the asset. Example: `compute.googleapis.com/Disk`See [Supported asset types](https://cloud.google.com/asset-inventory/docs/supported-asset-types) for more information.  
`ancestors[]` |  `string` The ancestors of an asset in Google Cloud [resource hierarchy](https://cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy), represented as a list of relative resource names. An ancestry path starts with the closest ancestor in the hierarchy and ends at root.Example: `["projects/123456789", "folders/5432", "organizations/1234"]`  
  
## RelatedAssets

The detailed related assets with the `relationship_type`.

Fields  
---  
`relationship_attributes` |  `[RelationshipAttributes](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1p7beta1#google.cloud.asset.v1p7beta1.RelationshipAttributes)` The detailed relation attributes.  
`assets[]` |  `[RelatedAsset](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1p7beta1#google.cloud.asset.v1p7beta1.RelatedAsset)` The peer resources of the relationship.  
  
## RelationshipAttributes

The relationship attributes which include `type`, `source_resource_type`, `target_resource_type` and `action`.

Fields  
---  
`type` |  `string` The unique identifier of the relationship type. Example: `INSTANCE_TO_INSTANCEGROUP`  
`source_resource_type` |  `string` The source asset type. Example: `compute.googleapis.com/Instance`  
`target_resource_type` |  `string` The target asset type. Example: `compute.googleapis.com/Disk`  
`action` |  `string` The detail of the relationship, e.g. `contains`, `attaches`  
  
## Resource

A representation of a Google Cloud resource.

Fields  
---  
`version` |  `string` The API version. Example: `v1`  
`discovery_document_uri` |  `string` The URL of the discovery document containing the resource's JSON schema. Example: `https://www.googleapis.com/discovery/v1/apis/compute/v1/rest`This value is unspecified for resources that do not have an API based on a discovery document, such as Cloud Bigtable.  
`discovery_name` |  `string` The JSON schema name listed in the discovery document. Example: `Project`This value is unspecified for resources that do not have an API based on a discovery document, such as Cloud Bigtable.  
`resource_url` |  `string` The REST URL for accessing the resource. An HTTP `GET` request using this URL returns the resource itself. Example: `https://cloudresourcemanager.googleapis.com/v1/projects/my-project-123`This value is unspecified for resources without a REST API.  
`parent` |  `string` The full name of the immediate parent of this resource. See [Resource Names](https://cloud.google.com/apis/design/resource_names#full_resource_name) for more information.For Google Cloud assets, this value is the parent resource defined in the [IAM policy hierarchy](https://cloud.google.com/iam/docs/overview#policy_hierarchy). Example: `//cloudresourcemanager.googleapis.com/projects/my_project_123`For third-party assets, this field may be set differently.  
`data` |  `[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` The content of the resource, in which some sensitive fields are removed and may not be present.  
`location` |  `string` The location of the resource in Google Cloud, such as its zone and region. For more information, see <https://cloud.google.com/about/locations/>.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-24 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-24 UTC."],[],[]] 
