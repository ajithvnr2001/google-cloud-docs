---
url: https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1p2beta1/feeds/patch/
title: Method: feeds.patch \u00a0|\u00a0 Cloud Asset Inventory \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:30:07.771844+00:00
---

# Method: feeds.patch  |  Cloud Asset Inventory  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1p2beta1/feeds/patch/

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
  * Response body
  * Authorization scopes
  * Try it!



Updates an asset feed configuration.

### HTTP request

`PATCH https://cloudasset.googleapis.com/v1p2beta1/{feed.name=*/*/feeds/*}`

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
        "contentType": enum ([ContentType](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1p2beta1/feeds#ContentType)),
        "feedOutputConfig": {
    
          // Union field destination can be only one of the following:
          "pubsubDestination": {
            object ([PubsubDestination](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1p2beta1/feeds#PubsubDestination))
          }
          // End of list of possible types for union field destination.
        }
      },
      "updateMask": string
    }  
  
Fields  
---  
`feed.assetNames[]` |  `string` A list of the full names of the assets to receive updates. You must specify either or both of assetNames and assetTypes. Only asset updates matching specified assetNames or assetTypes are exported to the feed. For example: `//compute.googleapis.com/projects/my_project_123/zones/zone1/instances/instance1`. See [Resource Names](https://cloud.google.com/apis/design/resource_names#full_resource_name) for more info.  
`feed.assetTypes[]` |  `string` A list of types of the assets to receive updates. You must specify either or both of assetNames and assetTypes. Only asset updates matching specified assetNames or assetTypes are exported to the feed. For example: "compute.googleapis.com/Disk" See [Introduction to Cloud Asset Inventory](https://cloud.google.com/resource-manager/docs/cloud-asset-inventory/overview) for all supported asset types.  
`feed.contentType` |  `enum (`[ContentType](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1p2beta1/feeds#ContentType)`)` Asset content type. If not specified, no content but the asset name and type will be returned.  
`feed.feedOutputConfig` |  `object (`[FeedOutputConfig](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1p2beta1/feeds#FeedOutputConfig)`)` Required. Feed output configuration defining where the asset updates are published to.  
`updateMask` |  `string (`[FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` format)` Required. Only updates the `feed` fields indicated by this mask. The field mask must not be empty, and it must not contain fields that are immutable or only set by the server.This is a comma-separated list of fully qualified names of fields. Example: `"user.displayName,photo"`.  
  
### Response body

If successful, the response body contains an instance of `[Feed](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1p2beta1/feeds#Feed)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-30 UTC."],[],[]] 
