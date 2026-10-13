---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ftp.V1/latest/Google.Cloud.Ftp.V1.StopServerRequest
title: Cloud FTP v1 API - Class StopServerRequest (1.0.0-beta01) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:16:31.124115+00:00
---

# Cloud FTP v1 API - Class StopServerRequest (1.0.0-beta01)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ftp.V1/latest/Google.Cloud.Ftp.V1.StopServerRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Cloud FTP v1 API - Class StopServerRequest (1.0.0-beta01) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    public sealed class StopServerRequest : IMessage<StopServerRequest>, IEquatable<StopServerRequest>, IDeepCloneable<StopServerRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the Cloud FTP v1 API class StopServerRequest.

Request message for stopping a Server.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > StopServerRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[StopServerRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ftp.V1/latest/Google.Cloud.Ftp.V1.StopServerRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[StopServerRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ftp.V1/latest/Google.Cloud.Ftp.V1.StopServerRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[StopServerRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ftp.V1/latest/Google.Cloud.Ftp.V1.StopServerRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Ftp.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ftp.V1/latest/Google.Cloud.Ftp.V1)

## Assembly

Google.Cloud.Ftp.V1.dll

## Constructors 

### StopServerRequest()
    
    
    public StopServerRequest()

### StopServerRequest(StopServerRequest)
    
    
    public StopServerRequest(StopServerRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[StopServerRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ftp.V1/latest/Google.Cloud.Ftp.V1.StopServerRequest)`  
  
  
## Properties 

### Name
    
    
    public string Name { get; set; }

Required. Name of the resource. Format: `projects/{project}/locations/{location}/servers/{server}`

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ServerName
    
    
    public ServerName ServerName { get; set; }

[ServerName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ftp.V1/latest/Google.Cloud.Ftp.V1.ServerName)-typed view over the [Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ftp.V1/latest/Google.Cloud.Ftp.V1.StopServerRequest#Google_Cloud_Ftp_V1_StopServerRequest_Name) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[ServerName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ftp.V1/latest/Google.Cloud.Ftp.V1.ServerName)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-18 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-18 UTC."],[],[]] 
