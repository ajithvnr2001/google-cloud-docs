---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.BatchUpdateEntityTypesRequest
title: Google Cloud Dialogflow v2 API - Class BatchUpdateEntityTypesRequest (4.33.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:58:11.533150+00:00
---

# Google Cloud Dialogflow v2 API - Class BatchUpdateEntityTypesRequest (4.33.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.BatchUpdateEntityTypesRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Dialogflow v2 API - Class BatchUpdateEntityTypesRequest (4.33.0) Stay organized with collections  Save and categorize content based on your preferences. 

4.33.0 (latest)  4.32.0  4.31.0  4.30.0  4.29.0  4.28.0  4.27.0  4.26.0  4.25.0  4.24.0  4.23.0  4.22.0  4.21.0  4.20.0  4.19.0  4.18.0  4.17.0  4.16.0  4.15.0  4.14.0  4.13.0  4.12.0  4.11.0  4.10.0  4.9.0  4.8.0  4.7.0  4.6.0  4.5.0  4.4.0  4.3.0  4.2.0  4.1.0  4.0.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0 
    
    
    public sealed class BatchUpdateEntityTypesRequest : IMessage<BatchUpdateEntityTypesRequest>, IEquatable<BatchUpdateEntityTypesRequest>, IDeepCloneable<BatchUpdateEntityTypesRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the Google Cloud Dialogflow v2 API class BatchUpdateEntityTypesRequest.

The request message for [EntityTypes.BatchUpdateEntityTypes][google.cloud.dialogflow.v2.EntityTypes.BatchUpdateEntityTypes].

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > BatchUpdateEntityTypesRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[BatchUpdateEntityTypesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.BatchUpdateEntityTypesRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[BatchUpdateEntityTypesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.BatchUpdateEntityTypesRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[BatchUpdateEntityTypesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.BatchUpdateEntityTypesRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Dialogflow.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2)

## Assembly

Google.Cloud.Dialogflow.V2.dll

## Constructors 

### BatchUpdateEntityTypesRequest()
    
    
    public BatchUpdateEntityTypesRequest()

### BatchUpdateEntityTypesRequest(BatchUpdateEntityTypesRequest)
    
    
    public BatchUpdateEntityTypesRequest(BatchUpdateEntityTypesRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[BatchUpdateEntityTypesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.BatchUpdateEntityTypesRequest)`  
  
  
## Properties 

### EntityTypeBatchCase
    
    
    public BatchUpdateEntityTypesRequest.EntityTypeBatchOneofCase EntityTypeBatchCase { get; }

**Property Value**  
---  
**Type** | **Description**  
`[BatchUpdateEntityTypesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.BatchUpdateEntityTypesRequest)[EntityTypeBatchOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.BatchUpdateEntityTypesRequest.EntityTypeBatchOneofCase)` |   
  
### EntityTypeBatchInline
    
    
    public EntityTypeBatch EntityTypeBatchInline { get; set; }

The collection of entity types to update or create.

**Property Value**  
---  
**Type** | **Description**  
`[EntityTypeBatch](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.EntityTypeBatch)` |   
  
### EntityTypeBatchUri
    
    
    public string EntityTypeBatchUri { get; set; }

The URI to a Google Cloud Storage file containing entity types to update or create. The file format can either be a serialized proto (of EntityBatch type) or a JSON object. Note: The URI must start with "gs://".

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### HasEntityTypeBatchUri
    
    
    public bool HasEntityTypeBatchUri { get; }

Gets whether the "entity_type_batch_uri" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### LanguageCode
    
    
    public string LanguageCode { get; set; }

Optional. The language used to access language-specific data. If not specified, the agent's default language is used. For more information, see [Multilingual intent and entity data](https://cloud.google.com/dialogflow/docs/agents-multilingual#intent-entity).

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Parent
    
    
    public string Parent { get; set; }

Required. The name of the agent to update or create entity types in. Format: `projects/<Project ID>/agent`.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ParentAsAgentName
    
    
    public AgentName ParentAsAgentName { get; set; }

[AgentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.AgentName)-typed view over the [Parent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.BatchUpdateEntityTypesRequest#Google_Cloud_Dialogflow_V2_BatchUpdateEntityTypesRequest_Parent) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[AgentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.AgentName)` |   
  
### UpdateMask
    
    
    public FieldMask UpdateMask { get; set; }

Optional. The mask to control which fields get updated.

**Property Value**  
---  
**Type** | **Description**  
`[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
