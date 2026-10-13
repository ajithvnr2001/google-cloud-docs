---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Commerce.Consumer.Procurement.V1/latest/Google.Cloud.Commerce.Consumer.Procurement.V1.ListOrdersRequest
title: Cloud Commerce Consumer Procurement v1 API - Class ListOrdersRequest (1.6.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:01:34.859814+00:00
---

# Cloud Commerce Consumer Procurement v1 API - Class ListOrdersRequest (1.6.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Commerce.Consumer.Procurement.V1/latest/Google.Cloud.Commerce.Consumer.Procurement.V1.ListOrdersRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Cloud Commerce Consumer Procurement v1 API - Class ListOrdersRequest (1.6.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 1.6.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Commerce.Consumer.Procurement.V1/latest/Google.Cloud.Commerce.Consumer.Procurement.V1.ListOrdersRequest)
  * [ 1.5.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Commerce.Consumer.Procurement.V1/1.5.0/Google.Cloud.Commerce.Consumer.Procurement.V1.ListOrdersRequest)
  * [ 1.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Commerce.Consumer.Procurement.V1/1.4.0/Google.Cloud.Commerce.Consumer.Procurement.V1.ListOrdersRequest)
  * [ 1.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Commerce.Consumer.Procurement.V1/1.3.0/Google.Cloud.Commerce.Consumer.Procurement.V1.ListOrdersRequest)
  * [ 1.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Commerce.Consumer.Procurement.V1/1.2.0/Google.Cloud.Commerce.Consumer.Procurement.V1.ListOrdersRequest)
  * [ 1.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Commerce.Consumer.Procurement.V1/1.1.0/Google.Cloud.Commerce.Consumer.Procurement.V1.ListOrdersRequest)
  * [ 1.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Commerce.Consumer.Procurement.V1/1.0.0/Google.Cloud.Commerce.Consumer.Procurement.V1.ListOrdersRequest)


    
    
    public sealed class ListOrdersRequest : IPageRequest, IMessage<ListOrdersRequest>, IEquatable<ListOrdersRequest>, IDeepCloneable<ListOrdersRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the Cloud Commerce Consumer Procurement v1 API class ListOrdersRequest.

Request message for [ConsumerProcurementService.ListOrders][google.cloud.commerce.consumer.procurement.v1.ConsumerProcurementService.ListOrders].

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ListOrdersRequest

## Implements

[IPageRequest](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.IPageRequest.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[ListOrdersRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Commerce.Consumer.Procurement.V1/latest/Google.Cloud.Commerce.Consumer.Procurement.V1.ListOrdersRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[ListOrdersRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Commerce.Consumer.Procurement.V1/latest/Google.Cloud.Commerce.Consumer.Procurement.V1.ListOrdersRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[ListOrdersRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Commerce.Consumer.Procurement.V1/latest/Google.Cloud.Commerce.Consumer.Procurement.V1.ListOrdersRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Commerce.Consumer.Procurement.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Commerce.Consumer.Procurement.V1/latest/Google.Cloud.Commerce.Consumer.Procurement.V1)

## Assembly

Google.Cloud.Commerce.Consumer.Procurement.V1.dll

## Constructors 

### ListOrdersRequest()
    
    
    public ListOrdersRequest()

### ListOrdersRequest(ListOrdersRequest)
    
    
    public ListOrdersRequest(ListOrdersRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[ListOrdersRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Commerce.Consumer.Procurement.V1/latest/Google.Cloud.Commerce.Consumer.Procurement.V1.ListOrdersRequest)`  
  
  
## Properties 

### Filter
    
    
    public string Filter { get; set; }

Filter that you can use to limit the list request.

A query string that can match a selected set of attributes with string values. For example, `display_name=abc`. Supported query attributes are

  * `display_name`



If the query contains special characters other than letters, underscore, or digits, the phrase must be quoted with double quotes. For example, `display_name="foo:bar"`, where the display name needs to be quoted because it contains special character colon.

Queries can be combined with `OR`, and `NOT` to form more complex queries. You can also group them to force a desired evaluation order. For example, `display_name=abc OR display_name=def`.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### PageSize
    
    
    public int PageSize { get; set; }

The maximum number of entries requested. The default page size is 25 and the maximum page size is 200.

**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### PageToken
    
    
    public string PageToken { get; set; }

The token for fetching the next page.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Parent
    
    
    public string Parent { get; set; }

Required. The parent resource to query for orders. This field has the form `billingAccounts/{billing-account-id}`.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
