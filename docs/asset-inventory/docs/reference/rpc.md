---
url: https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/
title: Cloud Asset API \u00a0|\u00a0 Cloud Asset Inventory \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:30:09.822149+00:00
---

# Cloud Asset API  |  Cloud Asset Inventory  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Cloud Asset Inventory ](https://docs.cloud.google.com/asset-inventory/docs)
  * [ Reference ](https://docs.cloud.google.com/asset-inventory/docs/asset-types)



Send feedback 

#  Cloud Asset API Stay organized with collections  Save and categorize content based on your preferences. 

The Cloud Asset API manages the history and inventory of Google Cloud resources.

## Service: cloudasset.googleapis.com

The Service name `cloudasset.googleapis.com` is needed to create RPC client stubs.

## `[google.cloud.asset.v1.AssetService](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.AssetService)`

Methods  
---  
``[AnalyzeIamPolicy](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.AssetService.AnalyzeIamPolicy)`` |  Analyzes IAM policies to answer which identities have what accesses on which resources.  
``[AnalyzeIamPolicyLongrunning](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.AssetService.AnalyzeIamPolicyLongrunning)`` |  Analyzes IAM policies asynchronously to answer which identities have what accesses on which resources, and writes the analysis results to a Google Cloud Storage or a BigQuery destination.  
``[AnalyzeMove](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.AssetService.AnalyzeMove)`` |  Analyze moving a resource to a specified destination without kicking off the actual move.  
``[AnalyzeOrgPolicies](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.AssetService.AnalyzeOrgPolicies)`` |  Analyzes organization policies under a scope.  
``[AnalyzeOrgPolicyGovernedAssets](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.AssetService.AnalyzeOrgPolicyGovernedAssets)`` |  Analyzes organization policies governed assets (Google Cloud resources or policies) under a scope.  
``[AnalyzeOrgPolicyGovernedContainers](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.AssetService.AnalyzeOrgPolicyGovernedContainers)`` |  Analyzes organization policies governed containers (projects, folders or organization) under a scope.  
``[BatchGetAssetsHistory](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.AssetService.BatchGetAssetsHistory)`` |  Batch gets the update history of assets that overlap a time window.  
``[BatchGetEffectiveIamPolicies](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.AssetService.BatchGetEffectiveIamPolicies)`` |  Gets effective IAM policies for a batch of resources.  
``[CreateFeed](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.AssetService.CreateFeed)`` |  Creates a feed in a parent project/folder/organization to listen to its asset updates.  
``[CreateSavedQuery](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.AssetService.CreateSavedQuery)`` |  Creates a saved query in a parent project/folder/organization.  
``[DeleteFeed](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.AssetService.DeleteFeed)`` |  Deletes an asset feed.  
``[DeleteSavedQuery](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.AssetService.DeleteSavedQuery)`` |  Deletes a saved query.  
``[ExportAssets](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.AssetService.ExportAssets)`` |  Exports assets with time and resource types to a given Cloud Storage location/BigQuery table.  
``[GetFeed](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.AssetService.GetFeed)`` |  Gets details about an asset feed.  
``[GetSavedQuery](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.AssetService.GetSavedQuery)`` |  Gets details about a saved query.  
``[ListAssets](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.AssetService.ListAssets)`` |  Lists assets with time and resource types and returns paged results in response.  
``[ListFeeds](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.AssetService.ListFeeds)`` |  Lists all asset feeds in a parent project/folder/organization.  
``[ListSavedQueries](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.AssetService.ListSavedQueries)`` |  Lists all saved queries in a parent project/folder/organization.  
``[QueryAssets](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.AssetService.QueryAssets)`` |  Issue a job that queries assets using a SQL statement compatible with [BigQuery SQL](https://cloud.google.com/bigquery/docs/introduction-sql).  
``[SearchAllIamPolicies](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.AssetService.SearchAllIamPolicies)`` |  Searches all IAM policies within the specified scope, such as a project, folder, or organization.  
``[SearchAllResources](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.AssetService.SearchAllResources)`` |  Searches all Google Cloud resources within the specified scope, such as a project, folder, or organization.  
``[UpdateFeed](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.AssetService.UpdateFeed)`` |  Updates an asset feed configuration.  
``[UpdateSavedQuery](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.AssetService.UpdateSavedQuery)`` |  Updates a saved query.  
  
## `[google.cloud.asset.v1p1beta1.AssetService](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1p1beta1#google.cloud.asset.v1p1beta1.AssetService)`

Methods  
---  
``[SearchAllIamPolicies](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1p1beta1#google.cloud.asset.v1p1beta1.AssetService.SearchAllIamPolicies)`` |  Searches all the IAM policies within a given accessible Resource Manager scope (project/folder/organization).  
``[SearchAllResources](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1p1beta1#google.cloud.asset.v1p1beta1.AssetService.SearchAllResources)`` |  Searches all the resources within a given accessible Resource Manager scope (project/folder/organization).  
  
## `[google.cloud.asset.v1p2beta1.AssetService](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1p2beta1#google.cloud.asset.v1p2beta1.AssetService)`

Methods  
---  
``[CreateFeed](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1p2beta1#google.cloud.asset.v1p2beta1.AssetService.CreateFeed)`` |  Creates a feed in a parent project/folder/organization to listen to its asset updates.  
``[DeleteFeed](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1p2beta1#google.cloud.asset.v1p2beta1.AssetService.DeleteFeed)`` |  Deletes an asset feed.  
``[GetFeed](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1p2beta1#google.cloud.asset.v1p2beta1.AssetService.GetFeed)`` |  Gets details about an asset feed.  
``[ListFeeds](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1p2beta1#google.cloud.asset.v1p2beta1.AssetService.ListFeeds)`` |  Lists all asset feeds in a parent project/folder/organization.  
``[UpdateFeed](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1p2beta1#google.cloud.asset.v1p2beta1.AssetService.UpdateFeed)`` |  Updates an asset feed configuration.  
  
## `[google.cloud.asset.v1p7beta1.AssetService](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1p7beta1#google.cloud.asset.v1p7beta1.AssetService)`

Methods  
---  
``[ExportAssets](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1p7beta1#google.cloud.asset.v1p7beta1.AssetService.ExportAssets)`` |  Exports assets with time and resource types to a given Cloud Storage location/BigQuery table.  
  
## `[google.longrunning.Operations](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.longrunning#google.longrunning.Operations)`

Methods  
---  
``[GetOperation](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.longrunning#google.longrunning.Operations.GetOperation)`` |  Gets the latest state of a long-running operation.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-05-08 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-08 UTC."],[],[]] 
