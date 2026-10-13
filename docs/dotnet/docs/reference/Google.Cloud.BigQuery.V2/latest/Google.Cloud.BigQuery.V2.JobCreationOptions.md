---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.JobCreationOptions
title: Google BigQuery v2 API - Class JobCreationOptions (3.12.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:31:40.000774+00:00
---

# Google BigQuery v2 API - Class JobCreationOptions (3.12.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.JobCreationOptions

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google BigQuery v2 API - Class JobCreationOptions (3.12.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.12.0 (latest)  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.4.0  2.3.0  2.2.0 
    
    
    public abstract class JobCreationOptions

Reference documentation and code samples for the Google BigQuery v2 API class JobCreationOptions.

Base class for options for operations that create jobs.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > JobCreationOptions

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Derived Types

[CreateCopyJobOptions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.CreateCopyJobOptions)

[CreateExtractJobOptions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.CreateExtractJobOptions)

[CreateLoadJobOptions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.CreateLoadJobOptions)

[CreateModelExtractJobOptions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.CreateModelExtractJobOptions)

[QueryOptions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.QueryOptions)

[UploadAvroOptions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.UploadAvroOptions)

[UploadCsvOptions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.UploadCsvOptions)

[UploadJsonOptions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.UploadJsonOptions)

[UploadOrcOptions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.UploadOrcOptions)

[UploadParquetOptions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.UploadParquetOptions)

## Namespace

[Google.Cloud.BigQuery.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2)

## Assembly

Google.Cloud.BigQuery.V2.dll

## Properties 

### JobConfigurationModifier
    
    
    public Action<JobConfiguration> JobConfigurationModifier { get; set; }

Optional action to perform after preparing the request. If this property is non-null, the [JobConfiguration](https://googleapis.dev/dotnet/Google.Apis.Bigquery.v2/1.74.0.4090/api/Google.Apis.Bigquery.v2.Data.JobConfiguration.html) used for a request will be passed to the delegate before the request is executed. This allows for fine-grained modifications which aren't otherwise directly supported by the properties in this options type or derived option types.

**Property Value**  
---  
**Type** | **Description**  
`[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[JobConfiguration](https://googleapis.dev/dotnet/Google.Apis.Bigquery.v2/1.74.0.4090/api/Google.Apis.Bigquery.v2.Data.JobConfiguration.html)` |   
**Remarks**

Prefer the properties on this type over this modifier to prepare the request. Only use this modifier to configure aspects for which there are no properties available. This modifier is applied to the request after all properties on this type have been applied. The delegate is only called once per operation, even if the request is automatically retried.

### JobId
    
    
    public string JobId { get; set; }

If specified, this ID will be used to create the job. It is an error to set both this property and [JobIdPrefix](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.JobCreationOptions#Google_Cloud_BigQuery_V2_JobCreationOptions_JobIdPrefix).

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### JobIdPrefix
    
    
    public string JobIdPrefix { get; set; }

If specified, use this prefix when generating a job ID. (Job IDs are always generated client-side by this library, to allow insertion to be retried where necessary.) It is an error to set both this property and [JobId](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.JobCreationOptions#Google_Cloud_BigQuery_V2_JobCreationOptions_JobId).

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### JobLocation
    
    
    public string JobLocation { get; set; }

If specified, the job will be created in this location. Otherwise, it will be created in the client's [default location](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.BigQueryClient#Google_Cloud_BigQuery_V2_BigQueryClient_DefaultLocation).

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
**See Also**

[WithDefaultLocation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.BigQueryClient#Google_Cloud_BigQuery_V2_BigQueryClient_WithDefaultLocation_System_String_)[string](https://learn.microsoft.com/dotnet/api/system.string)

### Labels
    
    
    public IDictionary<string, string> Labels { get; set; }
    
    
    The labels associated with the job to be created.
    Labels are key-value pairs.
    You can use these to organize and group your jobs.
    Label keys and values can be no longer than 63 characters,
    can only contain lowercase letters, numeric characters,
    underscores and dashes. International characters are allowed.
    If a label value is 
    
    
    
    null

, it won't be added to the job's labels. A label value can be [Empty](https://learn.microsoft.com/dotnet/api/system.string.empty). Label keys must start with a letter.

**Property Value**  
---  
**Type** | **Description**  
`[IDictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.idictionary-2)[string](https://learn.microsoft.com/dotnet/api/system.string)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
**Example**
    
    
    IDictionary<string, string> labels = new Dictionary<string, string>()
    {
        {"label-key", "label-value" }
    };
    
    BigQueryClient client = BigQueryClient.Create(projectId);
    BigQueryTable table = client.GetTable(projectId, datasetId, tableId);
    string destinationUri = $"gs://{bucketName}/{objectName}";
    
    // Just a couple examples of jobs marked with labels:
    // (These jobs will most certainly be created somewhere else.)
    // Running a query on a given table.
    BigQueryJob oneLabeledJob = client.CreateQueryJob(
        $"SELECT * FROM {table}", null,
        new QueryOptions { Labels = labels });
    // Extracting data from a table to GCS.
    BigQueryJob anotherLabeledJob = client.CreateExtractJob(
        projectId, datasetId, tableId, destinationUri,
        new CreateExtractJobOptions { Labels = labels });
    
    // Find jobs marked with a certain label.
    KeyValuePair<string, string> labelToBeFound = labels.First();
            // Specify full projection to make sure that
            // label information, if it exists, is returned for listed jobs.
    ListJobsOptions options = new ListJobsOptions { Projection = ProjectionEnum.Full };
    List <BigQueryJob> jobs = client
        .ListJobs(options)
        .Where(job => job.Resource.Configuration.Labels?.Contains(labelToBeFound) ?? false)
        .Take(2)
        .ToList();
    foreach (BigQueryJob job in jobs)
    {
        Console.WriteLine(job.Reference.JobId);
    }
    

### ProjectId
    
    
    public string ProjectId { get; set; }

The ID of the project in which to create the job. If this is not set, it defaults to the project ID of the client.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-30 UTC."],[],[]] 
