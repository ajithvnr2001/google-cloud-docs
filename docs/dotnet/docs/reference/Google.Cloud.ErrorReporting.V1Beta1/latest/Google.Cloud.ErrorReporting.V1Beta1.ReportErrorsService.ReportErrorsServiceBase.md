---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ErrorReporting.V1Beta1/latest/Google.Cloud.ErrorReporting.V1Beta1.ReportErrorsService.ReportErrorsServiceBase
title: Google Cloud Error Reporting v1beta1 API - Class ReportErrorsService.ReportErrorsServiceBase (3.0.0-beta06) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:11:36.528728+00:00
---

# Google Cloud Error Reporting v1beta1 API - Class ReportErrorsService.ReportErrorsServiceBase (3.0.0-beta06)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ErrorReporting.V1Beta1/latest/Google.Cloud.ErrorReporting.V1Beta1.ReportErrorsService.ReportErrorsServiceBase

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Error Reporting v1beta1 API - Class ReportErrorsService.ReportErrorsServiceBase (3.0.0-beta06) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 3.0.0-beta06 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ErrorReporting.V1Beta1/latest/Google.Cloud.ErrorReporting.V1Beta1.ReportErrorsService.ReportErrorsServiceBase)
  * [ 3.0.0-beta05 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ErrorReporting.V1Beta1/3.0.0-beta05/Google.Cloud.ErrorReporting.V1Beta1.ReportErrorsService.ReportErrorsServiceBase)
  * [ 2.0.0-beta05 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ErrorReporting.V1Beta1/2.0.0-beta05/Google.Cloud.ErrorReporting.V1Beta1.ReportErrorsService.ReportErrorsServiceBase)


    
    
    [BindServiceMethod(typeof(ReportErrorsService), "BindService")]
    public abstract class ReportErrorsService.ReportErrorsServiceBase

Reference documentation and code samples for the Google Cloud Error Reporting v1beta1 API class ReportErrorsService.ReportErrorsServiceBase.

Base class for server-side implementations of ReportErrorsService

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ReportErrorsService.ReportErrorsServiceBase

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.ErrorReporting.V1Beta1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ErrorReporting.V1Beta1/latest/Google.Cloud.ErrorReporting.V1Beta1)

## Assembly

Google.Cloud.ErrorReporting.V1Beta1.dll

## Methods 

### ReportErrorEvent(ReportErrorEventRequest, ServerCallContext)
    
    
    public virtual Task<ReportErrorEventResponse> ReportErrorEvent(ReportErrorEventRequest request, ServerCallContext context)

Report an individual error event and record the event to a log.

This endpoint accepts **either** an OAuth token, **or** an [API key](https://support.google.com/cloud/answer/6158862) for authentication. To use an API key, append it to the URL as the value of a `key` parameter. For example:

`POST https://clouderrorreporting.googleapis.com/v1beta1/{projectName}/events:report?key=123ABC456`

**Note:** [Error Reporting](https://cloud.google.com/error-reporting) is a service built on Cloud Logging and can analyze log entries when all of the following are true:

  * Customer-managed encryption keys (CMEK) are disabled on the log bucket.
  * The log bucket satisfies one of the following:
    * The log bucket is stored in the same project where the logs originated.
    * The logs were routed to a project, and then that project stored those logs in a log bucket that it owns.



**Parameters**  
---  
**Name** | **Description**  
`request` | `[ReportErrorEventRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ErrorReporting.V1Beta1/latest/Google.Cloud.ErrorReporting.V1Beta1.ReportErrorEventRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ReportErrorEventResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ErrorReporting.V1Beta1/latest/Google.Cloud.ErrorReporting.V1Beta1.ReportErrorEventResponse)` | The response to send back to the client (wrapped by a task).  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
