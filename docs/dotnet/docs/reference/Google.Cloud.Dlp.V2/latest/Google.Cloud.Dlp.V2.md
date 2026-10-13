---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2
title: Google Cloud Data Loss Prevention v2 API - Namespace Google.Cloud.Dlp.V2 (4.27.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:46:26.665255+00:00
---

# Google Cloud Data Loss Prevention v2 API - Namespace Google.Cloud.Dlp.V2 (4.27.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Data Loss Prevention v2 API - Namespace Google.Cloud.Dlp.V2 (4.27.0) Stay organized with collections  Save and categorize content based on your preferences. 

4.27.0 (latest)  4.26.0  4.25.0  4.24.0  4.23.0  4.22.0  4.21.0  4.20.0  4.19.0  4.18.0  4.17.0  4.16.0  4.15.0  4.14.0  4.13.0  4.12.0  4.11.0  4.10.0  4.9.0  4.8.0  4.7.0  4.6.0  4.5.0  4.4.0  4.3.0  4.2.0  4.1.0  4.0.0  3.5.0  3.4.0  3.3.0  3.2.0  2.16.0  2.15.0 

## Classes 

### [Action](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Action)

A task to execute on the completion of a job. See <https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-actions> to learn more.

### [Action.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Action.Types)

Container for nested types declared in the Action message type.

### [Action.Types.Deidentify](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Action.Types.Deidentify)

Create a de-identified copy of a storage bucket. Only compatible with Cloud Storage buckets.

A TransformationDetail will be created for each transformation.

Compatible with: Inspection of Cloud Storage

### [Action.Types.JobNotificationEmails](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Action.Types.JobNotificationEmails)

Sends an email when the job completes. The email goes to IAM project owners and technical [Essential Contacts](https://docs.cloud.google.com/resource-manager/docs/managing-notification-contacts).

### [Action.Types.PublishFindingsToCloudDataCatalog](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Action.Types.PublishFindingsToCloudDataCatalog)

Publish findings of a DlpJob to Data Catalog. In Data Catalog, tag templates are applied to the resource that Cloud DLP scanned. Data Catalog tag templates are stored in the same project and region where the BigQuery table exists. For Cloud DLP to create and apply the tag template, the Cloud DLP service agent must have the `roles/datacatalog.tagTemplateOwner` permission on the project. The tag template contains fields summarizing the results of the DlpJob. Any field values previously written by another DlpJob are deleted. [InfoType naming patterns][google.privacy.dlp.v2.InfoType] are strictly enforced when using this feature.

Findings are persisted in Data Catalog storage and are governed by service-specific policies for Data Catalog. For more information, see [Service Specific Terms](https://cloud.google.com/terms/service-terms).

Only a single instance of this action can be specified. This action is allowed only if all resources being scanned are BigQuery tables. Compatible with: Inspect

### [Action.Types.PublishFindingsToDataplexCatalog](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Action.Types.PublishFindingsToDataplexCatalog)

Publish findings of a DlpJob to Dataplex Universal Catalog as a `sensitive-data-protection-job-result` aspect. For more information, see [Send inspection results to Dataplex Universal Catalog as aspects](https://docs.cloud.google.com/sensitive-data-protection/docs/add-aspects-inspection-job).

Aspects are stored in Dataplex Universal Catalog storage and are governed by service-specific policies for Dataplex Universal Catalog. For more information, see [Service Specific Terms](https://cloud.google.com/terms/service-terms).

Only a single instance of this action can be specified. This action is allowed only if all resources being scanned are BigQuery tables. Compatible with: Inspect

### [Action.Types.PublishSummaryToCscc](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Action.Types.PublishSummaryToCscc)

Publish the result summary of a DlpJob to [Security Command Center](https://cloud.google.com/security-command-center). This action is available for only projects that belong to an organization. This action publishes the count of finding instances and their infoTypes. The summary of findings are persisted in Security Command Center and are governed by [service-specific policies for Security Command Center](https://cloud.google.com/terms/service-terms). Only a single instance of this action can be specified. Compatible with: Inspect

### [Action.Types.PublishToPubSub](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Action.Types.PublishToPubSub)

Publish a message into a given Pub/Sub topic when DlpJob has completed. The message contains a single field, `DlpJobName`, which is equal to the finished job's [`DlpJob.name`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.dlpJobs#DlpJob). Compatible with: Inspect, Risk

### [Action.Types.PublishToStackdriver](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Action.Types.PublishToStackdriver)

Enable Stackdriver metric dlp.googleapis.com/finding_count. This will publish a metric to stack driver on each infotype requested and how many findings were found for it. CustomDetectors will be bucketed as 'Custom' under the Stackdriver label 'info_type'.

### [Action.Types.SaveFindings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Action.Types.SaveFindings)

If set, the detailed findings will be persisted to the specified OutputStorageConfig. Only a single instance of this action can be specified. Compatible with: Inspect, Risk

### [ActionDetails](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ActionDetails)

The results of an [Action][google.privacy.dlp.v2.Action].

### [ActivateJobTriggerRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ActivateJobTriggerRequest)

Request message for ActivateJobTrigger.

### [AdjustByImageFindings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.AdjustByImageFindings)

AdjustmentRule condition for image findings. This rule is silently ignored if the content being inspected is not an image.

### [AdjustByMatchingInfoTypes](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.AdjustByMatchingInfoTypes)

AdjustmentRule condition for matching infoTypes.

### [AdjustmentRule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.AdjustmentRule)

Rule that specifies conditions when a certain infoType's finding details should be adjusted.

### [AllOtherDatabaseResources](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.AllOtherDatabaseResources)

Match database resources not covered by any other filter.

### [AllOtherResources](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.AllOtherResources)

Match discovery resources not covered by any other filter.

### [AmazonS3Bucket](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.AmazonS3Bucket)

Amazon S3 bucket.

### [AmazonS3BucketConditions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.AmazonS3BucketConditions)

Amazon S3 bucket conditions.

### [AmazonS3BucketConditions.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.AmazonS3BucketConditions.Types)

Container for nested types declared in the AmazonS3BucketConditions message type.

### [AmazonS3BucketRegex](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.AmazonS3BucketRegex)

Amazon S3 bucket regex.

### [AnalyzeDataSourceRiskDetails](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.AnalyzeDataSourceRiskDetails)

Result of a risk analysis operation request.

### [AnalyzeDataSourceRiskDetails.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.AnalyzeDataSourceRiskDetails.Types)

Container for nested types declared in the AnalyzeDataSourceRiskDetails message type.

### [AnalyzeDataSourceRiskDetails.Types.CategoricalStatsResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.AnalyzeDataSourceRiskDetails.Types.CategoricalStatsResult)

Result of the categorical stats computation.

### [AnalyzeDataSourceRiskDetails.Types.CategoricalStatsResult.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.AnalyzeDataSourceRiskDetails.Types.CategoricalStatsResult.Types)

Container for nested types declared in the CategoricalStatsResult message type.

### [AnalyzeDataSourceRiskDetails.Types.CategoricalStatsResult.Types.CategoricalStatsHistogramBucket](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.AnalyzeDataSourceRiskDetails.Types.CategoricalStatsResult.Types.CategoricalStatsHistogramBucket)

Histogram of value frequencies in the column.

### [AnalyzeDataSourceRiskDetails.Types.DeltaPresenceEstimationResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.AnalyzeDataSourceRiskDetails.Types.DeltaPresenceEstimationResult)

Result of the δ-presence computation. Note that these results are an estimation, not exact values.

### [AnalyzeDataSourceRiskDetails.Types.DeltaPresenceEstimationResult.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.AnalyzeDataSourceRiskDetails.Types.DeltaPresenceEstimationResult.Types)

Container for nested types declared in the DeltaPresenceEstimationResult message type.

### [AnalyzeDataSourceRiskDetails.Types.DeltaPresenceEstimationResult.Types.DeltaPresenceEstimationHistogramBucket](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.AnalyzeDataSourceRiskDetails.Types.DeltaPresenceEstimationResult.Types.DeltaPresenceEstimationHistogramBucket)

A DeltaPresenceEstimationHistogramBucket message with the following values: min_probability: 0.1 max_probability: 0.2 frequency: 42 means that there are 42 records for which δ is in [0.1, 0.2). An important particular case is when min_probability = max_probability = 1: then, every individual who shares this quasi-identifier combination is in the dataset.

### [AnalyzeDataSourceRiskDetails.Types.DeltaPresenceEstimationResult.Types.DeltaPresenceEstimationQuasiIdValues](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.AnalyzeDataSourceRiskDetails.Types.DeltaPresenceEstimationResult.Types.DeltaPresenceEstimationQuasiIdValues)

A tuple of values for the quasi-identifier columns.

### [AnalyzeDataSourceRiskDetails.Types.KAnonymityResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.AnalyzeDataSourceRiskDetails.Types.KAnonymityResult)

Result of the k-anonymity computation.

### [AnalyzeDataSourceRiskDetails.Types.KAnonymityResult.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.AnalyzeDataSourceRiskDetails.Types.KAnonymityResult.Types)

Container for nested types declared in the KAnonymityResult message type.

### [AnalyzeDataSourceRiskDetails.Types.KAnonymityResult.Types.KAnonymityEquivalenceClass](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.AnalyzeDataSourceRiskDetails.Types.KAnonymityResult.Types.KAnonymityEquivalenceClass)

The set of columns' values that share the same ldiversity value

### [AnalyzeDataSourceRiskDetails.Types.KAnonymityResult.Types.KAnonymityHistogramBucket](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.AnalyzeDataSourceRiskDetails.Types.KAnonymityResult.Types.KAnonymityHistogramBucket)

Histogram of k-anonymity equivalence classes.

### [AnalyzeDataSourceRiskDetails.Types.KMapEstimationResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.AnalyzeDataSourceRiskDetails.Types.KMapEstimationResult)

Result of the reidentifiability analysis. Note that these results are an estimation, not exact values.

### [AnalyzeDataSourceRiskDetails.Types.KMapEstimationResult.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.AnalyzeDataSourceRiskDetails.Types.KMapEstimationResult.Types)

Container for nested types declared in the KMapEstimationResult message type.

### [AnalyzeDataSourceRiskDetails.Types.KMapEstimationResult.Types.KMapEstimationHistogramBucket](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.AnalyzeDataSourceRiskDetails.Types.KMapEstimationResult.Types.KMapEstimationHistogramBucket)

A KMapEstimationHistogramBucket message with the following values: min_anonymity: 3 max_anonymity: 5 frequency: 42 means that there are 42 records whose quasi-identifier values correspond to 3, 4 or 5 people in the overlying population. An important particular case is when min_anonymity = max_anonymity = 1: the frequency field then corresponds to the number of uniquely identifiable records.

### [AnalyzeDataSourceRiskDetails.Types.KMapEstimationResult.Types.KMapEstimationQuasiIdValues](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.AnalyzeDataSourceRiskDetails.Types.KMapEstimationResult.Types.KMapEstimationQuasiIdValues)

A tuple of values for the quasi-identifier columns.

### [AnalyzeDataSourceRiskDetails.Types.LDiversityResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.AnalyzeDataSourceRiskDetails.Types.LDiversityResult)

Result of the l-diversity computation.

### [AnalyzeDataSourceRiskDetails.Types.LDiversityResult.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.AnalyzeDataSourceRiskDetails.Types.LDiversityResult.Types)

Container for nested types declared in the LDiversityResult message type.

### [AnalyzeDataSourceRiskDetails.Types.LDiversityResult.Types.LDiversityEquivalenceClass](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.AnalyzeDataSourceRiskDetails.Types.LDiversityResult.Types.LDiversityEquivalenceClass)

The set of columns' values that share the same ldiversity value.

### [AnalyzeDataSourceRiskDetails.Types.LDiversityResult.Types.LDiversityHistogramBucket](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.AnalyzeDataSourceRiskDetails.Types.LDiversityResult.Types.LDiversityHistogramBucket)

Histogram of l-diversity equivalence class sensitive value frequencies.

### [AnalyzeDataSourceRiskDetails.Types.NumericalStatsResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.AnalyzeDataSourceRiskDetails.Types.NumericalStatsResult)

Result of the numerical stats computation.

### [AnalyzeDataSourceRiskDetails.Types.RequestedRiskAnalysisOptions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.AnalyzeDataSourceRiskDetails.Types.RequestedRiskAnalysisOptions)

Risk analysis options.

### [AwsAccount](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.AwsAccount)

AWS account.

### [AwsAccountRegex](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.AwsAccountRegex)

AWS account regex.

### [BatchContentItem](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.BatchContentItem)

Represents a batch of content to inspect or redact.

### [BatchContentLocation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.BatchContentLocation)

Location within a batch of content.

### [BigQueryDiscoveryTarget](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.BigQueryDiscoveryTarget)

Target used to match against for discovery with BigQuery tables

### [BigQueryField](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.BigQueryField)

Message defining a field of a BigQuery table.

### [BigQueryKey](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.BigQueryKey)

Row key for identifying a record in BigQuery table.

### [BigQueryOptions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.BigQueryOptions)

Options defining BigQuery table and row identifiers.

### [BigQueryOptions.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.BigQueryOptions.Types)

Container for nested types declared in the BigQueryOptions message type.

### [BigQueryRegex](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.BigQueryRegex)

A pattern to match against one or more tables, datasets, or projects that contain BigQuery tables. At least one pattern must be specified. Regular expressions use RE2 [syntax](https://github.com/google/re2/wiki/Syntax); a guide can be found under the google/re2 repository on GitHub.

### [BigQueryRegexes](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.BigQueryRegexes)

A collection of regular expressions to determine what tables to match against.

### [BigQueryTable](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.BigQueryTable)

Message defining the location of a BigQuery table. A table is uniquely identified by its project_id, dataset_id, and table_name. Within a query a table is often referenced with a string in the format of: `<project_id>:<dataset_id>.<table_id>` or `<project_id>.<dataset_id>.<table_id>`.

### [BigQueryTableCollection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.BigQueryTableCollection)

Specifies a collection of BigQuery tables. Used for Discovery.

### [BigQueryTableTypes](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.BigQueryTableTypes)

The types of BigQuery tables supported by Cloud DLP.

### [BoundingBox](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.BoundingBox)

Bounding box encompassing detected text within an image. Coordinates are in pixels and strictly within the image or frame bounds.

### [BucketingConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.BucketingConfig)

Generalization function that buckets values based on ranges. The ranges and replacement values are dynamically provided by the user for custom behavior, such as 1-30 -> LOW, 31-65 -> MEDIUM, 66-100 -> HIGH.

This can be used on data of type: number, long, string, timestamp.

If the bound `Value` type differs from the type of data being transformed, we will first attempt converting the type of the data to be transformed to match the type of the bound before comparing. See <https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-bucketing> to learn more.

### [BucketingConfig.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.BucketingConfig.Types)

Container for nested types declared in the BucketingConfig message type.

### [BucketingConfig.Types.Bucket](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.BucketingConfig.Types.Bucket)

Bucket is represented as a range, along with replacement values.

### [ByteContentItem](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ByteContentItem)

Container for bytes to inspect or redact.

### [ByteContentItem.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ByteContentItem.Types)

Container for nested types declared in the ByteContentItem message type.

### [CancelDlpJobRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.CancelDlpJobRequest)

The request message for canceling a DLP job.

### [CharacterMaskConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.CharacterMaskConfig)

Partially mask a string by replacing a given number of characters with a fixed character. Masking can start from the beginning or end of the string. This can be used on data of any type (numbers, longs, and so on) and when de-identifying structured data we'll attempt to preserve the original data's type. (This allows you to take a long like 123 and modify it to a string like **3.

### [CharsToIgnore](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.CharsToIgnore)

Characters to skip when doing deidentification of a value. These will be left alone and skipped.

### [CharsToIgnore.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.CharsToIgnore.Types)

Container for nested types declared in the CharsToIgnore message type.

### [CloudSqlDiscoveryTarget](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.CloudSqlDiscoveryTarget)

Target used to match against for discovery with Cloud SQL tables.

### [CloudSqlIamCredential](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.CloudSqlIamCredential)

Use IAM authentication to connect. This requires the Cloud SQL IAM feature to be enabled on the instance, which is not the default for Cloud SQL. See <https://docs.cloud.google.com/sql/docs/postgres/authentication> and <https://docs.cloud.google.com/sql/docs/mysql/authentication>.

### [CloudSqlProperties](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.CloudSqlProperties)

Cloud SQL connection properties.

### [CloudSqlProperties.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.CloudSqlProperties.Types)

Container for nested types declared in the CloudSqlProperties message type.

### [CloudStorageDiscoveryTarget](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.CloudStorageDiscoveryTarget)

Target used to match against for discovery with Cloud Storage buckets.

### [CloudStorageFileSet](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.CloudStorageFileSet)

Message representing a set of files in Cloud Storage.

### [CloudStorageOptions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.CloudStorageOptions)

Options defining a file or a set of files within a Cloud Storage bucket.

### [CloudStorageOptions.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.CloudStorageOptions.Types)

Container for nested types declared in the CloudStorageOptions message type.

### [CloudStorageOptions.Types.FileSet](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.CloudStorageOptions.Types.FileSet)

Set of files to scan.

### [CloudStoragePath](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.CloudStoragePath)

Message representing a single file or path in Cloud Storage.

### [CloudStorageRegex](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.CloudStorageRegex)

A pattern to match against one or more file stores. At least one pattern must be specified. Regular expressions use RE2 [syntax](https://github.com/google/re2/wiki/Syntax); a guide can be found under the google/re2 repository on GitHub.

### [CloudStorageRegexFileSet](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.CloudStorageRegexFileSet)

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



### [CloudStorageResourceReference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.CloudStorageResourceReference)

Identifies a single Cloud Storage bucket.

### [Color](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Color)

Represents a color in the RGB color space.

### [ColumnDataProfile](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ColumnDataProfile)

The profile for a scanned column within a table.

### [ColumnDataProfile.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ColumnDataProfile.Types)

Container for nested types declared in the ColumnDataProfile message type.

### [ColumnDataProfileName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ColumnDataProfileName)

Resource name for the `ColumnDataProfile` resource.

### [Connection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Connection)

A data connection to allow the DLP API to profile data in locations that require additional configuration.

### [ConnectionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ConnectionName)

Resource name for the `Connection` resource.

### [Container](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Container)

Represents a container that may contain DLP findings. Examples of a container include a file, table, or database record.

### [ContentItem](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ContentItem)

Type of content to inspect.

### [ContentLocation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ContentLocation)

Precise location of the finding within a document, record, image, or metadata container.

### [ContentMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ContentMetadata)

Metadata on content to be scanned.

### [ContentPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ContentPolicy)

A policy to apply to content based on its inspection findings.

### [ContentPolicy.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ContentPolicy.Types)

Container for nested types declared in the ContentPolicy message type.

### [ContentPolicy.Types.LoggingConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ContentPolicy.Types.LoggingConfig)

A single logging configuration.

### [ContentPolicy.Types.LoggingConfig.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ContentPolicy.Types.LoggingConfig.Types)

Container for nested types declared in the LoggingConfig message type.

### [ContentPolicy.Types.LoggingConfig.Types.LogToBigQuery](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ContentPolicy.Types.LoggingConfig.Types.LogToBigQuery)

Configuration for logging content policy actions to BigQuery.

### [ContentPolicy.Types.PolicyAction](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ContentPolicy.Types.PolicyAction)

A possible action to take when applying a content policy.

### [ContentPolicy.Types.PolicyRule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ContentPolicy.Types.PolicyRule)

A single policy rule. The first rule to match from the list above controls the result.

### [ContentPolicy.Types.PolicyRule.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ContentPolicy.Types.PolicyRule.Types)

Container for nested types declared in the PolicyRule message type.

### [ContentPolicy.Types.PolicyRule.Types.PolicyCondition](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ContentPolicy.Types.PolicyRule.Types.PolicyCondition)

A condition that must match for this rule to apply.

### [ContentPolicy.Types.PolicyRule.Types.PolicyCondition.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ContentPolicy.Types.PolicyRule.Types.PolicyCondition.Types)

Container for nested types declared in the PolicyCondition message type.

### [ContentPolicy.Types.PolicyRule.Types.PolicyCondition.Types.InfoTypeCondition](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ContentPolicy.Types.PolicyRule.Types.PolicyCondition.Types.InfoTypeCondition)

A info type based condition.

### [ContentPolicy.Types.PolicyRule.Types.PolicyCondition.Types.InfoTypeCondition.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ContentPolicy.Types.PolicyRule.Types.PolicyCondition.Types.InfoTypeCondition.Types)

Container for nested types declared in the InfoTypeCondition message type.

### [ContentPolicy.Types.PolicyRule.Types.PolicyCondition.Types.InfoTypeCondition.Types.InfoTypes](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ContentPolicy.Types.PolicyRule.Types.PolicyCondition.Types.InfoTypeCondition.Types.InfoTypes)

Info types to match.

### [ContentPolicyName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ContentPolicyName)

Resource name for the `ContentPolicy` resource.

### [Conversation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Conversation)

Complete conversation or slice of a conversation. It is assumed that all included messages are contiguous and ordered in chronological order.

### [ConversationLocation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ConversationLocation)

Location within a conversation.

### [ConversationLocation.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ConversationLocation.Types)

Container for nested types declared in the ConversationLocation message type.

### [ConversationLocation.Types.AllMessages](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ConversationLocation.Types.AllMessages)

If set, indicates that the finding applies to all messages in the conversation.

### [ConversationMessage](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ConversationMessage)

Single message in a conversation.

### [ConversationMessage.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ConversationMessage.Types)

Container for nested types declared in the ConversationMessage message type.

### [CreateConnectionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.CreateConnectionRequest)

Request message for CreateConnection.

### [CreateContentPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.CreateContentPolicyRequest)

Request message for CreateContentPolicy.

### [CreateDeidentifyTemplateRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.CreateDeidentifyTemplateRequest)

Request message for CreateDeidentifyTemplate.

### [CreateDiscoveryConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.CreateDiscoveryConfigRequest)

Request message for CreateDiscoveryConfig.

### [CreateDlpJobRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.CreateDlpJobRequest)

Request message for CreateDlpJobRequest. Used to initiate long running jobs such as calculating risk metrics or inspecting Google Cloud Storage.

### [CreateInspectTemplateRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.CreateInspectTemplateRequest)

Request message for CreateInspectTemplate.

### [CreateJobTriggerRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.CreateJobTriggerRequest)

Request message for CreateJobTrigger.

### [CreateStoredInfoTypeRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.CreateStoredInfoTypeRequest)

Request message for CreateStoredInfoType.

### [CryptoDeterministicConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.CryptoDeterministicConfig)

Pseudonymization method that generates deterministic encryption for the given input. Outputs a base64 encoded representation of the encrypted output. Uses AES-SIV based on the RFC <https://tools.ietf.org/html/rfc5297>.

### [CryptoHashConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.CryptoHashConfig)

Pseudonymization method that generates surrogates via cryptographic hashing. Uses SHA-256. The key size must be either 32 or 64 bytes. Outputs a base64 encoded representation of the hashed output (for example, L7k0BHmF1ha5U3NfGykjro4xWi1MPVQPjhMAZbSV9mM=). Currently, only string and integer values can be hashed. See <https://docs.cloud.google.com/sensitive-data-protection/docs/pseudonymization> to learn more.

### [CryptoKey](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.CryptoKey)

This is a data encryption key (DEK) (as opposed to a key encryption key (KEK) stored by Cloud Key Management Service (Cloud KMS). When using Cloud KMS to wrap or unwrap a DEK, be sure to set an appropriate IAM policy on the KEK to ensure an attacker cannot unwrap the DEK.

### [CryptoReplaceFfxFpeConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.CryptoReplaceFfxFpeConfig)

Replaces an identifier with a surrogate using Format Preserving Encryption (FPE) with the FFX mode of operation; however when used in the `ReidentifyContent` API method, it serves the opposite function by reversing the surrogate back into the original identifier. The identifier must be encoded as ASCII. For a given crypto key and context, the same identifier will be replaced with the same surrogate. Identifiers must be at least two characters long. In the case that the identifier is the empty string, it will be skipped. See <https://docs.cloud.google.com/sensitive-data-protection/docs/pseudonymization> to learn more.

Note: We recommend using CryptoDeterministicConfig for all use cases which do not require preserving the input alphabet space and size, plus warrant referential integrity. FPE incurs significant latency costs.

### [CryptoReplaceFfxFpeConfig.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.CryptoReplaceFfxFpeConfig.Types)

Container for nested types declared in the CryptoReplaceFfxFpeConfig message type.

### [CustomInfoType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.CustomInfoType)

Custom information type provided by the user. Used to find domain-specific sensitive information configurable to the data in question.

### [CustomInfoType.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.CustomInfoType.Types)

Container for nested types declared in the CustomInfoType message type.

### [CustomInfoType.Types.DetectionRule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.CustomInfoType.Types.DetectionRule)

Deprecated; use `InspectionRuleSet` instead. Rule for modifying a `CustomInfoType` to alter behavior under certain circumstances, depending on the specific details of the rule. Not supported for the `surrogate_type` custom infoType.

### [CustomInfoType.Types.DetectionRule.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.CustomInfoType.Types.DetectionRule.Types)

Container for nested types declared in the DetectionRule message type.

### [CustomInfoType.Types.DetectionRule.Types.HotwordRule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.CustomInfoType.Types.DetectionRule.Types.HotwordRule)

The rule that adjusts the likelihood of findings within a certain proximity of hotwords.

### [CustomInfoType.Types.DetectionRule.Types.LikelihoodAdjustment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.CustomInfoType.Types.DetectionRule.Types.LikelihoodAdjustment)

Message for specifying an adjustment to the likelihood of a finding as part of a detection rule.

### [CustomInfoType.Types.DetectionRule.Types.Proximity](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.CustomInfoType.Types.DetectionRule.Types.Proximity)

Message for specifying a window around a finding to apply a detection rule.

### [CustomInfoType.Types.Dictionary](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.CustomInfoType.Types.Dictionary)

Custom information type based on a dictionary of words or phrases. This can be used to match sensitive information specific to the data, such as a list of employee IDs or job titles.

Dictionary words are case-insensitive and all characters other than letters and digits in the unicode [Basic Multilingual Plane](https://en.wikipedia.org/wiki/Plane_%28Unicode%29#Basic_Multilingual_Plane) will be replaced with whitespace when scanning for matches, so the dictionary phrase "Sam Johnson" will match all three phrases "sam johnson", "Sam, Johnson", and "Sam (Johnson)". Additionally, the characters surrounding any match must be of a different type than the adjacent characters within the word, so letters must be next to non-letters and digits next to non-digits. For example, the dictionary word "jen" will match the first three letters of the text "jen123" but will return no matches for "jennifer".

Dictionary words containing a large number of characters that are not letters or digits may result in unexpected findings because such characters are treated as whitespace. The [limits](https://docs.cloud.google.com/sensitive-data-protection/limits) page contains details about the size limits of dictionaries. For dictionaries that do not fit within these constraints, consider using `LargeCustomDictionaryConfig` in the `StoredInfoType` API.

### [CustomInfoType.Types.Dictionary.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.CustomInfoType.Types.Dictionary.Types)

Container for nested types declared in the Dictionary message type.

### [CustomInfoType.Types.Dictionary.Types.WordList](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.CustomInfoType.Types.Dictionary.Types.WordList)

Message defining a list of words or phrases to search for in the data.

### [CustomInfoType.Types.FileLabelInfoType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.CustomInfoType.Types.FileLabelInfoType)

Configuration for a custom infoType that detects file labels.

### [CustomInfoType.Types.FileLabelInfoType.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.CustomInfoType.Types.FileLabelInfoType.Types)

Container for nested types declared in the FileLabelInfoType message type.

### [CustomInfoType.Types.FileLabelInfoType.Types.GoogleDriveLabel](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.CustomInfoType.Types.FileLabelInfoType.Types.GoogleDriveLabel)

Google Drive labels published by Google.

### [CustomInfoType.Types.FileLabelInfoType.Types.GoogleDriveLabel.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.CustomInfoType.Types.FileLabelInfoType.Types.GoogleDriveLabel.Types)

Container for nested types declared in the GoogleDriveLabel message type.

### [CustomInfoType.Types.FileLabelInfoType.Types.GoogleDriveLabel.Types.LabelField](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.CustomInfoType.Types.FileLabelInfoType.Types.GoogleDriveLabel.Types.LabelField)

The field values of the Google Drive label to match.

### [CustomInfoType.Types.FileLabelInfoType.Types.SensitivityLabel](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.CustomInfoType.Types.FileLabelInfoType.Types.SensitivityLabel)

Sensitivity labels published by Microsoft.

### [CustomInfoType.Types.MetadataKeyValueExpression](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.CustomInfoType.Types.MetadataKeyValueExpression)

Configuration for a custom infoType that detects key-value pairs in the metadata matching the specified regular expressions.

### [CustomInfoType.Types.Regex](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.CustomInfoType.Types.Regex)

Message defining a custom regular expression.

### [CustomInfoType.Types.SurrogateType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.CustomInfoType.Types.SurrogateType)

Message for detecting output from deidentification transformations such as [`CryptoReplaceFfxFpeConfig`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.deidentifyTemplates#cryptoreplaceffxfpeconfig). These types of transformations are those that perform pseudonymization, thereby producing a "surrogate" as output. This should be used in conjunction with a field on the transformation such as `surrogate_info_type`. This CustomInfoType does not support the use of `detection_rules`.

### [DataProfileAction](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DataProfileAction)

A task to execute when a data profile has been generated.

### [DataProfileAction.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DataProfileAction.Types)

Container for nested types declared in the DataProfileAction message type.

### [DataProfileAction.Types.Export](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DataProfileAction.Types.Export)

If set, the detailed data profiles will be persisted to the location of your choice whenever updated.

### [DataProfileAction.Types.PubSubNotification](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DataProfileAction.Types.PubSubNotification)

Send a Pub/Sub message into the given Pub/Sub topic to connect other systems to data profile generation. The message payload data will be the byte serialization of `DataProfilePubSubMessage`.

### [DataProfileAction.Types.PubSubNotification.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DataProfileAction.Types.PubSubNotification.Types)

Container for nested types declared in the PubSubNotification message type.

### [DataProfileAction.Types.PublishToChronicle](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DataProfileAction.Types.PublishToChronicle)

Message expressing intention to publish to Google Security Operations.

### [DataProfileAction.Types.PublishToDataplexCatalog](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DataProfileAction.Types.PublishToDataplexCatalog)

Create Dataplex Universal Catalog aspects for profiled resources with the aspect type Sensitive Data Protection Profile. To learn more about aspects, see <https://docs.cloud.google.com/sensitive-data-protection/docs/add-aspects>.

### [DataProfileAction.Types.PublishToSecurityCommandCenter](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DataProfileAction.Types.PublishToSecurityCommandCenter)

If set, a summary finding will be created or updated in Security Command Center for each profile.

### [DataProfileAction.Types.TagResources](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DataProfileAction.Types.TagResources)

If set, attaches the [tags](https://docs.cloud.google.com/resource-manager/docs/tags/tags-overview) provided to profiled resources. Tags support [access control](https://docs.cloud.google.com/iam/docs/tags-access-control). You can conditionally grant or deny access to a resource based on whether the resource has a specific tag.

### [DataProfileAction.Types.TagResources.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DataProfileAction.Types.TagResources.Types)

Container for nested types declared in the TagResources message type.

### [DataProfileAction.Types.TagResources.Types.TagCondition](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DataProfileAction.Types.TagResources.Types.TagCondition)

The tag to attach to profiles matching the condition. At most one `TagCondition` can be specified per sensitivity level.

### [DataProfileAction.Types.TagResources.Types.TagValue](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DataProfileAction.Types.TagResources.Types.TagValue)

A value of a tag.

### [DataProfileBigQueryRowSchema](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DataProfileBigQueryRowSchema)

The schema of data to be saved to the BigQuery table when the `DataProfileAction` is enabled.

### [DataProfileConfigSnapshot](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DataProfileConfigSnapshot)

Snapshot of the configurations used to generate the profile.

### [DataProfileFinding](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DataProfileFinding)

Details about a piece of potentially sensitive information that was detected when the data resource was profiled.

### [DataProfileFindingLocation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DataProfileFindingLocation)

Location of a data profile finding within a resource.

### [DataProfileFindingRecordLocation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DataProfileFindingRecordLocation)

Location of a finding within a resource that produces a table data profile.

### [DataProfileJobConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DataProfileJobConfig)

Configuration for setting up a job to scan resources for profile generation. Only one data profile configuration may exist per organization, folder, or project.

The generated data profiles are retained according to the [data retention policy](https://docs.cloud.google.com/sensitive-data-protection/docs/data-profiles#retention).

### [DataProfileLocation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DataProfileLocation)

The data that will be profiled.

### [DataProfilePubSubCondition](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DataProfilePubSubCondition)

A condition for determining whether a Pub/Sub should be triggered.

### [DataProfilePubSubCondition.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DataProfilePubSubCondition.Types)

Container for nested types declared in the DataProfilePubSubCondition message type.

### [DataProfilePubSubCondition.Types.PubSubCondition](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DataProfilePubSubCondition.Types.PubSubCondition)

A condition consisting of a value.

### [DataProfilePubSubCondition.Types.PubSubExpressions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DataProfilePubSubCondition.Types.PubSubExpressions)

An expression, consisting of an operator and conditions.

### [DataProfilePubSubCondition.Types.PubSubExpressions.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DataProfilePubSubCondition.Types.PubSubExpressions.Types)

Container for nested types declared in the PubSubExpressions message type.

### [DataProfilePubSubMessage](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DataProfilePubSubMessage)

Pub/Sub topic message for a DataProfileAction.PubSubNotification event. To receive a message of protocol buffer schema type, convert the message data to an object of this proto class.

### [DataRiskLevel](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DataRiskLevel)

Score is a summary of all elements in the data profile. A higher number means more risk.

### [DataRiskLevel.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DataRiskLevel.Types)

Container for nested types declared in the DataRiskLevel message type.

### [DataSourceType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DataSourceType)

Message used to identify the type of resource being profiled.

### [DatabaseResourceCollection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DatabaseResourceCollection)

Match database resources using regex filters. Examples of database resources are tables, views, and stored procedures.

### [DatabaseResourceReference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DatabaseResourceReference)

Identifies a single database resource, like a table within a database.

### [DatabaseResourceRegex](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DatabaseResourceRegex)

A pattern to match against one or more database resources. At least one pattern must be specified. Regular expressions use RE2 [syntax](https://github.com/google/re2/wiki/Syntax); a guide can be found under the google/re2 repository on GitHub.

### [DatabaseResourceRegexes](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DatabaseResourceRegexes)

A collection of regular expressions to determine what database resources to match against.

### [DatastoreKey](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DatastoreKey)

Record key for a finding in Cloud Datastore.

### [DatastoreOptions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DatastoreOptions)

Options defining a data set within Google Cloud Datastore.

### [DateShiftConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DateShiftConfig)

Shifts dates by random number of days, with option to be consistent for the same context. See <https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-date-shifting> to learn more.

### [DateTime](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DateTime)

Message for a date time object. e.g. 2018-01-01, 5th August.

### [DateTime.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DateTime.Types)

Container for nested types declared in the DateTime message type.

### [DateTime.Types.TimeZone](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DateTime.Types.TimeZone)

Time zone of the date time object.

### [DeidentifyConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DeidentifyConfig)

The configuration that controls how the data will change.

### [DeidentifyContentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DeidentifyContentRequest)

Request to de-identify a ContentItem.

### [DeidentifyContentResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DeidentifyContentResponse)

Results of de-identifying a ContentItem.

### [DeidentifyDataSourceDetails](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DeidentifyDataSourceDetails)

The results of a [Deidentify][google.privacy.dlp.v2.Action.Deidentify] action from an inspect job.

### [DeidentifyDataSourceDetails.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DeidentifyDataSourceDetails.Types)

Container for nested types declared in the DeidentifyDataSourceDetails message type.

### [DeidentifyDataSourceDetails.Types.RequestedDeidentifyOptions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DeidentifyDataSourceDetails.Types.RequestedDeidentifyOptions)

De-identification options.

### [DeidentifyDataSourceStats](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DeidentifyDataSourceStats)

Summary of what was modified during a transformation.

### [DeidentifyTemplate](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DeidentifyTemplate)

DeidentifyTemplates contains instructions on how to de-identify content. See <https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-templates> to learn more.

### [DeidentifyTemplateName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DeidentifyTemplateName)

Resource name for the `DeidentifyTemplate` resource.

### [DeleteConnectionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DeleteConnectionRequest)

Request message for DeleteConnection.

### [DeleteContentPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DeleteContentPolicyRequest)

Request message for DeleteContentPolicy.

### [DeleteDeidentifyTemplateRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DeleteDeidentifyTemplateRequest)

Request message for DeleteDeidentifyTemplate.

### [DeleteDiscoveryConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DeleteDiscoveryConfigRequest)

Request message for DeleteDiscoveryConfig.

### [DeleteDlpJobRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DeleteDlpJobRequest)

The request message for deleting a DLP job.

### [DeleteFileStoreDataProfileRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DeleteFileStoreDataProfileRequest)

Request message for DeleteFileStoreProfile.

### [DeleteInspectTemplateRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DeleteInspectTemplateRequest)

Request message for DeleteInspectTemplate.

### [DeleteJobTriggerRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DeleteJobTriggerRequest)

Request message for DeleteJobTrigger.

### [DeleteStoredInfoTypeRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DeleteStoredInfoTypeRequest)

Request message for DeleteStoredInfoType.

### [DeleteTableDataProfileRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DeleteTableDataProfileRequest)

Request message for DeleteTableProfile.

### [Disabled](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Disabled)

Do not profile the tables.

### [DiscoveryBigQueryConditions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DiscoveryBigQueryConditions)

Requirements that must be true before a table is scanned in discovery for the first time. There is an AND relationship between the top-level attributes. Additionally, minimum conditions with an OR relationship that must be met before Cloud DLP scans a table can be set (like a minimum row count or a minimum table age).

### [DiscoveryBigQueryConditions.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DiscoveryBigQueryConditions.Types)

Container for nested types declared in the DiscoveryBigQueryConditions message type.

### [DiscoveryBigQueryConditions.Types.OrConditions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DiscoveryBigQueryConditions.Types.OrConditions)

There is an OR relationship between these attributes. They are used to determine if a table should be scanned or not in Discovery.

### [DiscoveryBigQueryFilter](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DiscoveryBigQueryFilter)

Determines what tables will have profiles generated within an organization or project. Includes the ability to filter by regular expression patterns on project ID, dataset ID, and table ID.

### [DiscoveryBigQueryFilter.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DiscoveryBigQueryFilter.Types)

Container for nested types declared in the DiscoveryBigQueryFilter message type.

### [DiscoveryBigQueryFilter.Types.AllOtherBigQueryTables](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DiscoveryBigQueryFilter.Types.AllOtherBigQueryTables)

Catch-all for all other tables not specified by other filters. Should always be last, except for single-table configurations, which will only have a TableReference target.

### [DiscoveryCloudSqlConditions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DiscoveryCloudSqlConditions)

Requirements that must be true before a table is profiled for the first time.

### [DiscoveryCloudSqlConditions.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DiscoveryCloudSqlConditions.Types)

Container for nested types declared in the DiscoveryCloudSqlConditions message type.

### [DiscoveryCloudSqlFilter](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DiscoveryCloudSqlFilter)

Determines what tables will have profiles generated within an organization or project. Includes the ability to filter by regular expression patterns on project ID, location, instance, database, and database resource name.

### [DiscoveryCloudSqlGenerationCadence](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DiscoveryCloudSqlGenerationCadence)

How often existing tables should have their profiles refreshed. New tables are scanned as quickly as possible depending on system capacity.

### [DiscoveryCloudSqlGenerationCadence.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DiscoveryCloudSqlGenerationCadence.Types)

Container for nested types declared in the DiscoveryCloudSqlGenerationCadence message type.

### [DiscoveryCloudSqlGenerationCadence.Types.SchemaModifiedCadence](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DiscoveryCloudSqlGenerationCadence.Types.SchemaModifiedCadence)

How frequently to modify the profile when the table's schema is modified.

### [DiscoveryCloudSqlGenerationCadence.Types.SchemaModifiedCadence.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DiscoveryCloudSqlGenerationCadence.Types.SchemaModifiedCadence.Types)

Container for nested types declared in the SchemaModifiedCadence message type.

### [DiscoveryCloudStorageConditions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DiscoveryCloudStorageConditions)

Requirements that must be true before a Cloud Storage bucket or object is scanned in discovery for the first time. There is an AND relationship between the top-level attributes.

### [DiscoveryCloudStorageConditions.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DiscoveryCloudStorageConditions.Types)

Container for nested types declared in the DiscoveryCloudStorageConditions message type.

### [DiscoveryCloudStorageFilter](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DiscoveryCloudStorageFilter)

Determines which buckets will have profiles generated within an organization or project. Includes the ability to filter by regular expression patterns on project ID and bucket name.

### [DiscoveryCloudStorageGenerationCadence](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DiscoveryCloudStorageGenerationCadence)

How often existing buckets should have their profiles refreshed. New buckets are scanned as quickly as possible depending on system capacity.

### [DiscoveryConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DiscoveryConfig)

Configuration for discovery to scan resources for profile generation. Only one discovery configuration may exist per organization, folder, or project.

The generated data profiles are retained according to the [data retention policy](https://docs.cloud.google.com/sensitive-data-protection/docs/data-profiles#retention).

### [DiscoveryConfig.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DiscoveryConfig.Types)

Container for nested types declared in the DiscoveryConfig message type.

### [DiscoveryConfig.Types.OrgConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DiscoveryConfig.Types.OrgConfig)

Project and scan location information. Only set when the parent is an org.

### [DiscoveryConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DiscoveryConfigName)

Resource name for the `DiscoveryConfig` resource.

### [DiscoveryFileStoreConditions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DiscoveryFileStoreConditions)

Requirements that must be true before a file store is scanned in discovery for the first time. There is an AND relationship between the top-level attributes.

### [DiscoveryGenerationCadence](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DiscoveryGenerationCadence)

What must take place for a profile to be updated and how frequently it should occur. New tables are scanned as quickly as possible depending on system capacity.

### [DiscoveryInspectTemplateModifiedCadence](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DiscoveryInspectTemplateModifiedCadence)

The cadence at which to update data profiles when the inspection rules defined by the `InspectTemplate` change.

### [DiscoveryOtherCloudConditions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DiscoveryOtherCloudConditions)

Requirements that must be true before a resource is profiled for the first time.

### [DiscoveryOtherCloudFilter](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DiscoveryOtherCloudFilter)

Determines which resources from the other cloud will have profiles generated. Includes the ability to filter by resource names.

### [DiscoveryOtherCloudGenerationCadence](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DiscoveryOtherCloudGenerationCadence)

How often existing resources should have their profiles refreshed. New resources are scanned as quickly as possible depending on system capacity.

### [DiscoverySchemaModifiedCadence](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DiscoverySchemaModifiedCadence)

The cadence at which to update data profiles when a schema is modified.

### [DiscoveryStartingLocation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DiscoveryStartingLocation)

The location to begin a discovery scan. Denotes an organization ID or folder ID within an organization.

### [DiscoveryTableModifiedCadence](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DiscoveryTableModifiedCadence)

The cadence at which to update data profiles when a table is modified.

### [DiscoveryTarget](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DiscoveryTarget)

Target used to match against for Discovery.

### [DiscoveryVertexDatasetConditions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DiscoveryVertexDatasetConditions)

Requirements that must be true before a dataset is profiled for the first time.

### [DiscoveryVertexDatasetFilter](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DiscoveryVertexDatasetFilter)

Determines what datasets will have profiles generated within an organization or project. Includes the ability to filter by regular expression patterns on project ID or dataset regex.

### [DiscoveryVertexDatasetGenerationCadence](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DiscoveryVertexDatasetGenerationCadence)

How often existing datasets should have their profiles refreshed. New datasets are scanned as quickly as possible depending on system capacity.

### [DlpContentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpContentName)

Resource name for the `DlpContent` resource.

### [DlpJob](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpJob)

Combines all of the information about a DLP job.

### [DlpJob.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpJob.Types)

Container for nested types declared in the DlpJob message type.

### [DlpJobName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpJobName)

Resource name for the `DlpJob` resource.

### [DlpService](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpService)

Sensitive Data Protection provides access to a powerful sensitive data inspection, classification, and de-identification platform that works on text, images, and Google Cloud storage repositories. To learn more about concepts and find how-to guides see <https://docs.cloud.google.com/sensitive-data-protection/docs/>.

### [DlpService.DlpServiceBase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpService.DlpServiceBase)

Base class for server-side implementations of DlpService

### [DlpService.DlpServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpService.DlpServiceClient)

Client for DlpService

### [DlpServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpServiceClient)

DlpService client wrapper, for convenient use.

### [DlpServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpServiceClientBuilder)

Builder class for [DlpServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpServiceClient) to provide simple configuration of credentials, endpoint etc.

### [DlpServiceClientImpl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpServiceClientImpl)

DlpService client wrapper implementation, for convenient use.

### [DlpServiceSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpServiceSettings)

Settings for [DlpServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpServiceClient) instances.

### [DocumentLocation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DocumentLocation)

Location of a finding within a document.

### [Domain](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Domain)

A domain represents a thematic category that a data profile can fall under.

### [Domain.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Domain.Types)

Container for nested types declared in the Domain message type.

### [Encloses](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Encloses)

Defines a condition where one bounding box encloses another.

### [EntityId](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.EntityId)

An entity in a dataset is a field or set of fields that correspond to a single person. For example, in medical records the `EntityId` might be a patient identifier, or for financial records it might be an account identifier. This message is used when generalizations or analysis must take into account that multiple rows correspond to the same entity.

### [Error](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Error)

Details information about an error encountered during job execution or the results of an unsuccessful activation of the JobTrigger.

### [Error.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Error.Types)

Container for nested types declared in the Error message type.

### [ExcludeByHotword](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ExcludeByHotword)

The rule to exclude findings based on a hotword. For record inspection of tables, column names are considered hotwords. An example of this is to exclude a finding if it belongs to a BigQuery column that matches a specific pattern.

### [ExcludeByImageFindings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ExcludeByImageFindings)

The rule to exclude image findings based on spatial relationships with other image findings. For example, exclude an image finding if it overlaps with another image finding. This rule is silently ignored if the content being inspected is not an image.

### [ExcludeInfoTypes](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ExcludeInfoTypes)

List of excluded infoTypes.

### [ExclusionRule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ExclusionRule)

The rule that specifies conditions when findings of infoTypes specified in `InspectionRuleSet` are removed from results.

### [FieldId](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.FieldId)

General identifier of a data field in a storage service.

### [FieldTransformation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.FieldTransformation)

The transformation to apply to the field.

### [FileClusterSummary](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.FileClusterSummary)

The file cluster summary.

### [FileClusterType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.FileClusterType)

Message used to identify file cluster type being profiled.

### [FileClusterType.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.FileClusterType.Types)

Container for nested types declared in the FileClusterType message type.

### [FileExtensionInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.FileExtensionInfo)

Information regarding the discovered file extension.

### [FileLabel](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.FileLabel)

Represents a file label.

### [FileLabel.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.FileLabel.Types)

Container for nested types declared in the FileLabel message type.

### [FileLabel.Types.GoogleDriveLabelMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.FileLabel.Types.GoogleDriveLabelMetadata)

Google Drive labels published by Google.

### [FileLabel.Types.GoogleDriveLabelMetadata.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.FileLabel.Types.GoogleDriveLabelMetadata.Types)

Container for nested types declared in the GoogleDriveLabelMetadata message type.

### [FileLabel.Types.GoogleDriveLabelMetadata.Types.LabelFieldMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.FileLabel.Types.GoogleDriveLabelMetadata.Types.LabelFieldMetadata)

The field values of the Google Drive label

### [FileLabel.Types.SensitivityLabelMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.FileLabel.Types.SensitivityLabelMetadata)

Sensitivity labels published by Microsoft.

### [FileStoreCollection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.FileStoreCollection)

Match file stores (e.g. buckets) using filters.

### [FileStoreDataProfile](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.FileStoreDataProfile)

The profile for a file store.

  * Cloud Storage: maps 1:1 with a bucket.
  * Amazon S3: maps 1:1 with a bucket.



### [FileStoreDataProfile.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.FileStoreDataProfile.Types)

Container for nested types declared in the FileStoreDataProfile message type.

### [FileStoreDataProfileName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.FileStoreDataProfileName)

Resource name for the `FileStoreDataProfile` resource.

### [FileStoreInfoTypeSummary](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.FileStoreInfoTypeSummary)

Information regarding the discovered InfoType.

### [FileStoreRegex](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.FileStoreRegex)

A pattern to match against one or more file stores.

### [FileStoreRegexes](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.FileStoreRegexes)

A collection of regular expressions to determine what file store to match against.

### [Finding](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Finding)

Represents a piece of potentially sensitive content.

### [FindingName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.FindingName)

Resource name for the `Finding` resource.

### [FinishDlpJobRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.FinishDlpJobRequest)

The request message for finishing a DLP hybrid job.

### [FixedSizeBucketingConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.FixedSizeBucketingConfig)

Buckets values based on fixed size ranges. The Bucketing transformation can provide all of this functionality, but requires more configuration. This message is provided as a convenience to the user for simple bucketing strategies.

The transformed value will be a hyphenated string of {lower_bound}-{upper_bound}. For example, if lower_bound = 10 and upper_bound = 20, all values that are within this bucket will be replaced with "10-20".

This can be used on data of type: double, long.

If the bound Value type differs from the type of data being transformed, we will first attempt converting the type of the data to be transformed to match the type of the bound before comparing.

See <https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-bucketing> to learn more.

### [FullyInside](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.FullyInside)

Defines a condition where one bounding box is fully inside another.

### [GetColumnDataProfileRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.GetColumnDataProfileRequest)

Request to get a column data profile.

### [GetConnectionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.GetConnectionRequest)

Request message for GetConnection.

### [GetContentPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.GetContentPolicyRequest)

Request message for GetContentPolicy.

### [GetDeidentifyTemplateRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.GetDeidentifyTemplateRequest)

Request message for GetDeidentifyTemplate.

### [GetDiscoveryConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.GetDiscoveryConfigRequest)

Request message for GetDiscoveryConfig.

### [GetDlpJobRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.GetDlpJobRequest)

The request message for [GetDlpJob][google.privacy.dlp.v2.DlpService.GetDlpJob].

### [GetFileStoreDataProfileRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.GetFileStoreDataProfileRequest)

Request to get a file store data profile.

### [GetInspectTemplateRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.GetInspectTemplateRequest)

Request message for GetInspectTemplate.

### [GetJobTriggerRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.GetJobTriggerRequest)

Request message for GetJobTrigger.

### [GetProjectDataProfileRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.GetProjectDataProfileRequest)

Request to get a project data profile.

### [GetStoredInfoTypeRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.GetStoredInfoTypeRequest)

Request message for GetStoredInfoType.

### [GetTableDataProfileRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.GetTableDataProfileRequest)

Request to get a table data profile.

### [HybridContentItem](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.HybridContentItem)

An individual hybrid item to inspect. Will be stored temporarily during processing.

### [HybridFindingDetails](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.HybridFindingDetails)

Populate to associate additional data with each finding.

### [HybridInspectDlpJobRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.HybridInspectDlpJobRequest)

Request to search for potentially sensitive info in a custom location.

### [HybridInspectJobTriggerRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.HybridInspectJobTriggerRequest)

Request to search for potentially sensitive info in a custom location.

### [HybridInspectResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.HybridInspectResponse)

Quota exceeded errors will be thrown once quota has been met.

### [HybridInspectStatistics](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.HybridInspectStatistics)

Statistics related to processing hybrid inspect requests.

### [HybridOptions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.HybridOptions)

Configuration to control jobs where the content being inspected is outside of Google Cloud Platform.

### [ImageContainmentType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ImageContainmentType)

Specifies the relationship between bounding boxes for image findings.

### [ImageLocation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ImageLocation)

Location of the finding within an image.

### [ImageTransformations](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ImageTransformations)

A type of transformation that is applied over images.

### [ImageTransformations.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ImageTransformations.Types)

Container for nested types declared in the ImageTransformations message type.

### [ImageTransformations.Types.ImageTransformation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ImageTransformations.Types.ImageTransformation)

Configuration for determining how redaction of images should occur.

### [ImageTransformations.Types.ImageTransformation.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ImageTransformations.Types.ImageTransformation.Types)

Container for nested types declared in the ImageTransformation message type.

### [ImageTransformations.Types.ImageTransformation.Types.AllInfoTypes](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ImageTransformations.Types.ImageTransformation.Types.AllInfoTypes)

Apply transformation to all findings.

### [ImageTransformations.Types.ImageTransformation.Types.AllText](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ImageTransformations.Types.ImageTransformation.Types.AllText)

Apply to all text.

### [ImageTransformations.Types.ImageTransformation.Types.SelectedInfoTypes](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ImageTransformations.Types.ImageTransformation.Types.SelectedInfoTypes)

Apply transformation to the selected info_types.

### [InfoType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InfoType)

Type of information detected by the API.

### [InfoTypeCategory](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InfoTypeCategory)

Classification of infoTypes to organize them according to geographic location, industry, and data type.

### [InfoTypeCategory.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InfoTypeCategory.Types)

Container for nested types declared in the InfoTypeCategory message type.

### [InfoTypeDescription](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InfoTypeDescription)

InfoType description.

### [InfoTypeDescription.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InfoTypeDescription.Types)

Container for nested types declared in the InfoTypeDescription message type.

### [InfoTypeStats](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InfoTypeStats)

Statistics regarding a specific InfoType.

### [InfoTypeSummary](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InfoTypeSummary)

The infoType details for this column.

### [InfoTypeTransformations](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InfoTypeTransformations)

A type of transformation that will scan unstructured text and apply various `PrimitiveTransformation`s to each finding, where the transformation is applied to only values that were identified as a specific info_type.

### [InfoTypeTransformations.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InfoTypeTransformations.Types)

Container for nested types declared in the InfoTypeTransformations message type.

### [InfoTypeTransformations.Types.InfoTypeTransformation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InfoTypeTransformations.Types.InfoTypeTransformation)

A transformation to apply to text that is identified as a specific info_type.

### [InspectConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InspectConfig)

Configuration description of the scanning process. When used with redactContent only info_types and min_likelihood are currently used.

### [InspectConfig.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InspectConfig.Types)

Container for nested types declared in the InspectConfig message type.

### [InspectConfig.Types.FindingLimits](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InspectConfig.Types.FindingLimits)

Configuration to control the number of findings returned for inspection. This is not used for de-identification or data profiling.

When redacting sensitive data from images, finding limits don't apply. They can cause unexpected or inconsistent results, where only some data is redacted. Don't include finding limits in [RedactImage][google.privacy.dlp.v2.DlpService.RedactImage] requests. Otherwise, Cloud DLP returns an error.

### [InspectConfig.Types.FindingLimits.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InspectConfig.Types.FindingLimits.Types)

Container for nested types declared in the FindingLimits message type.

### [InspectConfig.Types.FindingLimits.Types.InfoTypeLimit](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InspectConfig.Types.FindingLimits.Types.InfoTypeLimit)

Max findings configuration per infoType, per content item or long running DlpJob.

### [InspectConfig.Types.InfoTypeLikelihood](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InspectConfig.Types.InfoTypeLikelihood)

Configuration for setting a minimum likelihood per infotype. Used to customize the minimum likelihood level for specific infotypes in the request. For example, use this if you want to lower the precision for PERSON_NAME without lowering the precision for the other infotypes in the request.

### [InspectContentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InspectContentRequest)

Request to search for potentially sensitive info in a ContentItem.

### [InspectContentResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InspectContentResponse)

Results of inspecting an item.

### [InspectDataSourceDetails](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InspectDataSourceDetails)

The results of an inspect DataSource job.

### [InspectDataSourceDetails.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InspectDataSourceDetails.Types)

Container for nested types declared in the InspectDataSourceDetails message type.

### [InspectDataSourceDetails.Types.RequestedOptions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InspectDataSourceDetails.Types.RequestedOptions)

Snapshot of the inspection configuration.

### [InspectDataSourceDetails.Types.Result](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InspectDataSourceDetails.Types.Result)

All Result fields are updated while the job is processing.

### [InspectJobConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InspectJobConfig)

Controls what and how to inspect for findings.

### [InspectResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InspectResult)

All the findings for a single scanned item.

### [InspectTemplate](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InspectTemplate)

The inspectTemplate contains a configuration (set of types of sensitive data to be detected) to be used anywhere you otherwise would normally specify InspectConfig. See <https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-templates> to learn more.

### [InspectTemplateName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InspectTemplateName)

Resource name for the `InspectTemplate` resource.

### [InspectionRule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InspectionRule)

A single inspection rule to be applied to infoTypes, specified in `InspectionRuleSet`.

### [InspectionRuleSet](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InspectionRuleSet)

Rule set for modifying a set of infoTypes to alter behavior under certain circumstances, depending on the specific details of the rules within the set.

### [JobTrigger](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.JobTrigger)

Contains a configuration to make API calls on a repeating basis. See <https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-job-triggers> to learn more.

### [JobTrigger.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.JobTrigger.Types)

Container for nested types declared in the JobTrigger message type.

### [JobTrigger.Types.Trigger](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.JobTrigger.Types.Trigger)

What event needs to occur for a new job to be started.

### [JobTriggerName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.JobTriggerName)

Resource name for the `JobTrigger` resource.

### [Key](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Key)

A unique identifier for a Datastore entity. If a key's partition ID or any of its path kinds or names are reserved/read-only, the key is reserved/read-only. A reserved/read-only key is forbidden in certain documented contexts.

### [Key.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Key.Types)

Container for nested types declared in the Key message type.

### [Key.Types.PathElement](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Key.Types.PathElement)

A (kind, ID/name) pair used to construct a key path.

If either name or ID is set, the element is complete. If neither is set, the element is incomplete.

### [KeyValueMetadataLabel](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.KeyValueMetadataLabel)

The metadata key that contains a finding.

### [KeyValueMetadataProperty](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.KeyValueMetadataProperty)

A key-value pair in the Metadata.

### [KindExpression](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.KindExpression)

A representation of a Datastore kind.

### [KmsWrappedCryptoKey](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.KmsWrappedCryptoKey)

Include to use an existing data crypto key wrapped by KMS. The wrapped key must be a 128-, 192-, or 256-bit key. Authorization requires the following IAM permissions when sending a request to perform a crypto transformation using a KMS-wrapped crypto key: dlp.kms.encrypt

For more information, see [Creating a wrapped key](https://docs.cloud.google.com/sensitive-data-protection/docs/create-wrapped-key).

Note: When you use Cloud KMS for cryptographic operations, [charges apply](https://cloud.google.com/kms/pricing).

### [LargeCustomDictionaryConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.LargeCustomDictionaryConfig)

Configuration for a custom dictionary created from a data source of any size up to the maximum size defined in the [limits](https://docs.cloud.google.com/sensitive-data-protection/limits) page. The artifacts of dictionary creation are stored in the specified Cloud Storage location. Consider using `CustomInfoType.Dictionary` for smaller dictionaries that satisfy the size requirements.

### [LargeCustomDictionaryStats](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.LargeCustomDictionaryStats)

Summary statistics of a custom dictionary.

### [ListColumnDataProfilesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ListColumnDataProfilesRequest)

Request to list the profiles generated for a given organization or project.

### [ListColumnDataProfilesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ListColumnDataProfilesResponse)

List of profiles generated for a given organization or project.

### [ListConnectionsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ListConnectionsRequest)

Request message for ListConnections.

### [ListConnectionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ListConnectionsResponse)

Response message for ListConnections.

### [ListContentPoliciesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ListContentPoliciesRequest)

Request message for ListContentPolicies.

### [ListContentPoliciesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ListContentPoliciesResponse)

Response message for ListContentPolicies.

### [ListDeidentifyTemplatesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ListDeidentifyTemplatesRequest)

Request message for ListDeidentifyTemplates.

### [ListDeidentifyTemplatesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ListDeidentifyTemplatesResponse)

Response message for ListDeidentifyTemplates.

### [ListDiscoveryConfigsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ListDiscoveryConfigsRequest)

Request message for ListDiscoveryConfigs.

### [ListDiscoveryConfigsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ListDiscoveryConfigsResponse)

Response message for ListDiscoveryConfigs.

### [ListDlpJobsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ListDlpJobsRequest)

The request message for listing DLP jobs.

### [ListDlpJobsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ListDlpJobsResponse)

The response message for listing DLP jobs.

### [ListFileStoreDataProfilesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ListFileStoreDataProfilesRequest)

Request to list the file store profiles generated for a given organization or project.

### [ListFileStoreDataProfilesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ListFileStoreDataProfilesResponse)

List of file store data profiles generated for a given organization or project.

### [ListInfoTypesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ListInfoTypesRequest)

Request for the list of infoTypes.

### [ListInfoTypesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ListInfoTypesResponse)

Response to the ListInfoTypes request.

### [ListInspectTemplatesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ListInspectTemplatesRequest)

Request message for ListInspectTemplates.

### [ListInspectTemplatesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ListInspectTemplatesResponse)

Response message for ListInspectTemplates.

### [ListJobTriggersRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ListJobTriggersRequest)

Request message for ListJobTriggers.

### [ListJobTriggersResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ListJobTriggersResponse)

Response message for ListJobTriggers.

### [ListProjectDataProfilesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ListProjectDataProfilesRequest)

Request to list the profiles generated for a given organization or project.

### [ListProjectDataProfilesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ListProjectDataProfilesResponse)

List of profiles generated for a given organization or project.

### [ListStoredInfoTypesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ListStoredInfoTypesRequest)

Request message for ListStoredInfoTypes.

### [ListStoredInfoTypesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ListStoredInfoTypesResponse)

Response message for ListStoredInfoTypes.

### [ListTableDataProfilesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ListTableDataProfilesRequest)

Request to list the profiles generated for a given organization or project.

### [ListTableDataProfilesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ListTableDataProfilesResponse)

List of profiles generated for a given organization or project.

### [Location](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Location)

Specifies the location of the finding.

### [LocationSupport](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.LocationSupport)

Locations at which a feature can be used.

### [LocationSupport.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.LocationSupport.Types)

Container for nested types declared in the LocationSupport message type.

### [Manual](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Manual)

Job trigger option for hybrid jobs. Jobs must be manually created and finished.

### [MetadataLocation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.MetadataLocation)

Metadata Location

### [OrganizationLocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.OrganizationLocationName)

Resource name for the `OrganizationLocation` resource.

### [OtherCloudDiscoveryStartingLocation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.OtherCloudDiscoveryStartingLocation)

The other cloud starting location for discovery.

### [OtherCloudDiscoveryStartingLocation.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.OtherCloudDiscoveryStartingLocation.Types)

Container for nested types declared in the OtherCloudDiscoveryStartingLocation message type.

### [OtherCloudDiscoveryStartingLocation.Types.AwsDiscoveryStartingLocation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.OtherCloudDiscoveryStartingLocation.Types.AwsDiscoveryStartingLocation)

The AWS starting location for discovery.

### [OtherCloudDiscoveryTarget](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.OtherCloudDiscoveryTarget)

Target used to match against for discovery of resources from other clouds. An [AWS connector in Security Command Center (Enterprise](https://docs.cloud.google.com/security-command-center/docs/connect-scc-to-aws) is required to use this feature.

### [OtherCloudResourceCollection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.OtherCloudResourceCollection)

Match resources using regex filters.

### [OtherCloudResourceRegex](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.OtherCloudResourceRegex)

A pattern to match against one or more resources. At least one pattern must be specified. Regular expressions use RE2 [syntax](https://github.com/google/re2/wiki/Syntax); a guide can be found under the google/re2 repository on GitHub.

### [OtherCloudResourceRegexes](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.OtherCloudResourceRegexes)

A collection of regular expressions to determine what resources to match against.

### [OtherCloudSingleResourceReference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.OtherCloudSingleResourceReference)

Identifies a single resource, like a single Amazon S3 bucket.

### [OtherInfoTypeSummary](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.OtherInfoTypeSummary)

Infotype details for other infoTypes found within a column.

### [OutputStorageConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.OutputStorageConfig)

Cloud repository for storing output.

### [OutputStorageConfig.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.OutputStorageConfig.Types)

Container for nested types declared in the OutputStorageConfig message type.

### [Overlap](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Overlap)

Defines a condition for overlapping bounding boxes.

### [PartitionId](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.PartitionId)

Datastore partition ID. A partition ID identifies a grouping of entities. The grouping is always by project and namespace, however the namespace ID may be empty.

A partition ID contains several dimensions: project ID and namespace ID.

### [PrimitiveTransformation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.PrimitiveTransformation)

A rule for transforming a value.

### [PrivacyMetric](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.PrivacyMetric)

Privacy metric to compute for reidentification risk analysis.

### [PrivacyMetric.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.PrivacyMetric.Types)

Container for nested types declared in the PrivacyMetric message type.

### [PrivacyMetric.Types.CategoricalStatsConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.PrivacyMetric.Types.CategoricalStatsConfig)

Compute numerical stats over an individual column, including number of distinct values and value count distribution.

### [PrivacyMetric.Types.DeltaPresenceEstimationConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.PrivacyMetric.Types.DeltaPresenceEstimationConfig)

δ-presence metric, used to estimate how likely it is for an attacker to figure out that one given individual appears in a de-identified dataset. Similarly to the k-map metric, we cannot compute δ-presence exactly without knowing the attack dataset, so we use a statistical model instead.

### [PrivacyMetric.Types.KAnonymityConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.PrivacyMetric.Types.KAnonymityConfig)

k-anonymity metric, used for analysis of reidentification risk.

### [PrivacyMetric.Types.KMapEstimationConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.PrivacyMetric.Types.KMapEstimationConfig)

Reidentifiability metric. This corresponds to a risk model similar to what is called "journalist risk" in the literature, except the attack dataset is statistically modeled instead of being perfectly known. This can be done using publicly available data (like the US Census), or using a custom statistical model (indicated as one or several BigQuery tables), or by extrapolating from the distribution of values in the input dataset.

### [PrivacyMetric.Types.KMapEstimationConfig.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.PrivacyMetric.Types.KMapEstimationConfig.Types)

Container for nested types declared in the KMapEstimationConfig message type.

### [PrivacyMetric.Types.KMapEstimationConfig.Types.AuxiliaryTable](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.PrivacyMetric.Types.KMapEstimationConfig.Types.AuxiliaryTable)

An auxiliary table contains statistical information on the relative frequency of different quasi-identifiers values. It has one or several quasi-identifiers columns, and one column that indicates the relative frequency of each quasi-identifier tuple. If a tuple is present in the data but not in the auxiliary table, the corresponding relative frequency is assumed to be zero (and thus, the tuple is highly reidentifiable).

### [PrivacyMetric.Types.KMapEstimationConfig.Types.AuxiliaryTable.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.PrivacyMetric.Types.KMapEstimationConfig.Types.AuxiliaryTable.Types)

Container for nested types declared in the AuxiliaryTable message type.

### [PrivacyMetric.Types.KMapEstimationConfig.Types.AuxiliaryTable.Types.QuasiIdField](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.PrivacyMetric.Types.KMapEstimationConfig.Types.AuxiliaryTable.Types.QuasiIdField)

A quasi-identifier column has a custom_tag, used to know which column in the data corresponds to which column in the statistical model.

### [PrivacyMetric.Types.KMapEstimationConfig.Types.TaggedField](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.PrivacyMetric.Types.KMapEstimationConfig.Types.TaggedField)

A column with a semantic tag attached.

### [PrivacyMetric.Types.LDiversityConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.PrivacyMetric.Types.LDiversityConfig)

l-diversity metric, used for analysis of reidentification risk.

### [PrivacyMetric.Types.NumericalStatsConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.PrivacyMetric.Types.NumericalStatsConfig)

Compute numerical stats over an individual column, including min, max, and quantiles.

### [ProcessingLocation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ProcessingLocation)

Configure processing location for discovery and inspection. For example, image OCR is only provided in limited regions but configuring ProcessingLocation will redirect OCR to a location where OCR is provided.

### [ProcessingLocation.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ProcessingLocation.Types)

Container for nested types declared in the ProcessingLocation message type.

### [ProcessingLocation.Types.DocumentFallbackLocation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ProcessingLocation.Types.DocumentFallbackLocation)

Configure document processing to fall back to any of the following processing options if document processing is unavailable in the original request location.

### [ProcessingLocation.Types.GlobalProcessing](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ProcessingLocation.Types.GlobalProcessing)

Processing occurs in the global region.

### [ProcessingLocation.Types.ImageFallbackLocation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ProcessingLocation.Types.ImageFallbackLocation)

Configure image processing to fall back to any of the following processing options if image processing is unavailable in the original request location.

### [ProcessingLocation.Types.MultiRegionProcessing](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ProcessingLocation.Types.MultiRegionProcessing)

Processing occurs in a multi-region that contains the current region if available.

### [ProfileStatus](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ProfileStatus)

Success or errors for the profile generation.

### [ProjectDataProfile](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ProjectDataProfile)

An aggregated profile for this project, based on the resources profiled within it.

### [ProjectDataProfileName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ProjectDataProfileName)

Resource name for the `ProjectDataProfile` resource.

### [QuasiId](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.QuasiId)

A column with a semantic tag attached.

### [QuoteInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.QuoteInfo)

Message for infoType-dependent details parsed from quote.

### [Range](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Range)

Generic half-open interval [start, end)

### [RecordCondition](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.RecordCondition)

A condition for determining whether a transformation should be applied to a field.

### [RecordCondition.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.RecordCondition.Types)

Container for nested types declared in the RecordCondition message type.

### [RecordCondition.Types.Condition](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.RecordCondition.Types.Condition)

The field type of `value` and `field` do not need to match to be considered equal, but not all comparisons are possible. EQUAL_TO and NOT_EQUAL_TO attempt to compare even with incompatible types, but all other comparisons are invalid with incompatible types. A `value` of type:

  * `string` can be compared against all other types
  * `boolean` can only be compared against other booleans
  * `integer` can be compared against doubles or a string if the string value can be parsed as an integer.
  * `double` can be compared against integers or a string if the string can be parsed as a double.
  * `Timestamp` can be compared against strings in RFC 3339 date string format.
  * `TimeOfDay` can be compared against timestamps and strings in the format of 'HH:mm:ss'.



If we fail to compare do to type mismatch, a warning will be given and the condition will evaluate to false.

### [RecordCondition.Types.Conditions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.RecordCondition.Types.Conditions)

A collection of conditions.

### [RecordCondition.Types.Expressions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.RecordCondition.Types.Expressions)

An expression, consisting of an operator and conditions.

### [RecordCondition.Types.Expressions.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.RecordCondition.Types.Expressions.Types)

Container for nested types declared in the Expressions message type.

### [RecordKey](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.RecordKey)

Message for a unique key indicating a record that contains a finding.

### [RecordLocation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.RecordLocation)

Location of a finding within a row or record.

### [RecordSuppression](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.RecordSuppression)

Configuration to suppress records whose suppression conditions evaluate to true.

### [RecordTransformation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.RecordTransformation)

The field in a record to transform.

### [RecordTransformations](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.RecordTransformations)

A type of transformation that is applied over structured data such as a table.

### [RedactConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.RedactConfig)

Redact a given value. For example, if used with an `InfoTypeTransformation` transforming PHONE_NUMBER, and input 'My phone number is 206-555-0123', the output would be 'My phone number is '.

### [RedactImageRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.RedactImageRequest)

Request to search for potentially sensitive info in an image and redact it by covering it with a colored rectangle.

### [RedactImageRequest.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.RedactImageRequest.Types)

Container for nested types declared in the RedactImageRequest message type.

### [RedactImageRequest.Types.ImageRedactionConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.RedactImageRequest.Types.ImageRedactionConfig)

Configuration for determining how redaction of images should occur.

### [RedactImageResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.RedactImageResponse)

Results of redacting an image.

### [ReidentifyContentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ReidentifyContentRequest)

Request to re-identify an item.

### [ReidentifyContentResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ReidentifyContentResponse)

Results of re-identifying an item.

### [RelatedResource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.RelatedResource)

A related resource. Examples:

  * The source BigQuery table for a Vertex AI dataset.
  * The source Cloud Storage bucket for a Vertex AI dataset.



### [ReplaceDictionaryConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ReplaceDictionaryConfig)

Replace each input value with a value randomly selected from the dictionary.

### [ReplaceValueConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ReplaceValueConfig)

Replace each input value with a given `Value`.

### [ReplaceWithInfoTypeConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ReplaceWithInfoTypeConfig)

Replace each matching finding with the name of the info_type.

### [RiskAnalysisJobConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.RiskAnalysisJobConfig)

Configuration for a risk analysis job. See <https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-risk-analysis> to learn more.

### [SaveToGcsFindingsOutput](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.SaveToGcsFindingsOutput)

Collection of findings saved to a Cloud Storage bucket. This is used as the proto schema for textproto files created when specifying a cloud storage path to save Inspect findings.

### [Schedule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Schedule)

Schedule for inspect job triggers.

### [SearchConnectionsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.SearchConnectionsRequest)

Request message for SearchConnections.

### [SearchConnectionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.SearchConnectionsResponse)

Response message for SearchConnections.

### [SecretManagerCredential](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.SecretManagerCredential)

A credential consisting of a username and password, where the password is stored in a Secret Manager resource. Note: Secret Manager [charges apply](https://cloud.google.com/secret-manager/pricing).

### [SecretsDiscoveryTarget](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.SecretsDiscoveryTarget)

Discovery target for credentials and secrets in cloud resource metadata.

This target does not include any filtering or frequency controls. Cloud DLP will scan cloud resource metadata for secrets daily.

No inspect template should be included in the discovery config for a security benchmarks scan. Instead, the built-in list of secrets and credentials infoTypes will be used (see <https://docs.cloud.google.com/sensitive-data-protection/docs/infotypes-reference#credentials_and_secrets>).

Credentials and secrets discovered will be reported as vulnerabilities to Security Command Center.

### [SensitivityScore](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.SensitivityScore)

Score is calculated from of all elements in the data profile. A higher level means the data is more sensitive.

### [SensitivityScore.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.SensitivityScore.Types)

Container for nested types declared in the SensitivityScore message type.

### [StatisticalTable](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.StatisticalTable)

An auxiliary table containing statistical information on the relative frequency of different quasi-identifiers values. It has one or several quasi-identifiers columns, and one column that indicates the relative frequency of each quasi-identifier tuple. If a tuple is present in the data but not in the auxiliary table, the corresponding relative frequency is assumed to be zero (and thus, the tuple is highly reidentifiable).

### [StatisticalTable.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.StatisticalTable.Types)

Container for nested types declared in the StatisticalTable message type.

### [StatisticalTable.Types.QuasiIdentifierField](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.StatisticalTable.Types.QuasiIdentifierField)

A quasi-identifier column has a custom_tag, used to know which column in the data corresponds to which column in the statistical model.

### [StorageConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.StorageConfig)

Shared message indicating Cloud storage type.

### [StorageConfig.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.StorageConfig.Types)

Container for nested types declared in the StorageConfig message type.

### [StorageConfig.Types.TimespanConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.StorageConfig.Types.TimespanConfig)

Configuration of the timespan of the items to include in scanning. Currently only supported when inspecting Cloud Storage and BigQuery.

### [StorageMetadataLabel](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.StorageMetadataLabel)

Storage metadata label to indicate which metadata entry contains findings.

### [StoredInfoType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.StoredInfoType)

StoredInfoType resource message that contains information about the current version and any pending updates.

### [StoredInfoTypeConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.StoredInfoTypeConfig)

Configuration for stored infoTypes. All fields and subfield are provided by the user. For more information, see <https://docs.cloud.google.com/sensitive-data-protection/docs/creating-custom-infotypes>.

### [StoredInfoTypeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.StoredInfoTypeName)

Resource name for the `StoredInfoType` resource.

### [StoredInfoTypeStats](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.StoredInfoTypeStats)

Statistics for a StoredInfoType.

### [StoredInfoTypeVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.StoredInfoTypeVersion)

Version of a StoredInfoType, including the configuration used to build it, create timestamp, and current state.

### [StoredType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.StoredType)

A reference to a StoredInfoType to use with scanning.

### [StringValueBatch](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.StringValueBatch)

Represents a batch of string values to inspect or redact.

### [Table](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Table)

Structured content to inspect. Up to 50,000 `Value`s per request allowed. See <https://docs.cloud.google.com/sensitive-data-protection/docs/inspecting-structured-text#inspecting_a_table> to learn more.

### [Table.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Table.Types)

Container for nested types declared in the Table message type.

### [Table.Types.Row](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Table.Types.Row)

Values of the row.

### [TableDataProfile](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.TableDataProfile)

The profile for a scanned table.

### [TableDataProfile.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.TableDataProfile.Types)

Container for nested types declared in the TableDataProfile message type.

### [TableDataProfileName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.TableDataProfileName)

Resource name for the `TableDataProfile` resource.

### [TableLocation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.TableLocation)

Location of a finding within a table.

### [TableOptions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.TableOptions)

Instructions regarding the table content being inspected.

### [TableReference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.TableReference)

Message defining the location of a BigQuery table with the projectId inferred from the parent project.

### [Tag](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Tag)

A tag associated with a resource.

### [TagFilter](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.TagFilter)

A single tag to filter against.

### [TagFilters](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.TagFilters)

Tags to match against for filtering.

### [TimePartConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.TimePartConfig)

For use with `Date`, `Timestamp`, and `TimeOfDay`, extract or preserve a portion of the value.

### [TimePartConfig.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.TimePartConfig.Types)

Container for nested types declared in the TimePartConfig message type.

### [TransformationConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.TransformationConfig)

User specified templates and configs for how to deidentify structured, unstructures, and image files. User must provide either a unstructured deidentify template or at least one redact image config.

### [TransformationDescription](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.TransformationDescription)

A flattened description of a `PrimitiveTransformation` or `RecordSuppression`.

### [TransformationDetails](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.TransformationDetails)

Details about a single transformation. This object contains a description of the transformation, information about whether the transformation was successfully applied, and the precise location where the transformation occurred. These details are stored in a user-specified BigQuery table.

### [TransformationDetailsStorageConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.TransformationDetailsStorageConfig)

Config for storing transformation details.

### [TransformationErrorHandling](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.TransformationErrorHandling)

How to handle transformation errors during de-identification. A transformation error occurs when the requested transformation is incompatible with the data. For example, trying to de-identify an IP address using a `DateShift` transformation would result in a transformation error, since date info cannot be extracted from an IP address. Information about any incompatible transformations, and how they were handled, is returned in the response as part of the `TransformationOverviews`.

### [TransformationErrorHandling.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.TransformationErrorHandling.Types)

Container for nested types declared in the TransformationErrorHandling message type.

### [TransformationErrorHandling.Types.LeaveUntransformed](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.TransformationErrorHandling.Types.LeaveUntransformed)

Skips the data without modifying it if the requested transformation would cause an error. For example, if a `DateShift` transformation were applied an an IP address, this mode would leave the IP address unchanged in the response.

### [TransformationErrorHandling.Types.ThrowError](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.TransformationErrorHandling.Types.ThrowError)

Throw an error and fail the request when a transformation error occurs.

### [TransformationLocation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.TransformationLocation)

Specifies the location of a transformation.

### [TransformationOverview](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.TransformationOverview)

Overview of the modifications that occurred.

### [TransformationResultStatus](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.TransformationResultStatus)

The outcome of a transformation.

### [TransformationSummary](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.TransformationSummary)

Summary of a single transformation. Only one of 'transformation', 'field_transformation', or 'record_suppress' will be set.

### [TransformationSummary.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.TransformationSummary.Types)

Container for nested types declared in the TransformationSummary message type.

### [TransformationSummary.Types.SummaryResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.TransformationSummary.Types.SummaryResult)

A collection that informs the user the number of times a particular `TransformationResultCode` and error details occurred.

### [TransientCryptoKey](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.TransientCryptoKey)

Use this to have a random data crypto key generated. It will be discarded after the request finishes.

### [UnwrappedCryptoKey](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.UnwrappedCryptoKey)

Using raw keys is prone to security risks due to accidentally leaking the key. Choose another type of key if possible.

### [UpdateConnectionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.UpdateConnectionRequest)

Request message for UpdateConnection.

### [UpdateContentPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.UpdateContentPolicyRequest)

Request message for UpdateContentPolicy.

### [UpdateDeidentifyTemplateRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.UpdateDeidentifyTemplateRequest)

Request message for UpdateDeidentifyTemplate.

### [UpdateDiscoveryConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.UpdateDiscoveryConfigRequest)

Request message for UpdateDiscoveryConfig.

### [UpdateInspectTemplateRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.UpdateInspectTemplateRequest)

Request message for UpdateInspectTemplate.

### [UpdateJobTriggerRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.UpdateJobTriggerRequest)

Request message for UpdateJobTrigger.

### [UpdateStoredInfoTypeRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.UpdateStoredInfoTypeRequest)

Request message for UpdateStoredInfoType.

### [Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Value)

Set of primitive values supported by the system. Note that for the purposes of inspection or transformation, the number of bytes considered to comprise a 'Value' is based on its representation as a UTF-8 encoded string. For example, if 'integer_value' is set to 123456789, the number of bytes would be counted as 9, even though an int64 only holds up to 8 bytes of data.

### [ValueFrequency](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ValueFrequency)

A value of a field, including its frequency.

### [VersionDescription](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.VersionDescription)

Details about each available version for an infotype.

### [VertexDatasetCollection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.VertexDatasetCollection)

Match dataset resources using regex filters.

### [VertexDatasetDiscoveryTarget](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.VertexDatasetDiscoveryTarget)

Target used to match against for discovery with Vertex AI datasets.

### [VertexDatasetRegex](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.VertexDatasetRegex)

A pattern to match against one or more dataset resources.

### [VertexDatasetRegexes](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.VertexDatasetRegexes)

A collection of regular expressions to determine what datasets to match against.

### [VertexDatasetResourceReference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.VertexDatasetResourceReference)

Identifies a single Vertex AI resource. Only datasets are supported.

## Enums 

### [Action.ActionOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Action.ActionOneofCase)

Enum of possible cases for the "action" oneof.

### [Action.Types.Deidentify.OutputOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Action.Types.Deidentify.OutputOneofCase)

Enum of possible cases for the "output" oneof.

### [ActionDetails.DetailsOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ActionDetails.DetailsOneofCase)

Enum of possible cases for the "details" oneof.

### [AdjustmentRule.ConditionsOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.AdjustmentRule.ConditionsOneofCase)

Enum of possible cases for the "conditions" oneof.

### [AmazonS3BucketConditions.Types.BucketType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.AmazonS3BucketConditions.Types.BucketType)

Supported Amazon S3 bucket types. Defaults to TYPE_ALL_SUPPORTED.

### [AmazonS3BucketConditions.Types.ObjectStorageClass](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.AmazonS3BucketConditions.Types.ObjectStorageClass)

Supported Amazon S3 object storage classes. Defaults to ALL_SUPPORTED_CLASSES.

### [AnalyzeDataSourceRiskDetails.ResultOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.AnalyzeDataSourceRiskDetails.ResultOneofCase)

Enum of possible cases for the "result" oneof.

### [BatchContentItem.BatchOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.BatchContentItem.BatchOneofCase)

Enum of possible cases for the "batch" oneof.

### [BigQueryDiscoveryTarget.FrequencyOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.BigQueryDiscoveryTarget.FrequencyOneofCase)

Enum of possible cases for the "frequency" oneof.

### [BigQueryOptions.Types.SampleMethod](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.BigQueryOptions.Types.SampleMethod)

How to sample rows if not all rows are scanned. Meaningful only when used in conjunction with either rows_limit or rows_limit_percent. If not specified, rows are scanned in the order BigQuery reads them.

### [BigQuerySchemaModification](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.BigQuerySchemaModification)

Attributes evaluated to determine if a schema has been modified. New values may be added at a later time.

### [BigQueryTableCollection.PatternOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.BigQueryTableCollection.PatternOneofCase)

Enum of possible cases for the "pattern" oneof.

### [BigQueryTableModification](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.BigQueryTableModification)

Attributes evaluated to determine if a table has been modified. New values may be added at a later time.

### [BigQueryTableType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.BigQueryTableType)

Over time new types may be added. Currently VIEW, MATERIALIZED_VIEW, and non-BigLake external tables are not supported.

### [BigQueryTableTypeCollection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.BigQueryTableTypeCollection)

Over time new types may be added. Currently VIEW, MATERIALIZED_VIEW, and non-BigLake external tables are not supported.

### [ByteContentItem.Types.BytesType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ByteContentItem.Types.BytesType)

The type of data being sent for inspection. To learn more, see [Supported file types](https://docs.cloud.google.com/sensitive-data-protection/docs/supported-file-types).

Only the first frame of each multiframe image is inspected. Metadata and other frames aren't inspected.

### [CharsToIgnore.CharactersOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.CharsToIgnore.CharactersOneofCase)

Enum of possible cases for the "characters" oneof.

### [CharsToIgnore.Types.CommonCharsToIgnore](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.CharsToIgnore.Types.CommonCharsToIgnore)

Convenience enum for indicating common characters to not transform.

### [CloudSqlDiscoveryTarget.CadenceOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.CloudSqlDiscoveryTarget.CadenceOneofCase)

Enum of possible cases for the "cadence" oneof.

### [CloudSqlProperties.CredentialOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.CloudSqlProperties.CredentialOneofCase)

Enum of possible cases for the "credential" oneof.

### [CloudSqlProperties.Types.DatabaseEngine](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.CloudSqlProperties.Types.DatabaseEngine)

Database engine of a Cloud SQL instance. New values may be added over time.

### [CloudStorageDiscoveryTarget.CadenceOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.CloudStorageDiscoveryTarget.CadenceOneofCase)

Enum of possible cases for the "cadence" oneof.

### [CloudStorageOptions.Types.SampleMethod](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.CloudStorageOptions.Types.SampleMethod)

How to sample bytes if not all bytes are scanned. Meaningful only when used in conjunction with bytes_limit_per_file. If not specified, scanning would start from the top.

### [ColumnDataProfile.Types.ColumnDataType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ColumnDataProfile.Types.ColumnDataType)

Data types of the data in a column. Types may be added over time.

### [ColumnDataProfile.Types.ColumnPolicyState](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ColumnDataProfile.Types.ColumnPolicyState)

The possible policy states for a column.

### [ColumnDataProfile.Types.State](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ColumnDataProfile.Types.State)

Possible states of a profile. New items may be added.

### [ColumnDataProfileName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ColumnDataProfileName.ResourceNameType)

The possible contents of [ColumnDataProfileName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ColumnDataProfileName).

### [Connection.PropertiesOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Connection.PropertiesOneofCase)

Enum of possible cases for the "properties" oneof.

### [ConnectionName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ConnectionName.ResourceNameType)

The possible contents of [ConnectionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ConnectionName).

### [ConnectionState](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ConnectionState)

State of the connection. New values may be added over time.

### [ContentItem.DataItemOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ContentItem.DataItemOneofCase)

Enum of possible cases for the "data_item" oneof.

### [ContentLocation.LocationOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ContentLocation.LocationOneofCase)

Enum of possible cases for the "location" oneof.

### [ContentOption](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ContentOption)

Deprecated and unused.

### [ContentPolicy.Types.LoggingConfig.DestinationOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ContentPolicy.Types.LoggingConfig.DestinationOneofCase)

Enum of possible cases for the "destination" oneof.

### [ContentPolicy.Types.PolicyAction.ActionOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ContentPolicy.Types.PolicyAction.ActionOneofCase)

Enum of possible cases for the "action" oneof.

### [ContentPolicy.Types.PolicyRule.Types.PolicyCondition.ConditionOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ContentPolicy.Types.PolicyRule.Types.PolicyCondition.ConditionOneofCase)

Enum of possible cases for the "condition" oneof.

### [ContentPolicy.Types.PolicyRule.Types.PolicyCondition.Types.InfoTypeCondition.InfoTypeConditionOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ContentPolicy.Types.PolicyRule.Types.PolicyCondition.Types.InfoTypeCondition.InfoTypeConditionOneofCase)

Enum of possible cases for the "info_type_condition" oneof.

### [ContentPolicyName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ContentPolicyName.ResourceNameType)

The possible contents of [ContentPolicyName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ContentPolicyName).

### [ContentPolicyVerdict](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ContentPolicyVerdict)

Possible results of applying a content policy. This may expand to include additional result types in the future.

### [ConversationLocation.LocationOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ConversationLocation.LocationOneofCase)

Enum of possible cases for the "location" oneof.

### [ConversationMessage.Types.MessageType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ConversationMessage.Types.MessageType)

The type of message. New values may be added in the future.

### [CreateDlpJobRequest.JobOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.CreateDlpJobRequest.JobOneofCase)

Enum of possible cases for the "job" oneof.

### [CryptoKey.SourceOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.CryptoKey.SourceOneofCase)

Enum of possible cases for the "source" oneof.

### [CryptoReplaceFfxFpeConfig.AlphabetOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.CryptoReplaceFfxFpeConfig.AlphabetOneofCase)

Enum of possible cases for the "alphabet" oneof.

### [CryptoReplaceFfxFpeConfig.Types.FfxCommonNativeAlphabet](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.CryptoReplaceFfxFpeConfig.Types.FfxCommonNativeAlphabet)

These are commonly used subsets of the alphabet that the FFX mode natively supports. In the algorithm, the alphabet is selected using the "radix". Therefore each corresponds to a particular radix.

### [CustomInfoType.TypeOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.CustomInfoType.TypeOneofCase)

Enum of possible cases for the "type" oneof.

### [CustomInfoType.Types.DetectionRule.TypeOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.CustomInfoType.Types.DetectionRule.TypeOneofCase)

Enum of possible cases for the "type" oneof.

### [CustomInfoType.Types.DetectionRule.Types.LikelihoodAdjustment.AdjustmentOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.CustomInfoType.Types.DetectionRule.Types.LikelihoodAdjustment.AdjustmentOneofCase)

Enum of possible cases for the "adjustment" oneof.

### [CustomInfoType.Types.Dictionary.SourceOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.CustomInfoType.Types.Dictionary.SourceOneofCase)

Enum of possible cases for the "source" oneof.

### [CustomInfoType.Types.ExclusionType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.CustomInfoType.Types.ExclusionType)

Type of exclusion rule.

### [CustomInfoType.Types.FileLabelInfoType.TypeOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.CustomInfoType.Types.FileLabelInfoType.TypeOneofCase)

Enum of possible cases for the "type" oneof.

### [DataProfileAction.ActionOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DataProfileAction.ActionOneofCase)

Enum of possible cases for the "action" oneof.

### [DataProfileAction.Types.EventType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DataProfileAction.Types.EventType)

Types of event that can trigger an action.

### [DataProfileAction.Types.PubSubNotification.Types.DetailLevel](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DataProfileAction.Types.PubSubNotification.Types.DetailLevel)

The levels of detail that can be included in the Pub/Sub message.

### [DataProfileAction.Types.TagResources.Types.TagCondition.TypeOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DataProfileAction.Types.TagResources.Types.TagCondition.TypeOneofCase)

Enum of possible cases for the "type" oneof.

### [DataProfileAction.Types.TagResources.Types.TagValue.FormatOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DataProfileAction.Types.TagResources.Types.TagValue.FormatOneofCase)

Enum of possible cases for the "format" oneof.

### [DataProfileBigQueryRowSchema.DataProfileOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DataProfileBigQueryRowSchema.DataProfileOneofCase)

Enum of possible cases for the "data_profile" oneof.

### [DataProfileFindingLocation.LocationExtraDetailsOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DataProfileFindingLocation.LocationExtraDetailsOneofCase)

Enum of possible cases for the "location_extra_details" oneof.

### [DataProfileLocation.LocationOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DataProfileLocation.LocationOneofCase)

Enum of possible cases for the "location" oneof.

### [DataProfilePubSubCondition.Types.ProfileScoreBucket](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DataProfilePubSubCondition.Types.ProfileScoreBucket)

Various score levels for resources.

### [DataProfilePubSubCondition.Types.PubSubCondition.ValueOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DataProfilePubSubCondition.Types.PubSubCondition.ValueOneofCase)

Enum of possible cases for the "value" oneof.

### [DataProfilePubSubCondition.Types.PubSubExpressions.Types.PubSubLogicalOperator](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DataProfilePubSubCondition.Types.PubSubExpressions.Types.PubSubLogicalOperator)

Logical operators for conditional checks.

### [DataProfileUpdateFrequency](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DataProfileUpdateFrequency)

How frequently data profiles can be updated. New options can be added at a later time.

### [DataRiskLevel.Types.DataRiskLevelScore](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DataRiskLevel.Types.DataRiskLevelScore)

Various score levels for resources.

### [DatabaseResourceCollection.PatternOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DatabaseResourceCollection.PatternOneofCase)

Enum of possible cases for the "pattern" oneof.

### [DateShiftConfig.MethodOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DateShiftConfig.MethodOneofCase)

Enum of possible cases for the "method" oneof.

### [DeidentifyConfig.TransformationOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DeidentifyConfig.TransformationOneofCase)

Enum of possible cases for the "transformation" oneof.

### [DeidentifyTemplateName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DeidentifyTemplateName.ResourceNameType)

The possible contents of [DeidentifyTemplateName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DeidentifyTemplateName).

### [DiscoveryBigQueryConditions.IncludedTypesOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DiscoveryBigQueryConditions.IncludedTypesOneofCase)

Enum of possible cases for the "included_types" oneof.

### [DiscoveryBigQueryFilter.FilterOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DiscoveryBigQueryFilter.FilterOneofCase)

Enum of possible cases for the "filter" oneof.

### [DiscoveryCloudSqlConditions.Types.DatabaseEngine](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DiscoveryCloudSqlConditions.Types.DatabaseEngine)

The database engines that should be profiled.

### [DiscoveryCloudSqlConditions.Types.DatabaseResourceType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DiscoveryCloudSqlConditions.Types.DatabaseResourceType)

Cloud SQL database resource types. New values can be added at a later time.

### [DiscoveryCloudSqlFilter.FilterOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DiscoveryCloudSqlFilter.FilterOneofCase)

Enum of possible cases for the "filter" oneof.

### [DiscoveryCloudSqlGenerationCadence.Types.SchemaModifiedCadence.Types.CloudSqlSchemaModification](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DiscoveryCloudSqlGenerationCadence.Types.SchemaModifiedCadence.Types.CloudSqlSchemaModification)

The type of modification that causes a profile update.

### [DiscoveryCloudStorageConditions.Types.CloudStorageBucketAttribute](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DiscoveryCloudStorageConditions.Types.CloudStorageBucketAttribute)

The attribute of a bucket.

### [DiscoveryCloudStorageConditions.Types.CloudStorageObjectAttribute](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DiscoveryCloudStorageConditions.Types.CloudStorageObjectAttribute)

The attribute of an object. See <https://docs.cloud.google.com/storage/docs/storage-classes> for more information on storage classes.

### [DiscoveryCloudStorageFilter.FilterOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DiscoveryCloudStorageFilter.FilterOneofCase)

Enum of possible cases for the "filter" oneof.

### [DiscoveryConfig.Types.Status](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DiscoveryConfig.Types.Status)

Whether the discovery config is currently active. New options may be added at a later time.

### [DiscoveryConfigName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DiscoveryConfigName.ResourceNameType)

The possible contents of [DiscoveryConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DiscoveryConfigName).

### [DiscoveryFileStoreConditions.ConditionsOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DiscoveryFileStoreConditions.ConditionsOneofCase)

Enum of possible cases for the "conditions" oneof.

### [DiscoveryOtherCloudConditions.ConditionsOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DiscoveryOtherCloudConditions.ConditionsOneofCase)

Enum of possible cases for the "conditions" oneof.

### [DiscoveryOtherCloudFilter.FilterOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DiscoveryOtherCloudFilter.FilterOneofCase)

Enum of possible cases for the "filter" oneof.

### [DiscoveryStartingLocation.LocationOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DiscoveryStartingLocation.LocationOneofCase)

Enum of possible cases for the "location" oneof.

### [DiscoveryTarget.TargetOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DiscoveryTarget.TargetOneofCase)

Enum of possible cases for the "target" oneof.

### [DiscoveryVertexDatasetFilter.FilterOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DiscoveryVertexDatasetFilter.FilterOneofCase)

Enum of possible cases for the "filter" oneof.

### [DlpContentName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpContentName.ResourceNameType)

The possible contents of [DlpContentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpContentName).

### [DlpJob.DetailsOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpJob.DetailsOneofCase)

Enum of possible cases for the "details" oneof.

### [DlpJob.Types.JobState](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpJob.Types.JobState)

Possible states of a job. New items may be added.

### [DlpJobName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpJobName.ResourceNameType)

The possible contents of [DlpJobName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpJobName).

### [DlpJobType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpJobType)

An enum to represent the various types of DLP jobs.

### [Domain.Types.Category](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Domain.Types.Category)

This enum defines the various domain categories a data profile can fall under.

### [Domain.Types.Signal](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Domain.Types.Signal)

The signal used to determine the category. New values may be added in the future.

### [EncryptionStatus](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.EncryptionStatus)

How a resource is encrypted.

### [Error.Types.ErrorExtraInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Error.Types.ErrorExtraInfo)

Additional information about the error.

### [ExclusionRule.TypeOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ExclusionRule.TypeOneofCase)

Enum of possible cases for the "type" oneof.

### [FieldTransformation.TransformationOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.FieldTransformation.TransformationOneofCase)

Enum of possible cases for the "transformation" oneof.

### [FileClusterType.FileClusterTypeOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.FileClusterType.FileClusterTypeOneofCase)

Enum of possible cases for the "file_cluster_type" oneof.

### [FileClusterType.Types.Cluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.FileClusterType.Types.Cluster)

Cluster type. Each cluster corresponds to a set of file types. Over time, new types may be added and files may move between clusters.

### [FileLabel.TypeOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.FileLabel.TypeOneofCase)

Enum of possible cases for the "type" oneof.

### [FileStoreCollection.PatternOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.FileStoreCollection.PatternOneofCase)

Enum of possible cases for the "pattern" oneof.

### [FileStoreDataProfile.Types.State](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.FileStoreDataProfile.Types.State)

Possible states of a profile. New items may be added.

### [FileStoreDataProfileName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.FileStoreDataProfileName.ResourceNameType)

The possible contents of [FileStoreDataProfileName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.FileStoreDataProfileName).

### [FileStoreRegex.ResourceRegexOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.FileStoreRegex.ResourceRegexOneofCase)

Enum of possible cases for the "resource_regex" oneof.

### [FileType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.FileType)

Definitions of file type groups to scan. New types will be added to this list.

### [FindingName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.FindingName.ResourceNameType)

The possible contents of [FindingName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.FindingName).

### [ImageContainmentType.TypeOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ImageContainmentType.TypeOneofCase)

Enum of possible cases for the "type" oneof.

### [ImageTransformations.Types.ImageTransformation.TargetOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ImageTransformations.Types.ImageTransformation.TargetOneofCase)

Enum of possible cases for the "target" oneof.

### [InfoTypeCategory.CategoryOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InfoTypeCategory.CategoryOneofCase)

Enum of possible cases for the "category" oneof.

### [InfoTypeCategory.Types.IndustryCategory](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InfoTypeCategory.Types.IndustryCategory)

Enum of the current industries in the category. We might add more industries in the future.

### [InfoTypeCategory.Types.LocationCategory](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InfoTypeCategory.Types.LocationCategory)

Enum of the current locations. We might add more locations in the future.

### [InfoTypeCategory.Types.TypeCategory](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InfoTypeCategory.Types.TypeCategory)

Enum of the current types in the category. We might add more types in the future.

### [InfoTypeDescription.Types.InfoTypeLaunchStatus](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InfoTypeDescription.Types.InfoTypeLaunchStatus)

The launch status of an infoType.

### [InfoTypeSupportedBy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InfoTypeSupportedBy)

Parts of the APIs which use certain infoTypes.

### [InspectTemplateName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InspectTemplateName.ResourceNameType)

The possible contents of [InspectTemplateName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InspectTemplateName).

### [InspectionRule.TypeOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InspectionRule.TypeOneofCase)

Enum of possible cases for the "type" oneof.

### [JobTrigger.JobOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.JobTrigger.JobOneofCase)

Enum of possible cases for the "job" oneof.

### [JobTrigger.Types.Status](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.JobTrigger.Types.Status)

Whether the trigger is currently active. If PAUSED or CANCELLED, no jobs will be created with this configuration. The service may automatically pause triggers experiencing frequent errors. To restart a job, set the status to HEALTHY after correcting user errors.

### [JobTrigger.Types.Trigger.TriggerOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.JobTrigger.Types.Trigger.TriggerOneofCase)

Enum of possible cases for the "trigger" oneof.

### [JobTriggerName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.JobTriggerName.ResourceNameType)

The possible contents of [JobTriggerName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.JobTriggerName).

### [Key.Types.PathElement.IdTypeOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Key.Types.PathElement.IdTypeOneofCase)

Enum of possible cases for the "id_type" oneof.

### [LargeCustomDictionaryConfig.SourceOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.LargeCustomDictionaryConfig.SourceOneofCase)

Enum of possible cases for the "source" oneof.

### [Likelihood](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Likelihood)

Coarse-grained confidence level of how well a particular finding satisfies the criteria to match a particular infoType.

Likelihood is calculated based on the number of signals a finding has that implies that the finding matches the infoType. For example, a string that has an '@' and a '.com' is more likely to be a match for an email address than a string that only has an '@'.

In general, the highest likelihood level has the strongest signals that indicate a match. That is, a finding with a high likelihood has a low chance of being a false positive.

For more information about each likelihood level and how likelihood works, see [Match likelihood](https://docs.cloud.google.com/sensitive-data-protection/docs/likelihood).

### [LocationSupport.Types.RegionalizationScope](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.LocationSupport.Types.RegionalizationScope)

The location scope for a feature.

### [MatchingType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.MatchingType)

Type of the match which can be applied to different ways of matching, like Dictionary, regular expression and intersecting with findings of another infoType.

### [MetadataLocation.LabelOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.MetadataLocation.LabelOneofCase)

Enum of possible cases for the "label" oneof.

### [MetadataType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.MetadataType)

Type of metadata containing the finding.

### [NullPercentageLevel](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.NullPercentageLevel)

Bucketized nullness percentage levels. A higher level means a higher percentage of the column is null.

### [OrganizationLocationName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.OrganizationLocationName.ResourceNameType)

The possible contents of [OrganizationLocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.OrganizationLocationName).

### [OtherCloudDiscoveryStartingLocation.LocationOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.OtherCloudDiscoveryStartingLocation.LocationOneofCase)

Enum of possible cases for the "location" oneof.

### [OtherCloudDiscoveryStartingLocation.Types.AwsDiscoveryStartingLocation.ScopeOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.OtherCloudDiscoveryStartingLocation.Types.AwsDiscoveryStartingLocation.ScopeOneofCase)

Enum of possible cases for the "scope" oneof.

### [OtherCloudDiscoveryTarget.CadenceOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.OtherCloudDiscoveryTarget.CadenceOneofCase)

Enum of possible cases for the "cadence" oneof.

### [OtherCloudResourceCollection.PatternOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.OtherCloudResourceCollection.PatternOneofCase)

Enum of possible cases for the "pattern" oneof.

### [OtherCloudResourceRegex.ResourceRegexOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.OtherCloudResourceRegex.ResourceRegexOneofCase)

Enum of possible cases for the "resource_regex" oneof.

### [OtherCloudSingleResourceReference.ResourceOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.OtherCloudSingleResourceReference.ResourceOneofCase)

Enum of possible cases for the "resource" oneof.

### [OutputStorageConfig.TypeOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.OutputStorageConfig.TypeOneofCase)

Enum of possible cases for the "type" oneof.

### [OutputStorageConfig.Types.OutputSchema](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.OutputStorageConfig.Types.OutputSchema)

Predefined schemas for storing findings. Only for use with external storage.

### [PrimitiveTransformation.TransformationOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.PrimitiveTransformation.TransformationOneofCase)

Enum of possible cases for the "transformation" oneof.

### [PrivacyMetric.TypeOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.PrivacyMetric.TypeOneofCase)

Enum of possible cases for the "type" oneof.

### [PrivacyMetric.Types.KMapEstimationConfig.Types.TaggedField.TagOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.PrivacyMetric.Types.KMapEstimationConfig.Types.TaggedField.TagOneofCase)

Enum of possible cases for the "tag" oneof.

### [ProfileGeneration](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ProfileGeneration)

Whether a profile being created is the first generation or an update.

### [ProjectDataProfileName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ProjectDataProfileName.ResourceNameType)

The possible contents of [ProjectDataProfileName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ProjectDataProfileName).

### [QuasiId.TagOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.QuasiId.TagOneofCase)

Enum of possible cases for the "tag" oneof.

### [QuoteInfo.ParsedQuoteOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.QuoteInfo.ParsedQuoteOneofCase)

Enum of possible cases for the "parsed_quote" oneof.

### [RecordCondition.Types.Expressions.TypeOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.RecordCondition.Types.Expressions.TypeOneofCase)

Enum of possible cases for the "type" oneof.

### [RecordCondition.Types.Expressions.Types.LogicalOperator](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.RecordCondition.Types.Expressions.Types.LogicalOperator)

Logical operators for conditional checks.

### [RecordKey.TypeOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.RecordKey.TypeOneofCase)

Enum of possible cases for the "type" oneof.

### [RedactImageRequest.Types.ImageRedactionConfig.TargetOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.RedactImageRequest.Types.ImageRedactionConfig.TargetOneofCase)

Enum of possible cases for the "target" oneof.

### [RelationalOperator](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.RelationalOperator)

Operators available for comparing the value of fields.

### [ReplaceDictionaryConfig.TypeOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ReplaceDictionaryConfig.TypeOneofCase)

Enum of possible cases for the "type" oneof.

### [ResourceVisibility](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ResourceVisibility)

How broadly the data in the resource has been shared. New items may be added over time. A higher number means more restricted.

### [Schedule.OptionOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Schedule.OptionOneofCase)

Enum of possible cases for the "option" oneof.

### [SensitivityScore.Types.SensitivityScoreLevel](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.SensitivityScore.Types.SensitivityScoreLevel)

Various sensitivity score levels for resources.

### [StorageConfig.TypeOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.StorageConfig.TypeOneofCase)

Enum of possible cases for the "type" oneof.

### [StoredInfoTypeConfig.TypeOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.StoredInfoTypeConfig.TypeOneofCase)

Enum of possible cases for the "type" oneof.

### [StoredInfoTypeName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.StoredInfoTypeName.ResourceNameType)

The possible contents of [StoredInfoTypeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.StoredInfoTypeName).

### [StoredInfoTypeState](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.StoredInfoTypeState)

State of a StoredInfoType version.

### [StoredInfoTypeStats.TypeOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.StoredInfoTypeStats.TypeOneofCase)

Enum of possible cases for the "type" oneof.

### [TableDataProfile.Types.State](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.TableDataProfile.Types.State)

Possible states of a profile. New items may be added.

### [TableDataProfileName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.TableDataProfileName.ResourceNameType)

The possible contents of [TableDataProfileName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.TableDataProfileName).

### [TagFilter.FormatOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.TagFilter.FormatOneofCase)

Enum of possible cases for the "format" oneof.

### [TimePartConfig.Types.TimePart](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.TimePartConfig.Types.TimePart)

Components that make up time.

### [TransformationContainerType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.TransformationContainerType)

Describes functionality of a given container in its original format.

### [TransformationDetailsStorageConfig.TypeOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.TransformationDetailsStorageConfig.TypeOneofCase)

Enum of possible cases for the "type" oneof.

### [TransformationErrorHandling.ModeOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.TransformationErrorHandling.ModeOneofCase)

Enum of possible cases for the "mode" oneof.

### [TransformationLocation.LocationTypeOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.TransformationLocation.LocationTypeOneofCase)

Enum of possible cases for the "location_type" oneof.

### [TransformationResultStatusType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.TransformationResultStatusType)

Enum of possible outcomes of transformations. SUCCESS if transformation and storing of transformation was successful, otherwise, reason for not transforming.

### [TransformationSummary.Types.TransformationResultCode](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.TransformationSummary.Types.TransformationResultCode)

Possible outcomes of transformations.

### [TransformationType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.TransformationType)

An enum of rules that can be used to transform a value. Can be a record suppression, or one of the transformation rules specified under `PrimitiveTransformation`.

### [UniquenessScoreLevel](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.UniquenessScoreLevel)

Bucketized uniqueness score levels. A higher uniqueness score is a strong signal that the column may contain a unique identifier like user id. A low value indicates that the column contains few unique values like booleans or other classifiers.

### [Value.TypeOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Value.TypeOneofCase)

Enum of possible cases for the "type" oneof.

### [VertexDatasetCollection.PatternOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.VertexDatasetCollection.PatternOneofCase)

Enum of possible cases for the "pattern" oneof.

### [VertexDatasetDiscoveryTarget.CadenceOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.VertexDatasetDiscoveryTarget.CadenceOneofCase)

Enum of possible cases for the "cadence" oneof.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-01 UTC."],[],[]] 
