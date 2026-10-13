---
url: https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1p2beta1
title: Package google.cloud.asset.v1p2beta1 \u00a0|\u00a0 Cloud Asset Inventory \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:30:10.207156+00:00
---

# Package google.cloud.asset.v1p2beta1  |  Cloud Asset Inventory  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1p2beta1

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Cloud Asset Inventory ](https://docs.cloud.google.com/asset-inventory/docs)
  * [ Reference ](https://docs.cloud.google.com/asset-inventory/docs/asset-types)



Send feedback 

#  Package google.cloud.asset.v1p2beta1 Stay organized with collections  Save and categorize content based on your preferences. 

## Index

  * `[AssetService](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1p2beta1#google.cloud.asset.v1p2beta1.AssetService)` (interface)
  * `[Asset](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1p2beta1#google.cloud.asset.v1p2beta1.Asset)` (message)
  * `[BatchGetAssetsHistoryResponse](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1p2beta1#google.cloud.asset.v1p2beta1.BatchGetAssetsHistoryResponse)` (message)
  * `[ContentType](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1p2beta1#google.cloud.asset.v1p2beta1.ContentType)` (enum)
  * `[CreateFeedRequest](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1p2beta1#google.cloud.asset.v1p2beta1.CreateFeedRequest)` (message)
  * `[DeleteFeedRequest](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1p2beta1#google.cloud.asset.v1p2beta1.DeleteFeedRequest)` (message)
  * `[ExportAssetsResponse](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1p2beta1#google.cloud.asset.v1p2beta1.ExportAssetsResponse)` (message)
  * `[Feed](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1p2beta1#google.cloud.asset.v1p2beta1.Feed)` (message)
  * `[FeedOutputConfig](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1p2beta1#google.cloud.asset.v1p2beta1.FeedOutputConfig)` (message)
  * `[GcsDestination](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1p2beta1#google.cloud.asset.v1p2beta1.GcsDestination)` (message)
  * `[GetFeedRequest](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1p2beta1#google.cloud.asset.v1p2beta1.GetFeedRequest)` (message)
  * `[ListFeedsRequest](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1p2beta1#google.cloud.asset.v1p2beta1.ListFeedsRequest)` (message)
  * `[ListFeedsResponse](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1p2beta1#google.cloud.asset.v1p2beta1.ListFeedsResponse)` (message)
  * `[OutputConfig](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1p2beta1#google.cloud.asset.v1p2beta1.OutputConfig)` (message)
  * `[PubsubDestination](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1p2beta1#google.cloud.asset.v1p2beta1.PubsubDestination)` (message)
  * `[Resource](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1p2beta1#google.cloud.asset.v1p2beta1.Resource)` (message)
  * `[TemporalAsset](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1p2beta1#google.cloud.asset.v1p2beta1.TemporalAsset)` (message)
  * `[TimeWindow](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1p2beta1#google.cloud.asset.v1p2beta1.TimeWindow)` (message)
  * `[UpdateFeedRequest](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1p2beta1#google.cloud.asset.v1p2beta1.UpdateFeedRequest)` (message)



## AssetService

Asset service definition.

CreateFeed  
---  
` rpc CreateFeed(`[CreateFeedRequest](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1p2beta1#google.cloud.asset.v1p2beta1.CreateFeedRequest)`) returns (`[Feed](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1p2beta1#google.cloud.asset.v1p2beta1.Feed)`) ` Creates a feed in a parent project/folder/organization to listen to its asset updates.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
DeleteFeed  
---  
` rpc DeleteFeed(`[DeleteFeedRequest](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1p2beta1#google.cloud.asset.v1p2beta1.DeleteFeedRequest)`) returns (`[Empty](https://protobuf.dev/reference/protobuf/google.protobuf/#empty)`) ` Deletes an asset feed.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
GetFeed  
---  
` rpc GetFeed(`[GetFeedRequest](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1p2beta1#google.cloud.asset.v1p2beta1.GetFeedRequest)`) returns (`[Feed](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1p2beta1#google.cloud.asset.v1p2beta1.Feed)`) ` Gets details about an asset feed.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
ListFeeds  
---  
` rpc ListFeeds(`[ListFeedsRequest](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1p2beta1#google.cloud.asset.v1p2beta1.ListFeedsRequest)`) returns (`[ListFeedsResponse](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1p2beta1#google.cloud.asset.v1p2beta1.ListFeedsResponse)`) ` Lists all asset feeds in a parent project/folder/organization.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
UpdateFeed  
---  
` rpc UpdateFeed(`[UpdateFeedRequest](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1p2beta1#google.cloud.asset.v1p2beta1.UpdateFeedRequest)`) returns (`[Feed](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1p2beta1#google.cloud.asset.v1p2beta1.Feed)`) ` Updates an asset feed configuration.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
  
## Asset

An asset in Google Cloud. An asset can be any resource in the Google Cloud [resource hierarchy](https://cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy), a resource outside the Google Cloud resource hierarchy (such as Google Kubernetes Engine clusters and objects), or a policy (e.g. IAM policy). See [Supported asset types](https://cloud.google.com/asset-inventory/docs/supported-asset-types) for more information.

Fields  
---  
`name` |  `string` The full name of the asset. Example: `//compute.googleapis.com/projects/my_project_123/zones/zone1/instances/instance1`See [Resource names](https://cloud.google.com/apis/design/resource_names#full_resource_name) for more information.  
`asset_type` |  `string` The type of the asset. Example: `compute.googleapis.com/Disk`See [Supported asset types](https://cloud.google.com/asset-inventory/docs/supported-asset-types) for more information.  
`resource` |  `[Resource](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1p2beta1#google.cloud.asset.v1p2beta1.Resource)` A representation of the resource.  
`iam_policy` |  `[Policy](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.iam.v1#google.iam.v1.Policy)` A representation of the IAM policy set on a Google Cloud resource. There can be a maximum of one IAM policy set on any given resource. In addition, IAM policies inherit their granted access scope from any policies set on parent resources in the resource hierarchy. Therefore, the effectively policy is the union of both the policy set on this resource and each policy set on all of the resource's ancestry resource levels in the hierarchy. See [this topic](https://cloud.google.com/iam/help/allow-policies/inheritance) for more information.  
`ancestors[]` |  `string` The ancestry path of an asset in Google Cloud [resource hierarchy](https://cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy), represented as a list of relative resource names. An ancestry path starts with the closest ancestor in the hierarchy and ends at root. If the asset is a project, folder, or organization, the ancestry path starts from the asset itself.Example: `["projects/123456789", "folders/5432", "organizations/1234"]`  
`org_policy[]` |  `[Policy](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.orgpolicy.v1#google.cloud.orgpolicy.v1.Policy)` A representation of an [organization policy](https://cloud.google.com/resource-manager/docs/organization-policy/overview#organization_policy). There can be more than one organization policy with different constraints set on a given resource.  
Union field `access_context_policy`. A representation of an [access policy](https://cloud.google.com/access-context-manager/docs/overview#access-policies). `access_context_policy` can be only one of the following:  
`access_policy` |  `[AccessPolicy](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.identity.accesscontextmanager.v1#google.identity.accesscontextmanager.v1.AccessPolicy)` Please also refer to the [access policy user guide](https://cloud.google.com/access-context-manager/docs/overview#access-policies).  
`access_level` |  `[AccessLevel](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.identity.accesscontextmanager.v1#google.identity.accesscontextmanager.v1.AccessLevel)` Please also refer to the [access level user guide](https://cloud.google.com/access-context-manager/docs/overview#access-levels).  
`service_perimeter` |  `[ServicePerimeter](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.identity.accesscontextmanager.v1#google.identity.accesscontextmanager.v1.ServicePerimeter)` Please also refer to the [service perimeter user guide](https://cloud.google.com/vpc-service-controls/docs/overview).  
  
## BatchGetAssetsHistoryResponse

Batch get assets history response.

Fields  
---  
`assets[]` |  `[TemporalAsset](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1p2beta1#google.cloud.asset.v1p2beta1.TemporalAsset)` A list of assets with valid time windows.  
  
## ContentType

Asset content type.

Enums  
---  
`CONTENT_TYPE_UNSPECIFIED` | Unspecified content type.  
`RESOURCE` | Resource metadata.  
`IAM_POLICY` | The actual IAM policy set on a resource.  
  
## CreateFeedRequest

Create asset feed request.

Fields  
---  
`parent` |  `string` Required. The name of the project/folder/organization where this feed should be created in. It can only be an organization number (such as "organizations/123"), a folder number (such as "folders/123"), a project ID (such as "projects/my-project-id"), or a project number (such as "projects/12345").  
`feed_id` |  `string` Required. This is the client-assigned asset feed identifier and it needs to be unique under a specific parent project/folder/organization.  
`feed` |  `[Feed](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1p2beta1#google.cloud.asset.v1p2beta1.Feed)` Required. The feed details. The field `name` must be empty and it will be generated in the format of: projects/project_number/feeds/feed_id folders/folder_number/feeds/feed_id organizations/organization_number/feeds/feed_id  
  
## DeleteFeedRequest

Fields  
---  
`name` |  `string` Required. The name of the feed and it must be in the format of: projects/project_number/feeds/feed_id folders/folder_number/feeds/feed_id organizations/organization_number/feeds/feed_id  
  
## ExportAssetsResponse

The export asset response. This message is returned by the `[google.longrunning.Operations.GetOperation](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.longrunning#google.longrunning.Operations.GetOperation)` method in the returned `[google.longrunning.Operation.response](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.longrunning#google.longrunning.Operation.FIELDS.google.protobuf.Any.google.longrunning.Operation.response)` field.

Fields  
---  
`read_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Time the snapshot was taken.  
`output_config` |  `[OutputConfig](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1p2beta1#google.cloud.asset.v1p2beta1.OutputConfig)` Output configuration indicating where the results were output to.  
  
## Feed

An asset feed used to export asset updates to a destinations. An asset feed filter controls what updates are exported. The asset feed must be created within a project, organization, or folder. Supported destinations are: Cloud Pub/Sub topics.

Fields  
---  
`name` |  `string` Required. The format will be projects/{project_number}/feeds/{client-assigned_feed_identifier} or folders/{folder_number}/feeds/{client-assigned_feed_identifier} or organizations/{organization_number}/feeds/{client-assigned_feed_identifier}The client-assigned feed identifier must be unique within the parent project/folder/organization.  
`asset_names[]` |  `string` A list of the full names of the assets to receive updates. You must specify either or both of asset_names and asset_types. Only asset updates matching specified asset_names or asset_types are exported to the feed. For example: `//compute.googleapis.com/projects/my_project_123/zones/zone1/instances/instance1`. See [Resource Names](https://cloud.google.com/apis/design/resource_names#full_resource_name) for more info.  
`asset_types[]` |  `string` A list of types of the assets to receive updates. You must specify either or both of asset_names and asset_types. Only asset updates matching specified asset_names or asset_types are exported to the feed. For example: "compute.googleapis.com/Disk" See [Introduction to Cloud Asset Inventory](https://cloud.google.com/resource-manager/docs/cloud-asset-inventory/overview) for all supported asset types.  
`content_type` |  `[ContentType](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1p2beta1#google.cloud.asset.v1p2beta1.ContentType)` Asset content type. If not specified, no content but the asset name and type will be returned.  
`feed_output_config` |  `[FeedOutputConfig](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1p2beta1#google.cloud.asset.v1p2beta1.FeedOutputConfig)` Required. Feed output configuration defining where the asset updates are published to.  
  
## FeedOutputConfig

Output configuration for asset feed destination.

Fields  
---  
Union field `destination`. Asset feed destination. `destination` can be only one of the following:  
`pubsub_destination` |  `[PubsubDestination](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1p2beta1#google.cloud.asset.v1p2beta1.PubsubDestination)` Destination on Pub/Sub.  
  
## GcsDestination

A Cloud Storage location.

Fields  
---  
Union field `object_uri`. Required. `object_uri` can be only one of the following:  
`uri` |  `string` The URI of the Cloud Storage object. It's the same URI that is used by gcloud storage. For example: "gs://bucket_name/object_name". See [Viewing and Editing Object Metadata](https://cloud.google.com/storage/docs/viewing-editing-metadata) for more information.  
  
## GetFeedRequest

Get asset feed request.

Fields  
---  
`name` |  `string` Required. The name of the Feed and it must be in the format of: projects/project_number/feeds/feed_id folders/folder_number/feeds/feed_id organizations/organization_number/feeds/feed_id  
  
## ListFeedsRequest

List asset feeds request.

Fields  
---  
`parent` |  `string` Required. The parent project/folder/organization whose feeds are to be listed. It can only be using project/folder/organization number (such as "folders/12345")", or a project ID (such as "projects/my-project-id").  
  
## ListFeedsResponse

Fields  
---  
`feeds[]` |  `[Feed](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1p2beta1#google.cloud.asset.v1p2beta1.Feed)` A list of feeds.  
  
## OutputConfig

Output configuration for export assets destination.

Fields  
---  
Union field `destination`. Asset export destination. `destination` can be only one of the following:  
`gcs_destination` |  `[GcsDestination](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1p2beta1#google.cloud.asset.v1p2beta1.GcsDestination)` Destination on Cloud Storage.  
  
## PubsubDestination

A Pub/Sub destination.

Fields  
---  
`topic` |  `string` The name of the Pub/Sub topic to publish to. For example: `projects/PROJECT_ID/topics/TOPIC_ID`.  
  
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
  
## TemporalAsset

An asset in Google Cloud and its temporal metadata, including the time window when it was observed and its status during that window.

Fields  
---  
`window` |  `[TimeWindow](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1p2beta1#google.cloud.asset.v1p2beta1.TimeWindow)` The time window when the asset data and state was observed.  
`deleted` |  `bool` Whether the asset has been deleted or not.  
`asset` |  `[Asset](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1p2beta1#google.cloud.asset.v1p2beta1.Asset)` An asset in Google Cloud.  
  
## TimeWindow

A time window specified by its `start_time` and `end_time`.

Fields  
---  
`start_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Start time of the time window (exclusive).  
`end_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` End time of the time window (inclusive). If not specified, the current timestamp is used instead.  
  
## UpdateFeedRequest

Update asset feed request.

Fields  
---  
`feed` |  `[Feed](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1p2beta1#google.cloud.asset.v1p2beta1.Feed)` Required. The new values of feed details. It must match an existing feed and the field `name` must be in the format of: projects/project_number/feeds/feed_id or folders/folder_number/feeds/feed_id or organizations/organization_number/feeds/feed_id.  
`update_mask` |  `[FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` Required. Only updates the `feed` fields indicated by this mask. The field mask must not be empty, and it must not contain fields that are immutable or only set by the server.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-24 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-24 UTC."],[],[]] 
