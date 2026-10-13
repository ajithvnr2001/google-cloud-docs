---
url: https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/feeds/patch/
title: Method: feeds.patch \u00a0|\u00a0 Cloud Asset Inventory \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:51:18.270824+00:00
---

# Method: feeds.patch  |  Cloud Asset Inventory  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/feeds/patch/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Cloud Asset Inventory ](https://docs.cloud.google.com/asset-inventory/docs)
  * [ Reference ](https://docs.cloud.google.com/asset-inventory/docs/asset-types)



Send feedback 

#  Method: feeds.patch Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
      * JSON representation
      * JSON representation
  * Response body
  * Authorization scopes
  * Try it!



Updates an asset feed configuration.

### HTTP request

`PATCH https://cloudasset.googleapis.com/v1/{feed.name=*/*/feeds/*}`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`feed.name` |  `string` Required. The format will be projects/{projectNumber}/feeds/{client-assigned_feed_identifier} or folders/{folder_number}/feeds/{client-assigned_feed_identifier} or organizations/{organization_number}/feeds/{client-assigned_feed_identifier}The client-assigned feed identifier must be unique within the parent project/folder/organization.  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "feed": {
        "name": string,
        "assetNames": [
          string
        ],
        "assetTypes": [
          string
        ],
        "contentType": enum ([ContentType](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/feeds#ContentType)),
        "feedOutputConfig": {
    
          // Union field destination can be only one of the following:
          "pubsubDestination": {
            object ([PubsubDestination](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/feeds#PubsubDestination))
          }
          // End of list of possible types for union field destination.
        },
        "condition": {
          "expression": string,
          "title": string,
          "description": string,
          "location": string
        },
        "relationshipTypes": [
          string
        ]
      },
      "updateMask": string
    }  
  
Fields  
---  
`feed.assetNames[]` |  `string` A list of the full names of the assets to receive updates. You must specify either or both of assetNames and assetTypes. Only asset updates matching specified assetNames or assetTypes are exported to the feed. Example: `//compute.googleapis.com/projects/my_project_123/zones/zone1/instances/instance1`. For a list of the full names for supported asset types, see [Resource name format](https://docs.cloud.google.com/asset-inventory/docs/resource-name-format).  
`feed.assetTypes[]` |  `string` A list of types of the assets to receive updates. You must specify either or both of assetNames and assetTypes. Only asset updates matching specified assetNames or assetTypes are exported to the feed. Example: `"compute.googleapis.com/Disk"`For a list of all supported asset types, see [Supported asset types](https://docs.cloud.google.com/asset-inventory/docs/supported-asset-types).  
`feed.contentType` |  `enum (`[ContentType](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/feeds#ContentType)`)` Asset content type. If not specified, no content but the asset name and type will be returned.  
`feed.feedOutputConfig` |  `object (`[FeedOutputConfig](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/feeds#FeedOutputConfig)`)` Required. Feed output configuration defining where the asset updates are published to.  
`feed.condition` |  `object (`[Expr](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/Shared.Types/Binding#Expr)`)` A condition which determines whether an asset update should be published. If specified, an asset will be returned only when the expression evaluates to true. When set, `expression` field in the `Expr` must be a valid [CEL expression](https://github.com/google/cel-spec) on a TemporalAsset with name `temporal_asset`. Example: a Feed with expression ("temporal_asset.deleted == true") will only publish Asset deletions. Other fields of `Expr` are optional.See our [user guide](https://cloud.google.com/asset-inventory/docs/monitoring-asset-changes-with-condition) for detailed instructions.  
`feed.relationshipTypes[]` |  `string` A list of relationship types to output, for example: `INSTANCE_TO_INSTANCEGROUP`. This field should only be specified if contentType=RELATIONSHIP. * If specified: it outputs specified relationship updates on the [assetNames] or the [assetTypes]. It returns an error if any of the [relationshipTypes] doesn't belong to the supported relationship types of the [assetNames] or [assetTypes], or any of the [assetNames] or the [assetTypes] doesn't belong to the source types of the [relationshipTypes]. * Otherwise: it outputs the supported relationships of the types of [assetNames] and [assetTypes] or returns an error if any of the [assetNames] or the [assetTypes] has no replationship support. See [Introduction to Cloud Asset Inventory](https://cloud.google.com/asset-inventory/docs/overview) for all supported asset types and relationship types.  
`updateMask` |  `string (`[FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` format)` Required. Only updates the `feed` fields indicated by this mask. The field mask must not be empty, and it must not contain fields that are immutable or only set by the server.This is a comma-separated list of fully qualified names of fields. Example: `"user.displayName,photo"`.  
  
### Response body

If successful, the response body contains an instance of `[Feed](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/feeds#Feed)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-30 UTC."],[],[]] 
