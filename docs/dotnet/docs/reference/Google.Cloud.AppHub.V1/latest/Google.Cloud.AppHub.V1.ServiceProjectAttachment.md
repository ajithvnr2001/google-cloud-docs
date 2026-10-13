---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.ServiceProjectAttachment
title: App Hub v1 API - Class ServiceProjectAttachment (1.3.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:05:15.594682+00:00
---

# App Hub v1 API - Class ServiceProjectAttachment (1.3.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.ServiceProjectAttachment

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  App Hub v1 API - Class ServiceProjectAttachment (1.3.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.3.0 (latest)  1.2.0  1.1.0  1.0.0 
    
    
    public sealed class ServiceProjectAttachment : IMessage<ServiceProjectAttachment>, IEquatable<ServiceProjectAttachment>, IDeepCloneable<ServiceProjectAttachment>, IBufferMessage, IMessage

Reference documentation and code samples for the App Hub v1 API class ServiceProjectAttachment.

ServiceProjectAttachment represents an attachment from a service project to a host project. Service projects contain the underlying cloud infrastructure resources, and expose these resources to the host project through a ServiceProjectAttachment. With the attachments, the host project can provide an aggregated view of resources across all service projects.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ServiceProjectAttachment

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[ServiceProjectAttachment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.ServiceProjectAttachment), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[ServiceProjectAttachment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.ServiceProjectAttachment), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[ServiceProjectAttachment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.ServiceProjectAttachment), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.AppHub.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1)

## Assembly

Google.Cloud.AppHub.V1.dll

## Constructors 

### ServiceProjectAttachment()
    
    
    public ServiceProjectAttachment()

### ServiceProjectAttachment(ServiceProjectAttachment)
    
    
    public ServiceProjectAttachment(ServiceProjectAttachment other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[ServiceProjectAttachment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.ServiceProjectAttachment)`  
  
  
## Properties 

### CreateTime
    
    
    public Timestamp CreateTime { get; set; }

Output only. Create time.

**Property Value**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html)` |   
  
### Name
    
    
    public string Name { get; set; }

Identifier. The resource name of a ServiceProjectAttachment. Format: `"projects/{host-project-id}/locations/global/serviceProjectAttachments/{service-project-id}."`

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ServiceProject
    
    
    public string ServiceProject { get; set; }

Required. Immutable. Service project name in the format: `"projects/abc"` or `"projects/123"`. As input, project name with either project id or number are accepted. As output, this field will contain project number.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ServiceProjectAsProjectName
    
    
    public ProjectName ServiceProjectAsProjectName { get; set; }

[ProjectName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.ProjectName.html)-typed view over the [ServiceProject](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.ServiceProjectAttachment#Google_Cloud_AppHub_V1_ServiceProjectAttachment_ServiceProject) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[ProjectName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.ProjectName.html)` |   
  
### ServiceProjectAttachmentName
    
    
    public ServiceProjectAttachmentName ServiceProjectAttachmentName { get; set; }

[ServiceProjectAttachmentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.ServiceProjectAttachmentName)-typed view over the [Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.ServiceProjectAttachment#Google_Cloud_AppHub_V1_ServiceProjectAttachment_Name) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[ServiceProjectAttachmentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.ServiceProjectAttachmentName)` |   
  
### State
    
    
    public ServiceProjectAttachment.Types.State State { get; set; }

Output only. ServiceProjectAttachment state.

**Property Value**  
---  
**Type** | **Description**  
`[ServiceProjectAttachment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.ServiceProjectAttachment)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.ServiceProjectAttachment.Types)[State](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.ServiceProjectAttachment.Types.State)` |   
  
### Uid
    
    
    public string Uid { get; set; }

Output only. A globally unique identifier (in UUID4 format) for the `ServiceProjectAttachment`.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
