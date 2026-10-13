---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.GetServiceRequest
title: Dataproc Metastore v1beta API - Class GetServiceRequest (2.0.0-beta12) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:24:21.202082+00:00
---

# Dataproc Metastore v1beta API - Class GetServiceRequest (2.0.0-beta12)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.GetServiceRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Dataproc Metastore v1beta API - Class GetServiceRequest (2.0.0-beta12) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.0.0-beta12 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.GetServiceRequest)
  * [ 2.0.0-beta11 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/2.0.0-beta11/Google.Cloud.Metastore.V1Beta.GetServiceRequest)
  * [ 1.0.0-beta02 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/1.0.0-beta02/Google.Cloud.Metastore.V1Beta.GetServiceRequest)


    
    
    public sealed class GetServiceRequest : IMessage<GetServiceRequest>, IEquatable<GetServiceRequest>, IDeepCloneable<GetServiceRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the Dataproc Metastore v1beta API class GetServiceRequest.

Request message for [DataprocMetastore.GetService][google.cloud.metastore.v1beta.DataprocMetastore.GetService].

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > GetServiceRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[GetServiceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.GetServiceRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[GetServiceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.GetServiceRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[GetServiceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.GetServiceRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Metastore.V1Beta](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta)

## Assembly

Google.Cloud.Metastore.V1Beta.dll

## Constructors 

### GetServiceRequest()
    
    
    public GetServiceRequest()

### GetServiceRequest(GetServiceRequest)
    
    
    public GetServiceRequest(GetServiceRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[GetServiceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.GetServiceRequest)`  
  
  
## Properties 

### Name
    
    
    public string Name { get; set; }

Required. The relative resource name of the metastore service to retrieve, in the following form:

`projects/{project_number}/locations/{location_id}/services/{service_id}`.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ServiceName
    
    
    public ServiceName ServiceName { get; set; }

[ServiceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.ServiceName)-typed view over the [Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.GetServiceRequest#Google_Cloud_Metastore_V1Beta_GetServiceRequest_Name) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[ServiceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.ServiceName)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
