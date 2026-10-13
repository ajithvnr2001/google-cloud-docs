---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ContentLocation
title: Google Cloud Data Loss Prevention v2 API - Class ContentLocation (4.27.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:46:45.353487+00:00
---

# Google Cloud Data Loss Prevention v2 API - Class ContentLocation (4.27.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ContentLocation

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Data Loss Prevention v2 API - Class ContentLocation (4.27.0) Stay organized with collections  Save and categorize content based on your preferences. 

4.27.0 (latest)  4.26.0  4.25.0  4.24.0  4.23.0  4.22.0  4.21.0  4.20.0  4.19.0  4.18.0  4.17.0  4.16.0  4.15.0  4.14.0  4.13.0  4.12.0  4.11.0  4.10.0  4.9.0  4.8.0  4.7.0  4.6.0  4.5.0  4.4.0  4.3.0  4.2.0  4.1.0  4.0.0  3.5.0  3.4.0  3.3.0  3.2.0  2.16.0  2.15.0 
    
    
    public sealed class ContentLocation : IMessage<ContentLocation>, IEquatable<ContentLocation>, IDeepCloneable<ContentLocation>, IBufferMessage, IMessage

Reference documentation and code samples for the Google Cloud Data Loss Prevention v2 API class ContentLocation.

Precise location of the finding within a document, record, image, or metadata container.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ContentLocation

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[ContentLocation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ContentLocation), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[ContentLocation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ContentLocation), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[ContentLocation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ContentLocation), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Dlp.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2)

## Assembly

Google.Cloud.Dlp.V2.dll

## Constructors 

### ContentLocation()
    
    
    public ContentLocation()

### ContentLocation(ContentLocation)
    
    
    public ContentLocation(ContentLocation other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[ContentLocation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ContentLocation)`  
  
  
## Properties 

### BatchContentLocation
    
    
    public BatchContentLocation BatchContentLocation { get; set; }

Location within a batch of content.

**Property Value**  
---  
**Type** | **Description**  
`[BatchContentLocation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.BatchContentLocation)` |   
  
### ContainerName
    
    
    public string ContainerName { get; set; }

Name of the container where the finding is located. The top level name is the source file name or table name. Names of some common storage containers are formatted as follows:

  * BigQuery tables: `{project_id}:{dataset_id}.{table_id}`
  * Cloud Storage files: `gs://{bucket}/{path}`
  * Datastore namespace: {namespace}



Nested names could be absent if the embedded object has no string identifier (for example, an image contained within a document).

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ContainerTimestamp
    
    
    public Timestamp ContainerTimestamp { get; set; }

Finding container modification timestamp, if applicable. For Cloud Storage, this field contains the last file modification timestamp. For a BigQuery table, this field contains the last_modified_time property. For Datastore, this field isn't populated.

**Property Value**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html)` |   
  
### ContainerVersion
    
    
    public string ContainerVersion { get; set; }

Finding container version, if available ("generation" for Cloud Storage).

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ConversationLocation
    
    
    public ConversationLocation ConversationLocation { get; set; }

Location within a conversation.

**Property Value**  
---  
**Type** | **Description**  
`[ConversationLocation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ConversationLocation)` |   
  
### DocumentLocation
    
    
    public DocumentLocation DocumentLocation { get; set; }

Location data for document files.

**Property Value**  
---  
**Type** | **Description**  
`[DocumentLocation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DocumentLocation)` |   
  
### ImageLocation
    
    
    public ImageLocation ImageLocation { get; set; }

Location within an image's pixels.

**Property Value**  
---  
**Type** | **Description**  
`[ImageLocation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ImageLocation)` |   
  
### LocationCase
    
    
    public ContentLocation.LocationOneofCase LocationCase { get; }

**Property Value**  
---  
**Type** | **Description**  
`[ContentLocation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ContentLocation)[LocationOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ContentLocation.LocationOneofCase)` |   
  
### MetadataLocation
    
    
    public MetadataLocation MetadataLocation { get; set; }

Location within the metadata for inspected content.

**Property Value**  
---  
**Type** | **Description**  
`[MetadataLocation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.MetadataLocation)` |   
  
### RecordLocation
    
    
    public RecordLocation RecordLocation { get; set; }

Location within a row or record of a database table.

**Property Value**  
---  
**Type** | **Description**  
`[RecordLocation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.RecordLocation)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-01 UTC."],[],[]] 
