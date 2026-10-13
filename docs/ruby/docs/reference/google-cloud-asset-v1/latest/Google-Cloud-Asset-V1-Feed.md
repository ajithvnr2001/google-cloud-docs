---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Cloud-Asset-V1-Feed/
title: Cloud Asset V1 API - Class Google::Cloud::Asset::V1::Feed (v1.9.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:21:16.798788+00:00
---

# Cloud Asset V1 API - Class Google::Cloud::Asset::V1::Feed (v1.9.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Cloud-Asset-V1-Feed/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Asset V1 API - Class Google::Cloud::Asset::V1::Feed (v1.9.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.9.1 (latest)  1.9.0  1.8.0  1.7.0  1.6.1  1.5.0  1.4.1  1.3.1  1.2.0  1.1.0  1.0.2  0.32.0  0.31.0  0.30.0  0.29.3  0.28.1  0.27.0  0.26.1  0.25.0  0.24.0  0.23.0  0.22.0  0.21.1  0.20.1  0.19.0  0.18.0  0.17.3 

Reference documentation and code samples for the Cloud Asset V1 API class Google::Cloud::Asset::V1::Feed.

An asset feed used to export asset updates to a destinations. An asset feed filter controls what updates are exported. The asset feed must be created within a project, organization, or folder. Supported destinations are: Pub/Sub topics.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #asset_names
    
    
    def asset_names() -> ::Array<::String>

**Returns**

  * (::Array<::String>) — A list of the full names of the assets to receive updates. You must specify either or both of asset_names and asset_types. Only asset updates matching specified asset_names or asset_types are exported to the feed. Example: `//compute.googleapis.com/projects/my_project_123/zones/zone1/instances/instance1`. For a list of the full names for supported asset types, see [Resource name format](https://docs.cloud.google.com/asset-inventory/docs/resource-name-format). 



### #asset_names=
    
    
    def asset_names=(value) -> ::Array<::String>

**Parameter**

  * **value** (::Array<::String>) — A list of the full names of the assets to receive updates. You must specify either or both of asset_names and asset_types. Only asset updates matching specified asset_names or asset_types are exported to the feed. Example: `//compute.googleapis.com/projects/my_project_123/zones/zone1/instances/instance1`. For a list of the full names for supported asset types, see [Resource name format](https://docs.cloud.google.com/asset-inventory/docs/resource-name-format). 



**Returns**

  * (::Array<::String>) — A list of the full names of the assets to receive updates. You must specify either or both of asset_names and asset_types. Only asset updates matching specified asset_names or asset_types are exported to the feed. Example: `//compute.googleapis.com/projects/my_project_123/zones/zone1/instances/instance1`. For a list of the full names for supported asset types, see [Resource name format](https://docs.cloud.google.com/asset-inventory/docs/resource-name-format). 



### #asset_types
    
    
    def asset_types() -> ::Array<::String>

**Returns**

  * (::Array<::String>) — A list of types of the assets to receive updates. You must specify either or both of asset_names and asset_types. Only asset updates matching specified asset_names or asset_types are exported to the feed. Example: `"compute.googleapis.com/Disk"`

For a list of all supported asset types, see [Supported asset types](https://docs.cloud.google.com/asset-inventory/docs/supported-asset-types). 




### #asset_types=
    
    
    def asset_types=(value) -> ::Array<::String>

**Parameter**

  * **value** (::Array<::String>) — A list of types of the assets to receive updates. You must specify either or both of asset_names and asset_types. Only asset updates matching specified asset_names or asset_types are exported to the feed. Example: `"compute.googleapis.com/Disk"`

For a list of all supported asset types, see [Supported asset types](https://docs.cloud.google.com/asset-inventory/docs/supported-asset-types). 




**Returns**

  * (::Array<::String>) — A list of types of the assets to receive updates. You must specify either or both of asset_names and asset_types. Only asset updates matching specified asset_names or asset_types are exported to the feed. Example: `"compute.googleapis.com/Disk"`

For a list of all supported asset types, see [Supported asset types](https://docs.cloud.google.com/asset-inventory/docs/supported-asset-types). 




### #condition
    
    
    def condition() -> ::Google::Type::Expr

**Returns**

  * ([::Google::Type::Expr](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Type-Expr)) — A condition which determines whether an asset update should be published. If specified, an asset will be returned only when the expression evaluates to true. When set, `expression` field in the `Expr` must be a valid [CEL expression](https://github.com/google/cel-spec) on a TemporalAsset with name `temporal_asset`. Example: a Feed with expression ("temporal_asset.deleted == true") will only publish Asset deletions. Other fields of `Expr` are optional.

See our [user guide](https://cloud.google.com/asset-inventory/docs/monitoring-asset-changes-with-condition) for detailed instructions. 




### #condition=
    
    
    def condition=(value) -> ::Google::Type::Expr

**Parameter**

  * **value** ([::Google::Type::Expr](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Type-Expr)) — A condition which determines whether an asset update should be published. If specified, an asset will be returned only when the expression evaluates to true. When set, `expression` field in the `Expr` must be a valid [CEL expression](https://github.com/google/cel-spec) on a TemporalAsset with name `temporal_asset`. Example: a Feed with expression ("temporal_asset.deleted == true") will only publish Asset deletions. Other fields of `Expr` are optional.

See our [user guide](https://cloud.google.com/asset-inventory/docs/monitoring-asset-changes-with-condition) for detailed instructions. 




**Returns**

  * ([::Google::Type::Expr](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Type-Expr)) — A condition which determines whether an asset update should be published. If specified, an asset will be returned only when the expression evaluates to true. When set, `expression` field in the `Expr` must be a valid [CEL expression](https://github.com/google/cel-spec) on a TemporalAsset with name `temporal_asset`. Example: a Feed with expression ("temporal_asset.deleted == true") will only publish Asset deletions. Other fields of `Expr` are optional.

See our [user guide](https://cloud.google.com/asset-inventory/docs/monitoring-asset-changes-with-condition) for detailed instructions. 




### #content_type
    
    
    def content_type() -> ::Google::Cloud::Asset::V1::ContentType

**Returns**

  * ([::Google::Cloud::Asset::V1::ContentType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Cloud-Asset-V1-ContentType)) — Asset content type. If not specified, no content but the asset name and type will be returned. 



### #content_type=
    
    
    def content_type=(value) -> ::Google::Cloud::Asset::V1::ContentType

**Parameter**

  * **value** ([::Google::Cloud::Asset::V1::ContentType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Cloud-Asset-V1-ContentType)) — Asset content type. If not specified, no content but the asset name and type will be returned. 



**Returns**

  * ([::Google::Cloud::Asset::V1::ContentType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Cloud-Asset-V1-ContentType)) — Asset content type. If not specified, no content but the asset name and type will be returned. 



### #feed_output_config
    
    
    def feed_output_config() -> ::Google::Cloud::Asset::V1::FeedOutputConfig

**Returns**

  * ([::Google::Cloud::Asset::V1::FeedOutputConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Cloud-Asset-V1-FeedOutputConfig)) — Required. Feed output configuration defining where the asset updates are published to. 



### #feed_output_config=
    
    
    def feed_output_config=(value) -> ::Google::Cloud::Asset::V1::FeedOutputConfig

**Parameter**

  * **value** ([::Google::Cloud::Asset::V1::FeedOutputConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Cloud-Asset-V1-FeedOutputConfig)) — Required. Feed output configuration defining where the asset updates are published to. 



**Returns**

  * ([::Google::Cloud::Asset::V1::FeedOutputConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Cloud-Asset-V1-FeedOutputConfig)) — Required. Feed output configuration defining where the asset updates are published to. 



### #name
    
    
    def name() -> ::String

**Returns**

  * (::String) — Required. The format will be projects/{project_number}/feeds/{client-assigned_feed_identifier} or folders/{folder_number}/feeds/{client-assigned_feed_identifier} or organizations/{organization_number}/feeds/{client-assigned_feed_identifier}

The client-assigned feed identifier must be unique within the parent project/folder/organization. 




### #name=
    
    
    def name=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The format will be projects/{project_number}/feeds/{client-assigned_feed_identifier} or folders/{folder_number}/feeds/{client-assigned_feed_identifier} or organizations/{organization_number}/feeds/{client-assigned_feed_identifier}

The client-assigned feed identifier must be unique within the parent project/folder/organization. 




**Returns**

  * (::String) — Required. The format will be projects/{project_number}/feeds/{client-assigned_feed_identifier} or folders/{folder_number}/feeds/{client-assigned_feed_identifier} or organizations/{organization_number}/feeds/{client-assigned_feed_identifier}

The client-assigned feed identifier must be unique within the parent project/folder/organization. 




### #relationship_types
    
    
    def relationship_types() -> ::Array<::String>

**Returns**

  * (::Array<::String>) — 

A list of relationship types to output, for example: `INSTANCE_TO_INSTANCEGROUP`. This field should only be specified if content_type=RELATIONSHIP.

    * If specified: it outputs specified relationship updates on the [asset_names] or the [asset_types]. It returns an error if any of the [relationship_types] doesn't belong to the supported relationship types of the [asset_names] or [asset_types], or any of the [asset_names] or the [asset_types] doesn't belong to the source types of the [relationship_types].
    * Otherwise: it outputs the supported relationships of the types of [asset_names] and [asset_types] or returns an error if any of the [asset_names] or the [asset_types] has no replationship support. See [Introduction to Cloud Asset Inventory](https://cloud.google.com/asset-inventory/docs/overview) for all supported asset types and relationship types.



### #relationship_types=
    
    
    def relationship_types=(value) -> ::Array<::String>

**Parameter**

  * **value** (::Array<::String>) — 

A list of relationship types to output, for example: `INSTANCE_TO_INSTANCEGROUP`. This field should only be specified if content_type=RELATIONSHIP.

    * If specified: it outputs specified relationship updates on the [asset_names] or the [asset_types]. It returns an error if any of the [relationship_types] doesn't belong to the supported relationship types of the [asset_names] or [asset_types], or any of the [asset_names] or the [asset_types] doesn't belong to the source types of the [relationship_types].
    * Otherwise: it outputs the supported relationships of the types of [asset_names] and [asset_types] or returns an error if any of the [asset_names] or the [asset_types] has no replationship support. See [Introduction to Cloud Asset Inventory](https://cloud.google.com/asset-inventory/docs/overview) for all supported asset types and relationship types.



**Returns**

  * (::Array<::String>) — 

A list of relationship types to output, for example: `INSTANCE_TO_INSTANCEGROUP`. This field should only be specified if content_type=RELATIONSHIP.

    * If specified: it outputs specified relationship updates on the [asset_names] or the [asset_types]. It returns an error if any of the [relationship_types] doesn't belong to the supported relationship types of the [asset_names] or [asset_types], or any of the [asset_names] or the [asset_types] doesn't belong to the source types of the [relationship_types].
    * Otherwise: it outputs the supported relationships of the types of [asset_names] and [asset_types] or returns an error if any of the [asset_names] or the [asset_types] has no replationship support. See [Introduction to Cloud Asset Inventory](https://cloud.google.com/asset-inventory/docs/overview) for all supported asset types and relationship types.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
