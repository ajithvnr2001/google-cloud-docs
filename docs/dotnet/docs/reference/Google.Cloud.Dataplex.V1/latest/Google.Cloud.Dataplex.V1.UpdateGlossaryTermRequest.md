---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.UpdateGlossaryTermRequest
title: Cloud Dataplex v1 API - Class UpdateGlossaryTermRequest (3.15.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:39:07.857782+00:00
---

# Cloud Dataplex v1 API - Class UpdateGlossaryTermRequest (3.15.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.UpdateGlossaryTermRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Cloud Dataplex v1 API - Class UpdateGlossaryTermRequest (3.15.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.15.0 (latest)  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0  2.1.0  2.0.0  1.0.0 
    
    
    public sealed class UpdateGlossaryTermRequest : IMessage<UpdateGlossaryTermRequest>, IEquatable<UpdateGlossaryTermRequest>, IDeepCloneable<UpdateGlossaryTermRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the Cloud Dataplex v1 API class UpdateGlossaryTermRequest.

Update GlossaryTerm Request

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > UpdateGlossaryTermRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[UpdateGlossaryTermRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.UpdateGlossaryTermRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[UpdateGlossaryTermRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.UpdateGlossaryTermRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[UpdateGlossaryTermRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.UpdateGlossaryTermRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Dataplex.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1)

## Assembly

Google.Cloud.Dataplex.V1.dll

## Constructors 

### UpdateGlossaryTermRequest()
    
    
    public UpdateGlossaryTermRequest()

### UpdateGlossaryTermRequest(UpdateGlossaryTermRequest)
    
    
    public UpdateGlossaryTermRequest(UpdateGlossaryTermRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[UpdateGlossaryTermRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.UpdateGlossaryTermRequest)`  
  
  
## Properties 

### Term
    
    
    public GlossaryTerm Term { get; set; }

Required. The GlossaryTerm to update. The GlossaryTerm's `name` field is used to identify the GlossaryTerm to update. Format: projects/{project_id_or_number}/locations/{location_id}/glossaries/{glossary_id}/terms/{term_id}

**Property Value**  
---  
**Type** | **Description**  
`[GlossaryTerm](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.GlossaryTerm)` |   
  
### UpdateMask
    
    
    public FieldMask UpdateMask { get; set; }

Required. The list of fields to update.

**Property Value**  
---  
**Type** | **Description**  
`[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-30 UTC."],[],[]] 
