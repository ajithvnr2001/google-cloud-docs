---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ImportEntityTypesRequest
title: Dialogflow v3 API - Class ImportEntityTypesRequest (3.2.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:30:28.486933+00:00
---

# Dialogflow v3 API - Class ImportEntityTypesRequest (3.2.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ImportEntityTypesRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Dialogflow v3 API - Class ImportEntityTypesRequest (3.2.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.2.0 (latest)  3.1.0  3.0.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0  2.1.0  2.0.0  1.13.0  1.12.0  1.11.0  1.10.0  1.9.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0 
    
    
    public sealed class ImportEntityTypesRequest : IMessage<ImportEntityTypesRequest>, IEquatable<ImportEntityTypesRequest>, IDeepCloneable<ImportEntityTypesRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the Dialogflow v3 API class ImportEntityTypesRequest.

The request message for [EntityTypes.ImportEntityTypes][google.cloud.dialogflow.cx.v3.EntityTypes.ImportEntityTypes].

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ImportEntityTypesRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[ImportEntityTypesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ImportEntityTypesRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[ImportEntityTypesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ImportEntityTypesRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[ImportEntityTypesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ImportEntityTypesRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Dialogflow.Cx.V3](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3)

## Assembly

Google.Cloud.Dialogflow.Cx.V3.dll

## Constructors 

### ImportEntityTypesRequest()
    
    
    public ImportEntityTypesRequest()

### ImportEntityTypesRequest(ImportEntityTypesRequest)
    
    
    public ImportEntityTypesRequest(ImportEntityTypesRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[ImportEntityTypesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ImportEntityTypesRequest)`  
  
  
## Properties 

### EntityTypesCase
    
    
    public ImportEntityTypesRequest.EntityTypesOneofCase EntityTypesCase { get; }

**Property Value**  
---  
**Type** | **Description**  
`[ImportEntityTypesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ImportEntityTypesRequest)[EntityTypesOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ImportEntityTypesRequest.EntityTypesOneofCase)` |   
  
### EntityTypesContent
    
    
    public InlineSource EntityTypesContent { get; set; }

Uncompressed byte content of entity types.

**Property Value**  
---  
**Type** | **Description**  
`[InlineSource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.InlineSource)` |   
  
### EntityTypesUri
    
    
    public string EntityTypesUri { get; set; }

The [Google Cloud Storage](https://cloud.google.com/storage/docs/) URI to import entity types from. The format of this URI must be `gs://<bucket-name>/<object-name>`.

Dialogflow performs a read operation for the Cloud Storage object on the caller's behalf, so your request authentication must have read permissions for the object. For more information, see [Dialogflow access control](https://cloud.google.com/dialogflow/cx/docs/concept/access-control#storage).

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### HasEntityTypesUri
    
    
    public bool HasEntityTypesUri { get; }

Gets whether the "entity_types_uri" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### MergeOption
    
    
    public ImportEntityTypesRequest.Types.MergeOption MergeOption { get; set; }

Required. Merge option for importing entity types.

**Property Value**  
---  
**Type** | **Description**  
`[ImportEntityTypesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ImportEntityTypesRequest)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ImportEntityTypesRequest.Types)[MergeOption](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ImportEntityTypesRequest.Types.MergeOption)` |   
  
### Parent
    
    
    public string Parent { get; set; }

Required. The agent to import the entity types into. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>`.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ParentAsAgentName
    
    
    public AgentName ParentAsAgentName { get; set; }

[AgentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.AgentName)-typed view over the [Parent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ImportEntityTypesRequest#Google_Cloud_Dialogflow_Cx_V3_ImportEntityTypesRequest_Parent) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[AgentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.AgentName)` |   
  
### TargetEntityType
    
    
    public string TargetEntityType { get; set; }

Optional. The target entity type to import into. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/entity_types/<EntityTypeID>`. If set, there should be only one entity type included in [entity_types][google.cloud.dialogflow.cx.v3.ImportEntityTypesRequest.entity_types], of which the type should match the type of the target entity type. All [entities][google.cloud.dialogflow.cx.v3.EntityType.entities] in the imported entity type will be added to the target entity type.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### TargetEntityTypeAsEntityTypeName
    
    
    public EntityTypeName TargetEntityTypeAsEntityTypeName { get; set; }

[EntityTypeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.EntityTypeName)-typed view over the [TargetEntityType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ImportEntityTypesRequest#Google_Cloud_Dialogflow_Cx_V3_ImportEntityTypesRequest_TargetEntityType) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[EntityTypeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.EntityTypeName)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
