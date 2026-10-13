---
url: https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/batchGetAssetsHistory/
title: Method: batchGetAssetsHistory \u00a0|\u00a0 Cloud Asset Inventory \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:30:03.891501+00:00
---

# Method: batchGetAssetsHistory  |  Cloud Asset Inventory  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/batchGetAssetsHistory/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Cloud Asset Inventory ](https://docs.cloud.google.com/asset-inventory/docs)
  * [ Reference ](https://docs.cloud.google.com/asset-inventory/docs/asset-types)



Send feedback 

#  Method: batchGetAssetsHistory Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * TemporalAsset
    * JSON representation
  * PriorAssetState
  * Try it!



Batch gets the update history of assets that overlap a time window. For IAM_POLICY content, this API outputs history when the asset and its attached IAM POLICY both exist. This can create gaps in the output history. Otherwise, this API outputs history with asset in both non-delete or deleted status. If a specified asset does not exist, this API returns an INVALID_ARGUMENT error.

### HTTP request

`GET https://cloudasset.googleapis.com/v1/{parent=*/*}:batchGetAssetsHistory`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The relative name of the root asset. It can only be an organization number (such as "organizations/123"), a project ID (such as "projects/my-project-id")", or a project number (such as "projects/12345"). Authorization requires one or more of the following [IAM](https://cloud.google.com/iam/docs/) permissions on the specified resource `parent`:

  * `cloudasset.assets.exportResource`
  * `cloudasset.assets.exportIamPolicy`

  
  
### Query parameters

Parameters  
---  
`assetNames[]` |  `string` A list of the full names of the assets. See: <https://cloud.google.com/asset-inventory/docs/resource-name-format> Example:`//compute.googleapis.com/projects/my_project_123/zones/zone1/instances/instance1`.The request becomes a no-op if the asset name list is empty, and the max size of the asset name list is 100 in one request.  
`contentType` |  `enum (`[ContentType](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/feeds#ContentType)`)` Optional. The content type.  
`readTimeWindow` |  `object (`[TimeWindow](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TimeWindow)`)` Optional. The time window for the asset history. Both startTime and endTime are optional and if set, it must be after the current time minus 35 days. If endTime is not set, it is default to current timestamp. If startTime is not set, the snapshot of the assets at endTime will be returned. The returned results contain all temporal assets whose time window overlap with readTimeWindow.  
`relationshipTypes[]` |  `string` Optional. A list of relationship types to output, for example: `INSTANCE_TO_INSTANCEGROUP`. This field should only be specified if contentType=RELATIONSHIP. * If specified: it outputs specified relationships' history on the [assetNames]. It returns an error if any of the [relationshipTypes] doesn't belong to the supported relationship types of the [assetNames] or if any of the [assetNames]'s types doesn't belong to the source types of the [relationshipTypes]. * Otherwise: it outputs the supported relationships' history on the [assetNames] or returns an error if any of the [assetNames]'s types has no relationship support. See [Introduction to Cloud Asset Inventory](https://cloud.google.com/asset-inventory/docs/overview) for all supported asset types and relationship types.  
  
### Request body

The request body must be empty.

### Response body

Batch get assets history response.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "assets": [
        {
          object ([TemporalAsset](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/batchGetAssetsHistory#TemporalAsset))
        }
      ]
    }  
  
Fields  
---  
`assets[]` |  `object (`[TemporalAsset](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/batchGetAssetsHistory#TemporalAsset)`)` A list of assets with valid time windows.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

## TemporalAsset

An asset in Google Cloud and its temporal metadata, including the time window when it was observed and its status during that window.

JSON representation  
---  
      
    
    {
      "window": {
        object ([TimeWindow](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TimeWindow))
      },
      "deleted": boolean,
      "asset": {
        object ([Asset](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset))
      },
      "priorAssetState": enum ([PriorAssetState](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/batchGetAssetsHistory#PriorAssetState)),
      "priorAsset": {
        object ([Asset](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset))
      }
    }  
  
Fields  
---  
`window` |  `object (`[TimeWindow](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TimeWindow)`)` The time window when the asset data and state was observed.  
`deleted` |  `boolean` Whether the asset has been deleted or not.  
`asset` |  `object (`[Asset](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset)`)` An asset in Google Cloud.  
`priorAssetState` |  `enum (`[PriorAssetState](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/batchGetAssetsHistory#PriorAssetState)`)` State of priorAsset.  
`priorAsset` |  `object (`[Asset](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset)`)` Prior copy of the asset. Populated if priorAssetState is PRESENT. Currently this is only set for responses in Real-Time Feed.  
  
## PriorAssetState

State of prior asset.

Enums  
---  
`PRIOR_ASSET_STATE_UNSPECIFIED` | priorAsset is not applicable for the current asset.  
`PRESENT` | priorAsset is populated correctly.  
`INVALID` | Failed to set priorAsset.  
`DOES_NOT_EXIST` | Current asset is the first known state.  
`DELETED` | priorAsset is a deletion.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-30 UTC."],[],[]] 
