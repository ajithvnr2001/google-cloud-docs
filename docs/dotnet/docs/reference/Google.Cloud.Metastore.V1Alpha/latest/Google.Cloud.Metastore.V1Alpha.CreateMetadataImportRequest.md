---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Alpha/latest/Google.Cloud.Metastore.V1Alpha.CreateMetadataImportRequest
title: Dataproc Metastore v1alpha API - Class CreateMetadataImportRequest (2.0.0-alpha12) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:25:26.936503+00:00
---

# Dataproc Metastore v1alpha API - Class CreateMetadataImportRequest (2.0.0-alpha12)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Alpha/latest/Google.Cloud.Metastore.V1Alpha.CreateMetadataImportRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Dataproc Metastore v1alpha API - Class CreateMetadataImportRequest (2.0.0-alpha12) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.0.0-alpha12 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Alpha/latest/Google.Cloud.Metastore.V1Alpha.CreateMetadataImportRequest)
  * [ 2.0.0-alpha11 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Alpha/2.0.0-alpha11/Google.Cloud.Metastore.V1Alpha.CreateMetadataImportRequest)
  * [ 1.0.0-alpha04 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Alpha/1.0.0-alpha04/Google.Cloud.Metastore.V1Alpha.CreateMetadataImportRequest)


    
    
    public sealed class CreateMetadataImportRequest : IMessage<CreateMetadataImportRequest>, IEquatable<CreateMetadataImportRequest>, IDeepCloneable<CreateMetadataImportRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the Dataproc Metastore v1alpha API class CreateMetadataImportRequest.

Request message for [DataprocMetastore.CreateMetadataImport][google.cloud.metastore.v1alpha.DataprocMetastore.CreateMetadataImport].

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > CreateMetadataImportRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[CreateMetadataImportRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Alpha/latest/Google.Cloud.Metastore.V1Alpha.CreateMetadataImportRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[CreateMetadataImportRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Alpha/latest/Google.Cloud.Metastore.V1Alpha.CreateMetadataImportRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[CreateMetadataImportRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Alpha/latest/Google.Cloud.Metastore.V1Alpha.CreateMetadataImportRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Metastore.V1Alpha](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Alpha/latest/Google.Cloud.Metastore.V1Alpha)

## Assembly

Google.Cloud.Metastore.V1Alpha.dll

## Constructors 

### CreateMetadataImportRequest()
    
    
    public CreateMetadataImportRequest()

### CreateMetadataImportRequest(CreateMetadataImportRequest)
    
    
    public CreateMetadataImportRequest(CreateMetadataImportRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[CreateMetadataImportRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Alpha/latest/Google.Cloud.Metastore.V1Alpha.CreateMetadataImportRequest)`  
  
  
## Properties 

### MetadataImport
    
    
    public MetadataImport MetadataImport { get; set; }

Required. The metadata import to create. The `name` field is ignored. The ID of the created metadata import must be provided in the request's `metadata_import_id` field.

**Property Value**  
---  
**Type** | **Description**  
`[MetadataImport](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Alpha/latest/Google.Cloud.Metastore.V1Alpha.MetadataImport)` |   
  
### MetadataImportId
    
    
    public string MetadataImportId { get; set; }

Required. The ID of the metadata import, which is used as the final component of the metadata import's name.

This value must be between 1 and 64 characters long, begin with a letter, end with a letter or number, and consist of alpha-numeric ASCII characters or hyphens.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Parent
    
    
    public string Parent { get; set; }

Required. The relative resource name of the service in which to create a metastore import, in the following form:

`projects/{project_number}/locations/{location_id}/services/{service_id}`.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ParentAsServiceName
    
    
    public ServiceName ParentAsServiceName { get; set; }

[ServiceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Alpha/latest/Google.Cloud.Metastore.V1Alpha.ServiceName)-typed view over the [Parent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Alpha/latest/Google.Cloud.Metastore.V1Alpha.CreateMetadataImportRequest#Google_Cloud_Metastore_V1Alpha_CreateMetadataImportRequest_Parent) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[ServiceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Alpha/latest/Google.Cloud.Metastore.V1Alpha.ServiceName)` |   
  
### RequestId
    
    
    public string RequestId { get; set; }

Optional. A request ID. Specify a unique request ID to allow the server to ignore the request if it has completed. The server will ignore subsequent requests that provide a duplicate request ID for at least 60 minutes after the first request.

For example, if an initial request times out, followed by another request with the same request ID, the server ignores the second request to prevent the creation of duplicate commitments.

The request ID must be a valid [UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier#Format) A zero UUID (00000000-0000-0000-0000-000000000000) is not supported.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
