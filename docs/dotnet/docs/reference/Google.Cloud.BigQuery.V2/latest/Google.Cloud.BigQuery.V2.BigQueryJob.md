---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.BigQueryJob
title: Google BigQuery v2 API - Class BigQueryJob (3.12.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:30:03.766373+00:00
---

# Google BigQuery v2 API - Class BigQueryJob (3.12.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.BigQueryJob

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google BigQuery v2 API - Class BigQueryJob (3.12.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.12.0 (latest)  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.4.0  2.3.0  2.2.0 
    
    
    public sealed class BigQueryJob

Reference documentation and code samples for the Google BigQuery v2 API class BigQueryJob.

An asynchronous job within BigQuery.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > BigQueryJob

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.BigQuery.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2)

## Assembly

Google.Cloud.BigQuery.V2.dll

## Remarks

This class wraps the underlying REST API resource and retains a reference to the original client, allowing for simpler job-oriented operations.

## Constructors 

### BigQueryJob(BigQueryClient, Job)
    
    
    public BigQueryJob(BigQueryClient client, Job resource)

Constructs a new job.

**Parameters**  
---  
**Name** | **Description**  
`client` | `[BigQueryClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.BigQueryClient)`  
The client to use for operations on the job. Must not be null.  
`resource` | `[Job](https://googleapis.dev/dotnet/Google.Apis.Bigquery.v2/1.74.0.4090/api/Google.Apis.Bigquery.v2.Data.Job.html)`  
The REST-ful resource representing the job. Must not be null.  
**Remarks**

This is public to allow tests to construct instances for production code to consume; production code should not normally construct instances itself.

## Properties 

### Reference
    
    
    public JobReference Reference { get; }

The fully-qualified identifier for the job. This is short-hand for `Resource.JobReference`.

**Property Value**  
---  
**Type** | **Description**  
`[JobReference](https://googleapis.dev/dotnet/Google.Apis.Bigquery.v2/1.74.0.4090/api/Google.Apis.Bigquery.v2.Data.JobReference.html)` |   
**Remarks**

The properties within the reference can be used to determine the project ID and job ID components.

### Resource
    
    
    public Job Resource { get; }

The underlying REST-ful resource for the job.

**Property Value**  
---  
**Type** | **Description**  
`[Job](https://googleapis.dev/dotnet/Google.Apis.Bigquery.v2/1.74.0.4090/api/Google.Apis.Bigquery.v2.Data.Job.html)` |   
**Remarks**

The data within the resource may be incomplete, depending on how it was obtained.

### State
    
    
    public JobState State { get; }

The state of the job.

**Property Value**  
---  
**Type** | **Description**  
`[JobState](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.JobState)` |   
  
### Statistics
    
    
    public JobStatistics Statistics { get; }

The statistics of the job. This is short-hand for `Resource.Statistics`.

**Property Value**  
---  
**Type** | **Description**  
`[JobStatistics](https://googleapis.dev/dotnet/Google.Apis.Bigquery.v2/1.74.0.4090/api/Google.Apis.Bigquery.v2.Data.JobStatistics.html)` |   
  
### Status
    
    
    public JobStatus Status { get; }

The full status of the job, including any errors. This is short-hand for `Resource.Status`.

**Property Value**  
---  
**Type** | **Description**  
`[JobStatus](https://googleapis.dev/dotnet/Google.Apis.Bigquery.v2/1.74.0.4090/api/Google.Apis.Bigquery.v2.Data.JobStatus.html)` |   
  
## Methods 

### Cancel(CancelJobOptions)
    
    
    public BigQueryJob Cancel(CancelJobOptions options = null)

Cancels this job. This method just creates a [JobReference](https://googleapis.dev/dotnet/Google.Apis.Bigquery.v2/1.74.0.4090/api/Google.Apis.Bigquery.v2.Data.JobReference.html) and delegates to [CancelJob(JobReference, CancelJobOptions)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.BigQueryClient#Google_Cloud_BigQuery_V2_BigQueryClient_CancelJob_Google_Apis_Bigquery_v2_Data_JobReference_Google_Cloud_BigQuery_V2_CancelJobOptions_).

**Parameter**  
---  
**Name** | **Description**  
`options` | `[CancelJobOptions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.CancelJobOptions)`  
The options for the operation. May be null, in which case defaults will be supplied.  
**Returns**  
---  
**Type** | **Description**  
`[BigQueryJob](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.BigQueryJob)` | The final state of the job.  
**Example**

See [BigQueryClient.CancelJob](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.BigQueryClient#Google_Cloud_BigQuery_V2_BigQueryClient_CancelJob_System_String_Google_Cloud_BigQuery_V2_CancelJobOptions_) for an example using BigQueryClient.

### CancelAsync(CancelJobOptions, CancellationToken)
    
    
    public Task<BigQueryJob> CancelAsync(CancelJobOptions options = null, CancellationToken cancellationToken = default)

Asynchronously cancels this job. This method just creates a [JobReference](https://googleapis.dev/dotnet/Google.Apis.Bigquery.v2/1.74.0.4090/api/Google.Apis.Bigquery.v2.Data.JobReference.html) and delegates to [CancelJobAsync(JobReference, CancelJobOptions, CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.BigQueryClient#Google_Cloud_BigQuery_V2_BigQueryClient_CancelJobAsync_Google_Apis_Bigquery_v2_Data_JobReference_Google_Cloud_BigQuery_V2_CancelJobOptions_System_Threading_CancellationToken_).

**Parameters**  
---  
**Name** | **Description**  
`options` | `[CancelJobOptions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.CancelJobOptions)`  
The options for the operation. May be null, in which case defaults will be supplied.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
The token to monitor for cancellation requests.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[BigQueryJob](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.BigQueryJob)` | A task representing the asynchronous operation. When complete, the result is the final state of the job.  
**Example**

See [BigQueryClient.CancelJob](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.BigQueryClient#Google_Cloud_BigQuery_V2_BigQueryClient_CancelJob_System_String_Google_Cloud_BigQuery_V2_CancelJobOptions_) for an example using BigQueryClient.

### Delete(DeleteJobOptions)
    
    
    public void Delete(DeleteJobOptions options = null)

Deletes this job. This method just creates a [JobReference](https://googleapis.dev/dotnet/Google.Apis.Bigquery.v2/1.74.0.4090/api/Google.Apis.Bigquery.v2.Data.JobReference.html) and delegates to [DeleteJob(JobReference, DeleteJobOptions)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.BigQueryClient#Google_Cloud_BigQuery_V2_BigQueryClient_DeleteJob_Google_Apis_Bigquery_v2_Data_JobReference_Google_Cloud_BigQuery_V2_DeleteJobOptions_).

**Parameter**  
---  
**Name** | **Description**  
`options` | `[DeleteJobOptions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.DeleteJobOptions)`  
The options for the operation. May be null, in which case defaults will be supplied.  
  
### DeleteAsync(DeleteJobOptions, CancellationToken)
    
    
    public Task DeleteAsync(DeleteJobOptions options = null, CancellationToken cancellationToken = default)

Asynchronously deletes this job. This method just creates a [JobReference](https://googleapis.dev/dotnet/Google.Apis.Bigquery.v2/1.74.0.4090/api/Google.Apis.Bigquery.v2.Data.JobReference.html) and delegates to [DeleteJobAsync(JobReference, DeleteJobOptions, CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.BigQueryClient#Google_Cloud_BigQuery_V2_BigQueryClient_DeleteJobAsync_Google_Apis_Bigquery_v2_Data_JobReference_Google_Cloud_BigQuery_V2_DeleteJobOptions_System_Threading_CancellationToken_).

**Parameters**  
---  
**Name** | **Description**  
`options` | `[DeleteJobOptions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.DeleteJobOptions)`  
The options for the operation. May be null, in which case defaults will be supplied.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
The token to monitor for cancellation requests.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A task representing the asynchronous operation. When complete, the result is the final state of the job.  
  
### GetQueryResults(GetQueryResultsOptions)
    
    
    public BigQueryResults GetQueryResults(GetQueryResultsOptions options = null)

Retrieves the result of this job, which must be a query job. This method just creates a [JobReference](https://googleapis.dev/dotnet/Google.Apis.Bigquery.v2/1.74.0.4090/api/Google.Apis.Bigquery.v2.Data.JobReference.html) and delegates to [GetQueryResults(JobReference, GetQueryResultsOptions)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.BigQueryClient#Google_Cloud_BigQuery_V2_BigQueryClient_GetQueryResults_Google_Apis_Bigquery_v2_Data_JobReference_Google_Cloud_BigQuery_V2_GetQueryResultsOptions_).

**Parameter**  
---  
**Name** | **Description**  
`options` | `[GetQueryResultsOptions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.GetQueryResultsOptions)`  
The options for the operation. May be null, in which case defaults will be supplied.  
**Returns**  
---  
**Type** | **Description**  
`[BigQueryResults](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.BigQueryResults)` | The result of the query.  
**Remarks**

This method will only return when the query has completed. 

**Example**

See [BigQueryClient.GetQueryResults](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.BigQueryClient#Google_Cloud_BigQuery_V2_BigQueryClient_GetQueryResults_Google_Apis_Bigquery_v2_Data_JobReference_Google_Cloud_BigQuery_V2_GetQueryResultsOptions_) for an example using BigQueryClient.

### GetQueryResultsAsync(GetQueryResultsOptions, CancellationToken)
    
    
    public Task<BigQueryResults> GetQueryResultsAsync(GetQueryResultsOptions options = null, CancellationToken cancellationToken = default)

Asynchronously retrieves the result of this job, which must be a query job. This method just creates a [JobReference](https://googleapis.dev/dotnet/Google.Apis.Bigquery.v2/1.74.0.4090/api/Google.Apis.Bigquery.v2.Data.JobReference.html) and delegates to [GetQueryResultsAsync(JobReference, GetQueryResultsOptions, CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.BigQueryClient#Google_Cloud_BigQuery_V2_BigQueryClient_GetQueryResultsAsync_Google_Apis_Bigquery_v2_Data_JobReference_Google_Cloud_BigQuery_V2_GetQueryResultsOptions_System_Threading_CancellationToken_).

**Parameters**  
---  
**Name** | **Description**  
`options` | `[GetQueryResultsOptions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.GetQueryResultsOptions)`  
The options for the operation. May be null, in which case defaults will be supplied.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
The token to monitor for cancellation requests.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[BigQueryResults](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.BigQueryResults)` | A task representing the asynchronous operation. When complete, the result is a [BigQueryResults](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.BigQueryResults) representation of the query.  
**Remarks**

The task returned by this method will only complete when the query has completed. 

**Example**

See [BigQueryClient.GetQueryResultsAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.BigQueryClient#Google_Cloud_BigQuery_V2_BigQueryClient_GetQueryResultsAsync_Google_Apis_Bigquery_v2_Data_JobReference_Google_Cloud_BigQuery_V2_GetQueryResultsOptions_System_Threading_CancellationToken_) for an example using BigQueryClient.

### PollUntilCompleted(GetJobOptions, PollSettings)
    
    
    public BigQueryJob PollUntilCompleted(GetJobOptions options = null, PollSettings pollSettings = null)

Polls this job for completion, returning a new [BigQueryJob](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.BigQueryJob) object with the updated information. This method just creates a [JobReference](https://googleapis.dev/dotnet/Google.Apis.Bigquery.v2/1.74.0.4090/api/Google.Apis.Bigquery.v2.Data.JobReference.html) and delegates to [PollJobUntilCompleted(JobReference, GetJobOptions, PollSettings)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.BigQueryClient#Google_Cloud_BigQuery_V2_BigQueryClient_PollJobUntilCompleted_Google_Apis_Bigquery_v2_Data_JobReference_Google_Cloud_BigQuery_V2_GetJobOptions_Google_Api_Gax_PollSettings_).

**Parameters**  
---  
**Name** | **Description**  
`options` | `[GetJobOptions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.GetJobOptions)`  
The options for the operation. May be null, in which case defaults will be supplied.  
`pollSettings` | `[PollSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PollSettings.html)`  
The settings to control how often and long the job is fetched before timing out if it is still incomplete. May be null, in which case defaults will be supplied.  
**Returns**  
---  
**Type** | **Description**  
`[BigQueryJob](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.BigQueryJob)` | The completed job.  
**Remarks**

Note that this method does not modify the state of the object it is called on. Instead, a new object is returned. If you need to check that the job completed without errors, or access any other information, you need to use the return value of the method.

**Example**

See [BigQueryClient.PollJobUntilCompleted](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.BigQueryClient#Google_Cloud_BigQuery_V2_BigQueryClient_PollJobUntilCompleted_System_String_Google_Cloud_BigQuery_V2_GetJobOptions_Google_Api_Gax_PollSettings_) for an example using BigQueryClient.

### PollUntilCompletedAsync(GetJobOptions, PollSettings, CancellationToken)
    
    
    public Task<BigQueryJob> PollUntilCompletedAsync(GetJobOptions options = null, PollSettings pollSettings = null, CancellationToken cancellationToken = default)

Asynchronously polls this job for completion. This method just creates a [JobReference](https://googleapis.dev/dotnet/Google.Apis.Bigquery.v2/1.74.0.4090/api/Google.Apis.Bigquery.v2.Data.JobReference.html) and delegates to [PollJobUntilCompletedAsync(JobReference, GetJobOptions, PollSettings, CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.BigQueryClient#Google_Cloud_BigQuery_V2_BigQueryClient_PollJobUntilCompletedAsync_Google_Apis_Bigquery_v2_Data_JobReference_Google_Cloud_BigQuery_V2_GetJobOptions_Google_Api_Gax_PollSettings_System_Threading_CancellationToken_).

**Parameters**  
---  
**Name** | **Description**  
`options` | `[GetJobOptions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.GetJobOptions)`  
The options for the operation. May be null, in which case defaults will be supplied.  
`pollSettings` | `[PollSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PollSettings.html)`  
The settings to control how often and long the job is fetched before timing out if it is still incomplete. May be null, in which case defaults will be supplied.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
The token to monitor for cancellation requests.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[BigQueryJob](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.BigQueryJob)` | A task representing the asynchronous operation. When complete, the result is the completed job.  
**Example**

See [BigQueryClient.PollJobUntilCompleted](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.BigQueryClient#Google_Cloud_BigQuery_V2_BigQueryClient_PollJobUntilCompleted_System_String_Google_Cloud_BigQuery_V2_GetJobOptions_Google_Api_Gax_PollSettings_) for an example using BigQueryClient.

### ThrowOnAnyError()
    
    
    public BigQueryJob ThrowOnAnyError()

Throws an exception if the job has any errors, or returns `this` if the job has no errors so far. A job may have errors but still contain useful information, and may also contain errors before completing. If this method is called on a job that completed successfully but with errors, it will throw an exception. Use [ThrowOnFatalError()](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.BigQueryJob#Google_Cloud_BigQuery_V2_BigQueryJob_ThrowOnFatalError) to only throw an exception if a job has failed.

**Returns**  
---  
**Type** | **Description**  
`[BigQueryJob](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.BigQueryJob)` | `this` if the job has no errors.  
**Example**
    
    
    BigQueryClient client = BigQueryClient.Create(projectId);
    
    string sql = $"This is a broken query";
    BigQueryJob query = client.CreateQueryJob(sql, parameters: null).PollUntilCompleted();
    try
    {
        // Usually this method is called in a chain. It returns the same job
        // if there are no errors.
        query = query.ThrowOnAnyError();
    }
    catch (GoogleApiException exception)
    {
        foreach (var error in exception.Error.Errors)
        {
            Console.WriteLine($"Location: {error.Location}; Reason: {error.Reason}; Message: {error.Message}");
        }
    }
    

**Exceptions**  
---  
**Type** | **Description**  
`[GoogleApiException](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.GoogleApiException.html)` | The job has errors. The [Errors](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Requests.RequestError.html#Google_Apis_Requests_RequestError_Errors) property corresponds to the errors reported in Google.Apis.Bigquery.v2.Data.JobStatus.Errors.  
  
### ThrowOnFatalError()
    
    
    public BigQueryJob ThrowOnFatalError()

Throws an exception if the job has failed. Returns `this` if the job has not failed, even if it contains errors. A job may have errors but still contain useful information, and may also contain errors before completing. Use [ThrowOnAnyError()](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.BigQueryJob#Google_Cloud_BigQuery_V2_BigQueryJob_ThrowOnAnyError) to throw an exception if any errors have been reported.

**Returns**  
---  
**Type** | **Description**  
`[BigQueryJob](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.BigQueryJob)` | `this` if the job has not completed unsuccessfully (either because it hasn't completed, or it has completed successfully, potentially with non-fatal errors).  
**Exceptions**  
---  
**Type** | **Description**  
`[GoogleApiException](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.GoogleApiException.html)` | The job has failed. Within the [Errors](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Requests.RequestError.html#Google_Apis_Requests_RequestError_Errors) property, the first error is from the Google.Apis.Bigquery.v2.Data.JobStatus.ErrorResult, and any others are from Google.Apis.Bigquery.v2.Data.JobStatus.Errors.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-30 UTC."],[],[]] 
