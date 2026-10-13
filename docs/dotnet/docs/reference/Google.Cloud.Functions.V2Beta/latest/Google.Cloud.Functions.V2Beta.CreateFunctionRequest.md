---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2Beta/latest/Google.Cloud.Functions.V2Beta.CreateFunctionRequest
title: Cloud Functions v2beta API - Class CreateFunctionRequest (1.0.0-beta08) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:17:22.657490+00:00
---

# Cloud Functions v2beta API - Class CreateFunctionRequest (1.0.0-beta08)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2Beta/latest/Google.Cloud.Functions.V2Beta.CreateFunctionRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Cloud Functions v2beta API - Class CreateFunctionRequest (1.0.0-beta08) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 1.0.0-beta08 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2Beta/latest/Google.Cloud.Functions.V2Beta.CreateFunctionRequest)
  * [ 1.0.0-beta07 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2Beta/1.0.0-beta07/Google.Cloud.Functions.V2Beta.CreateFunctionRequest)


    
    
    public sealed class CreateFunctionRequest : IMessage<CreateFunctionRequest>, IEquatable<CreateFunctionRequest>, IDeepCloneable<CreateFunctionRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the Cloud Functions v2beta API class CreateFunctionRequest.

Request for the `CreateFunction` method.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > CreateFunctionRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[CreateFunctionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2Beta/latest/Google.Cloud.Functions.V2Beta.CreateFunctionRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[CreateFunctionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2Beta/latest/Google.Cloud.Functions.V2Beta.CreateFunctionRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[CreateFunctionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2Beta/latest/Google.Cloud.Functions.V2Beta.CreateFunctionRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Functions.V2Beta](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2Beta/latest/Google.Cloud.Functions.V2Beta)

## Assembly

Google.Cloud.Functions.V2Beta.dll

## Constructors 

### CreateFunctionRequest()
    
    
    public CreateFunctionRequest()

### CreateFunctionRequest(CreateFunctionRequest)
    
    
    public CreateFunctionRequest(CreateFunctionRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[CreateFunctionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2Beta/latest/Google.Cloud.Functions.V2Beta.CreateFunctionRequest)`  
  
  
## Properties 

### Function
    
    
    public Function Function { get; set; }

Required. Function to be created.

**Property Value**  
---  
**Type** | **Description**  
`[Function](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2Beta/latest/Google.Cloud.Functions.V2Beta.Function)` |   
  
### FunctionId
    
    
    public string FunctionId { get; set; }

The ID to use for the function, which will become the final component of the function's resource name.

This value should be 4-63 characters, and valid characters are /[a-z][0-9]-/.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Parent
    
    
    public string Parent { get; set; }

Required. The project and location in which the function should be created, specified in the format `projects/*/locations/*`

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ParentAsLocationName
    
    
    public LocationName ParentAsLocationName { get; set; }

[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)-typed view over the [Parent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2Beta/latest/Google.Cloud.Functions.V2Beta.CreateFunctionRequest#Google_Cloud_Functions_V2Beta_CreateFunctionRequest_Parent) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
