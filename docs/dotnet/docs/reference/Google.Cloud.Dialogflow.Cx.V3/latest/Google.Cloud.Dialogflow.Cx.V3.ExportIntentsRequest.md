---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ExportIntentsRequest
title: Dialogflow v3 API - Class ExportIntentsRequest (3.2.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:34:51.130374+00:00
---

# Dialogflow v3 API - Class ExportIntentsRequest (3.2.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ExportIntentsRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Dialogflow v3 API - Class ExportIntentsRequest (3.2.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.2.0 (latest)  3.1.0  3.0.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0  2.1.0  2.0.0  1.13.0  1.12.0  1.11.0  1.10.0  1.9.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0 
    
    
    public sealed class ExportIntentsRequest : IMessage<ExportIntentsRequest>, IEquatable<ExportIntentsRequest>, IDeepCloneable<ExportIntentsRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the Dialogflow v3 API class ExportIntentsRequest.

The request message for [Intents.ExportIntents][google.cloud.dialogflow.cx.v3.Intents.ExportIntents].

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ExportIntentsRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[ExportIntentsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ExportIntentsRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[ExportIntentsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ExportIntentsRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[ExportIntentsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ExportIntentsRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Dialogflow.Cx.V3](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3)

## Assembly

Google.Cloud.Dialogflow.Cx.V3.dll

## Constructors 

### ExportIntentsRequest()
    
    
    public ExportIntentsRequest()

### ExportIntentsRequest(ExportIntentsRequest)
    
    
    public ExportIntentsRequest(ExportIntentsRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[ExportIntentsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ExportIntentsRequest)`  
  
  
## Properties 

### DataFormat
    
    
    public ExportIntentsRequest.Types.DataFormat DataFormat { get; set; }

Optional. The data format of the exported intents. If not specified, `BLOB` is assumed.

**Property Value**  
---  
**Type** | **Description**  
`[ExportIntentsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ExportIntentsRequest)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ExportIntentsRequest.Types)[DataFormat](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ExportIntentsRequest.Types.DataFormat)` |   
  
### DestinationCase
    
    
    public ExportIntentsRequest.DestinationOneofCase DestinationCase { get; }

**Property Value**  
---  
**Type** | **Description**  
`[ExportIntentsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ExportIntentsRequest)[DestinationOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ExportIntentsRequest.DestinationOneofCase)` |   
  
### HasIntentsContentInline
    
    
    public bool HasIntentsContentInline { get; }

Gets whether the "intents_content_inline" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasIntentsUri
    
    
    public bool HasIntentsUri { get; }

Gets whether the "intents_uri" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### Intents
    
    
    public RepeatedField<string> Intents { get; }

Required. The name of the intents to export. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/intents/<IntentID>`.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### IntentsContentInline
    
    
    public bool IntentsContentInline { get; set; }

Optional. The option to return the serialized intents inline.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### IntentsUri
    
    
    public string IntentsUri { get; set; }

Optional. The [Google Cloud Storage](https://cloud.google.com/storage/docs/) URI to export the intents to. The format of this URI must be `gs://<bucket-name>/<object-name>`.

Dialogflow performs a write operation for the Cloud Storage object on the caller's behalf, so your request authentication must have write permissions for the object. For more information, see [Dialogflow access control](https://cloud.google.com/dialogflow/cx/docs/concept/access-control#storage).

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Parent
    
    
    public string Parent { get; set; }

Required. The name of the parent agent to export intents. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>`.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ParentAsAgentName
    
    
    public AgentName ParentAsAgentName { get; set; }

[AgentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.AgentName)-typed view over the [Parent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ExportIntentsRequest#Google_Cloud_Dialogflow_Cx_V3_ExportIntentsRequest_Parent) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[AgentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.AgentName)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
