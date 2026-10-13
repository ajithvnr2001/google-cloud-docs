---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.ListEncryptionConfigsRequest
title: Cloud Dataplex v1 API - Class ListEncryptionConfigsRequest (3.15.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:39:39.259188+00:00
---

# Cloud Dataplex v1 API - Class ListEncryptionConfigsRequest (3.15.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.ListEncryptionConfigsRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Cloud Dataplex v1 API - Class ListEncryptionConfigsRequest (3.15.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.15.0 (latest)  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0  2.1.0  2.0.0  1.0.0 
    
    
    public sealed class ListEncryptionConfigsRequest : IMessage<ListEncryptionConfigsRequest>, IEquatable<ListEncryptionConfigsRequest>, IDeepCloneable<ListEncryptionConfigsRequest>, IBufferMessage, IMessage, IPageRequest

Reference documentation and code samples for the Cloud Dataplex v1 API class ListEncryptionConfigsRequest.

List EncryptionConfigs Request

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ListEncryptionConfigsRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[ListEncryptionConfigsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.ListEncryptionConfigsRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[ListEncryptionConfigsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.ListEncryptionConfigsRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[ListEncryptionConfigsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.ListEncryptionConfigsRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html), [IPageRequest](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.IPageRequest.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Dataplex.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1)

## Assembly

Google.Cloud.Dataplex.V1.dll

## Constructors 

### ListEncryptionConfigsRequest()
    
    
    public ListEncryptionConfigsRequest()

### ListEncryptionConfigsRequest(ListEncryptionConfigsRequest)
    
    
    public ListEncryptionConfigsRequest(ListEncryptionConfigsRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[ListEncryptionConfigsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.ListEncryptionConfigsRequest)`  
  
  
## Properties 

### Filter
    
    
    public string Filter { get; set; }

Optional. Filter the EncryptionConfigs to be returned. Using bare literals: (These values will be matched anywhere it may appear in the object's field values)

  * filter=some_value Using fields: (These values will be matched only in the specified field)
  * filter=some_field=some_value Supported fields:
  * name, key, create_time, update_time, encryption_state Example:
  * filter=name=organizations/123/locations/us-central1/encryptionConfigs/test-config conjunctions: (AND, OR, NOT)
  * filter=name=organizations/123/locations/us-central1/encryptionConfigs/test-config AND mode=CMEK logical operators: (>, <, >=, <=, !=, =, :),
  * filter=create_time>2024-05-01T00:00:00.000Z



**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### OrderBy
    
    
    public string OrderBy { get; set; }

Optional. Order by fields for the result.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### PageSize
    
    
    public int PageSize { get; set; }

Optional. Maximum number of EncryptionConfigs to return. The service may return fewer than this value. If unspecified, at most 10 EncryptionConfigs will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000.

**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### PageToken
    
    
    public string PageToken { get; set; }

Optional. Page token received from a previous `ListEncryptionConfigs` call. Provide this to retrieve the subsequent page. When paginating, the parameters - filter and order_by provided to `ListEncryptionConfigs` must match the call that provided the page token.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Parent
    
    
    public string Parent { get; set; }

Required. The location for which the EncryptionConfig is to be listed.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ParentAsOrganizationLocationName
    
    
    public OrganizationLocationName ParentAsOrganizationLocationName { get; set; }

[OrganizationLocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.OrganizationLocationName)-typed view over the [Parent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.ListEncryptionConfigsRequest#Google_Cloud_Dataplex_V1_ListEncryptionConfigsRequest_Parent) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[OrganizationLocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.OrganizationLocationName)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-30 UTC."],[],[]] 
