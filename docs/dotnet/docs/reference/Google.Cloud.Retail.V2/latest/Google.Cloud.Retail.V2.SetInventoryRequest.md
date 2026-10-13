---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Retail.V2/latest/Google.Cloud.Retail.V2.SetInventoryRequest
title: Retail v2 API - Class SetInventoryRequest (2.16.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:08:30.167263+00:00
---

# Retail v2 API - Class SetInventoryRequest (2.16.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Retail.V2/latest/Google.Cloud.Retail.V2.SetInventoryRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Retail v2 API - Class SetInventoryRequest (2.16.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.16.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Retail.V2/latest/Google.Cloud.Retail.V2.SetInventoryRequest)
  * [ 2.15.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Retail.V2/2.15.0/Google.Cloud.Retail.V2.SetInventoryRequest)
  * [ 2.14.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Retail.V2/2.14.0/Google.Cloud.Retail.V2.SetInventoryRequest)
  * [ 2.13.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Retail.V2/2.13.0/Google.Cloud.Retail.V2.SetInventoryRequest)
  * [ 2.12.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Retail.V2/2.12.0/Google.Cloud.Retail.V2.SetInventoryRequest)
  * [ 2.11.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Retail.V2/2.11.0/Google.Cloud.Retail.V2.SetInventoryRequest)
  * [ 2.10.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Retail.V2/2.10.0/Google.Cloud.Retail.V2.SetInventoryRequest)
  * [ 2.9.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Retail.V2/2.9.0/Google.Cloud.Retail.V2.SetInventoryRequest)
  * [ 2.8.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Retail.V2/2.8.0/Google.Cloud.Retail.V2.SetInventoryRequest)
  * [ 2.7.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Retail.V2/2.7.0/Google.Cloud.Retail.V2.SetInventoryRequest)
  * [ 2.6.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Retail.V2/2.6.0/Google.Cloud.Retail.V2.SetInventoryRequest)
  * [ 2.5.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Retail.V2/2.5.0/Google.Cloud.Retail.V2.SetInventoryRequest)
  * [ 2.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Retail.V2/2.4.0/Google.Cloud.Retail.V2.SetInventoryRequest)
  * [ 2.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Retail.V2/2.3.0/Google.Cloud.Retail.V2.SetInventoryRequest)
  * [ 2.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Retail.V2/2.2.0/Google.Cloud.Retail.V2.SetInventoryRequest)
  * [ 2.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Retail.V2/2.1.0/Google.Cloud.Retail.V2.SetInventoryRequest)
  * [ 2.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Retail.V2/2.0.0/Google.Cloud.Retail.V2.SetInventoryRequest)
  * [ 1.6.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Retail.V2/1.6.0/Google.Cloud.Retail.V2.SetInventoryRequest)
  * [ 1.5.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Retail.V2/1.5.0/Google.Cloud.Retail.V2.SetInventoryRequest)
  * [ 1.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Retail.V2/1.4.0/Google.Cloud.Retail.V2.SetInventoryRequest)
  * [ 1.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Retail.V2/1.3.0/Google.Cloud.Retail.V2.SetInventoryRequest)
  * [ 1.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Retail.V2/1.2.0/Google.Cloud.Retail.V2.SetInventoryRequest)
  * [ 1.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Retail.V2/1.1.0/Google.Cloud.Retail.V2.SetInventoryRequest)
  * [ 1.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Retail.V2/1.0.0/Google.Cloud.Retail.V2.SetInventoryRequest)


    
    
    public sealed class SetInventoryRequest : IMessage<SetInventoryRequest>, IEquatable<SetInventoryRequest>, IDeepCloneable<SetInventoryRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the Retail v2 API class SetInventoryRequest.

Request message for [ProductService.SetInventory][google.cloud.retail.v2.ProductService.SetInventory] method.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > SetInventoryRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[SetInventoryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Retail.V2/latest/Google.Cloud.Retail.V2.SetInventoryRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[SetInventoryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Retail.V2/latest/Google.Cloud.Retail.V2.SetInventoryRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[SetInventoryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Retail.V2/latest/Google.Cloud.Retail.V2.SetInventoryRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Retail.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Retail.V2/latest/Google.Cloud.Retail.V2)

## Assembly

Google.Cloud.Retail.V2.dll

## Constructors 

### SetInventoryRequest()
    
    
    public SetInventoryRequest()

### SetInventoryRequest(SetInventoryRequest)
    
    
    public SetInventoryRequest(SetInventoryRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[SetInventoryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Retail.V2/latest/Google.Cloud.Retail.V2.SetInventoryRequest)`  
  
  
## Properties 

### AllowMissing
    
    
    public bool AllowMissing { get; set; }

If set to true, and the [Product][google.cloud.retail.v2.Product] with name [Product.name][google.cloud.retail.v2.Product.name] is not found, the inventory update will still be processed and retained for at most 1 day until the [Product][google.cloud.retail.v2.Product] is created. If set to false, a NOT_FOUND error is returned if the [Product][google.cloud.retail.v2.Product] is not found.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### Inventory
    
    
    public Product Inventory { get; set; }

Required. The inventory information to update. The allowable fields to update are:

  * [Product.price_info][google.cloud.retail.v2.Product.price_info]
  * [Product.availability][google.cloud.retail.v2.Product.availability]
  * [Product.available_quantity][google.cloud.retail.v2.Product.available_quantity]
  * [Product.fulfillment_info][google.cloud.retail.v2.Product.fulfillment_info] The updated inventory fields must be specified in [SetInventoryRequest.set_mask][google.cloud.retail.v2.SetInventoryRequest.set_mask].



If [SetInventoryRequest.inventory.name][google.cloud.retail.v2.Product.name] is empty or invalid, an INVALID_ARGUMENT error is returned.

If the caller does not have permission to update the [Product][google.cloud.retail.v2.Product] named in [Product.name][google.cloud.retail.v2.Product.name], regardless of whether or not it exists, a PERMISSION_DENIED error is returned.

If the [Product][google.cloud.retail.v2.Product] to update does not have existing inventory information, the provided inventory information will be inserted.

If the [Product][google.cloud.retail.v2.Product] to update has existing inventory information, the provided inventory information will be merged while respecting the last update time for each inventory field, using the provided or default value for [SetInventoryRequest.set_time][google.cloud.retail.v2.SetInventoryRequest.set_time].

The caller can replace place IDs for a subset of fulfillment types in the following ways:

  * Adds "fulfillment_info" in [SetInventoryRequest.set_mask][google.cloud.retail.v2.SetInventoryRequest.set_mask]
  * Specifies only the desired fulfillment types and corresponding place IDs to update in [SetInventoryRequest.inventory.fulfillment_info][google.cloud.retail.v2.Product.fulfillment_info]



The caller can clear all place IDs from a subset of fulfillment types in the following ways:

  * Adds "fulfillment_info" in [SetInventoryRequest.set_mask][google.cloud.retail.v2.SetInventoryRequest.set_mask]
  * Specifies only the desired fulfillment types to clear in [SetInventoryRequest.inventory.fulfillment_info][google.cloud.retail.v2.Product.fulfillment_info]
  * Checks that only the desired fulfillment info types have empty [SetInventoryRequest.inventory.fulfillment_info.place_ids][google.cloud.retail.v2.FulfillmentInfo.place_ids]



The last update time is recorded for the following inventory fields:

  * [Product.price_info][google.cloud.retail.v2.Product.price_info]
  * [Product.availability][google.cloud.retail.v2.Product.availability]
  * [Product.available_quantity][google.cloud.retail.v2.Product.available_quantity]
  * [Product.fulfillment_info][google.cloud.retail.v2.Product.fulfillment_info]



If a full overwrite of inventory information while ignoring timestamps is needed, [ProductService.UpdateProduct][google.cloud.retail.v2.ProductService.UpdateProduct] should be invoked instead.

**Property Value**  
---  
**Type** | **Description**  
`[Product](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Retail.V2/latest/Google.Cloud.Retail.V2.Product)` |   
  
### SetMask
    
    
    public FieldMask SetMask { get; set; }

Indicates which inventory fields in the provided [Product][google.cloud.retail.v2.Product] to update.

At least one field must be provided.

If an unsupported or unknown field is provided, an INVALID_ARGUMENT error is returned and the entire update will be ignored.

**Property Value**  
---  
**Type** | **Description**  
`[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)` |   
  
### SetTime
    
    
    public Timestamp SetTime { get; set; }

The time when the request is issued, used to prevent out-of-order updates on inventory fields with the last update time recorded. If not provided, the internal system time will be used.

**Property Value**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
