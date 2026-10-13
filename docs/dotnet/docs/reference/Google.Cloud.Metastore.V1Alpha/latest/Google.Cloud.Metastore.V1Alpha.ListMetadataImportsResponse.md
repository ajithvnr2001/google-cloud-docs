---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Alpha/latest/Google.Cloud.Metastore.V1Alpha.ListMetadataImportsResponse
title: Dataproc Metastore v1alpha API - Class ListMetadataImportsResponse (2.0.0-alpha12) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:54:19.059177+00:00
---

# Dataproc Metastore v1alpha API - Class ListMetadataImportsResponse (2.0.0-alpha12)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Alpha/latest/Google.Cloud.Metastore.V1Alpha.ListMetadataImportsResponse

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Dataproc Metastore v1alpha API - Class ListMetadataImportsResponse (2.0.0-alpha12) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.0.0-alpha12 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Alpha/latest/Google.Cloud.Metastore.V1Alpha.ListMetadataImportsResponse)
  * [ 2.0.0-alpha11 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Alpha/2.0.0-alpha11/Google.Cloud.Metastore.V1Alpha.ListMetadataImportsResponse)
  * [ 1.0.0-alpha04 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Alpha/1.0.0-alpha04/Google.Cloud.Metastore.V1Alpha.ListMetadataImportsResponse)


    
    
    public sealed class ListMetadataImportsResponse : IPageResponse<MetadataImport>, IEnumerable<MetadataImport>, IEnumerable, IMessage<ListMetadataImportsResponse>, IEquatable<ListMetadataImportsResponse>, IDeepCloneable<ListMetadataImportsResponse>, IBufferMessage, IMessage

Reference documentation and code samples for the Dataproc Metastore v1alpha API class ListMetadataImportsResponse.

Response message for [DataprocMetastore.ListMetadataImports][google.cloud.metastore.v1alpha.DataprocMetastore.ListMetadataImports].

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ListMetadataImportsResponse

## Implements

[IPageResponse](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.IPageResponse-1.html)[MetadataImport](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Alpha/latest/Google.Cloud.Metastore.V1Alpha.MetadataImport), [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)[MetadataImport](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Alpha/latest/Google.Cloud.Metastore.V1Alpha.MetadataImport), [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[ListMetadataImportsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Alpha/latest/Google.Cloud.Metastore.V1Alpha.ListMetadataImportsResponse), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[ListMetadataImportsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Alpha/latest/Google.Cloud.Metastore.V1Alpha.ListMetadataImportsResponse), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[ListMetadataImportsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Alpha/latest/Google.Cloud.Metastore.V1Alpha.ListMetadataImportsResponse), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Metastore.V1Alpha](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Alpha/latest/Google.Cloud.Metastore.V1Alpha)

## Assembly

Google.Cloud.Metastore.V1Alpha.dll

## Constructors 

### ListMetadataImportsResponse()
    
    
    public ListMetadataImportsResponse()

### ListMetadataImportsResponse(ListMetadataImportsResponse)
    
    
    public ListMetadataImportsResponse(ListMetadataImportsResponse other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[ListMetadataImportsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Alpha/latest/Google.Cloud.Metastore.V1Alpha.ListMetadataImportsResponse)`  
  
  
## Properties 

### MetadataImports
    
    
    public RepeatedField<MetadataImport> MetadataImports { get; }

The imports in the specified service.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[MetadataImport](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Alpha/latest/Google.Cloud.Metastore.V1Alpha.MetadataImport)` |   
  
### NextPageToken
    
    
    public string NextPageToken { get; set; }

A token that can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Unreachable
    
    
    public RepeatedField<string> Unreachable { get; }

Locations that could not be reached.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
## Methods 

### GetEnumerator()
    
    
    public IEnumerator<MetadataImport> GetEnumerator()

Returns an enumerator that iterates through the resources in this response.

**Returns**  
---  
**Type** | **Description**  
`[IEnumerator](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerator-1)[MetadataImport](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Alpha/latest/Google.Cloud.Metastore.V1Alpha.MetadataImport)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
