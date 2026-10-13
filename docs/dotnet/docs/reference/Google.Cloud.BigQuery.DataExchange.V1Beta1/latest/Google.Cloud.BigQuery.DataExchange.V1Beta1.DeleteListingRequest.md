---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataExchange.V1Beta1/latest/Google.Cloud.BigQuery.DataExchange.V1Beta1.DeleteListingRequest
title: Analytics Hub v1beta1 API - Class DeleteListingRequest (2.0.0-beta07) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:41:20.959422+00:00
---

# Analytics Hub v1beta1 API - Class DeleteListingRequest (2.0.0-beta07)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataExchange.V1Beta1/latest/Google.Cloud.BigQuery.DataExchange.V1Beta1.DeleteListingRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Analytics Hub v1beta1 API - Class DeleteListingRequest (2.0.0-beta07) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.0.0-beta07 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataExchange.V1Beta1/latest/Google.Cloud.BigQuery.DataExchange.V1Beta1.DeleteListingRequest)
  * [ 2.0.0-beta06 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataExchange.V1Beta1/2.0.0-beta06/Google.Cloud.BigQuery.DataExchange.V1Beta1.DeleteListingRequest)
  * [ 1.0.0-beta01 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataExchange.V1Beta1/1.0.0-beta01/Google.Cloud.BigQuery.DataExchange.V1Beta1.DeleteListingRequest)


    
    
    public sealed class DeleteListingRequest : IMessage<DeleteListingRequest>, IEquatable<DeleteListingRequest>, IDeepCloneable<DeleteListingRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the Analytics Hub v1beta1 API class DeleteListingRequest.

Message for deleting a listing.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > DeleteListingRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[DeleteListingRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataExchange.V1Beta1/latest/Google.Cloud.BigQuery.DataExchange.V1Beta1.DeleteListingRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[DeleteListingRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataExchange.V1Beta1/latest/Google.Cloud.BigQuery.DataExchange.V1Beta1.DeleteListingRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[DeleteListingRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataExchange.V1Beta1/latest/Google.Cloud.BigQuery.DataExchange.V1Beta1.DeleteListingRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.BigQuery.DataExchange.V1Beta1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataExchange.V1Beta1/latest/Google.Cloud.BigQuery.DataExchange.V1Beta1)

## Assembly

Google.Cloud.BigQuery.DataExchange.V1Beta1.dll

## Constructors 

### DeleteListingRequest()
    
    
    public DeleteListingRequest()

### DeleteListingRequest(DeleteListingRequest)
    
    
    public DeleteListingRequest(DeleteListingRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[DeleteListingRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataExchange.V1Beta1/latest/Google.Cloud.BigQuery.DataExchange.V1Beta1.DeleteListingRequest)`  
  
  
## Properties 

### ListingName
    
    
    public ListingName ListingName { get; set; }

[ListingName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataExchange.V1Beta1/latest/Google.Cloud.BigQuery.DataExchange.V1Beta1.ListingName)-typed view over the [Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataExchange.V1Beta1/latest/Google.Cloud.BigQuery.DataExchange.V1Beta1.DeleteListingRequest#Google_Cloud_BigQuery_DataExchange_V1Beta1_DeleteListingRequest_Name) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[ListingName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataExchange.V1Beta1/latest/Google.Cloud.BigQuery.DataExchange.V1Beta1.ListingName)` |   
  
### Name
    
    
    public string Name { get; set; }

Required. Resource name of the listing to delete. e.g. `projects/myproject/locations/US/dataExchanges/123/listings/456`.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
