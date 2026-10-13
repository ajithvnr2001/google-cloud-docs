---
url: https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1
title: Package google.cloud.asset.v1 \u00a0|\u00a0 Cloud Asset Inventory \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:30:11.153423+00:00
---

# Package google.cloud.asset.v1  |  Cloud Asset Inventory  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Cloud Asset Inventory ](https://docs.cloud.google.com/asset-inventory/docs)
  * [ Reference ](https://docs.cloud.google.com/asset-inventory/docs/asset-types)



Send feedback 

#  Package google.cloud.asset.v1 Stay organized with collections  Save and categorize content based on your preferences. 

## Index

  * `[AssetService](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.AssetService)` (interface)
  * `[AnalyzeIamPolicyLongrunningMetadata](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.AnalyzeIamPolicyLongrunningMetadata)` (message)
  * `[AnalyzeIamPolicyLongrunningRequest](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.AnalyzeIamPolicyLongrunningRequest)` (message)
  * `[AnalyzeIamPolicyLongrunningResponse](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.AnalyzeIamPolicyLongrunningResponse)` (message)
  * `[AnalyzeIamPolicyRequest](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.AnalyzeIamPolicyRequest)` (message)
  * `[AnalyzeIamPolicyResponse](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.AnalyzeIamPolicyResponse)` (message)
  * `[AnalyzeIamPolicyResponse.IamPolicyAnalysis](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.AnalyzeIamPolicyResponse.IamPolicyAnalysis)` (message)
  * `[AnalyzeMoveRequest](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.AnalyzeMoveRequest)` (message)
  * `[AnalyzeMoveRequest.AnalysisView](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.AnalyzeMoveRequest.AnalysisView)` (enum)
  * `[AnalyzeMoveResponse](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.AnalyzeMoveResponse)` (message)
  * `[AnalyzeOrgPoliciesRequest](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.AnalyzeOrgPoliciesRequest)` (message)
  * `[AnalyzeOrgPoliciesResponse](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.AnalyzeOrgPoliciesResponse)` (message)
  * `[AnalyzeOrgPoliciesResponse.OrgPolicyResult](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.AnalyzeOrgPoliciesResponse.OrgPolicyResult)` (message)
  * `[AnalyzeOrgPolicyGovernedAssetsRequest](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.AnalyzeOrgPolicyGovernedAssetsRequest)` (message)
  * `[AnalyzeOrgPolicyGovernedAssetsResponse](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.AnalyzeOrgPolicyGovernedAssetsResponse)` (message)
  * `[AnalyzeOrgPolicyGovernedAssetsResponse.GovernedAsset](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.AnalyzeOrgPolicyGovernedAssetsResponse.GovernedAsset)` (message)
  * `[AnalyzeOrgPolicyGovernedAssetsResponse.GovernedIamPolicy](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.AnalyzeOrgPolicyGovernedAssetsResponse.GovernedIamPolicy)` (message)
  * `[AnalyzeOrgPolicyGovernedAssetsResponse.GovernedResource](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.AnalyzeOrgPolicyGovernedAssetsResponse.GovernedResource)` (message)
  * `[AnalyzeOrgPolicyGovernedContainersRequest](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.AnalyzeOrgPolicyGovernedContainersRequest)` (message)
  * `[AnalyzeOrgPolicyGovernedContainersResponse](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.AnalyzeOrgPolicyGovernedContainersResponse)` (message)
  * `[AnalyzeOrgPolicyGovernedContainersResponse.GovernedContainer](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.AnalyzeOrgPolicyGovernedContainersResponse.GovernedContainer)` (message)
  * `[AnalyzerOrgPolicy](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.AnalyzerOrgPolicy)` (message)
  * `[AnalyzerOrgPolicy.Rule](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.AnalyzerOrgPolicy.Rule)` (message)
  * `[AnalyzerOrgPolicy.Rule.StringValues](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.AnalyzerOrgPolicy.Rule.StringValues)` (message)
  * `[AnalyzerOrgPolicyConstraint](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.AnalyzerOrgPolicyConstraint)` (message)
  * `[AnalyzerOrgPolicyConstraint.Constraint](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.AnalyzerOrgPolicyConstraint.Constraint)` (message)
  * `[AnalyzerOrgPolicyConstraint.Constraint.BooleanConstraint](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.AnalyzerOrgPolicyConstraint.Constraint.BooleanConstraint)` (message)
  * `[AnalyzerOrgPolicyConstraint.Constraint.ConstraintDefault](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.AnalyzerOrgPolicyConstraint.Constraint.ConstraintDefault)` (enum)
  * `[AnalyzerOrgPolicyConstraint.Constraint.ListConstraint](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.AnalyzerOrgPolicyConstraint.Constraint.ListConstraint)` (message)
  * `[AnalyzerOrgPolicyConstraint.CustomConstraint](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.AnalyzerOrgPolicyConstraint.CustomConstraint)` (message)
  * `[AnalyzerOrgPolicyConstraint.CustomConstraint.ActionType](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.AnalyzerOrgPolicyConstraint.CustomConstraint.ActionType)` (enum)
  * `[AnalyzerOrgPolicyConstraint.CustomConstraint.MethodType](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.AnalyzerOrgPolicyConstraint.CustomConstraint.MethodType)` (enum)
  * `[Asset](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.Asset)` (message)
  * `[AssetEnrichment](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.AssetEnrichment)` (message)
  * `[AssetException](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.AssetException)` (message)
  * `[AssetException.ExceptionType](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.AssetException.ExceptionType)` (enum)
  * `[AttachedResource](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.AttachedResource)` (message)
  * `[BatchGetAssetsHistoryRequest](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.BatchGetAssetsHistoryRequest)` (message)
  * `[BatchGetAssetsHistoryResponse](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.BatchGetAssetsHistoryResponse)` (message)
  * `[BatchGetEffectiveIamPoliciesRequest](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.BatchGetEffectiveIamPoliciesRequest)` (message)
  * `[BatchGetEffectiveIamPoliciesResponse](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.BatchGetEffectiveIamPoliciesResponse)` (message)
  * `[BatchGetEffectiveIamPoliciesResponse.EffectiveIamPolicy](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.BatchGetEffectiveIamPoliciesResponse.EffectiveIamPolicy)` (message)
  * `[BatchGetEffectiveIamPoliciesResponse.EffectiveIamPolicy.PolicyInfo](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.BatchGetEffectiveIamPoliciesResponse.EffectiveIamPolicy.PolicyInfo)` (message)
  * `[BigQueryDestination](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.BigQueryDestination)` (message)
  * `[ConditionEvaluation](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.ConditionEvaluation)` (message)
  * `[ConditionEvaluation.EvaluationValue](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.ConditionEvaluation.EvaluationValue)` (enum)
  * `[ContentType](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.ContentType)` (enum)
  * `[CreateFeedRequest](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.CreateFeedRequest)` (message)
  * `[CreateSavedQueryRequest](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.CreateSavedQueryRequest)` (message)
  * `[DeleteFeedRequest](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.DeleteFeedRequest)` (message)
  * `[DeleteSavedQueryRequest](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.DeleteSavedQueryRequest)` (message)
  * `[EffectiveTagDetails](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.EffectiveTagDetails)` (message)
  * `[ExportAssetsRequest](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.ExportAssetsRequest)` (message)
  * `[ExportAssetsResponse](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.ExportAssetsResponse)` (message)
  * `[Feed](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.Feed)` (message)
  * `[FeedOutputConfig](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.FeedOutputConfig)` (message)
  * `[GcsDestination](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.GcsDestination)` (message)
  * `[GcsOutputResult](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.GcsOutputResult)` (message)
  * `[GetFeedRequest](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.GetFeedRequest)` (message)
  * `[GetSavedQueryRequest](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.GetSavedQueryRequest)` (message)
  * `[IamPolicyAnalysisOutputConfig](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.IamPolicyAnalysisOutputConfig)` (message)
  * `[IamPolicyAnalysisOutputConfig.BigQueryDestination](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.IamPolicyAnalysisOutputConfig.BigQueryDestination)` (message)
  * `[IamPolicyAnalysisOutputConfig.BigQueryDestination.PartitionKey](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.IamPolicyAnalysisOutputConfig.BigQueryDestination.PartitionKey)` (enum)
  * `[IamPolicyAnalysisOutputConfig.GcsDestination](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.IamPolicyAnalysisOutputConfig.GcsDestination)` (message)
  * `[IamPolicyAnalysisQuery](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.IamPolicyAnalysisQuery)` (message)
  * `[IamPolicyAnalysisQuery.AccessSelector](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.IamPolicyAnalysisQuery.AccessSelector)` (message)
  * `[IamPolicyAnalysisQuery.ConditionContext](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.IamPolicyAnalysisQuery.ConditionContext)` (message)
  * `[IamPolicyAnalysisQuery.IdentitySelector](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.IamPolicyAnalysisQuery.IdentitySelector)` (message)
  * `[IamPolicyAnalysisQuery.Options](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.IamPolicyAnalysisQuery.Options)` (message)
  * `[IamPolicyAnalysisQuery.ResourceSelector](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.IamPolicyAnalysisQuery.ResourceSelector)` (message)
  * `[IamPolicyAnalysisResult](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.IamPolicyAnalysisResult)` (message)
  * `[IamPolicyAnalysisResult.Access](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.IamPolicyAnalysisResult.Access)` (message)
  * `[IamPolicyAnalysisResult.AccessControlList](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.IamPolicyAnalysisResult.AccessControlList)` (message)
  * `[IamPolicyAnalysisResult.Edge](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.IamPolicyAnalysisResult.Edge)` (message)
  * `[IamPolicyAnalysisResult.Identity](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.IamPolicyAnalysisResult.Identity)` (message)
  * `[IamPolicyAnalysisResult.IdentityList](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.IamPolicyAnalysisResult.IdentityList)` (message)
  * `[IamPolicyAnalysisResult.Resource](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.IamPolicyAnalysisResult.Resource)` (message)
  * `[IamPolicyAnalysisState](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.IamPolicyAnalysisState)` (message)
  * `[IamPolicySearchResult](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.IamPolicySearchResult)` (message)
  * `[IamPolicySearchResult.Explanation](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.IamPolicySearchResult.Explanation)` (message)
  * `[IamPolicySearchResult.Explanation.Permissions](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.IamPolicySearchResult.Explanation.Permissions)` (message)
  * `[ListAssetsRequest](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.ListAssetsRequest)` (message)
  * `[ListAssetsResponse](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.ListAssetsResponse)` (message)
  * `[ListFeedsRequest](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.ListFeedsRequest)` (message)
  * `[ListFeedsResponse](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.ListFeedsResponse)` (message)
  * `[ListSavedQueriesRequest](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.ListSavedQueriesRequest)` (message)
  * `[ListSavedQueriesResponse](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.ListSavedQueriesResponse)` (message)
  * `[MoveAnalysis](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.MoveAnalysis)` (message)
  * `[MoveAnalysisResult](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.MoveAnalysisResult)` (message)
  * `[MoveImpact](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.MoveImpact)` (message)
  * `[OutputConfig](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.OutputConfig)` (message)
  * `[OutputResult](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.OutputResult)` (message)
  * `[PartitionSpec](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.PartitionSpec)` (message)
  * `[PartitionSpec.PartitionKey](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.PartitionSpec.PartitionKey)` (enum)
  * `[PubsubDestination](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.PubsubDestination)` (message)
  * `[QueryAssetsOutputConfig](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.QueryAssetsOutputConfig)` (message)
  * `[QueryAssetsOutputConfig.BigQueryDestination](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.QueryAssetsOutputConfig.BigQueryDestination)` (message)
  * `[QueryAssetsRequest](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.QueryAssetsRequest)` (message)
  * `[QueryAssetsResponse](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.QueryAssetsResponse)` (message)
  * `[QueryResult](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.QueryResult)` (message)
  * `[RelatedAsset](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.RelatedAsset)` (message)
  * `[RelatedAssets](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.RelatedAssets)` (message) **(deprecated)**
  * `[RelatedResource](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.RelatedResource)` (message)
  * `[RelatedResources](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.RelatedResources)` (message)
  * `[RelationshipAttributes](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.RelationshipAttributes)` (message) **(deprecated)**
  * `[Resource](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.Resource)` (message)
  * `[ResourceOwners](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.ResourceOwners)` (message)
  * `[ResourceSearchResult](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.ResourceSearchResult)` (message)
  * `[SavedQuery](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.SavedQuery)` (message)
  * `[SavedQuery.QueryContent](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.SavedQuery.QueryContent)` (message)
  * `[SearchAllIamPoliciesRequest](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.SearchAllIamPoliciesRequest)` (message)
  * `[SearchAllIamPoliciesResponse](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.SearchAllIamPoliciesResponse)` (message)
  * `[SearchAllResourcesRequest](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.SearchAllResourcesRequest)` (message)
  * `[SearchAllResourcesResponse](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.SearchAllResourcesResponse)` (message)
  * `[TableFieldSchema](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.TableFieldSchema)` (message)
  * `[TableSchema](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.TableSchema)` (message)
  * `[Tag](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.Tag)` (message)
  * `[TemporalAsset](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.TemporalAsset)` (message)
  * `[TemporalAsset.PriorAssetState](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.TemporalAsset.PriorAssetState)` (enum)
  * `[TimeWindow](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.TimeWindow)` (message)
  * `[UpdateFeedRequest](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.UpdateFeedRequest)` (message)
  * `[UpdateSavedQueryRequest](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.UpdateSavedQueryRequest)` (message)
  * `[VersionedResource](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.VersionedResource)` (message)



## AssetService

Asset service definition.

AnalyzeIamPolicy  
---  
` rpc AnalyzeIamPolicy(`[AnalyzeIamPolicyRequest](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.AnalyzeIamPolicyRequest)`) returns (`[AnalyzeIamPolicyResponse](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.AnalyzeIamPolicyResponse)`) ` Analyzes IAM policies to answer which identities have what accesses on which resources.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
AnalyzeIamPolicyLongrunning  
---  
` rpc AnalyzeIamPolicyLongrunning(`[AnalyzeIamPolicyLongrunningRequest](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.AnalyzeIamPolicyLongrunningRequest)`) returns (`[Operation](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.longrunning#google.longrunning.Operation)`) ` Analyzes IAM policies asynchronously to answer which identities have what accesses on which resources, and writes the analysis results to a Google Cloud Storage or a BigQuery destination. For Cloud Storage destination, the output format is the JSON format that represents a `[AnalyzeIamPolicyResponse](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.AnalyzeIamPolicyResponse)`. This method implements the `[google.longrunning.Operation](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.longrunning#google.longrunning.Operation)`, which allows you to track the operation status. We recommend intervals of at least 2 seconds with exponential backoff retry to poll the operation result. The metadata contains the metadata for the long-running operation.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
AnalyzeMove  
---  
` rpc AnalyzeMove(`[AnalyzeMoveRequest](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.AnalyzeMoveRequest)`) returns (`[AnalyzeMoveResponse](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.AnalyzeMoveResponse)`) ` Analyze moving a resource to a specified destination without kicking off the actual move. The analysis is best effort depending on the user's permissions of viewing different hierarchical policies and configurations. The policies and configuration are subject to change before the actual resource migration takes place.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
AnalyzeOrgPolicies  
---  
` rpc AnalyzeOrgPolicies(`[AnalyzeOrgPoliciesRequest](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.AnalyzeOrgPoliciesRequest)`) returns (`[AnalyzeOrgPoliciesResponse](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.AnalyzeOrgPoliciesResponse)`) ` Analyzes organization policies under a scope.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
AnalyzeOrgPolicyGovernedAssets  
---  
` rpc AnalyzeOrgPolicyGovernedAssets(`[AnalyzeOrgPolicyGovernedAssetsRequest](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.AnalyzeOrgPolicyGovernedAssetsRequest)`) returns (`[AnalyzeOrgPolicyGovernedAssetsResponse](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.AnalyzeOrgPolicyGovernedAssetsResponse)`) ` Analyzes organization policies governed assets (Google Cloud resources or policies) under a scope. This RPC supports custom constraints and the following canned constraints:

  * constraints/ainotebooks.accessMode
  * constraints/ainotebooks.disableFileDownloads
  * constraints/ainotebooks.disableRootAccess
  * constraints/ainotebooks.disableTerminal
  * constraints/ainotebooks.environmentOptions
  * constraints/ainotebooks.requireAutoUpgradeSchedule
  * constraints/ainotebooks.restrictVpcNetworks
  * constraints/compute.disableGuestAttributesAccess
  * constraints/compute.disableInstanceDataAccessApis
  * constraints/compute.disableNestedVirtualization
  * constraints/compute.disableSerialPortAccess
  * constraints/compute.disableSerialPortLogging
  * constraints/compute.disableVpcExternalIpv6
  * constraints/compute.requireOsLogin
  * constraints/compute.requireShieldedVm
  * constraints/compute.restrictLoadBalancerCreationForTypes
  * constraints/compute.restrictProtocolForwardingCreationForTypes
  * constraints/compute.restrictXpnProjectLienRemoval
  * constraints/compute.setNewProjectDefaultToZonalDNSOnly
  * constraints/compute.skipDefaultNetworkCreation
  * constraints/compute.trustedImageProjects
  * constraints/compute.vmCanIpForward
  * constraints/compute.vmExternalIpAccess
  * constraints/gcp.detailedAuditLoggingMode
  * constraints/gcp.resourceLocations
  * constraints/iam.allowedPolicyMemberDomains
  * constraints/iam.automaticIamGrantsForDefaultServiceAccounts
  * constraints/iam.disableServiceAccountCreation
  * constraints/iam.disableServiceAccountKeyCreation
  * constraints/iam.disableServiceAccountKeyUpload
  * constraints/iam.restrictCrossProjectServiceAccountLienRemoval
  * constraints/iam.serviceAccountKeyExpiryHours
  * constraints/resourcemanager.accessBoundaries
  * constraints/resourcemanager.allowedExportDestinations
  * constraints/sql.restrictAuthorizedNetworks
  * constraints/sql.restrictNoncompliantDiagnosticDataAccess
  * constraints/sql.restrictNoncompliantResourceCreation
  * constraints/sql.restrictPublicIp
  * constraints/storage.publicAccessPrevention
  * constraints/storage.restrictAuthTypes
  * constraints/storage.uniformBucketLevelAccess

This RPC only returns either resources of types [supported by search APIs](https://cloud.google.com/asset-inventory/docs/supported-asset-types) or IAM policies.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
AnalyzeOrgPolicyGovernedContainers  
---  
` rpc AnalyzeOrgPolicyGovernedContainers(`[AnalyzeOrgPolicyGovernedContainersRequest](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.AnalyzeOrgPolicyGovernedContainersRequest)`) returns (`[AnalyzeOrgPolicyGovernedContainersResponse](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.AnalyzeOrgPolicyGovernedContainersResponse)`) ` Analyzes organization policies governed containers (projects, folders or organization) under a scope.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
BatchGetAssetsHistory  
---  
` rpc BatchGetAssetsHistory(`[BatchGetAssetsHistoryRequest](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.BatchGetAssetsHistoryRequest)`) returns (`[BatchGetAssetsHistoryResponse](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.BatchGetAssetsHistoryResponse)`) ` Batch gets the update history of assets that overlap a time window. For IAM_POLICY content, this API outputs history when the asset and its attached IAM POLICY both exist. This can create gaps in the output history. Otherwise, this API outputs history with asset in both non-delete or deleted status. If a specified asset does not exist, this API returns an INVALID_ARGUMENT error.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
BatchGetEffectiveIamPolicies  
---  
` rpc BatchGetEffectiveIamPolicies(`[BatchGetEffectiveIamPoliciesRequest](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.BatchGetEffectiveIamPoliciesRequest)`) returns (`[BatchGetEffectiveIamPoliciesResponse](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.BatchGetEffectiveIamPoliciesResponse)`) ` Gets effective IAM policies for a batch of resources.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
CreateFeed  
---  
` rpc CreateFeed(`[CreateFeedRequest](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.CreateFeedRequest)`) returns (`[Feed](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.Feed)`) ` Creates a feed in a parent project/folder/organization to listen to its asset updates.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
CreateSavedQuery  
---  
` rpc CreateSavedQuery(`[CreateSavedQueryRequest](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.CreateSavedQueryRequest)`) returns (`[SavedQuery](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.SavedQuery)`) ` Creates a saved query in a parent project/folder/organization.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
DeleteFeed  
---  
` rpc DeleteFeed(`[DeleteFeedRequest](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.DeleteFeedRequest)`) returns (`[Empty](https://protobuf.dev/reference/protobuf/google.protobuf/#empty)`) ` Deletes an asset feed.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
DeleteSavedQuery  
---  
` rpc DeleteSavedQuery(`[DeleteSavedQueryRequest](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.DeleteSavedQueryRequest)`) returns (`[Empty](https://protobuf.dev/reference/protobuf/google.protobuf/#empty)`) ` Deletes a saved query.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
ExportAssets  
---  
` rpc ExportAssets(`[ExportAssetsRequest](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.ExportAssetsRequest)`) returns (`[Operation](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.longrunning#google.longrunning.Operation)`) ` Exports assets with time and resource types to a given Cloud Storage location/BigQuery table. For Cloud Storage location destinations, the output format is newline-delimited JSON. Each line represents a `[google.cloud.asset.v1.Asset](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.Asset)` in the JSON format; for BigQuery table destinations, the output table stores the fields in asset Protobuf as columns. This API implements the `[google.longrunning.Operation](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.longrunning#google.longrunning.Operation)` API, which allows you to keep track of the export. We recommend intervals of at least 2 seconds with exponential retry to poll the export operation result. For regular-size resource parent, the export operation usually finishes within 5 minutes.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
GetFeed  
---  
` rpc GetFeed(`[GetFeedRequest](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.GetFeedRequest)`) returns (`[Feed](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.Feed)`) ` Gets details about an asset feed.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
GetSavedQuery  
---  
` rpc GetSavedQuery(`[GetSavedQueryRequest](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.GetSavedQueryRequest)`) returns (`[SavedQuery](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.SavedQuery)`) ` Gets details about a saved query.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
ListAssets  
---  
` rpc ListAssets(`[ListAssetsRequest](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.ListAssetsRequest)`) returns (`[ListAssetsResponse](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.ListAssetsResponse)`) ` Lists assets with time and resource types and returns paged results in response.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
ListFeeds  
---  
` rpc ListFeeds(`[ListFeedsRequest](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.ListFeedsRequest)`) returns (`[ListFeedsResponse](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.ListFeedsResponse)`) ` Lists all asset feeds in a parent project/folder/organization.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
ListSavedQueries  
---  
` rpc ListSavedQueries(`[ListSavedQueriesRequest](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.ListSavedQueriesRequest)`) returns (`[ListSavedQueriesResponse](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.ListSavedQueriesResponse)`) ` Lists all saved queries in a parent project/folder/organization.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
QueryAssets  
---  
` rpc QueryAssets(`[QueryAssetsRequest](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.QueryAssetsRequest)`) returns (`[QueryAssetsResponse](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.QueryAssetsResponse)`) ` Issue a job that queries assets using a SQL statement compatible with [BigQuery SQL](https://cloud.google.com/bigquery/docs/introduction-sql).If the query execution finishes within timeout and there's no pagination, the full query results will be returned in the `QueryAssetsResponse`.Otherwise, full query results can be obtained by issuing extra requests with the `job_reference` from the a previous `QueryAssets` call.Note, the query result has approximately 10 GB limitation enforced by [BigQuery](https://cloud.google.com/bigquery/docs/best-practices-performance-output). Queries return larger results will result in errors.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
SearchAllIamPolicies  
---  
` rpc SearchAllIamPolicies(`[SearchAllIamPoliciesRequest](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.SearchAllIamPoliciesRequest)`) returns (`[SearchAllIamPoliciesResponse](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.SearchAllIamPoliciesResponse)`) ` Searches all IAM policies within the specified scope, such as a project, folder, or organization. The caller must be granted the `cloudasset.assets.searchAllIamPolicies` permission on the desired scope, otherwise the request will be rejected.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
SearchAllResources  
---  
` rpc SearchAllResources(`[SearchAllResourcesRequest](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.SearchAllResourcesRequest)`) returns (`[SearchAllResourcesResponse](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.SearchAllResourcesResponse)`) ` Searches all Google Cloud resources within the specified scope, such as a project, folder, or organization. The caller must be granted the `cloudasset.assets.searchAllResources` permission on the desired scope, otherwise the request will be rejected.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
UpdateFeed  
---  
` rpc UpdateFeed(`[UpdateFeedRequest](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.UpdateFeedRequest)`) returns (`[Feed](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.Feed)`) ` Updates an asset feed configuration.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
UpdateSavedQuery  
---  
` rpc UpdateSavedQuery(`[UpdateSavedQueryRequest](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.UpdateSavedQueryRequest)`) returns (`[SavedQuery](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.SavedQuery)`) ` Updates a saved query.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
  
## AnalyzeIamPolicyLongrunningMetadata

Represents the metadata of the longrunning operation for the AnalyzeIamPolicyLongrunning RPC.

Fields  
---  
`create_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. The time the operation was created.  
  
## AnalyzeIamPolicyLongrunningRequest

A request message for `[AssetService.AnalyzeIamPolicyLongrunning](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.AssetService.AnalyzeIamPolicyLongrunning)`.

Fields  
---  
`analysis_query` |  `[IamPolicyAnalysisQuery](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.IamPolicyAnalysisQuery)` Required. The request query.  
`saved_analysis_query` |  `string` Optional. The name of a saved query, which must be in the format of:

  * projects/project_number/savedQueries/saved_query_id
  * folders/folder_number/savedQueries/saved_query_id
  * organizations/organization_number/savedQueries/saved_query_id

If both `analysis_query` and `saved_analysis_query` are provided, they will be merged together with the `saved_analysis_query` as base and the `analysis_query` as overrides. For more details of the merge behavior, refer to the [MergeFrom](https://developers.google.com/protocol-buffers/docs/reference/cpp/google.protobuf.message#Message.MergeFrom.details) doc.Note that you cannot override primitive fields with default value, such as 0 or empty string, etc., because we use proto3, which doesn't support field presence yet.  
`output_config` |  `[IamPolicyAnalysisOutputConfig](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.IamPolicyAnalysisOutputConfig)` Required. Output configuration indicating where the results will be output to.  
  
## AnalyzeIamPolicyLongrunningResponse

This type has no fields.

A response message for `[AssetService.AnalyzeIamPolicyLongrunning](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.AssetService.AnalyzeIamPolicyLongrunning)`.

## AnalyzeIamPolicyRequest

A request message for `[AssetService.AnalyzeIamPolicy](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.AssetService.AnalyzeIamPolicy)`.

Fields  
---  
`analysis_query` |  `[IamPolicyAnalysisQuery](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.IamPolicyAnalysisQuery)` Required. The request query.  
`saved_analysis_query` |  `string` Optional. The name of a saved query, which must be in the format of:

  * projects/project_number/savedQueries/saved_query_id
  * folders/folder_number/savedQueries/saved_query_id
  * organizations/organization_number/savedQueries/saved_query_id

If both `analysis_query` and `saved_analysis_query` are provided, they will be merged together with the `saved_analysis_query` as base and the `analysis_query` as overrides. For more details of the merge behavior, refer to the [MergeFrom](https://developers.google.com/protocol-buffers/docs/reference/cpp/google.protobuf.message#Message.MergeFrom.details) page.Note that you cannot override primitive fields with default value, such as 0 or empty string, etc., because we use proto3, which doesn't support field presence yet.  
`execution_timeout` |  `[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` Optional. Amount of time executable has to complete. See JSON representation of [Duration](https://developers.google.com/protocol-buffers/docs/proto3#json).If this field is set with a value less than the RPC deadline, and the execution of your query hasn't finished in the specified execution timeout, you will get a response with partial result. Otherwise, your query's execution will continue until the RPC deadline. If it's not finished until then, you will get a DEADLINE_EXCEEDED error.Default is empty.  
  
## AnalyzeIamPolicyResponse

A response message for `[AssetService.AnalyzeIamPolicy](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.AssetService.AnalyzeIamPolicy)`.

Fields  
---  
`main_analysis` |  `[IamPolicyAnalysis](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.AnalyzeIamPolicyResponse.IamPolicyAnalysis)` The main analysis that matches the original request.  
`service_account_impersonation_analysis[]` |  `[IamPolicyAnalysis](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.AnalyzeIamPolicyResponse.IamPolicyAnalysis)` The service account impersonation analysis if `[IamPolicyAnalysisQuery.Options.analyze_service_account_impersonation](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.IamPolicyAnalysisQuery.Options.FIELDS.bool.google.cloud.asset.v1.IamPolicyAnalysisQuery.Options.analyze_service_account_impersonation)` is enabled.  
`fully_explored` |  `bool` Represents whether all entries in the `[main_analysis](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.AnalyzeIamPolicyResponse.FIELDS.google.cloud.asset.v1.AnalyzeIamPolicyResponse.IamPolicyAnalysis.google.cloud.asset.v1.AnalyzeIamPolicyResponse.main_analysis)` and `[service_account_impersonation_analysis](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.AnalyzeIamPolicyResponse.FIELDS.repeated.google.cloud.asset.v1.AnalyzeIamPolicyResponse.IamPolicyAnalysis.google.cloud.asset.v1.AnalyzeIamPolicyResponse.service_account_impersonation_analysis)` have been fully explored to answer the query in the request.  
  
## IamPolicyAnalysis

An analysis message to group the query and results.

Fields  
---  
`analysis_query` |  `[IamPolicyAnalysisQuery](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.IamPolicyAnalysisQuery)` The analysis query.  
`analysis_results[]` |  `[IamPolicyAnalysisResult](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.IamPolicyAnalysisResult)` A list of `[IamPolicyAnalysisResult](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.IamPolicyAnalysisResult)` that matches the analysis query, or empty if no result is found.  
`fully_explored` |  `bool` Represents whether all entries in the `[analysis_results](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.AnalyzeIamPolicyResponse.IamPolicyAnalysis.FIELDS.repeated.google.cloud.asset.v1.IamPolicyAnalysisResult.google.cloud.asset.v1.AnalyzeIamPolicyResponse.IamPolicyAnalysis.analysis_results)` have been fully explored to answer the query.  
`non_critical_errors[]` |  `[IamPolicyAnalysisState](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.IamPolicyAnalysisState)` A list of non-critical errors happened during the query handling.  
  
## AnalyzeMoveRequest

The request message for performing resource move analysis.

Fields  
---  
`resource` |  `string` Required. Name of the resource to perform the analysis against. Only Google Cloud projects are supported as of today. Hence, this can only be a project ID (such as "projects/my-project-id") or a project number (such as "projects/12345").  
`destination_parent` |  `string` Required. Name of the Google Cloud folder or organization to reparent the target resource. The analysis will be performed against hypothetically moving the resource to this specified destination parent. This can only be a folder number (such as "folders/123") or an organization number (such as "organizations/123").  
`view` |  `[AnalysisView](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.AnalyzeMoveRequest.AnalysisView)` Analysis view indicating what information should be included in the analysis response. If unspecified, the default view is FULL.  
  
## AnalysisView

View enum for supporting partial analysis responses.

Enums  
---  
`ANALYSIS_VIEW_UNSPECIFIED` | The default/unset value. The API will default to the FULL view.  
`FULL` | Full analysis including all level of impacts of the specified resource move.  
`BASIC` | Basic analysis only including blockers which will prevent the specified resource move at runtime.  
  
## AnalyzeMoveResponse

The response message for resource move analysis.

Fields  
---  
`move_analysis[]` |  `[MoveAnalysis](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.MoveAnalysis)` The list of analyses returned from performing the intended resource move analysis. The analysis is grouped by different Google Cloud services.  
  
## AnalyzeOrgPoliciesRequest

A request message for `[AssetService.AnalyzeOrgPolicies](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.AssetService.AnalyzeOrgPolicies)`.

Fields  
---  
`scope` |  `string` Required. The organization to scope the request. Only organization policies within the scope will be analyzed.

  * organizations/{ORGANIZATION_NUMBER} (e.g., "organizations/123456")

Authorization requires one or more of the following [IAM](https://cloud.google.com/iam/docs/) permissions on the specified resource `scope`:

  * `cloudasset.assets.searchAllResources`
  * `cloudasset.assets.analyzeOrgPolicy`

  
`constraint` |  `string` Required. The name of the constraint to analyze organization policies for. The response only contains analyzed organization policies for the provided constraint.  
`filter` |  `string` The expression to filter `[AnalyzeOrgPoliciesResponse.org_policy_results](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.AnalyzeOrgPoliciesResponse.FIELDS.repeated.google.cloud.asset.v1.AnalyzeOrgPoliciesResponse.OrgPolicyResult.google.cloud.asset.v1.AnalyzeOrgPoliciesResponse.org_policy_results)`. Filtering is currently available for bare literal values and the following fields: * consolidated_policy.attached_resource * consolidated_policy.rules.enforceWhen filtering by a specific field, the only supported operator is `=`. For example, filtering by consolidated_policy.attached_resource="//cloudresourcemanager.googleapis.com/folders/001" will return all the Organization Policy results attached to "folders/001".  
`page_token` |  `string` The pagination token to retrieve the next page.  
`page_size` |  `int32` The maximum number of items to return per page. If unspecified, `[AnalyzeOrgPoliciesResponse.org_policy_results](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.AnalyzeOrgPoliciesResponse.FIELDS.repeated.google.cloud.asset.v1.AnalyzeOrgPoliciesResponse.OrgPolicyResult.google.cloud.asset.v1.AnalyzeOrgPoliciesResponse.org_policy_results)` will contain 20 items with a maximum of 200.  
  
## AnalyzeOrgPoliciesResponse

The response message for `[AssetService.AnalyzeOrgPolicies](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.AssetService.AnalyzeOrgPolicies)`.

Fields  
---  
`org_policy_results[]` |  `[OrgPolicyResult](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.AnalyzeOrgPoliciesResponse.OrgPolicyResult)` The organization policies under the `[AnalyzeOrgPoliciesRequest.scope](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.AnalyzeOrgPoliciesRequest.FIELDS.string.google.cloud.asset.v1.AnalyzeOrgPoliciesRequest.scope)` with the `[AnalyzeOrgPoliciesRequest.constraint](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.AnalyzeOrgPoliciesRequest.FIELDS.string.google.cloud.asset.v1.AnalyzeOrgPoliciesRequest.constraint)`.  
`constraint` |  `[AnalyzerOrgPolicyConstraint](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.AnalyzerOrgPolicyConstraint)` The definition of the constraint in the request.  
`next_page_token` |  `string` The page token to fetch the next page for `[AnalyzeOrgPoliciesResponse.org_policy_results](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.AnalyzeOrgPoliciesResponse.FIELDS.repeated.google.cloud.asset.v1.AnalyzeOrgPoliciesResponse.OrgPolicyResult.google.cloud.asset.v1.AnalyzeOrgPoliciesResponse.org_policy_results)`.  
  
## OrgPolicyResult

The organization policy result to the query.

Fields  
---  
`consolidated_policy` |  `[AnalyzerOrgPolicy](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.AnalyzerOrgPolicy)` The consolidated organization policy for the analyzed resource. The consolidated organization policy is computed by merging and evaluating `[policy_bundle](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.AnalyzeOrgPoliciesResponse.OrgPolicyResult.FIELDS.repeated.google.cloud.asset.v1.AnalyzerOrgPolicy.google.cloud.asset.v1.AnalyzeOrgPoliciesResponse.OrgPolicyResult.policy_bundle)`. The evaluation will respect the organization policy [hierarchy rules](https://cloud.google.com/resource-manager/docs/organization-policy/understanding-hierarchy).  
`policy_bundle[]` |  `[AnalyzerOrgPolicy](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.AnalyzerOrgPolicy)` The ordered list of all organization policies from the `[consolidated_policy.attached_resource](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.AnalyzerOrgPolicy.FIELDS.string.google.cloud.asset.v1.AnalyzerOrgPolicy.attached_resource)`. to the scope specified in the request.If the constraint is defined with default policy, it will also appear in the list.  
`project` |  `string` The project that this consolidated policy belongs to, in the format of projects/{PROJECT_NUMBER}. This field is available when the consolidated policy belongs to a project.  
`folders[]` |  `string` The folder(s) that this consolidated policy belongs to, in the format of folders/{FOLDER_NUMBER}. This field is available when the consolidated policy belongs (directly or cascadingly) to one or more folders.  
`organization` |  `string` The organization that this consolidated policy belongs to, in the format of organizations/{ORGANIZATION_NUMBER}. This field is available when the consolidated policy belongs (directly or cascadingly) to an organization.  
  
## AnalyzeOrgPolicyGovernedAssetsRequest

A request message for `[AssetService.AnalyzeOrgPolicyGovernedAssets](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.AssetService.AnalyzeOrgPolicyGovernedAssets)`.

Fields  
---  
`scope` |  `string` Required. The organization to scope the request. Only organization policies within the scope will be analyzed. The output assets will also be limited to the ones governed by those in-scope organization policies.

  * organizations/{ORGANIZATION_NUMBER} (e.g., "organizations/123456")

Authorization requires one or more of the following [IAM](https://cloud.google.com/iam/docs/) permissions on the specified resource `scope`:

  * `cloudasset.assets.searchAllResources`
  * `cloudasset.assets.searchAllIamPolicies`
  * `cloudasset.assets.analyzeOrgPolicy`

  
`constraint` |  `string` Required. The name of the constraint to analyze governed assets for. The analysis only contains analyzed organization policies for the provided constraint.  
`filter` |  `string` The expression to filter `[AnalyzeOrgPolicyGovernedAssetsResponse.governed_assets](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.AnalyzeOrgPolicyGovernedAssetsResponse.FIELDS.repeated.google.cloud.asset.v1.AnalyzeOrgPolicyGovernedAssetsResponse.GovernedAsset.google.cloud.asset.v1.AnalyzeOrgPolicyGovernedAssetsResponse.governed_assets)`.For governed resources, filtering is currently available for bare literal values and the following fields: * governed_resource.project * governed_resource.folders * consolidated_policy.rules.enforce When filtering by `governed_resource.project` or `consolidated_policy.rules.enforce`, the only supported operator is `=`. When filtering by `governed_resource.folders`, the supported operators are `=` and `:`. For example, filtering by `governed_resource.project="projects/12345678"` will return all the governed resources under "projects/12345678", including the project itself if applicable.For governed IAM policies, filtering is currently available for bare literal values and the following fields: * governed_iam_policy.project * governed_iam_policy.folders * consolidated_policy.rules.enforce When filtering by `governed_iam_policy.project` or `consolidated_policy.rules.enforce`, the only supported operator is `=`. When filtering by `governed_iam_policy.folders`, the supported operators are `=` and `:`. For example, filtering by `governed_iam_policy.folders:"folders/12345678"` will return all the governed IAM policies under "folders/001".  
`page_token` |  `string` The pagination token to retrieve the next page.  
`page_size` |  `int32` The maximum number of items to return per page. If unspecified, `[AnalyzeOrgPolicyGovernedAssetsResponse.governed_assets](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.AnalyzeOrgPolicyGovernedAssetsResponse.FIELDS.repeated.google.cloud.asset.v1.AnalyzeOrgPolicyGovernedAssetsResponse.GovernedAsset.google.cloud.asset.v1.AnalyzeOrgPolicyGovernedAssetsResponse.governed_assets)` will contain 100 items with a maximum of 200.  
  
## AnalyzeOrgPolicyGovernedAssetsResponse

The response message for `[AssetService.AnalyzeOrgPolicyGovernedAssets](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.AssetService.AnalyzeOrgPolicyGovernedAssets)`.

Fields  
---  
`governed_assets[]` |  `[GovernedAsset](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.AnalyzeOrgPolicyGovernedAssetsResponse.GovernedAsset)` The list of the analyzed governed assets.  
`constraint` |  `[AnalyzerOrgPolicyConstraint](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.AnalyzerOrgPolicyConstraint)` The definition of the constraint in the request.  
`next_page_token` |  `string` The page token to fetch the next page for `[AnalyzeOrgPolicyGovernedAssetsResponse.governed_assets](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.AnalyzeOrgPolicyGovernedAssetsResponse.FIELDS.repeated.google.cloud.asset.v1.AnalyzeOrgPolicyGovernedAssetsResponse.GovernedAsset.google.cloud.asset.v1.AnalyzeOrgPolicyGovernedAssetsResponse.governed_assets)`.  
  
## GovernedAsset

Represents a Google Cloud asset(resource or IAM policy) governed by the organization policies of the `[AnalyzeOrgPolicyGovernedAssetsRequest.constraint](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.AnalyzeOrgPolicyGovernedAssetsRequest.FIELDS.string.google.cloud.asset.v1.AnalyzeOrgPolicyGovernedAssetsRequest.constraint)`.

Fields  
---  
`consolidated_policy` |  `[AnalyzerOrgPolicy](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.AnalyzerOrgPolicy)` The consolidated policy for the analyzed asset. The consolidated policy is computed by merging and evaluating `[AnalyzeOrgPolicyGovernedAssetsResponse.GovernedAsset.policy_bundle](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.AnalyzeOrgPolicyGovernedAssetsResponse.GovernedAsset.FIELDS.repeated.google.cloud.asset.v1.AnalyzerOrgPolicy.google.cloud.asset.v1.AnalyzeOrgPolicyGovernedAssetsResponse.GovernedAsset.policy_bundle)`. The evaluation will respect the organization policy [hierarchy rules](https://cloud.google.com/resource-manager/docs/organization-policy/understanding-hierarchy).  
`policy_bundle[]` |  `[AnalyzerOrgPolicy](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.AnalyzerOrgPolicy)` The ordered list of all organization policies from the `[consolidated_policy.attached_resource](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.AnalyzerOrgPolicy.FIELDS.string.google.cloud.asset.v1.AnalyzerOrgPolicy.attached_resource)` to the scope specified in the request.If the constraint is defined with default policy, it will also appear in the list.  
Union field `governed_asset`.`governed_asset` can be only one of the following:  
`governed_resource` |  `[GovernedResource](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.AnalyzeOrgPolicyGovernedAssetsResponse.GovernedResource)` A Google Cloud resource governed by the organization policies of the `[AnalyzeOrgPolicyGovernedAssetsRequest.constraint](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.AnalyzeOrgPolicyGovernedAssetsRequest.FIELDS.string.google.cloud.asset.v1.AnalyzeOrgPolicyGovernedAssetsRequest.constraint)`.  
`governed_iam_policy` |  `[GovernedIamPolicy](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.AnalyzeOrgPolicyGovernedAssetsResponse.GovernedIamPolicy)` An IAM policy governed by the organization policies of the `[AnalyzeOrgPolicyGovernedAssetsRequest.constraint](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.AnalyzeOrgPolicyGovernedAssetsRequest.FIELDS.string.google.cloud.asset.v1.AnalyzeOrgPolicyGovernedAssetsRequest.constraint)`.  
  
## GovernedIamPolicy

The IAM policies governed by the organization policies of the `[AnalyzeOrgPolicyGovernedAssetsRequest.constraint](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.AnalyzeOrgPolicyGovernedAssetsRequest.FIELDS.string.google.cloud.asset.v1.AnalyzeOrgPolicyGovernedAssetsRequest.constraint)`.

Fields  
---  
`attached_resource` |  `string` The full resource name of the resource on which this IAM policy is set. Example: `//compute.googleapis.com/projects/my_project_123/zones/zone1/instances/instance1`. See [Cloud Asset Inventory Resource Name Format](https://cloud.google.com/asset-inventory/docs/resource-name-format) for more information.  
`policy` |  `[Policy](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.iam.v1#google.iam.v1.Policy)` The IAM policy directly set on the given resource.  
`project` |  `string` The project that this IAM policy belongs to, in the format of projects/{PROJECT_NUMBER}. This field is available when the IAM policy belongs to a project.  
`folders[]` |  `string` The folder(s) that this IAM policy belongs to, in the format of folders/{FOLDER_NUMBER}. This field is available when the IAM policy belongs (directly or cascadingly) to one or more folders.  
`organization` |  `string` The organization that this IAM policy belongs to, in the format of organizations/{ORGANIZATION_NUMBER}. This field is available when the IAM policy belongs (directly or cascadingly) to an organization.  
`asset_type` |  `string` The asset type of the `[AnalyzeOrgPolicyGovernedAssetsResponse.GovernedIamPolicy.attached_resource](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.AnalyzeOrgPolicyGovernedAssetsResponse.GovernedIamPolicy.FIELDS.string.google.cloud.asset.v1.AnalyzeOrgPolicyGovernedAssetsResponse.GovernedIamPolicy.attached_resource)`. Example: `cloudresourcemanager.googleapis.com/Project` See [Cloud Asset Inventory Supported Asset Types](https://cloud.google.com/asset-inventory/docs/supported-asset-types) for all supported asset types.  
  
## GovernedResource

The Google Cloud resources governed by the organization policies of the `[AnalyzeOrgPolicyGovernedAssetsRequest.constraint](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.AnalyzeOrgPolicyGovernedAssetsRequest.FIELDS.string.google.cloud.asset.v1.AnalyzeOrgPolicyGovernedAssetsRequest.constraint)`.

Fields  
---  
`full_resource_name` |  `string` The [full resource name](https://cloud.google.com/asset-inventory/docs/resource-name-format) of the Google Cloud resource.  
`parent` |  `string` The [full resource name](https://cloud.google.com/asset-inventory/docs/resource-name-format) of the parent of `[AnalyzeOrgPolicyGovernedAssetsResponse.GovernedResource.full_resource_name](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.AnalyzeOrgPolicyGovernedAssetsResponse.GovernedResource.FIELDS.string.google.cloud.asset.v1.AnalyzeOrgPolicyGovernedAssetsResponse.GovernedResource.full_resource_name)`.  
`project` |  `string` The project that this resource belongs to, in the format of projects/{PROJECT_NUMBER}. This field is available when the resource belongs to a project.  
`folders[]` |  `string` The folder(s) that this resource belongs to, in the format of folders/{FOLDER_NUMBER}. This field is available when the resource belongs (directly or cascadingly) to one or more folders.  
`organization` |  `string` The organization that this resource belongs to, in the format of organizations/{ORGANIZATION_NUMBER}. This field is available when the resource belongs (directly or cascadingly) to an organization.  
`asset_type` |  `string` The asset type of the `[AnalyzeOrgPolicyGovernedAssetsResponse.GovernedResource.full_resource_name](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.AnalyzeOrgPolicyGovernedAssetsResponse.GovernedResource.FIELDS.string.google.cloud.asset.v1.AnalyzeOrgPolicyGovernedAssetsResponse.GovernedResource.full_resource_name)` Example: `cloudresourcemanager.googleapis.com/Project` See [Cloud Asset Inventory Supported Asset Types](https://cloud.google.com/asset-inventory/docs/supported-asset-types) for all supported asset types.  
`effective_tags[]` |  `[EffectiveTagDetails](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.EffectiveTagDetails)` The effective tags on this resource.  
  
## AnalyzeOrgPolicyGovernedContainersRequest

A request message for `[AssetService.AnalyzeOrgPolicyGovernedContainers](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.AssetService.AnalyzeOrgPolicyGovernedContainers)`.

Fields  
---  
`scope` |  `string` Required. The organization to scope the request. Only organization policies within the scope will be analyzed. The output containers will also be limited to the ones governed by those in-scope organization policies.

  * organizations/{ORGANIZATION_NUMBER} (e.g., "organizations/123456")

Authorization requires one or more of the following [IAM](https://cloud.google.com/iam/docs/) permissions on the specified resource `scope`:

  * `cloudasset.assets.searchAllResources`
  * `cloudasset.assets.analyzeOrgPolicy`

  
`constraint` |  `string` Required. The name of the constraint to analyze governed containers for. The analysis only contains organization policies for the provided constraint.  
`filter` |  `string` The expression to filter `[AnalyzeOrgPolicyGovernedContainersResponse.governed_containers](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.AnalyzeOrgPolicyGovernedContainersResponse.FIELDS.repeated.google.cloud.asset.v1.AnalyzeOrgPolicyGovernedContainersResponse.GovernedContainer.google.cloud.asset.v1.AnalyzeOrgPolicyGovernedContainersResponse.governed_containers)`. Filtering is currently available for bare literal values and the following fields: * parent * consolidated_policy.rules.enforceWhen filtering by a specific field, the only supported operator is `=`. For example, filtering by parent="//cloudresourcemanager.googleapis.com/folders/001" will return all the containers under "folders/001".  
`page_token` |  `string` The pagination token to retrieve the next page.  
`page_size` |  `int32` The maximum number of items to return per page. If unspecified, `[AnalyzeOrgPolicyGovernedContainersResponse.governed_containers](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.AnalyzeOrgPolicyGovernedContainersResponse.FIELDS.repeated.google.cloud.asset.v1.AnalyzeOrgPolicyGovernedContainersResponse.GovernedContainer.google.cloud.asset.v1.AnalyzeOrgPolicyGovernedContainersResponse.governed_containers)` will contain 100 items with a maximum of 200.  
  
## AnalyzeOrgPolicyGovernedContainersResponse

The response message for `[AssetService.AnalyzeOrgPolicyGovernedContainers](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.AssetService.AnalyzeOrgPolicyGovernedContainers)`.

Fields  
---  
`governed_containers[]` |  `[GovernedContainer](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.AnalyzeOrgPolicyGovernedContainersResponse.GovernedContainer)` The list of the analyzed governed containers.  
`constraint` |  `[AnalyzerOrgPolicyConstraint](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.AnalyzerOrgPolicyConstraint)` The definition of the constraint in the request.  
`next_page_token` |  `string` The page token to fetch the next page for `[AnalyzeOrgPolicyGovernedContainersResponse.governed_containers](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.AnalyzeOrgPolicyGovernedContainersResponse.FIELDS.repeated.google.cloud.asset.v1.AnalyzeOrgPolicyGovernedContainersResponse.GovernedContainer.google.cloud.asset.v1.AnalyzeOrgPolicyGovernedContainersResponse.governed_containers)`.  
  
## GovernedContainer

The organization/folder/project resource governed by organization policies of `[AnalyzeOrgPolicyGovernedContainersRequest.constraint](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.AnalyzeOrgPolicyGovernedContainersRequest.FIELDS.string.google.cloud.asset.v1.AnalyzeOrgPolicyGovernedContainersRequest.constraint)`.

Fields  
---  
`full_resource_name` |  `string` The [full resource name](https://cloud.google.com/asset-inventory/docs/resource-name-format) of an organization/folder/project resource.  
`parent` |  `string` The [full resource name](https://cloud.google.com/asset-inventory/docs/resource-name-format) of the parent of `[AnalyzeOrgPolicyGovernedContainersResponse.GovernedContainer.full_resource_name](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.AnalyzeOrgPolicyGovernedContainersResponse.GovernedContainer.FIELDS.string.google.cloud.asset.v1.AnalyzeOrgPolicyGovernedContainersResponse.GovernedContainer.full_resource_name)`.  
`consolidated_policy` |  `[AnalyzerOrgPolicy](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.AnalyzerOrgPolicy)` The consolidated organization policy for the analyzed resource. The consolidated organization policy is computed by merging and evaluating `[AnalyzeOrgPolicyGovernedContainersResponse.GovernedContainer.policy_bundle](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.AnalyzeOrgPolicyGovernedContainersResponse.GovernedContainer.FIELDS.repeated.google.cloud.asset.v1.AnalyzerOrgPolicy.google.cloud.asset.v1.AnalyzeOrgPolicyGovernedContainersResponse.GovernedContainer.policy_bundle)`. The evaluation will respect the organization policy [hierarchy rules](https://cloud.google.com/resource-manager/docs/organization-policy/understanding-hierarchy).  
`policy_bundle[]` |  `[AnalyzerOrgPolicy](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.AnalyzerOrgPolicy)` The ordered list of all organization policies from the `[consolidated_policy.attached_resource](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.AnalyzerOrgPolicy.FIELDS.string.google.cloud.asset.v1.AnalyzerOrgPolicy.attached_resource)`. to the scope specified in the request.If the constraint is defined with default policy, it will also appear in the list.  
`project` |  `string` The project that this resource belongs to, in the format of projects/{PROJECT_NUMBER}. This field is available when the resource belongs to a project.  
`folders[]` |  `string` The folder(s) that this resource belongs to, in the format of folders/{FOLDER_NUMBER}. This field is available when the resource belongs (directly or cascadingly) to one or more folders.  
`organization` |  `string` The organization that this resource belongs to, in the format of organizations/{ORGANIZATION_NUMBER}. This field is available when the resource belongs (directly or cascadingly) to an organization.  
`effective_tags[]` |  `[EffectiveTagDetails](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.EffectiveTagDetails)` The effective tags on this resource.  
  
## AnalyzerOrgPolicy

This organization policy message is a modified version of the one defined in the Organization Policy system. This message contains several fields defined in the original organization policy with some new fields for analysis purpose.

Fields  
---  
`attached_resource` |  `string` The [full resource name](https://cloud.google.com/asset-inventory/docs/resource-name-format) of an organization/folder/project resource where this organization policy is set.Notice that some type of constraints are defined with default policy. This field will be empty for them.  
`applied_resource` |  `string` The [full resource name](https://cloud.google.com/asset-inventory/docs/resource-name-format) of an organization/folder/project resource where this organization policy applies to.For any user defined org policies, this field has the same value as the [attached_resource] field. Only for default policy, this field has the different value.  
`rules[]` |  `[Rule](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.AnalyzerOrgPolicy.Rule)` List of rules for this organization policy.  
`inherit_from_parent` |  `bool` If `inherit_from_parent` is true, Rules set higher up in the hierarchy (up to the closest root) are inherited and present in the effective policy. If it is false, then no rules are inherited, and this policy becomes the effective root for evaluation.  
`reset` |  `bool` Ignores policies set above this resource and restores the default behavior of the constraint at this resource. This field can be set in policies for either list or boolean constraints. If set, `rules` must be empty and `inherit_from_parent` must be set to false.  
  
## Rule

This rule message is a customized version of the one defined in the Organization Policy system. In addition to the fields defined in the original organization policy, it contains additional field(s) under specific circumstances to support analysis results.

Fields  
---  
`condition` |  `[Expr](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.type#google.type.Expr)` The evaluating condition for this rule.  
`condition_evaluation` |  `[ConditionEvaluation](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.ConditionEvaluation)` The condition evaluation result for this rule. Only populated if it meets all the following criteria:

  * There is a `[condition](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.AnalyzerOrgPolicy.Rule.FIELDS.google.type.Expr.google.cloud.asset.v1.AnalyzerOrgPolicy.Rule.condition)` defined for this rule.
  * This rule is within `[AnalyzeOrgPolicyGovernedContainersResponse.GovernedContainer.consolidated_policy](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.AnalyzeOrgPolicyGovernedContainersResponse.GovernedContainer.FIELDS.google.cloud.asset.v1.AnalyzerOrgPolicy.google.cloud.asset.v1.AnalyzeOrgPolicyGovernedContainersResponse.GovernedContainer.consolidated_policy)`, or `[AnalyzeOrgPolicyGovernedAssetsResponse.GovernedAsset.consolidated_policy](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.AnalyzeOrgPolicyGovernedAssetsResponse.GovernedAsset.FIELDS.google.cloud.asset.v1.AnalyzerOrgPolicy.google.cloud.asset.v1.AnalyzeOrgPolicyGovernedAssetsResponse.GovernedAsset.consolidated_policy)` when the `[AnalyzeOrgPolicyGovernedAssetsResponse.GovernedAsset](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.AnalyzeOrgPolicyGovernedAssetsResponse.GovernedAsset)` has `[AnalyzeOrgPolicyGovernedAssetsResponse.GovernedAsset.governed_resource](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.AnalyzeOrgPolicyGovernedAssetsResponse.GovernedAsset.FIELDS.google.cloud.asset.v1.AnalyzeOrgPolicyGovernedAssetsResponse.GovernedResource.google.cloud.asset.v1.AnalyzeOrgPolicyGovernedAssetsResponse.GovernedAsset.governed_resource)`.

  
Union field `kind`.`kind` can be only one of the following:  
`values` |  `[StringValues](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.AnalyzerOrgPolicy.Rule.StringValues)` List of values to be used for this policy rule. This field can be set only in policies for list constraints.  
`allow_all` |  `bool` Setting this to true means that all values are allowed. This field can be set only in Policies for list constraints.  
`deny_all` |  `bool` Setting this to true means that all values are denied. This field can be set only in Policies for list constraints.  
`enforce` |  `bool` If `true`, then the `Policy` is enforced. If `false`, then any configuration is acceptable. This field can be set only in Policies for boolean constraints.  
  
## StringValues

The string values for the list constraints.

Fields  
---  
`allowed_values[]` |  `string` List of values allowed at this resource.  
`denied_values[]` |  `string` List of values denied at this resource.  
  
## AnalyzerOrgPolicyConstraint

The organization policy constraint definition.

Fields  
---  
Union field `constraint_definition`.`constraint_definition` can be only one of the following:  
`google_defined_constraint` |  `[Constraint](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.AnalyzerOrgPolicyConstraint.Constraint)` The definition of the canned constraint defined by Google.  
`custom_constraint` |  `[CustomConstraint](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.AnalyzerOrgPolicyConstraint.CustomConstraint)` The definition of the custom constraint.  
  
## Constraint

The definition of a constraint.

Fields  
---  
`name` |  `string` The unique name of the constraint. Format of the name should be * `constraints/{constraint_name}`For example, `constraints/compute.disableSerialPortAccess`.  
`display_name` |  `string` The human readable name of the constraint.  
`description` |  `string` Detailed description of what this `Constraint` controls as well as how and where it is enforced.  
`constraint_default` |  `[ConstraintDefault](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.AnalyzerOrgPolicyConstraint.Constraint.ConstraintDefault)` The evaluation behavior of this constraint in the absence of 'Policy'.  
Union field `constraint_type`. The type of restrictions for this `Constraint`.Immutable after creation. `constraint_type` can be only one of the following:  
`list_constraint` |  `[ListConstraint](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.AnalyzerOrgPolicyConstraint.Constraint.ListConstraint)` Defines this constraint as being a ListConstraint.  
`boolean_constraint` |  `[BooleanConstraint](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.AnalyzerOrgPolicyConstraint.Constraint.BooleanConstraint)` Defines this constraint as being a BooleanConstraint.  
  
## BooleanConstraint

This type has no fields.

A `Constraint` that is either enforced or not.

For example a constraint `constraints/compute.disableSerialPortAccess`. If it is enforced on a VM instance, serial port connections will not be opened to that instance.

## ConstraintDefault

Specifies the default behavior in the absence of any `Policy` for the `Constraint`. This must not be `CONSTRAINT_DEFAULT_UNSPECIFIED`.

Enums  
---  
`CONSTRAINT_DEFAULT_UNSPECIFIED` | This is only used for distinguishing unset values and should never be used.  
`ALLOW` | Indicates that all values are allowed for list constraints. Indicates that enforcement is off for boolean constraints.  
`DENY` | Indicates that all values are denied for list constraints. Indicates that enforcement is on for boolean constraints.  
  
## ListConstraint

A `Constraint` that allows or disallows a list of string values, which are configured by an organization's policy administrator with a `Policy`.

Fields  
---  
`supports_in` |  `bool` Indicates whether values grouped into categories can be used in `Policy.allowed_values` and `Policy.denied_values`. For example, `"in:Python"` would match any value in the 'Python' group.  
`supports_under` |  `bool` Indicates whether subtrees of Cloud Resource Manager resource hierarchy can be used in `Policy.allowed_values` and `Policy.denied_values`. For example, `"under:folders/123"` would match any resource under the 'folders/123' folder.  
  
## CustomConstraint

The definition of a custom constraint.

Fields  
---  
`name` |  `string` Name of the constraint. This is unique within the organization. Format of the name should be * `organizations/{organization_id}/customConstraints/{custom_constraint_id}`Example : "organizations/123/customConstraints/custom.createOnlyE2TypeVms"  
`resource_types[]` |  `string` The Resource Instance type on which this policy applies to. Format will be of the form : "/" Example: * `compute.googleapis.com/Instance`.  
`method_types[]` |  `[MethodType](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.AnalyzerOrgPolicyConstraint.CustomConstraint.MethodType)` All the operations being applied for this constraint.  
`condition` |  `string` Organization Policy condition/expression. For example: `resource.instanceName.matches("(production|test)_(.+_)?[\d]+")'` or, `resource.management.auto_upgrade == true`  
`action_type` |  `[ActionType](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.AnalyzerOrgPolicyConstraint.CustomConstraint.ActionType)` Allow or deny type.  
`display_name` |  `string` One line display name for the UI.  
`description` |  `string` Detailed information about this custom policy constraint.  
  
## ActionType

Allow or deny type.

Enums  
---  
`ACTION_TYPE_UNSPECIFIED` | Unspecified. Will results in user error.  
`ALLOW` | Allowed action type.  
`DENY` | Deny action type.  
  
## MethodType

The operation in which this constraint will be applied. For example: If the constraint applies only when create VMs, the method_types will be "CREATE" only. If the constraint applied when create or delete VMs, the method_types will be "CREATE" and "DELETE".

Enums  
---  
`METHOD_TYPE_UNSPECIFIED` | Unspecified. Will results in user error.  
`CREATE` | Constraint applied when creating the resource.  
`UPDATE` | Constraint applied when updating the resource.  
`DELETE` | Constraint applied when deleting the resource.  
`REMOVE_GRANT` | Constraint applied when removing an IAM grant.  
`GOVERN_TAGS` | Constraint applied when enforcing forced tagging.  
  
## Asset

An asset in Google Cloud. An asset can be any resource in the Google Cloud [resource hierarchy](https://cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy), a resource outside the Google Cloud resource hierarchy (such as Google Kubernetes Engine clusters and objects), or a policy (e.g. IAM policy), or a relationship (e.g. an INSTANCE_TO_INSTANCEGROUP relationship). See [Supported asset types](https://cloud.google.com/asset-inventory/docs/supported-asset-types) for more information.

Fields  
---  
`update_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` The last update timestamp of an asset. update_time is updated when create/update/delete operation is performed.  
`name` |  `string` The full name of the asset. Example: `//compute.googleapis.com/projects/my_project_123/zones/zone1/instances/instance1`See [Resource names](https://cloud.google.com/apis/design/resource_names#full_resource_name) for more information.  
`asset_type` |  `string` The type of the asset. Example: `compute.googleapis.com/Disk`See [Supported asset types](https://cloud.google.com/asset-inventory/docs/supported-asset-types) for more information.  
`resource` |  `[Resource](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.Resource)` A representation of the resource.  
`iam_policy` |  `[Policy](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.iam.v1#google.iam.v1.Policy)` A representation of the IAM policy set on a Google Cloud resource. There can be a maximum of one IAM policy set on any given resource. In addition, IAM policies inherit their granted access scope from any policies set on parent resources in the resource hierarchy. Therefore, the effectively policy is the union of both the policy set on this resource and each policy set on all of the resource's ancestry resource levels in the hierarchy. See [this topic](https://cloud.google.com/iam/help/allow-policies/inheritance) for more information.  
`org_policy[]` |  `[Policy](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.orgpolicy.v1#google.cloud.orgpolicy.v1.Policy)` A representation of an [organization policy](https://cloud.google.com/resource-manager/docs/organization-policy/overview#organization_policy). There can be more than one organization policy with different constraints set on a given resource.  
`os_inventory` |  `[Inventory](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.osconfig.v1#google.cloud.osconfig.v1.Inventory)` A representation of runtime OS Inventory information. See [this topic](https://cloud.google.com/compute/docs/instances/os-inventory-management) for more information.  
`related_assets  
**(deprecated)**` |  `[RelatedAssets](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.RelatedAssets)` This item is deprecated!DEPRECATED. This field only presents for the purpose of backward-compatibility. The server will never generate responses with this field. The related assets of the asset of one relationship type. One asset only represents one type of relationship.  
`related_asset` |  `[RelatedAsset](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.RelatedAsset)` One related asset of the current asset.  
`ancestors[]` |  `string` The ancestry path of an asset in Google Cloud [resource hierarchy](https://cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy), represented as a list of relative resource names. An ancestry path starts with the closest ancestor in the hierarchy and ends at root. If the asset is a project, folder, or organization, the ancestry path starts from the asset itself.Example: `["projects/123456789", "folders/5432", "organizations/1234"]`  
`asset_exceptions[]` |  `[AssetException](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.AssetException)` The exceptions of a resource.  
Union field `access_context_policy`. A representation of an [access policy](https://cloud.google.com/access-context-manager/docs/overview#access-policies). `access_context_policy` can be only one of the following:  
`access_policy` |  `[AccessPolicy](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.identity.accesscontextmanager.v1#google.identity.accesscontextmanager.v1.AccessPolicy)` Also refer to the [access policy user guide](https://cloud.google.com/access-context-manager/docs/overview#access-policies).  
`access_level` |  `[AccessLevel](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.identity.accesscontextmanager.v1#google.identity.accesscontextmanager.v1.AccessLevel)` Also refer to the [access level user guide](https://cloud.google.com/access-context-manager/docs/overview#access-levels).  
`service_perimeter` |  `[ServicePerimeter](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.identity.accesscontextmanager.v1#google.identity.accesscontextmanager.v1.ServicePerimeter)` Also refer to the [service perimeter user guide](https://cloud.google.com/vpc-service-controls/docs/overview).  
  
## AssetEnrichment

The enhanced metadata information for a resource.

Fields  
---  
Union field `EnrichmentData`.`EnrichmentData` can be only one of the following:  
`resource_owners` |  `[ResourceOwners](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.ResourceOwners)` The resource owners for a resource.Note that this field only contains the members that have "roles/owner" role in the resource's IAM Policy.  
  
## AssetException

An exception of an asset.

Fields  
---  
`exception_type` |  `[ExceptionType](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.AssetException.ExceptionType)` The type of exception.  
`details` |  `string` The details of the exception.  
  
## ExceptionType

The type of exception.

Enums  
---  
`EXCEPTION_TYPE_UNSPECIFIED` | exception_type is not applicable for the current asset.  
`TRUNCATION` | The asset content is truncated.  
  
## AttachedResource

Attached resource representation, which is defined by the corresponding service provider. It represents an attached resource's payload.

Fields  
---  
`asset_type` |  `string` The type of this attached resource.Example: `osconfig.googleapis.com/Inventory`You can find the supported attached asset types of each resource in this table: `https://cloud.google.com/asset-inventory/docs/supported-asset-types`  
`versioned_resources[]` |  `[VersionedResource](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.VersionedResource)` Versioned resource representations of this attached resource. This is repeated because there could be multiple versions of the attached resource representations during version migration.  
  
## BatchGetAssetsHistoryRequest

Batch get assets history request.

Fields  
---  
`parent` |  `string` Required. The relative name of the root asset. It can only be an organization number (such as "organizations/123"), a project ID (such as "projects/my-project-id")", or a project number (such as "projects/12345"). Authorization requires one or more of the following [IAM](https://cloud.google.com/iam/docs/) permissions on the specified resource `parent`:

  * `cloudasset.assets.exportResource`
  * `cloudasset.assets.exportIamPolicy`

  
`asset_names[]` |  `string` A list of the full names of the assets. See: <https://cloud.google.com/asset-inventory/docs/resource-name-format> Example:`//compute.googleapis.com/projects/my_project_123/zones/zone1/instances/instance1`.The request becomes a no-op if the asset name list is empty, and the max size of the asset name list is 100 in one request.  
`content_type` |  `[ContentType](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.ContentType)` Optional. The content type.  
`read_time_window` |  `[TimeWindow](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.TimeWindow)` Optional. The time window for the asset history. Both start_time and end_time are optional and if set, it must be after the current time minus 35 days. If end_time is not set, it is default to current timestamp. If start_time is not set, the snapshot of the assets at end_time will be returned. The returned results contain all temporal assets whose time window overlap with read_time_window.  
`relationship_types[]` |  `string` Optional. A list of relationship types to output, for example: `INSTANCE_TO_INSTANCEGROUP`. This field should only be specified if content_type=RELATIONSHIP. * If specified: it outputs specified relationships' history on the [asset_names]. It returns an error if any of the [relationship_types] doesn't belong to the supported relationship types of the [asset_names] or if any of the [asset_names]'s types doesn't belong to the source types of the [relationship_types]. * Otherwise: it outputs the supported relationships' history on the [asset_names] or returns an error if any of the [asset_names]'s types has no relationship support. See [Introduction to Cloud Asset Inventory](https://cloud.google.com/asset-inventory/docs/overview) for all supported asset types and relationship types.  
  
## BatchGetAssetsHistoryResponse

Batch get assets history response.

Fields  
---  
`assets[]` |  `[TemporalAsset](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.TemporalAsset)` A list of assets with valid time windows.  
  
## BatchGetEffectiveIamPoliciesRequest

A request message for `[AssetService.BatchGetEffectiveIamPolicies](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.AssetService.BatchGetEffectiveIamPolicies)`.

Fields  
---  
`scope` |  `string` Required. Only IAM policies on or below the scope will be returned.This can only be an organization number (such as "organizations/123"), a folder number (such as "folders/123"), a project ID (such as "projects/my-project-id"), or a project number (such as "projects/12345").To know how to get organization ID, visit [here ](https://cloud.google.com/resource-manager/docs/creating-managing-organization#retrieving_your_organization_id).To know how to get folder or project ID, visit [here ](https://cloud.google.com/resource-manager/docs/creating-managing-folders#viewing_or_listing_folders_and_projects). Authorization requires one or more of the following [IAM](https://cloud.google.com/iam/docs/) permissions on the specified resource `scope`:

  * `cloudasset.assets.analyzeIamPolicy`
  * `cloudasset.assets.searchAllResources`
  * `cloudasset.assets.searchAllIamPolicies`

  
`names[]` |  `string` Required. The names refer to the [full_resource_names](https://cloud.google.com/asset-inventory/docs/resource-name-format) of the asset types [supported by search APIs](https://cloud.google.com/asset-inventory/docs/supported-asset-types). A maximum of 20 resources' effective policies can be retrieved in a batch.  
  
## BatchGetEffectiveIamPoliciesResponse

A response message for `[AssetService.BatchGetEffectiveIamPolicies](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.AssetService.BatchGetEffectiveIamPolicies)`.

Fields  
---  
`policy_results[]` |  `[EffectiveIamPolicy](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.BatchGetEffectiveIamPoliciesResponse.EffectiveIamPolicy)` The effective policies for a batch of resources. Note that the results order is the same as the order of `[BatchGetEffectiveIamPoliciesRequest.names](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.BatchGetEffectiveIamPoliciesRequest.FIELDS.repeated.string.google.cloud.asset.v1.BatchGetEffectiveIamPoliciesRequest.names)`. When a resource does not have any effective IAM policies, its corresponding policy_result will contain empty `[EffectiveIamPolicy.policies](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.BatchGetEffectiveIamPoliciesResponse.EffectiveIamPolicy.FIELDS.repeated.google.cloud.asset.v1.BatchGetEffectiveIamPoliciesResponse.EffectiveIamPolicy.PolicyInfo.google.cloud.asset.v1.BatchGetEffectiveIamPoliciesResponse.EffectiveIamPolicy.policies)`.  
  
## EffectiveIamPolicy

The effective IAM policies on one resource.

Fields  
---  
`full_resource_name` |  `string` The [full_resource_name](https://cloud.google.com/asset-inventory/docs/resource-name-format) for which the `[policies](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.BatchGetEffectiveIamPoliciesResponse.EffectiveIamPolicy.FIELDS.repeated.google.cloud.asset.v1.BatchGetEffectiveIamPoliciesResponse.EffectiveIamPolicy.PolicyInfo.google.cloud.asset.v1.BatchGetEffectiveIamPoliciesResponse.EffectiveIamPolicy.policies)` are computed. This is one of the `[BatchGetEffectiveIamPoliciesRequest.names](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.BatchGetEffectiveIamPoliciesRequest.FIELDS.repeated.string.google.cloud.asset.v1.BatchGetEffectiveIamPoliciesRequest.names)` the caller provides in the request.  
`policies[]` |  `[PolicyInfo](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.BatchGetEffectiveIamPoliciesResponse.EffectiveIamPolicy.PolicyInfo)` The effective policies for the `[full_resource_name](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.BatchGetEffectiveIamPoliciesResponse.EffectiveIamPolicy.FIELDS.string.google.cloud.asset.v1.BatchGetEffectiveIamPoliciesResponse.EffectiveIamPolicy.full_resource_name)`.These policies include the policy set on the `[full_resource_name](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.BatchGetEffectiveIamPoliciesResponse.EffectiveIamPolicy.FIELDS.string.google.cloud.asset.v1.BatchGetEffectiveIamPoliciesResponse.EffectiveIamPolicy.full_resource_name)` and those set on its parents and ancestors up to the `[BatchGetEffectiveIamPoliciesRequest.scope](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.BatchGetEffectiveIamPoliciesRequest.FIELDS.string.google.cloud.asset.v1.BatchGetEffectiveIamPoliciesRequest.scope)`. Note that these policies are not filtered according to the resource type of the `[full_resource_name](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.BatchGetEffectiveIamPoliciesResponse.EffectiveIamPolicy.FIELDS.string.google.cloud.asset.v1.BatchGetEffectiveIamPoliciesResponse.EffectiveIamPolicy.full_resource_name)`.These policies are hierarchically ordered by `[PolicyInfo.attached_resource](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.BatchGetEffectiveIamPoliciesResponse.EffectiveIamPolicy.PolicyInfo.FIELDS.string.google.cloud.asset.v1.BatchGetEffectiveIamPoliciesResponse.EffectiveIamPolicy.PolicyInfo.attached_resource)` starting from `[full_resource_name](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.BatchGetEffectiveIamPoliciesResponse.EffectiveIamPolicy.FIELDS.string.google.cloud.asset.v1.BatchGetEffectiveIamPoliciesResponse.EffectiveIamPolicy.full_resource_name)` itself to its parents and ancestors, such that policies[i]'s `[PolicyInfo.attached_resource](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.BatchGetEffectiveIamPoliciesResponse.EffectiveIamPolicy.PolicyInfo.FIELDS.string.google.cloud.asset.v1.BatchGetEffectiveIamPoliciesResponse.EffectiveIamPolicy.PolicyInfo.attached_resource)` is the child of policies[i+1]'s `[PolicyInfo.attached_resource](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.BatchGetEffectiveIamPoliciesResponse.EffectiveIamPolicy.PolicyInfo.FIELDS.string.google.cloud.asset.v1.BatchGetEffectiveIamPoliciesResponse.EffectiveIamPolicy.PolicyInfo.attached_resource)`, if policies[i+1] exists.  
  
## PolicyInfo

The IAM policy and its attached resource.

Fields  
---  
`attached_resource` |  `string` The full resource name the `[policy](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.BatchGetEffectiveIamPoliciesResponse.EffectiveIamPolicy.PolicyInfo.FIELDS.google.iam.v1.Policy.google.cloud.asset.v1.BatchGetEffectiveIamPoliciesResponse.EffectiveIamPolicy.PolicyInfo.policy)` is directly attached to.  
`policy` |  `[Policy](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.iam.v1#google.iam.v1.Policy)` The IAM policy that's directly attached to the `[attached_resource](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.BatchGetEffectiveIamPoliciesResponse.EffectiveIamPolicy.PolicyInfo.FIELDS.string.google.cloud.asset.v1.BatchGetEffectiveIamPoliciesResponse.EffectiveIamPolicy.PolicyInfo.attached_resource)`.  
  
## BigQueryDestination

A BigQuery destination for exporting assets to.

Fields  
---  
`dataset` |  `string` Required. The BigQuery dataset in format "projects/projectId/datasets/datasetId", to which the snapshot result should be exported. If this dataset does not exist, the export call returns an INVALID_ARGUMENT error. Setting the `contentType` for `exportAssets` determines the [schema](https://docs.cloud.google.com/asset-inventory/docs/exporting-to-bigquery#bigquery-schema) of the BigQuery table. Setting `separateTablesPerAssetType` to `TRUE` also influences the schema.  
`table` |  `string` Required. The BigQuery table to which the snapshot result should be written. If this table does not exist, a new table with the given name will be created.  
`force` |  `bool` If the destination table already exists and this flag is `TRUE`, the table will be overwritten by the contents of assets snapshot. If the flag is `FALSE` or unset and the destination table already exists, the export call returns an INVALID_ARGUMENT error.  
`partition_spec` |  `[PartitionSpec](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.PartitionSpec)` [partition_spec] determines whether to export to partitioned table(s) and how to partition the data.If [partition_spec] is unset or [partition_spec.partition_key] is unset or `PARTITION_KEY_UNSPECIFIED`, the snapshot results will be exported to non-partitioned table(s). [force] will decide whether to overwrite existing table(s).If [partition_spec] is specified. First, the snapshot results will be written to partitioned table(s) with two additional timestamp columns, readTime and requestTime, one of which will be the partition key. Secondly, in the case when any destination table already exists, it will first try to update existing table's schema as necessary by appending additional columns. Then, if [force] is `TRUE`, the corresponding partition will be overwritten by the snapshot results (data in different partitions will remain intact); if [force] is unset or `FALSE`, it will append the data. An error will be returned if the schema update or data appension fails.  
`separate_tables_per_asset_type` |  `bool` If this flag is `TRUE`, the snapshot results will be written to one or multiple tables, each of which contains results of one asset type. The [force] and [partition_spec] fields will apply to each of them.Field [table] will be concatenated with "_" and the asset type names (see <https://cloud.google.com/asset-inventory/docs/supported-asset-types> for supported asset types) to construct per-asset-type table names, in which all non-alphanumeric characters like "." and "/" will be substituted by "_". Example: if field [table] is "mytable" and snapshot results contain "storage.googleapis.com/Bucket" assets, the corresponding table name will be "mytable_storage_googleapis_com_Bucket". If any of these tables does not exist, a new table with the concatenated name will be created.When [content_type] in the ExportAssetsRequest is `RESOURCE`, the schema of each table will include RECORD-type columns mapped to the nested fields in the Asset.resource.data field of that asset type (up to the 15 nested level BigQuery supports (<https://cloud.google.com/bigquery/docs/nested-repeated#limitations))>. The fields in >15 nested levels will be stored in JSON format string as a child column of its parent RECORD column.If error occurs when exporting to any table, the whole export call will return an error but the export results that already succeed will persist. Example: if exporting to table_type_A succeeds when exporting to table_type_B fails during one export call, the results in table_type_A will persist and there will not be partial results persisting in a table.  
  
## ConditionEvaluation

The condition evaluation.

Fields  
---  
`evaluation_value` |  `[EvaluationValue](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.ConditionEvaluation.EvaluationValue)` The evaluation result.  
  
## EvaluationValue

Value of this expression.

Enums  
---  
`EVALUATION_VALUE_UNSPECIFIED` | Reserved for future use.  
`TRUE` | The evaluation result is `true`.  
`FALSE` | The evaluation result is `false`.  
`CONDITIONAL` | The evaluation result is `conditional` when the condition expression contains variables that are either missing input values or have not been supported by Policy Analyzer yet.  
  
## ContentType

Asset content type.

Enums  
---  
`CONTENT_TYPE_UNSPECIFIED` | Unspecified content type.  
`RESOURCE` | Resource metadata.  
`IAM_POLICY` | The actual IAM policy set on a resource.  
`ORG_POLICY` | The organization policy set on an asset.  
`ACCESS_POLICY` | The Access Context Manager policy set on an asset.  
`OS_INVENTORY` | The runtime OS Inventory information.  
`RELATIONSHIP` | The related resources.  
  
## CreateFeedRequest

Create asset feed request.

Fields  
---  
`parent` |  `string` Required. The name of the project/folder/organization where this feed should be created in. It can only be an organization number (such as "organizations/123"), a folder number (such as "folders/123"), a project ID (such as "projects/my-project-id"), or a project number (such as "projects/12345").  
`feed_id` |  `string` Required. This is the client-assigned asset feed identifier and it needs to be unique under a specific parent project/folder/organization.  
`feed` |  `[Feed](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.Feed)` Required. The feed details. The field `name` must be empty and it will be generated in the format of: projects/project_number/feeds/feed_id folders/folder_number/feeds/feed_id organizations/organization_number/feeds/feed_id  
  
## CreateSavedQueryRequest

Request to create a saved query.

Fields  
---  
`parent` |  `string` Required. The name of the project/folder/organization where this saved_query should be created in. It can only be an organization number (such as "organizations/123"), a folder number (such as "folders/123"), a project ID (such as "projects/my-project-id"), or a project number (such as "projects/12345").  
`saved_query` |  `[SavedQuery](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.SavedQuery)` Required. The saved_query details. The `name` field must be empty as it will be generated based on the parent and saved_query_id.  
`saved_query_id` |  `string` Required. The ID to use for the saved query, which must be unique in the specified parent. It will become the final component of the saved query's resource name.This value should be 4-63 characters, and valid characters are `[a-z][0-9]-`.Notice that this field is required in the saved query creation, and the `name` field of the `saved_query` will be ignored.  
  
## DeleteFeedRequest

Fields  
---  
`name` |  `string` Required. The name of the feed and it must be in the format of: projects/project_number/feeds/feed_id folders/folder_number/feeds/feed_id organizations/organization_number/feeds/feed_id  
  
## DeleteSavedQueryRequest

Request to delete a saved query.

Fields  
---  
`name` |  `string` Required. The name of the saved query to delete. It must be in the format of:

  * projects/project_number/savedQueries/saved_query_id
  * folders/folder_number/savedQueries/saved_query_id
  * organizations/organization_number/savedQueries/saved_query_id

  
  
## EffectiveTagDetails

The effective tags and the ancestor resources from which they were inherited.

Fields  
---  
`effective_tags[]` |  `[Tag](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.Tag)` The effective tags inherited from the `[attached_resource](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.EffectiveTagDetails.FIELDS.string.google.cloud.asset.v1.EffectiveTagDetails.attached_resource)`. Note that tags with the same key but different values may attach to resources at a different hierarchy levels. The lower hierarchy tag value will overwrite the higher hierarchy tag value of the same tag key. In this case, the tag value at the higher hierarchy level will be removed. For more information, see [tag inheritance](https://cloud.google.com/resource-manager/docs/tags/tags-overview#inheritance).  
`attached_resource` |  `string` The [full resource name](https://cloud.google.com/asset-inventory/docs/resource-name-format) of the ancestor from which `[effective_tags](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.EffectiveTagDetails.FIELDS.repeated.google.cloud.asset.v1.Tag.google.cloud.asset.v1.EffectiveTagDetails.effective_tags)` are inherited, according to [tag inheritance](https://cloud.google.com/resource-manager/docs/tags/tags-overview#inheritance).  
  
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
`content_type` |  `[ContentType](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.ContentType)` Asset content type. If not specified, no content but the asset name will be returned.  
`output_config` |  `[OutputConfig](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.OutputConfig)` Required. Output configuration indicating where the results will be output to.  
`relationship_types[]` |  `string` A list of relationship types to export, for example: `INSTANCE_TO_INSTANCEGROUP`. This field should only be specified if content_type=RELATIONSHIP. * If specified: it snapshots specified relationships. It returns an error if any of the [relationship_types] doesn't belong to the supported relationship types of the [asset_types] or if any of the [asset_types] doesn't belong to the source types of the [relationship_types]. * Otherwise: it snapshots the supported relationships for all [asset_types] or returns an error if any of the [asset_types] has no relationship support. An unspecified asset types field means all supported asset_types. See [Introduction to Cloud Asset Inventory](https://cloud.google.com/asset-inventory/docs/overview) for all supported asset types and relationship types.  
  
## ExportAssetsResponse

The export asset response. This message is returned by the `[google.longrunning.Operations.GetOperation](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.longrunning#google.longrunning.Operations.GetOperation)` method in the returned `[google.longrunning.Operation.response](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.longrunning#google.longrunning.Operation.FIELDS.google.protobuf.Any.google.longrunning.Operation.response)` field.

Fields  
---  
`read_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Time the snapshot was taken.  
`output_config` |  `[OutputConfig](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.OutputConfig)` Output configuration indicating where the results were output to.  
`output_result` |  `[OutputResult](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.OutputResult)` Output result indicating where the assets were exported to. For example, a set of actual Cloud Storage object URIs where the assets are exported to. The URIs can be different from what [output_config] has specified, as the service will split the output object into multiple ones once it exceeds a single Cloud Storage object limit.  
  
## Feed

An asset feed used to export asset updates to a destinations. An asset feed filter controls what updates are exported. The asset feed must be created within a project, organization, or folder. Supported destinations are: Pub/Sub topics.

Fields  
---  
`name` |  `string` Required. The format will be projects/{project_number}/feeds/{client-assigned_feed_identifier} or folders/{folder_number}/feeds/{client-assigned_feed_identifier} or organizations/{organization_number}/feeds/{client-assigned_feed_identifier}The client-assigned feed identifier must be unique within the parent project/folder/organization.  
`asset_names[]` |  `string` A list of the full names of the assets to receive updates. You must specify either or both of asset_names and asset_types. Only asset updates matching specified asset_names or asset_types are exported to the feed. Example: `//compute.googleapis.com/projects/my_project_123/zones/zone1/instances/instance1`. For a list of the full names for supported asset types, see [Resource name format](https://docs.cloud.google.com/asset-inventory/docs/resource-name-format).  
`asset_types[]` |  `string` A list of types of the assets to receive updates. You must specify either or both of asset_names and asset_types. Only asset updates matching specified asset_names or asset_types are exported to the feed. Example: `"compute.googleapis.com/Disk"`For a list of all supported asset types, see [Supported asset types](https://docs.cloud.google.com/asset-inventory/docs/supported-asset-types).  
`content_type` |  `[ContentType](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.ContentType)` Asset content type. If not specified, no content but the asset name and type will be returned.  
`feed_output_config` |  `[FeedOutputConfig](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.FeedOutputConfig)` Required. Feed output configuration defining where the asset updates are published to.  
`condition` |  `[Expr](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.type#google.type.Expr)` A condition which determines whether an asset update should be published. If specified, an asset will be returned only when the expression evaluates to true. When set, `expression` field in the `Expr` must be a valid [CEL expression](https://github.com/google/cel-spec) on a TemporalAsset with name `temporal_asset`. Example: a Feed with expression ("temporal_asset.deleted == true") will only publish Asset deletions. Other fields of `Expr` are optional.See our [user guide](https://cloud.google.com/asset-inventory/docs/monitoring-asset-changes-with-condition) for detailed instructions.  
`relationship_types[]` |  `string` A list of relationship types to output, for example: `INSTANCE_TO_INSTANCEGROUP`. This field should only be specified if content_type=RELATIONSHIP. * If specified: it outputs specified relationship updates on the [asset_names] or the [asset_types]. It returns an error if any of the [relationship_types] doesn't belong to the supported relationship types of the [asset_names] or [asset_types], or any of the [asset_names] or the [asset_types] doesn't belong to the source types of the [relationship_types]. * Otherwise: it outputs the supported relationships of the types of [asset_names] and [asset_types] or returns an error if any of the [asset_names] or the [asset_types] has no replationship support. See [Introduction to Cloud Asset Inventory](https://cloud.google.com/asset-inventory/docs/overview) for all supported asset types and relationship types.  
  
## FeedOutputConfig

Output configuration for asset feed destination.

Fields  
---  
Union field `destination`. Asset feed destination. `destination` can be only one of the following:  
`pubsub_destination` |  `[PubsubDestination](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.PubsubDestination)` Destination on Pub/Sub.  
  
## GcsDestination

A Cloud Storage location.

Fields  
---  
Union field `object_uri`. Required. `object_uri` can be only one of the following:  
`uri` |  `string` The URI of the Cloud Storage object. It's the same URI that is used by gcloud storage. Example: "gs://bucket_name/object_name". See [Viewing and Editing Object Metadata](https://cloud.google.com/storage/docs/viewing-editing-metadata) for more information.If the specified Cloud Storage object already exists and there is no [hold](https://cloud.google.com/storage/docs/object-holds), it will be overwritten with the exported result.  
`uri_prefix` |  `string` The URI prefix of all generated Cloud Storage objects. Example: "gs://bucket_name/object_name_prefix". Each object URI is in format: "gs://bucket_name/object_name_prefix// and only contains assets for that type.  starts from 0. Example: "gs://bucket_name/object_name_prefix/compute.googleapis.com/Disk/0" is the first shard of output objects containing all compute.googleapis.com/Disk assets. An INVALID_ARGUMENT error will be returned if file with the same name "gs://bucket_name/object_name_prefix" already exists.  
  
## GcsOutputResult

A Cloud Storage output result.

Fields  
---  
`uris[]` |  `string` List of URIs of the Cloud Storage objects. Example: "gs://bucket_name/object_name".  
  
## GetFeedRequest

Get asset feed request.

Fields  
---  
`name` |  `string` Required. The name of the Feed and it must be in the format of: projects/project_number/feeds/feed_id folders/folder_number/feeds/feed_id organizations/organization_number/feeds/feed_id  
  
## GetSavedQueryRequest

Request to get a saved query.

Fields  
---  
`name` |  `string` Required. The name of the saved query and it must be in the format of:

  * projects/project_number/savedQueries/saved_query_id
  * folders/folder_number/savedQueries/saved_query_id
  * organizations/organization_number/savedQueries/saved_query_id

  
  
## IamPolicyAnalysisOutputConfig

Output configuration for export IAM policy analysis destination.

Fields  
---  
Union field `destination`. IAM policy analysis export destination. `destination` can be only one of the following:  
`gcs_destination` |  `[GcsDestination](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.IamPolicyAnalysisOutputConfig.GcsDestination)` Destination on Cloud Storage.  
`bigquery_destination` |  `[BigQueryDestination](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.IamPolicyAnalysisOutputConfig.BigQueryDestination)` Destination on BigQuery.  
  
## BigQueryDestination

A BigQuery destination.

Fields  
---  
`dataset` |  `string` Required. The BigQuery dataset in format "projects/projectId/datasets/datasetId", to which the analysis results should be exported. If this dataset does not exist, the export call will return an INVALID_ARGUMENT error.  
`table_prefix` |  `string` Required. The prefix of the BigQuery tables to which the analysis results will be written. Tables will be created based on this table_prefix if not exist: * _analysis table will contain export operation's metadata. * _analysis_result will contain all the `[IamPolicyAnalysisResult](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.IamPolicyAnalysisResult)`. When [partition_key] is specified, both tables will be partitioned based on the [partition_key].  
`partition_key` |  `[PartitionKey](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.IamPolicyAnalysisOutputConfig.BigQueryDestination.PartitionKey)` The partition key for BigQuery partitioned table.  
`write_disposition` |  `string` Optional. Specifies the action that occurs if the destination table or partition already exists. The following values are supported:

  * WRITE_TRUNCATE: If the table or partition already exists, BigQuery overwrites the entire table or all the partitions data.
  * WRITE_APPEND: If the table or partition already exists, BigQuery appends the data to the table or the latest partition.
  * WRITE_EMPTY: If the table already exists and contains data, an error is returned.

The default value is WRITE_APPEND. Each action is atomic and only occurs if BigQuery is able to complete the job successfully. Details are at <https://cloud.google.com/bigquery/docs/loading-data-local#appending_to_or_overwriting_a_table_using_a_local_file>.  
  
## PartitionKey

This enum determines the partition key column for the bigquery tables. Partitioning can improve query performance and reduce query cost by filtering partitions. Refer to <https://cloud.google.com/bigquery/docs/partitioned-tables> for details.

Enums  
---  
`PARTITION_KEY_UNSPECIFIED` | Unspecified partition key. Tables won't be partitioned using this option.  
`REQUEST_TIME` | The time when the request is received. If specified as partition key, the result table(s) is partitioned by the RequestTime column, an additional timestamp column representing when the request was received.  
  
## GcsDestination

A Cloud Storage location.

Fields  
---  
`uri` |  `string` Required. The URI of the Cloud Storage object. It's the same URI that is used by gcloud storage. Example: "gs://bucket_name/object_name". See [Viewing and Editing Object Metadata](https://cloud.google.com/storage/docs/viewing-editing-metadata) for more information.If the specified Cloud Storage object already exists and there is no [hold](https://cloud.google.com/storage/docs/object-holds), it will be overwritten with the analysis result.  
  
## IamPolicyAnalysisQuery

IAM policy analysis query message.

Fields  
---  
`scope` |  `string` Required. The relative name of the root asset. Only resources and IAM policies within the scope will be analyzed.This can only be an organization number (such as "organizations/123"), a folder number (such as "folders/123"), a project ID (such as "projects/my-project-id"), or a project number (such as "projects/12345").To know how to get organization ID, visit [here ](https://cloud.google.com/resource-manager/docs/creating-managing-organization#retrieving_your_organization_id).To know how to get folder or project ID, visit [here ](https://cloud.google.com/resource-manager/docs/creating-managing-folders#viewing_or_listing_folders_and_projects). Authorization requires one or more of the following [IAM](https://cloud.google.com/iam/docs/) permissions on the specified resource `scope`:

  * `cloudasset.assets.analyzeIamPolicy`
  * `cloudasset.assets.searchAllResources`
  * `cloudasset.assets.searchAllIamPolicies`

  
`resource_selector` |  `[ResourceSelector](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.IamPolicyAnalysisQuery.ResourceSelector)` Optional. Specifies a resource for analysis.  
`identity_selector` |  `[IdentitySelector](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.IamPolicyAnalysisQuery.IdentitySelector)` Optional. Specifies an identity for analysis.  
`access_selector` |  `[AccessSelector](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.IamPolicyAnalysisQuery.AccessSelector)` Optional. Specifies roles or permissions for analysis. This is optional.  
`options` |  `[Options](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.IamPolicyAnalysisQuery.Options)` Optional. The query options.  
`condition_context` |  `[ConditionContext](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.IamPolicyAnalysisQuery.ConditionContext)` Optional. The hypothetical context for IAM conditions evaluation.  
  
## AccessSelector

Specifies roles and/or permissions to analyze, to determine both the identities possessing them and the resources they control. If multiple values are specified, results will include roles or permissions matching any of them. The total number of roles and permissions should be equal or less than 10.

Fields  
---  
`roles[]` |  `string` Optional. The roles to appear in result.  
`permissions[]` |  `string` Optional. The permissions to appear in result.  
  
## ConditionContext

The IAM conditions context.

Fields  
---  
Union field `TimeContext`. The IAM conditions time context. `TimeContext` can be only one of the following:  
`access_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` The hypothetical access timestamp to evaluate IAM conditions. Note that this value must not be earlier than the current time; otherwise, an INVALID_ARGUMENT error will be returned.  
  
## IdentitySelector

Specifies an identity for which to determine resource access, based on roles assigned either directly to them or to the groups they belong to, directly or indirectly.

Fields  
---  
`identity` |  `string` Required. The identity appear in the form of principals in [IAM policy binding](https://cloud.google.com/iam/reference/rest/v1/Binding).The examples of supported forms are: "user:[mike@example.com"](mailto:mike@example.com"), "group:[admins@example.com"](mailto:admins@example.com"), "domain:google.com", "serviceAccount:[my-project-id@appspot.gserviceaccount.com"](mailto:my-project-id@appspot.gserviceaccount.com").Notice that wildcard characters (such as * and ?) are not supported. You must give a specific identity.  
  
## Options

Contains query options.

Fields  
---  
`expand_groups` |  `bool` Optional. If true, the identities section of the result will expand any Google groups appearing in an IAM policy binding.If `[IamPolicyAnalysisQuery.identity_selector](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.IamPolicyAnalysisQuery.FIELDS.google.cloud.asset.v1.IamPolicyAnalysisQuery.IdentitySelector.google.cloud.asset.v1.IamPolicyAnalysisQuery.identity_selector)` is specified, the identity in the result will be determined by the selector, and this flag is not allowed to set.If true, the default max expansion per group is 1000 for AssetService.AnalyzeIamPolicy][].Default is false.  
`expand_roles` |  `bool` Optional. If true, the access section of result will expand any roles appearing in IAM policy bindings to include their permissions.If `[IamPolicyAnalysisQuery.access_selector](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.IamPolicyAnalysisQuery.FIELDS.google.cloud.asset.v1.IamPolicyAnalysisQuery.AccessSelector.google.cloud.asset.v1.IamPolicyAnalysisQuery.access_selector)` is specified, the access section of the result will be determined by the selector, and this flag is not allowed to set.Default is false.  
`expand_resources` |  `bool` Optional. If true and `[IamPolicyAnalysisQuery.resource_selector](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.IamPolicyAnalysisQuery.FIELDS.google.cloud.asset.v1.IamPolicyAnalysisQuery.ResourceSelector.google.cloud.asset.v1.IamPolicyAnalysisQuery.resource_selector)` is not specified, the resource section of the result will expand any resource attached to an IAM policy to include resources lower in the resource hierarchy.For example, if the request analyzes for which resources user A has permission P, and the results include an IAM policy with P on a Google Cloud folder, the results will also include resources in that folder with permission P.If true and `[IamPolicyAnalysisQuery.resource_selector](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.IamPolicyAnalysisQuery.FIELDS.google.cloud.asset.v1.IamPolicyAnalysisQuery.ResourceSelector.google.cloud.asset.v1.IamPolicyAnalysisQuery.resource_selector)` is specified, the resource section of the result will expand the specified resource to include resources lower in the resource hierarchy. Only project or lower resources are supported. Folder and organization resources cannot be used together with this option.For example, if the request analyzes for which users have permission P on a Google Cloud project with this option enabled, the results will include all users who have permission P on that project or any lower resource.If true, the default max expansion per resource is 1000 for AssetService.AnalyzeIamPolicy][] and 100000 for AssetService.AnalyzeIamPolicyLongrunning][].Default is false.  
`output_resource_edges` |  `bool` Optional. If true, the result will output the relevant parent/child relationships between resources. Default is false.  
`output_group_edges` |  `bool` Optional. If true, the result will output the relevant membership relationships between groups and other groups, and between groups and principals. Default is false.  
`analyze_service_account_impersonation` |  `bool` Optional. If true, the response will include access analysis from identities to resources via service account impersonation. This is a very expensive operation, because many derived queries will be executed. We highly recommend you use `[AssetService.AnalyzeIamPolicyLongrunning](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.AssetService.AnalyzeIamPolicyLongrunning)` RPC instead.For example, if the request analyzes for which resources user A has permission P, and there's an IAM policy states user A has iam.serviceAccounts.getAccessToken permission to a service account SA, and there's another IAM policy states service account SA has permission P to a Google Cloud folder F, then user A potentially has access to the Google Cloud folder F. And those advanced analysis results will be included in `[AnalyzeIamPolicyResponse.service_account_impersonation_analysis](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.AnalyzeIamPolicyResponse.FIELDS.repeated.google.cloud.asset.v1.AnalyzeIamPolicyResponse.IamPolicyAnalysis.google.cloud.asset.v1.AnalyzeIamPolicyResponse.service_account_impersonation_analysis)`.Another example, if the request analyzes for who has permission P to a Google Cloud folder F, and there's an IAM policy states user A has iam.serviceAccounts.actAs permission to a service account SA, and there's another IAM policy states service account SA has permission P to the Google Cloud folder F, then user A potentially has access to the Google Cloud folder F. And those advanced analysis results will be included in `[AnalyzeIamPolicyResponse.service_account_impersonation_analysis](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.AnalyzeIamPolicyResponse.FIELDS.repeated.google.cloud.asset.v1.AnalyzeIamPolicyResponse.IamPolicyAnalysis.google.cloud.asset.v1.AnalyzeIamPolicyResponse.service_account_impersonation_analysis)`.Only the following permissions are considered in this analysis:

  * `iam.serviceAccounts.actAs`
  * `iam.serviceAccounts.signBlob`
  * `iam.serviceAccounts.signJwt`
  * `iam.serviceAccounts.getAccessToken`
  * `iam.serviceAccounts.getOpenIdToken`
  * `iam.serviceAccounts.implicitDelegation`

Default is false.  
  
## ResourceSelector

Specifies the resource to analyze for access policies, which may be set directly on the resource, or on ancestors such as organizations, folders or projects.

Fields  
---  
`full_resource_name` |  `string` Required. The [full resource name](https://cloud.google.com/asset-inventory/docs/resource-name-format) of a resource of [supported resource types](https://cloud.google.com/asset-inventory/docs/supported-asset-types#analyzable_asset_types).  
  
## IamPolicyAnalysisResult

IAM Policy analysis result, consisting of one IAM policy binding and derived access control lists.

Fields  
---  
`attached_resource_full_name` |  `string` The [full resource name](https://cloud.google.com/asset-inventory/docs/resource-name-format) of the resource to which the `[iam_binding](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.IamPolicyAnalysisResult.FIELDS.google.iam.v1.Binding.google.cloud.asset.v1.IamPolicyAnalysisResult.iam_binding)` policy attaches.  
`iam_binding` |  `[Binding](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.iam.v1#google.iam.v1.Binding)` The IAM policy binding under analysis.  
`access_control_lists[]` |  `[AccessControlList](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.IamPolicyAnalysisResult.AccessControlList)` The access control lists derived from the `[iam_binding](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.IamPolicyAnalysisResult.FIELDS.google.iam.v1.Binding.google.cloud.asset.v1.IamPolicyAnalysisResult.iam_binding)` that match or potentially match resource and access selectors specified in the request.  
`identity_list` |  `[IdentityList](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.IamPolicyAnalysisResult.IdentityList)` The identity list derived from members of the `[iam_binding](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.IamPolicyAnalysisResult.FIELDS.google.iam.v1.Binding.google.cloud.asset.v1.IamPolicyAnalysisResult.iam_binding)` that match or potentially match identity selector specified in the request.  
`fully_explored` |  `bool` Represents whether all analyses on the `[iam_binding](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.IamPolicyAnalysisResult.FIELDS.google.iam.v1.Binding.google.cloud.asset.v1.IamPolicyAnalysisResult.iam_binding)` have successfully finished.  
  
## Access

An IAM role or permission under analysis.

Fields  
---  
`analysis_state` |  `[IamPolicyAnalysisState](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.IamPolicyAnalysisState)` The analysis state of this access.  
Union field `oneof_access`.`oneof_access` can be only one of the following:  
`role` |  `string` The role.  
`permission` |  `string` The permission.  
  
## AccessControlList

An access control list, derived from the above IAM policy binding, which contains a set of resources and accesses. May include one item from each set to compose an access control entry.

NOTICE that there could be multiple access control lists for one IAM policy binding. The access control lists are created based on resource and access combinations.

For example, assume we have the following cases in one IAM policy binding: - Permission P1 and P2 apply to resource R1 and R2; - Permission P3 applies to resource R2 and R3;

This will result in the following access control lists: - AccessControlList 1: [R1, R2], [P1, P2] - AccessControlList 2: [R2, R3], [P3]

Fields  
---  
`resources[]` |  `[Resource](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.IamPolicyAnalysisResult.Resource)` The resources that match one of the following conditions: - The resource_selector, if it is specified in request; - Otherwise, resources reachable from the policy attached resource.  
`accesses[]` |  `[Access](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.IamPolicyAnalysisResult.Access)` The accesses that match one of the following conditions: - The access_selector, if it is specified in request; - Otherwise, access specifiers reachable from the policy binding's role.  
`resource_edges[]` |  `[Edge](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.IamPolicyAnalysisResult.Edge)` Resource edges of the graph starting from the policy attached resource to any descendant resources. The `[Edge.source_node](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.IamPolicyAnalysisResult.Edge.FIELDS.string.google.cloud.asset.v1.IamPolicyAnalysisResult.Edge.source_node)` contains the full resource name of a parent resource and `[Edge.target_node](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.IamPolicyAnalysisResult.Edge.FIELDS.string.google.cloud.asset.v1.IamPolicyAnalysisResult.Edge.target_node)` contains the full resource name of a child resource. This field is present only if the output_resource_edges option is enabled in request.  
`condition_evaluation` |  `[ConditionEvaluation](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.ConditionEvaluation)` Condition evaluation for this AccessControlList, if there is a condition defined in the above IAM policy binding.  
  
## Edge

A directional edge.

Fields  
---  
`source_node` |  `string` The source node of the edge. For example, it could be a full resource name for a resource node or an email of an identity.  
`target_node` |  `string` The target node of the edge. For example, it could be a full resource name for a resource node or an email of an identity.  
  
## Identity

An identity under analysis.

Fields  
---  
`name` |  `string` The identity of members, formatted as appear in an [IAM policy binding](https://cloud.google.com/iam/reference/rest/v1/Binding). For example, they might be formatted like the following:

  * user:[foo@google.com](mailto:foo@google.com)
  * group:[group1@google.com](mailto:group1@google.com)
  * serviceAccount:[s1@prj1.iam.gserviceaccount.com](mailto:s1@prj1.iam.gserviceaccount.com)
  * projectOwner:some_project_id
  * domain:google.com
  * allUsers

  
`analysis_state` |  `[IamPolicyAnalysisState](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.IamPolicyAnalysisState)` The analysis state of this identity.  
  
## IdentityList

The identities and group edges.

Fields  
---  
`identities[]` |  `[Identity](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.IamPolicyAnalysisResult.Identity)` Only the identities that match one of the following conditions will be presented: - The identity_selector, if it is specified in request; - Otherwise, identities reachable from the policy binding's members.  
`group_edges[]` |  `[Edge](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.IamPolicyAnalysisResult.Edge)` Group identity edges of the graph starting from the binding's group members to any node of the `[identities](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.IamPolicyAnalysisResult.IdentityList.FIELDS.repeated.google.cloud.asset.v1.IamPolicyAnalysisResult.Identity.google.cloud.asset.v1.IamPolicyAnalysisResult.IdentityList.identities)`. The `[Edge.source_node](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.IamPolicyAnalysisResult.Edge.FIELDS.string.google.cloud.asset.v1.IamPolicyAnalysisResult.Edge.source_node)` contains a group, such as `group:parent@google.com`. The `[Edge.target_node](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.IamPolicyAnalysisResult.Edge.FIELDS.string.google.cloud.asset.v1.IamPolicyAnalysisResult.Edge.target_node)` contains a member of the group, such as `group:child@google.com` or `user:foo@google.com`. This field is present only if the output_group_edges option is enabled in request.  
  
## Resource

A Google Cloud resource under analysis.

Fields  
---  
`full_resource_name` |  `string` The [full resource name](https://cloud.google.com/asset-inventory/docs/resource-name-format)  
`analysis_state` |  `[IamPolicyAnalysisState](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.IamPolicyAnalysisState)` The analysis state of this resource.  
  
## IamPolicyAnalysisState

Represents the detailed state of an entity under analysis, such as a resource, an identity or an access.

Fields  
---  
`code` |  `[Code](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.rpc#google.rpc.Code)` The Google standard error code that best describes the state. For example: - OK means the analysis on this entity has been successfully finished; - PERMISSION_DENIED means an access denied error is encountered; - DEADLINE_EXCEEDED means the analysis on this entity hasn't been started in time;  
`cause` |  `string` The human-readable description of the cause of failure.  
  
## IamPolicySearchResult

A result of IAM Policy search, containing information of an IAM policy.

Fields  
---  
`resource` |  `string` The full resource name of the resource associated with this IAM policy. Example: `//compute.googleapis.com/projects/my_project_123/zones/zone1/instances/instance1`. See [Cloud Asset Inventory Resource Name Format](https://cloud.google.com/asset-inventory/docs/resource-name-format) for more information.To search against the `resource`:

  * use a field query. Example: `resource:organizations/123`

  
`asset_type` |  `string` The type of the resource associated with this IAM policy. Example: `compute.googleapis.com/Disk`.To search against the `asset_type`:

  * specify the `asset_types` field in your search request.

  
`project` |  `string` The project that the associated Google Cloud resource belongs to, in the form of projects/{PROJECT_NUMBER}. If an IAM policy is set on a resource (like VM instance, Cloud Storage bucket), the project field will indicate the project that contains the resource. If an IAM policy is set on a folder or organization, this field will be empty.To search against the `project`:

  * specify the `scope` field as this project in your search request.

  
`folders[]` |  `string` The folder(s) that the IAM policy belongs to, in the form of folders/{FOLDER_NUMBER}. This field is available when the IAM policy belongs to one or more folders.To search against `folders`:

  * use a field query. Example: `folders:(123 OR 456)`
  * use a free text query. Example: `123`
  * specify the `scope` field as this folder in your search request.

  
`organization` |  `string` The organization that the IAM policy belongs to, in the form of organizations/{ORGANIZATION_NUMBER}. This field is available when the IAM policy belongs to an organization.To search against `organization`:

  * use a field query. Example: `organization:123`
  * use a free text query. Example: `123`
  * specify the `scope` field as this organization in your search request.

  
`policy` |  `[Policy](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.iam.v1#google.iam.v1.Policy)` The IAM policy directly set on the given resource. Note that the original IAM policy can contain multiple bindings. This only contains the bindings that match the given query. For queries that don't contain a constrain on policies (e.g., an empty query), this contains all the bindings.To search against the `policy` bindings:

  * use a field query: 
    * query by the policy contained members. Example: `policy:amy@gmail.com`
    * query by the policy contained roles. Example: `policy:roles/compute.admin`
    * query by the policy contained roles' included permissions. Example: `policy.role.permissions:compute.instances.create`

  
`explanation` |  `[Explanation](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.IamPolicySearchResult.Explanation)` Explanation about the IAM policy search result. It contains additional information to explain why the search result matches the query.  
  
## Explanation

Explanation about the IAM policy search result.

Fields  
---  
`matched_permissions` |  `map<string, `[Permissions](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.IamPolicySearchResult.Explanation.Permissions)`>` The map from roles to their included permissions that match the permission query (i.e., a query containing `policy.role.permissions:`). Example: if query `policy.role.permissions:compute.disk.get` matches a policy binding that contains owner role, the matched_permissions will be `{"roles/owner": ["compute.disk.get"]}`. The roles can also be found in the returned `policy` bindings. Note that the map is populated only for requests with permission queries.  
  
## Permissions

IAM permissions

Fields  
---  
`permissions[]` |  `string` A list of permissions. A sample permission string: `compute.disk.get`.  
  
## ListAssetsRequest

ListAssets request.

Fields  
---  
`parent` |  `string` Required. Name of the organization, folder, or project the assets belong to. Format: "organizations/[organization-number]" (such as "organizations/123"), "projects/[project-id]" (such as "projects/my-project-id"), "projects/[project-number]" (such as "projects/12345"), or "folders/[folder-number]" (such as "folders/12345"). Authorization requires one or more of the following [IAM](https://cloud.google.com/iam/docs/) permissions on the specified resource `parent`:

  * `cloudasset.assets.listResource`
  * `cloudasset.assets.listIamPolicy`
  * `cloudasset.assets.listOrgPolicy`
  * `cloudasset.assets.listAccessPolicy`
  * `cloudasset.assets.listOSInventories`

  
`read_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Timestamp to take an asset snapshot. This can only be set to a timestamp between the current time and the current time minus 35 days (inclusive). If not specified, the current time will be used. Due to delays in resource data collection and indexing, there is a volatile window during which running the same query may get different results.  
`asset_types[]` |  `string` A list of asset types to take a snapshot for. For example: "compute.googleapis.com/Disk".Regular expression is also supported. For example:

  * "compute.googleapis.com.*" snapshots resources whose asset type starts with "compute.googleapis.com".
  * ".*Instance" snapshots resources whose asset type ends with "Instance".
  * ".*Instance.*" snapshots resources whose asset type contains "Instance".

See [RE2](https://github.com/google/re2/wiki/Syntax) for all supported regular expression syntax. If the regular expression does not match any supported asset type, an INVALID_ARGUMENT error will be returned.If specified, only matching assets will be returned, otherwise, it will snapshot all asset types. See [Introduction to Cloud Asset Inventory](https://cloud.google.com/asset-inventory/docs/overview) for all supported asset types.  
`content_type` |  `[ContentType](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.ContentType)` Asset content type. If not specified, no content but the asset name will be returned.  
`page_size` |  `int32` The maximum number of assets to be returned in a single response. Default is 100, minimum is 1, and maximum is 1000.  
`page_token` |  `string` The `next_page_token` returned from the previous `ListAssetsResponse`, or unspecified for the first `ListAssetsRequest`. It is a continuation of a prior `ListAssets` call, and the API should return the next page of assets.  
`relationship_types[]` |  `string` A list of relationship types to output, for example: `INSTANCE_TO_INSTANCEGROUP`. This field should only be specified if content_type=RELATIONSHIP. * If specified: it snapshots specified relationships. It returns an error if any of the [relationship_types] doesn't belong to the supported relationship types of the [asset_types] or if any of the [asset_types] doesn't belong to the source types of the [relationship_types]. * Otherwise: it snapshots the supported relationships for all [asset_types] or returns an error if any of the [asset_types] has no relationship support. An unspecified asset types field means all supported asset_types. See [Introduction to Cloud Asset Inventory](https://cloud.google.com/asset-inventory/docs/overview) for all supported asset types and relationship types.  
  
## ListAssetsResponse

ListAssets response.

Fields  
---  
`read_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Time the snapshot was taken.  
`assets[]` |  `[Asset](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.Asset)` Assets.  
`next_page_token` |  `string` Token to retrieve the next page of results. It expires 72 hours after the page token for the first page is generated. Set to empty if there are no remaining results.  
  
## ListFeedsRequest

List asset feeds request.

Fields  
---  
`parent` |  `string` Required. The parent project/folder/organization whose feeds are to be listed. It can only be using project/folder/organization number (such as "folders/12345")", or a project ID (such as "projects/my-project-id").  
  
## ListFeedsResponse

Fields  
---  
`feeds[]` |  `[Feed](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.Feed)` A list of feeds.  
  
## ListSavedQueriesRequest

Request to list saved queries.

Fields  
---  
`parent` |  `string` Required. The parent project/folder/organization whose savedQueries are to be listed. It can only be using project/folder/organization number (such as "folders/12345")", or a project ID (such as "projects/my-project-id").  
`filter` |  `string` Optional. The expression to filter resources. The expression is a list of zero or more restrictions combined via logical operators `AND` and `OR`. When `AND` and `OR` are both used in the expression, parentheses must be appropriately used to group the combinations. The expression may also contain regular expressions.See <https://google.aip.dev/160> for more information on the grammar.  
`page_size` |  `int32` Optional. The maximum number of saved queries to return per page. The service may return fewer than this value. If unspecified, at most 50 will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000.  
`page_token` |  `string` Optional. A page token, received from a previous `ListSavedQueries` call. Provide this to retrieve the subsequent page.When paginating, all other parameters provided to `ListSavedQueries` must match the call that provided the page token.  
  
## ListSavedQueriesResponse

Response of listing saved queries.

Fields  
---  
`saved_queries[]` |  `[SavedQuery](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.SavedQuery)` A list of savedQueries.  
`next_page_token` |  `string` A token, which can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages.  
  
## MoveAnalysis

A message to group the analysis information.

Fields  
---  
`display_name` |  `string` The user friendly display name of the analysis. E.g. IAM, organization policy etc.  
Union field `result`.`result` can be only one of the following:  
`analysis` |  `[MoveAnalysisResult](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.MoveAnalysisResult)` Analysis result of moving the target resource.  
`error` |  `[Status](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.rpc#google.rpc.Status)` Description of error encountered when performing the analysis.  
  
## MoveAnalysisResult

An analysis result including blockers and warnings.

Fields  
---  
`blockers[]` |  `[MoveImpact](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.MoveImpact)` Blocking information that would prevent the target resource from moving to the specified destination at runtime.  
`warnings[]` |  `[MoveImpact](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.MoveImpact)` Warning information indicating that moving the target resource to the specified destination might be unsafe. This can include important policy information and configuration changes, but will not block moves at runtime.  
  
## MoveImpact

A message to group impacts of moving the target resource.

Fields  
---  
`detail` |  `string` User friendly impact detail in a free form message.  
  
## OutputConfig

Output configuration for export assets destination.

Fields  
---  
Union field `destination`. Asset export destination. `destination` can be only one of the following:  
`gcs_destination` |  `[GcsDestination](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.GcsDestination)` Destination on Cloud Storage.  
`bigquery_destination` |  `[BigQueryDestination](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.BigQueryDestination)` Destination on BigQuery. The output table stores the fields in asset Protobuf as columns in BigQuery.  
  
## OutputResult

Output result of export assets.

Fields  
---  
Union field `result`. Asset export result. `result` can be only one of the following:  
`gcs_result` |  `[GcsOutputResult](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.GcsOutputResult)` Export result on Cloud Storage.  
  
## PartitionSpec

Specifications of BigQuery partitioned table as export destination.

Fields  
---  
`partition_key` |  `[PartitionKey](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.PartitionSpec.PartitionKey)` The partition key for BigQuery partitioned table.  
  
## PartitionKey

This enum is used to determine the partition key column when exporting assets to BigQuery partitioned table(s). Note that, if the partition key is a timestamp column, the actual partition is based on its date value (expressed in UTC. see details in <https://cloud.google.com/bigquery/docs/partitioned-tables#date_timestamp_partitioned_tables)>.

Enums  
---  
`PARTITION_KEY_UNSPECIFIED` | Unspecified partition key. If used, it means using non-partitioned table.  
`READ_TIME` | The time when the snapshot is taken. If specified as partition key, the result table(s) is partitioned by the additional timestamp column, readTime. If [read_time] in ExportAssetsRequest is specified, the readTime column's value will be the same as it. Otherwise, its value will be the current time that is used to take the snapshot.  
`REQUEST_TIME` | The time when the request is received and started to be processed. If specified as partition key, the result table(s) is partitioned by the requestTime column, an additional timestamp column representing when the request was received.  
  
## PubsubDestination

A Pub/Sub destination.

Fields  
---  
`topic` |  `string` The name of the Pub/Sub topic to publish to. Example: `projects/PROJECT_ID/topics/TOPIC_ID`.  
  
## QueryAssetsOutputConfig

Output configuration query assets.

Fields  
---  
`bigquery_destination` |  `[BigQueryDestination](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.QueryAssetsOutputConfig.BigQueryDestination)` BigQuery destination where the query results will be saved.  
  
## BigQueryDestination

BigQuery destination.

Fields  
---  
`dataset` |  `string` Required. The BigQuery dataset where the query results will be saved. It has the format of "projects/{projectId}/datasets/{datasetId}".  
`table` |  `string` Required. The BigQuery table where the query results will be saved. If this table does not exist, a new table with the given name will be created.  
`write_disposition` |  `string` Specifies the action that occurs if the destination table or partition already exists. The following values are supported:

  * WRITE_TRUNCATE: If the table or partition already exists, BigQuery overwrites the entire table or all the partitions data.
  * WRITE_APPEND: If the table or partition already exists, BigQuery appends the data to the table or the latest partition.
  * WRITE_EMPTY: If the table already exists and contains data, a 'duplicate' error is returned in the job result.

The default value is WRITE_EMPTY.  
  
## QueryAssetsRequest

QueryAssets request.

Fields  
---  
`parent` |  `string` Required. The relative name of the root asset. This can only be an organization number (such as "organizations/123"), a project ID (such as "projects/my-project-id"), or a project number (such as "projects/12345"), or a folder number (such as "folders/123").Only assets belonging to the `parent` will be returned.  
`page_size` |  `int32` Optional. The maximum number of rows to return in the results. Responses are limited to 10 MB and 1000 rows.By default, the maximum row count is 1000. When the byte or row count limit is reached, the rest of the query results will be paginated.The field will be ignored when [output_config] is specified.  
`page_token` |  `string` Optional. A page token received from previous `QueryAssets`.The field will be ignored when [output_config] is specified.  
`timeout` |  `[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` Optional. Specifies the maximum amount of time that the client is willing to wait for the query to complete. By default, this limit is 5 min for the first query, and 1 minute for the following queries. If the query is complete, the `done` field in the `QueryAssetsResponse` is true, otherwise false.Like BigQuery [jobs.query API](https://cloud.google.com/bigquery/docs/reference/rest/v2/jobs/query#queryrequest) The call is not guaranteed to wait for the specified timeout; it typically returns after around 200 seconds (200,000 milliseconds), even if the query is not complete.The field will be ignored when [output_config] is specified.  
`output_config` |  `[QueryAssetsOutputConfig](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.QueryAssetsOutputConfig)` Optional. Destination where the query results will be saved.When this field is specified, the query results won't be saved in the [QueryAssetsResponse.query_result]. Instead [QueryAssetsResponse.output_config] will be set.Meanwhile, [QueryAssetsResponse.job_reference] will be set and can be used to check the status of the query job when passed to a following [QueryAssets] API call.  
Union field `query`.`query` can be only one of the following:  
`statement` |  `string` Optional. A SQL statement that's compatible with [BigQuery SQL](https://cloud.google.com/bigquery/docs/introduction-sql).  
`job_reference` |  `string` Optional. Reference to the query job, which is from the `QueryAssetsResponse` of previous `QueryAssets` call.  
Union field `time`. Specifies what time period or point in time to query asset metadata at. * unset - query asset metadata as it is right now * [read_time_window] - query asset metadata as it was at any point in time between [start_time] and [end_time]. * [read_time] - query asset metadata as it was at that point in time. If data for the timestamp/date range selected does not exist, it will simply return a valid response with no rows. `time` can be only one of the following:  
`read_time_window` |  `[TimeWindow](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.TimeWindow)` Optional. [start_time] is required. [start_time] must be less than [end_time] Defaults [end_time] to now if [start_time] is set and [end_time] isn't. Maximum permitted time range is 7 days.  
`read_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Optional. Queries cloud assets as they appeared at the specified point in time.  
  
## QueryAssetsResponse

QueryAssets response.

Fields  
---  
`job_reference` |  `string` Reference to a query job.  
`done` |  `bool` The query response, which can be either an `error` or a valid `response`.If `done` == `false` and the query result is being saved in an output, the output_config field will be set. If `done` == `true`, exactly one of `error`, `query_result` or `output_config` will be set. [done] is unset unless the [QueryAssetsResponse] contains a [QueryAssetsResponse.job_reference].  
Union field `response`.`response` can be only one of the following:  
`error` |  `[Status](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.rpc#google.rpc.Status)` Error status.  
`query_result` |  `[QueryResult](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.QueryResult)` Result of the query.  
`output_config` |  `[QueryAssetsOutputConfig](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.QueryAssetsOutputConfig)` Output configuration, which indicates that instead of being returned in an API response on the fly, the query result will be saved in a specific output.  
  
## QueryResult

Execution results of the query.

The result is formatted as rows represented by BigQuery compatible [schema]. When pagination is necessary, it will contains the page token to retrieve the results of following pages.

Fields  
---  
`rows[]` |  `[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` Each row hold a query result in the format of `Struct`.  
`schema` |  `[TableSchema](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.TableSchema)` Describes the format of the [rows].  
`next_page_token` |  `string` Token to retrieve the next page of the results.  
`total_rows` |  `int64` Total rows of the whole query results.  
  
## RelatedAsset

An asset identifier in Google Cloud which contains its name, type and ancestors. An asset can be any resource in the Google Cloud [resource hierarchy](https://cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy), a resource outside the Google Cloud resource hierarchy (such as Google Kubernetes Engine clusters and objects), or a policy (e.g. IAM policy). See [Supported asset types](https://cloud.google.com/asset-inventory/docs/supported-asset-types) for more information.

Fields  
---  
`asset` |  `string` The full name of the asset. Example: `//compute.googleapis.com/projects/my_project_123/zones/zone1/instances/instance1`See [Resource names](https://cloud.google.com/apis/design/resource_names#full_resource_name) for more information.  
`asset_type` |  `string` The type of the asset. Example: `compute.googleapis.com/Disk`See [Supported asset types](https://cloud.google.com/asset-inventory/docs/supported-asset-types) for more information.  
`ancestors[]` |  `string` The ancestors of an asset in Google Cloud [resource hierarchy](https://cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy), represented as a list of relative resource names. An ancestry path starts with the closest ancestor in the hierarchy and ends at root.Example: `["projects/123456789", "folders/5432", "organizations/1234"]`  
`relationship_type` |  `string` The unique identifier of the relationship type. Example: `INSTANCE_TO_INSTANCEGROUP`  
  
## RelatedAssets

This item is deprecated!

DEPRECATED. This message only presents for the purpose of backward-compatibility. The server will never populate this message in responses. The detailed related assets with the `relationship_type`.

Fields  
---  
`relationship_attributes` |  `[RelationshipAttributes](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.RelationshipAttributes)` The detailed relationship attributes.  
`assets[]` |  `[RelatedAsset](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.RelatedAsset)` The peer resources of the relationship.  
  
## RelatedResource

The detailed related resource.

Fields  
---  
`asset_type` |  `string` The type of the asset. Example: `compute.googleapis.com/Instance`  
`full_resource_name` |  `string` The full resource name of the related resource. Example: `//compute.googleapis.com/projects/my_proj_123/zones/instance/instance123`  
  
## RelatedResources

The related resources of the primary resource.

Fields  
---  
`related_resources[]` |  `[RelatedResource](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.RelatedResource)` The detailed related resources of the primary resource.  
  
## RelationshipAttributes

This item is deprecated!

DEPRECATED. This message only presents for the purpose of backward-compatibility. The server will never populate this message in responses. The relationship attributes which include `type`, `source_resource_type`, `target_resource_type` and `action`.

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
`parent` |  `string` The full name of the immediate parent of this resource. See [Resource Names](https://cloud.google.com/apis/design/resource_names#full_resource_name) for more information.For Google Cloud assets, this value is the parent resource defined in the [IAM policy hierarchy](https://cloud.google.com/iam/docs/overview#policy_hierarchy). Example: `//cloudresourcemanager.googleapis.com/projects/my_project_123`  
`data` |  `[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` The content of the resource, in which some sensitive fields are removed and may not be present.  
`location` |  `string` The location of the resource in Google Cloud, such as its zone and region. For more information, see <https://cloud.google.com/about/locations/>.  
  
## ResourceOwners

The resource owners information.

Fields  
---  
`resource_owners[]` |  `string` List of resource owners.  
  
## ResourceSearchResult

A result of Resource Search, containing information of a cloud resource.

Fields  
---  
`name` |  `string` The full resource name of this resource. Example: `//compute.googleapis.com/projects/my_project_123/zones/zone1/instances/instance1`. See [Cloud Asset Inventory Resource Name Format](https://cloud.google.com/asset-inventory/docs/resource-name-format) for more information.To search against the `name`:

  * Use a field query. Example: `name:instance1`
  * Use a free text query. Example: `instance1`

  
`asset_type` |  `string` The type of this resource. Example: `compute.googleapis.com/Disk`.To search against the `asset_type`:

  * Specify the `asset_type` field in your search request.

  
`project` |  `string` The project that this resource belongs to, in the form of projects/{PROJECT_NUMBER}. This field is available when the resource belongs to a project.To search against `project`:

  * Use a field query. Example: `project:12345`
  * Use a free text query. Example: `12345`
  * Specify the `scope` field as this project in your search request.

  
`folders[]` |  `string` The folder(s) that this resource belongs to, in the form of folders/{FOLDER_NUMBER}. This field is available when the resource belongs to one or more folders.To search against `folders`:

  * Use a field query. Example: `folders:(123 OR 456)`
  * Use a free text query. Example: `123`
  * Specify the `scope` field as this folder in your search request.

  
`organization` |  `string` The organization that this resource belongs to, in the form of organizations/{ORGANIZATION_NUMBER}. This field is available when the resource belongs to an organization.To search against `organization`:

  * Use a field query. Example: `organization:123`
  * Use a free text query. Example: `123`
  * Specify the `scope` field as this organization in your search request.

  
`display_name` |  `string` The display name of this resource. This field is available only when the resource's Protobuf contains it.To search against the `display_name`:

  * Use a field query. Example: `displayName:"My Instance"`
  * Use a free text query. Example: `"My Instance"`

  
`description` |  `string` One or more paragraphs of text description of this resource. Maximum length could be up to 1M bytes. This field is available only when the resource's Protobuf contains it.To search against the `description`:

  * Use a field query. Example: `description:"important instance"`
  * Use a free text query. Example: `"important instance"`

  
`location` |  `string` Location can be `global`, regional like `us-east1`, or zonal like `us-west1-b`. This field is available only when the resource's Protobuf contains it.To search against the `location`:

  * Use a field query. Example: `location:us-west*`
  * Use a free text query. Example: `us-west*`

  
`labels` |  `map<string, string>` User labels associated with this resource. See [Labelling and grouping Google Cloud resources](https://cloud.google.com/blog/products/gcp/labelling-and-grouping-your-google-cloud-platform-resources) for more information. This field is available only when the resource's Protobuf contains it.To search against the `labels`:

  * Use a field query: 
    * query on any label's key or value. Example: `labels:prod`
    * query by a given label. Example: `labels.env:prod`
    * query by a given label's existence. Example: `labels.env:*`
  * Use a free text query. Example: `prod`

  
`network_tags[]` |  `string` Network tags associated with this resource. Like labels, network tags are a type of annotations used to group Google Cloud resources. See [Labelling Google Cloud resources](https://cloud.google.com/blog/products/gcp/labelling-and-grouping-your-google-cloud-platform-resources) for more information. This field is available only when the resource's Protobuf contains it.To search against the `network_tags`:

  * Use a field query. Example: `networkTags:internal`
  * Use a free text query. Example: `internal`

  
`kms_key  
**(deprecated)**` |  `string` This item is deprecated!The Cloud KMS [CryptoKey](https://cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys) name or [CryptoKeyVersion](https://cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions) name.This field only presents for the purpose of backward compatibility. Use the `kms_keys` field to retrieve Cloud KMS key information. This field is available only when the resource's Protobuf contains it and will only be populated for [these resource types](https://cloud.google.com/asset-inventory/docs/legacy-field-names#resource_types_with_the_to_be_deprecated_kmskey_field) for backward compatible purposes.To search against the `kms_key`:

  * Use a field query. Example: `kmsKey:key`
  * Use a free text query. Example: `key`

  
`kms_keys[]` |  `string` The Cloud KMS [CryptoKey](https://cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys) names or [CryptoKeyVersion](https://cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions) names. This field is available only when the resource's Protobuf contains it.To search against the `kms_keys`:

  * Use a field query. Example: `kmsKeys:key`
  * Use a free text query. Example: `key`

  
`create_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` The create timestamp of this resource, at which the resource was created. The granularity is in seconds. Timestamp.nanos will always be 0. This field is available only when the resource's Protobuf contains it.To search against `create_time`:

  * Use a field query. 
    * value in seconds since unix epoch. Example: `createTime > 1609459200`
    * value in date string. Example: `createTime > 2021-01-01`
    * value in date-time string (must be quoted). Example: `createTime > "2021-01-01T00:00:00"`

  
`update_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` The last update timestamp of this resource, at which the resource was last modified or deleted. The granularity is in seconds. Timestamp.nanos will always be 0. This field is available only when the resource's Protobuf contains it.To search against `update_time`:

  * Use a field query. 
    * value in seconds since unix epoch. Example: `updateTime < 1609459200`
    * value in date string. Example: `updateTime < 2021-01-01`
    * value in date-time string (must be quoted). Example: `updateTime < "2021-01-01T00:00:00"`

  
`state` |  `string` The state of this resource. Different resources types have different state definitions that are mapped from various fields of different resource types. This field is available only when the resource's Protobuf contains it.Example: If the resource is an instance provided by Compute Engine, its state will include PROVISIONING, STAGING, RUNNING, STOPPING, SUSPENDING, SUSPENDED, REPAIRING, and TERMINATED. See `status` definition in [API Reference](https://cloud.google.com/compute/docs/reference/rest/v1/instances). If the resource is a project provided by Resource Manager, its state will include LIFECYCLE_STATE_UNSPECIFIED, ACTIVE, DELETE_REQUESTED and DELETE_IN_PROGRESS. See `lifecycleState` definition in [API Reference](https://cloud.google.com/resource-manager/reference/rest/v1/projects).To search against the `state`:

  * Use a field query. Example: `state:RUNNING`
  * Use a free text query. Example: `RUNNING`

  
`additional_attributes` |  `[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` The additional searchable attributes of this resource. The attributes may vary from one resource type to another. Examples: `projectId` for Project, `dnsName` for DNS ManagedZone. This field contains a subset of the resource metadata fields that are returned by the List or Get APIs provided by the corresponding Google Cloud service (e.g., Compute Engine). see [API references and supported searchable attributes](https://cloud.google.com/asset-inventory/docs/supported-asset-types) to see which fields are included.You can search values of these fields through free text search. However, you should not consume the field programically as the field names and values may change as the Google Cloud service updates to a new incompatible API version.To search against the `additional_attributes`:

  * Use a free text query to match the attributes values. Example: to search `additional_attributes = { dnsName: "foobar" }`, you can issue a query `foobar`.

  
`parent_full_resource_name` |  `string` The full resource name of this resource's parent, if it has one. To search against the `parent_full_resource_name`:

  * Use a field query. Example: `parentFullResourceName:"project-name"`
  * Use a free text query. Example: `project-name`

  
`versioned_resources[]` |  `[VersionedResource](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.VersionedResource)` Versioned resource representations of this resource. This is repeated because there could be multiple versions of resource representations during version migration.This `versioned_resources` field is not searchable. Some attributes of the resource representations are exposed in `additional_attributes` field, so as to allow users to search on them.  
`attached_resources[]` |  `[AttachedResource](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.AttachedResource)` Attached resources of this resource. For example, an OSConfig Inventory is an attached resource of a Compute Instance. This field is repeated because a resource could have multiple attached resources.This `attached_resources` field is not searchable. Some attributes of the attached resources are exposed in `additional_attributes` field, so as to allow users to search on them.  
`relationships` |  `map<string, `[RelatedResources](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.RelatedResources)`>` A map of related resources of this resource, keyed by the relationship type. A relationship type is in the format of {SourceType}_{ACTION}_{DestType}. Example: `DISK_TO_INSTANCE`, `DISK_TO_NETWORK`, `INSTANCE_TO_INSTANCEGROUP`. See [supported relationship types](https://cloud.google.com/asset-inventory/docs/supported-asset-types#supported_relationship_types).  
`tag_keys[]  
**(deprecated)**` |  `string` This item is deprecated!This field is only present for the purpose of backward compatibility. Use the `tags` field instead.TagKey namespaced names, in the format of {ORG_ID}/{TAG_KEY_SHORT_NAME}. To search against the `tagKeys`:

  * Use a field query. Example:
    * `tagKeys:"123456789/env*"`
    * `tagKeys="123456789/env"`
    * `tagKeys:"env"`
  * Use a free text query. Example:
    * `env`

  
`tag_values[]  
**(deprecated)**` |  `string` This item is deprecated!This field is only present for the purpose of backward compatibility. Use the `tags` field instead.TagValue namespaced names, in the format of {ORG_ID}/{TAG_KEY_SHORT_NAME}/{TAG_VALUE_SHORT_NAME}. To search against the `tagValues`:

  * Use a field query. Example:
    * `tagValues:"env"`
    * `tagValues:"env/prod"`
    * `tagValues:"123456789/env/prod*"`
    * `tagValues="123456789/env/prod"`
  * Use a free text query. Example:
    * `prod`

  
`tag_value_ids[]  
**(deprecated)**` |  `string` This item is deprecated!This field is only present for the purpose of backward compatibility. Use the `tags` field instead.TagValue IDs, in the format of tagValues/{TAG_VALUE_ID}. To search against the `tagValueIds`:

  * Use a field query. Example:
    * `tagValueIds="tagValues/456"`
  * Use a free text query. Example:
    * `456`

  
`tags[]` |  `[Tag](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.Tag)` The tags directly attached to this resource.To search against the `tags`:

  * Use a field query. Example:
    * `tagKeys:"123456789/env*"`
    * `tagKeys="123456789/env"`
    * `tagKeys:"env"`
    * `tagKeyIds="tagKeys/123"`
    * `tagValues:"env"`
    * `tagValues:"env/prod"`
    * `tagValues:"123456789/env/prod*"`
    * `tagValues="123456789/env/prod"`
    * `tagValueIds="tagValues/456"`
  * Use a free text query. Example:
    * `env/prod`

  
`effective_tags[]` |  `[EffectiveTagDetails](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.EffectiveTagDetails)` The effective tags on this resource. All of the tags that are both attached to and inherited by a resource are collectively called the effective tags. For more information, see [tag inheritance](https://cloud.google.com/resource-manager/docs/tags/tags-overview#inheritance).To search against the `effective_tags`:

  * Use a field query. Example: 
    * `effectiveTagKeys:"123456789/env*"`
    * `effectiveTagKeys="123456789/env"`
    * `effectiveTagKeys:"env"`
    * `effectiveTagKeyIds="tagKeys/123"`
    * `effectiveTagValues:"env"`
    * `effectiveTagValues:"env/prod"`
    * `effectiveTagValues:"123456789/env/prod*"`
    * `effectiveTagValues="123456789/env/prod"`
    * `effectiveTagValueIds="tagValues/456"`

  
`enrichments[]` |  `[AssetEnrichment](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.AssetEnrichment)` Enrichments of the asset. Currently supported enrichment types with SearchAllResources API:

  * RESOURCE_OWNERS

The corresponding read masks in order to get the enrichment:

  * enrichments.resource_owners

The corresponding required permissions:

  * cloudasset.assets.searchEnrichmentResourceOwners

Example query to get resource owner enrichment:
    
    
      scope: "projects/my-project"
      query: "name: my-project"
      assetTypes: "cloudresourcemanager.googleapis.com/Project"
      readMask: {
         paths: "asset_type"
         paths: "name"
         paths: "enrichments.resource_owners"
      }
      
  
`parent_asset_type` |  `string` The type of this resource's immediate parent, if there is one.To search against the `parent_asset_type`:

  * Use a field query. Example: `parentAssetType:"cloudresourcemanager.googleapis.com/Project"`
  * Use a free text query. Example: `cloudresourcemanager.googleapis.com/Project`

  
`scc_security_marks` |  `map<string, string>` The actual content of Security Command Center security marks associated with the asset.To search against SCC SecurityMarks field:

  * Use a field query: 
    * query by a given key value pair. Example: `sccSecurityMarks.foo=bar`
    * query by a given key's existence. Example: `sccSecurityMarks.foo:*`

  
  
## SavedQuery

A saved query which can be shared with others or used later.

Fields  
---  
`name` |  `string` The resource name of the saved query. The format must be:

  * projects/project_number/savedQueries/saved_query_id
  * folders/folder_number/savedQueries/saved_query_id
  * organizations/organization_number/savedQueries/saved_query_id

  
`description` |  `string` The description of this saved query. This value should be fewer than 255 characters.  
`create_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. The create time of this saved query.  
`creator` |  `string` Output only. The account's email address who has created this saved query.  
`last_update_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. The last update time of this saved query.  
`last_updater` |  `string` Output only. The account's email address who has updated this saved query most recently.  
`labels` |  `map<string, string>` Labels applied on the resource. This value should not contain more than 10 entries. The key and value of each entry must be non-empty and fewer than 64 characters.  
`content` |  `[QueryContent](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.SavedQuery.QueryContent)` The query content.  
  
## QueryContent

The query content.

Fields  
---  
Union field `query_content`.`query_content` can be only one of the following:  
`iam_policy_analysis_query` |  `[IamPolicyAnalysisQuery](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.IamPolicyAnalysisQuery)` An IAM Policy Analysis query, which could be used in the `[AssetService.AnalyzeIamPolicy](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.AssetService.AnalyzeIamPolicy)` RPC or the `[AssetService.AnalyzeIamPolicyLongrunning](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.AssetService.AnalyzeIamPolicyLongrunning)` RPC.  
  
## SearchAllIamPoliciesRequest

Search all IAM policies request.

Fields  
---  
`scope` |  `string` Required. A scope can be a project, a folder, or an organization. The search is limited to the IAM policies within the `scope`. The caller must be granted the [`cloudasset.assets.searchAllIamPolicies`](https://cloud.google.com/asset-inventory/docs/access-control#required_permissions) permission on the desired scope.The allowed values are:

  * projects/{PROJECT_ID} (e.g., "projects/foo-bar")
  * projects/{PROJECT_NUMBER} (e.g., "projects/12345678")
  * folders/{FOLDER_NUMBER} (e.g., "folders/1234567")
  * organizations/{ORGANIZATION_NUMBER} (e.g., "organizations/123456")

Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `scope`:

  * `cloudasset.assets.searchAllIamPolicies`

  
`query` |  `string` Optional. The query statement. See [how to construct a query](https://cloud.google.com/asset-inventory/docs/searching-iam-policies#how_to_construct_a_query) for more information. If not specified or empty, it will search all the IAM policies within the specified `scope`. Note that the query string is compared against each IAM policy binding, including its principals, roles, and IAM conditions. The returned IAM policies will only contain the bindings that match your query. To learn more about the IAM policy structure, see the [IAM policy documentation](https://cloud.google.com/iam/help/allow-policies/structure).Examples:

  * `policy:amy@gmail.com` to find IAM policy bindings that specify user "amy@gmail.com".
  * `policy:roles/compute.admin` to find IAM policy bindings that specify the Compute Admin role.
  * `policy:comp*` to find IAM policy bindings that contain "comp" as a prefix of any word in the binding.
  * `policy.role.permissions:storage.buckets.update` to find IAM policy bindings that specify a role containing "storage.buckets.update" permission. Note that if callers don't have `iam.roles.get` access to a role's included permissions, policy bindings that specify this role will be dropped from the search results.
  * `policy.role.permissions:upd*` to find IAM policy bindings that specify a role containing "upd" as a prefix of any word in the role permission. Note that if callers don't have `iam.roles.get` access to a role's included permissions, policy bindings that specify this role will be dropped from the search results.
  * `resource:organizations/123456` to find IAM policy bindings that are set on "organizations/123456".
  * `resource=//cloudresourcemanager.googleapis.com/projects/myproject` to find IAM policy bindings that are set on the project named "myproject".
  * `Important` to find IAM policy bindings that contain "Important" as a word in any of the searchable fields (except for the included permissions).
  * `resource:(instance1 OR instance2) policy:amy` to find IAM policy bindings that are set on resources "instance1" or "instance2" and also specify user "amy".
  * `roles:roles/compute.admin` to find IAM policy bindings that specify the Compute Admin role.
  * `memberTypes:user` to find IAM policy bindings that contain the principal type "user".

  
`page_size` |  `int32` Optional. The page size for search result pagination. Page size is capped at 500 even if a larger value is given. If set to zero or a negative value, server will pick an appropriate default. Returned results may be fewer than requested. When this happens, there could be more results as long as `next_page_token` is returned.  
`page_token` |  `string` Optional. If present, retrieve the next batch of results from the preceding call to this method. `page_token` must be the value of `next_page_token` from the previous response. The values of all other method parameters must be identical to those in the previous call.  
`asset_types[]` |  `string` Optional. A list of asset types that the IAM policies are attached to. If empty, it will search the IAM policies that are attached to all the asset types [supported by search APIs](https://cloud.google.com/asset-inventory/docs/supported-asset-types)Regular expressions are also supported. For example:

  * "compute.googleapis.com.*" snapshots IAM policies attached to asset type starts with "compute.googleapis.com".
  * ".*Instance" snapshots IAM policies attached to asset type ends with "Instance".
  * ".*Instance.*" snapshots IAM policies attached to asset type contains "Instance".

See [RE2](https://github.com/google/re2/wiki/Syntax) for all supported regular expression syntax. If the regular expression does not match any supported asset type, an INVALID_ARGUMENT error will be returned.  
`order_by` |  `string` Optional. A comma-separated list of fields specifying the sorting order of the results. The default order is ascending. Add " DESC" after the field name to indicate descending order. Redundant space characters are ignored. Example: "assetType DESC, resource". Only singular primitive fields in the response are sortable: * resource * assetType * project All the other fields such as repeated fields (e.g., `folders`) and non-primitive fields (e.g., `policy`) are not supported.  
  
## SearchAllIamPoliciesResponse

Search all IAM policies response.

Fields  
---  
`results[]` |  `[IamPolicySearchResult](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.IamPolicySearchResult)` A list of IAM policies that match the search query. Related information such as the associated resource is returned along with the policy.  
`next_page_token` |  `string` Set if there are more results than those appearing in this response; to get the next set of results, call this method again, using this value as the `page_token`.  
  
## SearchAllResourcesRequest

Search all resources request.

Fields  
---  
`scope` |  `string` Required. A scope can be a project, a folder, or an organization. The search is limited to the resources within the `scope`. The caller must be granted the [`cloudasset.assets.searchAllResources`](https://cloud.google.com/asset-inventory/docs/access-control#required_permissions) permission on the desired scope.The allowed values are:

  * projects/{PROJECT_ID} (e.g., "projects/foo-bar")
  * projects/{PROJECT_NUMBER} (e.g., "projects/12345678")
  * folders/{FOLDER_NUMBER} (e.g., "folders/1234567")
  * organizations/{ORGANIZATION_NUMBER} (e.g., "organizations/123456")

Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `scope`:

  * `cloudasset.assets.searchAllResources`

  
`query` |  `string` Optional. The query statement. See [how to construct a query](https://cloud.google.com/asset-inventory/docs/searching-resources#how_to_construct_a_query) for more information. If not specified or empty, it will search all the resources within the specified `scope`.Examples:

  * `name:Important` to find Google Cloud resources whose name contains `Important` as a word.
  * `name=Important` to find the Google Cloud resource whose name is exactly `Important`.
  * `displayName:Impor*` to find Google Cloud resources whose display name contains `Impor` as a prefix of any word in the field.
  * `location:us-west*` to find Google Cloud resources whose location contains both `us` and `west` as prefixes.
  * `labels:prod` to find Google Cloud resources whose labels contain `prod` as a key or value.
  * `labels.env:prod` to find Google Cloud resources that have a label `env` and its value is `prod`.
  * `labels.env:*` to find Google Cloud resources that have a label `env`.
  * `tagKeys:env` to find Google Cloud resources that have directly attached tags where the [`TagKey.namespacedName`](https://cloud.google.com/resource-manager/reference/rest/v3/tagKeys#resource:-tagkey) contains `env`.
  * `tagValues:prod*` to find Google Cloud resources that have directly attached tags where the [`TagValue.namespacedName`](https://cloud.google.com/resource-manager/reference/rest/v3/tagValues#resource:-tagvalue) contains a word prefixed by `prod`.
  * `tagValueIds=tagValues/123` to find Google Cloud resources that have directly attached tags where the [`TagValue.name`](https://cloud.google.com/resource-manager/reference/rest/v3/tagValues#resource:-tagvalue) is exactly `tagValues/123`.
  * `effectiveTagKeys:env` to find Google Cloud resources that have directly attached or inherited tags where the [`TagKey.namespacedName`](https://cloud.google.com/resource-manager/reference/rest/v3/tagKeys#resource:-tagkey) contains `env`.
  * `effectiveTagValues:prod*` to find Google Cloud resources that have directly attached or inherited tags where the [`TagValue.namespacedName`](https://cloud.google.com/resource-manager/reference/rest/v3/tagValues#resource:-tagvalue) contains a word prefixed by `prod`.
  * `effectiveTagValueIds=tagValues/123` to find Google Cloud resources that have directly attached or inherited tags where the [`TagValue.name`](https://cloud.google.com/resource-manager/reference/rest/v3/tagValues#resource:-tagvalue) is exactly `tagValues/123`.
  * `kmsKey:key` to find Google Cloud resources encrypted with a customer-managed encryption key whose name contains `key` as a word. This field is deprecated. Use the `kmsKeys` field to retrieve Cloud KMS key information.
  * `kmsKeys:key` to find Google Cloud resources encrypted with customer-managed encryption keys whose name contains the word `key`.
  * `relationships:instance-group-1` to find Google Cloud resources that have relationships with `instance-group-1` in the related resource name.
  * `relationships:INSTANCE_TO_INSTANCEGROUP` to find Compute Engine instances that have relationships of type `INSTANCE_TO_INSTANCEGROUP`.
  * `relationships.INSTANCE_TO_INSTANCEGROUP:instance-group-1` to find Compute Engine instances that have relationships with `instance-group-1` in the Compute Engine instance group resource name, for relationship type `INSTANCE_TO_INSTANCEGROUP`.
  * `sccSecurityMarks.key=value` to find Cloud resources that are attached with security marks whose key is `key` and value is `value`.
  * `sccSecurityMarks.key:*` to find Cloud resources that are attached with security marks whose key is `key`.
  * `state:ACTIVE` to find Google Cloud resources whose state contains `ACTIVE` as a word.
  * `NOT state:ACTIVE` to find Google Cloud resources whose state doesn't contain `ACTIVE` as a word.
  * `createTime<1609459200` to find Google Cloud resources that were created before `2021-01-01 00:00:00 UTC`. `1609459200` is the epoch timestamp of `2021-01-01 00:00:00 UTC` in seconds.
  * `updateTime>1609459200` to find Google Cloud resources that were updated after `2021-01-01 00:00:00 UTC`. `1609459200` is the epoch timestamp of `2021-01-01 00:00:00 UTC` in seconds.
  * `Important` to find Google Cloud resources that contain `Important` as a word in any of the searchable fields.
  * `Impor*` to find Google Cloud resources that contain `Impor` as a prefix of any word in any of the searchable fields.
  * `Important location:(us-west1 OR global)` to find Google Cloud resources that contain `Important` as a word in any of the searchable fields and are also located in the `us-west1` region or the `global` location.

  
`asset_types[]` |  `string` Optional. A list of asset types that this request searches for. If empty, it will search all the asset types [supported by search APIs](https://cloud.google.com/asset-inventory/docs/supported-asset-types).Regular expressions are also supported. For example:

  * "compute.googleapis.com.*" snapshots resources whose asset type starts with "compute.googleapis.com".
  * ".*Instance" snapshots resources whose asset type ends with "Instance".
  * ".*Instance.*" snapshots resources whose asset type contains "Instance".

See [RE2](https://github.com/google/re2/wiki/Syntax) for all supported regular expression syntax. If the regular expression does not match any supported asset type, an INVALID_ARGUMENT error will be returned.  
`page_size` |  `int32` Optional. The page size for search result pagination. Page size is capped at 500 even if a larger value is given. If set to zero or a negative value, server will pick an appropriate default. Returned results may be fewer than requested. When this happens, there could be more results as long as `next_page_token` is returned.  
`page_token` |  `string` Optional. If present, then retrieve the next batch of results from the preceding call to this method. `page_token` must be the value of `next_page_token` from the previous response. The values of all other method parameters, must be identical to those in the previous call.  
`order_by` |  `string` Optional. A comma-separated list of fields specifying the sorting order of the results. The default order is ascending. Add " DESC" after the field name to indicate descending order. Redundant space characters are ignored. Example: "location DESC, name". Only the following fields in the response are sortable:

  * name
  * assetType
  * project
  * displayName
  * description
  * location
  * createTime
  * updateTime
  * state
  * parentFullResourceName
  * parentAssetType

  
`read_mask` |  `[FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` Optional. A comma-separated list of fields that you want returned in the results. The following fields are returned by default if not specified:

  * `name`
  * `assetType`
  * `project`
  * `folders`
  * `organization`
  * `displayName`
  * `description`
  * `location`
  * `labels`
  * `tags`
  * `effectiveTags`
  * `networkTags`
  * `kmsKeys`
  * `createTime`
  * `updateTime`
  * `state`
  * `additionalAttributes`
  * `parentFullResourceName`
  * `parentAssetType`

Some fields of large size, such as `versionedResources`, `attachedResources`, `effectiveTags` etc., are not returned by default, but you can specify them in the `read_mask` parameter if you want to include them. If `"*"` is specified, all [available fields](https://cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/searchAllResources#resourcesearchresult) are returned. Examples: `"name,location"`, `"name,versionedResources"`, `"*"`. Any invalid field path will trigger INVALID_ARGUMENT error.  
  
## SearchAllResourcesResponse

Search all resources response.

Fields  
---  
`results[]` |  `[ResourceSearchResult](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.ResourceSearchResult)` A list of Resources that match the search query. It contains the resource standard metadata information.  
`next_page_token` |  `string` If there are more results than those appearing in this response, then `next_page_token` is included. To get the next set of results, call this method again using the value of `next_page_token` as `page_token`.  
  
## TableFieldSchema

A field in TableSchema.

Fields  
---  
`field` |  `string` The field name. The name must contain only letters (a-z, A-Z), numbers (0-9), or underscores (_), and must start with a letter or underscore. The maximum length is 128 characters.  
`type` |  `string` The field data type. Possible values include * STRING * BYTES * INTEGER * FLOAT * BOOLEAN * TIMESTAMP * DATE * TIME * DATETIME * GEOGRAPHY, * NUMERIC, * BIGNUMERIC, * RECORD (where RECORD indicates that the field contains a nested schema).  
`mode` |  `string` The field mode. Possible values include NULLABLE, REQUIRED and REPEATED. The default value is NULLABLE.  
`fields[]` |  `[TableFieldSchema](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.TableFieldSchema)` Describes the nested schema fields if the type property is set to RECORD.  
  
## TableSchema

BigQuery Compatible table schema.

Fields  
---  
`fields[]` |  `[TableFieldSchema](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.TableFieldSchema)` Describes the fields in a table.  
  
## Tag

The key and value for a [tag](https://cloud.google.com/resource-manager/docs/tags/tags-overview).

Fields  
---  
`tag_key` |  `string` TagKey namespaced name, in the format of {ORG_ID}/{TAG_KEY_SHORT_NAME}.  
`tag_key_id` |  `string` TagKey ID, in the format of tagKeys/{TAG_KEY_ID}.  
`tag_value` |  `string` TagValue namespaced name, in the format of {ORG_ID}/{TAG_KEY_SHORT_NAME}/{TAG_VALUE_SHORT_NAME}.  
`tag_value_id` |  `string` TagValue ID, in the format of tagValues/{TAG_VALUE_ID}.  
  
## TemporalAsset

An asset in Google Cloud and its temporal metadata, including the time window when it was observed and its status during that window.

Fields  
---  
`window` |  `[TimeWindow](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.TimeWindow)` The time window when the asset data and state was observed.  
`deleted` |  `bool` Whether the asset has been deleted or not.  
`asset` |  `[Asset](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.Asset)` An asset in Google Cloud.  
`prior_asset_state` |  `[PriorAssetState](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.TemporalAsset.PriorAssetState)` State of prior_asset.  
`prior_asset` |  `[Asset](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.Asset)` Prior copy of the asset. Populated if prior_asset_state is PRESENT. Currently this is only set for responses in Real-Time Feed.  
  
## PriorAssetState

State of prior asset.

Enums  
---  
`PRIOR_ASSET_STATE_UNSPECIFIED` | prior_asset is not applicable for the current asset.  
`PRESENT` | prior_asset is populated correctly.  
`INVALID` | Failed to set prior_asset.  
`DOES_NOT_EXIST` | Current asset is the first known state.  
`DELETED` | prior_asset is a deletion.  
  
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
`feed` |  `[Feed](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.Feed)` Required. The new values of feed details. It must match an existing feed and the field `name` must be in the format of: projects/project_number/feeds/feed_id or folders/folder_number/feeds/feed_id or organizations/organization_number/feeds/feed_id.  
`update_mask` |  `[FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` Required. Only updates the `feed` fields indicated by this mask. The field mask must not be empty, and it must not contain fields that are immutable or only set by the server.  
  
## UpdateSavedQueryRequest

Request to update a saved query.

Fields  
---  
`saved_query` |  `[SavedQuery](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.SavedQuery)` Required. The saved query to update.The saved query's `name` field is used to identify the one to update, which has format as below:

  * projects/project_number/savedQueries/saved_query_id
  * folders/folder_number/savedQueries/saved_query_id
  * organizations/organization_number/savedQueries/saved_query_id

  
`update_mask` |  `[FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` Required. The list of fields to update.  
  
## VersionedResource

Resource representation as defined by the corresponding service providing the resource for a given API version.

Fields  
---  
`version` |  `string` API version of the resource.Example: If the resource is an instance provided by Compute Engine v1 API as defined in `https://cloud.google.com/compute/docs/reference/rest/v1/instances`, version will be "v1".  
`resource` |  `[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` JSON representation of the resource as defined by the corresponding service providing this resource.Example: If the resource is an instance provided by Compute Engine, this field will contain the JSON representation of the instance as defined by Compute Engine: `https://cloud.google.com/compute/docs/reference/rest/v1/instances`.You can find the resource definition for each supported resource type in this table: `https://cloud.google.com/asset-inventory/docs/supported-asset-types`  
`asset_exceptions[]` |  `[AssetException](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.AssetException)` The exceptions of a resource.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-24 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-24 UTC."],[],[]] 
