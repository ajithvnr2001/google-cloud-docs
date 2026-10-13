---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceDirectory.V1Beta1/latest/Google.Cloud.ServiceDirectory.V1Beta1.ListNamespacesRequest
title: Service Directory v1beta1 API - Class ListNamespacesRequest (2.0.0-beta07) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:09:01.901512+00:00
---

# Service Directory v1beta1 API - Class ListNamespacesRequest (2.0.0-beta07)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceDirectory.V1Beta1/latest/Google.Cloud.ServiceDirectory.V1Beta1.ListNamespacesRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Service Directory v1beta1 API - Class ListNamespacesRequest (2.0.0-beta07) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.0.0-beta07 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceDirectory.V1Beta1/latest/Google.Cloud.ServiceDirectory.V1Beta1.ListNamespacesRequest)
  * [ 2.0.0-beta06 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceDirectory.V1Beta1/2.0.0-beta06/Google.Cloud.ServiceDirectory.V1Beta1.ListNamespacesRequest)
  * [ 1.0.0-beta06 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceDirectory.V1Beta1/1.0.0-beta06/Google.Cloud.ServiceDirectory.V1Beta1.ListNamespacesRequest)


    
    
    public sealed class ListNamespacesRequest : IMessage<ListNamespacesRequest>, IEquatable<ListNamespacesRequest>, IDeepCloneable<ListNamespacesRequest>, IBufferMessage, IMessage, IPageRequest

Reference documentation and code samples for the Service Directory v1beta1 API class ListNamespacesRequest.

The request message for [RegistrationService.ListNamespaces][google.cloud.servicedirectory.v1beta1.RegistrationService.ListNamespaces].

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ListNamespacesRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[ListNamespacesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceDirectory.V1Beta1/latest/Google.Cloud.ServiceDirectory.V1Beta1.ListNamespacesRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[ListNamespacesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceDirectory.V1Beta1/latest/Google.Cloud.ServiceDirectory.V1Beta1.ListNamespacesRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[ListNamespacesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceDirectory.V1Beta1/latest/Google.Cloud.ServiceDirectory.V1Beta1.ListNamespacesRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html), [IPageRequest](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.IPageRequest.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.ServiceDirectory.V1Beta1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceDirectory.V1Beta1/latest/Google.Cloud.ServiceDirectory.V1Beta1)

## Assembly

Google.Cloud.ServiceDirectory.V1Beta1.dll

## Constructors 

### ListNamespacesRequest()
    
    
    public ListNamespacesRequest()

### ListNamespacesRequest(ListNamespacesRequest)
    
    
    public ListNamespacesRequest(ListNamespacesRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[ListNamespacesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceDirectory.V1Beta1/latest/Google.Cloud.ServiceDirectory.V1Beta1.ListNamespacesRequest)`  
  
  
## Properties 

### Filter
    
    
    public string Filter { get; set; }

Optional. The filter to list results by.

General `filter` string syntax: `<field> <operator> <value> (<logical connector>)`

  * `<field>` can be `name`, `labels.<key>` for map field, or `attributes.<field>` for attributes field
  * `<operator>` can be `<`, `>`, `<=`, `>=`, `!=`, `=`, `:`. Of which `:` means `HAS`, and is roughly the same as `=`
  * `<value>` must be the same data type as field
  * `<logical connector>` can be `AND`, `OR`, `NOT`



Examples of valid filters:

  * `labels.owner` returns namespaces that have a label with the key `owner`, this is the same as `labels:owner`
  * `labels.owner=sd` returns namespaces that have key/value `owner=sd`
  * `name>projects/my-project/locations/us-east1/namespaces/namespace-c` returns namespaces that have name that is alphabetically later than the string, so "namespace-e" is returned but "namespace-a" is not
  * `labels.owner!=sd AND labels.foo=bar` returns namespaces that have `owner` in label key but value is not `sd` AND have key/value `foo=bar`
  * `doesnotexist.foo=bar` returns an empty list. Note that namespace doesn't have a field called "doesnotexist". Since the filter does not match any namespaces, it returns no results
  * `attributes.managed_registration=true` returns namespaces that are managed by a GCP product or service



For more information about filtering, see [API Filtering](https://aip.dev/160).

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### OrderBy
    
    
    public string OrderBy { get; set; }

Optional. The order to list results by.

General `order_by` string syntax: `<field> (<asc|desc>) (,)`

  * `<field>` allows value: `name`
  * `<asc|desc>` ascending or descending order by `<field>`. If this is left blank, `asc` is used



Note that an empty `order_by` string results in default order, which is order by `name` in ascending order.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### PageSize
    
    
    public int PageSize { get; set; }

Optional. The maximum number of items to return. The default value is 100.

**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### PageToken
    
    
    public string PageToken { get; set; }

Optional. The next_page_token value returned from a previous List request, if any.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Parent
    
    
    public string Parent { get; set; }

Required. The resource name of the project and location whose namespaces you'd like to list.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ParentAsLocationName
    
    
    public LocationName ParentAsLocationName { get; set; }

[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)-typed view over the [Parent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceDirectory.V1Beta1/latest/Google.Cloud.ServiceDirectory.V1Beta1.ListNamespacesRequest#Google_Cloud_ServiceDirectory_V1Beta1_ListNamespacesRequest_Parent) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
