---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.SetDefaultProcessorVersionRequest
title: Cloud Document AI v1 API - Class SetDefaultProcessorVersionRequest (3.25.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:46:32.377325+00:00
---

# Cloud Document AI v1 API - Class SetDefaultProcessorVersionRequest (3.25.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.SetDefaultProcessorVersionRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Cloud Document AI v1 API - Class SetDefaultProcessorVersionRequest (3.25.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.25.0 (latest)  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.0.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0 
    
    
    public sealed class SetDefaultProcessorVersionRequest : IMessage<SetDefaultProcessorVersionRequest>, IEquatable<SetDefaultProcessorVersionRequest>, IDeepCloneable<SetDefaultProcessorVersionRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the Cloud Document AI v1 API class SetDefaultProcessorVersionRequest.

Request message for the [SetDefaultProcessorVersion][google.cloud.documentai.v1.DocumentProcessorService.SetDefaultProcessorVersion] method.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > SetDefaultProcessorVersionRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[SetDefaultProcessorVersionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.SetDefaultProcessorVersionRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[SetDefaultProcessorVersionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.SetDefaultProcessorVersionRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[SetDefaultProcessorVersionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.SetDefaultProcessorVersionRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.DocumentAI.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1)

## Assembly

Google.Cloud.DocumentAI.V1.dll

## Constructors 

### SetDefaultProcessorVersionRequest()
    
    
    public SetDefaultProcessorVersionRequest()

### SetDefaultProcessorVersionRequest(SetDefaultProcessorVersionRequest)
    
    
    public SetDefaultProcessorVersionRequest(SetDefaultProcessorVersionRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[SetDefaultProcessorVersionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.SetDefaultProcessorVersionRequest)`  
  
  
## Properties 

### DefaultProcessorVersion
    
    
    public string DefaultProcessorVersion { get; set; }

Required. The resource name of child [ProcessorVersion][google.cloud.documentai.v1.ProcessorVersion] to use as default. Format: `projects/{project}/locations/{location}/processors/{processor}/processorVersions/{version}`

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### DefaultProcessorVersionAsProcessorVersionName
    
    
    public ProcessorVersionName DefaultProcessorVersionAsProcessorVersionName { get; set; }

[ProcessorVersionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.ProcessorVersionName)-typed view over the [DefaultProcessorVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.SetDefaultProcessorVersionRequest#Google_Cloud_DocumentAI_V1_SetDefaultProcessorVersionRequest_DefaultProcessorVersion) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[ProcessorVersionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.ProcessorVersionName)` |   
  
### Processor
    
    
    public string Processor { get; set; }

Required. The resource name of the [Processor][google.cloud.documentai.v1.Processor] to change default version.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ProcessorAsProcessorName
    
    
    public ProcessorName ProcessorAsProcessorName { get; set; }

[ProcessorName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.ProcessorName)-typed view over the [Processor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.SetDefaultProcessorVersionRequest#Google_Cloud_DocumentAI_V1_SetDefaultProcessorVersionRequest_Processor) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[ProcessorName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.ProcessorName)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-23 UTC."],[],[]] 
