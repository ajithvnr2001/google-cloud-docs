---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.ChangeRequest
title: Cloud Dataplex v1 API - Class ChangeRequest (3.15.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:46:44.761687+00:00
---

# Cloud Dataplex v1 API - Class ChangeRequest (3.15.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.ChangeRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Cloud Dataplex v1 API - Class ChangeRequest (3.15.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.15.0 (latest)  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0  2.1.0  2.0.0  1.0.0 
    
    
    public sealed class ChangeRequest : IMessage<ChangeRequest>, IEquatable<ChangeRequest>, IDeepCloneable<ChangeRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the Cloud Dataplex v1 API class ChangeRequest.

Represents a proposed change to a metadata resource.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ChangeRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[ChangeRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.ChangeRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[ChangeRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.ChangeRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[ChangeRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.ChangeRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Dataplex.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1)

## Assembly

Google.Cloud.Dataplex.V1.dll

## Constructors 

### ChangeRequest()
    
    
    public ChangeRequest()

### ChangeRequest(ChangeRequest)
    
    
    public ChangeRequest(ChangeRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[ChangeRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.ChangeRequest)`  
  
  
## Properties 

### Approver
    
    
    public string Approver { get; set; }

Output only. The email address of the user who approved/rejected the ChangeRequest.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Author
    
    
    public string Author { get; set; }

Output only. The email address of the user who created the ChangeRequest.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ChangePayloadCase
    
    
    public ChangeRequest.ChangePayloadOneofCase ChangePayloadCase { get; }

**Property Value**  
---  
**Type** | **Description**  
`[ChangeRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.ChangeRequest)[ChangePayloadOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.ChangeRequest.ChangePayloadOneofCase)` |   
  
### ChangeRequestName
    
    
    public ChangeRequestName ChangeRequestName { get; set; }

[ChangeRequestName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.ChangeRequestName)-typed view over the [Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.ChangeRequest#Google_Cloud_Dataplex_V1_ChangeRequest_Name) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[ChangeRequestName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.ChangeRequestName)` |   
  
### ChangeType
    
    
    public ChangeRequest.Types.ChangeType ChangeType { get; set; }

Output only. The type of change represented by the change_payload. This field is derived from the populated field in the change_payload oneof.

**Property Value**  
---  
**Type** | **Description**  
`[ChangeRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.ChangeRequest)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.ChangeRequest.Types)[ChangeType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.ChangeRequest.Types.ChangeType)` |   
  
### CreateEntry
    
    
    public CreateEntryRequest CreateEntry { get; set; }

Payload for creating an Entry.

**Property Value**  
---  
**Type** | **Description**  
`[CreateEntryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.CreateEntryRequest)` |   
  
### CreateEntryLink
    
    
    public CreateEntryLinkRequest CreateEntryLink { get; set; }

Payload for creating an EntryLink.

**Property Value**  
---  
**Type** | **Description**  
`[CreateEntryLinkRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.CreateEntryLinkRequest)` |   
  
### CreateGlossary
    
    
    public CreateGlossaryRequest CreateGlossary { get; set; }

Payload for creating a Glossary.

**Property Value**  
---  
**Type** | **Description**  
`[CreateGlossaryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.CreateGlossaryRequest)` |   
  
### CreateGlossaryCategory
    
    
    public CreateGlossaryCategoryRequest CreateGlossaryCategory { get; set; }

Payload for creating a GlossaryCategory.

**Property Value**  
---  
**Type** | **Description**  
`[CreateGlossaryCategoryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.CreateGlossaryCategoryRequest)` |   
  
### CreateGlossaryTerm
    
    
    public CreateGlossaryTermRequest CreateGlossaryTerm { get; set; }

Payload for creating a GlossaryTerm.

**Property Value**  
---  
**Type** | **Description**  
`[CreateGlossaryTermRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.CreateGlossaryTermRequest)` |   
  
### CreateTime
    
    
    public Timestamp CreateTime { get; set; }

Output only. The time when the ChangeRequest was created.

**Property Value**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html)` |   
  
### DataProductAccessRequest
    
    
    public DataProductAccessRequest DataProductAccessRequest { get; set; }

Payload for Data Product access request.

**Property Value**  
---  
**Type** | **Description**  
`[DataProductAccessRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataProductAccessRequest)` |   
  
### DeleteEntry
    
    
    public DeleteEntryRequest DeleteEntry { get; set; }

Payload for deleting an Entry.

**Property Value**  
---  
**Type** | **Description**  
`[DeleteEntryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DeleteEntryRequest)` |   
  
### DeleteEntryLink
    
    
    public DeleteEntryLinkRequest DeleteEntryLink { get; set; }

Payload for deleting an EntryLink.

**Property Value**  
---  
**Type** | **Description**  
`[DeleteEntryLinkRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DeleteEntryLinkRequest)` |   
  
### DeleteGlossary
    
    
    public DeleteGlossaryRequest DeleteGlossary { get; set; }

Payload for deleting a Glossary.

**Property Value**  
---  
**Type** | **Description**  
`[DeleteGlossaryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DeleteGlossaryRequest)` |   
  
### DeleteGlossaryCategory
    
    
    public DeleteGlossaryCategoryRequest DeleteGlossaryCategory { get; set; }

Payload for deleting a GlossaryCategory.

**Property Value**  
---  
**Type** | **Description**  
`[DeleteGlossaryCategoryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DeleteGlossaryCategoryRequest)` |   
  
### DeleteGlossaryTerm
    
    
    public DeleteGlossaryTermRequest DeleteGlossaryTerm { get; set; }

Payload for deleting a GlossaryTerm.

**Property Value**  
---  
**Type** | **Description**  
`[DeleteGlossaryTermRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DeleteGlossaryTermRequest)` |   
  
### Etag
    
    
    public string Etag { get; set; }

Optional. This checksum is computed by the service. It can be sent on update and delete requests to ensure the client has an up-to-date value before proceeding.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Justification
    
    
    public string Justification { get; set; }

Optional. Justification of the ChangeRequest. This should explain _why_ the change is needed or why it should be approved.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Labels
    
    
    public MapField<string, string> Labels { get; }

Optional. User-defined labels for the ChangeRequest.

**Property Value**  
---  
**Type** | **Description**  
`[MapField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.MapField-2.html)[string](https://learn.microsoft.com/dotnet/api/system.string)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Name
    
    
    public string Name { get; set; }

Identifier. The relative resource name of the ChangeRequest, of the form: projects/{project_number}/locations/{location_id}/changeRequests/{change_request_id}

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### RejectionComment
    
    
    public string RejectionComment { get; set; }

Output only. The reason provided for rejecting the ChangeRequest.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Resource
    
    
    public string Resource { get; set; }

Output only. The full resource name of the target resource to be modified. Example: //dataplex.googleapis.com/projects/my-project/locations/us-central1/entryGroups/my-group/entries/my-entry

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ResourceAsResourceName
    
    
    public IResourceName ResourceAsResourceName { get; set; }

[IResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.IResourceName.html)-typed view over the [Resource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.ChangeRequest#Google_Cloud_Dataplex_V1_ChangeRequest_Resource) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[IResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.IResourceName.html)` |   
  
### State
    
    
    public ChangeRequest.Types.State State { get; set; }

Output only. The current state of the ChangeRequest.

**Property Value**  
---  
**Type** | **Description**  
`[ChangeRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.ChangeRequest)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.ChangeRequest.Types)[State](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.ChangeRequest.Types.State)` |   
  
### Uid
    
    
    public string Uid { get; set; }

Output only. System generated globally unique ID for the ChangeRequest.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### UpdateEntry
    
    
    public UpdateEntryRequest UpdateEntry { get; set; }

Payload for updating an Entry.

**Property Value**  
---  
**Type** | **Description**  
`[UpdateEntryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.UpdateEntryRequest)` |   
  
### UpdateGlossary
    
    
    public UpdateGlossaryRequest UpdateGlossary { get; set; }

Payload for updating a Glossary.

**Property Value**  
---  
**Type** | **Description**  
`[UpdateGlossaryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.UpdateGlossaryRequest)` |   
  
### UpdateGlossaryCategory
    
    
    public UpdateGlossaryCategoryRequest UpdateGlossaryCategory { get; set; }

Payload for updating a GlossaryCategory.

**Property Value**  
---  
**Type** | **Description**  
`[UpdateGlossaryCategoryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.UpdateGlossaryCategoryRequest)` |   
  
### UpdateGlossaryTerm
    
    
    public UpdateGlossaryTermRequest UpdateGlossaryTerm { get; set; }

Payload for updating a GlossaryTerm.

**Property Value**  
---  
**Type** | **Description**  
`[UpdateGlossaryTermRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.UpdateGlossaryTermRequest)` |   
  
### UpdateTime
    
    
    public Timestamp UpdateTime { get; set; }

Output only. The time when the ChangeRequest was last updated.

**Property Value**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-30 UTC."],[],[]] 
