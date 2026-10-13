---
url: https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1p2beta1/feeds/
title: REST Resource: feeds \u00a0|\u00a0 Cloud Asset Inventory \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:30:07.164741+00:00
---

# REST Resource: feeds  |  Cloud Asset Inventory  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1p2beta1/feeds/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Cloud Asset Inventory ](https://docs.cloud.google.com/asset-inventory/docs)
  * [ Reference ](https://docs.cloud.google.com/asset-inventory/docs/asset-types)



Send feedback 

#  REST Resource: feeds Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Feed
    * JSON representation
  * ContentType
  * FeedOutputConfig
    * JSON representation
  * PubsubDestination
    * JSON representation
  * Methods



## Resource: Feed

An asset feed used to export asset updates to a destinations. An asset feed filter controls what updates are exported. The asset feed must be created within a project, organization, or folder. Supported destinations are: Cloud Pub/Sub topics.

JSON representation  
---  
      
    
    {
      "name": string,
      "assetNames": [
        string
      ],
      "assetTypes": [
        string
      ],
      "contentType": enum ([ContentType](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1p2beta1/feeds#ContentType)),
      "feedOutputConfig": {
        object ([FeedOutputConfig](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1p2beta1/feeds#FeedOutputConfig))
      }
    }  
  
Fields  
---  
`name` |  `string` Required. The format will be projects/{projectNumber}/feeds/{client-assigned_feed_identifier} or folders/{folder_number}/feeds/{client-assigned_feed_identifier} or organizations/{organization_number}/feeds/{client-assigned_feed_identifier}The client-assigned feed identifier must be unique within the parent project/folder/organization.  
`assetNames[]` |  `string` A list of the full names of the assets to receive updates. You must specify either or both of assetNames and assetTypes. Only asset updates matching specified assetNames or assetTypes are exported to the feed. For example: `//compute.googleapis.com/projects/my_project_123/zones/zone1/instances/instance1`. See [Resource Names](https://cloud.google.com/apis/design/resource_names#full_resource_name) for more info.  
`assetTypes[]` |  `string` A list of types of the assets to receive updates. You must specify either or both of assetNames and assetTypes. Only asset updates matching specified assetNames or assetTypes are exported to the feed. For example: "compute.googleapis.com/Disk" See [Introduction to Cloud Asset Inventory](https://cloud.google.com/resource-manager/docs/cloud-asset-inventory/overview) for all supported asset types.  
`contentType` |  `enum (`[ContentType](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1p2beta1/feeds#ContentType)`)` Asset content type. If not specified, no content but the asset name and type will be returned.  
`feedOutputConfig` |  `object (`[FeedOutputConfig](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1p2beta1/feeds#FeedOutputConfig)`)` Required. Feed output configuration defining where the asset updates are published to.  
  
## ContentType

Asset content type.

Enums  
---  
`CONTENT_TYPE_UNSPECIFIED` | Unspecified content type.  
`RESOURCE` | Resource metadata.  
`IAM_POLICY` | The actual IAM policy set on a resource.  
  
## FeedOutputConfig

Output configuration for asset feed destination.

JSON representation  
---  
      
    
    {
    
      // Union field destination can be only one of the following:
      "pubsubDestination": {
        object ([PubsubDestination](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1p2beta1/feeds#PubsubDestination))
      }
      // End of list of possible types for union field destination.
    }  
  
Fields  
---  
Union field `destination`. Asset feed destination. `destination` can be only one of the following:  
`pubsubDestination` |  `object (`[PubsubDestination](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1p2beta1/feeds#PubsubDestination)`)` Destination on Pub/Sub.  
  
## PubsubDestination

A Pub/Sub destination.

JSON representation  
---  
      
    
    {
      "topic": string
    }  
  
Fields  
---  
`topic` |  `string` The name of the Pub/Sub topic to publish to. For example: `projects/PROJECT_ID/topics/TOPIC_ID`.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1p2beta1/feeds/create)`

|  Creates a feed in a parent project/folder/organization to listen to its asset updates.  
  
### `[delete](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1p2beta1/feeds/delete)`

|  Deletes an asset feed.  
  
### `[get](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1p2beta1/feeds/get)`

|  Gets details about an asset feed.  
  
### `[list](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1p2beta1/feeds/list)`

|  Lists all asset feeds in a parent project/folder/organization.  
  
### `[patch](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1p2beta1/feeds/patch)`

|  Updates an asset feed configuration.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-05-08 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-08 UTC."],[],[]] 
