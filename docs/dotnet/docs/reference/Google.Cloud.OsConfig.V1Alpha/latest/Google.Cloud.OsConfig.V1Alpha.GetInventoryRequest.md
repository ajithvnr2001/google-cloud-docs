---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.GetInventoryRequest
title: Google Cloud OS Config v1alpha API - Class GetInventoryRequest (2.0.0-alpha07) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:52:21.979119+00:00
---

# Google Cloud OS Config v1alpha API - Class GetInventoryRequest (2.0.0-alpha07)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.GetInventoryRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud OS Config v1alpha API - Class GetInventoryRequest (2.0.0-alpha07) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.0.0-alpha07 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.GetInventoryRequest)
  * [ 2.0.0-alpha06 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/2.0.0-alpha06/Google.Cloud.OsConfig.V1Alpha.GetInventoryRequest)
  * [ 1.0.0-alpha04 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/1.0.0-alpha04/Google.Cloud.OsConfig.V1Alpha.GetInventoryRequest)


    
    
    public sealed class GetInventoryRequest : IMessage<GetInventoryRequest>, IEquatable<GetInventoryRequest>, IDeepCloneable<GetInventoryRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the Google Cloud OS Config v1alpha API class GetInventoryRequest.

A request message for getting inventory data for the specified VM.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > GetInventoryRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[GetInventoryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.GetInventoryRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[GetInventoryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.GetInventoryRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[GetInventoryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.GetInventoryRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.OsConfig.V1Alpha](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha)

## Assembly

Google.Cloud.OsConfig.V1Alpha.dll

## Constructors 

### GetInventoryRequest()
    
    
    public GetInventoryRequest()

### GetInventoryRequest(GetInventoryRequest)
    
    
    public GetInventoryRequest(GetInventoryRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[GetInventoryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.GetInventoryRequest)`  
  
  
## Properties 

### InventoryName
    
    
    public InventoryName InventoryName { get; set; }

[InventoryName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.InventoryName)-typed view over the [Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.GetInventoryRequest#Google_Cloud_OsConfig_V1Alpha_GetInventoryRequest_Name) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[InventoryName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.InventoryName)` |   
  
### Name
    
    
    public string Name { get; set; }

Required. API resource name for inventory resource.

Format: `projects/{project}/locations/{location}/instances/{instance}/inventory`

For `{project}`, either `project-number` or `project-id` can be provided. For `{instance}`, either Compute Engine `instance-id` or `instance-name` can be provided.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### View
    
    
    public InventoryView View { get; set; }

Inventory view indicating what information should be included in the inventory resource. If unspecified, the default view is BASIC.

**Property Value**  
---  
**Type** | **Description**  
`[InventoryView](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.InventoryView)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
