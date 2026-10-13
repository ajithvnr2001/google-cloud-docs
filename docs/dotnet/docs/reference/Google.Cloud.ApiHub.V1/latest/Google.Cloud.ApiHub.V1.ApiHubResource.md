---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.ApiHubResource
title: API hub v1 API - Class ApiHubResource (1.2.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:03:24.397290+00:00
---

# API hub v1 API - Class ApiHubResource (1.2.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.ApiHubResource

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  API hub v1 API - Class ApiHubResource (1.2.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 1.2.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.ApiHubResource)
  * [ 1.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/1.1.0/Google.Cloud.ApiHub.V1.ApiHubResource)
  * [ 1.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/1.0.0/Google.Cloud.ApiHub.V1.ApiHubResource)


    
    
    public sealed class ApiHubResource : IMessage<ApiHubResource>, IEquatable<ApiHubResource>, IDeepCloneable<ApiHubResource>, IBufferMessage, IMessage

Reference documentation and code samples for the API hub v1 API class ApiHubResource.

ApiHubResource is one of the resources such as Api, Operation, Deployment, Definition, Spec and Version resources stored in API-Hub.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ApiHubResource

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[ApiHubResource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.ApiHubResource), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[ApiHubResource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.ApiHubResource), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[ApiHubResource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.ApiHubResource), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.ApiHub.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1)

## Assembly

Google.Cloud.ApiHub.V1.dll

## Constructors 

### ApiHubResource()
    
    
    public ApiHubResource()

### ApiHubResource(ApiHubResource)
    
    
    public ApiHubResource(ApiHubResource other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[ApiHubResource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.ApiHubResource)`  
  
  
## Properties 

### Api
    
    
    public Api Api { get; set; }

This represents Api resource in search results. Only name, display_name, description and owner fields are populated in search results.

**Property Value**  
---  
**Type** | **Description**  
`[Api](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.Api)` |   
  
### Definition
    
    
    public Definition Definition { get; set; }

This represents Definition resource in search results. Only name field is populated in search results.

**Property Value**  
---  
**Type** | **Description**  
`[Definition](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.Definition)` |   
  
### Deployment
    
    
    public Deployment Deployment { get; set; }

This represents Deployment resource in search results. Only name, display_name, description, deployment_type and api_versions fields are populated in search results.

**Property Value**  
---  
**Type** | **Description**  
`[Deployment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.Deployment)` |   
  
### Operation
    
    
    public ApiOperation Operation { get; set; }

This represents ApiOperation resource in search results. Only name, description, spec and details fields are populated in search results.

**Property Value**  
---  
**Type** | **Description**  
`[ApiOperation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.ApiOperation)` |   
  
### ResourceCase
    
    
    public ApiHubResource.ResourceOneofCase ResourceCase { get; }

**Property Value**  
---  
**Type** | **Description**  
`[ApiHubResource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.ApiHubResource)[ResourceOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.ApiHubResource.ResourceOneofCase)` |   
  
### Spec
    
    
    public Spec Spec { get; set; }

This represents Spec resource in search results. Only name, display_name, description, spec_type and documentation fields are populated in search results.

**Property Value**  
---  
**Type** | **Description**  
`[Spec](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.Spec)` |   
  
### Version
    
    
    public Version Version { get; set; }

This represents Version resource in search results. Only name, display_name, description, lifecycle, compliance and accreditation fields are populated in search results.

**Property Value**  
---  
**Type** | **Description**  
`[Version](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.Version)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
