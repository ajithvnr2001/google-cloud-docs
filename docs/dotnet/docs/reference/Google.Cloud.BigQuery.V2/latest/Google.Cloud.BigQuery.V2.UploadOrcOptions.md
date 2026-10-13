---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.UploadOrcOptions
title: Google BigQuery v2 API - Class UploadOrcOptions (3.12.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:18:53.586043+00:00
---

# Google BigQuery v2 API - Class UploadOrcOptions (3.12.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.UploadOrcOptions

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google BigQuery v2 API - Class UploadOrcOptions (3.12.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.12.0 (latest)  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.4.0  2.3.0  2.2.0 
    
    
    public sealed class UploadOrcOptions : JobCreationOptions

Reference documentation and code samples for the Google BigQuery v2 API class UploadOrcOptions.

Options for `UploadOrc` operations.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > [JobCreationOptions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.JobCreationOptions) > UploadOrcOptions

## Inherited Members

[JobCreationOptions.ProjectId](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.JobCreationOptions#Google_Cloud_BigQuery_V2_JobCreationOptions_ProjectId)

[JobCreationOptions.JobIdPrefix](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.JobCreationOptions#Google_Cloud_BigQuery_V2_JobCreationOptions_JobIdPrefix)

[JobCreationOptions.JobId](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.JobCreationOptions#Google_Cloud_BigQuery_V2_JobCreationOptions_JobId)

[JobCreationOptions.JobLocation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.JobCreationOptions#Google_Cloud_BigQuery_V2_JobCreationOptions_JobLocation)

[JobCreationOptions.Labels](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.JobCreationOptions#Google_Cloud_BigQuery_V2_JobCreationOptions_Labels)

[JobCreationOptions.JobConfigurationModifier](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.JobCreationOptions#Google_Cloud_BigQuery_V2_JobCreationOptions_JobConfigurationModifier)

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.BigQuery.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2)

## Assembly

Google.Cloud.BigQuery.V2.dll

## Properties 

### AllowUnknownFields
    
    
    public bool? AllowUnknownFields { get; set; }

Whether or not to accept rows with fields that are not specified in the schema, ignoring the extra fields. If not set, this is effectively false.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### ConfigurationModifier
    
    
    public Action<JobConfigurationLoad> ConfigurationModifier { get; set; }

Optional action to perform after preparing the request. If this property is non-null, the [JobConfigurationLoad](https://googleapis.dev/dotnet/Google.Apis.Bigquery.v2/1.74.0.4090/api/Google.Apis.Bigquery.v2.Data.JobConfigurationLoad.html) used for a request will be passed to the delegate before the request is executed. This allows for fine-grained modifications which aren't otherwise directly supported by the properties in this options type.

**Property Value**  
---  
**Type** | **Description**  
`[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[JobConfigurationLoad](https://googleapis.dev/dotnet/Google.Apis.Bigquery.v2/1.74.0.4090/api/Google.Apis.Bigquery.v2.Data.JobConfigurationLoad.html)` |   
**Remarks**

Prefer the properties on this type over this modifier to prepare the request. Only use this modifier to configure aspects for which there are no properties available. This modifier is applied to the request after all properties on this type have been applied. The delegate is only called once per operation, even if the request is automatically retried.

### CreateDisposition
    
    
    public CreateDisposition? CreateDisposition { get; set; }

Specifies whether the operation is allowed to create new tables. If not set, this is effectively [CreateIfNeeded](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.CreateDisposition#Google_Cloud_BigQuery_V2_CreateDisposition_CreateIfNeeded).

**Property Value**  
---  
**Type** | **Description**  
`[CreateDisposition](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.CreateDisposition)` |   
  
### DestinationEncryptionConfiguration
    
    
    public EncryptionConfiguration DestinationEncryptionConfiguration { get; set; }

The encryption configuration to apply to the destination table, if any.

**Property Value**  
---  
**Type** | **Description**  
`[EncryptionConfiguration](https://googleapis.dev/dotnet/Google.Apis.Bigquery.v2/1.74.0.4090/api/Google.Apis.Bigquery.v2.Data.EncryptionConfiguration.html)` |   
  
### DestinationSchemaUpdateOptions
    
    
    public SchemaUpdateOption? DestinationSchemaUpdateOptions { get; set; }

Allows the schema of the destination table to be updated as a side effect of the load job if a schema is autodetected or supplied in the job configuration. Schema update options are supported in two cases: when [WriteDisposition](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.UploadOrcOptions#Google_Cloud_BigQuery_V2_UploadOrcOptions_WriteDisposition) is [WriteAppend](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.WriteDisposition#Google_Cloud_BigQuery_V2_WriteDisposition_WriteAppend); when [WriteDisposition](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.UploadOrcOptions#Google_Cloud_BigQuery_V2_UploadOrcOptions_WriteDisposition) is [WriteTruncate](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.WriteDisposition#Google_Cloud_BigQuery_V2_WriteDisposition_WriteTruncate) and the destination table is a partition of a table, specified by partition decorators. [SchemaUpdateOption](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.SchemaUpdateOption) is marked with the [FlagsAttribute](https://learn.microsoft.com/dotnet/api/system.flagsattribute) so several flags can be specified.

**Property Value**  
---  
**Type** | **Description**  
`[SchemaUpdateOption](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.SchemaUpdateOption)` |   
  
### MaxBadRecords
    
    
    public int? MaxBadRecords { get; set; }

The maximum number of bad records that are ignored before the overall job fails. If not set, this is effectively 0.

**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### TimePartitioning
    
    
    public TimePartitioning TimePartitioning { get; set; }

The time partitioning to apply, if any. See [TimePartition](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.TimePartition) to create instances of [TimePartitioning](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.UploadOrcOptions#Google_Cloud_BigQuery_V2_UploadOrcOptions_TimePartitioning).

**Property Value**  
---  
**Type** | **Description**  
`[TimePartitioning](https://googleapis.dev/dotnet/Google.Apis.Bigquery.v2/1.74.0.4090/api/Google.Apis.Bigquery.v2.Data.TimePartitioning.html)` |   
  
### WriteDisposition
    
    
    public WriteDisposition? WriteDisposition { get; set; }

Specifies the behavior if the destination table exists. If not set, this is effectively [WriteAppend](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.WriteDisposition#Google_Cloud_BigQuery_V2_WriteDisposition_WriteAppend).

**Property Value**  
---  
**Type** | **Description**  
`[WriteDisposition](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.WriteDisposition)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-30 UTC."],[],[]] 
