---
url: https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2
title: Package google.privacy.dlp.v2 \u00a0|\u00a0 Sensitive Data Protection \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:55:37.037559+00:00
---

# Package google.privacy.dlp.v2  |  Sensitive Data Protection  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2

Cloud Data Loss Prevention (Cloud DLP) is now a part of Sensitive Data Protection. The API name remains the same: Cloud Data Loss Prevention API (DLP API). For information about the services that make up Sensitive Data Protection, see [Sensitive Data Protection overview](https://cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Sensitive Data Protection ](https://docs.cloud.google.com/sensitive-data-protection/docs)
  * [ Reference ](https://docs.cloud.google.com/sensitive-data-protection/docs/apis)



Send feedback 

#  Package google.privacy.dlp.v2 Stay organized with collections  Save and categorize content based on your preferences. 

## Index

  * `[DlpService](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DlpService)` (interface)
  * `[Action](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.Action)` (message)
  * `[Action.Deidentify](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.Action.Deidentify)` (message)
  * `[Action.JobNotificationEmails](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.Action.JobNotificationEmails)` (message)
  * `[Action.PublishFindingsToCloudDataCatalog](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.Action.PublishFindingsToCloudDataCatalog)` (message)
  * `[Action.PublishFindingsToDataplexCatalog](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.Action.PublishFindingsToDataplexCatalog)` (message)
  * `[Action.PublishSummaryToCscc](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.Action.PublishSummaryToCscc)` (message)
  * `[Action.PublishToPubSub](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.Action.PublishToPubSub)` (message)
  * `[Action.PublishToStackdriver](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.Action.PublishToStackdriver)` (message)
  * `[Action.SaveFindings](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.Action.SaveFindings)` (message)
  * `[ActionDetails](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ActionDetails)` (message)
  * `[ActivateJobTriggerRequest](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ActivateJobTriggerRequest)` (message)
  * `[AdjustByImageFindings](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.AdjustByImageFindings)` (message)
  * `[AdjustByMatchingInfoTypes](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.AdjustByMatchingInfoTypes)` (message)
  * `[AdjustmentRule](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.AdjustmentRule)` (message)
  * `[AllOtherDatabaseResources](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.AllOtherDatabaseResources)` (message)
  * `[AllOtherResources](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.AllOtherResources)` (message)
  * `[AmazonS3Bucket](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.AmazonS3Bucket)` (message)
  * `[AmazonS3BucketConditions](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.AmazonS3BucketConditions)` (message)
  * `[AmazonS3BucketConditions.BucketType](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.AmazonS3BucketConditions.BucketType)` (enum)
  * `[AmazonS3BucketConditions.ObjectStorageClass](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.AmazonS3BucketConditions.ObjectStorageClass)` (enum)
  * `[AmazonS3BucketRegex](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.AmazonS3BucketRegex)` (message)
  * `[AnalyzeDataSourceRiskDetails](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.AnalyzeDataSourceRiskDetails)` (message)
  * `[AnalyzeDataSourceRiskDetails.CategoricalStatsResult](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.AnalyzeDataSourceRiskDetails.CategoricalStatsResult)` (message)
  * `[AnalyzeDataSourceRiskDetails.CategoricalStatsResult.CategoricalStatsHistogramBucket](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.AnalyzeDataSourceRiskDetails.CategoricalStatsResult.CategoricalStatsHistogramBucket)` (message)
  * `[AnalyzeDataSourceRiskDetails.DeltaPresenceEstimationResult](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.AnalyzeDataSourceRiskDetails.DeltaPresenceEstimationResult)` (message)
  * `[AnalyzeDataSourceRiskDetails.DeltaPresenceEstimationResult.DeltaPresenceEstimationHistogramBucket](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.AnalyzeDataSourceRiskDetails.DeltaPresenceEstimationResult.DeltaPresenceEstimationHistogramBucket)` (message)
  * `[AnalyzeDataSourceRiskDetails.DeltaPresenceEstimationResult.DeltaPresenceEstimationQuasiIdValues](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.AnalyzeDataSourceRiskDetails.DeltaPresenceEstimationResult.DeltaPresenceEstimationQuasiIdValues)` (message)
  * `[AnalyzeDataSourceRiskDetails.KAnonymityResult](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.AnalyzeDataSourceRiskDetails.KAnonymityResult)` (message)
  * `[AnalyzeDataSourceRiskDetails.KAnonymityResult.KAnonymityEquivalenceClass](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.AnalyzeDataSourceRiskDetails.KAnonymityResult.KAnonymityEquivalenceClass)` (message)
  * `[AnalyzeDataSourceRiskDetails.KAnonymityResult.KAnonymityHistogramBucket](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.AnalyzeDataSourceRiskDetails.KAnonymityResult.KAnonymityHistogramBucket)` (message)
  * `[AnalyzeDataSourceRiskDetails.KMapEstimationResult](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.AnalyzeDataSourceRiskDetails.KMapEstimationResult)` (message)
  * `[AnalyzeDataSourceRiskDetails.KMapEstimationResult.KMapEstimationHistogramBucket](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.AnalyzeDataSourceRiskDetails.KMapEstimationResult.KMapEstimationHistogramBucket)` (message)
  * `[AnalyzeDataSourceRiskDetails.KMapEstimationResult.KMapEstimationQuasiIdValues](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.AnalyzeDataSourceRiskDetails.KMapEstimationResult.KMapEstimationQuasiIdValues)` (message)
  * `[AnalyzeDataSourceRiskDetails.LDiversityResult](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.AnalyzeDataSourceRiskDetails.LDiversityResult)` (message)
  * `[AnalyzeDataSourceRiskDetails.LDiversityResult.LDiversityEquivalenceClass](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.AnalyzeDataSourceRiskDetails.LDiversityResult.LDiversityEquivalenceClass)` (message)
  * `[AnalyzeDataSourceRiskDetails.LDiversityResult.LDiversityHistogramBucket](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.AnalyzeDataSourceRiskDetails.LDiversityResult.LDiversityHistogramBucket)` (message)
  * `[AnalyzeDataSourceRiskDetails.NumericalStatsResult](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.AnalyzeDataSourceRiskDetails.NumericalStatsResult)` (message)
  * `[AnalyzeDataSourceRiskDetails.RequestedRiskAnalysisOptions](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.AnalyzeDataSourceRiskDetails.RequestedRiskAnalysisOptions)` (message)
  * `[AwsAccount](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.AwsAccount)` (message)
  * `[AwsAccountRegex](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.AwsAccountRegex)` (message)
  * `[BatchContentItem](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.BatchContentItem)` (message)
  * `[BatchContentLocation](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.BatchContentLocation)` (message)
  * `[BigQueryDiscoveryTarget](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.BigQueryDiscoveryTarget)` (message)
  * `[BigQueryField](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.BigQueryField)` (message)
  * `[BigQueryKey](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.BigQueryKey)` (message)
  * `[BigQueryOptions](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.BigQueryOptions)` (message)
  * `[BigQueryOptions.SampleMethod](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.BigQueryOptions.SampleMethod)` (enum)
  * `[BigQueryRegex](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.BigQueryRegex)` (message)
  * `[BigQueryRegexes](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.BigQueryRegexes)` (message)
  * `[BigQuerySchemaModification](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.BigQuerySchemaModification)` (enum)
  * `[BigQueryTable](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.BigQueryTable)` (message)
  * `[BigQueryTableCollection](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.BigQueryTableCollection)` (message)
  * `[BigQueryTableModification](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.BigQueryTableModification)` (enum)
  * `[BigQueryTableType](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.BigQueryTableType)` (enum)
  * `[BigQueryTableTypeCollection](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.BigQueryTableTypeCollection)` (enum)
  * `[BigQueryTableTypes](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.BigQueryTableTypes)` (message)
  * `[BoundingBox](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.BoundingBox)` (message)
  * `[BucketingConfig](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.BucketingConfig)` (message)
  * `[BucketingConfig.Bucket](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.BucketingConfig.Bucket)` (message)
  * `[ByteContentItem](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ByteContentItem)` (message)
  * `[ByteContentItem.BytesType](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ByteContentItem.BytesType)` (enum)
  * `[CancelDlpJobRequest](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.CancelDlpJobRequest)` (message)
  * `[CharacterMaskConfig](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.CharacterMaskConfig)` (message)
  * `[CharsToIgnore](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.CharsToIgnore)` (message)
  * `[CharsToIgnore.CommonCharsToIgnore](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.CharsToIgnore.CommonCharsToIgnore)` (enum)
  * `[CloudSqlDiscoveryTarget](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.CloudSqlDiscoveryTarget)` (message)
  * `[CloudSqlIamCredential](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.CloudSqlIamCredential)` (message)
  * `[CloudSqlProperties](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.CloudSqlProperties)` (message)
  * `[CloudSqlProperties.DatabaseEngine](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.CloudSqlProperties.DatabaseEngine)` (enum)
  * `[CloudStorageDiscoveryTarget](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.CloudStorageDiscoveryTarget)` (message)
  * `[CloudStorageFileSet](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.CloudStorageFileSet)` (message)
  * `[CloudStorageOptions](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.CloudStorageOptions)` (message)
  * `[CloudStorageOptions.FileSet](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.CloudStorageOptions.FileSet)` (message)
  * `[CloudStorageOptions.SampleMethod](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.CloudStorageOptions.SampleMethod)` (enum)
  * `[CloudStoragePath](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.CloudStoragePath)` (message)
  * `[CloudStorageRegex](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.CloudStorageRegex)` (message)
  * `[CloudStorageRegexFileSet](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.CloudStorageRegexFileSet)` (message)
  * `[CloudStorageResourceReference](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.CloudStorageResourceReference)` (message)
  * `[Color](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.Color)` (message)
  * `[ColumnDataProfile](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ColumnDataProfile)` (message)
  * `[ColumnDataProfile.ColumnDataType](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ColumnDataProfile.ColumnDataType)` (enum)
  * `[ColumnDataProfile.ColumnPolicyState](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ColumnDataProfile.ColumnPolicyState)` (enum)
  * `[ColumnDataProfile.State](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ColumnDataProfile.State)` (enum)
  * `[Connection](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.Connection)` (message)
  * `[ConnectionState](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ConnectionState)` (enum)
  * `[Container](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.Container)` (message)
  * `[ContentItem](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ContentItem)` (message)
  * `[ContentLocation](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ContentLocation)` (message)
  * `[ContentMetadata](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ContentMetadata)` (message)
  * `[ContentOption](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ContentOption)` (enum)
  * `[ContentPolicy](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ContentPolicy)` (message)
  * `[ContentPolicy.LoggingConfig](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ContentPolicy.LoggingConfig)` (message)
  * `[ContentPolicy.LoggingConfig.LogToBigQuery](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ContentPolicy.LoggingConfig.LogToBigQuery)` (message)
  * `[ContentPolicy.PolicyAction](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ContentPolicy.PolicyAction)` (message)
  * `[ContentPolicy.PolicyRule](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ContentPolicy.PolicyRule)` (message)
  * `[ContentPolicy.PolicyRule.PolicyCondition](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ContentPolicy.PolicyRule.PolicyCondition)` (message)
  * `[ContentPolicy.PolicyRule.PolicyCondition.InfoTypeCondition](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ContentPolicy.PolicyRule.PolicyCondition.InfoTypeCondition)` (message)
  * `[ContentPolicy.PolicyRule.PolicyCondition.InfoTypeCondition.InfoTypes](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ContentPolicy.PolicyRule.PolicyCondition.InfoTypeCondition.InfoTypes)` (message)
  * `[ContentPolicyActionLog](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ContentPolicyActionLog)` (message)
  * `[ContentPolicyActionLog.FallbackActionType](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ContentPolicyActionLog.FallbackActionType)` (enum)
  * `[ContentPolicyActionLog.InfoTypeMatch](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ContentPolicyActionLog.InfoTypeMatch)` (message)
  * `[ContentPolicyActionLog.ScannedContent](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ContentPolicyActionLog.ScannedContent)` (message)
  * `[ContentPolicyVerdict](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ContentPolicyVerdict)` (enum)
  * `[Conversation](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.Conversation)` (message)
  * `[ConversationLocation](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ConversationLocation)` (message)
  * `[ConversationLocation.AllMessages](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ConversationLocation.AllMessages)` (message)
  * `[ConversationMessage](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ConversationMessage)` (message)
  * `[ConversationMessage.MessagePart](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ConversationMessage.MessagePart)` (message)
  * `[ConversationMessage.MessageType](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ConversationMessage.MessageType)` (enum)
  * `[CreateConnectionRequest](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.CreateConnectionRequest)` (message)
  * `[CreateContentPolicyRequest](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.CreateContentPolicyRequest)` (message)
  * `[CreateDeidentifyTemplateRequest](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.CreateDeidentifyTemplateRequest)` (message)
  * `[CreateDiscoveryConfigRequest](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.CreateDiscoveryConfigRequest)` (message)
  * `[CreateDlpJobRequest](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.CreateDlpJobRequest)` (message)
  * `[CreateInspectTemplateRequest](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.CreateInspectTemplateRequest)` (message)
  * `[CreateJobTriggerRequest](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.CreateJobTriggerRequest)` (message)
  * `[CreateStoredInfoTypeRequest](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.CreateStoredInfoTypeRequest)` (message)
  * `[CryptoDeterministicConfig](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.CryptoDeterministicConfig)` (message)
  * `[CryptoHashConfig](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.CryptoHashConfig)` (message)
  * `[CryptoKey](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.CryptoKey)` (message)
  * `[CryptoReplaceFfxFpeConfig](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.CryptoReplaceFfxFpeConfig)` (message)
  * `[CryptoReplaceFfxFpeConfig.FfxCommonNativeAlphabet](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.CryptoReplaceFfxFpeConfig.FfxCommonNativeAlphabet)` (enum)
  * `[CustomInfoType](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.CustomInfoType)` (message)
  * `[CustomInfoType.DetectionRule](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.CustomInfoType.DetectionRule)` (message)
  * `[CustomInfoType.DetectionRule.HotwordRule](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.CustomInfoType.DetectionRule.HotwordRule)` (message)
  * `[CustomInfoType.DetectionRule.LikelihoodAdjustment](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.CustomInfoType.DetectionRule.LikelihoodAdjustment)` (message)
  * `[CustomInfoType.DetectionRule.Proximity](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.CustomInfoType.DetectionRule.Proximity)` (message)
  * `[CustomInfoType.Dictionary](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.CustomInfoType.Dictionary)` (message)
  * `[CustomInfoType.Dictionary.WordList](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.CustomInfoType.Dictionary.WordList)` (message)
  * `[CustomInfoType.ExclusionType](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.CustomInfoType.ExclusionType)` (enum)
  * `[CustomInfoType.FileLabelInfoType](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.CustomInfoType.FileLabelInfoType)` (message)
  * `[CustomInfoType.FileLabelInfoType.GoogleDriveLabel](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.CustomInfoType.FileLabelInfoType.GoogleDriveLabel)` (message)
  * `[CustomInfoType.FileLabelInfoType.GoogleDriveLabel.LabelField](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.CustomInfoType.FileLabelInfoType.GoogleDriveLabel.LabelField)` (message)
  * `[CustomInfoType.FileLabelInfoType.SensitivityLabel](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.CustomInfoType.FileLabelInfoType.SensitivityLabel)` (message)
  * `[CustomInfoType.MetadataKeyValueExpression](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.CustomInfoType.MetadataKeyValueExpression)` (message)
  * `[CustomInfoType.Regex](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.CustomInfoType.Regex)` (message)
  * `[CustomInfoType.SurrogateType](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.CustomInfoType.SurrogateType)` (message)
  * `[DataProfileAction](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DataProfileAction)` (message)
  * `[DataProfileAction.EventType](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DataProfileAction.EventType)` (enum)
  * `[DataProfileAction.Export](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DataProfileAction.Export)` (message)
  * `[DataProfileAction.PubSubNotification](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DataProfileAction.PubSubNotification)` (message)
  * `[DataProfileAction.PubSubNotification.DetailLevel](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DataProfileAction.PubSubNotification.DetailLevel)` (enum)
  * `[DataProfileAction.PublishToChronicle](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DataProfileAction.PublishToChronicle)` (message)
  * `[DataProfileAction.PublishToDataplexCatalog](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DataProfileAction.PublishToDataplexCatalog)` (message)
  * `[DataProfileAction.PublishToSecurityCommandCenter](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DataProfileAction.PublishToSecurityCommandCenter)` (message)
  * `[DataProfileAction.TagResources](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DataProfileAction.TagResources)` (message)
  * `[DataProfileAction.TagResources.TagCondition](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DataProfileAction.TagResources.TagCondition)` (message)
  * `[DataProfileAction.TagResources.TagValue](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DataProfileAction.TagResources.TagValue)` (message)
  * `[DataProfileBigQueryRowSchema](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DataProfileBigQueryRowSchema)` (message)
  * `[DataProfileConfigSnapshot](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DataProfileConfigSnapshot)` (message)
  * `[DataProfileFinding](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DataProfileFinding)` (message)
  * `[DataProfileFindingLocation](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DataProfileFindingLocation)` (message)
  * `[DataProfileFindingRecordLocation](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DataProfileFindingRecordLocation)` (message)
  * `[DataProfileJobConfig](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DataProfileJobConfig)` (message)
  * `[DataProfileLocation](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DataProfileLocation)` (message)
  * `[DataProfilePubSubCondition](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DataProfilePubSubCondition)` (message)
  * `[DataProfilePubSubCondition.ProfileScoreBucket](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DataProfilePubSubCondition.ProfileScoreBucket)` (enum)
  * `[DataProfilePubSubCondition.PubSubCondition](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DataProfilePubSubCondition.PubSubCondition)` (message)
  * `[DataProfilePubSubCondition.PubSubExpressions](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DataProfilePubSubCondition.PubSubExpressions)` (message)
  * `[DataProfilePubSubCondition.PubSubExpressions.PubSubLogicalOperator](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DataProfilePubSubCondition.PubSubExpressions.PubSubLogicalOperator)` (enum)
  * `[DataProfilePubSubMessage](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DataProfilePubSubMessage)` (message)
  * `[DataProfileUpdateFrequency](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DataProfileUpdateFrequency)` (enum)
  * `[DataRiskLevel](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DataRiskLevel)` (message)
  * `[DataRiskLevel.DataRiskLevelScore](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DataRiskLevel.DataRiskLevelScore)` (enum)
  * `[DataSourceType](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DataSourceType)` (message)
  * `[DatabaseResourceCollection](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DatabaseResourceCollection)` (message)
  * `[DatabaseResourceReference](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DatabaseResourceReference)` (message)
  * `[DatabaseResourceRegex](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DatabaseResourceRegex)` (message)
  * `[DatabaseResourceRegexes](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DatabaseResourceRegexes)` (message)
  * `[DatastoreKey](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DatastoreKey)` (message)
  * `[DatastoreOptions](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DatastoreOptions)` (message)
  * `[DateShiftConfig](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DateShiftConfig)` (message)
  * `[DateTime](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DateTime)` (message)
  * `[DateTime.TimeZone](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DateTime.TimeZone)` (message)
  * `[DeidentifyConfig](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DeidentifyConfig)` (message)
  * `[DeidentifyContentRequest](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DeidentifyContentRequest)` (message)
  * `[DeidentifyContentResponse](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DeidentifyContentResponse)` (message)
  * `[DeidentifyDataSourceDetails](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DeidentifyDataSourceDetails)` (message)
  * `[DeidentifyDataSourceDetails.RequestedDeidentifyOptions](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DeidentifyDataSourceDetails.RequestedDeidentifyOptions)` (message)
  * `[DeidentifyDataSourceStats](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DeidentifyDataSourceStats)` (message)
  * `[DeidentifyTemplate](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DeidentifyTemplate)` (message)
  * `[DeleteConnectionRequest](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DeleteConnectionRequest)` (message)
  * `[DeleteContentPolicyRequest](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DeleteContentPolicyRequest)` (message)
  * `[DeleteDeidentifyTemplateRequest](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DeleteDeidentifyTemplateRequest)` (message)
  * `[DeleteDiscoveryConfigRequest](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DeleteDiscoveryConfigRequest)` (message)
  * `[DeleteDlpJobRequest](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DeleteDlpJobRequest)` (message)
  * `[DeleteFileStoreDataProfileRequest](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DeleteFileStoreDataProfileRequest)` (message)
  * `[DeleteInspectTemplateRequest](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DeleteInspectTemplateRequest)` (message)
  * `[DeleteJobTriggerRequest](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DeleteJobTriggerRequest)` (message)
  * `[DeleteStoredInfoTypeRequest](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DeleteStoredInfoTypeRequest)` (message)
  * `[DeleteTableDataProfileRequest](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DeleteTableDataProfileRequest)` (message)
  * `[Disabled](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.Disabled)` (message)
  * `[DiscoveryBigQueryConditions](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DiscoveryBigQueryConditions)` (message)
  * `[DiscoveryBigQueryConditions.OrConditions](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DiscoveryBigQueryConditions.OrConditions)` (message)
  * `[DiscoveryBigQueryFilter](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DiscoveryBigQueryFilter)` (message)
  * `[DiscoveryBigQueryFilter.AllOtherBigQueryTables](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DiscoveryBigQueryFilter.AllOtherBigQueryTables)` (message)
  * `[DiscoveryCloudSqlConditions](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DiscoveryCloudSqlConditions)` (message)
  * `[DiscoveryCloudSqlConditions.DatabaseEngine](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DiscoveryCloudSqlConditions.DatabaseEngine)` (enum)
  * `[DiscoveryCloudSqlConditions.DatabaseResourceType](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DiscoveryCloudSqlConditions.DatabaseResourceType)` (enum)
  * `[DiscoveryCloudSqlFilter](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DiscoveryCloudSqlFilter)` (message)
  * `[DiscoveryCloudSqlGenerationCadence](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DiscoveryCloudSqlGenerationCadence)` (message)
  * `[DiscoveryCloudSqlGenerationCadence.SchemaModifiedCadence](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DiscoveryCloudSqlGenerationCadence.SchemaModifiedCadence)` (message)
  * `[DiscoveryCloudSqlGenerationCadence.SchemaModifiedCadence.CloudSqlSchemaModification](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DiscoveryCloudSqlGenerationCadence.SchemaModifiedCadence.CloudSqlSchemaModification)` (enum)
  * `[DiscoveryCloudStorageConditions](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DiscoveryCloudStorageConditions)` (message)
  * `[DiscoveryCloudStorageConditions.CloudStorageBucketAttribute](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DiscoveryCloudStorageConditions.CloudStorageBucketAttribute)` (enum)
  * `[DiscoveryCloudStorageConditions.CloudStorageObjectAttribute](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DiscoveryCloudStorageConditions.CloudStorageObjectAttribute)` (enum)
  * `[DiscoveryCloudStorageFilter](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DiscoveryCloudStorageFilter)` (message)
  * `[DiscoveryCloudStorageGenerationCadence](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DiscoveryCloudStorageGenerationCadence)` (message)
  * `[DiscoveryConfig](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DiscoveryConfig)` (message)
  * `[DiscoveryConfig.OrgConfig](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DiscoveryConfig.OrgConfig)` (message)
  * `[DiscoveryConfig.Status](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DiscoveryConfig.Status)` (enum)
  * `[DiscoveryFileStoreConditions](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DiscoveryFileStoreConditions)` (message)
  * `[DiscoveryGenerationCadence](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DiscoveryGenerationCadence)` (message)
  * `[DiscoveryInspectTemplateModifiedCadence](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DiscoveryInspectTemplateModifiedCadence)` (message)
  * `[DiscoveryOtherCloudConditions](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DiscoveryOtherCloudConditions)` (message)
  * `[DiscoveryOtherCloudFilter](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DiscoveryOtherCloudFilter)` (message)
  * `[DiscoveryOtherCloudGenerationCadence](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DiscoveryOtherCloudGenerationCadence)` (message)
  * `[DiscoverySchemaModifiedCadence](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DiscoverySchemaModifiedCadence)` (message)
  * `[DiscoveryStartingLocation](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DiscoveryStartingLocation)` (message)
  * `[DiscoveryTableModifiedCadence](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DiscoveryTableModifiedCadence)` (message)
  * `[DiscoveryTarget](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DiscoveryTarget)` (message)
  * `[DiscoveryVertexDatasetConditions](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DiscoveryVertexDatasetConditions)` (message)
  * `[DiscoveryVertexDatasetFilter](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DiscoveryVertexDatasetFilter)` (message)
  * `[DiscoveryVertexDatasetGenerationCadence](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DiscoveryVertexDatasetGenerationCadence)` (message)
  * `[DlpJob](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DlpJob)` (message)
  * `[DlpJob.JobState](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DlpJob.JobState)` (enum)
  * `[DlpJobType](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DlpJobType)` (enum)
  * `[DocumentLocation](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DocumentLocation)` (message)
  * `[Domain](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.Domain)` (message)
  * `[Domain.Category](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.Domain.Category)` (enum)
  * `[Domain.Signal](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.Domain.Signal)` (enum)
  * `[Encloses](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.Encloses)` (message)
  * `[EncryptionStatus](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.EncryptionStatus)` (enum)
  * `[EntityId](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.EntityId)` (message)
  * `[Error](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.Error)` (message)
  * `[Error.ErrorExtraInfo](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.Error.ErrorExtraInfo)` (enum)
  * `[ExcludeByHotword](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ExcludeByHotword)` (message)
  * `[ExcludeByImageFindings](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ExcludeByImageFindings)` (message)
  * `[ExcludeInfoTypes](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ExcludeInfoTypes)` (message)
  * `[ExclusionRule](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ExclusionRule)` (message)
  * `[FieldId](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.FieldId)` (message)
  * `[FieldTransformation](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.FieldTransformation)` (message)
  * `[FileClusterSummary](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.FileClusterSummary)` (message)
  * `[FileClusterType](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.FileClusterType)` (message)
  * `[FileClusterType.Cluster](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.FileClusterType.Cluster)` (enum)
  * `[FileExtensionInfo](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.FileExtensionInfo)` (message)
  * `[FileLabel](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.FileLabel)` (message)
  * `[FileLabel.GoogleDriveLabelMetadata](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.FileLabel.GoogleDriveLabelMetadata)` (message)
  * `[FileLabel.GoogleDriveLabelMetadata.LabelFieldMetadata](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.FileLabel.GoogleDriveLabelMetadata.LabelFieldMetadata)` (message)
  * `[FileLabel.SensitivityLabelMetadata](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.FileLabel.SensitivityLabelMetadata)` (message)
  * `[FileStoreCollection](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.FileStoreCollection)` (message)
  * `[FileStoreDataProfile](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.FileStoreDataProfile)` (message)
  * `[FileStoreDataProfile.State](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.FileStoreDataProfile.State)` (enum)
  * `[FileStoreInfoTypeSummary](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.FileStoreInfoTypeSummary)` (message)
  * `[FileStoreRegex](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.FileStoreRegex)` (message)
  * `[FileStoreRegexes](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.FileStoreRegexes)` (message)
  * `[FileType](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.FileType)` (enum)
  * `[Finding](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.Finding)` (message)
  * `[FinishDlpJobRequest](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.FinishDlpJobRequest)` (message)
  * `[FixedSizeBucketingConfig](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.FixedSizeBucketingConfig)` (message)
  * `[FullyInside](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.FullyInside)` (message)
  * `[GetColumnDataProfileRequest](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.GetColumnDataProfileRequest)` (message)
  * `[GetConnectionRequest](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.GetConnectionRequest)` (message)
  * `[GetContentPolicyRequest](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.GetContentPolicyRequest)` (message)
  * `[GetDeidentifyTemplateRequest](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.GetDeidentifyTemplateRequest)` (message)
  * `[GetDiscoveryConfigRequest](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.GetDiscoveryConfigRequest)` (message)
  * `[GetDlpJobRequest](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.GetDlpJobRequest)` (message)
  * `[GetFileStoreDataProfileRequest](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.GetFileStoreDataProfileRequest)` (message)
  * `[GetInspectTemplateRequest](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.GetInspectTemplateRequest)` (message)
  * `[GetJobTriggerRequest](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.GetJobTriggerRequest)` (message)
  * `[GetProjectDataProfileRequest](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.GetProjectDataProfileRequest)` (message)
  * `[GetStoredInfoTypeRequest](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.GetStoredInfoTypeRequest)` (message)
  * `[GetTableDataProfileRequest](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.GetTableDataProfileRequest)` (message)
  * `[HybridContentItem](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.HybridContentItem)` (message)
  * `[HybridFindingDetails](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.HybridFindingDetails)` (message)
  * `[HybridInspectDlpJobRequest](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.HybridInspectDlpJobRequest)` (message)
  * `[HybridInspectJobTriggerRequest](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.HybridInspectJobTriggerRequest)` (message)
  * `[HybridInspectResponse](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.HybridInspectResponse)` (message)
  * `[HybridInspectStatistics](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.HybridInspectStatistics)` (message)
  * `[HybridOptions](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.HybridOptions)` (message)
  * `[ImageContainmentType](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ImageContainmentType)` (message)
  * `[ImageLocation](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ImageLocation)` (message)
  * `[ImageTransformations](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ImageTransformations)` (message)
  * `[ImageTransformations.ImageTransformation](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ImageTransformations.ImageTransformation)` (message)
  * `[ImageTransformations.ImageTransformation.AllInfoTypes](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ImageTransformations.ImageTransformation.AllInfoTypes)` (message)
  * `[ImageTransformations.ImageTransformation.AllText](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ImageTransformations.ImageTransformation.AllText)` (message)
  * `[ImageTransformations.ImageTransformation.SelectedInfoTypes](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ImageTransformations.ImageTransformation.SelectedInfoTypes)` (message)
  * `[InfoType](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.InfoType)` (message)
  * `[InfoTypeCategory](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.InfoTypeCategory)` (message)
  * `[InfoTypeCategory.IndustryCategory](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.InfoTypeCategory.IndustryCategory)` (enum)
  * `[InfoTypeCategory.LocationCategory](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.InfoTypeCategory.LocationCategory)` (enum)
  * `[InfoTypeCategory.TypeCategory](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.InfoTypeCategory.TypeCategory)` (enum)
  * `[InfoTypeDescription](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.InfoTypeDescription)` (message)
  * `[InfoTypeDescription.InfoTypeLaunchStatus](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.InfoTypeDescription.InfoTypeLaunchStatus)` (enum)
  * `[InfoTypeStats](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.InfoTypeStats)` (message)
  * `[InfoTypeSummary](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.InfoTypeSummary)` (message)
  * `[InfoTypeSupportedBy](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.InfoTypeSupportedBy)` (enum)
  * `[InfoTypeTransformations](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.InfoTypeTransformations)` (message)
  * `[InfoTypeTransformations.InfoTypeTransformation](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.InfoTypeTransformations.InfoTypeTransformation)` (message)
  * `[InspectConfig](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.InspectConfig)` (message)
  * `[InspectConfig.FindingLimits](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.InspectConfig.FindingLimits)` (message)
  * `[InspectConfig.FindingLimits.InfoTypeLimit](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.InspectConfig.FindingLimits.InfoTypeLimit)` (message)
  * `[InspectConfig.InfoTypeLikelihood](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.InspectConfig.InfoTypeLikelihood)` (message)
  * `[InspectContentRequest](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.InspectContentRequest)` (message)
  * `[InspectContentResponse](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.InspectContentResponse)` (message)
  * `[InspectDataSourceDetails](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.InspectDataSourceDetails)` (message)
  * `[InspectDataSourceDetails.RequestedOptions](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.InspectDataSourceDetails.RequestedOptions)` (message)
  * `[InspectDataSourceDetails.Result](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.InspectDataSourceDetails.Result)` (message)
  * `[InspectJobConfig](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.InspectJobConfig)` (message)
  * `[InspectResult](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.InspectResult)` (message)
  * `[InspectTemplate](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.InspectTemplate)` (message)
  * `[InspectionRule](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.InspectionRule)` (message)
  * `[InspectionRuleSet](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.InspectionRuleSet)` (message)
  * `[JobTrigger](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.JobTrigger)` (message)
  * `[JobTrigger.Status](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.JobTrigger.Status)` (enum)
  * `[JobTrigger.Trigger](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.JobTrigger.Trigger)` (message)
  * `[Key](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.Key)` (message)
  * `[Key.PathElement](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.Key.PathElement)` (message)
  * `[KeyValueMetadataLabel](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.KeyValueMetadataLabel)` (message)
  * `[KeyValueMetadataProperty](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.KeyValueMetadataProperty)` (message)
  * `[KindExpression](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.KindExpression)` (message)
  * `[KmsWrappedCryptoKey](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.KmsWrappedCryptoKey)` (message)
  * `[LargeCustomDictionaryConfig](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.LargeCustomDictionaryConfig)` (message)
  * `[LargeCustomDictionaryStats](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.LargeCustomDictionaryStats)` (message)
  * `[Likelihood](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.Likelihood)` (enum)
  * `[ListColumnDataProfilesRequest](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ListColumnDataProfilesRequest)` (message)
  * `[ListColumnDataProfilesResponse](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ListColumnDataProfilesResponse)` (message)
  * `[ListConnectionsRequest](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ListConnectionsRequest)` (message)
  * `[ListConnectionsResponse](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ListConnectionsResponse)` (message)
  * `[ListContentPoliciesRequest](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ListContentPoliciesRequest)` (message)
  * `[ListContentPoliciesResponse](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ListContentPoliciesResponse)` (message)
  * `[ListDeidentifyTemplatesRequest](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ListDeidentifyTemplatesRequest)` (message)
  * `[ListDeidentifyTemplatesResponse](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ListDeidentifyTemplatesResponse)` (message)
  * `[ListDiscoveryConfigsRequest](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ListDiscoveryConfigsRequest)` (message)
  * `[ListDiscoveryConfigsResponse](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ListDiscoveryConfigsResponse)` (message)
  * `[ListDlpJobsRequest](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ListDlpJobsRequest)` (message)
  * `[ListDlpJobsResponse](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ListDlpJobsResponse)` (message)
  * `[ListFileStoreDataProfilesRequest](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ListFileStoreDataProfilesRequest)` (message)
  * `[ListFileStoreDataProfilesResponse](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ListFileStoreDataProfilesResponse)` (message)
  * `[ListInfoTypesRequest](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ListInfoTypesRequest)` (message)
  * `[ListInfoTypesResponse](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ListInfoTypesResponse)` (message)
  * `[ListInspectTemplatesRequest](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ListInspectTemplatesRequest)` (message)
  * `[ListInspectTemplatesResponse](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ListInspectTemplatesResponse)` (message)
  * `[ListJobTriggersRequest](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ListJobTriggersRequest)` (message)
  * `[ListJobTriggersResponse](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ListJobTriggersResponse)` (message)
  * `[ListProjectDataProfilesRequest](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ListProjectDataProfilesRequest)` (message)
  * `[ListProjectDataProfilesResponse](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ListProjectDataProfilesResponse)` (message)
  * `[ListStoredInfoTypesRequest](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ListStoredInfoTypesRequest)` (message)
  * `[ListStoredInfoTypesResponse](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ListStoredInfoTypesResponse)` (message)
  * `[ListTableDataProfilesRequest](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ListTableDataProfilesRequest)` (message)
  * `[ListTableDataProfilesResponse](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ListTableDataProfilesResponse)` (message)
  * `[Location](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.Location)` (message)
  * `[LocationSupport](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.LocationSupport)` (message)
  * `[LocationSupport.RegionalizationScope](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.LocationSupport.RegionalizationScope)` (enum)
  * `[Manual](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.Manual)` (message)
  * `[MatchingType](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.MatchingType)` (enum)
  * `[MetadataLocation](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.MetadataLocation)` (message)
  * `[MetadataType](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.MetadataType)` (enum)
  * `[NullPercentageLevel](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.NullPercentageLevel)` (enum)
  * `[OtherCloudDiscoveryStartingLocation](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.OtherCloudDiscoveryStartingLocation)` (message)
  * `[OtherCloudDiscoveryStartingLocation.AwsDiscoveryStartingLocation](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.OtherCloudDiscoveryStartingLocation.AwsDiscoveryStartingLocation)` (message)
  * `[OtherCloudDiscoveryTarget](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.OtherCloudDiscoveryTarget)` (message)
  * `[OtherCloudResourceCollection](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.OtherCloudResourceCollection)` (message)
  * `[OtherCloudResourceRegex](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.OtherCloudResourceRegex)` (message)
  * `[OtherCloudResourceRegexes](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.OtherCloudResourceRegexes)` (message)
  * `[OtherCloudSingleResourceReference](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.OtherCloudSingleResourceReference)` (message)
  * `[OtherInfoTypeSummary](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.OtherInfoTypeSummary)` (message)
  * `[OutputStorageConfig](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.OutputStorageConfig)` (message)
  * `[OutputStorageConfig.OutputSchema](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.OutputStorageConfig.OutputSchema)` (enum)
  * `[Overlap](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.Overlap)` (message)
  * `[PartitionId](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.PartitionId)` (message)
  * `[PrimitiveTransformation](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.PrimitiveTransformation)` (message)
  * `[PrivacyMetric](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.PrivacyMetric)` (message)
  * `[PrivacyMetric.CategoricalStatsConfig](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.PrivacyMetric.CategoricalStatsConfig)` (message)
  * `[PrivacyMetric.DeltaPresenceEstimationConfig](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.PrivacyMetric.DeltaPresenceEstimationConfig)` (message)
  * `[PrivacyMetric.KAnonymityConfig](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.PrivacyMetric.KAnonymityConfig)` (message)
  * `[PrivacyMetric.KMapEstimationConfig](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.PrivacyMetric.KMapEstimationConfig)` (message)
  * `[PrivacyMetric.KMapEstimationConfig.AuxiliaryTable](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.PrivacyMetric.KMapEstimationConfig.AuxiliaryTable)` (message)
  * `[PrivacyMetric.KMapEstimationConfig.AuxiliaryTable.QuasiIdField](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.PrivacyMetric.KMapEstimationConfig.AuxiliaryTable.QuasiIdField)` (message)
  * `[PrivacyMetric.KMapEstimationConfig.TaggedField](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.PrivacyMetric.KMapEstimationConfig.TaggedField)` (message)
  * `[PrivacyMetric.LDiversityConfig](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.PrivacyMetric.LDiversityConfig)` (message)
  * `[PrivacyMetric.NumericalStatsConfig](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.PrivacyMetric.NumericalStatsConfig)` (message)
  * `[ProcessingLocation](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ProcessingLocation)` (message)
  * `[ProcessingLocation.DocumentFallbackLocation](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ProcessingLocation.DocumentFallbackLocation)` (message)
  * `[ProcessingLocation.GlobalProcessing](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ProcessingLocation.GlobalProcessing)` (message)
  * `[ProcessingLocation.ImageFallbackLocation](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ProcessingLocation.ImageFallbackLocation)` (message)
  * `[ProcessingLocation.MultiRegionProcessing](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ProcessingLocation.MultiRegionProcessing)` (message)
  * `[ProfileGeneration](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ProfileGeneration)` (enum)
  * `[ProfileStatus](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ProfileStatus)` (message)
  * `[ProjectDataProfile](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ProjectDataProfile)` (message)
  * `[QuasiId](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.QuasiId)` (message)
  * `[QuoteInfo](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.QuoteInfo)` (message)
  * `[Range](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.Range)` (message)
  * `[RecordCondition](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.RecordCondition)` (message)
  * `[RecordCondition.Condition](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.RecordCondition.Condition)` (message)
  * `[RecordCondition.Conditions](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.RecordCondition.Conditions)` (message)
  * `[RecordCondition.Expressions](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.RecordCondition.Expressions)` (message)
  * `[RecordCondition.Expressions.LogicalOperator](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.RecordCondition.Expressions.LogicalOperator)` (enum)
  * `[RecordKey](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.RecordKey)` (message)
  * `[RecordLocation](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.RecordLocation)` (message)
  * `[RecordSuppression](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.RecordSuppression)` (message)
  * `[RecordTransformation](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.RecordTransformation)` (message)
  * `[RecordTransformations](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.RecordTransformations)` (message)
  * `[RedactConfig](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.RedactConfig)` (message)
  * `[RedactImageRequest](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.RedactImageRequest)` (message)
  * `[RedactImageRequest.ImageRedactionConfig](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.RedactImageRequest.ImageRedactionConfig)` (message)
  * `[RedactImageResponse](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.RedactImageResponse)` (message)
  * `[ReidentifyContentRequest](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ReidentifyContentRequest)` (message)
  * `[ReidentifyContentResponse](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ReidentifyContentResponse)` (message)
  * `[RelatedResource](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.RelatedResource)` (message)
  * `[RelationalOperator](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.RelationalOperator)` (enum)
  * `[ReplaceDictionaryConfig](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ReplaceDictionaryConfig)` (message)
  * `[ReplaceValueConfig](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ReplaceValueConfig)` (message)
  * `[ReplaceWithInfoTypeConfig](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ReplaceWithInfoTypeConfig)` (message)
  * `[ResourceVisibility](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ResourceVisibility)` (enum)
  * `[RiskAnalysisJobConfig](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.RiskAnalysisJobConfig)` (message)
  * `[SaveToGcsFindingsOutput](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.SaveToGcsFindingsOutput)` (message)
  * `[Schedule](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.Schedule)` (message)
  * `[SearchConnectionsRequest](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.SearchConnectionsRequest)` (message)
  * `[SearchConnectionsResponse](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.SearchConnectionsResponse)` (message)
  * `[SecretManagerCredential](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.SecretManagerCredential)` (message)
  * `[SecretsDiscoveryTarget](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.SecretsDiscoveryTarget)` (message)
  * `[SensitivityScore](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.SensitivityScore)` (message)
  * `[SensitivityScore.SensitivityScoreLevel](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.SensitivityScore.SensitivityScoreLevel)` (enum)
  * `[StatisticalTable](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.StatisticalTable)` (message)
  * `[StatisticalTable.QuasiIdentifierField](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.StatisticalTable.QuasiIdentifierField)` (message)
  * `[StorageConfig](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.StorageConfig)` (message)
  * `[StorageConfig.TimespanConfig](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.StorageConfig.TimespanConfig)` (message)
  * `[StorageMetadataLabel](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.StorageMetadataLabel)` (message)
  * `[StoredInfoType](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.StoredInfoType)` (message)
  * `[StoredInfoTypeConfig](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.StoredInfoTypeConfig)` (message)
  * `[StoredInfoTypeState](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.StoredInfoTypeState)` (enum)
  * `[StoredInfoTypeStats](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.StoredInfoTypeStats)` (message)
  * `[StoredInfoTypeVersion](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.StoredInfoTypeVersion)` (message)
  * `[StoredType](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.StoredType)` (message)
  * `[StringValueBatch](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.StringValueBatch)` (message)
  * `[Table](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.Table)` (message)
  * `[Table.Row](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.Table.Row)` (message)
  * `[TableDataProfile](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.TableDataProfile)` (message)
  * `[TableDataProfile.State](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.TableDataProfile.State)` (enum)
  * `[TableLocation](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.TableLocation)` (message)
  * `[TableOptions](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.TableOptions)` (message)
  * `[TableReference](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.TableReference)` (message)
  * `[Tag](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.Tag)` (message)
  * `[TagFilter](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.TagFilter)` (message)
  * `[TagFilters](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.TagFilters)` (message)
  * `[TimePartConfig](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.TimePartConfig)` (message)
  * `[TimePartConfig.TimePart](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.TimePartConfig.TimePart)` (enum)
  * `[TransformationConfig](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.TransformationConfig)` (message)
  * `[TransformationContainerType](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.TransformationContainerType)` (enum)
  * `[TransformationDescription](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.TransformationDescription)` (message)
  * `[TransformationDetails](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.TransformationDetails)` (message)
  * `[TransformationDetailsStorageConfig](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.TransformationDetailsStorageConfig)` (message)
  * `[TransformationErrorHandling](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.TransformationErrorHandling)` (message)
  * `[TransformationErrorHandling.LeaveUntransformed](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.TransformationErrorHandling.LeaveUntransformed)` (message)
  * `[TransformationErrorHandling.ThrowError](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.TransformationErrorHandling.ThrowError)` (message)
  * `[TransformationLocation](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.TransformationLocation)` (message)
  * `[TransformationOverview](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.TransformationOverview)` (message)
  * `[TransformationResultStatus](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.TransformationResultStatus)` (message)
  * `[TransformationResultStatusType](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.TransformationResultStatusType)` (enum)
  * `[TransformationSummary](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.TransformationSummary)` (message)
  * `[TransformationSummary.SummaryResult](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.TransformationSummary.SummaryResult)` (message)
  * `[TransformationSummary.TransformationResultCode](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.TransformationSummary.TransformationResultCode)` (enum)
  * `[TransformationType](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.TransformationType)` (enum)
  * `[TransientCryptoKey](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.TransientCryptoKey)` (message)
  * `[UniquenessScoreLevel](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.UniquenessScoreLevel)` (enum)
  * `[UnwrappedCryptoKey](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.UnwrappedCryptoKey)` (message)
  * `[UpdateConnectionRequest](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.UpdateConnectionRequest)` (message)
  * `[UpdateContentPolicyRequest](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.UpdateContentPolicyRequest)` (message)
  * `[UpdateDeidentifyTemplateRequest](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.UpdateDeidentifyTemplateRequest)` (message)
  * `[UpdateDiscoveryConfigRequest](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.UpdateDiscoveryConfigRequest)` (message)
  * `[UpdateInspectTemplateRequest](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.UpdateInspectTemplateRequest)` (message)
  * `[UpdateJobTriggerRequest](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.UpdateJobTriggerRequest)` (message)
  * `[UpdateStoredInfoTypeRequest](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.UpdateStoredInfoTypeRequest)` (message)
  * `[Value](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.Value)` (message)
  * `[ValueFrequency](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ValueFrequency)` (message)
  * `[VersionDescription](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.VersionDescription)` (message)
  * `[VertexDatasetCollection](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.VertexDatasetCollection)` (message)
  * `[VertexDatasetDiscoveryTarget](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.VertexDatasetDiscoveryTarget)` (message)
  * `[VertexDatasetRegex](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.VertexDatasetRegex)` (message)
  * `[VertexDatasetRegexes](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.VertexDatasetRegexes)` (message)
  * `[VertexDatasetResourceReference](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.VertexDatasetResourceReference)` (message)



## DlpService

Sensitive Data Protection provides access to a powerful sensitive data inspection, classification, and de-identification platform that works on text, images, and Google Cloud storage repositories. To learn more about concepts and find how-to guides see <https://docs.cloud.google.com/sensitive-data-protection/docs/>.

ActivateJobTrigger  
---  
` rpc ActivateJobTrigger(`[ActivateJobTriggerRequest](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ActivateJobTriggerRequest)`) returns (`[DlpJob](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DlpJob)`) ` Activate a job trigger. Causes the immediate execute of a trigger instead of waiting on the trigger event to occur.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
CancelDlpJob  
---  
` rpc CancelDlpJob(`[CancelDlpJobRequest](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.CancelDlpJobRequest)`) returns (`[Empty](https://protobuf.dev/reference/protobuf/google.protobuf/#empty)`) ` Starts asynchronous cancellation on a long-running DlpJob. The server makes a best effort to cancel the DlpJob, but success is not guaranteed. See <https://docs.cloud.google.com/sensitive-data-protection/docs/inspecting-storage> and <https://docs.cloud.google.com/sensitive-data-protection/docs/compute-risk-analysis> to learn more.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
CreateConnection  
---  
` rpc CreateConnection(`[CreateConnectionRequest](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.CreateConnectionRequest)`) returns (`[Connection](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.Connection)`) ` Create a Connection to an external data source.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
CreateContentPolicy  
---  
` rpc CreateContentPolicy(`[CreateContentPolicyRequest](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.CreateContentPolicyRequest)`) returns (`[ContentPolicy](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ContentPolicy)`) ` Create a ContentPolicy.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
CreateDeidentifyTemplate  
---  
` rpc CreateDeidentifyTemplate(`[CreateDeidentifyTemplateRequest](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.CreateDeidentifyTemplateRequest)`) returns (`[DeidentifyTemplate](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DeidentifyTemplate)`) ` Creates a DeidentifyTemplate for reusing frequently used configuration for de-identifying content, images, and storage. See <https://docs.cloud.google.com/sensitive-data-protection/docs/creating-templates-deid> to learn more.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
CreateDiscoveryConfig  
---  
` rpc CreateDiscoveryConfig(`[CreateDiscoveryConfigRequest](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.CreateDiscoveryConfigRequest)`) returns (`[DiscoveryConfig](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DiscoveryConfig)`) ` Creates a config for discovery to scan and profile storage.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
CreateDlpJob  
---  
` rpc CreateDlpJob(`[CreateDlpJobRequest](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.CreateDlpJobRequest)`) returns (`[DlpJob](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DlpJob)`) ` Creates a new job to inspect storage or calculate risk metrics. See <https://docs.cloud.google.com/sensitive-data-protection/docs/inspecting-storage> and <https://docs.cloud.google.com/sensitive-data-protection/docs/compute-risk-analysis> to learn more.When no InfoTypes or CustomInfoTypes are specified in inspect jobs, the system will automatically choose what detectors to run. By default this may be all types, but may change over time as detectors are updated.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
CreateInspectTemplate  
---  
` rpc CreateInspectTemplate(`[CreateInspectTemplateRequest](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.CreateInspectTemplateRequest)`) returns (`[InspectTemplate](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.InspectTemplate)`) ` Creates an InspectTemplate for reusing frequently used configuration for inspecting content, images, and storage. See <https://docs.cloud.google.com/sensitive-data-protection/docs/creating-templates> to learn more.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
CreateJobTrigger  
---  
` rpc CreateJobTrigger(`[CreateJobTriggerRequest](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.CreateJobTriggerRequest)`) returns (`[JobTrigger](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.JobTrigger)`) ` Creates a job trigger to run DLP actions such as scanning storage for sensitive information on a set schedule. See <https://docs.cloud.google.com/sensitive-data-protection/docs/creating-job-triggers> to learn more.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
CreateStoredInfoType  
---  
` rpc CreateStoredInfoType(`[CreateStoredInfoTypeRequest](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.CreateStoredInfoTypeRequest)`) returns (`[StoredInfoType](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.StoredInfoType)`) ` Creates a pre-built stored infoType to be used for inspection. See <https://docs.cloud.google.com/sensitive-data-protection/docs/creating-stored-infotypes> to learn more.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
DeidentifyContent  
---  
` rpc DeidentifyContent(`[DeidentifyContentRequest](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DeidentifyContentRequest)`) returns (`[DeidentifyContentResponse](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DeidentifyContentResponse)`) ` De-identifies potentially sensitive info from a ContentItem. This method has limits on input size and output size. See <https://docs.cloud.google.com/sensitive-data-protection/docs/deidentify-sensitive-data> to learn more.When no InfoTypes or CustomInfoTypes are specified in this request, the system will automatically choose what detectors to run. By default this may be all types, but may change over time as detectors are updated.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
DeleteConnection  
---  
` rpc DeleteConnection(`[DeleteConnectionRequest](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DeleteConnectionRequest)`) returns (`[Empty](https://protobuf.dev/reference/protobuf/google.protobuf/#empty)`) ` Delete a Connection.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
DeleteContentPolicy  
---  
` rpc DeleteContentPolicy(`[DeleteContentPolicyRequest](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DeleteContentPolicyRequest)`) returns (`[Empty](https://protobuf.dev/reference/protobuf/google.protobuf/#empty)`) ` Delete a ContentPolicy.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
DeleteDeidentifyTemplate  
---  
` rpc DeleteDeidentifyTemplate(`[DeleteDeidentifyTemplateRequest](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DeleteDeidentifyTemplateRequest)`) returns (`[Empty](https://protobuf.dev/reference/protobuf/google.protobuf/#empty)`) ` Deletes a DeidentifyTemplate. See <https://docs.cloud.google.com/sensitive-data-protection/docs/creating-templates-deid> to learn more.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
DeleteDiscoveryConfig  
---  
` rpc DeleteDiscoveryConfig(`[DeleteDiscoveryConfigRequest](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DeleteDiscoveryConfigRequest)`) returns (`[Empty](https://protobuf.dev/reference/protobuf/google.protobuf/#empty)`) ` Deletes a discovery configuration.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
DeleteDlpJob  
---  
` rpc DeleteDlpJob(`[DeleteDlpJobRequest](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DeleteDlpJobRequest)`) returns (`[Empty](https://protobuf.dev/reference/protobuf/google.protobuf/#empty)`) ` Deletes a long-running DlpJob. This method indicates that the client is no longer interested in the DlpJob result. The job will be canceled if possible. See <https://docs.cloud.google.com/sensitive-data-protection/docs/inspecting-storage> and <https://docs.cloud.google.com/sensitive-data-protection/docs/compute-risk-analysis> to learn more.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
DeleteFileStoreDataProfile  
---  
` rpc DeleteFileStoreDataProfile(`[DeleteFileStoreDataProfileRequest](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DeleteFileStoreDataProfileRequest)`) returns (`[Empty](https://protobuf.dev/reference/protobuf/google.protobuf/#empty)`) ` Delete a FileStoreDataProfile. Will not prevent the profile from being regenerated if the resource is still included in a discovery configuration.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
DeleteInspectTemplate  
---  
` rpc DeleteInspectTemplate(`[DeleteInspectTemplateRequest](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DeleteInspectTemplateRequest)`) returns (`[Empty](https://protobuf.dev/reference/protobuf/google.protobuf/#empty)`) ` Deletes an InspectTemplate. See <https://docs.cloud.google.com/sensitive-data-protection/docs/creating-templates> to learn more.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
DeleteJobTrigger  
---  
` rpc DeleteJobTrigger(`[DeleteJobTriggerRequest](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DeleteJobTriggerRequest)`) returns (`[Empty](https://protobuf.dev/reference/protobuf/google.protobuf/#empty)`) ` Deletes a job trigger. See <https://docs.cloud.google.com/sensitive-data-protection/docs/creating-job-triggers> to learn more.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
DeleteStoredInfoType  
---  
` rpc DeleteStoredInfoType(`[DeleteStoredInfoTypeRequest](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DeleteStoredInfoTypeRequest)`) returns (`[Empty](https://protobuf.dev/reference/protobuf/google.protobuf/#empty)`) ` Deletes a stored infoType. See <https://docs.cloud.google.com/sensitive-data-protection/docs/creating-stored-infotypes> to learn more.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
DeleteTableDataProfile  
---  
` rpc DeleteTableDataProfile(`[DeleteTableDataProfileRequest](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DeleteTableDataProfileRequest)`) returns (`[Empty](https://protobuf.dev/reference/protobuf/google.protobuf/#empty)`) ` Delete a TableDataProfile. Will not prevent the profile from being regenerated if the table is still included in a discovery configuration.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
FinishDlpJob  
---  
` rpc FinishDlpJob(`[FinishDlpJobRequest](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.FinishDlpJobRequest)`) returns (`[Empty](https://protobuf.dev/reference/protobuf/google.protobuf/#empty)`) ` Finish a running hybrid DlpJob. Triggers the finalization steps and running of any enabled actions that have not yet run.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
GetColumnDataProfile  
---  
` rpc GetColumnDataProfile(`[GetColumnDataProfileRequest](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.GetColumnDataProfileRequest)`) returns (`[ColumnDataProfile](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ColumnDataProfile)`) ` Gets a column data profile.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
GetConnection  
---  
` rpc GetConnection(`[GetConnectionRequest](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.GetConnectionRequest)`) returns (`[Connection](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.Connection)`) ` Get a Connection by name.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
GetContentPolicy  
---  
` rpc GetContentPolicy(`[GetContentPolicyRequest](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.GetContentPolicyRequest)`) returns (`[ContentPolicy](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ContentPolicy)`) ` Get a ContentPolicy.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
GetDeidentifyTemplate  
---  
` rpc GetDeidentifyTemplate(`[GetDeidentifyTemplateRequest](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.GetDeidentifyTemplateRequest)`) returns (`[DeidentifyTemplate](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DeidentifyTemplate)`) ` Gets a DeidentifyTemplate. See <https://docs.cloud.google.com/sensitive-data-protection/docs/creating-templates-deid> to learn more.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
GetDiscoveryConfig  
---  
` rpc GetDiscoveryConfig(`[GetDiscoveryConfigRequest](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.GetDiscoveryConfigRequest)`) returns (`[DiscoveryConfig](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DiscoveryConfig)`) ` Gets a discovery configuration.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
GetDlpJob  
---  
` rpc GetDlpJob(`[GetDlpJobRequest](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.GetDlpJobRequest)`) returns (`[DlpJob](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DlpJob)`) ` Gets the latest state of a long-running DlpJob. See <https://docs.cloud.google.com/sensitive-data-protection/docs/inspecting-storage> and <https://docs.cloud.google.com/sensitive-data-protection/docs/compute-risk-analysis> to learn more.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
GetFileStoreDataProfile  
---  
` rpc GetFileStoreDataProfile(`[GetFileStoreDataProfileRequest](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.GetFileStoreDataProfileRequest)`) returns (`[FileStoreDataProfile](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.FileStoreDataProfile)`) ` Gets a file store data profile.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
GetInspectTemplate  
---  
` rpc GetInspectTemplate(`[GetInspectTemplateRequest](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.GetInspectTemplateRequest)`) returns (`[InspectTemplate](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.InspectTemplate)`) ` Gets an InspectTemplate. See <https://docs.cloud.google.com/sensitive-data-protection/docs/creating-templates> to learn more.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
GetJobTrigger  
---  
` rpc GetJobTrigger(`[GetJobTriggerRequest](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.GetJobTriggerRequest)`) returns (`[JobTrigger](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.JobTrigger)`) ` Gets a job trigger. See <https://docs.cloud.google.com/sensitive-data-protection/docs/creating-job-triggers> to learn more.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
GetProjectDataProfile  
---  
` rpc GetProjectDataProfile(`[GetProjectDataProfileRequest](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.GetProjectDataProfileRequest)`) returns (`[ProjectDataProfile](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ProjectDataProfile)`) ` Gets a project data profile.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
GetStoredInfoType  
---  
` rpc GetStoredInfoType(`[GetStoredInfoTypeRequest](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.GetStoredInfoTypeRequest)`) returns (`[StoredInfoType](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.StoredInfoType)`) ` Gets a stored infoType. See <https://docs.cloud.google.com/sensitive-data-protection/docs/creating-stored-infotypes> to learn more.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
GetTableDataProfile  
---  
` rpc GetTableDataProfile(`[GetTableDataProfileRequest](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.GetTableDataProfileRequest)`) returns (`[TableDataProfile](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.TableDataProfile)`) ` Gets a table data profile.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
HybridInspectDlpJob  
---  
` rpc HybridInspectDlpJob(`[HybridInspectDlpJobRequest](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.HybridInspectDlpJobRequest)`) returns (`[HybridInspectResponse](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.HybridInspectResponse)`) ` Inspect hybrid content and store findings to a job. To review the findings, inspect the job. Inspection will occur asynchronously.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
HybridInspectJobTrigger  
---  
` rpc HybridInspectJobTrigger(`[HybridInspectJobTriggerRequest](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.HybridInspectJobTriggerRequest)`) returns (`[HybridInspectResponse](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.HybridInspectResponse)`) ` Inspect hybrid content and store findings to a trigger. The inspection will be processed asynchronously. To review the findings monitor the jobs within the trigger.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
InspectContent  
---  
` rpc InspectContent(`[InspectContentRequest](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.InspectContentRequest)`) returns (`[InspectContentResponse](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.InspectContentResponse)`) ` Finds potentially sensitive info in content. This method has limits on input size, processing time, and output size.When no InfoTypes or CustomInfoTypes are specified in this request, the system will automatically choose what detectors to run. By default this may be all types, but may change over time as detectors are updated.For how to guides, see <https://docs.cloud.google.com/sensitive-data-protection/docs/inspecting-images> and <https://docs.cloud.google.com/sensitive-data-protection/docs/inspecting-text>,

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
ListColumnDataProfiles  
---  
` rpc ListColumnDataProfiles(`[ListColumnDataProfilesRequest](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ListColumnDataProfilesRequest)`) returns (`[ListColumnDataProfilesResponse](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ListColumnDataProfilesResponse)`) ` Lists column data profiles for an organization.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
ListConnections  
---  
` rpc ListConnections(`[ListConnectionsRequest](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ListConnectionsRequest)`) returns (`[ListConnectionsResponse](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ListConnectionsResponse)`) ` Lists Connections in a parent. Use SearchConnections to see all connections within an organization.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
ListContentPolicies  
---  
` rpc ListContentPolicies(`[ListContentPoliciesRequest](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ListContentPoliciesRequest)`) returns (`[ListContentPoliciesResponse](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ListContentPoliciesResponse)`) ` Lists ContentPolicies in a parent.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
ListDeidentifyTemplates  
---  
` rpc ListDeidentifyTemplates(`[ListDeidentifyTemplatesRequest](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ListDeidentifyTemplatesRequest)`) returns (`[ListDeidentifyTemplatesResponse](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ListDeidentifyTemplatesResponse)`) ` Lists DeidentifyTemplates. See <https://docs.cloud.google.com/sensitive-data-protection/docs/creating-templates-deid> to learn more.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
ListDiscoveryConfigs  
---  
` rpc ListDiscoveryConfigs(`[ListDiscoveryConfigsRequest](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ListDiscoveryConfigsRequest)`) returns (`[ListDiscoveryConfigsResponse](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ListDiscoveryConfigsResponse)`) ` Lists discovery configurations.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
ListDlpJobs  
---  
` rpc ListDlpJobs(`[ListDlpJobsRequest](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ListDlpJobsRequest)`) returns (`[ListDlpJobsResponse](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ListDlpJobsResponse)`) ` Lists DlpJobs that match the specified filter in the request. See <https://docs.cloud.google.com/sensitive-data-protection/docs/inspecting-storage> and <https://docs.cloud.google.com/sensitive-data-protection/docs/compute-risk-analysis> to learn more.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
ListFileStoreDataProfiles  
---  
` rpc ListFileStoreDataProfiles(`[ListFileStoreDataProfilesRequest](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ListFileStoreDataProfilesRequest)`) returns (`[ListFileStoreDataProfilesResponse](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ListFileStoreDataProfilesResponse)`) ` Lists file store data profiles for an organization.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
ListInfoTypes  
---  
` rpc ListInfoTypes(`[ListInfoTypesRequest](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ListInfoTypesRequest)`) returns (`[ListInfoTypesResponse](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ListInfoTypesResponse)`) ` Returns a list of the sensitive information types that the DLP API supports. See <https://docs.cloud.google.com/sensitive-data-protection/docs/infotypes-reference> to learn more.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
ListInspectTemplates  
---  
` rpc ListInspectTemplates(`[ListInspectTemplatesRequest](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ListInspectTemplatesRequest)`) returns (`[ListInspectTemplatesResponse](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ListInspectTemplatesResponse)`) ` Lists InspectTemplates. See <https://docs.cloud.google.com/sensitive-data-protection/docs/creating-templates> to learn more.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
ListJobTriggers  
---  
` rpc ListJobTriggers(`[ListJobTriggersRequest](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ListJobTriggersRequest)`) returns (`[ListJobTriggersResponse](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ListJobTriggersResponse)`) ` Lists job triggers. See <https://docs.cloud.google.com/sensitive-data-protection/docs/creating-job-triggers> to learn more.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
ListProjectDataProfiles  
---  
` rpc ListProjectDataProfiles(`[ListProjectDataProfilesRequest](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ListProjectDataProfilesRequest)`) returns (`[ListProjectDataProfilesResponse](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ListProjectDataProfilesResponse)`) ` Lists project data profiles for an organization.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
ListStoredInfoTypes  
---  
` rpc ListStoredInfoTypes(`[ListStoredInfoTypesRequest](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ListStoredInfoTypesRequest)`) returns (`[ListStoredInfoTypesResponse](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ListStoredInfoTypesResponse)`) ` Lists stored infoTypes. See <https://docs.cloud.google.com/sensitive-data-protection/docs/creating-stored-infotypes> to learn more.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
ListTableDataProfiles  
---  
` rpc ListTableDataProfiles(`[ListTableDataProfilesRequest](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ListTableDataProfilesRequest)`) returns (`[ListTableDataProfilesResponse](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ListTableDataProfilesResponse)`) ` Lists table data profiles for an organization.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
RedactImage  
---  
` rpc RedactImage(`[RedactImageRequest](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.RedactImageRequest)`) returns (`[RedactImageResponse](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.RedactImageResponse)`) ` Redacts potentially sensitive info from an image. This method has limits on input size, processing time, and output size. See <https://docs.cloud.google.com/sensitive-data-protection/docs/redacting-sensitive-data-images> to learn more.When no InfoTypes or CustomInfoTypes are specified in this request, the system will automatically choose what detectors to run. By default this may be all types, but may change over time as detectors are updated.Only the first frame of each multiframe image is redacted. Metadata and other frames are omitted in the response.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
ReidentifyContent  
---  
` rpc ReidentifyContent(`[ReidentifyContentRequest](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ReidentifyContentRequest)`) returns (`[ReidentifyContentResponse](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ReidentifyContentResponse)`) ` Re-identifies content that has been de-identified. See <https://docs.cloud.google.com/sensitive-data-protection/docs/pseudonymization#re-identification_in_free_text_code_example> to learn more.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
SearchConnections  
---  
` rpc SearchConnections(`[SearchConnectionsRequest](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.SearchConnectionsRequest)`) returns (`[SearchConnectionsResponse](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.SearchConnectionsResponse)`) ` Searches for Connections in a parent.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
UpdateConnection  
---  
` rpc UpdateConnection(`[UpdateConnectionRequest](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.UpdateConnectionRequest)`) returns (`[Connection](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.Connection)`) ` Update a Connection.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
UpdateContentPolicy  
---  
` rpc UpdateContentPolicy(`[UpdateContentPolicyRequest](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.UpdateContentPolicyRequest)`) returns (`[ContentPolicy](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ContentPolicy)`) ` Update a ContentPolicy.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
UpdateDeidentifyTemplate  
---  
` rpc UpdateDeidentifyTemplate(`[UpdateDeidentifyTemplateRequest](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.UpdateDeidentifyTemplateRequest)`) returns (`[DeidentifyTemplate](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DeidentifyTemplate)`) ` Updates the DeidentifyTemplate. See <https://docs.cloud.google.com/sensitive-data-protection/docs/creating-templates-deid> to learn more.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
UpdateDiscoveryConfig  
---  
` rpc UpdateDiscoveryConfig(`[UpdateDiscoveryConfigRequest](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.UpdateDiscoveryConfigRequest)`) returns (`[DiscoveryConfig](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DiscoveryConfig)`) ` Updates a discovery configuration.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
UpdateInspectTemplate  
---  
` rpc UpdateInspectTemplate(`[UpdateInspectTemplateRequest](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.UpdateInspectTemplateRequest)`) returns (`[InspectTemplate](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.InspectTemplate)`) ` Updates the InspectTemplate. See <https://docs.cloud.google.com/sensitive-data-protection/docs/creating-templates> to learn more.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
UpdateJobTrigger  
---  
` rpc UpdateJobTrigger(`[UpdateJobTriggerRequest](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.UpdateJobTriggerRequest)`) returns (`[JobTrigger](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.JobTrigger)`) ` Updates a job trigger. See <https://docs.cloud.google.com/sensitive-data-protection/docs/creating-job-triggers> to learn more.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
UpdateStoredInfoType  
---  
` rpc UpdateStoredInfoType(`[UpdateStoredInfoTypeRequest](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.UpdateStoredInfoTypeRequest)`) returns (`[StoredInfoType](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.StoredInfoType)`) ` Updates the stored infoType by creating a new version. The existing version will continue to be used until the new version is ready. See <https://docs.cloud.google.com/sensitive-data-protection/docs/creating-stored-infotypes> to learn more.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
  
## Action

A task to execute on the completion of a job. See <https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-actions> to learn more.

Fields  
---  
Union field `action`. Extra events to execute after the job has finished. `action` can be only one of the following:  
`save_findings` |  `[SaveFindings](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.Action.SaveFindings)` Save resulting findings in a provided location.  
`pub_sub` |  `[PublishToPubSub](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.Action.PublishToPubSub)` Publish a notification to a Pub/Sub topic.  
`publish_summary_to_cscc` |  `[PublishSummaryToCscc](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.Action.PublishSummaryToCscc)` Publish summary to Cloud Security Command Center (Alpha).  
`publish_findings_to_cloud_data_catalog  
**(deprecated)**` |  `[PublishFindingsToCloudDataCatalog](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.Action.PublishFindingsToCloudDataCatalog)` This item is deprecated!Deprecated because Data Catalog is being turned down. Use publish_findings_to_dataplex_catalog to publish findings to Dataplex Universal Catalog.  
`publish_findings_to_dataplex_catalog` |  `[PublishFindingsToDataplexCatalog](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.Action.PublishFindingsToDataplexCatalog)` Publish findings as an aspect to Dataplex Universal Catalog.  
`deidentify` |  `[Deidentify](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.Action.Deidentify)` Create a de-identified copy of the input data.  
`job_notification_emails` |  `[JobNotificationEmails](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.Action.JobNotificationEmails)` Sends an email when the job completes. The email goes to IAM project owners and technical [Essential Contacts](https://docs.cloud.google.com/resource-manager/docs/managing-notification-contacts).  
`publish_to_stackdriver` |  `[PublishToStackdriver](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.Action.PublishToStackdriver)` Enable Stackdriver metric dlp.googleapis.com/finding_count.  
  
## Deidentify

Create a de-identified copy of a storage bucket. Only compatible with Cloud Storage buckets.

A TransformationDetail will be created for each transformation.

Compatible with: Inspection of Cloud Storage

Fields  
---  
`transformation_config` |  `[TransformationConfig](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.TransformationConfig)` User specified deidentify templates and configs for structured, unstructured, and image files.  
`transformation_details_storage_config` |  `[TransformationDetailsStorageConfig](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.TransformationDetailsStorageConfig)` Config for storing transformation details.This field specifies the configuration for storing detailed metadata about each transformation performed during a de-identification process. The metadata is stored separately from the de-identified content itself and provides a granular record of both successful transformations and any failures that occurred.Enabling this configuration is essential for users who need to access comprehensive information about the status, outcome, and specifics of each transformation. The details are captured in the `[TransformationDetails](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.TransformationDetails)` message for each operation.Key use cases:

  * **Auditing and compliance**
    * Provides a verifiable audit trail of de-identification activities, which is crucial for meeting regulatory requirements and internal data governance policies.
    * Logs what data was transformed, what transformations were applied, when they occurred, and their success status. This helps demonstrate accountability and due diligence in protecting sensitive data.
  * **Troubleshooting and debugging**
    * Offers detailed error messages and context if a transformation fails. This information is useful for diagnosing and resolving issues in the de-identification pipeline.
    * Helps pinpoint the exact location and nature of failures, speeding up the debugging process.
  * **Process verification and quality assurance**
    * Allows users to confirm that de-identification rules and transformations were applied correctly and consistently across the dataset as intended.
    * Helps in verifying the effectiveness of the chosen de-identification strategies.
  * **Data lineage and impact analysis**
    * Creates a record of how data elements were modified, contributing to data lineage. This is useful for understanding the provenance of de-identified data.
    * Aids in assessing the potential impact of de-identification choices on downstream analytical processes or data usability.
  * **Reporting and operational insights**
    * You can analyze the metadata stored in a queryable BigQuery table to generate reports on transformation success rates, common error types, processing volumes (e.g., transformedBytes), and the types of transformations applied.
    * These insights can inform optimization of de-identification configurations and resource planning.

To take advantage of these benefits, set this configuration. The stored details include a description of the transformation, success or error codes, error messages, the number of bytes transformed, the location of the transformed content, and identifiers for the job and source data.  
`file_types_to_transform[]` |  `[FileType](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.FileType)` List of user-specified file type groups to transform. If specified, only the files with these file types are transformed. If empty, all supported files are transformed. Supported types may be automatically added over time. Any unsupported file types that are set in this field are excluded from de-identification. An error is recorded for each unsupported file in the TransformationDetails output table. Currently the only file types supported are: IMAGES, TEXT_FILES, CSV, TSV.  
Union field `output`. Where to store the output. `output` can be only one of the following:  
`cloud_storage_output` |  `string` Required. User settable Cloud Storage bucket and folders to store de-identified files. This field must be set for Cloud Storage deidentification. The output Cloud Storage bucket must be different from the input bucket. De-identified files will overwrite files in the output path.Form of: gs://bucket/folder/ or gs://bucket  
  
## JobNotificationEmails

This type has no fields.

Sends an email when the job completes. The email goes to IAM project owners and technical [Essential Contacts](https://docs.cloud.google.com/resource-manager/docs/managing-notification-contacts).

## PublishFindingsToCloudDataCatalog

This type has no fields.

Publish findings of a DlpJob to Data Catalog. In Data Catalog, tag templates are applied to the resource that Cloud DLP scanned. Data Catalog tag templates are stored in the same project and region where the BigQuery table exists. For Cloud DLP to create and apply the tag template, the Cloud DLP service agent must have the `roles/datacatalog.tagTemplateOwner` permission on the project. The tag template contains fields summarizing the results of the DlpJob. Any field values previously written by another DlpJob are deleted. `[InfoType naming patterns](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.InfoType)` are strictly enforced when using this feature.

Findings are persisted in Data Catalog storage and are governed by service-specific policies for Data Catalog. For more information, see [Service Specific Terms](https://cloud.google.com/terms/service-terms).

Only a single instance of this action can be specified. This action is allowed only if all resources being scanned are BigQuery tables. Compatible with: Inspect

## PublishFindingsToDataplexCatalog

This type has no fields.

Publish findings of a DlpJob to Dataplex Universal Catalog as a `sensitive-data-protection-job-result` aspect. For more information, see [Send inspection results to Dataplex Universal Catalog as aspects](https://docs.cloud.google.com/sensitive-data-protection/docs/add-aspects-inspection-job).

Aspects are stored in Dataplex Universal Catalog storage and are governed by service-specific policies for Dataplex Universal Catalog. For more information, see [Service Specific Terms](https://cloud.google.com/terms/service-terms).

Only a single instance of this action can be specified. This action is allowed only if all resources being scanned are BigQuery tables. Compatible with: Inspect

## PublishSummaryToCscc

This type has no fields.

Publish the result summary of a DlpJob to [Security Command Center](https://cloud.google.com/security-command-center). This action is available for only projects that belong to an organization. This action publishes the count of finding instances and their infoTypes. The summary of findings are persisted in Security Command Center and are governed by [service-specific policies for Security Command Center](https://cloud.google.com/terms/service-terms). Only a single instance of this action can be specified. Compatible with: Inspect

## PublishToPubSub

Publish a message into a given Pub/Sub topic when DlpJob has completed. The message contains a single field, `DlpJobName`, which is equal to the finished job's [`DlpJob.name`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.dlpJobs#DlpJob). Compatible with: Inspect, Risk

Fields  
---  
`topic` |  `string` Cloud Pub/Sub topic to send notifications to. The topic must have given publishing access rights to the DLP API service account executing the long running DlpJob sending the notifications. Format is projects/{project}/topics/{topic}.  
  
## PublishToStackdriver

This type has no fields.

Enable Stackdriver metric dlp.googleapis.com/finding_count. This will publish a metric to stack driver on each infotype requested and how many findings were found for it. CustomDetectors will be bucketed as 'Custom' under the Stackdriver label 'info_type'.

## SaveFindings

If set, the detailed findings will be persisted to the specified OutputStorageConfig. Only a single instance of this action can be specified. Compatible with: Inspect, Risk

Fields  
---  
`output_config` |  `[OutputStorageConfig](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.OutputStorageConfig)` Location to store findings outside of DLP.  
  
## ActionDetails

The results of an `[Action](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.Action)`.

Fields  
---  
Union field `details`. Summary of what occurred in the actions. `details` can be only one of the following:  
`deidentify_details` |  `[DeidentifyDataSourceDetails](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DeidentifyDataSourceDetails)` Outcome of a de-identification action.  
  
## ActivateJobTriggerRequest

Request message for ActivateJobTrigger.

Fields  
---  
`name` |  `string` Required. Resource name of the trigger to activate, for example `projects/dlp-test-project/jobTriggers/53234423`. Authorization requires one or more of the following [IAM](https://cloud.google.com/iam/docs/) permissions on the specified resource `name`:

  * `dlp.jobTriggers.get`
  * `dlp.jobs.create`

  
  
## AdjustByImageFindings

AdjustmentRule condition for image findings. This rule is silently ignored if the content being inspected is not an image.

Fields  
---  
`info_types[]` |  `[InfoType](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.InfoType)` A list of image-supported infoTypes—excluding [document infoTypes](https://docs.cloud.google.com/sensitive-data-protection/docs/infotypes-reference#documents)—to be used as context for the adjustment rule. Sensitive Data Protection adjusts the likelihood of an image finding if its bounding box has the specified spatial relationship (defined by `image_containment_type`) with a finding of an infoType in this list.For example, you can create a rule to adjust the likelihood of a `US_PASSPORT` finding if it is enclosed by a finding of `OBJECT_TYPE/PERSON/PASSPORT`. To configure this, set `US_PASSPORT` in `InspectionRuleSet.info_types`. Add an `adjustment_rule` with an `adjust_by_image_findings.info_types` that contains `OBJECT_TYPE/PERSON/PASSPORT` and `image_containment_type` set to `encloses`. In this case, the likelihood of the `US_PASSPORT` finding is adjusted, but the likelihood of the `OBJECT_TYPE/PERSON/PASSPORT` finding is not.  
`min_likelihood` |  `[Likelihood](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.Likelihood)` Required. Minimum likelihood of the `adjust_by_image_findings.info_types` finding. If the likelihood is lower than this value, Sensitive Data Protection doesn't adjust the likelihood of the `InspectionRuleSet.info_types` finding.  
`image_containment_type` |  `[ImageContainmentType](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ImageContainmentType)` Specifies the required spatial relationship between the bounding boxes of the target finding and the context infoType findings.  
  
## AdjustByMatchingInfoTypes

AdjustmentRule condition for matching infoTypes.

Fields  
---  
`info_types[]` |  `[InfoType](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.InfoType)` Sensitive Data Protection adjusts the likelihood of a finding if that finding also matches one of these infoTypes.For example, you can create a rule to adjust the likelihood of a `PHONE_NUMBER` finding if the string is found within a document that is classified as `DOCUMENT_TYPE/HR/RESUME`. To configure this, set `PHONE_NUMBER` in `InspectionRuleSet.info_types`. Add an `adjustment_rule` with an `adjust_by_matching_info_types.info_types` that contains `DOCUMENT_TYPE/HR/RESUME`. In this case, the likelihood of the `PHONE_NUMBER` finding is adjusted, but the likelihood of the `DOCUMENT_TYPE/HR/RESUME` finding is not.  
`min_likelihood` |  `[Likelihood](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.Likelihood)` Required. Minimum likelihood of the `adjust_by_matching_info_types.info_types` finding. If the likelihood is lower than this value, Sensitive Data Protection doesn't adjust the likelihood of the `InspectionRuleSet.info_types` finding.  
`matching_type` |  `[MatchingType](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.MatchingType)` How the adjustment rule is applied.Only `MATCHING_TYPE_PARTIAL_MATCH` is supported:

  * Partial match: adjusts the findings of infoTypes specified in the inspection rule when they have a nonempty intersection with a finding of an infoType specified in this adjustment rule.

  
  
## AdjustmentRule

Rule that specifies conditions when a certain infoType's finding details should be adjusted.

Fields  
---  
`likelihood_adjustment` |  `[LikelihoodAdjustment](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.CustomInfoType.DetectionRule.LikelihoodAdjustment)` Likelihood adjustment to apply to the infoType.  
Union field `conditions`. Condition under which the adjustment rule is applied. `conditions` can be only one of the following:  
`adjust_by_matching_info_types` |  `[AdjustByMatchingInfoTypes](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.AdjustByMatchingInfoTypes)` Set of infoTypes for which findings would affect this rule.  
`adjust_by_image_findings` |  `[AdjustByImageFindings](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.AdjustByImageFindings)` AdjustmentRule condition for image findings.  
  
## AllOtherDatabaseResources

This type has no fields.

Match database resources not covered by any other filter.

## AllOtherResources

This type has no fields.

Match discovery resources not covered by any other filter.

## AmazonS3Bucket

Amazon S3 bucket.

Fields  
---  
`aws_account` |  `[AwsAccount](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.AwsAccount)` The AWS account.  
`bucket_name` |  `string` Required. The bucket name.  
  
## AmazonS3BucketConditions

Amazon S3 bucket conditions.

Fields  
---  
`bucket_types[]` |  `[BucketType](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.AmazonS3BucketConditions.BucketType)` Optional. Bucket types that should be profiled. Optional. Defaults to TYPE_ALL_SUPPORTED if unspecified.  
`object_storage_classes[]` |  `[ObjectStorageClass](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.AmazonS3BucketConditions.ObjectStorageClass)` Optional. Object classes that should be profiled. Optional. Defaults to ALL_SUPPORTED_CLASSES if unspecified.  
  
## BucketType

Supported Amazon S3 bucket types. Defaults to TYPE_ALL_SUPPORTED.

Enums  
---  
`TYPE_UNSPECIFIED` | Unused.  
`TYPE_ALL_SUPPORTED` | All supported classes.  
`TYPE_GENERAL_PURPOSE` | A general purpose Amazon S3 bucket.  
  
## ObjectStorageClass

Supported Amazon S3 object storage classes. Defaults to ALL_SUPPORTED_CLASSES.

Enums  
---  
`UNSPECIFIED` | Unused.  
`ALL_SUPPORTED_CLASSES` | All supported classes.  
`STANDARD` | Standard object class.  
`STANDARD_INFREQUENT_ACCESS` | Standard - infrequent access object class.  
`GLACIER_INSTANT_RETRIEVAL` | Glacier - instant retrieval object class.  
`INTELLIGENT_TIERING` | Objects in the S3 Intelligent-Tiering access tiers.  
  
## AmazonS3BucketRegex

Amazon S3 bucket regex.

Fields  
---  
`aws_account_regex` |  `[AwsAccountRegex](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.AwsAccountRegex)` The AWS account regex.  
`bucket_name_regex` |  `string` Optional. Regex to test the bucket name against. If empty, all buckets match.  
  
## AnalyzeDataSourceRiskDetails

Result of a risk analysis operation request.

Fields  
---  
`requested_privacy_metric` |  `[PrivacyMetric](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.PrivacyMetric)` Privacy metric to compute.  
`requested_source_table` |  `[BigQueryTable](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.BigQueryTable)` Input dataset to compute metrics over.  
`requested_options` |  `[RequestedRiskAnalysisOptions](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.AnalyzeDataSourceRiskDetails.RequestedRiskAnalysisOptions)` The configuration used for this job.  
Union field `result`. Values associated with this metric. `result` can be only one of the following:  
`numerical_stats_result` |  `[NumericalStatsResult](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.AnalyzeDataSourceRiskDetails.NumericalStatsResult)` Output only. Numerical stats result  
`categorical_stats_result` |  `[CategoricalStatsResult](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.AnalyzeDataSourceRiskDetails.CategoricalStatsResult)` Output only. Categorical stats result  
`k_anonymity_result` |  `[KAnonymityResult](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.AnalyzeDataSourceRiskDetails.KAnonymityResult)` Output only. K-anonymity result  
`l_diversity_result` |  `[LDiversityResult](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.AnalyzeDataSourceRiskDetails.LDiversityResult)` Output only. L-divesity result  
`k_map_estimation_result` |  `[KMapEstimationResult](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.AnalyzeDataSourceRiskDetails.KMapEstimationResult)` Output only. K-map result  
`delta_presence_estimation_result` |  `[DeltaPresenceEstimationResult](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.AnalyzeDataSourceRiskDetails.DeltaPresenceEstimationResult)` Output only. Delta-presence result  
  
## CategoricalStatsResult

Result of the categorical stats computation.

Fields  
---  
`value_frequency_histogram_buckets[]` |  `[CategoricalStatsHistogramBucket](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.AnalyzeDataSourceRiskDetails.CategoricalStatsResult.CategoricalStatsHistogramBucket)` Histogram of value frequencies in the column.  
  
## CategoricalStatsHistogramBucket

Histogram of value frequencies in the column.

Fields  
---  
`value_frequency_lower_bound` |  `int64` Lower bound on the value frequency of the values in this bucket.  
`value_frequency_upper_bound` |  `int64` Upper bound on the value frequency of the values in this bucket.  
`bucket_size` |  `int64` Total number of values in this bucket.  
`bucket_values[]` |  `[ValueFrequency](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ValueFrequency)` Sample of value frequencies in this bucket. The total number of values returned per bucket is capped at 20.  
`bucket_value_count` |  `int64` Total number of distinct values in this bucket.  
  
## DeltaPresenceEstimationResult

Result of the δ-presence computation. Note that these results are an estimation, not exact values.

Fields  
---  
`delta_presence_estimation_histogram[]` |  `[DeltaPresenceEstimationHistogramBucket](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.AnalyzeDataSourceRiskDetails.DeltaPresenceEstimationResult.DeltaPresenceEstimationHistogramBucket)` The intervals [min_probability, max_probability) do not overlap. If a value doesn't correspond to any such interval, the associated frequency is zero. For example, the following records: {min_probability: 0, max_probability: 0.1, frequency: 17} {min_probability: 0.2, max_probability: 0.3, frequency: 42} {min_probability: 0.3, max_probability: 0.4, frequency: 99} mean that there are no record with an estimated probability in [0.1, 0.2) nor larger or equal to 0.4.  
  
## DeltaPresenceEstimationHistogramBucket

A DeltaPresenceEstimationHistogramBucket message with the following values: min_probability: 0.1 max_probability: 0.2 frequency: 42 means that there are 42 records for which δ is in [0.1, 0.2). An important particular case is when min_probability = max_probability = 1: then, every individual who shares this quasi-identifier combination is in the dataset.

Fields  
---  
`min_probability` |  `double` Between 0 and 1.  
`max_probability` |  `double` Always greater than or equal to min_probability.  
`bucket_size` |  `int64` Number of records within these probability bounds.  
`bucket_values[]` |  `[DeltaPresenceEstimationQuasiIdValues](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.AnalyzeDataSourceRiskDetails.DeltaPresenceEstimationResult.DeltaPresenceEstimationQuasiIdValues)` Sample of quasi-identifier tuple values in this bucket. The total number of classes returned per bucket is capped at 20.  
`bucket_value_count` |  `int64` Total number of distinct quasi-identifier tuple values in this bucket.  
  
## DeltaPresenceEstimationQuasiIdValues

A tuple of values for the quasi-identifier columns.

Fields  
---  
`quasi_ids_values[]` |  `[Value](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.Value)` The quasi-identifier values.  
`estimated_probability` |  `double` The estimated probability that a given individual sharing these quasi-identifier values is in the dataset. This value, typically called δ, is the ratio between the number of records in the dataset with these quasi-identifier values, and the total number of individuals (inside _and_ outside the dataset) with these quasi-identifier values. For example, if there are 15 individuals in the dataset who share the same quasi-identifier values, and an estimated 100 people in the entire population with these values, then δ is 0.15.  
  
## KAnonymityResult

Result of the k-anonymity computation.

Fields  
---  
`equivalence_class_histogram_buckets[]` |  `[KAnonymityHistogramBucket](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.AnalyzeDataSourceRiskDetails.KAnonymityResult.KAnonymityHistogramBucket)` Histogram of k-anonymity equivalence classes.  
  
## KAnonymityEquivalenceClass

The set of columns' values that share the same ldiversity value

Fields  
---  
`quasi_ids_values[]` |  `[Value](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.Value)` Set of values defining the equivalence class. One value per quasi-identifier column in the original KAnonymity metric message. The order is always the same as the original request.  
`equivalence_class_size` |  `int64` Size of the equivalence class, for example number of rows with the above set of values.  
  
## KAnonymityHistogramBucket

Histogram of k-anonymity equivalence classes.

Fields  
---  
`equivalence_class_size_lower_bound` |  `int64` Lower bound on the size of the equivalence classes in this bucket.  
`equivalence_class_size_upper_bound` |  `int64` Upper bound on the size of the equivalence classes in this bucket.  
`bucket_size` |  `int64` Total number of equivalence classes in this bucket.  
`bucket_values[]` |  `[KAnonymityEquivalenceClass](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.AnalyzeDataSourceRiskDetails.KAnonymityResult.KAnonymityEquivalenceClass)` Sample of equivalence classes in this bucket. The total number of classes returned per bucket is capped at 20.  
`bucket_value_count` |  `int64` Total number of distinct equivalence classes in this bucket.  
  
## KMapEstimationResult

Result of the reidentifiability analysis. Note that these results are an estimation, not exact values.

Fields  
---  
`k_map_estimation_histogram[]` |  `[KMapEstimationHistogramBucket](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.AnalyzeDataSourceRiskDetails.KMapEstimationResult.KMapEstimationHistogramBucket)` The intervals [min_anonymity, max_anonymity] do not overlap. If a value doesn't correspond to any such interval, the associated frequency is zero. For example, the following records: {min_anonymity: 1, max_anonymity: 1, frequency: 17} {min_anonymity: 2, max_anonymity: 3, frequency: 42} {min_anonymity: 5, max_anonymity: 10, frequency: 99} mean that there are no record with an estimated anonymity of 4, 5, or larger than 10.  
  
## KMapEstimationHistogramBucket

A KMapEstimationHistogramBucket message with the following values: min_anonymity: 3 max_anonymity: 5 frequency: 42 means that there are 42 records whose quasi-identifier values correspond to 3, 4 or 5 people in the overlying population. An important particular case is when min_anonymity = max_anonymity = 1: the frequency field then corresponds to the number of uniquely identifiable records.

Fields  
---  
`min_anonymity` |  `int64` Always positive.  
`max_anonymity` |  `int64` Always greater than or equal to min_anonymity.  
`bucket_size` |  `int64` Number of records within these anonymity bounds.  
`bucket_values[]` |  `[KMapEstimationQuasiIdValues](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.AnalyzeDataSourceRiskDetails.KMapEstimationResult.KMapEstimationQuasiIdValues)` Sample of quasi-identifier tuple values in this bucket. The total number of classes returned per bucket is capped at 20.  
`bucket_value_count` |  `int64` Total number of distinct quasi-identifier tuple values in this bucket.  
  
## KMapEstimationQuasiIdValues

A tuple of values for the quasi-identifier columns.

Fields  
---  
`quasi_ids_values[]` |  `[Value](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.Value)` The quasi-identifier values.  
`estimated_anonymity` |  `int64` The estimated anonymity for these quasi-identifier values.  
  
## LDiversityResult

Result of the l-diversity computation.

Fields  
---  
`sensitive_value_frequency_histogram_buckets[]` |  `[LDiversityHistogramBucket](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.AnalyzeDataSourceRiskDetails.LDiversityResult.LDiversityHistogramBucket)` Histogram of l-diversity equivalence class sensitive value frequencies.  
  
## LDiversityEquivalenceClass

The set of columns' values that share the same ldiversity value.

Fields  
---  
`quasi_ids_values[]` |  `[Value](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.Value)` Quasi-identifier values defining the k-anonymity equivalence class. The order is always the same as the original request.  
`equivalence_class_size` |  `int64` Size of the k-anonymity equivalence class.  
`num_distinct_sensitive_values` |  `int64` Number of distinct sensitive values in this equivalence class.  
`top_sensitive_values[]` |  `[ValueFrequency](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ValueFrequency)` Estimated frequencies of top sensitive values.  
  
## LDiversityHistogramBucket

Histogram of l-diversity equivalence class sensitive value frequencies.

Fields  
---  
`sensitive_value_frequency_lower_bound` |  `int64` Lower bound on the sensitive value frequencies of the equivalence classes in this bucket.  
`sensitive_value_frequency_upper_bound` |  `int64` Upper bound on the sensitive value frequencies of the equivalence classes in this bucket.  
`bucket_size` |  `int64` Total number of equivalence classes in this bucket.  
`bucket_values[]` |  `[LDiversityEquivalenceClass](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.AnalyzeDataSourceRiskDetails.LDiversityResult.LDiversityEquivalenceClass)` Sample of equivalence classes in this bucket. The total number of classes returned per bucket is capped at 20.  
`bucket_value_count` |  `int64` Total number of distinct equivalence classes in this bucket.  
  
## NumericalStatsResult

Result of the numerical stats computation.

Fields  
---  
`min_value` |  `[Value](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.Value)` Minimum value appearing in the column.  
`max_value` |  `[Value](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.Value)` Maximum value appearing in the column.  
`quantile_values[]` |  `[Value](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.Value)` List of 99 values that partition the set of field values into 100 equal sized buckets.  
  
## RequestedRiskAnalysisOptions

Risk analysis options.

Fields  
---  
`job_config` |  `[RiskAnalysisJobConfig](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.RiskAnalysisJobConfig)` The job config for the risk job.  
  
## AwsAccount

AWS account.

Fields  
---  
`account_id` |  `string` Required. AWS account ID.  
  
## AwsAccountRegex

AWS account regex.

Fields  
---  
`account_id_regex` |  `string` Optional. Regex to test the AWS account ID against. If empty, all accounts match.  
  
## BatchContentItem

Represents a batch of content to inspect or redact.

Fields  
---  
Union field `batch`. Represents the batch to inspect or redact. `batch` can be only one of the following:  
`string_value_batch` |  `[StringValueBatch](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.StringValueBatch)` Optional. Represents a batch of string values to inspect or redact.  
  
## BatchContentLocation

Location within a batch of content.

Fields  
---  
`item_index` |  `int32` Matches an index of a batch item in the batch provided in the request.  
  
## BigQueryDiscoveryTarget

Target used to match against for discovery with BigQuery tables

Fields  
---  
`filter` |  `[DiscoveryBigQueryFilter](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DiscoveryBigQueryFilter)` Required. The tables the discovery cadence applies to. The first target with a matching filter will be the one to apply to a table.  
`conditions` |  `[DiscoveryBigQueryConditions](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DiscoveryBigQueryConditions)` In addition to matching the filter, these conditions must be true before a profile is generated.  
Union field `frequency`. The generation rule includes the logic on how frequently to update the data profiles. If not specified, discovery will re-run and update no more than once a month if new columns appear in the table. `frequency` can be only one of the following:  
`cadence` |  `[DiscoveryGenerationCadence](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DiscoveryGenerationCadence)` How often and when to update profiles. New tables that match both the filter and conditions are scanned as quickly as possible depending on system capacity.  
`disabled` |  `[Disabled](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.Disabled)` Tables that match this filter will not have profiles created.  
  
## BigQueryField

Message defining a field of a BigQuery table.

Fields  
---  
`table` |  `[BigQueryTable](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.BigQueryTable)` Source table of the field.  
`field` |  `[FieldId](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.FieldId)` Designated field in the BigQuery table.  
  
## BigQueryKey

Row key for identifying a record in BigQuery table.

Fields  
---  
`table_reference` |  `[BigQueryTable](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.BigQueryTable)` Complete BigQuery table reference.  
`row_number` |  `int64` Row number inferred at the time the table was scanned. This value is nondeterministic, cannot be queried, and may be null for inspection jobs. To locate findings within a table, specify `inspect_job.storage_config.big_query_options.identifying_fields` in `CreateDlpJobRequest`.  
  
## BigQueryOptions

Options defining BigQuery table and row identifiers.

Fields  
---  
`table_reference` |  `[BigQueryTable](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.BigQueryTable)` Complete BigQuery table reference.  
`identifying_fields[]` |  `[FieldId](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.FieldId)` Table fields that may uniquely identify a row within the table. When `actions.saveFindings.outputConfig.table` is specified, the values of columns specified here are available in the output table under `location.content_locations.record_location.record_key.id_values`. Nested fields such as `person.birthdate.year` are allowed.  
`rows_limit` |  `int64` Max number of rows to scan. If the table has more rows than this value, the rest of the rows are omitted. If not set, or if set to 0, all rows will be scanned. Only one of rows_limit and rows_limit_percent can be specified. Cannot be used in conjunction with TimespanConfig.  
`rows_limit_percent` |  `int32` Max percentage of rows to scan. The rest are omitted. The number of rows scanned is rounded down. Must be between 0 and 100, inclusively. Both 0 and 100 means no limit. Defaults to 0. Only one of rows_limit and rows_limit_percent can be specified. Cannot be used in conjunction with TimespanConfig.Caution: A [known issue](https://docs.cloud.google.com/sensitive-data-protection/docs/known-issues#bq-sampling) is causing the `rowsLimitPercent` field to behave unexpectedly. We recommend using `rowsLimit` instead.  
`sample_method` |  `[SampleMethod](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.BigQueryOptions.SampleMethod)` How to sample the data.  
`excluded_fields[]` |  `[FieldId](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.FieldId)` References to fields excluded from scanning. This allows you to skip inspection of entire columns which you know have no findings. When inspecting a table, we recommend that you inspect all columns. Otherwise, findings might be affected because hints from excluded columns will not be used.  
`included_fields[]` |  `[FieldId](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.FieldId)` Limit scanning only to these fields. When inspecting a table, we recommend that you inspect all columns. Otherwise, findings might be affected because hints from excluded columns will not be used.  
  
## SampleMethod

How to sample rows if not all rows are scanned. Meaningful only when used in conjunction with either rows_limit or rows_limit_percent. If not specified, rows are scanned in the order BigQuery reads them.

Enums  
---  
`SAMPLE_METHOD_UNSPECIFIED` | No sampling.  
`TOP` | Scan groups of rows in the order BigQuery provides (default). Multiple groups of rows may be scanned in parallel, so results may not appear in the same order the rows are read.  
`RANDOM_START` | Randomly pick groups of rows to scan.  
  
## BigQueryRegex

A pattern to match against one or more tables, datasets, or projects that contain BigQuery tables. At least one pattern must be specified. Regular expressions use RE2 [syntax](https://github.com/google/re2/wiki/Syntax); a guide can be found under the google/re2 repository on GitHub.

Fields  
---  
`project_id_regex` |  `string` For organizations, if unset, will match all projects. Has no effect for data profile configurations created within a project.  
`dataset_id_regex` |  `string` If unset, this property matches all datasets.  
`table_id_regex` |  `string` If unset, this property matches all tables.  
  
## BigQueryRegexes

A collection of regular expressions to determine what tables to match against.

Fields  
---  
`patterns[]` |  `[BigQueryRegex](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.BigQueryRegex)` A single BigQuery regular expression pattern to match against one or more tables, datasets, or projects that contain BigQuery tables.  
  
## BigQuerySchemaModification

Attributes evaluated to determine if a schema has been modified. New values may be added at a later time.

Enums  
---  
`SCHEMA_MODIFICATION_UNSPECIFIED` | Unused  
`SCHEMA_NEW_COLUMNS` | Profiles should be regenerated when new columns are added to the table. Default.  
`SCHEMA_REMOVED_COLUMNS` | Profiles should be regenerated when columns are removed from the table.  
  
## BigQueryTable

Message defining the location of a BigQuery table. A table is uniquely identified by its project_id, dataset_id, and table_name. Within a query a table is often referenced with a string in the format of: `<project_id>:<dataset_id>.<table_id>` or `<project_id>.<dataset_id>.<table_id>`.

Fields  
---  
`project_id` |  `string` The Google Cloud project ID of the project containing the table. If omitted, project ID is inferred from the API call.  
`dataset_id` |  `string` Dataset ID of the table.  
`table_id` |  `string` Name of the table.  
  
## BigQueryTableCollection

Specifies a collection of BigQuery tables. Used for Discovery.

Fields  
---  
Union field `pattern`. Maximum of 100 entries. The first filter containing a pattern that matches a table will be used. `pattern` can be only one of the following:  
`include_regexes` |  `[BigQueryRegexes](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.BigQueryRegexes)` A collection of regular expressions to match a BigQuery table against.  
  
## BigQueryTableModification

Attributes evaluated to determine if a table has been modified. New values may be added at a later time.

Enums  
---  
`TABLE_MODIFICATION_UNSPECIFIED` | Unused.  
`TABLE_MODIFIED_TIMESTAMP` | A table will be considered modified when the last_modified_time from BigQuery has been updated.  
  
## BigQueryTableType

Over time new types may be added. Currently VIEW, MATERIALIZED_VIEW, and non-BigLake external tables are not supported.

Enums  
---  
`BIG_QUERY_TABLE_TYPE_UNSPECIFIED` | Unused.  
`BIG_QUERY_TABLE_TYPE_TABLE` | A normal BigQuery table.  
`BIG_QUERY_TABLE_TYPE_EXTERNAL_BIG_LAKE` | A table that references data stored in Cloud Storage.  
`BIG_QUERY_TABLE_TYPE_SNAPSHOT` | A snapshot of a BigQuery table.  
  
## BigQueryTableTypeCollection

Over time new types may be added. Currently VIEW, MATERIALIZED_VIEW, and non-BigLake external tables are not supported.

Enums  
---  
`BIG_QUERY_COLLECTION_UNSPECIFIED` | Unused.  
`BIG_QUERY_COLLECTION_ALL_TYPES` | Automatically generate profiles for all tables, even if the table type is not yet fully supported for analysis. Profiles for unsupported tables will be generated with errors to indicate their partial support. When full support is added, the tables will automatically be profiled during the next scheduled run.  
`BIG_QUERY_COLLECTION_ONLY_SUPPORTED_TYPES` | Only those types fully supported will be profiled. Will expand automatically as Cloud DLP adds support for new table types. Unsupported table types will not have partial profiles generated.  
  
## BigQueryTableTypes

The types of BigQuery tables supported by Cloud DLP.

Fields  
---  
`types[]` |  `[BigQueryTableType](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.BigQueryTableType)` A set of BigQuery table types.  
  
## BoundingBox

Bounding box encompassing detected text within an image. Coordinates are in pixels and strictly within the image or frame bounds.

Fields  
---  
`top` |  `int32` Top coordinate of the bounding box. (0,0) is upper left.  
`left` |  `int32` Left coordinate of the bounding box. (0,0) is upper left.  
`width` |  `int32` Width of the bounding box in pixels.  
`height` |  `int32` Height of the bounding box in pixels.  
  
## BucketingConfig

Generalization function that buckets values based on ranges. The ranges and replacement values are dynamically provided by the user for custom behavior, such as 1-30 -> LOW, 31-65 -> MEDIUM, 66-100 -> HIGH.

This can be used on data of type: number, long, string, timestamp.

If the bound `Value` type differs from the type of data being transformed, we will first attempt converting the type of the data to be transformed to match the type of the bound before comparing. See <https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-bucketing> to learn more.

Fields  
---  
`buckets[]` |  `[Bucket](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.BucketingConfig.Bucket)` Set of buckets. Ranges must be non-overlapping.  
  
## Bucket

Bucket is represented as a range, along with replacement values.

Fields  
---  
`min` |  `[Value](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.Value)` Lower bound of the range, inclusive. Type should be the same as max if used.  
`max` |  `[Value](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.Value)` Upper bound of the range, exclusive; type must match min.  
`replacement_value` |  `[Value](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.Value)` Required. Replacement value for this bucket.  
  
## ByteContentItem

Container for bytes to inspect or redact.

Fields  
---  
`type` |  `[BytesType](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ByteContentItem.BytesType)` The type of data stored in the bytes string. Default will be TEXT_UTF8.  
`data` |  `bytes` Content data to inspect or redact.  
  
## BytesType

The type of data being sent for inspection. To learn more, see [Supported file types](https://docs.cloud.google.com/sensitive-data-protection/docs/supported-file-types).

Only the first frame of each multiframe image is inspected. Metadata and other frames aren't inspected.

Enums  
---  
`BYTES_TYPE_UNSPECIFIED` | Unused  
`IMAGE` | Any image type.  
`IMAGE_JPEG` | jpeg  
`IMAGE_BMP` | bmp  
`IMAGE_PNG` | png  
`IMAGE_SVG` | svg  
`TEXT_UTF8` | plain text  
`WORD_DOCUMENT` | docx, docm, dotx, dotm  
`PDF` | pdf  
`POWERPOINT_DOCUMENT` | pptx, pptm, potx, potm, pot  
`EXCEL_DOCUMENT` | xlsx, xlsm, xltx, xltm  
`AVRO` | avro  
`CSV` | csv  
`TSV` | tsv  
`AUDIO` | Audio file types. Only used for profiling.  
`VIDEO` | Video file types. Only used for profiling.  
`EXECUTABLE` | Executable file types. Only used for profiling.  
`AI_MODEL` | AI model file types. Only used for profiling.  
  
## CancelDlpJobRequest

The request message for canceling a DLP job.

Fields  
---  
`name` |  `string` Required. The name of the DlpJob resource to be cancelled. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `dlp.jobs.cancel`

  
  
## CharacterMaskConfig

Partially mask a string by replacing a given number of characters with a fixed character. Masking can start from the beginning or end of the string. This can be used on data of any type (numbers, longs, and so on) and when de-identifying structured data we'll attempt to preserve the original data's type. (This allows you to take a long like 123 and modify it to a string like **3.

Fields  
---  
`masking_character` |  `string` Character to use to mask the sensitive values—for example, `*` for an alphabetic string such as a name, or `0` for a numeric string such as ZIP code or credit card number. This string must have a length of 1. If not supplied, this value defaults to `*` for strings, and `0` for digits.  
`number_to_mask` |  `int32` Number of characters to mask. If not set, all matching chars will be masked. Skipped characters do not count towards this tally.If `number_to_mask` is negative, this denotes inverse masking. Cloud DLP masks all but a number of characters. For example, suppose you have the following values:

  * `masking_character` is `*`
  * `number_to_mask` is `-4`
  * `reverse_order` is `false`
  * `CharsToIgnore` includes `-`
  * Input string is `1234-5678-9012-3456`

The resulting de-identified string is `****-****-****-3456`. Cloud DLP masks all but the last four characters. If `reverse_order` is `true`, all but the first four characters are masked as `1234-****-****-****`.  
`reverse_order` |  `bool` Mask characters in reverse order. For example, if `masking_character` is `0`, `number_to_mask` is `14`, and `reverse_order` is `false`, then the input string `1234-5678-9012-3456` is masked as `00000000000000-3456`. If `masking_character` is `*`, `number_to_mask` is `3`, and `reverse_order` is `true`, then the string `12345` is masked as `12***`.  
`characters_to_ignore[]` |  `[CharsToIgnore](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.CharsToIgnore)` When masking a string, items in this list will be skipped when replacing characters. For example, if the input string is `555-555-5555` and you instruct Cloud DLP to skip `-` and mask 5 characters with `*`, Cloud DLP returns `***-**5-5555`.  
  
## CharsToIgnore

Characters to skip when doing deidentification of a value. These will be left alone and skipped.

Fields  
---  
Union field `characters`. Type of characters to skip. `characters` can be only one of the following:  
`characters_to_skip` |  `string` Characters to not transform when masking.  
`common_characters_to_ignore` |  `[CommonCharsToIgnore](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.CharsToIgnore.CommonCharsToIgnore)` Common characters to not transform when masking. Useful to avoid removing punctuation.  
  
## CommonCharsToIgnore

Convenience enum for indicating common characters to not transform.

Enums  
---  
`COMMON_CHARS_TO_IGNORE_UNSPECIFIED` | Unused.  
`NUMERIC` | 0-9  
`ALPHA_UPPER_CASE` | A-Z  
`ALPHA_LOWER_CASE` | a-z  
`PUNCTUATION` | US Punctuation, one of !"#$%&'()*+,-./:;<=>?@[]^_`{|}~  
`WHITESPACE` | Whitespace character, one of [ \t\n\x0B\f\r]  
  
## CloudSqlDiscoveryTarget

Target used to match against for discovery with Cloud SQL tables.

Fields  
---  
`filter` |  `[DiscoveryCloudSqlFilter](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DiscoveryCloudSqlFilter)` Required. The tables the discovery cadence applies to. The first target with a matching filter will be the one to apply to a table.  
`conditions` |  `[DiscoveryCloudSqlConditions](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DiscoveryCloudSqlConditions)` In addition to matching the filter, these conditions must be true before a profile is generated.  
Union field `cadence`. Type of schedule. `cadence` can be only one of the following:  
`generation_cadence` |  `[DiscoveryCloudSqlGenerationCadence](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DiscoveryCloudSqlGenerationCadence)` How often and when to update profiles. New tables that match both the filter and conditions are scanned as quickly as possible depending on system capacity.  
`disabled` |  `[Disabled](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.Disabled)` Disable profiling for database resources that match this filter.  
  
## CloudSqlIamCredential

This type has no fields.

Use IAM authentication to connect. This requires the Cloud SQL IAM feature to be enabled on the instance, which is not the default for Cloud SQL. See <https://docs.cloud.google.com/sql/docs/postgres/authentication> and <https://docs.cloud.google.com/sql/docs/mysql/authentication>.

## CloudSqlProperties

Cloud SQL connection properties.

Fields  
---  
`connection_name` |  `string` Optional. Immutable. The Cloud SQL instance for which the connection is defined. Only one connection per instance is allowed. This can only be set at creation time, and cannot be updated.It is an error to use a connection_name from different project or region than the one that holds the connection. For example, a Connection resource for Cloud SQL connection_name `project-id:us-central1:sql-instance` must be created under the parent `projects/project-id/locations/us-central1`  
`max_connections` |  `int32` Required. The DLP API will limit its connections to max_connections. Must be 2 or greater.  
`database_engine` |  `[DatabaseEngine](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.CloudSqlProperties.DatabaseEngine)` Required. The database engine used by the Cloud SQL instance that this connection configures.  
Union field `credential`. How to authenticate to the instance. `credential` can be only one of the following:  
`username_password` |  `[SecretManagerCredential](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.SecretManagerCredential)` A username and password stored in Secret Manager.  
`cloud_sql_iam` |  `[CloudSqlIamCredential](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.CloudSqlIamCredential)` Built-in IAM authentication (must be configured in Cloud SQL).  
  
## DatabaseEngine

Database engine of a Cloud SQL instance. New values may be added over time.

Enums  
---  
`DATABASE_ENGINE_UNKNOWN` | An engine that is not currently supported by Sensitive Data Protection.  
`DATABASE_ENGINE_MYSQL` | Cloud SQL for MySQL instance.  
`DATABASE_ENGINE_POSTGRES` | Cloud SQL for PostgreSQL instance.  
  
## CloudStorageDiscoveryTarget

Target used to match against for discovery with Cloud Storage buckets.

Fields  
---  
`filter` |  `[DiscoveryCloudStorageFilter](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DiscoveryCloudStorageFilter)` Required. The buckets the generation_cadence applies to. The first target with a matching filter will be the one to apply to a bucket.  
`conditions` |  `[DiscoveryFileStoreConditions](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DiscoveryFileStoreConditions)` Optional. In addition to matching the filter, these conditions must be true before a profile is generated.  
Union field `cadence`. How often and when to update profiles. `cadence` can be only one of the following:  
`generation_cadence` |  `[DiscoveryCloudStorageGenerationCadence](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DiscoveryCloudStorageGenerationCadence)` Optional. How often and when to update profiles. New buckets that match both the filter and conditions are scanned as quickly as possible depending on system capacity.  
`disabled` |  `[Disabled](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.Disabled)` Optional. Disable profiling for buckets that match this filter.  
  
## CloudStorageFileSet

Message representing a set of files in Cloud Storage.

Fields  
---  
`url` |  `string` The url, in the format `gs://<bucket>/<path>`. Trailing wildcard in the path is allowed.  
  
## CloudStorageOptions

Options defining a file or a set of files within a Cloud Storage bucket.

Fields  
---  
`file_set` |  `[FileSet](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.CloudStorageOptions.FileSet)` The set of one or more files to scan.  
`bytes_limit_per_file` |  `int64` Max number of bytes to scan from a file. If a scanned file's size is bigger than this value then the rest of the bytes are omitted. Only one of `bytes_limit_per_file` and `bytes_limit_per_file_percent` can be specified. This field can't be set if de-identification is requested. For certain file types, setting this field has no effect. For more information, see [Limits on bytes scanned per file](https://docs.cloud.google.com/sensitive-data-protection/docs/supported-file-types#max-byte-size-per-file).  
`bytes_limit_per_file_percent` |  `int32` Max percentage of bytes to scan from a file. The rest are omitted. The number of bytes scanned is rounded down. Must be between 0 and 100, inclusively. Both 0 and 100 means no limit. Defaults to 0. Only one of bytes_limit_per_file and bytes_limit_per_file_percent can be specified. This field can't be set if de-identification is requested. For certain file types, setting this field has no effect. For more information, see [Limits on bytes scanned per file](https://docs.cloud.google.com/sensitive-data-protection/docs/supported-file-types#max-byte-size-per-file).  
`file_types[]` |  `[FileType](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.FileType)` List of file type groups to include in the scan. If empty, all files are scanned and available data format processors are applied. In addition, the binary content of the selected files is always scanned as well. Images are scanned only as binary if the specified region does not support image inspection and no file_types were specified. Image inspection is restricted to 'global', 'us', 'asia', and 'europe'.  
`sample_method` |  `[SampleMethod](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.CloudStorageOptions.SampleMethod)` How to sample the data.  
`files_limit_percent` |  `int32` Limits the number of files to scan to this percentage of the input FileSet. Number of files scanned is rounded down. Must be between 0 and 100, inclusively. Both 0 and 100 means no limit. Defaults to 0.  
  
## FileSet

Set of files to scan.

Fields  
---  
`url` |  `string` The Cloud Storage url of the file(s) to scan, in the format `gs://<bucket>/<path>`. Trailing wildcard in the path is allowed.If the url ends in a trailing slash, the bucket or directory represented by the url will be scanned non-recursively (content in sub-directories will not be scanned). This means that `gs://mybucket/` is equivalent to `gs://mybucket/*`, and `gs://mybucket/directory/` is equivalent to `gs://mybucket/directory/*`.Exactly one of `url` or `regex_file_set` must be set.  
`regex_file_set` |  `[CloudStorageRegexFileSet](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.CloudStorageRegexFileSet)` The regex-filtered set of files to scan. Exactly one of `url` or `regex_file_set` must be set.  
  
## SampleMethod

How to sample bytes if not all bytes are scanned. Meaningful only when used in conjunction with bytes_limit_per_file. If not specified, scanning would start from the top.

Enums  
---  
`SAMPLE_METHOD_UNSPECIFIED` | No sampling.  
`TOP` | Scan from the top (default).  
`RANDOM_START` | For each file larger than bytes_limit_per_file, randomly pick the offset to start scanning. The scanned bytes are contiguous.  
  
## CloudStoragePath

Message representing a single file or path in Cloud Storage.

Fields  
---  
`path` |  `string` A URL representing a file or path (no wildcards) in Cloud Storage. Example: `gs://[BUCKET_NAME]/dictionary.txt`  
  
## CloudStorageRegex

A pattern to match against one or more file stores. At least one pattern must be specified. Regular expressions use RE2 [syntax](https://github.com/google/re2/wiki/Syntax); a guide can be found under the google/re2 repository on GitHub.

Fields  
---  
`project_id_regex` |  `string` Optional. For organizations, if unset, will match all projects.  
`bucket_name_regex` |  `string` Optional. Regex to test the bucket name against. If empty, all buckets match. Example: "marketing2021" or "(marketing)\d{4}" will both match the bucket gs://marketing2021  
  
## CloudStorageRegexFileSet

Message representing a set of files in a Cloud Storage bucket. Regular expressions are used to allow fine-grained control over which files in the bucket to include.

Included files are those that match at least one item in `include_regex` and do not match any items in `exclude_regex`. Note that a file that matches items from both lists will _not_ be included. For a match to occur, the entire file path (i.e., everything in the url after the bucket name) must match the regular expression.

For example, given the input `{bucket_name: "mybucket", include_regex: ["directory1/.*"], exclude_regex: ["directory1/excluded.*"]}`:

  * `gs://mybucket/directory1/myfile` will be included
  * `gs://mybucket/directory1/directory2/myfile` will be included (`.*` matches across `/`)
  * `gs://mybucket/directory0/directory1/myfile` will _not_ be included (the full path doesn't match any items in `include_regex`)
  * `gs://mybucket/directory1/excludedfile` will _not_ be included (the path matches an item in `exclude_regex`)



If `include_regex` is left empty, it will match all files by default (this is equivalent to setting `include_regex: [".*"]`).

Some other common use cases:

  * `{bucket_name: "mybucket", exclude_regex: [".*\.pdf"]}` will include all files in `mybucket` except for .pdf files
  * `{bucket_name: "mybucket", include_regex: ["directory/[^/]+"]}` will include all files directly under `gs://mybucket/directory/`, without matching across `/`

Fields  
---  
`bucket_name` |  `string` The name of a Cloud Storage bucket. Required.  
`include_regex[]` |  `string` A list of regular expressions matching file paths to include. All files in the bucket that match at least one of these regular expressions will be included in the set of files, except for those that also match an item in `exclude_regex`. Leaving this field empty will match all files by default (this is equivalent to including `.*` in the list).Regular expressions use RE2 [syntax](https://github.com/google/re2/wiki/Syntax); a guide can be found under the google/re2 repository on GitHub.  
`exclude_regex[]` |  `string` A list of regular expressions matching file paths to exclude. All files in the bucket that match at least one of these regular expressions will be excluded from the scan.Regular expressions use RE2 [syntax](https://github.com/google/re2/wiki/Syntax); a guide can be found under the google/re2 repository on GitHub.  
  
## CloudStorageResourceReference

Identifies a single Cloud Storage bucket.

Fields  
---  
`bucket_name` |  `string` Required. The bucket to scan.  
`project_id` |  `string` Required. If within a project-level config, then this must match the config's project id.  
  
## Color

Represents a color in the RGB color space.

Fields  
---  
`red` |  `float` The amount of red in the color as a value in the interval [0, 1].  
`green` |  `float` The amount of green in the color as a value in the interval [0, 1].  
`blue` |  `float` The amount of blue in the color as a value in the interval [0, 1].  
  
## ColumnDataProfile

The profile for a scanned column within a table.

Fields  
---  
`name` |  `string` The name of the profile.  
`profile_status` |  `[ProfileStatus](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ProfileStatus)` Success or error status from the most recent profile generation attempt. May be empty if the profile is still being generated.  
`state` |  `[State](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ColumnDataProfile.State)` State of a profile.  
`profile_last_generated` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` The last time the profile was generated.  
`table_data_profile` |  `string` The resource name of the table data profile.  
`table_full_resource` |  `string` The resource name of the resource this column is within.  
`dataset_project_id` |  `string` The Google Cloud project ID that owns the profiled resource.  
`dataset_location` |  `string` If supported, the location where the dataset's data is stored. See <https://docs.cloud.google.com/bigquery/docs/locations> for supported BigQuery locations.  
`dataset_id` |  `string` The BigQuery dataset ID, if the resource profiled is a BigQuery table.  
`table_id` |  `string` The table ID.  
`column` |  `string` The name of the column.  
`sensitivity_score` |  `[SensitivityScore](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.SensitivityScore)` The sensitivity of this column.  
`data_risk_level` |  `[DataRiskLevel](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DataRiskLevel)` The data risk level for this column.  
`column_info_type` |  `[InfoTypeSummary](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.InfoTypeSummary)` If it's been determined this column can be identified as a single type, this will be set. Otherwise the column either has unidentifiable content or mixed types.  
`other_matches[]` |  `[OtherInfoTypeSummary](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.OtherInfoTypeSummary)` Other types found within this column. List will be unordered.  
`estimated_null_percentage` |  `[NullPercentageLevel](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.NullPercentageLevel)` Approximate percentage of entries being null in the column.  
`estimated_uniqueness_score` |  `[UniquenessScoreLevel](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.UniquenessScoreLevel)` Approximate uniqueness of the column.  
`free_text_score` |  `double` The likelihood that this column contains free-form text. A value close to 1 may indicate the column is likely to contain free-form or natural language text. Range in 0-1.  
`column_type` |  `[ColumnDataType](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ColumnDataProfile.ColumnDataType)` The data type of a given column.  
`policy_state` |  `[ColumnPolicyState](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ColumnDataProfile.ColumnPolicyState)` Indicates if a policy tag has been applied to the column.  
  
## ColumnDataType

Data types of the data in a column. Types may be added over time.

Enums  
---  
`COLUMN_DATA_TYPE_UNSPECIFIED` | Invalid type.  
`TYPE_INT64` | Encoded as a string in decimal format.  
`TYPE_BOOL` | Encoded as a boolean "false" or "true".  
`TYPE_FLOAT64` | Encoded as a number, or string "NaN", "Infinity" or "-Infinity".  
`TYPE_STRING` | Encoded as a string value.  
`TYPE_BYTES` | Encoded as a base64 string per RFC 4648, section 4.  
`TYPE_TIMESTAMP` | Encoded as an RFC 3339 timestamp with mandatory "Z" time zone string: 1985-04-12T23:20:50.52Z  
`TYPE_DATE` | Encoded as RFC 3339 full-date format string: 1985-04-12  
`TYPE_TIME` | Encoded as RFC 3339 partial-time format string: 23:20:50.52  
`TYPE_DATETIME` | Encoded as RFC 3339 full-date "T" partial-time: 1985-04-12T23:20:50.52  
`TYPE_GEOGRAPHY` | Encoded as WKT  
`TYPE_NUMERIC` | Encoded as a decimal string.  
`TYPE_RECORD` | Container of ordered fields, each with a type and field name.  
`TYPE_BIGNUMERIC` | Decimal type.  
`TYPE_JSON` | Json type.  
`TYPE_INTERVAL` | Interval type.  
`TYPE_RANGE_DATE` | `Range<Date>` type.  
`TYPE_RANGE_DATETIME` | `Range<Datetime>` type.  
`TYPE_RANGE_TIMESTAMP` | `Range<Timestamp>` type.  
  
## ColumnPolicyState

The possible policy states for a column.

Enums  
---  
`COLUMN_POLICY_STATE_UNSPECIFIED` | No policy tags.  
`COLUMN_POLICY_TAGGED` | Column has policy tag applied.  
  
## State

Possible states of a profile. New items may be added.

Enums  
---  
`STATE_UNSPECIFIED` | Unused.  
`RUNNING` | The profile is currently running. Once a profile has finished it will transition to DONE.  
`DONE` | The profile is no longer generating. If profile_status.status.code is 0, the profile succeeded, otherwise, it failed.  
  
## Connection

A data connection to allow the DLP API to profile data in locations that require additional configuration.

Fields  
---  
`name` |  `string` Output only. Name of the connection: `projects/{project}/locations/{location}/connections/{name}`.  
`state` |  `[ConnectionState](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ConnectionState)` Required. The connection's state in its lifecycle.  
`errors[]` |  `[Error](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.Error)` Output only. Set if status == ERROR, to provide additional details. Will store the last 10 errors sorted with the most recent first.  
Union field `properties`. Type of connection. `properties` can be only one of the following:  
`cloud_sql` |  `[CloudSqlProperties](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.CloudSqlProperties)` Connect to a Cloud SQL instance.  
  
## ConnectionState

State of the connection. New values may be added over time.

Enums  
---  
`CONNECTION_STATE_UNSPECIFIED` | Unused  
`MISSING_CREDENTIALS` | The DLP API automatically created this connection during an initial scan, and it is awaiting full configuration by a user.  
`AVAILABLE` | A configured connection that has not encountered any errors.  
`ERROR` | A configured connection that encountered errors during its last use. It will not be used again until it is set to AVAILABLE.If the resolution requires external action, then the client must send a request to set the status to AVAILABLE when the connection is ready for use. If the resolution doesn't require external action, then any changes to the connection properties will automatically mark it as AVAILABLE.  
  
## Container

Represents a container that may contain DLP findings. Examples of a container include a file, table, or database record.

Fields  
---  
`type` |  `string` Container type, for example BigQuery or Cloud Storage.  
`project_id` |  `string` Project where the finding was found. Can be different from the project that owns the finding.  
`full_path` |  `string` A string representation of the full container name. Examples: - BigQuery: 'Project:DataSetId.TableId' - Cloud Storage: 'gs://Bucket/folders/filename.txt'  
`root_path` |  `string` The root of the container. Examples:

  * For BigQuery table `project_id:dataset_id.table_id`, the root is `dataset_id`
  * For Cloud Storage file `gs://bucket/folder/filename.txt`, the root is `gs://bucket`

  
`relative_path` |  `string` The rest of the path after the root. Examples:

  * For BigQuery table `project_id:dataset_id.table_id`, the relative path is `table_id`
  * For Cloud Storage file `gs://bucket/folder/filename.txt`, the relative path is `folder/filename.txt`

  
`update_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Findings container modification timestamp, if applicable. For Cloud Storage, this field contains the last file modification timestamp. For a BigQuery table, this field contains the last_modified_time property. For Datastore, this field isn't populated.  
`version` |  `string` Findings container version, if available ("generation" for Cloud Storage).  
  
## ContentItem

Type of content to inspect.

Fields  
---  
`content_metadata` |  `[ContentMetadata](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ContentMetadata)` User provided metadata for the content.  
Union field `data_item`. Data of the item either in the byte array or UTF-8 string form, or table. `data_item` can be only one of the following:  
`value` |  `string` String data to inspect or redact.  
`table` |  `[Table](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.Table)` Structured content for inspection. See <https://docs.cloud.google.com/sensitive-data-protection/docs/inspecting-text#inspecting_a_table> to learn more.  
`byte_item` |  `[ByteContentItem](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ByteContentItem)` Content data to inspect or redact. Replaces `type` and `data`.  
`conversation` |  `[Conversation](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.Conversation)` Represents a conversation (either complete or a slice). It is assumed that all included messages are contiguous and ordered in chronological order.  
`batch_content_item` |  `[BatchContentItem](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.BatchContentItem)` Represents a batch of items to inspect.  
  
## ContentLocation

Precise location of the finding within a document, record, image, or metadata container.

Fields  
---  
`container_name` |  `string` Name of the container where the finding is located. The top level name is the source file name or table name. Names of some common storage containers are formatted as follows:

  * BigQuery tables: `{project_id}:{dataset_id}.{table_id}`
  * Cloud Storage files: `gs://{bucket}/{path}`
  * Datastore namespace: {namespace}

Nested names could be absent if the embedded object has no string identifier (for example, an image contained within a document).  
`container_timestamp` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Finding container modification timestamp, if applicable. For Cloud Storage, this field contains the last file modification timestamp. For a BigQuery table, this field contains the last_modified_time property. For Datastore, this field isn't populated.  
`container_version` |  `string` Finding container version, if available ("generation" for Cloud Storage).  
Union field `location`. Type of the container within the file with location of the finding. `location` can be only one of the following:  
`record_location` |  `[RecordLocation](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.RecordLocation)` Location within a row or record of a database table.  
`image_location` |  `[ImageLocation](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ImageLocation)` Location within an image's pixels.  
`document_location` |  `[DocumentLocation](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DocumentLocation)` Location data for document files.  
`metadata_location` |  `[MetadataLocation](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.MetadataLocation)` Location within the metadata for inspected content.  
`conversation_location` |  `[ConversationLocation](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ConversationLocation)` Location within a conversation.  
`batch_content_location` |  `[BatchContentLocation](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.BatchContentLocation)` Location within a batch of content.  
  
## ContentMetadata

Metadata on content to be scanned.

Fields  
---  
`properties[]` |  `[KeyValueMetadataProperty](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.KeyValueMetadataProperty)` User provided key-value pairs of content metadata.  
`file_labels[]` |  `[FileLabel](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.FileLabel)` Optional. The file labels associated with the content.  
  
## ContentOption

Deprecated and unused.

Enums  
---  
`CONTENT_UNSPECIFIED` | Includes entire content of a file or a data stream.  
`CONTENT_TEXT` | Text content within the data, excluding any metadata.  
`CONTENT_IMAGE` | Images found in the data.  
  
## ContentPolicy

A policy to apply to content based on its inspection findings.

Fields  
---  
`name` |  `string` Output only. Resource name of the policy.  
`create_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. The creation timestamp of a contentPolicy; output-only field.  
`update_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. The last update timestamp of a contentPolicy; output-only field.  
`display_name` |  `string` Optional. Display name (max 63 chars)  
`inspect_config` |  `[InspectConfig](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.InspectConfig)` Optional. InspectConfig to use to produce findings.  
`rules[]` |  `[PolicyRule](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ContentPolicy.PolicyRule)` Required. Policies to apply, based on the findings returned by inspection. The first rule to match applies.  
`unsupported_file_type` |  `[PolicyAction](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ContentPolicy.PolicyAction)` Optional. Action to take if the content is an unsupported file type.  
`input_too_large` |  `[PolicyAction](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ContentPolicy.PolicyAction)` Optional. Action to take if the content is a supported file type but is too large to be scanned.  
`failed_to_scan_supported_file_type` |  `[PolicyAction](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ContentPolicy.PolicyAction)` Optional. Action to take if the content is a supported file type and size but fails to be scanned, for example because the file is encrypted or corrupted.  
`default_action` |  `[PolicyAction](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ContentPolicy.PolicyAction)` Action to take if the content is scanned and no rules match. Defaults to returning an ALLOW verdict if not set.  
`logging_configs[]` |  `[LoggingConfig](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ContentPolicy.LoggingConfig)` Optional. Log the actions taken by the content policy to external systems.  
`errors[]` |  `[Error](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.Error)` Output only. A stream of errors encountered when the policy was applied. Output only field. Will return the last 100 errors. Whenever the policy is modified this list will be cleared.  
  
## LoggingConfig

A single logging configuration.

Fields  
---  
Union field `destination`. The destination for the action logs. `destination` can be only one of the following:  
`log_to_big_query` |  `[LogToBigQuery](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ContentPolicy.LoggingConfig.LogToBigQuery)` Optional. Log the actions taken to a BigQuery table.  
  
## LogToBigQuery

Configuration for logging content policy actions to BigQuery.

Fields  
---  
`project_id` |  `string` Required. The ID of the project containing the BigQuery table to write to.  
`dataset_id` |  `string` Required. The ID of the dataset containing the BigQuery table to write to.  
`table_id` |  `string` Required. The ID of the BigQuery table to write to.  
  
## PolicyAction

A possible action to take when applying a content policy.

Fields  
---  
Union field `action`.`action` can be only one of the following:  
`return_verdict` |  `[ContentPolicyVerdict](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ContentPolicyVerdict)` Optional. If set, the verdict will be returned to the user.  
  
## PolicyRule

A single policy rule. The first rule to match from the list above controls the result.

Fields  
---  
`conditions[]` |  `[PolicyCondition](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ContentPolicy.PolicyRule.PolicyCondition)` Optional. Conditions that must match for this rule to apply. All conditions must match (`AND`). For `OR` conditions, use multiple rules.  
`action` |  `[PolicyAction](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ContentPolicy.PolicyAction)` Required. Action to take if this rule applies.  
  
## PolicyCondition

A condition that must match for this rule to apply.

Fields  
---  
Union field `condition`. A condition. `condition` can be only one of the following:  
`info_type_condition` |  `[InfoTypeCondition](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ContentPolicy.PolicyRule.PolicyCondition.InfoTypeCondition)` A condition based on info types.  
  
## InfoTypeCondition

A info type based condition.

Fields  
---  
`min_count` |  `int64` Optional. The minimum total number of findings of all matching info types required for this condition to evaluate to true. Defaults to 1 if unset.  
Union field `info_type_condition`. A condition based on info types. `info_type_condition` can be only one of the following:  
`info_types` |  `[InfoTypes](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ContentPolicy.PolicyRule.PolicyCondition.InfoTypeCondition.InfoTypes)` match any of these info types.  
`any_info_type` |  `[Empty](https://protobuf.dev/reference/protobuf/google.protobuf/#empty)` match any info types.  
  
## InfoTypes

Info types to match.

Fields  
---  
`info_type_names[]` |  `string` Required. A list of info types to match.  
  
## ContentPolicyActionLog

Message used when saving content policy logs to external storage (such as BigQuery or Cloud Storage).

Fields  
---  
`content_policy` |  `string` The resource name of the content policy that produced this log.  
`log_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` The timestamp of when the action was taken.  
`data_source_type` |  `[DataSourceType](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DataSourceType)` The client-supplied source of the data that is being processed. This allows for aggregating logs by source, for example, "geminienterprise/slack".  
`container_id` |  `string` The client-supplied identifier for a container from which content was scanned, also to aid in aggregation, for example, a specific folder or chat room.  
`document_id` |  `string` The client-supplied identifier for the document that was scanned. This allows tracking down the exact source that produced this log, for example, a message id.  
`matching_info_types[]` |  `[InfoTypeMatch](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ContentPolicyActionLog.InfoTypeMatch)` Unordered set of matching infoTypes found in the content.  
`correlation_id` |  `string` Optional. A correlation ID to associate this log with other logs or systems.  
`scanned_content` |  `[ScannedContent](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ContentPolicyActionLog.ScannedContent)` Optional. Details about the scanned content.  
Union field `action_taken`. The resulting action from evaluating the content policy. `action_taken` can be only one of the following:  
`returned_verdict` |  `[ContentPolicyVerdict](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ContentPolicyVerdict)` The verdict that was returned.  
Union field `trigger`. Trigger for the action. `trigger` can be only one of the following:  
`policy_rule` |  `[PolicyRule](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ContentPolicy.PolicyRule)` A user-defined rule in the content policy was matched.  
`fallback_action` |  `[FallbackActionType](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ContentPolicyActionLog.FallbackActionType)` A fallback action was taken.  
  
## FallbackActionType

Type of fallback action.

Enums  
---  
`FALLBACK_ACTION_TYPE_UNSPECIFIED` | Unused.  
`FALLBACK_ACTION_UNSUPPORTED_FILE_TYPE` | The content was of an unsupported file type.  
`FALLBACK_ACTION_INPUT_TOO_LARGE` | The content exceeded the size limits for scanning.  
`FALLBACK_ACTION_FAILED_TO_SCAN_SUPPORTED_FILE_TYPE` | The content was of a supported file type and size but failed to be scanned, for example because the file is encrypted or corrupted.  
`FALLBACK_ACTION_DEFAULT_ACTION` | No user-defined rule in the content policy matched the content.  
  
## InfoTypeMatch

Information about a matching infoType found in the content.

Fields  
---  
`info_type_name` |  `string`  
  
## ScannedContent

Details about the scanned content.

Fields  
---  
`bytes_type` |  `[BytesType](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ByteContentItem.BytesType)` Optional. The type of the content that was scanned.  
`file_size_bytes` |  `int64` Optional. The size of the content in bytes that was scanned.  
  
## ContentPolicyVerdict

Possible results of applying a content policy. This may expand to include additional result types in the future.

Enums  
---  
`CONTENT_POLICY_VERDICT_UNSPECIFIED` | Not used.  
`ALLOW` | The policy allows the provided content to be used.  
`BLOCK` | The policy prevents the provided content from being used. This should result in a blocked file upload, exclusion from training dataset, or other similar block action. (specific action will depend on the caller).  
  
## Conversation

Complete conversation or slice of a conversation. It is assumed that all included messages are contiguous and ordered in chronological order.

Fields  
---  
`messages[]` |  `[ConversationMessage](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ConversationMessage)` Messages exchanged within this conversation. The maximum number of messages allowed is 50k. The order of the messages is assumed to be chronological and will be used to index findings in the response.  
  
## ConversationLocation

Location within a conversation.

Fields  
---  
Union field `location`. The location of the finding within a conversation. `location` can be only one of the following:  
`message_index` |  `int32` Matches an index of a message in the conversation provided in the request.  
`all_messages` |  `[AllMessages](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ConversationLocation.AllMessages)` If set, indicates that the finding applies to all messages in the conversation.  
  
## AllMessages

This type has no fields.

If set, indicates that the finding applies to all messages in the conversation.

## ConversationMessage

Single message in a conversation.

Fields  
---  
`content  
**(deprecated)**` |  `string` This item is deprecated!Deprecated: Use `message_parts` instead. The contents of this message. Only one of `content` and `message_parts` can be set.  
`message_parts[]` |  `[MessagePart](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ConversationMessage.MessagePart)` Optional. The parts of the message. Restricted to being at most a single text item. Only one of `content` and `message_parts` can be set.  
`message_type` |  `[MessageType](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ConversationMessage.MessageType)` The type of message.  
`participant_id` |  `string` Optional. The identifier of the participant, for example 'test-user' or 'gemini'. The participant ID can contain lowercase letters, numbers, and hyphens; that is, it must match the regular expression: `^[a-z]([a-z0-9-]{0,61}[a-z0-9])?$`. The maximum length is 63 characters.  
  
## MessagePart

A part of a conversation message.

Fields  
---  
Union field `content`. The content of the message part. `content` can be only one of the following:  
`text` |  `string` String content for text-based messages.  
  
## MessageType

The type of message. New values can be added in the future.

Enums  
---  
`MESSAGE_TYPE_UNSPECIFIED` | Unused.  
`CONTENT` | Message contains content to be inspected.  
`CONTEXT` | Message contains context only and will not have findings reported from it during inspection or redacted from it during de-identification.  
  
## CreateConnectionRequest

Request message for CreateConnection.

Fields  
---  
`parent` |  `string` Required. Parent resource name.The format of this value varies depending on the scope of the request (project or organization):

  * Projects scope: `projects/{project_id}/locations/{location_id}`
  * Organizations scope: `organizations/{org_id}/locations/{location_id}`

Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `dlp.connections.create`

  
`connection` |  `[Connection](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.Connection)` Required. The connection resource.  
  
## CreateContentPolicyRequest

Request message for CreateContentPolicy.

Fields  
---  
`parent` |  `string` Required. Parent resource name.The format of this value varies depending on the scope of the request (project):

  * Projects scope: `projects/{project_id}/locations/{location_id}`

Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `dlp.contentPolicies.create`

  
`content_policy` |  `[ContentPolicy](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ContentPolicy)` Required. The content_policy resource.  
`content_policy_id` |  `string` Optional. The content policy ID can contain uppercase and lowercase letters, numbers, and hyphens; that is, it must match the regular expression: `[a-zA-Z\d-_]+`. The maximum length is 100 characters. If empty, the system will generate a random id.  
  
## CreateDeidentifyTemplateRequest

Request message for CreateDeidentifyTemplate.

Fields  
---  
`parent` |  `string` Required. Parent resource name.The format of this value varies depending on the scope of the request (project or organization) and whether you have [specified a processing location](https://docs.cloud.google.com/sensitive-data-protection/docs/specifying-location):

  * Projects scope, location specified: `projects/{project_id}/locations/{location_id}`
  * Projects scope, no location specified (defaults to global): `projects/{project_id}`
  * Organizations scope, location specified: `organizations/{org_id}/locations/{location_id}`
  * Organizations scope, no location specified (defaults to global): `organizations/{org_id}`

The following example `parent` string specifies a parent project with the identifier `example-project`, and specifies the `europe-west3` location for processing data:
    
    
    parent=projects/example-project/locations/europe-west3
    

Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `dlp.deidentifyTemplates.create`

  
`deidentify_template` |  `[DeidentifyTemplate](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DeidentifyTemplate)` Required. The DeidentifyTemplate to create.  
`template_id` |  `string` The template id can contain uppercase and lowercase letters, numbers, and hyphens; that is, it must match the regular expression: `[a-zA-Z\d-_]+`. The maximum length is 100 characters. Can be empty to allow the system to generate one.  
`location_id` |  `string` Deprecated. This field has no effect.  
  
## CreateDiscoveryConfigRequest

Request message for CreateDiscoveryConfig.

Fields  
---  
`parent` |  `string` Required. Parent resource name.The format of this value varies depending on the scope of the request (project or organization):

  * Projects scope: `projects/{project_id}/locations/{location_id}`
  * Organizations scope: `organizations/{org_id}/locations/{location_id}`

The following example `parent` string specifies a parent project with the identifier `example-project`, and specifies the `europe-west3` location for processing data:
    
    
    parent=projects/example-project/locations/europe-west3
    

Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `dlp.jobTriggers.create`

  
`discovery_config` |  `[DiscoveryConfig](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DiscoveryConfig)` Required. The DiscoveryConfig to create.  
`config_id` |  `string` The config ID can contain uppercase and lowercase letters, numbers, and hyphens; that is, it must match the regular expression: `[a-zA-Z\d-_]+`. The maximum length is 100 characters. Can be empty to allow the system to generate one.  
  
## CreateDlpJobRequest

Request message for CreateDlpJobRequest. Used to initiate long running jobs such as calculating risk metrics or inspecting Google Cloud Storage.

Fields  
---  
`parent` |  `string` Required. Parent resource name.The format of this value varies depending on whether you have [specified a processing location](https://docs.cloud.google.com/sensitive-data-protection/docs/specifying-location):

  * Projects scope, location specified: `projects/{project_id}/locations/{location_id}`
  * Projects scope, no location specified (defaults to global): `projects/{project_id}`

The following example `parent` string specifies a parent project with the identifier `example-project`, and specifies the `europe-west3` location for processing data:
    
    
    parent=projects/example-project/locations/europe-west3
    

Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `dlp.jobs.create`

  
`job_id` |  `string` The job id can contain uppercase and lowercase letters, numbers, and hyphens; that is, it must match the regular expression: `[a-zA-Z\d-_]+`. The maximum length is 100 characters. Can be empty to allow the system to generate one.  
`location_id` |  `string` Deprecated. This field has no effect.  
Union field `job`. The configuration details for the specific type of job to run. `job` can be only one of the following:  
`inspect_job` |  `[InspectJobConfig](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.InspectJobConfig)` An inspection job scans a storage repository for InfoTypes.  
`risk_job` |  `[RiskAnalysisJobConfig](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.RiskAnalysisJobConfig)` A risk analysis job calculates re-identification risk metrics for a BigQuery table.  
  
## CreateInspectTemplateRequest

Request message for CreateInspectTemplate.

Fields  
---  
`parent` |  `string` Required. Parent resource name.The format of this value varies depending on the scope of the request (project or organization) and whether you have [specified a processing location](https://docs.cloud.google.com/sensitive-data-protection/docs/specifying-location):

  * Projects scope, location specified: `projects/{project_id}/locations/{location_id}`
  * Projects scope, no location specified (defaults to global): `projects/{project_id}`
  * Organizations scope, location specified: `organizations/{org_id}/locations/{location_id}`
  * Organizations scope, no location specified (defaults to global): `organizations/{org_id}`

The following example `parent` string specifies a parent project with the identifier `example-project`, and specifies the `europe-west3` location for processing data:
    
    
    parent=projects/example-project/locations/europe-west3
    

Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `dlp.inspectTemplates.create`

  
`inspect_template` |  `[InspectTemplate](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.InspectTemplate)` Required. The InspectTemplate to create.  
`template_id` |  `string` The template id can contain uppercase and lowercase letters, numbers, and hyphens; that is, it must match the regular expression: `[a-zA-Z\d-_]+`. The maximum length is 100 characters. Can be empty to allow the system to generate one.  
`location_id` |  `string` Deprecated. This field has no effect.  
  
## CreateJobTriggerRequest

Request message for CreateJobTrigger.

Fields  
---  
`parent` |  `string` Required. Parent resource name.The format of this value varies depending on whether you have [specified a processing location](https://docs.cloud.google.com/sensitive-data-protection/docs/specifying-location):

  * Projects scope, location specified: `projects/{project_id}/locations/{location_id}`
  * Projects scope, no location specified (defaults to global): `projects/{project_id}`

The following example `parent` string specifies a parent project with the identifier `example-project`, and specifies the `europe-west3` location for processing data:
    
    
    parent=projects/example-project/locations/europe-west3
    

Authorization requires one or more of the following [IAM](https://cloud.google.com/iam/docs/) permissions on the specified resource `parent`:

  * `dlp.jobTriggers.create`
  * `dlp.jobs.create`

  
`job_trigger` |  `[JobTrigger](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.JobTrigger)` Required. The JobTrigger to create.  
`trigger_id` |  `string` The trigger id can contain uppercase and lowercase letters, numbers, and hyphens; that is, it must match the regular expression: `[a-zA-Z\d-_]+`. The maximum length is 100 characters. Can be empty to allow the system to generate one.  
`location_id` |  `string` Deprecated. This field has no effect.  
  
## CreateStoredInfoTypeRequest

Request message for CreateStoredInfoType.

Fields  
---  
`parent` |  `string` Required. Parent resource name.The format of this value varies depending on the scope of the request (project or organization) and whether you have [specified a processing location](https://docs.cloud.google.com/sensitive-data-protection/docs/specifying-location):

  * Projects scope, location specified: `projects/{project_id}/locations/{location_id}`
  * Projects scope, no location specified (defaults to global): `projects/{project_id}`
  * Organizations scope, location specified: `organizations/{org_id}/locations/{location_id}`
  * Organizations scope, no location specified (defaults to global): `organizations/{org_id}`

The following example `parent` string specifies a parent project with the identifier `example-project`, and specifies the `europe-west3` location for processing data:
    
    
    parent=projects/example-project/locations/europe-west3
    

Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `dlp.storedInfoType.create`

  
`config` |  `[StoredInfoTypeConfig](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.StoredInfoTypeConfig)` Required. Configuration of the storedInfoType to create.  
`stored_info_type_id` |  `string` The storedInfoType ID can contain uppercase and lowercase letters, numbers, and hyphens; that is, it must match the regular expression: `[a-zA-Z\d-_]+`. The maximum length is 100 characters. Can be empty to allow the system to generate one.  
`location_id` |  `string` Deprecated. This field has no effect.  
  
## CryptoDeterministicConfig

Pseudonymization method that generates deterministic encryption for the given input. Outputs a base64 encoded representation of the encrypted output. Uses AES-SIV based on the RFC <https://tools.ietf.org/html/rfc5297>.

Fields  
---  
`crypto_key` |  `[CryptoKey](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.CryptoKey)` The key used by the encryption function. For deterministic encryption using AES-SIV, the provided key is internally expanded to 64 bytes prior to use.  
`surrogate_info_type` |  `[InfoType](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.InfoType)` The custom info type to annotate the surrogate with. This annotation will be applied to the surrogate by prefixing it with the name of the custom info type followed by the number of characters comprising the surrogate. The following scheme defines the format: {info type name}({surrogate character count}):{surrogate}For example, if the name of custom info type is 'MY_TOKEN_INFO_TYPE' and the surrogate is 'abc', the full replacement value will be: 'MY_TOKEN_INFO_TYPE(3):abc'This annotation identifies the surrogate when inspecting content using the custom info type 'Surrogate'. This facilitates reversal of the surrogate when it occurs in free text.Note: For record transformations where the entire cell in a table is being transformed, surrogates are not mandatory. Surrogates are used to denote the location of the token and are necessary for re-identification in free form text.In order for inspection to work properly, the name of this info type must not occur naturally anywhere in your data; otherwise, inspection may either

  * reverse a surrogate that does not correspond to an actual identifier
  * be unable to parse the surrogate and result in an error

Therefore, choose your custom info type name carefully after considering what your data looks like. One way to select a name that has a high chance of yielding reliable detection is to include one or more unicode characters that are highly improbable to exist in your data. For example, assuming your data is entered from a regular ASCII keyboard, the symbol with the hex code point 29DD might be used like so: ⧝MY_TOKEN_TYPE.  
`context` |  `[FieldId](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.FieldId)` A context may be used for higher security and maintaining referential integrity such that the same identifier in two different contexts will be given a distinct surrogate. The context is appended to plaintext value being encrypted. On decryption the provided context is validated against the value used during encryption. If a context was provided during encryption, same context must be provided during decryption as well.If the context is not set, plaintext would be used as is for encryption. If the context is set but:

  1. there is no record present when transforming a given value or
  2. the field is not present when transforming a given value,

plaintext would be used as is for encryption.Note that case (1) is expected when an `InfoTypeTransformation` is applied to both structured and unstructured `ContentItem`s.  
  
## CryptoHashConfig

Pseudonymization method that generates surrogates via cryptographic hashing. Uses SHA-256. The key size must be either 32 or 64 bytes. Outputs a base64 encoded representation of the hashed output (for example, L7k0BHmF1ha5U3NfGykjro4xWi1MPVQPjhMAZbSV9mM=). Currently, only string and integer values can be hashed. See <https://docs.cloud.google.com/sensitive-data-protection/docs/pseudonymization> to learn more.

Fields  
---  
`crypto_key` |  `[CryptoKey](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.CryptoKey)` The key used by the hash function.  
  
## CryptoKey

This is a data encryption key (DEK) (as opposed to a key encryption key (KEK) stored by Cloud Key Management Service (Cloud KMS). When using Cloud KMS to wrap or unwrap a DEK, be sure to set an appropriate IAM policy on the KEK to ensure an attacker cannot unwrap the DEK.

Fields  
---  
Union field `source`. Sources of crypto keys. `source` can be only one of the following:  
`transient` |  `[TransientCryptoKey](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.TransientCryptoKey)` Transient crypto key  
`unwrapped` |  `[UnwrappedCryptoKey](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.UnwrappedCryptoKey)` Unwrapped crypto key  
`kms_wrapped` |  `[KmsWrappedCryptoKey](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.KmsWrappedCryptoKey)` Key wrapped using Cloud KMS  
  
## CryptoReplaceFfxFpeConfig

Replaces an identifier with a surrogate using Format Preserving Encryption (FPE) with the FFX mode of operation; however when used in the `ReidentifyContent` API method, it serves the opposite function by reversing the surrogate back into the original identifier. The identifier must be encoded as ASCII. For a given crypto key and context, the same identifier will be replaced with the same surrogate. Identifiers must be at least two characters long. In the case that the identifier is the empty string, it will be skipped. See <https://docs.cloud.google.com/sensitive-data-protection/docs/pseudonymization> to learn more.

Note: We recommend using CryptoDeterministicConfig for all use cases which do not require preserving the input alphabet space and size, plus warrant referential integrity. FPE incurs significant latency costs.

Fields  
---  
`crypto_key` |  `[CryptoKey](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.CryptoKey)` Required. The key used by the encryption algorithm.  
`context` |  `[FieldId](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.FieldId)` The 'tweak', a context may be used for higher security since the same identifier in two different contexts won't be given the same surrogate. If the context is not set, a default tweak will be used.If the context is set but:

  1. there is no record present when transforming a given value or
  2. the field is not present when transforming a given value,

a default tweak will be used.Note that case (1) is expected when an `InfoTypeTransformation` is applied to both structured and unstructured `ContentItem`s. Currently, the referenced field may be of value type integer or string.The tweak is constructed as a sequence of bytes in big endian byte order such that:

  * a 64 bit integer is encoded followed by a single byte of value 1
  * a string is encoded in UTF-8 format followed by a single byte of value 2

  
`surrogate_info_type` |  `[InfoType](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.InfoType)` The custom infoType to annotate the surrogate with. This annotation will be applied to the surrogate by prefixing it with the name of the custom infoType followed by the number of characters comprising the surrogate. The following scheme defines the format: info_type_name(surrogate_character_count):surrogateFor example, if the name of custom infoType is 'MY_TOKEN_INFO_TYPE' and the surrogate is 'abc', the full replacement value will be: 'MY_TOKEN_INFO_TYPE(3):abc'This annotation identifies the surrogate when inspecting content using the custom infoType [`SurrogateType`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectConfig#surrogatetype). This facilitates reversal of the surrogate when it occurs in free text.In order for inspection to work properly, the name of this infoType must not occur naturally anywhere in your data; otherwise, inspection may find a surrogate that does not correspond to an actual identifier. Therefore, choose your custom infoType name carefully after considering what your data looks like. One way to select a name that has a high chance of yielding reliable detection is to include one or more unicode characters that are highly improbable to exist in your data. For example, assuming your data is entered from a regular ASCII keyboard, the symbol with the hex code point 29DD might be used like so: ⧝MY_TOKEN_TYPE  
Union field `alphabet`. Choose an alphabet which the data being transformed will be made up of. `alphabet` can be only one of the following:  
`common_alphabet` |  `[FfxCommonNativeAlphabet](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.CryptoReplaceFfxFpeConfig.FfxCommonNativeAlphabet)` Common alphabets.  
`custom_alphabet` |  `string` This is supported by mapping these to the alphanumeric characters that the FFX mode natively supports. This happens before/after encryption/decryption. Each character listed must appear only once. Number of characters must be in the range [2, 95]. This must be encoded as ASCII. The order of characters does not matter. The full list of allowed characters is: `0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz~`!@#$%^&*()_-+={[}]|\:;"'<,>.?/`  
`radix` |  `int32` The native way to select the alphabet. Must be in the range [2, 95].  
  
## FfxCommonNativeAlphabet

These are commonly used subsets of the alphabet that the FFX mode natively supports. In the algorithm, the alphabet is selected using the "radix". Therefore each corresponds to a particular radix.

Enums  
---  
`FFX_COMMON_NATIVE_ALPHABET_UNSPECIFIED` | Unused.  
`NUMERIC` | `[0-9]` (radix of 10)  
`HEXADECIMAL` | `[0-9A-F]` (radix of 16)  
`UPPER_CASE_ALPHA_NUMERIC` | `[0-9A-Z]` (radix of 36)  
`ALPHA_NUMERIC` | `[0-9A-Za-z]` (radix of 62)  
  
## CustomInfoType

Custom information type provided by the user. Used to find domain-specific sensitive information configurable to the data in question.

Fields  
---  
`info_type` |  `[InfoType](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.InfoType)` CustomInfoType can either be a new infoType, or an extension of built-in infoType, when the name matches one of existing infoTypes and that infoType is specified in `InspectContent.info_types` field. Specifying the latter adds findings to the one detected by the system. If built-in info type is not specified in `InspectContent.info_types` list then the name is treated as a custom info type.  
`likelihood` |  `[Likelihood](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.Likelihood)` Likelihood to return for this CustomInfoType. This base value can be altered by a detection rule if the finding meets the criteria specified by the rule. Defaults to `VERY_LIKELY` if not specified.  
`detection_rules[]` |  `[DetectionRule](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.CustomInfoType.DetectionRule)` Set of detection rules to apply to all findings of this CustomInfoType. Rules are applied in the order that they are specified. Only supported for the `dictionary`, `regex`, and `stored_type` CustomInfoTypes.  
`exclusion_type` |  `[ExclusionType](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.CustomInfoType.ExclusionType)` If set to EXCLUSION_TYPE_EXCLUDE this infoType will not cause a finding to be returned. It still can be used for rules matching. Only supported for the `dictionary`, `regex`, and `stored_type` CustomInfoTypes.  
`sensitivity_score` |  `[SensitivityScore](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.SensitivityScore)` Sensitivity for this CustomInfoType. If this CustomInfoType extends an existing InfoType, the sensitivity here will take precedence over that of the original InfoType. If unset for a CustomInfoType, it will default to HIGH. This only applies to data profiling.  
Union field `type`. Type of custom detector. `type` can be only one of the following:  
`dictionary` |  `[Dictionary](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.CustomInfoType.Dictionary)` A list of phrases to detect as a CustomInfoType.  
`regex` |  `[Regex](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.CustomInfoType.Regex)` Regular expression based CustomInfoType.  
`surrogate_type` |  `[SurrogateType](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.CustomInfoType.SurrogateType)` Message for detecting output from deidentification transformations that support reversing.  
`stored_type` |  `[StoredType](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.StoredType)` Loads an existing `StoredInfoType` resource.  
`metadata_key_value_expression` |  `[MetadataKeyValueExpression](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.CustomInfoType.MetadataKeyValueExpression)` Key-value pair to detect in the metadata.  
`file_label_info_type` |  `[FileLabelInfoType](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.CustomInfoType.FileLabelInfoType)` File label to detect.  
  
## DetectionRule

Deprecated; use `InspectionRuleSet` instead. Rule for modifying a `CustomInfoType` to alter behavior under certain circumstances, depending on the specific details of the rule. Not supported for the `surrogate_type` custom infoType.

Fields  
---  
Union field `type`. Type of hotword rule. `type` can be only one of the following:  
`hotword_rule` |  `[HotwordRule](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.CustomInfoType.DetectionRule.HotwordRule)` Hotword-based detection rule.  
  
## HotwordRule

The rule that adjusts the likelihood of findings within a certain proximity of hotwords.

Fields  
---  
`hotword_regex` |  `[Regex](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.CustomInfoType.Regex)` Regular expression pattern defining what qualifies as a hotword.  
`proximity` |  `[Proximity](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.CustomInfoType.DetectionRule.Proximity)` Range of characters within which the entire hotword must reside. The total length of the window cannot exceed 1000 characters. The finding itself will be included in the window, so that hotwords can be used to match substrings of the finding itself. Suppose you want Cloud DLP to promote the likelihood of the phone number regex "(\d{3}) \d{3}-\d{4}" if the area code is known to be the area code of a company's office. In this case, use the hotword regex "(xxx)", where "xxx" is the area code in question.For tabular data, if you want to modify the likelihood of an entire column of findngs, see [Hotword example: Set the match likelihood of a table column](https://docs.cloud.google.com/sensitive-data-protection/docs/creating-custom-infotypes-likelihood#match-column-values).  
`likelihood_adjustment` |  `[LikelihoodAdjustment](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.CustomInfoType.DetectionRule.LikelihoodAdjustment)` Likelihood adjustment to apply to all matching findings.  
  
## LikelihoodAdjustment

Message for specifying an adjustment to the likelihood of a finding as part of a detection rule.

Fields  
---  
Union field `adjustment`. How the likelihood will be modified. `adjustment` can be only one of the following:  
`fixed_likelihood` |  `[Likelihood](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.Likelihood)` Set the likelihood of a finding to a fixed value.  
`relative_likelihood` |  `int32` Increase or decrease the likelihood by the specified number of levels. For example, if a finding would be `POSSIBLE` without the detection rule and `relative_likelihood` is 1, then it is upgraded to `LIKELY`, while a value of -1 would downgrade it to `UNLIKELY`. Likelihood may never drop below `VERY_UNLIKELY` or exceed `VERY_LIKELY`, so applying an adjustment of 1 followed by an adjustment of -1 when base likelihood is `VERY_LIKELY` will result in a final likelihood of `LIKELY`.  
  
## Proximity

Message for specifying a window around a finding to apply a detection rule.

Fields  
---  
`window_before` |  `int32` Number of characters before the finding to consider. For tabular data, if you want to modify the likelihood of an entire column of findngs, set this to 1. For more information, see [Hotword example: Set the match likelihood of a table column](https://docs.cloud.google.com/sensitive-data-protection/docs/creating-custom-infotypes-likelihood#match-column-values).  
`window_after` |  `int32` Number of characters after the finding to consider.  
  
## Dictionary

Custom information type based on a dictionary of words or phrases. This can be used to match sensitive information specific to the data, such as a list of employee IDs or job titles.

Dictionary words are case-insensitive and all characters other than letters and digits in the unicode [Basic Multilingual Plane](https://en.wikipedia.org/wiki/Plane_%28Unicode%29#Basic_Multilingual_Plane) will be replaced with whitespace when scanning for matches, so the dictionary phrase "Sam Johnson" will match all three phrases "sam johnson", "Sam, Johnson", and "Sam (Johnson)". Additionally, the characters surrounding any match must be of a different type than the adjacent characters within the word, so letters must be next to non-letters and digits next to non-digits. For example, the dictionary word "jen" will match the first three letters of the text "jen123" but will return no matches for "jennifer".

Dictionary words containing a large number of characters that are not letters or digits may result in unexpected findings because such characters are treated as whitespace. The [limits](https://docs.cloud.google.com/sensitive-data-protection/limits) page contains details about the size limits of dictionaries. For dictionaries that do not fit within these constraints, consider using `LargeCustomDictionaryConfig` in the `StoredInfoType` API.

Fields  
---  
Union field `source`. The potential places the data can be read from. `source` can be only one of the following:  
`word_list` |  `[WordList](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.CustomInfoType.Dictionary.WordList)` List of words or phrases to search for.  
`cloud_storage_path` |  `[CloudStoragePath](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.CloudStoragePath)` Newline-delimited file of words in Cloud Storage. Only a single file is accepted.  
  
## WordList

Message defining a list of words or phrases to search for in the data.

Fields  
---  
`words[]` |  `string` Words or phrases defining the dictionary. The dictionary must contain at least one phrase and every phrase must contain at least 2 characters that are letters or digits. [required]  
  
## ExclusionType

Type of exclusion rule.

Enums  
---  
`EXCLUSION_TYPE_UNSPECIFIED` | A finding of this custom info type will not be excluded from results.  
`EXCLUSION_TYPE_EXCLUDE` | A finding of this custom info type will be excluded from final results, but can still affect rule execution.  
  
## FileLabelInfoType

Configuration for a custom infoType that detects file labels.

Fields  
---  
Union field `type`. The type of file label to detect. `type` can be only one of the following:  
`sensitivity_label` |  `[SensitivityLabel](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.CustomInfoType.FileLabelInfoType.SensitivityLabel)` Sensitivity labels published by Microsoft.  
`google_drive_label` |  `[GoogleDriveLabel](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.CustomInfoType.FileLabelInfoType.GoogleDriveLabel)` Google Drive labels published by Google.  
  
## GoogleDriveLabel

Google Drive labels published by Google.

Fields  
---  
`label_id` |  `string` The [label ID](https://developers.google.com/workspace/drive/labels/guides/overview) of the Google Drive label.  
`label_fields_to_match[]` |  `[LabelField](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.CustomInfoType.FileLabelInfoType.GoogleDriveLabel.LabelField)` The field values of the Google Drive label to match.  
  
## LabelField

The field values of the Google Drive label to match.

Fields  
---  
`id` |  `string` The identifier of the Label Field.  
`value` |  `string` The value of the Label Field to match.  
  
## SensitivityLabel

Sensitivity labels published by Microsoft.

Fields  
---  
`guid` |  `string` The GUID of the sensitivity label.  
  
## MetadataKeyValueExpression

Configuration for a custom infoType that detects key-value pairs in the metadata matching the specified regular expressions.

Fields  
---  
`key_regex` |  `string` The regular expression for the key. Key should be non-empty.  
`value_regex` |  `string` The regular expression for the value. Value should be non-empty.  
  
## Regex

Message defining a custom regular expression.

Fields  
---  
`pattern` |  `string` Pattern defining the regular expression. Its syntax (<https://github.com/google/re2/wiki/Syntax>) can be found under the google/re2 repository on GitHub.  
`group_indexes[]` |  `int32` The index of the submatch to extract as findings. When not specified, the entire match is returned. No more than 3 may be included.  
  
## SurrogateType

This type has no fields.

Message for detecting output from deidentification transformations such as [`CryptoReplaceFfxFpeConfig`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.deidentifyTemplates#cryptoreplaceffxfpeconfig). These types of transformations are those that perform pseudonymization, thereby producing a "surrogate" as output. This should be used in conjunction with a field on the transformation such as `surrogate_info_type`. This CustomInfoType does not support the use of `detection_rules`.

## DataProfileAction

A task to execute when a data profile has been generated.

Fields  
---  
Union field `action`. Type of action to execute when a profile is generated. `action` can be only one of the following:  
`export_data` |  `[Export](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DataProfileAction.Export)` Export data profiles into a provided location.  
`pub_sub_notification` |  `[PubSubNotification](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DataProfileAction.PubSubNotification)` Publish a message into the Pub/Sub topic.  
`publish_to_chronicle` |  `[PublishToChronicle](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DataProfileAction.PublishToChronicle)` Publishes generated data profiles to Google Security Operations. For more information, see [Use Sensitive Data Protection data in context-aware analytics](https://docs.cloud.google.com/chronicle/docs/detection/usecase-dlp-high-risk-user-download).  
`publish_to_scc` |  `[PublishToSecurityCommandCenter](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DataProfileAction.PublishToSecurityCommandCenter)` Publishes findings to Security Command Center for each data profile.  
`tag_resources` |  `[TagResources](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DataProfileAction.TagResources)` Tags the profiled resources with the specified tag values.  
`publish_to_dataplex_catalog` |  `[PublishToDataplexCatalog](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DataProfileAction.PublishToDataplexCatalog)` Publishes a portion of each profile to Dataplex Universal Catalog with the aspect type Sensitive Data Protection Profile.  
  
## EventType

Types of event that can trigger an action.

Enums  
---  
`EVENT_TYPE_UNSPECIFIED` | Unused.  
`NEW_PROFILE` | New profile (not a re-profile).  
`CHANGED_PROFILE` | One of the following profile metrics changed: Data risk score, Sensitivity score, Resource visibility, Encryption type, Predicted infoTypes, Other infoTypes  
`SCORE_INCREASED` | Table data risk score or sensitivity score increased.  
`ERROR_CHANGED` | A user (non-internal) error occurred.  
  
## Export

If set, the detailed data profiles will be persisted to the location of your choice whenever updated.

Fields  
---  
`profile_table` |  `[BigQueryTable](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.BigQueryTable)` Store all profiles to BigQuery.

  * The system will create a new dataset and table for you if none are are provided. The dataset will be named `sensitive_data_protection_discovery` and table will be named `discovery_profiles`. This table will be placed in the same project as the container project running the scan. After the first profile is generated and the dataset and table are created, the discovery scan configuration will be updated with the dataset and table names.
  * See [Analyze data profiles stored in BigQuery](https://docs.cloud.google.com/sensitive-data-protection/docs/analyze-data-profiles).
  * See [Sample queries for your BigQuery table](https://docs.cloud.google.com/sensitive-data-protection/docs/analyze-data-profiles#sample_sql_queries).
  * Data is inserted using [streaming insert](https://cloud.google.com/blog/products/bigquery/life-of-a-bigquery-streaming-insert) and so data may be in the buffer for a period of time after the profile has finished.
  * The Pub/Sub notification is sent before the streaming buffer is guaranteed to be written, so data may not be instantly visible to queries by the time your topic receives the Pub/Sub notification.
  * The best practice is to use the same table for an entire organization so that you can take advantage of the [provided Data Studio reports](https://docs.cloud.google.com/sensitive-data-protection/docs/analyze-data-profiles#use_a_premade_report). If you use VPC Service Controls to define security perimeters, then you must use a separate table for each boundary.

  
`sample_findings_table` |  `[BigQueryTable](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.BigQueryTable)` Store sample `[data profile findings](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DataProfileFinding)` in an existing table or a new table in an existing dataset. Each regeneration will result in new rows in BigQuery. Data is inserted using [streaming insert](https://cloud.google.com/blog/products/bigquery/life-of-a-bigquery-streaming-insert) and so data may be in the buffer for a period of time after the profile has finished.  
  
## PubSubNotification

Send a Pub/Sub message into the given Pub/Sub topic to connect other systems to data profile generation. The message payload data will be the byte serialization of `DataProfilePubSubMessage`.

Fields  
---  
`topic` |  `string` Cloud Pub/Sub topic to send notifications to. Format is projects/{project}/topics/{topic}.  
`event` |  `[EventType](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DataProfileAction.EventType)` The type of event that triggers a Pub/Sub. At most one `PubSubNotification` per EventType is permitted.  
`pubsub_condition` |  `[DataProfilePubSubCondition](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DataProfilePubSubCondition)` Conditions (e.g., data risk or sensitivity level) for triggering a Pub/Sub.  
`detail_of_message` |  `[DetailLevel](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DataProfileAction.PubSubNotification.DetailLevel)` How much data to include in the Pub/Sub message. If the user wishes to limit the size of the message, they can use resource_name and fetch the profile fields they wish to. Per table profile (not per column).  
  
## DetailLevel

The levels of detail that can be included in the Pub/Sub message.

Enums  
---  
`DETAIL_LEVEL_UNSPECIFIED` | Unused.  
`TABLE_PROFILE` | The full table data profile.  
`RESOURCE_NAME` | The name of the profiled resource.  
`FILE_STORE_PROFILE` | The full file store data profile.  
  
## PublishToChronicle

This type has no fields.

Message expressing intention to publish to Google Security Operations.

## PublishToDataplexCatalog

Create Dataplex Universal Catalog aspects for profiled resources with the aspect type Sensitive Data Protection Profile. To learn more about aspects, see <https://docs.cloud.google.com/sensitive-data-protection/docs/add-aspects>.

Fields  
---  
`lower_data_risk_to_low` |  `bool` Whether creating a Dataplex Universal Catalog aspect for a profiled resource should lower the risk of the profile for that resource. This also lowers the data risk of resources at the lower levels of the resource hierarchy. For example, reducing the data risk of a table data profile also reduces the data risk of the constituent column data profiles.  
  
## PublishToSecurityCommandCenter

This type has no fields.

If set, a summary finding will be created or updated in Security Command Center for each profile.

## TagResources

If set, attaches the [tags](https://docs.cloud.google.com/resource-manager/docs/tags/tags-overview) provided to profiled resources. Tags support [access control](https://docs.cloud.google.com/iam/docs/tags-access-control). You can conditionally grant or deny access to a resource based on whether the resource has a specific tag.

Fields  
---  
`tag_conditions[]` |  `[TagCondition](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DataProfileAction.TagResources.TagCondition)` The tags to associate with different conditions.  
`profile_generations_to_tag[]` |  `[ProfileGeneration](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ProfileGeneration)` The profile generations for which the tag should be attached to resources. If you attach a tag to only new profiles, then if the sensitivity score of a profile subsequently changes, its tag doesn't change. By default, this field includes only new profiles. To include both new and updated profiles for tagging, this field should explicitly include both `PROFILE_GENERATION_NEW` and `PROFILE_GENERATION_UPDATE`.  
`lower_data_risk_to_low` |  `bool` Whether applying a tag to a resource should lower the risk of the profile for that resource. For example, in conjunction with an [IAM deny policy](https://docs.cloud.google.com/iam/docs/deny-overview), you can deny all principals a permission if a tag value is present, mitigating the risk of the resource. This also lowers the data risk of resources at the lower levels of the resource hierarchy. For example, reducing the data risk of a table data profile also reduces the data risk of the constituent column data profiles.  
  
## TagCondition

The tag to attach to profiles matching the condition. At most one `TagCondition` can be specified per sensitivity level.

Fields  
---  
`tag` |  `[TagValue](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DataProfileAction.TagResources.TagValue)` The tag value to attach to resources.  
Union field `type`. The type of condition on which attaching the tag will be predicated. `type` can be only one of the following:  
`sensitivity_score` |  `[SensitivityScore](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.SensitivityScore)` Conditions attaching the tag to a resource on its profile having this sensitivity score.  
  
## TagValue

A value of a tag.

Fields  
---  
Union field `format`. The format of the tag value. `format` can be only one of the following:  
`namespaced_value` |  `string` The namespaced name for the tag value to attach to resources. Must be in the format `{parent_id}/{tag_key_short_name}/{short_name}`, for example, "123456/environment/prod" for an organization parent, or "my-project/environment/prod" for a project parent.  
  
## DataProfileBigQueryRowSchema

The schema of data to be saved to the BigQuery table when the `DataProfileAction` is enabled.

Fields  
---  
Union field `data_profile`. Data profile type. `data_profile` can be only one of the following:  
`table_profile` |  `[TableDataProfile](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.TableDataProfile)` Table data profile column  
`column_profile` |  `[ColumnDataProfile](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ColumnDataProfile)` Column data profile column  
`file_store_profile` |  `[FileStoreDataProfile](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.FileStoreDataProfile)` File store data profile column.  
  
## DataProfileConfigSnapshot

Snapshot of the configurations used to generate the profile.

Fields  
---  
`inspect_config` |  `[InspectConfig](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.InspectConfig)` A copy of the inspection config used to generate this profile. This is a copy of the inspect_template specified in `DataProfileJobConfig`.  
`data_profile_job  
**(deprecated)**` |  `[DataProfileJobConfig](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DataProfileJobConfig)` This item is deprecated!A copy of the configuration used to generate this profile. This is deprecated, and the DiscoveryConfig field is preferred moving forward. DataProfileJobConfig will still be written here for Discovery in BigQuery for backwards compatibility, but will not be updated with new fields, while DiscoveryConfig will.  
`discovery_config` |  `[DiscoveryConfig](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DiscoveryConfig)` A copy of the configuration used to generate this profile.  
`inspect_template_name` |  `string` Name of the inspection template used to generate this profile  
`inspect_template_modified_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Timestamp when the template was modified  
  
## DataProfileFinding

Details about a piece of potentially sensitive information that was detected when the data resource was profiled.

Fields  
---  
`quote` |  `string` The content that was found. Even if the content is not textual, it may be converted to a textual representation here. If the finding exceeds 4096 bytes in length, the quote may be omitted.  
`infotype` |  `[InfoType](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.InfoType)` The [type of content](https://docs.cloud.google.com/sensitive-data-protection/docs/infotypes-reference) that might have been found.  
`quote_info` |  `[QuoteInfo](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.QuoteInfo)` Contains data parsed from quotes. Currently supported infoTypes: DATE, DATE_OF_BIRTH, and TIME.  
`data_profile_resource_name` |  `string` Resource name of the data profile associated with the finding.  
`finding_id` |  `string` A unique identifier for the finding.  
`timestamp` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Timestamp when the finding was detected.  
`location` |  `[DataProfileFindingLocation](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DataProfileFindingLocation)` Where the content was found.  
`resource_visibility` |  `[ResourceVisibility](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ResourceVisibility)` How broadly a resource has been shared.  
`full_resource_name` |  `string` The [full resource name](https://cloud.google.com/apis/design/resource_names#full_resource_name) of the resource profiled for this finding.  
`data_source_type` |  `[DataSourceType](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DataSourceType)` The type of the resource that was profiled.  
  
## DataProfileFindingLocation

Location of a data profile finding within a resource.

Fields  
---  
`container_name` |  `string` Name of the container where the finding is located. The top-level name is the source file name or table name. Names of some common storage containers are formatted as follows:

  * BigQuery tables: `{project_id}:{dataset_id}.{table_id}`
  * Cloud Storage files: `gs://{bucket}/{path}`

  
Union field `location_extra_details`. Additional location details that may be provided for some types of profiles. At this time, only findings for table data profiles include such details. `location_extra_details` can be only one of the following:  
`data_profile_finding_record_location` |  `[DataProfileFindingRecordLocation](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DataProfileFindingRecordLocation)` Location of a finding within a resource that produces a table data profile.  
  
## DataProfileFindingRecordLocation

Location of a finding within a resource that produces a table data profile.

Fields  
---  
`field` |  `[FieldId](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.FieldId)` Field ID of the column containing the finding.  
  
## DataProfileJobConfig

Configuration for setting up a job to scan resources for profile generation. Only one data profile configuration may exist per organization, folder, or project.

The generated data profiles are retained according to the [data retention policy](https://docs.cloud.google.com/sensitive-data-protection/docs/data-profiles#retention).

Fields  
---  
`location` |  `[DataProfileLocation](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DataProfileLocation)` The data to scan.  
`project_id` |  `string` The project that will run the scan. The DLP service account that exists within this project must have access to all resources that are profiled, and the DLP API must be enabled.  
`other_cloud_starting_location` |  `[OtherCloudDiscoveryStartingLocation](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.OtherCloudDiscoveryStartingLocation)` Must be set only when scanning other clouds.  
`inspect_templates[]` |  `string` Detection logic for profile generation.Not all template features are used by profiles. FindingLimits, include_quote and exclude_info_types have no impact on data profiling.Multiple templates may be provided if there is data in multiple regions. At most one template must be specified per-region (including "global"). Each region is scanned using the applicable template. If no region-specific template is specified, but a "global" template is specified, it will be copied to that region and used instead. If no global or region-specific template is provided for a region with data, that region's data will not be scanned.For more information, see <https://docs.cloud.google.com/sensitive-data-protection/docs/data-profiles#data-residency>.  
`data_profile_actions[]` |  `[DataProfileAction](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DataProfileAction)` Actions to execute at the completion of the job.  
  
## DataProfileLocation

The data that will be profiled.

Fields  
---  
Union field `location`. The location to be scanned. `location` can be only one of the following:  
`organization_id` |  `int64` The ID of an organization to scan.  
`folder_id` |  `int64` The ID of the folder within an organization to scan.  
  
## DataProfilePubSubCondition

A condition for determining whether a Pub/Sub should be triggered.

Fields  
---  
`expressions` |  `[PubSubExpressions](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DataProfilePubSubCondition.PubSubExpressions)` An expression.  
  
## ProfileScoreBucket

Various score levels for resources.

Enums  
---  
`PROFILE_SCORE_BUCKET_UNSPECIFIED` | Unused.  
`HIGH` | High risk/sensitivity detected.  
`MEDIUM_OR_HIGH` | Medium or high risk/sensitivity detected.  
  
## PubSubCondition

A condition consisting of a value.

Fields  
---  
Union field `value`. The value for the condition to trigger. `value` can be only one of the following:  
`minimum_risk_score` |  `[ProfileScoreBucket](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DataProfilePubSubCondition.ProfileScoreBucket)` The minimum data risk score that triggers the condition.  
`minimum_sensitivity_score` |  `[ProfileScoreBucket](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DataProfilePubSubCondition.ProfileScoreBucket)` The minimum sensitivity level that triggers the condition.  
  
## PubSubExpressions

An expression, consisting of an operator and conditions.

Fields  
---  
`logical_operator` |  `[PubSubLogicalOperator](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DataProfilePubSubCondition.PubSubExpressions.PubSubLogicalOperator)` The operator to apply to the collection of conditions.  
`conditions[]` |  `[PubSubCondition](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DataProfilePubSubCondition.PubSubCondition)` Conditions to apply to the expression.  
  
## PubSubLogicalOperator

Logical operators for conditional checks.

Enums  
---  
`LOGICAL_OPERATOR_UNSPECIFIED` | Unused.  
`OR` | Conditional OR.  
`AND` | Conditional AND.  
  
## DataProfilePubSubMessage

Pub/Sub topic message for a DataProfileAction.PubSubNotification event. To receive a message of protocol buffer schema type, convert the message data to an object of this proto class.

Fields  
---  
`profile` |  `[TableDataProfile](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.TableDataProfile)` If `DetailLevel` is `TABLE_PROFILE` this will be fully populated. Otherwise, if `DetailLevel` is `RESOURCE_NAME`, then only `name` and `full_resource` will be populated.  
`file_store_profile` |  `[FileStoreDataProfile](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.FileStoreDataProfile)` If `DetailLevel` is `FILE_STORE_PROFILE` this will be fully populated. Otherwise, if `DetailLevel` is `RESOURCE_NAME`, then only `name` and `file_store_path` will be populated.  
`event` |  `[EventType](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DataProfileAction.EventType)` The event that caused the Pub/Sub message to be sent.  
  
## DataProfileUpdateFrequency

How frequently data profiles can be updated. New options can be added at a later time.

Enums  
---  
`UPDATE_FREQUENCY_UNSPECIFIED` | Unspecified.  
`UPDATE_FREQUENCY_NEVER` | After the data profile is created, it will never be updated.  
`UPDATE_FREQUENCY_DAILY` | The data profile can be updated up to once every 24 hours.  
`UPDATE_FREQUENCY_MONTHLY` | The data profile can be updated up to once every 30 days. Default.  
  
## DataRiskLevel

Score is a summary of all elements in the data profile. A higher number means more risk.

Fields  
---  
`score` |  `[DataRiskLevelScore](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DataRiskLevel.DataRiskLevelScore)` The score applied to the resource.  
  
## DataRiskLevelScore

Various score levels for resources.

Enums  
---  
`RISK_SCORE_UNSPECIFIED` | Unused.  
`RISK_LOW` | Low risk - Lower indication of sensitive data that appears to have additional access restrictions in place or no indication of sensitive data found.  
`RISK_UNKNOWN` | Unable to determine risk.  
`RISK_MODERATE` | Medium risk - Sensitive data may be present but additional access or fine grain access restrictions appear to be present. Consider limiting access even further or transform data to mask.  
`RISK_HIGH` | High risk – SPII may be present. Access controls may include public ACLs. Exfiltration of data may lead to user data loss. Re-identification of users may be possible. Consider limiting usage and or removing SPII.  
  
## DataSourceType

Message used to identify the type of resource being profiled.

Fields  
---  
`data_source` |  `string` A string that identifies the type of resource being profiled. Current values:

  * google/bigquery/table
  * google/project
  * google/sql/table
  * google/gcs/bucket

  
  
## DatabaseResourceCollection

Match database resources using regex filters. Examples of database resources are tables, views, and stored procedures.

Fields  
---  
Union field `pattern`. The first filter containing a pattern that matches a database resource will be used. `pattern` can be only one of the following:  
`include_regexes` |  `[DatabaseResourceRegexes](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DatabaseResourceRegexes)` A collection of regular expressions to match a database resource against.  
  
## DatabaseResourceReference

Identifies a single database resource, like a table within a database.

Fields  
---  
`project_id` |  `string` Required. If within a project-level config, then this must match the config's project ID.  
`instance` |  `string` Required. The instance where this resource is located. For example: Cloud SQL instance ID.  
`database` |  `string` Required. Name of a database within the instance.  
`database_resource` |  `string` Required. Name of a database resource, for example, a table within the database.  
  
## DatabaseResourceRegex

A pattern to match against one or more database resources. At least one pattern must be specified. Regular expressions use RE2 [syntax](https://github.com/google/re2/wiki/Syntax); a guide can be found under the google/re2 repository on GitHub.

Fields  
---  
`project_id_regex` |  `string` For organizations, if unset, will match all projects. Has no effect for configurations created within a project.  
`instance_regex` |  `string` Regex to test the instance name against. If empty, all instances match.  
`database_regex` |  `string` Regex to test the database name against. If empty, all databases match.  
`database_resource_name_regex` |  `string` Regex to test the database resource's name against. An example of a database resource name is a table's name. Other database resource names like view names could be included in the future. If empty, all database resources match.  
  
## DatabaseResourceRegexes

A collection of regular expressions to determine what database resources to match against.

Fields  
---  
`patterns[]` |  `[DatabaseResourceRegex](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DatabaseResourceRegex)` A group of regular expression patterns to match against one or more database resources. Maximum of 100 entries. The sum of all regular expression's length can't exceed 10 KiB.  
  
## DatastoreKey

Record key for a finding in Cloud Datastore.

Fields  
---  
`entity_key` |  `[Key](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.Key)` Datastore entity key.  
  
## DatastoreOptions

Options defining a data set within Google Cloud Datastore.

Fields  
---  
`partition_id` |  `[PartitionId](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.PartitionId)` A partition ID identifies a grouping of entities. The grouping is always by project and namespace, however the namespace ID may be empty.  
`kind` |  `[KindExpression](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.KindExpression)` The kind to process.  
  
## DateShiftConfig

Shifts dates by random number of days, with option to be consistent for the same context. See <https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-date-shifting> to learn more.

Fields  
---  
`upper_bound_days` |  `int32` Required. Range of shift in days. Actual shift will be selected at random within this range (inclusive ends). Negative means shift to earlier in time. Must not be more than 365250 days (1000 years) each direction.For example, 3 means shift date to at most 3 days into the future.  
`lower_bound_days` |  `int32` Required. For example, -5 means shift date to at most 5 days back in the past.  
`context` |  `[FieldId](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.FieldId)` Points to the field that contains the context, for example, an entity id. If set, must also set cryptoKey. If set, shift will be consistent for the given context.  
Union field `method`. Method for calculating shift that takes context into consideration. If set, must also set context. Can only be applied to table items. `method` can be only one of the following:  
`crypto_key` |  `[CryptoKey](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.CryptoKey)` Causes the shift to be computed based on this key and the context. This results in the same shift for the same context and crypto_key. If set, must also set context. Can only be applied to table items.  
  
## DateTime

Message for a date time object. e.g. 2018-01-01, 5th August.

Fields  
---  
`date` |  `[Date](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.type#google.type.Date)` One or more of the following must be set. Must be a valid date or time value.  
`day_of_week` |  `[DayOfWeek](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.type#google.type.DayOfWeek)` Day of week  
`time` |  `[TimeOfDay](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.type#google.type.TimeOfDay)` Time of day  
`time_zone` |  `[TimeZone](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DateTime.TimeZone)` Time zone  
  
## TimeZone

Time zone of the date time object.

Fields  
---  
`offset_minutes` |  `int32` Set only if the offset can be determined. Positive for time ahead of UTC. E.g. For "UTC-9", this value is -540.  
  
## DeidentifyConfig

The configuration that controls how the data will change.

Fields  
---  
`transformation_error_handling` |  `[TransformationErrorHandling](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.TransformationErrorHandling)` Mode for handling transformation errors. If left unspecified, the default mode is `TransformationErrorHandling.ThrowError`.  
Union field `transformation`. Type of transformation `transformation` can be only one of the following:  
`info_type_transformations` |  `[InfoTypeTransformations](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.InfoTypeTransformations)` Treat the dataset as free-form text and apply the same free text transformation everywhere.  
`record_transformations` |  `[RecordTransformations](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.RecordTransformations)` Treat the dataset as structured. Transformations can be applied to specific locations within structured datasets, such as transforming a column within a table.  
`image_transformations` |  `[ImageTransformations](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ImageTransformations)` Treat the dataset as an image and redact.  
  
## DeidentifyContentRequest

Request to de-identify a ContentItem.

Fields  
---  
`parent` |  `string` Parent resource name.The format of this value varies depending on whether you have [specified a processing location](https://docs.cloud.google.com/sensitive-data-protection/docs/specifying-location):

  * Projects scope, location specified: `projects/{project_id}/locations/{location_id}`
  * Projects scope, no location specified (defaults to global): `projects/{project_id}`

The following example `parent` string specifies a parent project with the identifier `example-project`, and specifies the `europe-west3` location for processing data:
    
    
    parent=projects/example-project/locations/europe-west3
    

Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `serviceusage.services.use`

  
`deidentify_config` |  `[DeidentifyConfig](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DeidentifyConfig)` Configuration for the de-identification of the content item. Items specified here will override the template referenced by the deidentify_template_name argument.  
`inspect_config` |  `[InspectConfig](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.InspectConfig)` Configuration for the inspector. Items specified here will override the template referenced by the inspect_template_name argument.  
`item` |  `[ContentItem](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ContentItem)` The item to de-identify. Will be treated as text.This value must be of type `[Table](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.Table)` if your `[deidentify_config](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DeidentifyContentRequest.FIELDS.google.privacy.dlp.v2.DeidentifyConfig.google.privacy.dlp.v2.DeidentifyContentRequest.deidentify_config)` is a `[RecordTransformations](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.RecordTransformations)` object.  
`inspect_template_name` |  `string` Template to use. Any configuration directly specified in inspect_config will override those set in the template. Singular fields that are set in this request will replace their corresponding fields in the template. Repeated fields are appended. Singular sub-messages and groups are recursively merged.  
`deidentify_template_name` |  `string` Template to use. Any configuration directly specified in deidentify_config will override those set in the template. Singular fields that are set in this request will replace their corresponding fields in the template. Repeated fields are appended. Singular sub-messages and groups are recursively merged.  
`location_id` |  `string` Deprecated. This field has no effect.  
  
## DeidentifyContentResponse

Results of de-identifying a ContentItem.

Fields  
---  
`item` |  `[ContentItem](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ContentItem)` The de-identified item.  
`overview` |  `[TransformationOverview](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.TransformationOverview)` An overview of the changes that were made on the `item`.  
  
## DeidentifyDataSourceDetails

The results of a `[Deidentify](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.Action.Deidentify)` action from an inspect job.

Fields  
---  
`requested_options` |  `[RequestedDeidentifyOptions](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DeidentifyDataSourceDetails.RequestedDeidentifyOptions)` De-identification config used for the request.  
`deidentify_stats` |  `[DeidentifyDataSourceStats](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DeidentifyDataSourceStats)` Stats about the de-identification operation.  
  
## RequestedDeidentifyOptions

De-identification options.

Fields  
---  
`snapshot_deidentify_template` |  `[DeidentifyTemplate](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DeidentifyTemplate)` Snapshot of the state of the `DeidentifyTemplate` from the `[Deidentify](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.Action.Deidentify)` action at the time this job was run.  
`snapshot_structured_deidentify_template` |  `[DeidentifyTemplate](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DeidentifyTemplate)` Snapshot of the state of the structured `DeidentifyTemplate` from the `Deidentify` action at the time this job was run.  
`snapshot_image_redact_template` |  `[DeidentifyTemplate](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DeidentifyTemplate)` Snapshot of the state of the image transformation `DeidentifyTemplate` from the `Deidentify` action at the time this job was run.  
  
## DeidentifyDataSourceStats

Summary of what was modified during a transformation.

Fields  
---  
`transformed_bytes` |  `int64` Total size in bytes that were transformed in some way.  
`transformation_count` |  `int64` Number of successfully applied transformations.  
`transformation_error_count` |  `int64` Number of errors encountered while trying to apply transformations.  
  
## DeidentifyTemplate

DeidentifyTemplates contains instructions on how to de-identify content. See <https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-templates> to learn more.

Fields  
---  
`name` |  `string` Output only. The template name.The template will have one of the following formats: `projects/PROJECT_ID/deidentifyTemplates/TEMPLATE_ID` OR `organizations/ORGANIZATION_ID/deidentifyTemplates/TEMPLATE_ID`  
`display_name` |  `string` Display name (max 256 chars).  
`description` |  `string` Short description (max 256 chars).  
`create_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. The creation timestamp of an inspectTemplate.  
`update_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. The last update timestamp of an inspectTemplate.  
`deidentify_config` |  `[DeidentifyConfig](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DeidentifyConfig)` The core content of the template.  
  
## DeleteConnectionRequest

Request message for DeleteConnection.

Fields  
---  
`name` |  `string` Required. Resource name of the Connection to be deleted, in the format: `projects/{project}/locations/{location}/connections/{connection}`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `dlp.connections.delete`

  
  
## DeleteContentPolicyRequest

Request message for DeleteContentPolicy.

Fields  
---  
`name` |  `string` Required. Resource name of the ContentPolicy to be deleted, in the format: `projects/{project}/locations/{location}/contentPolicies/{content_policy}`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `dlp.contentPolicies.delete`

  
  
## DeleteDeidentifyTemplateRequest

Request message for DeleteDeidentifyTemplate.

Fields  
---  
`name` |  `string` Required. Resource name of the organization and deidentify template to be deleted, for example `organizations/433245324/deidentifyTemplates/432452342` or projects/project-id/deidentifyTemplates/432452342. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `dlp.deidentifyTemplates.delete`

  
  
## DeleteDiscoveryConfigRequest

Request message for DeleteDiscoveryConfig.

Fields  
---  
`name` |  `string` Required. Resource name of the project and the config, for example `projects/dlp-test-project/discoveryConfigs/53234423`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `dlp.jobTriggers.delete`

  
  
## DeleteDlpJobRequest

The request message for deleting a DLP job.

Fields  
---  
`name` |  `string` Required. The name of the DlpJob resource to be deleted. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `dlp.jobs.delete`

  
  
## DeleteFileStoreDataProfileRequest

Request message for DeleteFileStoreProfile.

Fields  
---  
`name` |  `string` Required. Resource name of the file store data profile. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `dlp.fileStoreDataProfiles.delete`

  
  
## DeleteInspectTemplateRequest

Request message for DeleteInspectTemplate.

Fields  
---  
`name` |  `string` Required. Resource name of the organization and inspectTemplate to be deleted, for example `organizations/433245324/inspectTemplates/432452342` or projects/project-id/inspectTemplates/432452342. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `dlp.inspectTemplates.delete`

  
  
## DeleteJobTriggerRequest

Request message for DeleteJobTrigger.

Fields  
---  
`name` |  `string` Required. Resource name of the project and the triggeredJob, for example `projects/dlp-test-project/jobTriggers/53234423`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `dlp.jobTriggers.delete`

  
  
## DeleteStoredInfoTypeRequest

Request message for DeleteStoredInfoType.

Fields  
---  
`name` |  `string` Required. Resource name of the organization and storedInfoType to be deleted, for example `organizations/433245324/storedInfoTypes/432452342` or projects/project-id/storedInfoTypes/432452342. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `dlp.storedInfoTypes.delete`

  
  
## DeleteTableDataProfileRequest

Request message for DeleteTableProfile.

Fields  
---  
`name` |  `string` Required. Resource name of the table data profile. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `dlp.tableDataProfiles.delete`

  
  
## Disabled

This type has no fields.

Do not profile the tables.

## DiscoveryBigQueryConditions

Requirements that must be true before a table is scanned in discovery for the first time. There is an AND relationship between the top-level attributes. Additionally, minimum conditions with an OR relationship that must be met before Cloud DLP scans a table can be set (like a minimum row count or a minimum table age).

Fields  
---  
`created_after` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` BigQuery table must have been created after this date. Used to avoid backfilling.  
`or_conditions` |  `[OrConditions](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DiscoveryBigQueryConditions.OrConditions)` At least one of the conditions must be true for a table to be scanned.  
Union field `included_types`. The type of BigQuery tables to scan. If nothing is set the default behavior is to scan only tables of type TABLE and to give errors for all unsupported tables. `included_types` can be only one of the following:  
`types` |  `[BigQueryTableTypes](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.BigQueryTableTypes)` Restrict discovery to specific table types.  
`type_collection` |  `[BigQueryTableTypeCollection](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.BigQueryTableTypeCollection)` Restrict discovery to categories of table types.  
  
## OrConditions

There is an OR relationship between these attributes. They are used to determine if a table should be scanned or not in Discovery.

Fields  
---  
`min_row_count` |  `int32` Minimum number of rows that should be present before Cloud DLP profiles a table  
`min_age` |  `[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` Minimum age a table must have before Cloud DLP can profile it. Value must be 1 hour or greater.  
  
## DiscoveryBigQueryFilter

Determines what tables will have profiles generated within an organization or project. Includes the ability to filter by regular expression patterns on project ID, dataset ID, and table ID.

Fields  
---  
Union field `filter`. Whether the filter applies to a specific set of tables or all other tables within the location being profiled. The first filter to match will be applied, regardless of the condition. If none is set, will default to `other_tables`. `filter` can be only one of the following:  
`tables` |  `[BigQueryTableCollection](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.BigQueryTableCollection)` A specific set of tables for this filter to apply to. A table collection must be specified in only one filter per config. If a table id or dataset is empty, Cloud DLP assumes all tables in that collection must be profiled. Must specify a project ID.  
`other_tables` |  `[AllOtherBigQueryTables](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DiscoveryBigQueryFilter.AllOtherBigQueryTables)` Catch-all. This should always be the last filter in the list because anything above it will apply first. Should only appear once in a configuration. If none is specified, a default one will be added automatically.  
`table_reference` |  `[TableReference](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.TableReference)` The table to scan. Discovery configurations including this can only include one DiscoveryTarget (the DiscoveryTarget with this TableReference).  
  
## AllOtherBigQueryTables

This type has no fields.

Catch-all for all other tables not specified by other filters. Should always be last, except for single-table configurations, which will only have a TableReference target.

## DiscoveryCloudSqlConditions

Requirements that must be true before a table is profiled for the first time.

Fields  
---  
`database_engines[]` |  `[DatabaseEngine](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DiscoveryCloudSqlConditions.DatabaseEngine)` Optional. Database engines that should be profiled. Optional. Defaults to ALL_SUPPORTED_DATABASE_ENGINES if unspecified.  
`types[]` |  `[DatabaseResourceType](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DiscoveryCloudSqlConditions.DatabaseResourceType)` Data profiles will only be generated for the database resource types specified in this field. If not specified, defaults to [DATABASE_RESOURCE_TYPE_ALL_SUPPORTED_TYPES].  
  
## DatabaseEngine

The database engines that should be profiled.

Enums  
---  
`DATABASE_ENGINE_UNSPECIFIED` | Unused.  
`ALL_SUPPORTED_DATABASE_ENGINES` | Include all supported database engines.  
`MYSQL` | MySQL database.  
`POSTGRES` | PostgreSQL database.  
  
## DatabaseResourceType

Cloud SQL database resource types. New values can be added at a later time.

Enums  
---  
`DATABASE_RESOURCE_TYPE_UNSPECIFIED` | Unused.  
`DATABASE_RESOURCE_TYPE_ALL_SUPPORTED_TYPES` | Includes database resource types that become supported at a later time.  
`DATABASE_RESOURCE_TYPE_TABLE` | Tables.  
  
## DiscoveryCloudSqlFilter

Determines what tables will have profiles generated within an organization or project. Includes the ability to filter by regular expression patterns on project ID, location, instance, database, and database resource name.

Fields  
---  
Union field `filter`. Whether the filter applies to a specific set of database resources or all other database resources within the location being profiled. The first filter to match will be applied, regardless of the condition. If none is set, will default to `others`. `filter` can be only one of the following:  
`collection` |  `[DatabaseResourceCollection](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DatabaseResourceCollection)` A specific set of database resources for this filter to apply to.  
`others` |  `[AllOtherDatabaseResources](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.AllOtherDatabaseResources)` Catch-all. This should always be the last target in the list because anything above it will apply first. Should only appear once in a configuration. If none is specified, a default one will be added automatically.  
`database_resource_reference` |  `[DatabaseResourceReference](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DatabaseResourceReference)` The database resource to scan. Targets including this can only include one target (the target with this database resource reference).  
  
## DiscoveryCloudSqlGenerationCadence

How often existing tables should have their profiles refreshed. New tables are scanned as quickly as possible depending on system capacity.

Fields  
---  
`schema_modified_cadence` |  `[SchemaModifiedCadence](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DiscoveryCloudSqlGenerationCadence.SchemaModifiedCadence)` When to reprofile if the schema has changed.  
`refresh_frequency` |  `[DataProfileUpdateFrequency](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DataProfileUpdateFrequency)` Data changes (non-schema changes) in Cloud SQL tables can't trigger reprofiling. If you set this field, profiles are refreshed at this frequency regardless of whether the underlying tables have changed. Defaults to never.  
`inspect_template_modified_cadence` |  `[DiscoveryInspectTemplateModifiedCadence](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DiscoveryInspectTemplateModifiedCadence)` Governs when to update data profiles when the inspection rules defined by the `InspectTemplate` change. If not set, changing the template will not cause a data profile to update.  
  
## SchemaModifiedCadence

How frequently to modify the profile when the table's schema is modified.

Fields  
---  
`types[]` |  `[CloudSqlSchemaModification](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DiscoveryCloudSqlGenerationCadence.SchemaModifiedCadence.CloudSqlSchemaModification)` The types of schema modifications to consider. Defaults to NEW_COLUMNS.  
`frequency` |  `[DataProfileUpdateFrequency](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DataProfileUpdateFrequency)` Frequency to regenerate data profiles when the schema is modified. Defaults to monthly.  
  
## CloudSqlSchemaModification

The type of modification that causes a profile update.

Enums  
---  
`SQL_SCHEMA_MODIFICATION_UNSPECIFIED` | Unused.  
`NEW_COLUMNS` | New columns have appeared.  
`REMOVED_COLUMNS` | Columns have been removed from the table.  
  
## DiscoveryCloudStorageConditions

Requirements that must be true before a Cloud Storage bucket or object is scanned in discovery for the first time. There is an AND relationship between the top-level attributes.

Fields  
---  
`included_object_attributes[]` |  `[CloudStorageObjectAttribute](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DiscoveryCloudStorageConditions.CloudStorageObjectAttribute)` Required. Only objects with the specified attributes will be scanned. If an object has one of the specified attributes but is inside an excluded bucket, it will not be scanned. Defaults to [ALL_SUPPORTED_OBJECTS]. A profile will be created even if no objects match the included_object_attributes.  
`included_bucket_attributes[]` |  `[CloudStorageBucketAttribute](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DiscoveryCloudStorageConditions.CloudStorageBucketAttribute)` Required. Only objects with the specified attributes will be scanned. Defaults to [ALL_SUPPORTED_BUCKETS] if unset.  
  
## CloudStorageBucketAttribute

The attribute of a bucket.

Enums  
---  
`CLOUD_STORAGE_BUCKET_ATTRIBUTE_UNSPECIFIED` | Unused.  
`ALL_SUPPORTED_BUCKETS` | Scan buckets regardless of the attribute.  
`AUTOCLASS_DISABLED` | Buckets with [Autoclass](https://docs.cloud.google.com/storage/docs/autoclass) disabled. Only one of AUTOCLASS_DISABLED or AUTOCLASS_ENABLED should be set.  
`AUTOCLASS_ENABLED` | Buckets with [Autoclass](https://docs.cloud.google.com/storage/docs/autoclass) enabled. Only one of AUTOCLASS_DISABLED or AUTOCLASS_ENABLED should be set. Scanning Autoclass-enabled buckets can affect object storage classes.  
  
## CloudStorageObjectAttribute

The attribute of an object. See <https://docs.cloud.google.com/storage/docs/storage-classes> for more information on storage classes.

Enums  
---  
`CLOUD_STORAGE_OBJECT_ATTRIBUTE_UNSPECIFIED` | Unused.  
`ALL_SUPPORTED_OBJECTS` | Scan objects regardless of the attribute.  
`STANDARD` | Scan objects with the standard storage class.  
`NEARLINE` | Scan objects with the nearline storage class. This will incur retrieval fees.  
`COLDLINE` | Scan objects with the coldline storage class. This will incur retrieval fees.  
`ARCHIVE` | Scan objects with the archive storage class. This will incur retrieval fees.  
`REGIONAL` | Scan objects with the regional storage class.  
`MULTI_REGIONAL` | Scan objects with the multi-regional storage class.  
`DURABLE_REDUCED_AVAILABILITY` | Scan objects with the dual-regional storage class. This will incur retrieval fees.  
  
## DiscoveryCloudStorageFilter

Determines which buckets will have profiles generated within an organization or project. Includes the ability to filter by regular expression patterns on project ID and bucket name.

Fields  
---  
Union field `filter`. Whether the filter applies to a specific set of buckets or all other buckets within the location being profiled. The first filter to match will be applied, regardless of the condition. If none is set, will default to `others`. `filter` can be only one of the following:  
`collection` |  `[FileStoreCollection](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.FileStoreCollection)` Optional. A specific set of buckets for this filter to apply to.  
`cloud_storage_resource_reference` |  `[CloudStorageResourceReference](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.CloudStorageResourceReference)` Optional. The bucket to scan. Targets including this can only include one target (the target with this bucket). This enables profiling the contents of a single bucket, while the other options allow for easy profiling of many bucets within a project or an organization.  
`others` |  `[AllOtherResources](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.AllOtherResources)` Optional. Catch-all. This should always be the last target in the list because anything above it will apply first. Should only appear once in a configuration. If none is specified, a default one will be added automatically.  
  
## DiscoveryCloudStorageGenerationCadence

How often existing buckets should have their profiles refreshed. New buckets are scanned as quickly as possible depending on system capacity.

Fields  
---  
`refresh_frequency` |  `[DataProfileUpdateFrequency](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DataProfileUpdateFrequency)` Optional. Data changes in Cloud Storage can't trigger reprofiling. If you set this field, profiles are refreshed at this frequency regardless of whether the underlying buckets have changed. Defaults to never.  
`inspect_template_modified_cadence` |  `[DiscoveryInspectTemplateModifiedCadence](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DiscoveryInspectTemplateModifiedCadence)` Optional. Governs when to update data profiles when the inspection rules defined by the `InspectTemplate` change. If not set, changing the template will not cause a data profile to update.  
  
## DiscoveryConfig

Configuration for discovery to scan resources for profile generation. Only one discovery configuration may exist per organization, folder, or project.

The generated data profiles are retained according to the [data retention policy](https://docs.cloud.google.com/sensitive-data-protection/docs/data-profiles#retention).

Fields  
---  
`name` |  `string` Output only. Unique resource name for the DiscoveryConfig, assigned by the service when the DiscoveryConfig is created, for example `projects/dlp-test-project/locations/global/discoveryConfigs/53234423`.  
`display_name` |  `string` Display name (max 100 chars)  
`org_config` |  `[OrgConfig](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DiscoveryConfig.OrgConfig)` Only set when the parent is an org.  
`other_cloud_starting_location` |  `[OtherCloudDiscoveryStartingLocation](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.OtherCloudDiscoveryStartingLocation)` Must be set only when scanning other clouds.  
`inspect_templates[]` |  `string` Detection logic for profile generation.Not all template features are used by Discovery. FindingLimits, include_quote and exclude_info_types have no impact on Discovery.Multiple templates may be provided if there is data in multiple regions. At most one template must be specified per-region (including "global"). Each region is scanned using the applicable template. If no region-specific template is specified, but a "global" template is specified, it will be copied to that region and used instead. If no global or region-specific template is provided for a region with data, that region's data will not be scanned.For more information, see <https://docs.cloud.google.com/sensitive-data-protection/docs/data-profiles#data-residency>.  
`actions[]` |  `[DataProfileAction](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DataProfileAction)` Actions to execute at the completion of scanning.  
`targets[]` |  `[DiscoveryTarget](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DiscoveryTarget)` Target to match against for determining what to scan and how frequently.  
`errors[]` |  `[Error](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.Error)` Output only. A stream of errors encountered when the config was activated. Repeated errors may result in the config automatically being paused. Output only field. Will return the last 100 errors. Whenever the config is modified this list will be cleared.  
`create_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. The creation timestamp of a DiscoveryConfig.  
`update_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. The last update timestamp of a DiscoveryConfig.  
`last_run_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. The timestamp of the last time this config was executed.  
`status` |  `[Status](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DiscoveryConfig.Status)` Required. A status for this configuration.  
`processing_location` |  `[ProcessingLocation](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ProcessingLocation)` Optional. Processing location configuration. Vertex AI dataset scanning will set processing_location.image_fallback_type to MultiRegionProcessing by default.  
  
## OrgConfig

Project and scan location information. Only set when the parent is an org.

Fields  
---  
`location` |  `[DiscoveryStartingLocation](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DiscoveryStartingLocation)` The data to scan: folder, org, or project  
`project_id` |  `string` The project that will run the scan. The DLP service account that exists within this project must have access to all resources that are profiled, and the DLP API must be enabled.  
  
## Status

Whether the discovery config is currently active. New options may be added at a later time.

Enums  
---  
`STATUS_UNSPECIFIED` | Unused  
`RUNNING` | The discovery config is currently active.  
`PAUSED` | The discovery config is paused temporarily.  
  
## DiscoveryFileStoreConditions

Requirements that must be true before a file store is scanned in discovery for the first time. There is an AND relationship between the top-level attributes.

Fields  
---  
`created_after` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Optional. File store must have been created after this date. Used to avoid backfilling.  
`min_age` |  `[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` Optional. Minimum age a file store must have. If set, the value must be 1 hour or greater.  
Union field `conditions`. File store specific conditions. `conditions` can be only one of the following:  
`cloud_storage_conditions` |  `[DiscoveryCloudStorageConditions](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DiscoveryCloudStorageConditions)` Optional. Cloud Storage conditions.  
  
## DiscoveryGenerationCadence

What must take place for a profile to be updated and how frequently it should occur. New tables are scanned as quickly as possible depending on system capacity.

Fields  
---  
`schema_modified_cadence` |  `[DiscoverySchemaModifiedCadence](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DiscoverySchemaModifiedCadence)` Governs when to update data profiles when a schema is modified.  
`table_modified_cadence` |  `[DiscoveryTableModifiedCadence](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DiscoveryTableModifiedCadence)` Governs when to update data profiles when a table is modified.  
`inspect_template_modified_cadence` |  `[DiscoveryInspectTemplateModifiedCadence](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DiscoveryInspectTemplateModifiedCadence)` Governs when to update data profiles when the inspection rules defined by the `InspectTemplate` change. If not set, changing the template will not cause a data profile to update.  
`refresh_frequency` |  `[DataProfileUpdateFrequency](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DataProfileUpdateFrequency)` Frequency at which profiles should be updated, regardless of whether the underlying resource has changed. Defaults to never.  
  
## DiscoveryInspectTemplateModifiedCadence

The cadence at which to update data profiles when the inspection rules defined by the `InspectTemplate` change.

Fields  
---  
`frequency` |  `[DataProfileUpdateFrequency](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DataProfileUpdateFrequency)` How frequently data profiles can be updated when the template is modified. Defaults to never.  
  
## DiscoveryOtherCloudConditions

Requirements that must be true before a resource is profiled for the first time.

Fields  
---  
`min_age` |  `[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` Minimum age a resource must be before Cloud DLP can profile it. Value must be 1 hour or greater.  
Union field `conditions`. The conditions to apply. `conditions` can be only one of the following:  
`amazon_s3_bucket_conditions` |  `[AmazonS3BucketConditions](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.AmazonS3BucketConditions)` Amazon S3 bucket conditions.  
  
## DiscoveryOtherCloudFilter

Determines which resources from the other cloud will have profiles generated. Includes the ability to filter by resource names.

Fields  
---  
Union field `filter`. Whether the filter applies to a specific set of resources or all other resources. The first filter to match will be applied, regardless of the condition. Defaults to `others` if none is set. `filter` can be only one of the following:  
`collection` |  `[OtherCloudResourceCollection](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.OtherCloudResourceCollection)` A collection of resources for this filter to apply to.  
`single_resource` |  `[OtherCloudSingleResourceReference](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.OtherCloudSingleResourceReference)` The resource to scan. Configs using this filter can only have one target (the target with this single resource reference).  
`others` |  `[AllOtherResources](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.AllOtherResources)` Optional. Catch-all. This should always be the last target in the list because anything above it will apply first. Should only appear once in a configuration. If none is specified, a default one will be added automatically.  
  
## DiscoveryOtherCloudGenerationCadence

How often existing resources should have their profiles refreshed. New resources are scanned as quickly as possible depending on system capacity.

Fields  
---  
`refresh_frequency` |  `[DataProfileUpdateFrequency](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DataProfileUpdateFrequency)` Optional. Frequency to update profiles regardless of whether the underlying resource has changes. Defaults to never.  
`inspect_template_modified_cadence` |  `[DiscoveryInspectTemplateModifiedCadence](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DiscoveryInspectTemplateModifiedCadence)` Optional. Governs when to update data profiles when the inspection rules defined by the `InspectTemplate` change. If not set, changing the template will not cause a data profile to update.  
  
## DiscoverySchemaModifiedCadence

The cadence at which to update data profiles when a schema is modified.

Fields  
---  
`types[]` |  `[BigQuerySchemaModification](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.BigQuerySchemaModification)` The type of events to consider when deciding if the table's schema has been modified and should have the profile updated. Defaults to NEW_COLUMNS.  
`frequency` |  `[DataProfileUpdateFrequency](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DataProfileUpdateFrequency)` How frequently profiles may be updated when schemas are modified. Defaults to monthly.  
  
## DiscoveryStartingLocation

The location to begin a discovery scan. Denotes an organization ID or folder ID within an organization.

Fields  
---  
Union field `location`. The location to be scanned. `location` can be only one of the following:  
`organization_id` |  `int64` The ID of an organization to scan.  
`folder_id` |  `int64` The ID of the folder within an organization to be scanned.  
  
## DiscoveryTableModifiedCadence

The cadence at which to update data profiles when a table is modified.

Fields  
---  
`types[]` |  `[BigQueryTableModification](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.BigQueryTableModification)` The type of events to consider when deciding if the table has been modified and should have the profile updated. Defaults to MODIFIED_TIMESTAMP.  
`frequency` |  `[DataProfileUpdateFrequency](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DataProfileUpdateFrequency)` How frequently data profiles can be updated when tables are modified. Defaults to never.  
  
## DiscoveryTarget

Target used to match against for Discovery.

Fields  
---  
Union field `target`. A target to match against for Discovery. `target` can be only one of the following:  
`big_query_target` |  `[BigQueryDiscoveryTarget](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.BigQueryDiscoveryTarget)` BigQuery target for Discovery. The first target to match a table will be the one applied.  
`cloud_sql_target` |  `[CloudSqlDiscoveryTarget](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.CloudSqlDiscoveryTarget)` Cloud SQL target for Discovery. The first target to match a table will be the one applied.  
`secrets_target` |  `[SecretsDiscoveryTarget](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.SecretsDiscoveryTarget)` Discovery target that looks for credentials and secrets stored in cloud resource metadata and reports them as vulnerabilities to Security Command Center. Only one target of this type is allowed.  
`cloud_storage_target` |  `[CloudStorageDiscoveryTarget](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.CloudStorageDiscoveryTarget)` Cloud Storage target for Discovery. The first target to match a table will be the one applied.  
`other_cloud_target` |  `[OtherCloudDiscoveryTarget](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.OtherCloudDiscoveryTarget)` Other clouds target for discovery. The first target to match a resource will be the one applied.  
`vertex_dataset_target` |  `[VertexDatasetDiscoveryTarget](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.VertexDatasetDiscoveryTarget)` Vertex AI dataset target for Discovery. The first target to match a dataset will be the one applied. Note that discovery for Vertex AI can incur Cloud Storage Class B operation charges for storage.objects.get operations and retrieval fees. For more information, see [Cloud Storage pricing](https://cloud.google.com/storage/pricing#price-tables). Note that discovery for Vertex AI dataset will not be able to scan images unless DiscoveryConfig.processing_location.image_fallback_location has multi_region_processing or global_processing configured.  
  
## DiscoveryVertexDatasetConditions

Requirements that must be true before a dataset is profiled for the first time.

Fields  
---  
`created_after` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Vertex AI dataset must have been created after this date. Used to avoid backfilling.  
`min_age` |  `[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` Minimum age a Vertex AI dataset must have. If set, the value must be 1 hour or greater.  
  
## DiscoveryVertexDatasetFilter

Determines what datasets will have profiles generated within an organization or project. Includes the ability to filter by regular expression patterns on project ID or dataset regex.

Fields  
---  
Union field `filter`. Whether the filter applies to a specific set of datasets or all other datasets within the location being profiled. The first filter to match will be applied, regardless of the condition. If none is set, this field defaults to `others`. `filter` can be only one of the following:  
`collection` |  `[VertexDatasetCollection](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.VertexDatasetCollection)` A specific set of Vertex AI datasets for this filter to apply to.  
`vertex_dataset_resource_reference` |  `[VertexDatasetResourceReference](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.VertexDatasetResourceReference)` The dataset resource to scan. Targets including this can only include one target (the target with this dataset resource reference).  
`others` |  `[AllOtherResources](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.AllOtherResources)` Catch-all. This should always be the last target in the list because anything above it will apply first. Should only appear once in a configuration. If none is specified, a default one will be added automatically.  
  
## DiscoveryVertexDatasetGenerationCadence

How often existing datasets should have their profiles refreshed. New datasets are scanned as quickly as possible depending on system capacity.

Fields  
---  
`refresh_frequency` |  `[DataProfileUpdateFrequency](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DataProfileUpdateFrequency)` If you set this field, profiles are refreshed at this frequency regardless of whether the underlying datasets have changed. Defaults to never.  
`inspect_template_modified_cadence` |  `[DiscoveryInspectTemplateModifiedCadence](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DiscoveryInspectTemplateModifiedCadence)` Governs when to update data profiles when the inspection rules defined by the `InspectTemplate` change. If not set, changing the template will not cause a data profile to be updated.  
  
## DlpJob

Combines all of the information about a DLP job.

Fields  
---  
`name` |  `string` Output only. The server-assigned name.  
`type` |  `[DlpJobType](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DlpJobType)` The type of job.  
`state` |  `[JobState](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DlpJob.JobState)` Output only. State of a job.  
`create_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. Time when the job was created.  
`start_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. Time when the job started.  
`end_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. Time when the job finished.  
`last_modified` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. Time when the job was last modified by the system.  
`job_trigger_name` |  `string` Output only. If created by a job trigger, the resource name of the trigger that instantiated the job.  
`errors[]` |  `[Error](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.Error)` Output only. A stream of errors encountered running the job.  
`action_details[]` |  `[ActionDetails](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ActionDetails)` Output only. Events that should occur after the job has completed.  
Union field `details`. Job details. `details` can be only one of the following:  
`risk_details` |  `[AnalyzeDataSourceRiskDetails](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.AnalyzeDataSourceRiskDetails)` Results from analyzing risk of a data source.  
`inspect_details` |  `[InspectDataSourceDetails](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.InspectDataSourceDetails)` Results from inspecting a data source.  
  
## JobState

Possible states of a job. New items may be added.

Enums  
---  
`JOB_STATE_UNSPECIFIED` | Unused.  
`PENDING` | The job has not yet started.  
`RUNNING` | The job is currently running. Once a job has finished it will transition to FAILED or DONE.  
`DONE` | The job is no longer running.  
`CANCELED` | The job was canceled before it could be completed.  
`FAILED` | The job had an error and did not complete.  
`ACTIVE` | The job is currently accepting findings via hybridInspect. A hybrid job in ACTIVE state may continue to have findings added to it through the calling of hybridInspect. After the job has finished no more calls to hybridInspect may be made. ACTIVE jobs can transition to DONE.  
  
## DlpJobType

An enum to represent the various types of DLP jobs.

Enums  
---  
`DLP_JOB_TYPE_UNSPECIFIED` | Defaults to INSPECT_JOB.  
`INSPECT_JOB` | The job inspected Google Cloud for sensitive data.  
`RISK_ANALYSIS_JOB` | The job executed a Risk Analysis computation.  
  
## DocumentLocation

Location of a finding within a document.

Fields  
---  
`file_offset` |  `int64` Offset of the line, from the beginning of the file, where the finding is located.  
  
## Domain

A domain represents a thematic category that a data profile can fall under.

Fields  
---  
`category` |  `[Category](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.Domain.Category)` A domain category that this profile is related to.  
`signals[]` |  `[Signal](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.Domain.Signal)` The collection of signals that influenced selection of the category.  
  
## Category

This enum defines the various domain categories a data profile can fall under.

Enums  
---  
`CATEGORY_UNSPECIFIED` | Category unspecified.  
`AI` | Indicates that the data profile is related to artificial intelligence. When set, all findings stored to Security Command Center will set the corresponding AI domain field of `Finding` objects.  
`CODE` | Indicates that the data profile is related to code.  
  
## Signal

The signal used to determine the category. New values may be added in the future.

Enums  
---  
`SIGNAL_UNSPECIFIED` | Unused.  
`MODEL` | One or more machine learning models are present.  
`TEXT_EMBEDDING` | A table appears to contain text embeddings.  
`EMBEDDING` | A table appears to contain embeddings of any type (for example, text, image, multimodal). The `TEXT_EMBEDDING` signal might also be present if the table contains text embeddings.  
`VERTEX_PLUGIN` | The [Cloud SQL Vertex AI](https://docs.cloud.google.com/sql/docs/postgres/integrate-cloud-sql-with-vertex-ai) plugin is installed on the database.  
`VECTOR_PLUGIN` | Support for [Cloud SQL vector embeddings](https://docs.cloud.google.com/sql/docs/mysql/enable-vector-search) is enabled on the database.  
`SOURCE_CODE` | Source code is present.  
`SERVICE` | If the service determines the category type. For example, Vertex AI assets would always have a `Category` of `AI`.  
  
## Encloses

This type has no fields.

Defines a condition where one bounding box encloses another.

## EncryptionStatus

How a resource is encrypted.

Enums  
---  
`ENCRYPTION_STATUS_UNSPECIFIED` | Unused.  
`ENCRYPTION_GOOGLE_MANAGED` | Google manages server-side encryption keys on your behalf.  
`ENCRYPTION_CUSTOMER_MANAGED` | Customer provides the key.  
  
## EntityId

An entity in a dataset is a field or set of fields that correspond to a single person. For example, in medical records the `EntityId` might be a patient identifier, or for financial records it might be an account identifier. This message is used when generalizations or analysis must take into account that multiple rows correspond to the same entity.

Fields  
---  
`field` |  `[FieldId](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.FieldId)` Composite key indicating which field contains the entity identifier.  
  
## Error

Details information about an error encountered during job execution or the results of an unsuccessful activation of the JobTrigger.

Fields  
---  
`details` |  `[Status](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.rpc#google.rpc.Status)` Detailed error codes and messages.  
`timestamps[]` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` The times the error occurred. List includes the oldest timestamp and the last 9 timestamps.  
`extra_info` |  `[ErrorExtraInfo](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.Error.ErrorExtraInfo)` Additional information about the error.  
  
## ErrorExtraInfo

Additional information about the error.

Enums  
---  
`ERROR_INFO_UNSPECIFIED` | Unused.  
`IMAGE_SCAN_UNAVAILABLE_IN_REGION` | Image scan is not available in the region.  
`FILE_STORE_CLUSTER_UNSUPPORTED` | File store cluster is not supported for profile generation.  
  
## ExcludeByHotword

The rule to exclude findings based on a hotword. For record inspection of tables, column names are considered hotwords. An example of this is to exclude a finding if it belongs to a BigQuery column that matches a specific pattern.

Fields  
---  
`hotword_regex` |  `[Regex](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.CustomInfoType.Regex)` Regular expression pattern defining what qualifies as a hotword.  
`proximity` |  `[Proximity](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.CustomInfoType.DetectionRule.Proximity)` Range of characters within which the entire hotword must reside. The total length of the window cannot exceed 1000 characters. The windowBefore property in proximity should be set to 1 if the hotword needs to be included in a column header.  
  
## ExcludeByImageFindings

The rule to exclude image findings based on spatial relationships with other image findings. For example, exclude an image finding if it overlaps with another image finding. This rule is silently ignored if the content being inspected is not an image.

Fields  
---  
`info_types[]` |  `[InfoType](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.InfoType)` A list of image-supported infoTypes—excluding [document infoTypes](https://docs.cloud.google.com/sensitive-data-protection/docs/infotypes-reference#documents)—to be used as context for the exclusion rule. A finding is excluded if its bounding box has the specified spatial relationship (defined by `image_containment_type`) with a finding of an infoType in this list.For example, if `InspectionRuleSet.info_types` includes `OBJECT_TYPE/PERSON` and this `exclusion_rule` specifies `info_types` as `OBJECT_TYPE/PERSON/PASSPORT` with `image_containment_type` set to `encloses`, then `OBJECT_TYPE/PERSON` findings will be excluded if they are fully contained within the bounding box of an `OBJECT_TYPE/PERSON/PASSPORT` finding.  
`image_containment_type` |  `[ImageContainmentType](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ImageContainmentType)` Specifies the required spatial relationship between the bounding boxes of the target finding and the context infoType findings.  
  
## ExcludeInfoTypes

List of excluded infoTypes.

Fields  
---  
`info_types[]` |  `[InfoType](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.InfoType)` InfoType list in ExclusionRule rule drops a finding when it overlaps or contained within with a finding of an infoType from this list. For example, for `InspectionRuleSet.info_types` containing "PHONE_NUMBER"`and `exclusion_rule`containing`exclude_info_types.info_types` with "EMAIL_ADDRESS" the phone number findings are dropped if they overlap with EMAIL_ADDRESS finding. That leads to "555-222-2222@example.org" to generate only a single finding, namely email address.  
  
## ExclusionRule

The rule that specifies conditions when findings of infoTypes specified in `InspectionRuleSet` are removed from results.

Fields  
---  
`matching_type` |  `[MatchingType](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.MatchingType)` How the rule is applied, see MatchingType documentation for details.  
Union field `type`. Exclusion rule types. `type` can be only one of the following:  
`dictionary` |  `[Dictionary](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.CustomInfoType.Dictionary)` Dictionary which defines the rule.  
`regex` |  `[Regex](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.CustomInfoType.Regex)` Regular expression which defines the rule.  
`exclude_info_types` |  `[ExcludeInfoTypes](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ExcludeInfoTypes)` Set of infoTypes for which findings would affect this rule.  
`exclude_by_hotword` |  `[ExcludeByHotword](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ExcludeByHotword)` Drop if the hotword rule is contained in the proximate context. For tabular data, the context includes the column name.  
`exclude_by_image_findings` |  `[ExcludeByImageFindings](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ExcludeByImageFindings)` Exclude findings based on image containment rules. For example, exclude an image finding if it overlaps with another image finding.  
  
## FieldId

General identifier of a data field in a storage service.

Fields  
---  
`name` |  `string` Name describing the field.  
  
## FieldTransformation

The transformation to apply to the field.

Fields  
---  
`fields[]` |  `[FieldId](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.FieldId)` Required. Input field(s) to apply the transformation to. When you have columns that reference their position within a list, omit the index from the FieldId. FieldId name matching ignores the index. For example, instead of "contact.nums[0].type", use "contact.nums.type".  
`condition` |  `[RecordCondition](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.RecordCondition)` Only apply the transformation if the condition evaluates to true for the given `RecordCondition`. The conditions are allowed to reference fields that are not used in the actual transformation.Example Use Cases:

  * Apply a different bucket transformation to an age column if the zip code column for the same record is within a specific range.
  * Redact a field if the date of birth field is greater than 85.

  
Union field `transformation`. Transformation to apply. [required] `transformation` can be only one of the following:  
`primitive_transformation` |  `[PrimitiveTransformation](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.PrimitiveTransformation)` Apply the transformation to the entire field.  
`info_type_transformations` |  `[InfoTypeTransformations](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.InfoTypeTransformations)` Treat the contents of the field as free text, and selectively transform content that matches an `InfoType`.  
  
## FileClusterSummary

The file cluster summary.

Fields  
---  
`file_cluster_type` |  `[FileClusterType](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.FileClusterType)` The file cluster type.  
`file_store_info_type_summaries[]` |  `[FileStoreInfoTypeSummary](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.FileStoreInfoTypeSummary)` InfoTypes detected in this cluster.  
`sensitivity_score` |  `[SensitivityScore](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.SensitivityScore)` The sensitivity score of this cluster. The score will be SENSITIVITY_LOW if nothing has been scanned.  
`data_risk_level` |  `[DataRiskLevel](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DataRiskLevel)` The data risk level of this cluster. RISK_LOW if nothing has been scanned.  
`errors[]` |  `[Error](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.Error)` A list of errors detected while scanning this cluster. The list is truncated to 10 per cluster.  
`file_extensions_scanned[]` |  `[FileExtensionInfo](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.FileExtensionInfo)` A sample of file types scanned in this cluster. Empty if no files were scanned. File extensions can be derived from the file name or the file content.  
`file_extensions_seen[]` |  `[FileExtensionInfo](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.FileExtensionInfo)` A sample of file types seen in this cluster. Empty if no files were seen. File extensions can be derived from the file name or the file content.  
`no_files_exist` |  `bool` True if no files exist in this cluster. If the file store had more files than could be listed, this will be false even if no files for this cluster were seen and file_extensions_seen is empty.  
  
## FileClusterType

Message used to identify file cluster type being profiled.

Fields  
---  
Union field `file_cluster_type`. File cluster type. `file_cluster_type` can be only one of the following:  
`cluster` |  `[Cluster](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.FileClusterType.Cluster)` Cluster type.  
  
## Cluster

Cluster type. Each cluster corresponds to a set of file types. Over time, new types may be added and files may move between clusters.

Enums  
---  
`CLUSTER_UNSPECIFIED` | Unused.  
`CLUSTER_UNKNOWN` | Unsupported files.  
`CLUSTER_TEXT` | Plain text.  
`CLUSTER_STRUCTURED_DATA` | Structured data like CSV, TSV etc.  
`CLUSTER_SOURCE_CODE` | Source code.  
`CLUSTER_RICH_DOCUMENT` | Rich document like docx, xlsx etc.  
`CLUSTER_IMAGE` | Images like jpeg, bmp.  
`CLUSTER_ARCHIVE` | Archives and containers like .zip, .tar etc.  
`CLUSTER_MULTIMEDIA` | Multimedia like .mp4, .avi etc.  
`CLUSTER_EXECUTABLE` | Executable files like .exe, .class, .apk etc.  
`CLUSTER_AI_MODEL` | AI models like .tflite etc.  
  
## FileExtensionInfo

Information regarding the discovered file extension.

Fields  
---  
`file_extension` |  `string` The file extension if set. (aka .pdf, .jpg, .txt)  
  
## FileLabel

Represents a file label.

Fields  
---  
Union field `type`. The type of file label. `type` can be only one of the following:  
`sensitivity_label` |  `[SensitivityLabelMetadata](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.FileLabel.SensitivityLabelMetadata)` Sensitivity labels published by Microsoft.  
`google_drive_label` |  `[GoogleDriveLabelMetadata](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.FileLabel.GoogleDriveLabelMetadata)` Google Drive labels published by Google.  
  
## GoogleDriveLabelMetadata

Google Drive labels published by Google.

Fields  
---  
`label_id` |  `string` The [label ID](https://developers.google.com/workspace/drive/labels/guides/overview) of the Google Drive label.  
`label_fields[]` |  `[LabelFieldMetadata](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.FileLabel.GoogleDriveLabelMetadata.LabelFieldMetadata)` The field values of the Google Drive label  
  
## LabelFieldMetadata

The field values of the Google Drive label

Fields  
---  
`id` |  `string` The identifier of the Label Field.  
`value` |  `[Value](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.Value)` The value of the Label Field.  
  
## SensitivityLabelMetadata

Sensitivity labels published by Microsoft.

Fields  
---  
`guid` |  `string` Required. The GUID of the sensitivity label.  
  
## FileStoreCollection

Match file stores (e.g. buckets) using filters.

Fields  
---  
`include_tags` |  `[TagFilters](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.TagFilters)` Optional. To be included in the collection, a resource must meet all of the following requirements:

  * If tag filters are provided, match all provided tag filters.
  * If one or more patterns are specified, match at least one pattern.

For a resource to match the tag filters, the resource must have all of the provided tags attached. Tags refer to Resource Manager tags bound to the resource or its ancestors. For more information, see [Manage schedules](https://docs.cloud.google.com/sensitive-data-protection/docs/profile-project-cloud-storage#manage-schedules).  
Union field `pattern`. The first filter containing a pattern that matches a file store will be used. `pattern` can be only one of the following:  
`include_regexes` |  `[FileStoreRegexes](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.FileStoreRegexes)` Optional. A collection of regular expressions to match a file store against.  
  
## FileStoreDataProfile

The profile for a file store.

  * Cloud Storage: maps 1:1 with a bucket.
  * Amazon S3: maps 1:1 with a bucket.

Fields  
---  
`name` |  `string` The name of the profile.  
`data_source_type` |  `[DataSourceType](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DataSourceType)` The resource type that was profiled.  
`project_data_profile` |  `string` The resource name of the project data profile for this file store.  
`project_id` |  `string` The Google Cloud project ID that owns the resource. For Amazon S3 buckets, this is the AWS Account Id.  
`file_store_location` |  `string` The location of the file store.

  * Cloud Storage: <https://docs.cloud.google.com/storage/docs/locations#available-locations>
  * Amazon S3: <https://docs.aws.amazon.com/general/latest/gr/rande.html#regional-endpoints>

  
`data_storage_locations[]` |  `string` For resources that have multiple storage locations, these are those regions. For Cloud Storage this is the list of regions chosen for dual-region storage. `file_store_location` will normally be the corresponding multi-region for the list of individual locations. The first region is always picked as the processing and storage location for the data profile.  
`location_type` |  `string` The location type of the file store (region, dual-region, multi-region, etc). If dual-region, expect data_storage_locations to be populated.  
`file_store_path` |  `string` The file store path.

  * Cloud Storage: `gs://{bucket}`
  * Amazon S3: `s3://{bucket}`
  * Vertex AI dataset: `projects/{project_number}/locations/{location}/datasets/{dataset_id}`

  
`full_resource` |  `string` The resource name of the resource profiled. <https://cloud.google.com/apis/design/resource_names#full_resource_name>Example format of an S3 bucket full resource name: `//cloudasset.googleapis.com/organizations/{org_id}/otherCloudConnections/aws/arn:aws:s3:::{bucket_name}`  
`config_snapshot` |  `[DataProfileConfigSnapshot](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DataProfileConfigSnapshot)` The snapshot of the configurations used to generate the profile.  
`profile_status` |  `[ProfileStatus](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ProfileStatus)` Success or error status from the most recent profile generation attempt. May be empty if the profile is still being generated.  
`state` |  `[State](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.FileStoreDataProfile.State)` State of a profile.  
`profile_last_generated` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` The last time the profile was generated.  
`resource_visibility` |  `[ResourceVisibility](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ResourceVisibility)` How broadly a resource has been shared.  
`sensitivity_score` |  `[SensitivityScore](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.SensitivityScore)` The sensitivity score of this resource.  
`data_risk_level` |  `[DataRiskLevel](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DataRiskLevel)` The data risk level of this resource.  
`create_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` The time the file store was first created.  
`last_modified_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` The time the file store was last modified.  
`file_cluster_summaries[]` |  `[FileClusterSummary](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.FileClusterSummary)` FileClusterSummary per each cluster.  
`resource_attributes` |  `map<string, `[Value](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.Value)`>` Attributes of the resource being profiled. Currently used attributes:

  * customer_managed_encryption: boolean 
    * true: the resource is encrypted with a customer-managed key.
    * false: the resource is encrypted with a provider-managed key.

  
`resource_labels` |  `map<string, string>` The labels applied to the resource at the time the profile was generated.  
`file_store_info_type_summaries[]` |  `[FileStoreInfoTypeSummary](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.FileStoreInfoTypeSummary)` InfoTypes detected in this file store.  
`sample_findings_table` |  `[BigQueryTable](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.BigQueryTable)` The BigQuery table to which the sample findings are written.  
`file_store_is_empty` |  `bool` The file store does not have any files. If the profiling operation failed, this is false.  
`tags[]` |  `[Tag](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.Tag)` The tags attached to the resource, including any tags attached during profiling.  
`related_resources[]` |  `[RelatedResource](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.RelatedResource)` Resources related to this profile.  
`domains[]` |  `[Domain](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.Domain)` Domains associated with the profile.  
  
## State

Possible states of a profile. New items may be added.

Enums  
---  
`STATE_UNSPECIFIED` | Unused.  
`RUNNING` | The profile is currently running. Once a profile has finished it will transition to DONE.  
`DONE` | The profile is no longer generating. If profile_status.status.code is 0, the profile succeeded, otherwise, it failed.  
  
## FileStoreInfoTypeSummary

Information regarding the discovered InfoType.

Fields  
---  
`info_type` |  `[InfoType](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.InfoType)` The InfoType seen.  
  
## FileStoreRegex

A pattern to match against one or more file stores.

Fields  
---  
Union field `resource_regex`. The type of resource regex to use. `resource_regex` can be only one of the following:  
`cloud_storage_regex` |  `[CloudStorageRegex](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.CloudStorageRegex)` Optional. Regex for Cloud Storage.  
  
## FileStoreRegexes

A collection of regular expressions to determine what file store to match against.

Fields  
---  
`patterns[]` |  `[FileStoreRegex](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.FileStoreRegex)` Required. The group of regular expression patterns to match against one or more file stores. Maximum of 100 entries. The sum of all regular expression's length can't exceed 10 KiB.  
  
## FileType

Definitions of file type groups to scan. New types will be added to this list.

Enums  
---  
`FILE_TYPE_UNSPECIFIED` | Includes all files.  
`BINARY_FILE` | Includes all file extensions not covered by another entry. Binary scanning attempts to convert the content of the file to utf_8 to scan the file. If you wish to avoid this fall back, specify one or more of the other file types in your storage scan.  
`TEXT_FILE` | Included file extensions: asc,asp, aspx, brf, c, cc,cfm, cgi, cpp, csv, cxx, c++, cs, css, dart, dat, dot, eml,, epbub, ged, go, h, hh, hpp, hxx, h++, hs, html, htm, mkd, markdown, m, ml, mli, perl, pl, plist, pm, php, phtml, pht, properties, py, pyw, rb, rbw, rs, rss, rc, scala, sh, sql, swift, tex, shtml, shtm, xhtml, lhs, ics, ini, java, js, json, jsonl, kix, kml, ocaml, md, txt, text, tsv, vb, vcard, vcs, wml, xcodeproj, xml, xsl, xsd, yml, yaml.  
`IMAGE` | Included file extensions: bmp, gif, jpg, jpeg, jpe, png. Setting `[bytes_limit_per_file](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.CloudStorageOptions.FIELDS.int64.google.privacy.dlp.v2.CloudStorageOptions.bytes_limit_per_file)` or `[bytes_limit_per_file_percent](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.CloudStorageOptions.FIELDS.int64.google.privacy.dlp.v2.CloudStorageOptions.bytes_limit_per_file)` has no effect on image files. Image inspection is restricted to the `global`, `us`, `asia`, and `europe` regions.  
`WORD` | Microsoft Word files larger than 30 MB will be scanned as binary files. Included file extensions: docx, dotx, docm, dotm. Setting `bytes_limit_per_file` or `bytes_limit_per_file_percent` has no effect on Word files.  
`PDF` | PDF files larger than 30 MB will be scanned as binary files. Included file extensions: pdf. Setting `bytes_limit_per_file` or `bytes_limit_per_file_percent` has no effect on PDF files.  
`AVRO` | Included file extensions: avro  
`CSV` | Included file extensions: csv  
`TSV` | Included file extensions: tsv  
`POWERPOINT` | Microsoft PowerPoint files larger than 30 MB will be scanned as binary files. Included file extensions: pptx, pptm, potx, potm, pot. Setting `bytes_limit_per_file` or `bytes_limit_per_file_percent` has no effect on PowerPoint files.  
`EXCEL` | Microsoft Excel files larger than 30 MB will be scanned as binary files. Included file extensions: xlsx, xlsm, xltx, xltm. Setting `bytes_limit_per_file` or `bytes_limit_per_file_percent` has no effect on Excel files.  
  
## Finding

Represents a piece of potentially sensitive content.

Fields  
---  
`name` |  `string` Resource name in format projects/{project}/locations/{location}/findings/{finding} Populated only when viewing persisted findings.  
`quote` |  `string` The content that was found. Even if the content is not textual, it may be converted to a textual representation here. Provided if `include_quote` is true and the finding is less than or equal to 4096 bytes long. If the finding exceeds 4096 bytes in length, the quote may be omitted.  
`info_type` |  `[InfoType](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.InfoType)` The type of content that might have been found. Provided if `excluded_types` is false.  
`likelihood` |  `[Likelihood](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.Likelihood)` Confidence of how likely it is that the `info_type` is correct.  
`location` |  `[Location](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.Location)` Where the content was found.  
`create_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Timestamp when finding was detected.  
`quote_info` |  `[QuoteInfo](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.QuoteInfo)` Contains data parsed from quotes. Only populated if include_quote was set to true and a supported infoType was requested. Currently supported infoTypes: DATE, DATE_OF_BIRTH and TIME.  
`resource_name` |  `string` The job that stored the finding.  
`trigger_name` |  `string` Job trigger name, if applicable, for this finding.  
`labels` |  `map<string, string>` The labels associated with this `Finding`.Label keys must be between 1 and 63 characters long and must conform to the following regular expression: `[a-z]([-a-z0-9]*[a-z0-9])?`.Label values must be between 0 and 63 characters long and must conform to the regular expression `([a-z]([-a-z0-9]*[a-z0-9])?)?`.No more than 10 labels can be associated with a given finding.Examples:

  * `"environment" : "production"`
  * `"pipeline" : "etl"`

  
`job_create_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Time the job started that produced this finding.  
`job_name` |  `string` The job that stored the finding.  
`finding_id` |  `string` The unique finding id.  
  
## FinishDlpJobRequest

The request message for finishing a DLP hybrid job.

Fields  
---  
`name` |  `string` Required. The name of the DlpJob resource to be finished. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `dlp.jobs.finish`

  
  
## FixedSizeBucketingConfig

Buckets values based on fixed size ranges. The Bucketing transformation can provide all of this functionality, but requires more configuration. This message is provided as a convenience to the user for simple bucketing strategies.

The transformed value will be a hyphenated string of {lower_bound}-{upper_bound}. For example, if lower_bound = 10 and upper_bound = 20, all values that are within this bucket will be replaced with "10-20".

This can be used on data of type: double, long.

If the bound Value type differs from the type of data being transformed, we will first attempt converting the type of the data to be transformed to match the type of the bound before comparing.

See <https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-bucketing> to learn more.

Fields  
---  
`lower_bound` |  `[Value](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.Value)` Required. Lower bound value of buckets. All values less than `lower_bound` are grouped together into a single bucket; for example if `lower_bound` = 10, then all values less than 10 are replaced with the value "-10".  
`upper_bound` |  `[Value](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.Value)` Required. Upper bound value of buckets. All values greater than upper_bound are grouped together into a single bucket; for example if `upper_bound` = 89, then all values greater than 89 are replaced with the value "89+".  
`bucket_size` |  `double` Required. Size of each bucket (except for minimum and maximum buckets). So if `lower_bound` = 10, `upper_bound` = 89, and `bucket_size` = 10, then the following buckets would be used: -10, 10-20, 20-30, 30-40, 40-50, 50-60, 60-70, 70-80, 80-89, 89+. Precision up to 2 decimals works.  
  
## FullyInside

This type has no fields.

Defines a condition where one bounding box is fully inside another.

## GetColumnDataProfileRequest

Request to get a column data profile.

Fields  
---  
`name` |  `string` Required. Resource name, for example `organizations/12345/locations/us/columnDataProfiles/53234423`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `dlp.columnDataProfiles.get`

  
  
## GetConnectionRequest

Request message for GetConnection.

Fields  
---  
`name` |  `string` Required. Resource name in the format: `projects/{project}/locations/{location}/connections/{connection}`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `dlp.connections.get`

  
  
## GetContentPolicyRequest

Request message for GetContentPolicy.

Fields  
---  
`name` |  `string` Required. Resource name in the format: `projects/{project}/locations/{location}/contentPolicies/{content_policy}`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `dlp.contentPolicies.get`

  
  
## GetDeidentifyTemplateRequest

Request message for GetDeidentifyTemplate.

Fields  
---  
`name` |  `string` Required. Resource name of the organization and deidentify template to be read, for example `organizations/433245324/deidentifyTemplates/432452342` or projects/project-id/deidentifyTemplates/432452342. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `dlp.deidentifyTemplates.get`

  
  
## GetDiscoveryConfigRequest

Request message for GetDiscoveryConfig.

Fields  
---  
`name` |  `string` Required. Resource name of the project and the configuration, for example `projects/dlp-test-project/discoveryConfigs/53234423`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `dlp.jobTriggers.get`

  
  
## GetDlpJobRequest

The request message for `[GetDlpJob](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DlpService.GetDlpJob)`.

Fields  
---  
`name` |  `string` Required. The name of the DlpJob resource. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `dlp.jobs.get`

  
  
## GetFileStoreDataProfileRequest

Request to get a file store data profile.

Fields  
---  
`name` |  `string` Required. Resource name, for example `organizations/12345/locations/us/fileStoreDataProfiles/53234423`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `dlp.fileStoreProfiles.get`

  
  
## GetInspectTemplateRequest

Request message for GetInspectTemplate.

Fields  
---  
`name` |  `string` Required. Resource name of the organization and inspectTemplate to be read, for example `organizations/433245324/inspectTemplates/432452342` or projects/project-id/inspectTemplates/432452342. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `dlp.inspectTemplates.get`

  
  
## GetJobTriggerRequest

Request message for GetJobTrigger.

Fields  
---  
`name` |  `string` Required. Resource name of the project and the triggeredJob, for example `projects/dlp-test-project/jobTriggers/53234423`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `dlp.jobTriggers.get`

  
  
## GetProjectDataProfileRequest

Request to get a project data profile.

Fields  
---  
`name` |  `string` Required. Resource name, for example `organizations/12345/locations/us/projectDataProfiles/53234423`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `dlp.projectDataProfiles.get`

  
  
## GetStoredInfoTypeRequest

Request message for GetStoredInfoType.

Fields  
---  
`name` |  `string` Required. Resource name of the organization and storedInfoType to be read, for example `organizations/433245324/storedInfoTypes/432452342` or projects/project-id/storedInfoTypes/432452342. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `dlp.storedInfoTypes.get`

  
  
## GetTableDataProfileRequest

Request to get a table data profile.

Fields  
---  
`name` |  `string` Required. Resource name, for example `organizations/12345/locations/us/tableDataProfiles/53234423`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `dlp.tableDataProfiles.get`

  
  
## HybridContentItem

An individual hybrid item to inspect. Will be stored temporarily during processing.

Fields  
---  
`item` |  `[ContentItem](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ContentItem)` The item to inspect.  
`finding_details` |  `[HybridFindingDetails](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.HybridFindingDetails)` Supplementary information that will be added to each finding.  
  
## HybridFindingDetails

Populate to associate additional data with each finding.

Fields  
---  
`container_details` |  `[Container](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.Container)` Details about the container where the content being inspected is from.  
`file_offset` |  `int64` Offset in bytes of the line, from the beginning of the file, where the finding is located. Populate if the item being scanned is only part of a bigger item, such as a shard of a file and you want to track the absolute position of the finding.  
`row_offset` |  `int64` Offset of the row for tables. Populate if the row(s) being scanned are part of a bigger dataset and you want to keep track of their absolute position.  
`table_options` |  `[TableOptions](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.TableOptions)` If the container is a table, additional information to make findings meaningful such as the columns that are primary keys. If not known ahead of time, can also be set within each inspect hybrid call and the two will be merged. Note that identifying_fields will only be stored to BigQuery, and only if the BigQuery action has been included.  
`labels` |  `map<string, string>` Labels to represent user provided metadata about the data being inspected. If configured by the job, some key values may be required. The labels associated with `Finding`'s produced by hybrid inspection.Label keys must be between 1 and 63 characters long and must conform to the following regular expression: `[a-z]([-a-z0-9]*[a-z0-9])?`.Label values must be between 0 and 63 characters long and must conform to the regular expression `([a-z]([-a-z0-9]*[a-z0-9])?)?`.No more than 10 labels can be associated with a given finding.Examples:

  * `"environment" : "production"`
  * `"pipeline" : "etl"`

  
  
## HybridInspectDlpJobRequest

Request to search for potentially sensitive info in a custom location.

Fields  
---  
`name` |  `string` Required. Resource name of the job to execute a hybrid inspect on, for example `projects/dlp-test-project/dlpJob/53234423`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `dlp.jobs.hybridInspect`

  
`hybrid_item` |  `[HybridContentItem](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.HybridContentItem)` The item to inspect.  
  
## HybridInspectJobTriggerRequest

Request to search for potentially sensitive info in a custom location.

Fields  
---  
`name` |  `string` Required. Resource name of the trigger to execute a hybrid inspect on, for example `projects/dlp-test-project/jobTriggers/53234423`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `dlp.jobTriggers.hybridInspect`

  
`hybrid_item` |  `[HybridContentItem](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.HybridContentItem)` The item to inspect.  
  
## HybridInspectResponse

This type has no fields.

Quota exceeded errors will be thrown once quota has been met.

## HybridInspectStatistics

Statistics related to processing hybrid inspect requests.

Fields  
---  
`processed_count` |  `int64` The number of hybrid inspection requests processed within this job.  
`aborted_count` |  `int64` The number of hybrid inspection requests aborted because the job ran out of quota or was ended before they could be processed.  
`pending_count` |  `int64` The number of hybrid requests currently being processed. Only populated when called via method `getDlpJob`. A burst of traffic may cause hybrid inspect requests to be enqueued. Processing will take place as quickly as possible, but resource limitations may impact how long a request is enqueued for.  
  
## HybridOptions

Configuration to control jobs where the content being inspected is outside of Google Cloud Platform.

Fields  
---  
`description` |  `string` A short description of where the data is coming from. Will be stored once in the job. 256 max length.  
`required_finding_label_keys[]` |  `string` These are labels that each inspection request must include within their 'finding_labels' map. Request may contain others, but any missing one of these will be rejected.Label keys must be between 1 and 63 characters long and must conform to the following regular expression: `[a-z]([-a-z0-9]*[a-z0-9])?`.No more than 10 keys can be required.  
`labels` |  `map<string, string>` To organize findings, these labels will be added to each finding.Label keys must be between 1 and 63 characters long and must conform to the following regular expression: `[a-z]([-a-z0-9]*[a-z0-9])?`.Label values must be between 0 and 63 characters long and must conform to the regular expression `([a-z]([-a-z0-9]*[a-z0-9])?)?`.No more than 10 labels can be associated with a given finding.Examples:

  * `"environment" : "production"`
  * `"pipeline" : "etl"`

  
`table_options` |  `[TableOptions](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.TableOptions)` If the container is a table, additional information to make findings meaningful such as the columns that are primary keys.  
  
## ImageContainmentType

Specifies the relationship between bounding boxes for image findings.

Fields  
---  
Union field `type`. The type of relationship to check between the target finding and the context finding. `type` can be only one of the following:  
`encloses` |  `[Encloses](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.Encloses)` The context finding's bounding box must fully contain the target finding's bounding box.  
`fully_inside` |  `[FullyInside](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.FullyInside)` The context finding's bounding box must be fully inside the target finding's bounding box.  
`overlaps` |  `[Overlap](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.Overlap)` The context finding's bounding box and the target finding's bounding box must have a non-zero intersection.  
  
## ImageLocation

Location of the finding within an image.

Fields  
---  
`bounding_boxes[]` |  `[BoundingBox](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.BoundingBox)` Bounding boxes locating the pixels within the image containing the finding.  
  
## ImageTransformations

A type of transformation that is applied over images.

Fields  
---  
`transforms[]` |  `[ImageTransformation](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ImageTransformations.ImageTransformation)` List of transforms to make.  
  
## ImageTransformation

Configuration for determining how redaction of images should occur.

Fields  
---  
`redaction_color` |  `[Color](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.Color)` The color to use when redacting content from an image. If not specified, the default is black.  
Union field `target`. Part of the image to transform. `target` can be only one of the following:  
`selected_info_types` |  `[SelectedInfoTypes](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ImageTransformations.ImageTransformation.SelectedInfoTypes)` Apply transformation to the selected info_types.  
`all_info_types` |  `[AllInfoTypes](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ImageTransformations.ImageTransformation.AllInfoTypes)` Apply transformation to all findings not specified in other ImageTransformation's selected_info_types. Only one instance is allowed within the ImageTransformations message.  
`all_text` |  `[AllText](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ImageTransformations.ImageTransformation.AllText)` Apply transformation to all text that doesn't match an infoType. Only one instance is allowed within the ImageTransformations message.  
  
## AllInfoTypes

This type has no fields.

Apply transformation to all findings.

## AllText

This type has no fields.

Apply to all text.

## SelectedInfoTypes

Apply transformation to the selected info_types.

Fields  
---  
`info_types[]` |  `[InfoType](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.InfoType)` Required. InfoTypes to apply the transformation to. Required. Provided InfoType must be unique within the ImageTransformations message.  
  
## InfoType

Type of information detected by the API.

Fields  
---  
`name` |  `string` Name of the information type. Either a name of your choosing when creating a CustomInfoType, or one of the names listed at <https://docs.cloud.google.com/sensitive-data-protection/docs/infotypes-reference> when specifying a built-in type. When sending Cloud DLP results to Data Catalog, infoType names should conform to the pattern `[A-Za-z0-9$_-]{1,64}`.  
`version` |  `string` Optional version name for this InfoType.  
`sensitivity_score` |  `[SensitivityScore](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.SensitivityScore)` Optional custom sensitivity for this InfoType. This only applies to data profiling.  
  
## InfoTypeCategory

Classification of infoTypes to organize them according to geographic location, industry, and data type.

Fields  
---  
Union field `category`. Categories of infotypes. `category` can be only one of the following:  
`location_category` |  `[LocationCategory](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.InfoTypeCategory.LocationCategory)` The region or country that issued the ID or document represented by the infoType.  
`industry_category` |  `[IndustryCategory](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.InfoTypeCategory.IndustryCategory)` The group of relevant businesses where this infoType is commonly used  
`type_category` |  `[TypeCategory](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.InfoTypeCategory.TypeCategory)` The class of identifiers where this infoType belongs  
  
## IndustryCategory

Enum of the current industries in the category. We might add more industries in the future.

Enums  
---  
`INDUSTRY_UNSPECIFIED` | Unused industry  
`FINANCE` | The infoType is typically used in the finance industry.  
`HEALTH` | The infoType is typically used in the health industry.  
`TELECOMMUNICATIONS` | The infoType is typically used in the telecommunications industry.  
  
## LocationCategory

Enum of the current locations. We might add more locations in the future.

Enums  
---  
`LOCATION_UNSPECIFIED` | Unused location  
`GLOBAL` | The infoType is not issued by or tied to a specific region, but is used almost everywhere.  
`ARGENTINA` | The infoType is typically used in Argentina.  
`ARMENIA` | The infoType is typically used in Armenia.  
`AUSTRALIA` | The infoType is typically used in Australia.  
`AUSTRIA` | The infoType is typically used in Austria.  
`AZERBAIJAN` | The infoType is typically used in Azerbaijan.  
`BELARUS` | The infoType is typically used in Belarus.  
`BELGIUM` | The infoType is typically used in Belgium.  
`BRAZIL` | The infoType is typically used in Brazil.  
`CANADA` | The infoType is typically used in Canada.  
`CHILE` | The infoType is typically used in Chile.  
`CHINA` | The infoType is typically used in China.  
`COLOMBIA` | The infoType is typically used in Colombia.  
`CROATIA` | The infoType is typically used in Croatia.  
`CZECHIA` | The infoType is typically used in Czechia.  
`DENMARK` | The infoType is typically used in Denmark.  
`FRANCE` | The infoType is typically used in France.  
`FINLAND` | The infoType is typically used in Finland.  
`GERMANY` | The infoType is typically used in Germany.  
`HONG_KONG` | The infoType is typically used in Hong Kong.  
`INDIA` | The infoType is typically used in India.  
`INDONESIA` | The infoType is typically used in Indonesia.  
`IRELAND` | The infoType is typically used in Ireland.  
`ISRAEL` | The infoType is typically used in Israel.  
`ITALY` | The infoType is typically used in Italy.  
`JAPAN` | The infoType is typically used in Japan.  
`KAZAKHSTAN` | The infoType is typically used in Kazakhstan.  
`KOREA` | The infoType is typically used in Korea.  
`MEXICO` | The infoType is typically used in Mexico.  
`THE_NETHERLANDS` | The infoType is typically used in the Netherlands.  
`NEW_ZEALAND` | The infoType is typically used in New Zealand.  
`NORWAY` | The infoType is typically used in Norway.  
`PARAGUAY` | The infoType is typically used in Paraguay.  
`PERU` | The infoType is typically used in Peru.  
`POLAND` | The infoType is typically used in Poland.  
`PORTUGAL` | The infoType is typically used in Portugal.  
`RUSSIA` | The infoType is typically used in Russia.  
`SINGAPORE` | The infoType is typically used in Singapore.  
`SOUTH_AFRICA` | The infoType is typically used in South Africa.  
`SPAIN` | The infoType is typically used in Spain.  
`SWEDEN` | The infoType is typically used in Sweden.  
`SWITZERLAND` | The infoType is typically used in Switzerland.  
`TAIWAN` | The infoType is typically used in Taiwan.  
`THAILAND` | The infoType is typically used in Thailand.  
`TURKEY` | The infoType is typically used in Turkey.  
`UKRAINE` | The infoType is typically used in Ukraine.  
`UNITED_KINGDOM` | The infoType is typically used in the United Kingdom.  
`UNITED_STATES` | The infoType is typically used in the United States.  
`URUGUAY` | The infoType is typically used in Uruguay.  
`UZBEKISTAN` | The infoType is typically used in Uzbekistan.  
`VENEZUELA` | The infoType is typically used in Venezuela.  
`INTERNAL` | The infoType is typically used in Google internally.  
  
## TypeCategory

Enum of the current types in the category. We might add more types in the future.

Enums  
---  
`TYPE_UNSPECIFIED` | Unused type  
`PII` | Personally identifiable information, for example, a name or phone number  
`SPII` | Personally identifiable information that is especially sensitive, for example, a passport number.  
`DEMOGRAPHIC` | Attributes that can partially identify someone, especially in combination with other attributes, like age, height, and gender.  
`CREDENTIAL` | Confidential or secret information, for example, a password.  
`GOVERNMENT_ID` | An identification document issued by a government.  
`DOCUMENT` | A document, for example, a resume or source code.  
`CONTEXTUAL_INFORMATION` | Information that is not sensitive on its own, but provides details about the circumstances surrounding an entity or an event.  
`CUSTOM` | Category for `CustomInfoType` types.  
  
## InfoTypeDescription

InfoType description.

Fields  
---  
`name` |  `string` Internal name of the infoType.  
`display_name` |  `string` Human readable form of the infoType name.  
`supported_by[]` |  `[InfoTypeSupportedBy](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.InfoTypeSupportedBy)` Which parts of the API supports this InfoType.  
`description` |  `string` Description of the infotype. Translated when language is provided in the request.  
`location_support` |  `[LocationSupport](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.LocationSupport)` Locations at which this feature can be used. May change over time.  
`example` |  `string` A sample that is a true positive for this infoType.  
`versions[]` |  `[VersionDescription](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.VersionDescription)` A list of available versions for the infotype.  
`categories[]` |  `[InfoTypeCategory](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.InfoTypeCategory)` The category of the infoType.  
`sensitivity_score` |  `[SensitivityScore](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.SensitivityScore)` The default sensitivity of the infoType.  
`specific_info_types[]` |  `string` If this field is set, this infoType is a general infoType and these specific infoTypes are contained within it. General infoTypes are infoTypes that encompass multiple specific infoTypes. For example, the "GEOGRAPHIC_DATA" general infoType would have set for this field "LOCATION", "LOCATION_COORDINATES", and "STREET_ADDRESS".  
`launch_status` |  `[InfoTypeLaunchStatus](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.InfoTypeDescription.InfoTypeLaunchStatus)` The launch status of the infoType.  
  
## InfoTypeLaunchStatus

The launch status of an infoType.

Enums  
---  
`INFO_TYPE_LAUNCH_STATUS_UNSPECIFIED` | Unspecified.  
`GENERAL_AVAILABILITY` | InfoType is generally available.  
`PUBLIC_PREVIEW` | InfoType is in public preview.  
`PRIVATE_PREVIEW` | InfoType is in private preview.  
  
## InfoTypeStats

Statistics regarding a specific InfoType.

Fields  
---  
`info_type` |  `[InfoType](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.InfoType)` The type of finding this stat is for.  
`count` |  `int64` Number of findings for this infoType.  
  
## InfoTypeSummary

The infoType details for this column.

Fields  
---  
`info_type` |  `[InfoType](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.InfoType)` The infoType.  
`estimated_prevalence  
**(deprecated)**` |  `int32` This item is deprecated!Not populated for predicted infotypes.  
  
## InfoTypeSupportedBy

Parts of the APIs which use certain infoTypes.

Enums  
---  
`ENUM_TYPE_UNSPECIFIED` | Unused.  
`INSPECT` | Supported by the inspect operations.  
`RISK_ANALYSIS` | Supported by the risk analysis operations.  
  
## InfoTypeTransformations

A type of transformation that will scan unstructured text and apply various `PrimitiveTransformation`s to each finding, where the transformation is applied to only values that were identified as a specific info_type.

Fields  
---  
`transformations[]` |  `[InfoTypeTransformation](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.InfoTypeTransformations.InfoTypeTransformation)` Required. Transformation for each infoType. Cannot specify more than one for a given infoType.  
  
## InfoTypeTransformation

A transformation to apply to text that is identified as a specific info_type.

Fields  
---  
`info_types[]` |  `[InfoType](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.InfoType)` InfoTypes to apply the transformation to. An empty list will cause this transformation to apply to all findings that correspond to infoTypes that were requested in `InspectConfig`.  
`primitive_transformation` |  `[PrimitiveTransformation](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.PrimitiveTransformation)` Required. Primitive transformation to apply to the infoType.  
  
## InspectConfig

Configuration description of the scanning process. When used with redactContent only info_types and min_likelihood are currently used.

Fields  
---  
`info_types[]` |  `[InfoType](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.InfoType)` Restricts what info_types to look for. The values must correspond to InfoType values returned by ListInfoTypes or listed at <https://docs.cloud.google.com/sensitive-data-protection/docs/infotypes-reference>.When no InfoTypes or CustomInfoTypes are specified in a request, the system may automatically choose a default list of detectors to run, which may change over time.If you need precise control and predictability as to what detectors are run you should specify specific InfoTypes listed in the reference, otherwise a default list will be used, which may change over time.  
`min_likelihood` |  `[Likelihood](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.Likelihood)` Only returns findings equal to or above this threshold. The default is POSSIBLE.In general, the highest likelihood setting yields the fewest findings in results and the lowest chance of a false positive. For more information, see [Match likelihood](https://docs.cloud.google.com/sensitive-data-protection/docs/likelihood).  
`min_likelihood_per_info_type[]` |  `[InfoTypeLikelihood](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.InspectConfig.InfoTypeLikelihood)` Minimum likelihood per infotype. For each infotype, a user can specify a minimum likelihood. The system only returns a finding if its likelihood is above this threshold. If this field is not set, the system uses the InspectConfig min_likelihood.  
`limits` |  `[FindingLimits](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.InspectConfig.FindingLimits)` Configuration to control the number of findings returned. This is not used for data profiling.When redacting sensitive data from images, finding limits don't apply. They can cause unexpected or inconsistent results, where only some data is redacted. Don't include finding limits in `[RedactImage](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DlpService.RedactImage)` requests. Otherwise, Cloud DLP returns an error.When set within an `[InspectJobConfig](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.InspectJobConfig)`, the specified maximum values aren't hard limits. If an inspection job reaches these limits, the job ends gradually, not abruptly. Therefore, the actual number of findings that Cloud DLP returns can be multiple times higher than these maximum values.  
`include_quote` |  `bool` When true, a contextual quote from the data that triggered a finding is included in the response; see `[Finding.quote](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.Finding.FIELDS.string.google.privacy.dlp.v2.Finding.quote)`. This is not used for data profiling.  
`exclude_info_types` |  `bool` When true, excludes type information of the findings. This is not used for data profiling.  
`custom_info_types[]` |  `[CustomInfoType](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.CustomInfoType)` CustomInfoTypes provided by the user. See <https://docs.cloud.google.com/sensitive-data-protection/docs/creating-custom-infotypes> to learn more.  
`content_options[]` |  `[ContentOption](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ContentOption)` Deprecated and unused.  
`rule_set[]` |  `[InspectionRuleSet](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.InspectionRuleSet)` Set of rules to apply to the findings for this InspectConfig. Exclusion rules, contained in the set are executed in the end, other rules are executed in the order they are specified for each info type. Not supported for the `metadata_key_value_expression` CustomInfoType.  
  
## FindingLimits

Configuration to control the number of findings returned for inspection. This is not used for de-identification or data profiling.

When redacting sensitive data from images, finding limits don't apply. They can cause unexpected or inconsistent results, where only some data is redacted. Don't include finding limits in `[RedactImage](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DlpService.RedactImage)` requests. Otherwise, Cloud DLP returns an error.

Fields  
---  
`max_findings_per_item` |  `int32` Max number of findings that are returned for each item scanned.When set within an `[InspectContentRequest](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.InspectContentRequest)`, this field is ignored.This value isn't a hard limit. If the number of findings for an item reaches this limit, the inspection of that item ends gradually, not abruptly. Therefore, the actual number of findings that Cloud DLP returns for the item can be multiple times higher than this value.  
`max_findings_per_request` |  `int32` Max number of findings that are returned per request or job.If you set this field in an `[InspectContentRequest](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.InspectContentRequest)`, the resulting maximum value is the value that you set or 3,000, whichever is lower.This value isn't a hard limit. If an inspection reaches this limit, the inspection ends gradually, not abruptly. Therefore, the actual number of findings that Cloud DLP returns can be multiple times higher than this value.  
`max_findings_per_info_type[]` |  `[InfoTypeLimit](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.InspectConfig.FindingLimits.InfoTypeLimit)` Configuration of findings limit given for specified infoTypes.  
  
## InfoTypeLimit

Max findings configuration per infoType, per content item or long running DlpJob.

Fields  
---  
`info_type` |  `[InfoType](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.InfoType)` Type of information the findings limit applies to. Only one limit per info_type should be provided. If InfoTypeLimit does not have an info_type, the DLP API applies the limit against all info_types that are found but not specified in another InfoTypeLimit.  
`max_findings` |  `int32` Max findings limit for the given infoType.  
  
## InfoTypeLikelihood

Configuration for setting a minimum likelihood per infotype. Used to customize the minimum likelihood level for specific infotypes in the request. For example, use this if you want to lower the precision for PERSON_NAME without lowering the precision for the other infotypes in the request.

Fields  
---  
`info_type` |  `[InfoType](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.InfoType)` Type of information the likelihood threshold applies to. Only one likelihood per info_type should be provided. If InfoTypeLikelihood does not have an info_type, the configuration fails.  
`min_likelihood` |  `[Likelihood](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.Likelihood)` Only returns findings equal to or above this threshold. This field is required or else the configuration fails.  
  
## InspectContentRequest

Request to search for potentially sensitive info in a ContentItem.

Fields  
---  
`parent` |  `string` Parent resource name.The format of this value varies depending on whether you have [specified a processing location](https://docs.cloud.google.com/sensitive-data-protection/docs/specifying-location):

  * Projects scope, location specified: `projects/{project_id}/locations/{location_id}`
  * Projects scope, no location specified (defaults to global): `projects/{project_id}`

The following example `parent` string specifies a parent project with the identifier `example-project`, and specifies the `europe-west3` location for processing data:
    
    
    parent=projects/example-project/locations/europe-west3
    

Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `serviceusage.services.use`

  
`inspect_config` |  `[InspectConfig](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.InspectConfig)` Configuration for the inspector. What specified here will override the template referenced by the inspect_template_name argument.  
`item` |  `[ContentItem](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ContentItem)` The item to inspect.  
`inspect_template_name` |  `string` Template to use. Any configuration directly specified in inspect_config will override those set in the template. Singular fields that are set in this request will replace their corresponding fields in the template. Repeated fields are appended. Singular sub-messages and groups are recursively merged.  
`location_id` |  `string` Deprecated. This field has no effect.  
  
## InspectContentResponse

Results of inspecting an item.

Fields  
---  
`result` |  `[InspectResult](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.InspectResult)` The findings.  
  
## InspectDataSourceDetails

The results of an inspect DataSource job.

Fields  
---  
`requested_options` |  `[RequestedOptions](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.InspectDataSourceDetails.RequestedOptions)` The configuration used for this job.  
`result` |  `[Result](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.InspectDataSourceDetails.Result)` Output only. A summary of the outcome of this inspection job.  
  
## RequestedOptions

Snapshot of the inspection configuration.

Fields  
---  
`snapshot_inspect_template` |  `[InspectTemplate](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.InspectTemplate)` Output only. If run with an InspectTemplate, a snapshot of its state at the time of this run.  
`job_config` |  `[InspectJobConfig](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.InspectJobConfig)` Inspect config.  
  
## Result

All Result fields are updated while the job is processing.

Fields  
---  
`processed_bytes` |  `int64` Total size in bytes that were processed.  
`total_estimated_bytes` |  `int64` Estimate of the number of bytes to process.  
`info_type_stats[]` |  `[InfoTypeStats](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.InfoTypeStats)` Statistics of how many instances of each info type were found during inspect job.  
`num_rows_processed` |  `int64` Number of rows scanned after sampling and time filtering (applicable for row based stores such as BigQuery).  
`hybrid_stats` |  `[HybridInspectStatistics](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.HybridInspectStatistics)` Statistics related to the processing of hybrid inspect.  
  
## InspectJobConfig

Controls what and how to inspect for findings.

Fields  
---  
`storage_config` |  `[StorageConfig](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.StorageConfig)` The data to scan.  
`inspect_config` |  `[InspectConfig](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.InspectConfig)` How and what to scan for.  
`inspect_template_name` |  `string` If provided, will be used as the default for all values in InspectConfig. `inspect_config` will be merged into the values persisted as part of the template.  
`actions[]` |  `[Action](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.Action)` Actions to execute at the completion of the job.  
  
## InspectResult

All the findings for a single scanned item.

Fields  
---  
`findings[]` |  `[Finding](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.Finding)` List of findings for an item.  
`findings_truncated` |  `bool` If true, then this item might have more findings than were returned, and the findings returned are an arbitrary subset of all findings. The findings list might be truncated because the input items were too large, or because the server reached the maximum amount of resources allowed for a single API call. For best results, divide the input into smaller batches.  
  
## InspectTemplate

The inspectTemplate contains a configuration (set of types of sensitive data to be detected) to be used anywhere you otherwise would normally specify InspectConfig. See <https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-templates> to learn more.

Fields  
---  
`name` |  `string` Output only. The template name.The template will have one of the following formats: `projects/PROJECT_ID/inspectTemplates/TEMPLATE_ID` OR `organizations/ORGANIZATION_ID/inspectTemplates/TEMPLATE_ID`;  
`display_name` |  `string` Display name (max 256 chars).  
`description` |  `string` Short description (max 256 chars).  
`create_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. The creation timestamp of an inspectTemplate.  
`update_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. The last update timestamp of an inspectTemplate.  
`inspect_config` |  `[InspectConfig](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.InspectConfig)` The core content of the template. Configuration of the scanning process.  
`allow_limited_availability_info_types` |  `bool` Optional. Enables the use of [limited-availability built-in infoTypes](https://docs.cloud.google.com/sensitive-data-protection/docs/infotypes-reference#limited-availability-infotypes) in inspect_config. These infoTypes are supported only in specific regions and can cause scanning errors if used elsewhere.  
  
## InspectionRule

A single inspection rule to be applied to infoTypes, specified in `InspectionRuleSet`.

Fields  
---  
Union field `type`. Inspection rule types. `type` can be only one of the following:  
`hotword_rule` |  `[HotwordRule](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.CustomInfoType.DetectionRule.HotwordRule)` Hotword-based detection rule.  
`exclusion_rule` |  `[ExclusionRule](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ExclusionRule)` Exclusion rule.  
`adjustment_rule` |  `[AdjustmentRule](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.AdjustmentRule)` Adjustment rule.  
  
## InspectionRuleSet

Rule set for modifying a set of infoTypes to alter behavior under certain circumstances, depending on the specific details of the rules within the set.

Fields  
---  
`info_types[]` |  `[InfoType](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.InfoType)` List of infoTypes this rule set is applied to.  
`rules[]` |  `[InspectionRule](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.InspectionRule)` Set of rules to be applied to infoTypes. The rules are applied in order.  
  
## JobTrigger

Contains a configuration to make API calls on a repeating basis. See <https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-job-triggers> to learn more.

Fields  
---  
`name` |  `string` Output only. Unique resource name for the triggeredJob, assigned by the service when the triggeredJob is created, for example `projects/dlp-test-project/jobTriggers/53234423`.  
`display_name` |  `string` Display name (max 100 chars)  
`description` |  `string` User provided description (max 256 chars)  
`triggers[]` |  `[Trigger](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.JobTrigger.Trigger)` A list of triggers which will be OR'ed together. Only one in the list needs to trigger for a job to be started. The list may contain only a single Schedule trigger and must have at least one object.  
`errors[]` |  `[Error](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.Error)` Output only. A stream of errors encountered when the trigger was activated. Repeated errors may result in the JobTrigger automatically being paused. Will return the last 100 errors. Whenever the JobTrigger is modified this list will be cleared.  
`create_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. The creation timestamp of a triggeredJob.  
`update_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. The last update timestamp of a triggeredJob.  
`last_run_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. The timestamp of the last time this trigger executed.  
`status` |  `[Status](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.JobTrigger.Status)` Required. A status for this trigger.  
Union field `job`. The configuration details for the specific type of job to run. `job` can be only one of the following:  
`inspect_job` |  `[InspectJobConfig](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.InspectJobConfig)` For inspect jobs, a snapshot of the configuration.  
  
## Status

Whether the trigger is currently active. If PAUSED or CANCELLED, no jobs will be created with this configuration. The service may automatically pause triggers experiencing frequent errors. To restart a job, set the status to HEALTHY after correcting user errors.

Enums  
---  
`STATUS_UNSPECIFIED` | Unused.  
`HEALTHY` | Trigger is healthy.  
`PAUSED` | Trigger is temporarily paused.  
`CANCELLED` | Trigger is cancelled and can not be resumed.  
  
## Trigger

What event needs to occur for a new job to be started.

Fields  
---  
Union field `trigger`. What event needs to occur for a new job to be started. `trigger` can be only one of the following:  
`schedule` |  `[Schedule](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.Schedule)` Create a job on a repeating basis based on the elapse of time.  
`manual` |  `[Manual](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.Manual)` For use with hybrid jobs. Jobs must be manually created and finished.  
  
## Key

A unique identifier for a Datastore entity. If a key's partition ID or any of its path kinds or names are reserved/read-only, the key is reserved/read-only. A reserved/read-only key is forbidden in certain documented contexts.

Fields  
---  
`partition_id` |  `[PartitionId](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.PartitionId)` Entities are partitioned into subsets, currently identified by a project ID and namespace ID. Queries are scoped to a single partition.  
`path[]` |  `[PathElement](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.Key.PathElement)` The entity path. An entity path consists of one or more elements composed of a kind and a string or numerical identifier, which identify entities. The first element identifies a _root entity_ , the second element identifies a _child_ of the root entity, the third element identifies a child of the second entity, and so forth. The entities identified by all prefixes of the path are called the element's _ancestors_.A path can never be empty, and a path can have at most 100 elements.  
  
## PathElement

A (kind, ID/name) pair used to construct a key path.

If either name or ID is set, the element is complete. If neither is set, the element is incomplete.

Fields  
---  
`kind` |  `string` The kind of the entity. A kind matching regex `__.*__` is reserved/read-only. A kind must not contain more than 1500 bytes when UTF-8 encoded. Cannot be `""`.  
Union field `id_type`. The type of ID. `id_type` can be only one of the following:  
`id` |  `int64` The auto-allocated ID of the entity. Never equal to zero. Values less than zero are discouraged and may not be supported in the future.  
`name` |  `string` The name of the entity. A name matching regex `__.*__` is reserved/read-only. A name must not be more than 1500 bytes when UTF-8 encoded. Cannot be `""`.  
  
## KeyValueMetadataLabel

The metadata key that contains a finding.

Fields  
---  
`key` |  `string` The metadata key. The format depends on the source of the metadata.Example:

  * `MSIP_Label_122709e3-8f6b-4860-985f-7f722a94f61e_Enabled` (a Microsoft Purview Information Protection key example)

  
  
## KeyValueMetadataProperty

A key-value pair in the Metadata.

Fields  
---  
`key` |  `string` The key of the property.  
`value` |  `string` The value of the property.  
  
## KindExpression

A representation of a Datastore kind.

Fields  
---  
`name` |  `string` The name of the kind.  
  
## KmsWrappedCryptoKey

Include to use an existing data crypto key wrapped by KMS. The wrapped key must be a 128-, 192-, or 256-bit key. Authorization requires the following IAM permissions when sending a request to perform a crypto transformation using a KMS-wrapped crypto key: dlp.kms.encrypt

For more information, see [Creating a wrapped key](https://docs.cloud.google.com/sensitive-data-protection/docs/create-wrapped-key).

Note: When you use Cloud KMS for cryptographic operations, [charges apply](https://cloud.google.com/kms/pricing).

Fields  
---  
`wrapped_key` |  `bytes` Required. The wrapped data crypto key.  
`crypto_key_name` |  `string` Required. The resource name of the KMS CryptoKey to use for unwrapping.  
  
## LargeCustomDictionaryConfig

Configuration for a custom dictionary created from a data source of any size up to the maximum size defined in the [limits](https://docs.cloud.google.com/sensitive-data-protection/limits) page. The artifacts of dictionary creation are stored in the specified Cloud Storage location. Consider using `CustomInfoType.Dictionary` for smaller dictionaries that satisfy the size requirements.

Fields  
---  
`output_path` |  `[CloudStoragePath](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.CloudStoragePath)` Location to store dictionary artifacts in Cloud Storage. These files will only be accessible by project owners and the DLP API. If any of these artifacts are modified, the dictionary is considered invalid and can no longer be used.  
Union field `source`. Source of the dictionary. `source` can be only one of the following:  
`cloud_storage_file_set` |  `[CloudStorageFileSet](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.CloudStorageFileSet)` Set of files containing newline-delimited lists of dictionary phrases.  
`big_query_field` |  `[BigQueryField](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.BigQueryField)` Field in a BigQuery table where each cell represents a dictionary phrase.  
  
## LargeCustomDictionaryStats

Summary statistics of a custom dictionary.

Fields  
---  
`approx_num_phrases` |  `int64` Approximate number of distinct phrases in the dictionary.  
  
## Likelihood

Coarse-grained confidence level of how well a particular finding satisfies the criteria to match a particular infoType.

Likelihood is calculated based on the number of signals a finding has that implies that the finding matches the infoType. For example, a string that has an '@' and a '.com' is more likely to be a match for an email address than a string that only has an '@'.

In general, the highest likelihood level has the strongest signals that indicate a match. That is, a finding with a high likelihood has a low chance of being a false positive.

For more information about each likelihood level and how likelihood works, see [Match likelihood](https://docs.cloud.google.com/sensitive-data-protection/docs/likelihood).

Enums  
---  
`LIKELIHOOD_UNSPECIFIED` | Default value; same as POSSIBLE.  
`VERY_UNLIKELY` | Highest chance of a false positive.  
`UNLIKELY` | High chance of a false positive.  
`POSSIBLE` | Some matching signals. The default value.  
`LIKELY` | Low chance of a false positive.  
`VERY_LIKELY` | Confidence level is high. Lowest chance of a false positive.  
  
## ListColumnDataProfilesRequest

Request to list the profiles generated for a given organization or project.

Fields  
---  
`parent` |  `string` Required. Resource name of the organization or project, for example `organizations/433245324/locations/europe` or `projects/project-id/locations/asia`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `dlp.columnDataProfiles.list`

  
`page_token` |  `string` Page token to continue retrieval.  
`page_size` |  `int32` Size of the page. This value can be limited by the server. If zero, server returns a page of max size 100.  
`order_by` |  `string` Comma-separated list of fields to order by, followed by `asc` or `desc` postfix. This list is case insensitive. The default sorting order is ascending. Redundant space characters are insignificant. Only one order field at a time is allowed.Examples:

  * `project_id asc`
  * `table_id`
  * `sensitivity_level desc`

Supported fields are:

  * `project_id`: The Google Cloud project ID.
  * `dataset_id`: The ID of a BigQuery dataset.
  * `table_id`: The ID of a BigQuery table.
  * `sensitivity_level`: How sensitive the data in a column is, at most.
  * `data_risk_level`: How much risk is associated with this data.
  * `profile_last_generated`: When the profile was last updated in epoch seconds.

  
`filter` |  `string` Allows filtering.Supported syntax:

  * Filter expressions are made up of one or more restrictions.
  * Restrictions can be combined by `AND` or `OR` logical operators. A sequence of restrictions implicitly uses `AND`.
  * A restriction has the form of `{field} {operator} {value}`.
  * Supported fields: 
    * `table_data_profile_name`: The name of the related table data profile
    * `project_id`: The Google Cloud project ID (REQUIRED)
    * `dataset_id`: The BigQuery dataset ID (REQUIRED)
    * `table_id`: The BigQuery table ID (REQUIRED)
    * `field_id`: The ID of the BigQuery field
    * `info_type`: The infotype detected in the resource
    * `sensitivity_level`: HIGH|MEDIUM|LOW
    * `data_risk_level`: How much risk is associated with this data
    * `status_code`: An RPC status code as defined in <https://github.com/googleapis/googleapis/blob/master/google/rpc/code.proto>
    * `profile_last_generated`: Date and time the profile was last generated
  * The operator must be `=` for project_id, dataset_id, and table_id. Other filters also support `!=`. The `profile_last_generated` filter also supports `<` and `>`.

The syntax is based on <https://google.aip.dev/160>.Examples:

  * project_id = 12345 AND status_code = 1
  * project_id = 12345 AND sensitivity_level = HIGH
  * project_id = 12345 AND info_type = STREET_ADDRESS
  * profile_last_generated < "2025-01-01T00:00:00.000Z"

The length of this field should be no more than 500 characters.  
  
## ListColumnDataProfilesResponse

List of profiles generated for a given organization or project.

Fields  
---  
`column_data_profiles[]` |  `[ColumnDataProfile](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ColumnDataProfile)` List of data profiles.  
`next_page_token` |  `string` The next page token.  
  
## ListConnectionsRequest

Request message for ListConnections.

Fields  
---  
`parent` |  `string` Required. Resource name of the organization or project, for example, `organizations/433245324/locations/europe` or `projects/project-id/locations/asia`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `dlp.connections.list`

  
`page_size` |  `int32` Optional. Number of results per page, max 1000.  
`page_token` |  `string` Optional. Page token from a previous page to return the next set of results. If set, all other request fields must match the original request.  
`filter` |  `string` Optional. Supported field/value: `state` \- MISSING|AVAILABLE|ERRORThe syntax is based on <https://google.aip.dev/160>.  
  
## ListConnectionsResponse

Response message for ListConnections.

Fields  
---  
`connections[]` |  `[Connection](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.Connection)` List of connections.  
`next_page_token` |  `string` Token to retrieve the next page of results. An empty value means there are no more results.  
  
## ListContentPoliciesRequest

Request message for ListContentPolicies.

Fields  
---  
`parent` |  `string` Required. Resource name of the project, for example, `projects/project-id/locations/asia`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `dlp.contentPolicies.list`

  
`page_size` |  `int32` Optional. Number of results per page, max 1000.  
`page_token` |  `string` Optional. Page token from a previous page to return the next set of results. If set, all other request fields must match the original request.  
  
## ListContentPoliciesResponse

Response message for ListContentPolicies.

Fields  
---  
`content_policies[]` |  `[ContentPolicy](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ContentPolicy)` List of content policies.  
`next_page_token` |  `string` Token to retrieve the next page of results. An empty value means there are no more results.  
  
## ListDeidentifyTemplatesRequest

Request message for ListDeidentifyTemplates.

Fields  
---  
`parent` |  `string` Required. Parent resource name.The format of this value varies depending on the scope of the request (project or organization) and whether you have [specified a processing location](https://docs.cloud.google.com/sensitive-data-protection/docs/specifying-location):

  * Projects scope, location specified: `projects/{project_id}/locations/{location_id}`
  * Projects scope, no location specified (defaults to global): `projects/{project_id}`
  * Organizations scope, location specified: `organizations/{org_id}/locations/{location_id}`
  * Organizations scope, no location specified (defaults to global): `organizations/{org_id}`

The following example `parent` string specifies a parent project with the identifier `example-project`, and specifies the `europe-west3` location for processing data:
    
    
    parent=projects/example-project/locations/europe-west3
    

Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `dlp.deidentifyTemplates.list`

  
`page_token` |  `string` Page token to continue retrieval. Comes from the previous call to `ListDeidentifyTemplates`.  
`page_size` |  `int32` Size of the page. This value can be limited by the server. If zero server returns a page of max size 100.  
`order_by` |  `string` Comma-separated list of fields to order by, followed by `asc` or `desc` postfix. This list is case insensitive. The default sorting order is ascending. Redundant space characters are insignificant.Example: `name asc,update_time, create_time desc`Supported fields are:

  * `create_time`: corresponds to the time the template was created.
  * `update_time`: corresponds to the time the template was last updated.
  * `name`: corresponds to the template's name.
  * `display_name`: corresponds to the template's display name.

  
`location_id` |  `string` Deprecated. This field has no effect.  
  
## ListDeidentifyTemplatesResponse

Response message for ListDeidentifyTemplates.

Fields  
---  
`deidentify_templates[]` |  `[DeidentifyTemplate](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DeidentifyTemplate)` List of deidentify templates, up to page_size in ListDeidentifyTemplatesRequest.  
`next_page_token` |  `string` If the next page is available then the next page token to be used in the following ListDeidentifyTemplates request.  
  
## ListDiscoveryConfigsRequest

Request message for ListDiscoveryConfigs.

Fields  
---  
`parent` |  `string` Required. Parent resource name.The format of this value is as follows: `projects/{project_id}/locations/{location_id}`The following example `parent` string specifies a parent project with the identifier `example-project`, and specifies the `europe-west3` location for processing data:
    
    
    parent=projects/example-project/locations/europe-west3
    

Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `dlp.jobTriggers.list`

  
`page_token` |  `string` Page token to continue retrieval. Comes from the previous call to ListDiscoveryConfigs. `order_by` field must not change for subsequent calls.  
`page_size` |  `int32` Size of the page. This value can be limited by a server.  
`order_by` |  `string` Comma-separated list of config fields to order by, followed by `asc` or `desc` postfix. This list is case insensitive. The default sorting order is ascending. Redundant space characters are insignificant.Example: `name asc,update_time, create_time desc`Supported fields are:

  * `last_run_time`: corresponds to the last time the DiscoveryConfig ran.
  * `name`: corresponds to the DiscoveryConfig's name.
  * `status`: corresponds to DiscoveryConfig's status.

  
  
## ListDiscoveryConfigsResponse

Response message for ListDiscoveryConfigs.

Fields  
---  
`discovery_configs[]` |  `[DiscoveryConfig](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DiscoveryConfig)` List of configs, up to page_size in ListDiscoveryConfigsRequest.  
`next_page_token` |  `string` If the next page is available then this value is the next page token to be used in the following ListDiscoveryConfigs request.  
  
## ListDlpJobsRequest

The request message for listing DLP jobs.

Fields  
---  
`parent` |  `string` Required. Parent resource name.The format of this value varies depending on whether you have [specified a processing location](https://docs.cloud.google.com/sensitive-data-protection/docs/specifying-location):

  * Projects scope, location specified: `projects/{project_id}/locations/{location_id}`
  * Projects scope, no location specified (defaults to global): `projects/{project_id}`

The following example `parent` string specifies a parent project with the identifier `example-project`, and specifies the `europe-west3` location for processing data:
    
    
    parent=projects/example-project/locations/europe-west3
    

Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `dlp.jobs.list`

  
`filter` |  `string` Allows filtering.Supported syntax:

  * Filter expressions are made up of one or more restrictions.
  * Restrictions can be combined by `AND` or `OR` logical operators. A sequence of restrictions implicitly uses `AND`.
  * A restriction has the form of `{field} {operator} {value}`.
  * Supported fields/values for inspect jobs: 
    * `state` \- PENDING|RUNNING|CANCELED|FINISHED|FAILED
    * `inspected_storage` \- DATASTORE|CLOUD_STORAGE|BIGQUERY
    * `trigger_name` \- The name of the trigger that created the job.
    * 'end_time` - Corresponds to the time the job finished.
    * 'start_time` - Corresponds to the time the job finished.
  * Supported fields for risk analysis jobs: 
    * `state` \- RUNNING|CANCELED|FINISHED|FAILED
    * 'end_time` - Corresponds to the time the job finished.
    * 'start_time` - Corresponds to the time the job finished.
  * The operator must be `=` or `!=`.

The syntax is based on <https://google.aip.dev/160>.Examples:

  * inspected_storage = cloud_storage AND state = done
  * inspected_storage = cloud_storage OR inspected_storage = bigquery
  * inspected_storage = cloud_storage AND (state = done OR state = canceled)
  * end_time > "2017-12-12T00:00:00+00:00"

The length of this field should be no more than 500 characters.  
`page_size` |  `int32` The standard list page size.  
`page_token` |  `string` The standard list page token.  
`type` |  `[DlpJobType](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DlpJobType)` The type of job. Defaults to `DlpJobType.INSPECT`  
`order_by` |  `string` Comma-separated list of fields to order by, followed by `asc` or `desc` postfix. This list is case insensitive. The default sorting order is ascending. Redundant space characters are insignificant.Example: `name asc, end_time asc, create_time desc`Supported fields are:

  * `create_time`: corresponds to the time the job was created.
  * `end_time`: corresponds to the time the job ended.
  * `name`: corresponds to the job's name.
  * `state`: corresponds to `state`

  
`location_id` |  `string` Deprecated. This field has no effect.  
  
## ListDlpJobsResponse

The response message for listing DLP jobs.

Fields  
---  
`jobs[]` |  `[DlpJob](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DlpJob)` A list of DlpJobs that matches the specified filter in the request.  
`next_page_token` |  `string` The standard List next-page token.  
  
## ListFileStoreDataProfilesRequest

Request to list the file store profiles generated for a given organization or project.

Fields  
---  
`parent` |  `string` Required. Resource name of the organization or project, for example `organizations/433245324/locations/europe` or `projects/project-id/locations/asia`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `dlp.fileStoreProfiles.list`

  
`page_token` |  `string` Optional. Page token to continue retrieval.  
`page_size` |  `int32` Optional. Size of the page. This value can be limited by the server. If zero, server returns a page of max size 100.  
`order_by` |  `string` Optional. Comma-separated list of fields to order by, followed by `asc` or `desc` postfix. This list is case insensitive. The default sorting order is ascending. Redundant space characters are insignificant. Only one order field at a time is allowed.Examples:

  * `project_id asc`
  * `name`
  * `sensitivity_level desc`

Supported fields are:

  * `project_id`: The Google Cloud project ID.
  * `sensitivity_level`: How sensitive the data in a table is, at most.
  * `data_risk_level`: How much risk is associated with this data.
  * `profile_last_generated`: When the profile was last updated in epoch seconds.
  * `last_modified`: The last time the resource was modified.
  * `resource_visibility`: Visibility restriction for this resource.
  * `name`: The name of the profile.
  * `create_time`: The time the file store was first created.

  
`filter` |  `string` Optional. Allows filtering.Supported syntax:

  * Filter expressions are made up of one or more restrictions.
  * Restrictions can be combined by `AND` or `OR` logical operators. A sequence of restrictions implicitly uses `AND`.
  * A restriction has the form of `{field} {operator} {value}`.
  * Supported fields: 
    * `project_id`: The Google Cloud project ID
    * `account_id`: The AWS account ID
    * `file_store_path`: The path like "gs://bucket"
    * `data_source_type`: The profile's data source type, like "google/storage/bucket"
    * `data_storage_location`: The location where the file store's data is stored, like "us-central1"
    * `sensitivity_level`: HIGH|MODERATE|LOW
    * `data_risk_level`: HIGH|MODERATE|LOW
    * `resource_visibility`: PUBLIC|RESTRICTED
    * `status_code`: an RPC status code as defined in <https://github.com/googleapis/googleapis/blob/master/google/rpc/code.proto>
    * `profile_last_generated`: Date and time the profile was last generated
  * The operator must be `=` or `!=`. The `profile_last_generated` filter also supports `<` and `>`.

The syntax is based on <https://google.aip.dev/160>.Examples:

  * `project_id = 12345 AND status_code = 1`
  * `project_id = 12345 AND sensitivity_level = HIGH`
  * `project_id = 12345 AND resource_visibility = PUBLIC`
  * `file_store_path = "gs://mybucket"`
  * `profile_last_generated < "2025-01-01T00:00:00.000Z"`

The length of this field should be no more than 500 characters.  
  
## ListFileStoreDataProfilesResponse

List of file store data profiles generated for a given organization or project.

Fields  
---  
`file_store_data_profiles[]` |  `[FileStoreDataProfile](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.FileStoreDataProfile)` List of data profiles.  
`next_page_token` |  `string` The next page token.  
  
## ListInfoTypesRequest

Request for the list of infoTypes.

Fields  
---  
`parent` |  `string` The parent resource name.The format of this value is as follows:
    
    
    `locations/{location_id}`
      
  
`language_code` |  `string` BCP-47 language code for localized infoType friendly names. If omitted, or if localized strings are not available, en-US strings will be returned.  
`filter` |  `string` filter to only return infoTypes supported by certain parts of the API. Defaults to supported_by=INSPECT.  
`location_id` |  `string` Deprecated. This field has no effect.  
  
## ListInfoTypesResponse

Response to the ListInfoTypes request.

Fields  
---  
`info_types[]` |  `[InfoTypeDescription](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.InfoTypeDescription)` Set of sensitive infoTypes.  
  
## ListInspectTemplatesRequest

Request message for ListInspectTemplates.

Fields  
---  
`parent` |  `string` Required. Parent resource name.The format of this value varies depending on the scope of the request (project or organization) and whether you have [specified a processing location](https://docs.cloud.google.com/sensitive-data-protection/docs/specifying-location):

  * Projects scope, location specified: `projects/{project_id}/locations/{location_id}`
  * Projects scope, no location specified (defaults to global): `projects/{project_id}`
  * Organizations scope, location specified: `organizations/{org_id}/locations/{location_id}`
  * Organizations scope, no location specified (defaults to global): `organizations/{org_id}`

The following example `parent` string specifies a parent project with the identifier `example-project`, and specifies the `europe-west3` location for processing data:
    
    
    parent=projects/example-project/locations/europe-west3
    

Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `dlp.inspectTemplates.list`

  
`page_token` |  `string` Page token to continue retrieval. Comes from the previous call to `ListInspectTemplates`.  
`page_size` |  `int32` Size of the page. This value can be limited by the server. If zero server returns a page of max size 100.  
`order_by` |  `string` Comma-separated list of fields to order by, followed by `asc` or `desc` postfix. This list is case insensitive. The default sorting order is ascending. Redundant space characters are insignificant.Example: `name asc,update_time, create_time desc`Supported fields are:

  * `create_time`: corresponds to the time the template was created.
  * `update_time`: corresponds to the time the template was last updated.
  * `name`: corresponds to the template's name.
  * `display_name`: corresponds to the template's display name.

  
`location_id` |  `string` Deprecated. This field has no effect.  
  
## ListInspectTemplatesResponse

Response message for ListInspectTemplates.

Fields  
---  
`inspect_templates[]` |  `[InspectTemplate](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.InspectTemplate)` List of inspectTemplates, up to page_size in ListInspectTemplatesRequest.  
`next_page_token` |  `string` If the next page is available then the next page token to be used in the following ListInspectTemplates request.  
  
## ListJobTriggersRequest

Request message for ListJobTriggers.

Fields  
---  
`parent` |  `string` Required. Parent resource name.The format of this value varies depending on whether you have [specified a processing location](https://docs.cloud.google.com/sensitive-data-protection/docs/specifying-location):

  * Projects scope, location specified: `projects/{project_id}/locations/{location_id}`
  * Projects scope, no location specified (defaults to global): `projects/{project_id}`

The following example `parent` string specifies a parent project with the identifier `example-project`, and specifies the `europe-west3` location for processing data:
    
    
    parent=projects/example-project/locations/europe-west3
    

Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `dlp.jobTriggers.list`

  
`page_token` |  `string` Page token to continue retrieval. Comes from the previous call to ListJobTriggers. `order_by` field must not change for subsequent calls.  
`page_size` |  `int32` Size of the page. This value can be limited by a server.  
`order_by` |  `string` Comma-separated list of triggeredJob fields to order by, followed by `asc` or `desc` postfix. This list is case insensitive. The default sorting order is ascending. Redundant space characters are insignificant.Example: `name asc,update_time, create_time desc`Supported fields are:

  * `create_time`: corresponds to the time the JobTrigger was created.
  * `update_time`: corresponds to the time the JobTrigger was last updated.
  * `last_run_time`: corresponds to the last time the JobTrigger ran.
  * `name`: corresponds to the JobTrigger's name.
  * `display_name`: corresponds to the JobTrigger's display name.
  * `status`: corresponds to JobTrigger's status.

  
`filter` |  `string` Allows filtering.Supported syntax:

  * Filter expressions are made up of one or more restrictions.
  * Restrictions can be combined by `AND` or `OR` logical operators. A sequence of restrictions implicitly uses `AND`.
  * A restriction has the form of `{field} {operator} {value}`.
  * Supported fields/values for inspect triggers: 
    * `status` \- HEALTHY|PAUSED|CANCELLED
    * `inspected_storage` \- DATASTORE|CLOUD_STORAGE|BIGQUERY
    * 'last_run_time` - RFC 3339 formatted timestamp, surrounded by quotation marks. Nanoseconds are ignored.
    * 'error_count' - Number of errors that have occurred while running.
  * The operator must be `=` or `!=` for status and inspected_storage.

The syntax is based on <https://google.aip.dev/160>.Examples:

  * inspected_storage = cloud_storage AND status = HEALTHY
  * inspected_storage = cloud_storage OR inspected_storage = bigquery
  * inspected_storage = cloud_storage AND (state = PAUSED OR state = HEALTHY)
  * last_run_time > "2017-12-12T00:00:00+00:00"

The length of this field should be no more than 500 characters.  
`type` |  `[DlpJobType](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DlpJobType)` The type of jobs. Will use `DlpJobType.INSPECT` if not set.  
`location_id` |  `string` Deprecated. This field has no effect.  
  
## ListJobTriggersResponse

Response message for ListJobTriggers.

Fields  
---  
`job_triggers[]` |  `[JobTrigger](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.JobTrigger)` List of triggeredJobs, up to page_size in ListJobTriggersRequest.  
`next_page_token` |  `string` If the next page is available then this value is the next page token to be used in the following ListJobTriggers request.  
  
## ListProjectDataProfilesRequest

Request to list the profiles generated for a given organization or project.

Fields  
---  
`parent` |  `string` Required. organizations/{org_id}/locations/{loc_id} Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `dlp.projectDataProfiles.list`

  
`page_token` |  `string` Page token to continue retrieval.  
`page_size` |  `int32` Size of the page. This value can be limited by the server. If zero, server returns a page of max size 100.  
`order_by` |  `string` Comma-separated list of fields to order by, followed by `asc` or `desc` postfix. This list is case insensitive. The default sorting order is ascending. Redundant space characters are insignificant. Only one order field at a time is allowed.Examples: * `project_id` * `sensitivity_level desc`Supported fields:

  * `project_id`: Google Cloud project ID
  * `sensitivity_level`: How sensitive the data in a project is, at most
  * `data_risk_level`: How much risk is associated with this data
  * `profile_last_generated`: Date and time (in epoch seconds) the profile was last generated

  
`filter` |  `string` Allows filtering.Supported syntax:

  * Filter expressions are made up of one or more restrictions.
  * Restrictions can be combined by `AND` or `OR` logical operators. A sequence of restrictions implicitly uses `AND`.
  * A restriction has the form of `{field} {operator} {value}`.
  * Supported fields: 
    * `project_id`: the Google Cloud project ID
    * `sensitivity_level`: HIGH|MODERATE|LOW
    * `data_risk_level`: HIGH|MODERATE|LOW
    * `status_code`: an RPC status code as defined in <https://github.com/googleapis/googleapis/blob/master/google/rpc/code.proto>
    * `profile_last_generated`: Date and time the profile was last generated
  * The operator must be `=` or `!=`. The `profile_last_generated` filter also supports `<` and `>`.

The syntax is based on <https://google.aip.dev/160>.Examples:

  * `project_id = 12345 AND status_code = 1`
  * `project_id = 12345 AND sensitivity_level = HIGH`
  * `profile_last_generated < "2025-01-01T00:00:00.000Z"`

The length of this field should be no more than 500 characters.  
  
## ListProjectDataProfilesResponse

List of profiles generated for a given organization or project.

Fields  
---  
`project_data_profiles[]` |  `[ProjectDataProfile](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ProjectDataProfile)` List of data profiles.  
`next_page_token` |  `string` The next page token.  
  
## ListStoredInfoTypesRequest

Request message for ListStoredInfoTypes.

Fields  
---  
`parent` |  `string` Required. Parent resource name.The format of this value varies depending on the scope of the request (project or organization) and whether you have [specified a processing location](https://docs.cloud.google.com/sensitive-data-protection/docs/specifying-location):

  * Projects scope, location specified: `projects/{project_id}/locations/{location_id}`
  * Projects scope, no location specified (defaults to global): `projects/{project_id}`

The following example `parent` string specifies a parent project with the identifier `example-project`, and specifies the `europe-west3` location for processing data:
    
    
    parent=projects/example-project/locations/europe-west3
    

Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `dlp.storedInfoTypes.list`

  
`page_token` |  `string` Page token to continue retrieval. Comes from the previous call to `ListStoredInfoTypes`.  
`page_size` |  `int32` Size of the page. This value can be limited by the server. If zero server returns a page of max size 100.  
`order_by` |  `string` Comma-separated list of fields to order by, followed by `asc` or `desc` postfix. This list is case insensitive. The default sorting order is ascending. Redundant space characters are insignificant.Example: `name asc, display_name, create_time desc`Supported fields are:

  * `create_time`: corresponds to the time the most recent version of the resource was created.
  * `state`: corresponds to the state of the resource.
  * `name`: corresponds to resource name.
  * `display_name`: corresponds to info type's display name.

  
`location_id` |  `string` Deprecated. This field has no effect.  
  
## ListStoredInfoTypesResponse

Response message for ListStoredInfoTypes.

Fields  
---  
`stored_info_types[]` |  `[StoredInfoType](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.StoredInfoType)` List of storedInfoTypes, up to page_size in ListStoredInfoTypesRequest.  
`next_page_token` |  `string` If the next page is available then the next page token to be used in the following ListStoredInfoTypes request.  
  
## ListTableDataProfilesRequest

Request to list the profiles generated for a given organization or project.

Fields  
---  
`parent` |  `string` Required. Resource name of the organization or project, for example `organizations/433245324/locations/europe` or `projects/project-id/locations/asia`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `dlp.tableDataProfiles.list`

  
`page_token` |  `string` Page token to continue retrieval.  
`page_size` |  `int32` Size of the page. This value can be limited by the server. If zero, server returns a page of max size 100.  
`order_by` |  `string` Comma-separated list of fields to order by, followed by `asc` or `desc` postfix. This list is case insensitive. The default sorting order is ascending. Redundant space characters are insignificant. Only one order field at a time is allowed.Examples: * `project_id asc` * `table_id` * `sensitivity_level desc`Supported fields are:

  * `project_id`: The Google Cloud project ID.
  * `dataset_id`: The ID of a BigQuery dataset.
  * `table_id`: The ID of a BigQuery table.
  * `sensitivity_level`: How sensitive the data in a table is, at most.
  * `data_risk_level`: How much risk is associated with this data.
  * `profile_last_generated`: When the profile was last updated in epoch seconds.
  * `last_modified`: The last time the resource was modified.
  * `resource_visibility`: Visibility restriction for this resource.
  * `row_count`: Number of rows in this resource.

  
`filter` |  `string` Allows filtering.Supported syntax:

  * Filter expressions are made up of one or more restrictions.
  * Restrictions can be combined by `AND` or `OR` logical operators. A sequence of restrictions implicitly uses `AND`.
  * A restriction has the form of `{field} {operator} {value}`.
  * Supported fields: 
    * `project_id`: The Google Cloud project ID
    * `dataset_id`: The BigQuery dataset ID
    * `table_id`: The ID of the BigQuery table
    * `sensitivity_level`: HIGH|MODERATE|LOW
    * `data_risk_level`: HIGH|MODERATE|LOW
    * `resource_visibility`: PUBLIC|RESTRICTED
    * `status_code`: an RPC status code as defined in <https://github.com/googleapis/googleapis/blob/master/google/rpc/code.proto>
    * `profile_last_generated`: Date and time the profile was last generated
  * The operator must be `=` or `!=`. The `profile_last_generated` filter also supports `<` and `>`.

The syntax is based on <https://google.aip.dev/160>.Examples:

  * `project_id = 12345 AND status_code = 1`
  * `project_id = 12345 AND sensitivity_level = HIGH`
  * `project_id = 12345 AND resource_visibility = PUBLIC`
  * `profile_last_generated < "2025-01-01T00:00:00.000Z"`

The length of this field should be no more than 500 characters.  
  
## ListTableDataProfilesResponse

List of profiles generated for a given organization or project.

Fields  
---  
`table_data_profiles[]` |  `[TableDataProfile](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.TableDataProfile)` List of data profiles.  
`next_page_token` |  `string` The next page token.  
  
## Location

Specifies the location of the finding.

Fields  
---  
`byte_range` |  `[Range](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.Range)` Zero-based byte offsets delimiting the finding. These are relative to the finding's containing element. Note that when the content is not textual, this references the UTF-8 encoded textual representation of the content. Omitted if content is an image.  
`codepoint_range` |  `[Range](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.Range)` Unicode character offsets delimiting the finding. These are relative to the finding's containing element. Provided when the content is text.  
`content_locations[]` |  `[ContentLocation](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ContentLocation)` List of nested objects pointing to the precise location of the finding within the file or record.  
`container` |  `[Container](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.Container)` Information about the container where this finding occurred, if available.  
  
## LocationSupport

Locations at which a feature can be used.

Fields  
---  
`regionalization_scope` |  `[RegionalizationScope](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.LocationSupport.RegionalizationScope)` The current scope for location on this feature. This may expand over time.  
`locations[]` |  `string` Specific locations where the feature may be used. Examples: us-central1, us, asia, global If scope is ANY_LOCATION, no regions will be listed.  
  
## RegionalizationScope

The location scope for a feature.

Enums  
---  
`REGIONALIZATION_SCOPE_UNSPECIFIED` | Invalid.  
`REGIONAL` | Feature may be used with one or more regions. See locations for details.  
`ANY_LOCATION` | Feature may be used anywhere. Default value.  
  
## Manual

This type has no fields.

Job trigger option for hybrid jobs. Jobs must be manually created and finished.

## MatchingType

Type of the match which can be applied to different ways of matching, like Dictionary, regular expression and intersecting with findings of another infoType.

Enums  
---  
`MATCHING_TYPE_UNSPECIFIED` | Invalid.  
`MATCHING_TYPE_FULL_MATCH` | Full match.

  * Dictionary: join of Dictionary results matched the complete finding quote
  * Regex: all regex matches fill a finding quote from start to end
  * Exclude infoType: completely inside affecting infoTypes findings

  
`MATCHING_TYPE_PARTIAL_MATCH` | Partial match.

  * Dictionary: at least one of the tokens in the finding matches
  * Regex: substring of the finding matches
  * Exclude infoType: intersects with affecting infoTypes findings

  
`MATCHING_TYPE_INVERSE_MATCH` | Inverse match.

  * Dictionary: no tokens in the finding match the dictionary
  * Regex: finding doesn't match the regex
  * Exclude infoType: no intersection with affecting infoTypes findings

  
`MATCHING_TYPE_RULE_SPECIFIC` | Rule-specific match.The matching logic is based on the specific rule being used. This is required for rules where the matching behavior is not a simple string comparison (e.g., image containment). This matching type can only be used with the `ExcludeByImageFindings` rule.

  * Exclude by image findings: The matching logic is defined within `ExcludeByImageFindings` based on spatial relationships between bounding boxes.

  
  
## MetadataLocation

Metadata Location

Fields  
---  
`type` |  `[MetadataType](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.MetadataType)` Type of metadata containing the finding.  
Union field `label`. Label of the piece of metadata containing the finding, for example - latitude, author, caption. `label` can be only one of the following:  
`storage_label` |  `[StorageMetadataLabel](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.StorageMetadataLabel)` Storage metadata.  
`key_value_metadata_label` |  `[KeyValueMetadataLabel](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.KeyValueMetadataLabel)` Metadata key that contains the finding.  
  
## MetadataType

Type of metadata containing the finding.

Enums  
---  
`METADATATYPE_UNSPECIFIED` | Unused  
`STORAGE_METADATA` | General file metadata provided by Cloud Storage.  
`CONTENT_METADATA` | Metadata extracted from the files.  
`CLIENT_PROVIDED_METADATA` | Metadata provided by the client.  
  
## NullPercentageLevel

Bucketized nullness percentage levels. A higher level means a higher percentage of the column is null.

Enums  
---  
`NULL_PERCENTAGE_LEVEL_UNSPECIFIED` | Unused.  
`NULL_PERCENTAGE_VERY_LOW` | Very few null entries.  
`NULL_PERCENTAGE_LOW` | Some null entries.  
`NULL_PERCENTAGE_MEDIUM` | A few null entries.  
`NULL_PERCENTAGE_HIGH` | A lot of null entries.  
  
## OtherCloudDiscoveryStartingLocation

The other cloud starting location for discovery.

Fields  
---  
Union field `location`. The other cloud starting location for discovery. `location` can be only one of the following:  
`aws_location` |  `[AwsDiscoveryStartingLocation](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.OtherCloudDiscoveryStartingLocation.AwsDiscoveryStartingLocation)` The AWS starting location for discovery.  
  
## AwsDiscoveryStartingLocation

The AWS starting location for discovery.

Fields  
---  
Union field `scope`. The scope of this starting location. `scope` can be only one of the following:  
`account_id` |  `string` The AWS account ID that this discovery config applies to. Within an AWS organization, you can find the AWS account ID inside an AWS account ARN. Example: arn:{partition}:organizations::{management_account_id}:account/{org_id}/{account_id}  
`all_asset_inventory_assets` |  `bool` All AWS assets stored in Asset Inventory that didn't match other AWS discovery configs.  
  
## OtherCloudDiscoveryTarget

Target used to match against for discovery of resources from other clouds. An [AWS connector in Security Command Center (Enterprise](https://docs.cloud.google.com/security-command-center/docs/connect-scc-to-aws) is required to use this feature.

Fields  
---  
`data_source_type` |  `[DataSourceType](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DataSourceType)` Required. The type of data profiles generated by this discovery target. Supported values are: * aws/s3/bucket  
`filter` |  `[DiscoveryOtherCloudFilter](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DiscoveryOtherCloudFilter)` Required. The resources that the discovery cadence applies to. The first target with a matching filter will be the one to apply to a resource.  
`conditions` |  `[DiscoveryOtherCloudConditions](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DiscoveryOtherCloudConditions)` Optional. In addition to matching the filter, these conditions must be true before a profile is generated.  
Union field `cadence`. Type of cadence. `cadence` can be only one of the following:  
`generation_cadence` |  `[DiscoveryOtherCloudGenerationCadence](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DiscoveryOtherCloudGenerationCadence)` How often and when to update data profiles. New resources that match both the filter and conditions are scanned as quickly as possible depending on system capacity.  
`disabled` |  `[Disabled](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.Disabled)` Disable profiling for resources that match this filter.  
  
## OtherCloudResourceCollection

Match resources using regex filters.

Fields  
---  
Union field `pattern`. The first filter containing a pattern that matches a resource will be used. `pattern` can be only one of the following:  
`include_regexes` |  `[OtherCloudResourceRegexes](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.OtherCloudResourceRegexes)` A collection of regular expressions to match a resource against.  
  
## OtherCloudResourceRegex

A pattern to match against one or more resources. At least one pattern must be specified. Regular expressions use RE2 [syntax](https://github.com/google/re2/wiki/Syntax); a guide can be found under the google/re2 repository on GitHub.

Fields  
---  
Union field `resource_regex`. The type of resource regex to use. `resource_regex` can be only one of the following:  
`amazon_s3_bucket_regex` |  `[AmazonS3BucketRegex](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.AmazonS3BucketRegex)` Regex for Amazon S3 buckets.  
  
## OtherCloudResourceRegexes

A collection of regular expressions to determine what resources to match against.

Fields  
---  
`patterns[]` |  `[OtherCloudResourceRegex](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.OtherCloudResourceRegex)` A group of regular expression patterns to match against one or more resources. Maximum of 100 entries. The sum of all regular expression's length can't exceed 10 KiB.  
  
## OtherCloudSingleResourceReference

Identifies a single resource, like a single Amazon S3 bucket.

Fields  
---  
Union field `resource`. The resource to scan. `resource` can be only one of the following:  
`amazon_s3_bucket` |  `[AmazonS3Bucket](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.AmazonS3Bucket)` Amazon S3 bucket.  
  
## OtherInfoTypeSummary

Infotype details for other infoTypes found within a column.

Fields  
---  
`info_type` |  `[InfoType](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.InfoType)` The other infoType.  
`estimated_prevalence` |  `int32` Approximate percentage of non-null rows that contained data detected by this infotype.  
`excluded_from_analysis` |  `bool` Whether this infoType was excluded from sensitivity and risk analysis due to factors such as low prevalence (subject to change).  
  
## OutputStorageConfig

Cloud repository for storing output.

Fields  
---  
`output_schema` |  `[OutputSchema](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.OutputStorageConfig.OutputSchema)` Schema used for writing the findings for Inspect jobs. This field is only used for Inspect and must be unspecified for Risk jobs. Columns are derived from the `Finding` object. If appending to an existing table, any columns from the predefined schema that are missing will be added. No columns in the existing table will be deleted.If unspecified, then all available columns will be used for a new table or an (existing) table with no schema, and no changes will be made to an existing table that has a schema. Only for use with external storage.  
Union field `type`. Output storage types. * `type` can be only one of the following:  
`table` |  `[BigQueryTable](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.BigQueryTable)` Store findings in an existing table or a new table in an existing dataset. If table_id is not set a new one will be generated for you with the following format: dlp_googleapis_yyyy_mm_dd_[dlp_job_id]. Pacific time zone will be used for generating the date details.For Inspect, each column in an existing output table must have the same name, type, and mode of a field in the `Finding` object.For Risk, an existing output table should be the output of a previous Risk analysis job run on the same source table, with the same privacy metric and quasi-identifiers. Risk jobs that analyze the same table but compute a different privacy metric, or use different sets of quasi-identifiers, cannot store their results in the same table.  
`storage_path` |  `[CloudStoragePath](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.CloudStoragePath)` Store findings in an existing Cloud Storage bucket. Files will be generated with the job ID and file part number as the filename and will contain findings in textproto format as `[SaveToGcsFindingsOutput](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.SaveToGcsFindingsOutput)`. The filename will follow the naming convention `<job_id>-<shard_number>`. Example: `my-job-id-2`.Supported for `[Inspect jobs](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.InspectJobConfig)`. The bucket must not be the same as the bucket being inspected. If storing findings to Cloud Storage, the output schema field should not be set. If set, it will be ignored.  
  
## OutputSchema

Predefined schemas for storing findings. Only for use with external storage.

Enums  
---  
`OUTPUT_SCHEMA_UNSPECIFIED` | Unused.  
`BASIC_COLUMNS` | Basic schema including only `info_type`, `quote`, `certainty`, and `timestamp`.  
`GCS_COLUMNS` | Schema tailored to findings from scanning Cloud Storage.  
`DATASTORE_COLUMNS` | Schema tailored to findings from scanning Google Datastore.  
`BIG_QUERY_COLUMNS` | Schema tailored to findings from scanning Google BigQuery.  
`ALL_COLUMNS` | Schema containing all columns.  
  
## Overlap

This type has no fields.

Defines a condition for overlapping bounding boxes.

## PartitionId

Datastore partition ID. A partition ID identifies a grouping of entities. The grouping is always by project and namespace, however the namespace ID may be empty.

A partition ID contains several dimensions: project ID and namespace ID.

Fields  
---  
`project_id` |  `string` The ID of the project to which the entities belong.  
`namespace_id` |  `string` If not empty, the ID of the namespace to which the entities belong.  
  
## PrimitiveTransformation

A rule for transforming a value.

Fields  
---  
Union field `transformation`. Type of transformation. `transformation` can be only one of the following:  
`replace_config` |  `[ReplaceValueConfig](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ReplaceValueConfig)` Replace with a specified value.  
`redact_config` |  `[RedactConfig](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.RedactConfig)` Redact  
`character_mask_config` |  `[CharacterMaskConfig](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.CharacterMaskConfig)` Mask  
`crypto_replace_ffx_fpe_config` |  `[CryptoReplaceFfxFpeConfig](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.CryptoReplaceFfxFpeConfig)` Ffx-Fpe. Strongly discouraged, consider using CryptoDeterministicConfig instead. Fpe is computationally expensive incurring latency costs.  
`fixed_size_bucketing_config` |  `[FixedSizeBucketingConfig](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.FixedSizeBucketingConfig)` Fixed size bucketing  
`bucketing_config` |  `[BucketingConfig](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.BucketingConfig)` Bucketing  
`replace_with_info_type_config` |  `[ReplaceWithInfoTypeConfig](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ReplaceWithInfoTypeConfig)` Replace with infotype  
`time_part_config` |  `[TimePartConfig](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.TimePartConfig)` Time extraction  
`crypto_hash_config` |  `[CryptoHashConfig](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.CryptoHashConfig)` Crypto  
`date_shift_config` |  `[DateShiftConfig](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DateShiftConfig)` Date Shift  
`crypto_deterministic_config` |  `[CryptoDeterministicConfig](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.CryptoDeterministicConfig)` Deterministic Crypto  
`replace_dictionary_config` |  `[ReplaceDictionaryConfig](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ReplaceDictionaryConfig)` Replace with a value randomly drawn (with replacement) from a dictionary.  
  
## PrivacyMetric

Privacy metric to compute for reidentification risk analysis.

Fields  
---  
Union field `type`. Types of analysis. `type` can be only one of the following:  
`numerical_stats_config` |  `[NumericalStatsConfig](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.PrivacyMetric.NumericalStatsConfig)` Numerical stats  
`categorical_stats_config` |  `[CategoricalStatsConfig](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.PrivacyMetric.CategoricalStatsConfig)` Categorical stats  
`k_anonymity_config` |  `[KAnonymityConfig](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.PrivacyMetric.KAnonymityConfig)` K-anonymity  
`l_diversity_config` |  `[LDiversityConfig](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.PrivacyMetric.LDiversityConfig)` l-diversity  
`k_map_estimation_config` |  `[KMapEstimationConfig](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.PrivacyMetric.KMapEstimationConfig)` k-map  
`delta_presence_estimation_config` |  `[DeltaPresenceEstimationConfig](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.PrivacyMetric.DeltaPresenceEstimationConfig)` delta-presence  
  
## CategoricalStatsConfig

Compute numerical stats over an individual column, including number of distinct values and value count distribution.

Fields  
---  
`field` |  `[FieldId](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.FieldId)` Field to compute categorical stats on. All column types are supported except for arrays and structs. However, it may be more informative to use NumericalStats when the field type is supported, depending on the data.  
  
## DeltaPresenceEstimationConfig

δ-presence metric, used to estimate how likely it is for an attacker to figure out that one given individual appears in a de-identified dataset. Similarly to the k-map metric, we cannot compute δ-presence exactly without knowing the attack dataset, so we use a statistical model instead.

Fields  
---  
`quasi_ids[]` |  `[QuasiId](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.QuasiId)` Required. Fields considered to be quasi-identifiers. No two fields can have the same tag.  
`region_code` |  `string` ISO 3166-1 alpha-2 region code to use in the statistical modeling. Set if no column is tagged with a region-specific InfoType (like US_ZIP_5) or a region code.  
`auxiliary_tables[]` |  `[StatisticalTable](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.StatisticalTable)` Several auxiliary tables can be used in the analysis. Each custom_tag used to tag a quasi-identifiers field must appear in exactly one field of one auxiliary table.  
  
## KAnonymityConfig

k-anonymity metric, used for analysis of reidentification risk.

Fields  
---  
`quasi_ids[]` |  `[FieldId](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.FieldId)` Set of fields to compute k-anonymity over. When multiple fields are specified, they are considered a single composite key. Structs and repeated data types are not supported; however, nested fields are supported so long as they are not structs themselves or nested within a repeated field.  
`entity_id` |  `[EntityId](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.EntityId)` Message indicating that multiple rows might be associated to a single individual. If the same entity_id is associated to multiple quasi-identifier tuples over distinct rows, we consider the entire collection of tuples as the composite quasi-identifier. This collection is a multiset: the order in which the different tuples appear in the dataset is ignored, but their frequency is taken into account.Important note: a maximum of 1000 rows can be associated to a single entity ID. If more rows are associated with the same entity ID, some might be ignored.  
  
## KMapEstimationConfig

Reidentifiability metric. This corresponds to a risk model similar to what is called "journalist risk" in the literature, except the attack dataset is statistically modeled instead of being perfectly known. This can be done using publicly available data (like the US Census), or using a custom statistical model (indicated as one or several BigQuery tables), or by extrapolating from the distribution of values in the input dataset.

Fields  
---  
`quasi_ids[]` |  `[TaggedField](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.PrivacyMetric.KMapEstimationConfig.TaggedField)` Required. Fields considered to be quasi-identifiers. No two columns can have the same tag.  
`region_code` |  `string` ISO 3166-1 alpha-2 region code to use in the statistical modeling. Set if no column is tagged with a region-specific InfoType (like US_ZIP_5) or a region code.  
`auxiliary_tables[]` |  `[AuxiliaryTable](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.PrivacyMetric.KMapEstimationConfig.AuxiliaryTable)` Several auxiliary tables can be used in the analysis. Each custom_tag used to tag a quasi-identifiers column must appear in exactly one column of one auxiliary table.  
  
## AuxiliaryTable

An auxiliary table contains statistical information on the relative frequency of different quasi-identifiers values. It has one or several quasi-identifiers columns, and one column that indicates the relative frequency of each quasi-identifier tuple. If a tuple is present in the data but not in the auxiliary table, the corresponding relative frequency is assumed to be zero (and thus, the tuple is highly reidentifiable).

Fields  
---  
`table` |  `[BigQueryTable](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.BigQueryTable)` Required. Auxiliary table location.  
`quasi_ids[]` |  `[QuasiIdField](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.PrivacyMetric.KMapEstimationConfig.AuxiliaryTable.QuasiIdField)` Required. Quasi-identifier columns.  
`relative_frequency` |  `[FieldId](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.FieldId)` Required. The relative frequency column must contain a floating-point number between 0 and 1 (inclusive). Null values are assumed to be zero.  
  
## QuasiIdField

A quasi-identifier column has a custom_tag, used to know which column in the data corresponds to which column in the statistical model.

Fields  
---  
`field` |  `[FieldId](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.FieldId)` Identifies the column.  
`custom_tag` |  `string` A auxiliary field.  
  
## TaggedField

A column with a semantic tag attached.

Fields  
---  
`field` |  `[FieldId](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.FieldId)` Required. Identifies the column.  
Union field `tag`. Semantic tag that identifies what a column contains, to determine which statistical model to use to estimate the reidentifiability of each value. [required] `tag` can be only one of the following:  
`info_type` |  `[InfoType](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.InfoType)` A column can be tagged with a InfoType to use the relevant public dataset as a statistical model of population, if available. We currently support US ZIP codes, region codes, ages and genders. To programmatically obtain the list of supported InfoTypes, use ListInfoTypes with the supported_by=RISK_ANALYSIS filter.  
`custom_tag` |  `string` A column can be tagged with a custom tag. In this case, the user must indicate an auxiliary table that contains statistical information on the possible values of this column.  
`inferred` |  `[Empty](https://protobuf.dev/reference/protobuf/google.protobuf/#empty)` If no semantic tag is indicated, we infer the statistical model from the distribution of values in the input data  
  
## LDiversityConfig

l-diversity metric, used for analysis of reidentification risk.

Fields  
---  
`quasi_ids[]` |  `[FieldId](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.FieldId)` Set of quasi-identifiers indicating how equivalence classes are defined for the l-diversity computation. When multiple fields are specified, they are considered a single composite key.  
`sensitive_attribute` |  `[FieldId](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.FieldId)` Sensitive field for computing the l-value.  
  
## NumericalStatsConfig

Compute numerical stats over an individual column, including min, max, and quantiles.

Fields  
---  
`field` |  `[FieldId](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.FieldId)` Field to compute numerical stats on. Supported types are integer, float, date, datetime, timestamp, time.  
  
## ProcessingLocation

Configure processing location for discovery and inspection. For example, image OCR is only provided in limited regions but configuring ProcessingLocation will redirect OCR to a location where OCR is provided.

Fields  
---  
`image_fallback_location` |  `[ImageFallbackLocation](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ProcessingLocation.ImageFallbackLocation)` Image processing falls back using this configuration.  
`document_fallback_location` |  `[DocumentFallbackLocation](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ProcessingLocation.DocumentFallbackLocation)` Document processing falls back using this configuration.  
  
## DocumentFallbackLocation

Configure document processing to fall back to any of the following processing options if document processing is unavailable in the original request location.

Fields  
---  
`multi_region_processing` |  `[MultiRegionProcessing](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ProcessingLocation.MultiRegionProcessing)` Processing occurs in a multi-region that contains the current region if available.  
`global_processing` |  `[GlobalProcessing](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ProcessingLocation.GlobalProcessing)` Processing occurs in the global region.  
  
## GlobalProcessing

This type has no fields.

Processing occurs in the global region.

## ImageFallbackLocation

Configure image processing to fall back to any of the following processing options if image processing is unavailable in the original request location.

Fields  
---  
`multi_region_processing` |  `[MultiRegionProcessing](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ProcessingLocation.MultiRegionProcessing)` Processing occurs in a multi-region that contains the current region if available.  
`global_processing` |  `[GlobalProcessing](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ProcessingLocation.GlobalProcessing)` Processing occurs in the global region.  
  
## MultiRegionProcessing

This type has no fields.

Processing occurs in a multi-region that contains the current region if available.

## ProfileGeneration

Whether a profile being created is the first generation or an update.

Enums  
---  
`PROFILE_GENERATION_UNSPECIFIED` | Unused.  
`PROFILE_GENERATION_NEW` | The profile is the first profile for the resource.  
`PROFILE_GENERATION_UPDATE` | The profile is an update to a previous profile.  
  
## ProfileStatus

Success or errors for the profile generation.

Fields  
---  
`status` |  `[Status](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.rpc#google.rpc.Status)` Profiling status code and optional message. The `status.code` value is 0 (default value) for OK.  
`timestamp` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Time when the profile generation status was updated  
  
## ProjectDataProfile

An aggregated profile for this project, based on the resources profiled within it.

Fields  
---  
`name` |  `string` The resource name of the profile.  
`project_id` |  `string` Project ID or account that was profiled.  
`profile_last_generated` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` The last time the profile was generated.  
`sensitivity_score` |  `[SensitivityScore](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.SensitivityScore)` The sensitivity score of this project.  
`data_risk_level` |  `[DataRiskLevel](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DataRiskLevel)` The data risk level of this project.  
`profile_status` |  `[ProfileStatus](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ProfileStatus)` Success or error status of the last attempt to profile the project.  
`table_data_profile_count` |  `int64` The number of table data profiles generated for this project.  
`file_store_data_profile_count` |  `int64` The number of file store data profiles generated for this project.  
  
## QuasiId

A column with a semantic tag attached.

Fields  
---  
`field` |  `[FieldId](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.FieldId)` Required. Identifies the column.  
Union field `tag`. Semantic tag that identifies what a column contains, to determine which statistical model to use to estimate the reidentifiability of each value. [required] `tag` can be only one of the following:  
`info_type` |  `[InfoType](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.InfoType)` A column can be tagged with a InfoType to use the relevant public dataset as a statistical model of population, if available. We currently support US ZIP codes, region codes, ages and genders. To programmatically obtain the list of supported InfoTypes, use ListInfoTypes with the supported_by=RISK_ANALYSIS filter.  
`custom_tag` |  `string` A column can be tagged with a custom tag. In this case, the user must indicate an auxiliary table that contains statistical information on the possible values of this column.  
`inferred` |  `[Empty](https://protobuf.dev/reference/protobuf/google.protobuf/#empty)` If no semantic tag is indicated, we infer the statistical model from the distribution of values in the input data  
  
## QuoteInfo

Message for infoType-dependent details parsed from quote.

Fields  
---  
Union field `parsed_quote`. Object representation of the quote. `parsed_quote` can be only one of the following:  
`date_time` |  `[DateTime](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DateTime)` The date time indicated by the quote.  
  
## Range

Generic half-open interval [start, end)

Fields  
---  
`start` |  `int64` Index of the first character of the range (inclusive).  
`end` |  `int64` Index of the last character of the range (exclusive).  
  
## RecordCondition

A condition for determining whether a transformation should be applied to a field.

Fields  
---  
`expressions` |  `[Expressions](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.RecordCondition.Expressions)` An expression.  
  
## Condition

The field type of `value` and `field` do not need to match to be considered equal, but not all comparisons are possible. EQUAL_TO and NOT_EQUAL_TO attempt to compare even with incompatible types, but all other comparisons are invalid with incompatible types. A `value` of type:

  * `string` can be compared against all other types
  * `boolean` can only be compared against other booleans
  * `integer` can be compared against doubles or a string if the string value can be parsed as an integer.
  * `double` can be compared against integers or a string if the string can be parsed as a double.
  * `Timestamp` can be compared against strings in RFC 3339 date string format.
  * `TimeOfDay` can be compared against timestamps and strings in the format of 'HH:mm:ss'.



If we fail to compare do to type mismatch, a warning will be given and the condition will evaluate to false.

Fields  
---  
`field` |  `[FieldId](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.FieldId)` Required. Field within the record this condition is evaluated against.  
`operator` |  `[RelationalOperator](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.RelationalOperator)` Required. Operator used to compare the field or infoType to the value.  
`value` |  `[Value](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.Value)` Value to compare against. [Mandatory, except for `EXISTS` tests.]  
  
## Conditions

A collection of conditions.

Fields  
---  
`conditions[]` |  `[Condition](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.RecordCondition.Condition)` A collection of conditions.  
  
## Expressions

An expression, consisting of an operator and conditions.

Fields  
---  
`logical_operator` |  `[LogicalOperator](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.RecordCondition.Expressions.LogicalOperator)` The operator to apply to the result of conditions. Default and currently only supported value is `AND`.  
Union field `type`. Expression types. `type` can be only one of the following:  
`conditions` |  `[Conditions](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.RecordCondition.Conditions)` Conditions to apply to the expression.  
  
## LogicalOperator

Logical operators for conditional checks.

Enums  
---  
`LOGICAL_OPERATOR_UNSPECIFIED` | Unused  
`AND` | Conditional AND  
  
## RecordKey

Message for a unique key indicating a record that contains a finding.

Fields  
---  
`id_values[]` |  `string` Values of identifying columns in the given row. Order of values matches the order of `identifying_fields` specified in the scanning request.  
Union field `type`. Type of key `type` can be only one of the following:  
`datastore_key` |  `[DatastoreKey](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DatastoreKey)` BigQuery key  
`big_query_key` |  `[BigQueryKey](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.BigQueryKey)` Datastore key  
  
## RecordLocation

Location of a finding within a row or record.

Fields  
---  
`record_key` |  `[RecordKey](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.RecordKey)` Key of the finding.  
`field_id` |  `[FieldId](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.FieldId)` Field id of the field containing the finding.  
`table_location` |  `[TableLocation](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.TableLocation)` Location within a `ContentItem.Table`.  
  
## RecordSuppression

Configuration to suppress records whose suppression conditions evaluate to true.

Fields  
---  
`condition` |  `[RecordCondition](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.RecordCondition)` A condition that when it evaluates to true will result in the record being evaluated to be suppressed from the transformed content.  
  
## RecordTransformation

The field in a record to transform.

Fields  
---  
`field_id` |  `[FieldId](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.FieldId)` For record transformations, provide a field.  
`container_timestamp` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Findings container modification timestamp, if applicable.  
`container_version` |  `string` Container version, if available ("generation" for Cloud Storage).  
  
## RecordTransformations

A type of transformation that is applied over structured data such as a table.

Fields  
---  
`field_transformations[]` |  `[FieldTransformation](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.FieldTransformation)` Transform the record by applying various field transformations.  
`record_suppressions[]` |  `[RecordSuppression](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.RecordSuppression)` Configuration defining which records get suppressed entirely. Records that match any suppression rule are omitted from the output.  
  
## RedactConfig

This type has no fields.

Redact a given value. For example, if used with an `InfoTypeTransformation` transforming PHONE_NUMBER, and input 'My phone number is 206-555-0123', the output would be 'My phone number is '.

## RedactImageRequest

Request to search for potentially sensitive info in an image and redact it by covering it with a colored rectangle.

Fields  
---  
`parent` |  `string` Parent resource name.The format of this value varies depending on whether you have [specified a processing location](https://docs.cloud.google.com/sensitive-data-protection/docs/specifying-location):

  * Projects scope, location specified: `projects/{project_id}/locations/{location_id}`
  * Projects scope, no location specified (defaults to global): `projects/{project_id}`

The following example `parent` string specifies a parent project with the identifier `example-project`, and specifies the `europe-west3` location for processing data:
    
    
    parent=projects/example-project/locations/europe-west3
    

Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `serviceusage.services.use`

  
`location_id` |  `string` Deprecated. This field has no effect.  
`inspect_config` |  `[InspectConfig](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.InspectConfig)` Configuration for the inspector.  
`image_redaction_configs[]` |  `[ImageRedactionConfig](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.RedactImageRequest.ImageRedactionConfig)` The configuration for specifying what content to redact from images.  
`include_findings` |  `bool` Whether the response should include findings along with the redacted image.  
`byte_item` |  `[ByteContentItem](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ByteContentItem)` The content must be PNG, JPEG, SVG or BMP.  
`inspect_template` |  `string` The full resource name of the inspection template to use. Settings in the main `inspect_config` field override the corresponding settings in this inspection template.The merge behavior is as follows:

  * Singular field: The main field's value replaces the value of the corresponding field in the template.
  * Repeated fields: The field values are appended to the list defined in the template.
  * Sub-messages and groups: The fields are recursively merged.

  
`deidentify_template` |  `string` The full resource name of the de-identification template to use. Settings in the main `image_redaction_configs` field override the corresponding settings in this de-identification template. The request fails if the type of the template's deidentify_config is not image_transformations.  
  
## ImageRedactionConfig

Configuration for determining how redaction of images should occur.

Fields  
---  
`redaction_color` |  `[Color](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.Color)` The color to use when redacting content from an image. If not specified, the default is black.  
Union field `target`. Type of information to redact from images. `target` can be only one of the following:  
`info_type` |  `[InfoType](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.InfoType)` Only one per info_type should be provided per request. If not specified, and redact_all_text is false, the DLP API will redact all text that it matches against all info_types that are found, but not specified in another ImageRedactionConfig.  
`redact_all_text` |  `bool` If true, all text found in the image, regardless whether it matches an info_type, is redacted. Only one should be provided.  
  
## RedactImageResponse

Results of redacting an image.

Fields  
---  
`redacted_image` |  `bytes` The redacted image. The type will be the same as the original image.  
`extracted_text` |  `string` If an image was being inspected and the InspectConfig's include_quote was set to true, then this field will include all text, if any, that was found in the image.  
`inspect_result` |  `[InspectResult](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.InspectResult)` The findings. Populated when include_findings in the request is true.  
  
## ReidentifyContentRequest

Request to re-identify an item.

Fields  
---  
`parent` |  `string` Required. Parent resource name.The format of this value varies depending on whether you have [specified a processing location](https://docs.cloud.google.com/sensitive-data-protection/docs/specifying-location):

  * Projects scope, location specified: `projects/{project_id}/locations/{location_id}`
  * Projects scope, no location specified (defaults to global): `projects/{project_id}`

The following example `parent` string specifies a parent project with the identifier `example-project`, and specifies the `europe-west3` location for processing data:
    
    
    parent=projects/example-project/locations/europe-west3
    

Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `serviceusage.services.use`

  
`reidentify_config` |  `[DeidentifyConfig](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DeidentifyConfig)` Configuration for the re-identification of the content item. This field shares the same proto message type that is used for de-identification, however its usage here is for the reversal of the previous de-identification. Re-identification is performed by examining the transformations used to de-identify the items and executing the reverse. This requires that only reversible transformations be provided here. The reversible transformations are:

  * `CryptoDeterministicConfig`
  * `CryptoReplaceFfxFpeConfig`

  
`inspect_config` |  `[InspectConfig](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.InspectConfig)` Configuration for the inspector.  
`item` |  `[ContentItem](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ContentItem)` The item to re-identify. Will be treated as text.  
`inspect_template_name` |  `string` Template to use. Any configuration directly specified in `inspect_config` will override those set in the template. Singular fields that are set in this request will replace their corresponding fields in the template. Repeated fields are appended. Singular sub-messages and groups are recursively merged.  
`reidentify_template_name` |  `string` Template to use. References an instance of `DeidentifyTemplate`. Any configuration directly specified in `reidentify_config` or `inspect_config` will override those set in the template. The `DeidentifyTemplate` used must include only reversible transformations. Singular fields that are set in this request will replace their corresponding fields in the template. Repeated fields are appended. Singular sub-messages and groups are recursively merged.  
`location_id` |  `string` Deprecated. This field has no effect.  
  
## ReidentifyContentResponse

Results of re-identifying an item.

Fields  
---  
`item` |  `[ContentItem](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ContentItem)` The re-identified item.  
`overview` |  `[TransformationOverview](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.TransformationOverview)` An overview of the changes that were made to the `item`.  
  
## RelatedResource

A related resource. Examples:

  * The source BigQuery table for a Vertex AI dataset.
  * The source Cloud Storage bucket for a Vertex AI dataset.

Fields  
---  
`full_resource` |  `string` The full resource name of the related resource.  
  
## RelationalOperator

Operators available for comparing the value of fields.

Enums  
---  
`RELATIONAL_OPERATOR_UNSPECIFIED` | Unused  
`EQUAL_TO` | Equal. Attempts to match even with incompatible types.  
`NOT_EQUAL_TO` | Not equal to. Attempts to match even with incompatible types.  
`GREATER_THAN` | Greater than.  
`LESS_THAN` | Less than.  
`GREATER_THAN_OR_EQUALS` | Greater than or equals.  
`LESS_THAN_OR_EQUALS` | Less than or equals.  
`EXISTS` | Exists  
  
## ReplaceDictionaryConfig

Replace each input value with a value randomly selected from the dictionary.

Fields  
---  
Union field `type`. Type of dictionary. `type` can be only one of the following:  
`word_list` |  `[WordList](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.CustomInfoType.Dictionary.WordList)` A list of words to select from for random replacement. The [limits](https://docs.cloud.google.com/sensitive-data-protection/limits) page contains details about the size limits of dictionaries.  
  
## ReplaceValueConfig

Replace each input value with a given `Value`.

Fields  
---  
`new_value` |  `[Value](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.Value)` Value to replace it with.  
  
## ReplaceWithInfoTypeConfig

This type has no fields.

Replace each matching finding with the name of the info_type.

## ResourceVisibility

How broadly the data in the resource has been shared. New items may be added over time. A higher number means more restricted.

Enums  
---  
`RESOURCE_VISIBILITY_UNSPECIFIED` | Unused.  
`RESOURCE_VISIBILITY_PUBLIC` | Visible to any user.  
`RESOURCE_VISIBILITY_INCONCLUSIVE` | May contain public items. For example, if a Cloud Storage bucket has uniform bucket level access disabled, some objects inside it may be public, but none are known yet.  
`RESOURCE_VISIBILITY_RESTRICTED` | Visible only to specific users.  
  
## RiskAnalysisJobConfig

Configuration for a risk analysis job. See <https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-risk-analysis> to learn more.

Fields  
---  
`privacy_metric` |  `[PrivacyMetric](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.PrivacyMetric)` Privacy metric to compute.  
`source_table` |  `[BigQueryTable](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.BigQueryTable)` Input dataset to compute metrics over.  
`actions[]` |  `[Action](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.Action)` Actions to execute at the completion of the job. Are executed in the order provided.  
  
## SaveToGcsFindingsOutput

Collection of findings saved to a Cloud Storage bucket. This is used as the proto schema for textproto files created when specifying a cloud storage path to save Inspect findings.

Fields  
---  
`findings[]` |  `[Finding](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.Finding)` List of findings.  
  
## Schedule

Schedule for inspect job triggers.

Fields  
---  
Union field `option`. Type of schedule. `option` can be only one of the following:  
`recurrence_period_duration` |  `[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` With this option a job is started on a regular periodic basis. For example: every day (86400 seconds).A scheduled start time will be skipped if the previous execution has not ended when its scheduled time occurs.This value must be set to a time duration greater than or equal to 1 day and can be no longer than 60 days.  
  
## SearchConnectionsRequest

Request message for SearchConnections.

Fields  
---  
`parent` |  `string` Required. Resource name of the organization or project with a wildcard location, for example, `organizations/433245324/locations/-` or `projects/project-id/locations/-`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `dlp.connections.search`

  
`page_size` |  `int32` Optional. Number of results per page, max 1000.  
`page_token` |  `string` Optional. Page token from a previous page to return the next set of results. If set, all other request fields must match the original request.  
`filter` |  `string` Optional. Supported field/value: - `state` \- MISSING|AVAILABLE|ERRORThe syntax is based on <https://google.aip.dev/160>.  
  
## SearchConnectionsResponse

Response message for SearchConnections.

Fields  
---  
`connections[]` |  `[Connection](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.Connection)` List of connections that match the search query. Note that only a subset of the fields will be populated, and only "name" is guaranteed to be set. For full details of a Connection, call GetConnection with the name.  
`next_page_token` |  `string` Token to retrieve the next page of results. An empty value means there are no more results.  
  
## SecretManagerCredential

A credential consisting of a username and password, where the password is stored in a Secret Manager resource. Note: Secret Manager [charges apply](https://cloud.google.com/secret-manager/pricing).

Fields  
---  
`username` |  `string` Required. The username.  
`password_secret_version_name` |  `string` Required. The name of the Secret Manager resource that stores the password, in the form `projects/project-id/secrets/secret-name/versions/version`.  
  
## SecretsDiscoveryTarget

This type has no fields.

Discovery target for credentials and secrets in cloud resource metadata.

This target does not include any filtering or frequency controls. Cloud DLP will scan cloud resource metadata for secrets daily.

No inspect template should be included in the discovery config for a security benchmarks scan. Instead, the built-in list of secrets and credentials infoTypes will be used (see <https://docs.cloud.google.com/sensitive-data-protection/docs/infotypes-reference#credentials_and_secrets)>.

Credentials and secrets discovered will be reported as vulnerabilities to Security Command Center.

## SensitivityScore

Score is calculated from of all elements in the data profile. A higher level means the data is more sensitive.

Fields  
---  
`score` |  `[SensitivityScoreLevel](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.SensitivityScore.SensitivityScoreLevel)` The sensitivity score applied to the resource.  
  
## SensitivityScoreLevel

Various sensitivity score levels for resources.

Enums  
---  
`SENSITIVITY_SCORE_UNSPECIFIED` | Unused.  
`SENSITIVITY_LOW` | No sensitive information detected. The resource isn't publicly accessible.  
`SENSITIVITY_UNKNOWN` | Unable to determine sensitivity.  
`SENSITIVITY_MODERATE` | Medium risk. Contains personally identifiable information (PII), potentially sensitive data, or fields with free-text data that are at a higher risk of having intermittent sensitive data. Consider limiting access.  
`SENSITIVITY_HIGH` | High risk. Sensitive personally identifiable information (SPII) can be present. Exfiltration of data can lead to user data loss. Re-identification of users might be possible. Consider limiting usage and or removing SPII.  
  
## StatisticalTable

An auxiliary table containing statistical information on the relative frequency of different quasi-identifiers values. It has one or several quasi-identifiers columns, and one column that indicates the relative frequency of each quasi-identifier tuple. If a tuple is present in the data but not in the auxiliary table, the corresponding relative frequency is assumed to be zero (and thus, the tuple is highly reidentifiable).

Fields  
---  
`table` |  `[BigQueryTable](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.BigQueryTable)` Required. Auxiliary table location.  
`quasi_ids[]` |  `[QuasiIdentifierField](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.StatisticalTable.QuasiIdentifierField)` Required. Quasi-identifier columns.  
`relative_frequency` |  `[FieldId](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.FieldId)` Required. The relative frequency column must contain a floating-point number between 0 and 1 (inclusive). Null values are assumed to be zero.  
  
## QuasiIdentifierField

A quasi-identifier column has a custom_tag, used to know which column in the data corresponds to which column in the statistical model.

Fields  
---  
`field` |  `[FieldId](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.FieldId)` Identifies the column.  
`custom_tag` |  `string` A column can be tagged with a custom tag. In this case, the user must indicate an auxiliary table that contains statistical information on the possible values of this column.  
  
## StorageConfig

Shared message indicating Cloud storage type.

Fields  
---  
`timespan_config` |  `[TimespanConfig](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.StorageConfig.TimespanConfig)` Configuration of the timespan of the items to include in scanning.  
Union field `type`. Type of storage system to inspect. `type` can be only one of the following:  
`datastore_options` |  `[DatastoreOptions](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DatastoreOptions)` Google Cloud Datastore options.  
`cloud_storage_options` |  `[CloudStorageOptions](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.CloudStorageOptions)` Cloud Storage options.  
`big_query_options` |  `[BigQueryOptions](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.BigQueryOptions)` BigQuery options.  
`hybrid_options` |  `[HybridOptions](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.HybridOptions)` Hybrid inspection options.  
  
## TimespanConfig

Configuration of the timespan of the items to include in scanning. Currently only supported when inspecting Cloud Storage and BigQuery.

Fields  
---  
`start_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Exclude files, tables, or rows older than this value. If not set, no lower time limit is applied.  
`end_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Exclude files, tables, or rows newer than this value. If not set, no upper time limit is applied.  
`timestamp_field` |  `[FieldId](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.FieldId)` Specification of the field containing the timestamp of scanned items. Used for data sources like Datastore and BigQuery.**For BigQuery** If this value is not specified and the table was modified between the given start and end times, the entire table will be scanned. If this value is specified, then rows are filtered based on the given start and end times. Rows with a `NULL` value in the provided BigQuery column are skipped. Valid data types of the provided BigQuery column are: `INTEGER`, `DATE`, `TIMESTAMP`, and `DATETIME`.If your BigQuery table is [partitioned at ingestion time](https://docs.cloud.google.com/bigquery/docs/partitioned-tables#ingestion_time), you can use any of the following pseudo-columns as your timestamp field. When used with Cloud DLP, these pseudo-column names are case sensitive.

  * `_PARTITIONTIME`
  * `_PARTITIONDATE`
  * `_PARTITION_LOAD_TIME`

**For Datastore** If this value is specified, then entities are filtered based on the given start and end times. If an entity does not contain the provided timestamp property or contains empty or invalid values, then it is included. Valid data types of the provided timestamp property are: `TIMESTAMP`.See the [known issue](https://docs.cloud.google.com/sensitive-data-protection/docs/known-issues#bq-timespan) related to this operation.  
`enable_auto_population_of_timespan_config` |  `bool` When the job is started by a JobTrigger we will automatically figure out a valid start_time to avoid scanning files that have not been modified since the last time the JobTrigger executed. This will be based on the time of the execution of the last run of the JobTrigger or the timespan end_time used in the last run of the JobTrigger.**For BigQuery** Inspect jobs triggered by automatic population will scan data that is at least three hours old when the job starts. This is because streaming buffer rows are not read during inspection and reading up to the current timestamp will result in skipped rows.See the [known issue](https://docs.cloud.google.com/sensitive-data-protection/docs/known-issues#recently-streamed-data) related to this operation.  
  
## StorageMetadataLabel

Storage metadata label to indicate which metadata entry contains findings.

Fields  
---  
`key` |  `string` Label name.  
  
## StoredInfoType

StoredInfoType resource message that contains information about the current version and any pending updates.

Fields  
---  
`name` |  `string` Output only. Resource name.  
`current_version` |  `[StoredInfoTypeVersion](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.StoredInfoTypeVersion)` Current version of the stored info type.  
`pending_versions[]` |  `[StoredInfoTypeVersion](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.StoredInfoTypeVersion)` Pending versions of the stored info type. Empty if no versions are pending.  
  
## StoredInfoTypeConfig

Configuration for stored infoTypes. All fields and subfield are provided by the user. For more information, see <https://docs.cloud.google.com/sensitive-data-protection/docs/creating-custom-infotypes>.

Fields  
---  
`display_name` |  `string` Display name of the StoredInfoType (max 256 characters).  
`description` |  `string` Description of the StoredInfoType (max 256 characters).  
Union field `type`. Stored infotype types. `type` can be only one of the following:  
`large_custom_dictionary` |  `[LargeCustomDictionaryConfig](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.LargeCustomDictionaryConfig)` StoredInfoType where findings are defined by a dictionary of phrases.  
`dictionary` |  `[Dictionary](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.CustomInfoType.Dictionary)` Store dictionary-based CustomInfoType.  
`regex` |  `[Regex](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.CustomInfoType.Regex)` Store regular expression-based StoredInfoType.  
  
## StoredInfoTypeState

State of a StoredInfoType version.

Enums  
---  
`STORED_INFO_TYPE_STATE_UNSPECIFIED` | Unused  
`PENDING` | StoredInfoType version is being created.  
`READY` | StoredInfoType version is ready for use.  
`FAILED` | StoredInfoType creation failed. All relevant error messages are returned in the `StoredInfoTypeVersion` message.  
`INVALID` | StoredInfoType is no longer valid because artifacts stored in user-controlled storage were modified. To fix an invalid StoredInfoType, use the `UpdateStoredInfoType` method to create a new version.  
  
## StoredInfoTypeStats

Statistics for a StoredInfoType.

Fields  
---  
Union field `type`. Stat types `type` can be only one of the following:  
`large_custom_dictionary` |  `[LargeCustomDictionaryStats](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.LargeCustomDictionaryStats)` StoredInfoType where findings are defined by a dictionary of phrases.  
  
## StoredInfoTypeVersion

Version of a StoredInfoType, including the configuration used to build it, create timestamp, and current state.

Fields  
---  
`config` |  `[StoredInfoTypeConfig](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.StoredInfoTypeConfig)` StoredInfoType configuration.  
`create_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. Create timestamp of the version. Read-only, determined by the system when the version is created.  
`state` |  `[StoredInfoTypeState](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.StoredInfoTypeState)` Output only. Stored info type version state. Read-only, updated by the system during dictionary creation.  
`errors[]` |  `[Error](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.Error)` Output only. Errors that occurred when creating this storedInfoType version, or anomalies detected in the storedInfoType data that render it unusable. Only the five most recent errors will be displayed, with the most recent error appearing first.For example, some of the data for stored custom dictionaries is put in the user's Cloud Storage bucket, and if this data is modified or deleted by the user or another system, the dictionary becomes invalid.If any errors occur, fix the problem indicated by the error message and use the UpdateStoredInfoType API method to create another version of the storedInfoType to continue using it, reusing the same `config` if it was not the source of the error.  
`stats` |  `[StoredInfoTypeStats](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.StoredInfoTypeStats)` Output only. Statistics about this storedInfoType version.  
  
## StoredType

A reference to a StoredInfoType to use with scanning.

Fields  
---  
`name` |  `string` Resource name of the requested `StoredInfoType`, for example `organizations/433245324/storedInfoTypes/432452342` or `projects/project-id/storedInfoTypes/432452342`.  
`create_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Timestamp indicating when the version of the `StoredInfoType` used for inspection was created. Output-only field, populated by the system.  
  
## StringValueBatch

Represents a batch of string values to inspect or redact.

Fields  
---  
`values[]` |  `string` Optional. Represents string data to inspect or redact.  
  
## Table

Structured content to inspect. Up to 50,000 `Value`s per request allowed. See <https://docs.cloud.google.com/sensitive-data-protection/docs/inspecting-structured-text#inspecting_a_table> to learn more.

Fields  
---  
`headers[]` |  `[FieldId](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.FieldId)` Headers of the table.  
`rows[]` |  `[Row](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.Table.Row)` Rows of the table.  
  
## Row

Values of the row.

Fields  
---  
`values[]` |  `[Value](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.Value)` Individual cells.  
  
## TableDataProfile

The profile for a scanned table.

Fields  
---  
`name` |  `string` The name of the profile.  
`data_source_type` |  `[DataSourceType](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DataSourceType)` The resource type that was profiled.  
`project_data_profile` |  `string` The resource name of the project data profile for this table.  
`dataset_project_id` |  `string` The Google Cloud project ID that owns the resource.  
`dataset_location` |  `string` If supported, the location where the dataset's data is stored. See <https://docs.cloud.google.com/bigquery/docs/locations> for supported locations.  
`dataset_id` |  `string` If the resource is BigQuery, the dataset ID.  
`table_id` |  `string` The table ID.  
`full_resource` |  `string` The Cloud Asset Inventory resource that was profiled in order to generate this TableDataProfile. <https://cloud.google.com/apis/design/resource_names#full_resource_name>  
`profile_status` |  `[ProfileStatus](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ProfileStatus)` Success or error status from the most recent profile generation attempt. May be empty if the profile is still being generated.  
`state` |  `[State](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.TableDataProfile.State)` State of a profile. This will always be set to DONE when the table data profile is written to another service like BigQuery or Pub/Sub.  
`sensitivity_score` |  `[SensitivityScore](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.SensitivityScore)` The sensitivity score of this table.  
`data_risk_level` |  `[DataRiskLevel](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DataRiskLevel)` The data risk level of this table.  
`predicted_info_types[]` |  `[InfoTypeSummary](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.InfoTypeSummary)` The infoTypes predicted from this table's data.  
`other_info_types[]` |  `[OtherInfoTypeSummary](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.OtherInfoTypeSummary)` Other infoTypes found in this table's data.  
`config_snapshot` |  `[DataProfileConfigSnapshot](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DataProfileConfigSnapshot)` The snapshot of the configurations used to generate the profile.  
`last_modified_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` The time when this table was last modified  
`expiration_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Optional. The time when this table expires.  
`scanned_column_count` |  `int64` The number of columns profiled in the table.  
`failed_column_count` |  `int64` The number of columns skipped in the table because of an error.  
`table_size_bytes` |  `int64` The size of the table when the profile was generated.  
`row_count` |  `int64` Number of rows in the table when the profile was generated. This will not be populated for BigLake tables.  
`encryption_status` |  `[EncryptionStatus](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.EncryptionStatus)` How the table is encrypted.  
`resource_visibility` |  `[ResourceVisibility](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ResourceVisibility)` How broadly a resource has been shared.  
`profile_last_generated` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` The last time the profile was generated.  
`resource_labels` |  `map<string, string>` The labels applied to the resource at the time the profile was generated.  
`create_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` The time at which the table was created.  
`sample_findings_table` |  `[BigQueryTable](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.BigQueryTable)` The BigQuery table to which the sample findings are written.  
`tags[]` |  `[Tag](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.Tag)` The tags attached to the table, including any tags attached during profiling. Because tags are attached to Cloud SQL instances rather than Cloud SQL tables, this field is empty for Cloud SQL table profiles.  
`related_resources[]` |  `[RelatedResource](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.RelatedResource)` Resources related to this profile.  
`domains[]` |  `[Domain](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.Domain)` Domains associated with the profile.  
  
## State

Possible states of a profile. New items may be added.

Enums  
---  
`STATE_UNSPECIFIED` | Unused.  
`RUNNING` | The profile is currently running. Once a profile has finished it will transition to DONE.  
`DONE` | The profile is no longer generating. If profile_status.status.code is 0, the profile succeeded, otherwise, it failed.  
  
## TableLocation

Location of a finding within a table.

Fields  
---  
`row_index` |  `int64` The zero-based index of the row where the finding is located. Only populated for resources that have a natural ordering, not BigQuery. In BigQuery, to identify the row a finding came from, populate BigQueryOptions.identifying_fields with your primary key column names and when you store the findings the value of those columns will be stored inside of Finding.  
  
## TableOptions

Instructions regarding the table content being inspected.

Fields  
---  
`identifying_fields[]` |  `[FieldId](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.FieldId)` The columns that are the primary keys for table objects included in ContentItem. A copy of this cell's value will stored alongside alongside each finding so that the finding can be traced to the specific row it came from. No more than 3 may be provided.  
  
## TableReference

Message defining the location of a BigQuery table with the projectId inferred from the parent project.

Fields  
---  
`dataset_id` |  `string` Dataset ID of the table.  
`table_id` |  `string` Name of the table.  
`project_id` |  `string` The Google Cloud project ID of the project containing the table. If omitted, the project ID is inferred from the parent project. This field is required if the parent resource is an organization.  
  
## Tag

A tag associated with a resource.

Fields  
---  
`namespaced_tag_value` |  `string` The namespaced name for the tag value to attach to Google Cloud resources. Must be in the format `{parent_id}/{tag_key_short_name}/{short_name}`, for example, "123456/environment/prod" for an organization parent, or "my-project/environment/prod" for a project parent. This is only set for Google Cloud resources.  
`key` |  `string` The key of a tag key-value pair. For Google Cloud resources, this is the resource name of the key, for example, "tagKeys/123456".  
`value` |  `string` The value of a tag key-value pair. For Google Cloud resources, this is the resource name of the value, for example, "tagValues/123456".  
  
## TagFilter

A single tag to filter against.

Fields  
---  
Union field `format`. Tag filter formats. Tags refer to Resource Manager tags bound to the resource or its ancestors. `format` can be only one of the following:  
`namespaced_tag_value` |  `string` The namespaced name for the tag value. Must be in the format `{parent_id}/{tag_key_short_name}/{short_name}`, for example, "123456/environment/prod" for an organization parent, or "my-project/environment/prod" for a project parent.  
`namespaced_tag_key` |  `string` The namespaced name for the tag key. Must be in the format `{parent_id}/{tag_key_short_name}`, for example, "123456/sensitive" for an organization parent, or "my-project/sensitive" for a project parent.  
  
## TagFilters

Tags to match against for filtering.

Fields  
---  
`tag_filters[]` |  `[TagFilter](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.TagFilter)` Required. A resource must match ALL of the specified tag filters to be included in the collection.  
  
## TimePartConfig

For use with `Date`, `Timestamp`, and `TimeOfDay`, extract or preserve a portion of the value.

Fields  
---  
`part_to_extract` |  `[TimePart](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.TimePartConfig.TimePart)` The part of the time to keep.  
  
## TimePart

Components that make up time.

Enums  
---  
`TIME_PART_UNSPECIFIED` | Unused  
`YEAR` | [0-9999]  
`MONTH` | [1-12]  
`DAY_OF_MONTH` | [1-31]  
`DAY_OF_WEEK` | [1-7]  
`WEEK_OF_YEAR` | [1-53]  
`HOUR_OF_DAY` | [0-23]  
  
## TransformationConfig

User specified templates and configs for how to deidentify structured, unstructures, and image files. User must provide either a unstructured deidentify template or at least one redact image config.

Fields  
---  
`deidentify_template` |  `string` De-identify template. If this template is specified, it will serve as the default de-identify template. This template cannot contain `record_transformations` since it can be used for unstructured content such as free-form text files. If this template is not set, a default `ReplaceWithInfoTypeConfig` will be used to de-identify unstructured content.  
`structured_deidentify_template` |  `string` Structured de-identify template. If this template is specified, it will serve as the de-identify template for structured content such as delimited files and tables. If this template is not set but the `deidentify_template` is set, then `deidentify_template` will also apply to the structured content. If neither template is set, a default `ReplaceWithInfoTypeConfig` will be used to de-identify structured content.  
`image_redact_template` |  `string` Image redact template. If this template is specified, it will serve as the de-identify template for images. If this template is not set, all findings in the image will be redacted with a black box.  
  
## TransformationContainerType

Describes functionality of a given container in its original format.

Enums  
---  
`TRANSFORM_UNKNOWN_CONTAINER` | Unused.  
`TRANSFORM_BODY` | Body of a file.  
`TRANSFORM_METADATA` | Metadata for a file.  
`TRANSFORM_TABLE` | A table.  
  
## TransformationDescription

A flattened description of a `PrimitiveTransformation` or `RecordSuppression`.

Fields  
---  
`type` |  `[TransformationType](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.TransformationType)` The transformation type.  
`description` |  `string` A description of the transformation. This is empty for a RECORD_SUPPRESSION, or is the output of calling toString() on the `PrimitiveTransformation` protocol buffer message for any other type of transformation.  
`condition` |  `string` A human-readable string representation of the `RecordCondition` corresponding to this transformation. Set if a `RecordCondition` was used to determine whether or not to apply this transformation.Examples: * (age_field > 85) * (age_field <= 18) * (zip_field exists) * (zip_field == 01234) && (city_field != "Springville") * (zip_field == 01234) && (age_field <= 18) && (city_field exists)  
`info_type` |  `[InfoType](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.InfoType)` Set if the transformation was limited to a specific `InfoType`.  
  
## TransformationDetails

Details about a single transformation. This object contains a description of the transformation, information about whether the transformation was successfully applied, and the precise location where the transformation occurred. These details are stored in a user-specified BigQuery table.

Fields  
---  
`resource_name` |  `string` The name of the job that completed the transformation.  
`container_name` |  `string` The top level name of the container where the transformation is located (this will be the source file name or table name).  
`transformation[]` |  `[TransformationDescription](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.TransformationDescription)` Description of transformation. This would only contain more than one element if there were multiple matching transformations and which one to apply was ambiguous. Not set for states that contain no transformation, currently only state that contains no transformation is TransformationResultStateType.METADATA_UNRETRIEVABLE.  
`status_details` |  `[TransformationResultStatus](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.TransformationResultStatus)` Status of the transformation, if transformation was not successful, this will specify what caused it to fail, otherwise it will show that the transformation was successful.  
`transformed_bytes` |  `int64` The number of bytes that were transformed. If transformation was unsuccessful or did not take place because there was no content to transform, this will be zero.  
`transformation_location` |  `[TransformationLocation](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.TransformationLocation)` The precise location of the transformed content in the original container.  
  
## TransformationDetailsStorageConfig

Config for storing transformation details.

Fields  
---  
Union field `type`. Location to store the transformation summary. `type` can be only one of the following:  
`table` |  `[BigQueryTable](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.BigQueryTable)` The BigQuery table in which to store the output. This may be an existing table or in a new table in an existing dataset. If table_id is not set a new one will be generated for you with the following format: dlp_googleapis_transformation_details_yyyy_mm_dd_[dlp_job_id]. Pacific time zone will be used for generating the date details.  
  
## TransformationErrorHandling

How to handle transformation errors during de-identification. A transformation error occurs when the requested transformation is incompatible with the data. For example, trying to de-identify an IP address using a `DateShift` transformation would result in a transformation error, since date info cannot be extracted from an IP address. Information about any incompatible transformations, and how they were handled, is returned in the response as part of the `TransformationOverviews`.

Fields  
---  
Union field `mode`. How transformation errors should be handled. `mode` can be only one of the following:  
`throw_error` |  `[ThrowError](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.TransformationErrorHandling.ThrowError)` Throw an error  
`leave_untransformed` |  `[LeaveUntransformed](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.TransformationErrorHandling.LeaveUntransformed)` Ignore errors  
  
## LeaveUntransformed

This type has no fields.

Skips the data without modifying it if the requested transformation would cause an error. For example, if a `DateShift` transformation were applied an an IP address, this mode would leave the IP address unchanged in the response.

## ThrowError

This type has no fields.

Throw an error and fail the request when a transformation error occurs.

## TransformationLocation

Specifies the location of a transformation.

Fields  
---  
`container_type` |  `[TransformationContainerType](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.TransformationContainerType)` Information about the functionality of the container where this finding occurred, if available.  
Union field `location_type`. Location type. `location_type` can be only one of the following:  
`finding_id` |  `string` For infotype transformations, link to the corresponding findings ID so that location information does not need to be duplicated. Each findings ID correlates to an entry in the findings output table, this table only gets created when users specify to save findings (add the save findings action to the request).  
`record_transformation` |  `[RecordTransformation](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.RecordTransformation)` For record transformations, provide a field and container information.  
  
## TransformationOverview

Overview of the modifications that occurred.

Fields  
---  
`transformed_bytes` |  `int64` Total size in bytes that were transformed in some way.  
`transformation_summaries[]` |  `[TransformationSummary](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.TransformationSummary)` Transformations applied to the dataset.  
  
## TransformationResultStatus

The outcome of a transformation.

Fields  
---  
`result_status_type` |  `[TransformationResultStatusType](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.TransformationResultStatusType)` Transformation result status type, this will be either SUCCESS, or it will be the reason for why the transformation was not completely successful.  
`details` |  `[Status](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.rpc#google.rpc.Status)` Detailed error codes and messages  
  
## TransformationResultStatusType

Enum of possible outcomes of transformations. SUCCESS if transformation and storing of transformation was successful, otherwise, reason for not transforming.

Enums  
---  
`STATE_TYPE_UNSPECIFIED` | Unused.  
`INVALID_TRANSFORM` | This is set when a finding cannot be transformed (i.e. outside user set bucket range).  
`BIGQUERY_MAX_ROW_SIZE_EXCEEDED` | This is set when a transformation is successful but cannot be stored in BigQuery because the transformed row exceeds BigQuery's max row size.  
`METADATA_UNRETRIEVABLE` | This is set when there is a finding in the custom metadata of a file, but at the write time of the transformed file, this key / value pair is unretrievable.  
`SUCCESS` | This is set when the transformation and its storage are successful.  
  
## TransformationSummary

Summary of a single transformation. Only one of 'transformation', 'field_transformation', or 'record_suppress' will be set.

Fields  
---  
`info_type` |  `[InfoType](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.InfoType)` Set if the transformation was limited to a specific InfoType.  
`field` |  `[FieldId](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.FieldId)` Set if the transformation was limited to a specific FieldId.  
`transformation` |  `[PrimitiveTransformation](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.PrimitiveTransformation)` The specific transformation these stats apply to.  
`field_transformations[]` |  `[FieldTransformation](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.FieldTransformation)` The field transformation that was applied. If multiple field transformations are requested for a single field, this list will contain all of them; otherwise, only one is supplied.  
`record_suppress` |  `[RecordSuppression](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.RecordSuppression)` The specific suppression option these stats apply to.  
`results[]` |  `[SummaryResult](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.TransformationSummary.SummaryResult)` Collection of all transformations that took place or had an error.  
`transformed_bytes` |  `int64` Total size in bytes that were transformed in some way.  
  
## SummaryResult

A collection that informs the user the number of times a particular `TransformationResultCode` and error details occurred.

Fields  
---  
`count` |  `int64` Number of transformations counted by this result.  
`code` |  `[TransformationResultCode](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.TransformationSummary.TransformationResultCode)` Outcome of the transformation.  
`details` |  `string` A place for warnings or errors to show up if a transformation didn't work as expected.  
  
## TransformationResultCode

Possible outcomes of transformations.

Enums  
---  
`TRANSFORMATION_RESULT_CODE_UNSPECIFIED` | Unused  
`SUCCESS` | Transformation completed without an error.  
`ERROR` | Transformation had an error.  
  
## TransformationType

An enum of rules that can be used to transform a value. Can be a record suppression, or one of the transformation rules specified under `PrimitiveTransformation`.

Enums  
---  
`TRANSFORMATION_TYPE_UNSPECIFIED` | Unused  
`RECORD_SUPPRESSION` | Record suppression  
`REPLACE_VALUE` | Replace value  
`REPLACE_DICTIONARY` | Replace value using a dictionary.  
`REDACT` | Redact  
`CHARACTER_MASK` | Character mask  
`CRYPTO_REPLACE_FFX_FPE` | FFX-FPE  
`FIXED_SIZE_BUCKETING` | Fixed size bucketing  
`BUCKETING` | Bucketing  
`REPLACE_WITH_INFO_TYPE` | Replace with info type  
`TIME_PART` | Time part  
`CRYPTO_HASH` | Crypto hash  
`DATE_SHIFT` | Date shift  
`CRYPTO_DETERMINISTIC_CONFIG` | Deterministic crypto  
`REDACT_IMAGE` | Redact image  
  
## TransientCryptoKey

Use this to have a random data crypto key generated. It will be discarded after the request finishes.

Fields  
---  
`name` |  `string` Required. Name of the key. This is an arbitrary string used to differentiate different keys. A unique key is generated per name: two separate `TransientCryptoKey` protos share the same generated key if their names are the same. When the data crypto key is generated, this name is not used in any way (repeating the api call will result in a different key being generated).  
  
## UniquenessScoreLevel

Bucketized uniqueness score levels. A higher uniqueness score is a strong signal that the column may contain a unique identifier like user id. A low value indicates that the column contains few unique values like booleans or other classifiers.

Enums  
---  
`UNIQUENESS_SCORE_LEVEL_UNSPECIFIED` | Some columns do not have estimated uniqueness. Possible reasons include having too few values.  
`UNIQUENESS_SCORE_LOW` | Low uniqueness, possibly a boolean, enum or similiarly typed column.  
`UNIQUENESS_SCORE_MEDIUM` | Medium uniqueness.  
`UNIQUENESS_SCORE_HIGH` | High uniqueness, possibly a column of free text or unique identifiers.  
  
## UnwrappedCryptoKey

Using raw keys is prone to security risks due to accidentally leaking the key. Choose another type of key if possible.

Fields  
---  
`key` |  `bytes` Required. A 128/192/256 bit key.  
  
## UpdateConnectionRequest

Request message for UpdateConnection.

Fields  
---  
`name` |  `string` Required. Resource name in the format: `projects/{project}/locations/{location}/connections/{connection}`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `dlp.connections.update`

  
`connection` |  `[Connection](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.Connection)` Required. The connection with new values for the relevant fields.  
`update_mask` |  `[FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` Optional. Mask to control which fields get updated.  
  
## UpdateContentPolicyRequest

Request message for UpdateContentPolicy.

Fields  
---  
`name` |  `string` Required. Resource name in the format: `projects/{project}/locations/{location}/contentPolicies/{content_policy}`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `dlp.contentPolicies.update`

  
`content_policy` |  `[ContentPolicy](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.ContentPolicy)` Required. The content_policy with new values for the relevant fields.  
`update_mask` |  `[FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` Optional. Mask to control which fields get updated.  
  
## UpdateDeidentifyTemplateRequest

Request message for UpdateDeidentifyTemplate.

Fields  
---  
`name` |  `string` Required. Resource name of organization and deidentify template to be updated, for example `organizations/433245324/deidentifyTemplates/432452342` or projects/project-id/deidentifyTemplates/432452342. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `dlp.deidentifyTemplates.update`

  
`deidentify_template` |  `[DeidentifyTemplate](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DeidentifyTemplate)` New DeidentifyTemplate value.  
`update_mask` |  `[FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` Mask to control which fields get updated.  
  
## UpdateDiscoveryConfigRequest

Request message for UpdateDiscoveryConfig.

Fields  
---  
`name` |  `string` Required. Resource name of the project and the configuration, for example `projects/dlp-test-project/discoveryConfigs/53234423`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `dlp.jobTriggers.update`

  
`discovery_config` |  `[DiscoveryConfig](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DiscoveryConfig)` Required. New DiscoveryConfig value.  
`update_mask` |  `[FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` Mask to control which fields get updated.  
  
## UpdateInspectTemplateRequest

Request message for UpdateInspectTemplate.

Fields  
---  
`name` |  `string` Required. Resource name of organization and inspectTemplate to be updated, for example `organizations/433245324/inspectTemplates/432452342` or projects/project-id/inspectTemplates/432452342. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `dlp.inspectTemplates.update`

  
`inspect_template` |  `[InspectTemplate](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.InspectTemplate)` New InspectTemplate value.  
`update_mask` |  `[FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` Mask to control which fields get updated.  
  
## UpdateJobTriggerRequest

Request message for UpdateJobTrigger.

Fields  
---  
`name` |  `string` Required. Resource name of the project and the triggeredJob, for example `projects/dlp-test-project/jobTriggers/53234423`. Authorization requires one or more of the following [IAM](https://cloud.google.com/iam/docs/) permissions on the specified resource `name`:

  * `dlp.jobTriggers.update`
  * `dlp.jobs.create`

  
`job_trigger` |  `[JobTrigger](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.JobTrigger)` New JobTrigger value.  
`update_mask` |  `[FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` Mask to control which fields get updated.  
  
## UpdateStoredInfoTypeRequest

Request message for UpdateStoredInfoType.

Fields  
---  
`name` |  `string` Required. Resource name of organization and storedInfoType to be updated, for example `organizations/433245324/storedInfoTypes/432452342` or projects/project-id/storedInfoTypes/432452342. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `dlp.storedInfoTypes.update`

  
`config` |  `[StoredInfoTypeConfig](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.StoredInfoTypeConfig)` Updated configuration for the storedInfoType. If not provided, a new version of the storedInfoType will be created with the existing configuration.  
`update_mask` |  `[FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` Mask to control which fields get updated.  
  
## Value

Set of primitive values supported by the system. Note that for the purposes of inspection or transformation, the number of bytes considered to comprise a 'Value' is based on its representation as a UTF-8 encoded string. For example, if 'integer_value' is set to 123456789, the number of bytes would be counted as 9, even though an int64 only holds up to 8 bytes of data.

Fields  
---  
Union field `type`. Value types `type` can be only one of the following:  
`integer_value` |  `int64` integer  
`float_value` |  `double` float  
`string_value` |  `string` string  
`boolean_value` |  `bool` boolean  
`timestamp_value` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` timestamp  
`time_value` |  `[TimeOfDay](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.type#google.type.TimeOfDay)` time of day  
`date_value` |  `[Date](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.type#google.type.Date)` date  
`day_of_week_value` |  `[DayOfWeek](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.type#google.type.DayOfWeek)` day of week  
  
## ValueFrequency

A value of a field, including its frequency.

Fields  
---  
`value` |  `[Value](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.Value)` A value contained in the field in question.  
`count` |  `int64` How many times the value is contained in the field.  
  
## VersionDescription

Details about each available version for an infotype.

Fields  
---  
`version` |  `string` Name of the version  
`description` |  `string` Description of the version.  
  
## VertexDatasetCollection

Match dataset resources using regex filters.

Fields  
---  
Union field `pattern`. The pattern used to filter dataset resources. `pattern` can be only one of the following:  
`vertex_dataset_regexes` |  `[VertexDatasetRegexes](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.VertexDatasetRegexes)` The regex used to filter dataset resources.  
  
## VertexDatasetDiscoveryTarget

Target used to match against for discovery with Vertex AI datasets.

Fields  
---  
`filter` |  `[DiscoveryVertexDatasetFilter](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DiscoveryVertexDatasetFilter)` Required. The datasets the discovery cadence applies to. The first target with a matching filter will be the one to apply to a dataset.  
`conditions` |  `[DiscoveryVertexDatasetConditions](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DiscoveryVertexDatasetConditions)` In addition to matching the filter, these conditions must be true before a profile is generated.  
Union field `cadence`. Type of schedule. `cadence` can be only one of the following:  
`generation_cadence` |  `[DiscoveryVertexDatasetGenerationCadence](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.DiscoveryVertexDatasetGenerationCadence)` How often and when to update profiles. New datasets that match both the filter and conditions are scanned as quickly as possible depending on system capacity.  
`disabled` |  `[Disabled](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.Disabled)` Disable profiling for datasets that match this filter.  
  
## VertexDatasetRegex

A pattern to match against one or more dataset resources.

Fields  
---  
`project_id_regex` |  `string` For organizations, if unset, will match all projects. Has no effect for configurations created within a project.  
  
## VertexDatasetRegexes

A collection of regular expressions to determine what datasets to match against.

Fields  
---  
`patterns[]` |  `[VertexDatasetRegex](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.VertexDatasetRegex)` Required. The group of regular expression patterns to match against one or more datasets. Maximum of 100 entries. The sum of the lengths of all regular expressions can't exceed 10 KiB.  
  
## VertexDatasetResourceReference

Identifies a single Vertex AI resource. Only datasets are supported.

Fields  
---  
`dataset_resource_name` |  `string` Required. The name of the Vertex AI resource. If set within a project-level configuration, the specified resource must be within the project. Examples:

  * `projects/{project}/locations/{location}/datasets/{dataset}`

  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
