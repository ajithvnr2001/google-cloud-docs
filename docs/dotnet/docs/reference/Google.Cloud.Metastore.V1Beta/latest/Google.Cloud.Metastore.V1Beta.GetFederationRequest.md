---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.GetFederationRequest
title: Dataproc Metastore v1beta API - Class GetFederationRequest (2.0.0-beta12) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:24:21.131114+00:00
---

# Dataproc Metastore v1beta API - Class GetFederationRequest (2.0.0-beta12)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.GetFederationRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Dataproc Metastore v1beta API - Class GetFederationRequest (2.0.0-beta12) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.0.0-beta12 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.GetFederationRequest)
  * [ 2.0.0-beta11 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/2.0.0-beta11/Google.Cloud.Metastore.V1Beta.GetFederationRequest)
  * [ 1.0.0-beta02 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/1.0.0-beta02/Google.Cloud.Metastore.V1Beta.GetFederationRequest)


    
    
    public sealed class GetFederationRequest : IMessage<GetFederationRequest>, IEquatable<GetFederationRequest>, IDeepCloneable<GetFederationRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the Dataproc Metastore v1beta API class GetFederationRequest.

Request message for GetFederation.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > GetFederationRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[GetFederationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.GetFederationRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[GetFederationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.GetFederationRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[GetFederationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.GetFederationRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Metastore.V1Beta](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta)

## Assembly

Google.Cloud.Metastore.V1Beta.dll

## Constructors 

### GetFederationRequest()
    
    
    public GetFederationRequest()

### GetFederationRequest(GetFederationRequest)
    
    
    public GetFederationRequest(GetFederationRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[GetFederationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.GetFederationRequest)`  
  
  
## Properties 

### FederationName
    
    
    public FederationName FederationName { get; set; }

[FederationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.FederationName)-typed view over the [Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.GetFederationRequest#Google_Cloud_Metastore_V1Beta_GetFederationRequest_Name) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[FederationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.FederationName)` |   
  
### Name
    
    
    public string Name { get; set; }

Required. The relative resource name of the metastore federation to retrieve, in the following form:

`projects/{project_number}/locations/{location_id}/federations/{federation_id}`.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
