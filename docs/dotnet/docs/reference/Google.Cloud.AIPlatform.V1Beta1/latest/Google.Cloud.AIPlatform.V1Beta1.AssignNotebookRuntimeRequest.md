---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.AssignNotebookRuntimeRequest
title: Vertex AI v1beta1 API - Class AssignNotebookRuntimeRequest (1.0.0-beta87) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:30:25.224602+00:00
---

# Vertex AI v1beta1 API - Class AssignNotebookRuntimeRequest (1.0.0-beta87)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.AssignNotebookRuntimeRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Vertex AI v1beta1 API - Class AssignNotebookRuntimeRequest (1.0.0-beta87) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta87 (latest)  1.0.0-beta86 
    
    
    public sealed class AssignNotebookRuntimeRequest : IMessage<AssignNotebookRuntimeRequest>, IEquatable<AssignNotebookRuntimeRequest>, IDeepCloneable<AssignNotebookRuntimeRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the Vertex AI v1beta1 API class AssignNotebookRuntimeRequest.

Request message for [NotebookService.AssignNotebookRuntime][google.cloud.aiplatform.v1beta1.NotebookService.AssignNotebookRuntime].

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > AssignNotebookRuntimeRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[AssignNotebookRuntimeRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.AssignNotebookRuntimeRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[AssignNotebookRuntimeRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.AssignNotebookRuntimeRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[AssignNotebookRuntimeRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.AssignNotebookRuntimeRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.AIPlatform.V1Beta1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1)

## Assembly

Google.Cloud.AIPlatform.V1Beta1.dll

## Constructors 

### AssignNotebookRuntimeRequest()
    
    
    public AssignNotebookRuntimeRequest()

### AssignNotebookRuntimeRequest(AssignNotebookRuntimeRequest)
    
    
    public AssignNotebookRuntimeRequest(AssignNotebookRuntimeRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[AssignNotebookRuntimeRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.AssignNotebookRuntimeRequest)`  
  
  
## Properties 

### NotebookRuntime
    
    
    public NotebookRuntime NotebookRuntime { get; set; }

Required. Provide runtime specific information (e.g. runtime owner, notebook id) used for NotebookRuntime assignment.

**Property Value**  
---  
**Type** | **Description**  
`[NotebookRuntime](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.NotebookRuntime)` |   
  
### NotebookRuntimeId
    
    
    public string NotebookRuntimeId { get; set; }

Optional. User specified ID for the notebook runtime.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### NotebookRuntimeTemplate
    
    
    public string NotebookRuntimeTemplate { get; set; }

Required. The resource name of the NotebookRuntimeTemplate based on which a NotebookRuntime will be assigned (reuse or create a new one).

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### NotebookRuntimeTemplateAsNotebookRuntimeTemplateName
    
    
    public NotebookRuntimeTemplateName NotebookRuntimeTemplateAsNotebookRuntimeTemplateName { get; set; }

[NotebookRuntimeTemplateName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.NotebookRuntimeTemplateName)-typed view over the [NotebookRuntimeTemplate](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.AssignNotebookRuntimeRequest#Google_Cloud_AIPlatform_V1Beta1_AssignNotebookRuntimeRequest_NotebookRuntimeTemplate) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[NotebookRuntimeTemplateName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.NotebookRuntimeTemplateName)` |   
  
### Parent
    
    
    public string Parent { get; set; }

Required. The resource name of the Location to get the NotebookRuntime assignment. Format: `projects/{project}/locations/{location}`

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ParentAsLocationName
    
    
    public LocationName ParentAsLocationName { get; set; }

[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)-typed view over the [Parent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.AssignNotebookRuntimeRequest#Google_Cloud_AIPlatform_V1Beta1_AssignNotebookRuntimeRequest_Parent) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
