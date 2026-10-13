---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.CommentServiceSettings
title: Google Cloud Support v2 API - Class CommentServiceSettings (1.8.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:43:39.320774+00:00
---

# Google Cloud Support v2 API - Class CommentServiceSettings (1.8.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.CommentServiceSettings

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Support v2 API - Class CommentServiceSettings (1.8.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.8.0 (latest)  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0 
    
    
    public sealed class CommentServiceSettings : ServiceSettingsBase

Reference documentation and code samples for the Google Cloud Support v2 API class CommentServiceSettings.

Settings for [CommentServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.CommentServiceClient) instances.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > [ServiceSettingsBase](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.ServiceSettingsBase.html) > CommentServiceSettings

## Inherited Members

[ServiceSettingsBase.VersionHeaderBuilder](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.ServiceSettingsBase.html#Google_Api_Gax_Grpc_ServiceSettingsBase_VersionHeaderBuilder)

[ServiceSettingsBase.CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.ServiceSettingsBase.html#Google_Api_Gax_Grpc_ServiceSettingsBase_CallSettings)

[ServiceSettingsBase.Clock](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.ServiceSettingsBase.html#Google_Api_Gax_Grpc_ServiceSettingsBase_Clock)

[ServiceSettingsBase.Scheduler](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.ServiceSettingsBase.html#Google_Api_Gax_Grpc_ServiceSettingsBase_Scheduler)

[ServiceSettingsBase.Interceptor](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.ServiceSettingsBase.html#Google_Api_Gax_Grpc_ServiceSettingsBase_Interceptor)

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Support.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2)

## Assembly

Google.Cloud.Support.V2.dll

## Constructors 

### CommentServiceSettings()
    
    
    public CommentServiceSettings()

Constructs a new [CommentServiceSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.CommentServiceSettings) object with default settings.

## Properties 

### CreateCommentSettings
    
    
    public CallSettings CreateCommentSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `CommentServiceClient.CreateComment` and `CommentServiceClient.CreateCommentAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * This call will not be retried.
  * Timeout: 60 seconds.



### GetCommentSettings
    
    
    public CallSettings GetCommentSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `CommentServiceClient.GetComment` and `CommentServiceClient.GetCommentAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * This call will not be retried.
  * No timeout is applied.



### ListCommentsSettings
    
    
    public CallSettings ListCommentsSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `CommentServiceClient.ListComments` and `CommentServiceClient.ListCommentsAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * Initial retry delay: 1000 milliseconds.
  * Retry delay multiplier: 1.3
  * Retry maximum delay: 10000 milliseconds.
  * Maximum attempts: 5
  * Retriable status codes: [Unavailable](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html#Grpc_Core_StatusCode_Unavailable).
  * Timeout: 60 seconds.



## Methods 

### Clone()
    
    
    public CommentServiceSettings Clone()

Creates a deep clone of this object, with all the same property values.

**Returns**  
---  
**Type** | **Description**  
`[CommentServiceSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.CommentServiceSettings)` | A deep clone of this [CommentServiceSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.CommentServiceSettings) object.  
  
### GetDefault()
    
    
    public static CommentServiceSettings GetDefault()

Get a new instance of the default [CommentServiceSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.CommentServiceSettings).

**Returns**  
---  
**Type** | **Description**  
`[CommentServiceSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.CommentServiceSettings)` | A new instance of the default [CommentServiceSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.CommentServiceSettings).  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-30 UTC."],[],[]] 
