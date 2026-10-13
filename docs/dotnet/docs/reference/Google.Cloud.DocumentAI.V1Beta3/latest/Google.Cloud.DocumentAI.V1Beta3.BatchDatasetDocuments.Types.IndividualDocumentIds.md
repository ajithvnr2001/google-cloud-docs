---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1Beta3/latest/Google.Cloud.DocumentAI.V1Beta3.BatchDatasetDocuments.Types.IndividualDocumentIds
title: Cloud Document AI v1beta3 API - Class BatchDatasetDocuments.Types.IndividualDocumentIds (2.0.0-beta30) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:19:01.808798+00:00
---

# Cloud Document AI v1beta3 API - Class BatchDatasetDocuments.Types.IndividualDocumentIds (2.0.0-beta30)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1Beta3/latest/Google.Cloud.DocumentAI.V1Beta3.BatchDatasetDocuments.Types.IndividualDocumentIds

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Cloud Document AI v1beta3 API - Class BatchDatasetDocuments.Types.IndividualDocumentIds (2.0.0-beta30) Stay organized with collections  Save and categorize content based on your preferences. 

2.0.0-beta30 (latest)  2.0.0-beta29  1.0.0-beta04 
    
    
    public sealed class BatchDatasetDocuments.Types.IndividualDocumentIds : IMessage<BatchDatasetDocuments.Types.IndividualDocumentIds>, IEquatable<BatchDatasetDocuments.Types.IndividualDocumentIds>, IDeepCloneable<BatchDatasetDocuments.Types.IndividualDocumentIds>, IBufferMessage, IMessage

Reference documentation and code samples for the Cloud Document AI v1beta3 API class BatchDatasetDocuments.Types.IndividualDocumentIds.

List of individual DocumentIds.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > BatchDatasetDocuments.Types.IndividualDocumentIds

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[BatchDatasetDocuments](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1Beta3/latest/Google.Cloud.DocumentAI.V1Beta3.BatchDatasetDocuments)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1Beta3/latest/Google.Cloud.DocumentAI.V1Beta3.BatchDatasetDocuments.Types)[IndividualDocumentIds](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1Beta3/latest/Google.Cloud.DocumentAI.V1Beta3.BatchDatasetDocuments.Types.IndividualDocumentIds), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[BatchDatasetDocuments](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1Beta3/latest/Google.Cloud.DocumentAI.V1Beta3.BatchDatasetDocuments)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1Beta3/latest/Google.Cloud.DocumentAI.V1Beta3.BatchDatasetDocuments.Types)[IndividualDocumentIds](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1Beta3/latest/Google.Cloud.DocumentAI.V1Beta3.BatchDatasetDocuments.Types.IndividualDocumentIds), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[BatchDatasetDocuments](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1Beta3/latest/Google.Cloud.DocumentAI.V1Beta3.BatchDatasetDocuments)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1Beta3/latest/Google.Cloud.DocumentAI.V1Beta3.BatchDatasetDocuments.Types)[IndividualDocumentIds](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1Beta3/latest/Google.Cloud.DocumentAI.V1Beta3.BatchDatasetDocuments.Types.IndividualDocumentIds), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.DocumentAI.V1Beta3](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1Beta3/latest/Google.Cloud.DocumentAI.V1Beta3)

## Assembly

Google.Cloud.DocumentAI.V1Beta3.dll

## Constructors 

### IndividualDocumentIds()
    
    
    public IndividualDocumentIds()

### IndividualDocumentIds(IndividualDocumentIds)
    
    
    public IndividualDocumentIds(BatchDatasetDocuments.Types.IndividualDocumentIds other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[BatchDatasetDocuments](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1Beta3/latest/Google.Cloud.DocumentAI.V1Beta3.BatchDatasetDocuments)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1Beta3/latest/Google.Cloud.DocumentAI.V1Beta3.BatchDatasetDocuments.Types)[IndividualDocumentIds](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1Beta3/latest/Google.Cloud.DocumentAI.V1Beta3.BatchDatasetDocuments.Types.IndividualDocumentIds)`  
  
  
## Properties 

### DocumentIds
    
    
    public RepeatedField<DocumentId> DocumentIds { get; }

Required. List of Document IDs indicating where the actual documents are stored.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[DocumentId](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1Beta3/latest/Google.Cloud.DocumentAI.V1Beta3.DocumentId)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-16 UTC."],[],[]] 
