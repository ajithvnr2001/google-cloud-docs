---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.CreateToolRequest
title: Gemini Enterprise for Customer Experience v1beta API - Class CreateToolRequest (1.0.0-beta09) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:40:03.866752+00:00
---

# Gemini Enterprise for Customer Experience v1beta API - Class CreateToolRequest (1.0.0-beta09)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.CreateToolRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Gemini Enterprise for Customer Experience v1beta API - Class CreateToolRequest (1.0.0-beta09) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta09 (latest)  1.0.0-beta08 
    
    
    public sealed class CreateToolRequest : IMessage<CreateToolRequest>, IEquatable<CreateToolRequest>, IDeepCloneable<CreateToolRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the Gemini Enterprise for Customer Experience v1beta API class CreateToolRequest.

Request message for [AgentService.CreateTool][google.cloud.ces.v1beta.AgentService.CreateTool].

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > CreateToolRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[CreateToolRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.CreateToolRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[CreateToolRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.CreateToolRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[CreateToolRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.CreateToolRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Ces.V1Beta](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta)

## Assembly

Google.Cloud.Ces.V1Beta.dll

## Constructors 

### CreateToolRequest()
    
    
    public CreateToolRequest()

### CreateToolRequest(CreateToolRequest)
    
    
    public CreateToolRequest(CreateToolRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[CreateToolRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.CreateToolRequest)`  
  
  
## Properties 

### Parent
    
    
    public string Parent { get; set; }

Required. The resource name of the app to create a tool in.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ParentAsAppName
    
    
    public AppName ParentAsAppName { get; set; }

[AppName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AppName)-typed view over the [Parent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.CreateToolRequest#Google_Cloud_Ces_V1Beta_CreateToolRequest_Parent) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[AppName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AppName)` |   
  
### Tool
    
    
    public Tool Tool { get; set; }

Required. The tool to create.

**Property Value**  
---  
**Type** | **Description**  
`[Tool](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Tool)` |   
  
### ToolId
    
    
    public string ToolId { get; set; }

Optional. The ID to use for the tool, which will become the final component of the tool's resource name. If not provided, a unique ID will be automatically assigned for the tool.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-14 UTC."],[],[]] 
