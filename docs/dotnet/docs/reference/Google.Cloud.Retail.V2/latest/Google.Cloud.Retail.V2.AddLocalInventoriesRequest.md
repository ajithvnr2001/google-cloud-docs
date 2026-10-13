---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Retail.V2/latest/Google.Cloud.Retail.V2.AddLocalInventoriesRequest
title: Retail v2 API - Class AddLocalInventoriesRequest (2.16.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:59:52.985764+00:00
---

# Retail v2 API - Class AddLocalInventoriesRequest (2.16.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Retail.V2/latest/Google.Cloud.Retail.V2.AddLocalInventoriesRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Retail v2 API - Class AddLocalInventoriesRequest (2.16.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.16.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Retail.V2/latest/Google.Cloud.Retail.V2.AddLocalInventoriesRequest)
  * [ 2.15.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Retail.V2/2.15.0/Google.Cloud.Retail.V2.AddLocalInventoriesRequest)
  * [ 2.14.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Retail.V2/2.14.0/Google.Cloud.Retail.V2.AddLocalInventoriesRequest)
  * [ 2.13.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Retail.V2/2.13.0/Google.Cloud.Retail.V2.AddLocalInventoriesRequest)
  * [ 2.12.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Retail.V2/2.12.0/Google.Cloud.Retail.V2.AddLocalInventoriesRequest)
  * [ 2.11.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Retail.V2/2.11.0/Google.Cloud.Retail.V2.AddLocalInventoriesRequest)
  * [ 2.10.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Retail.V2/2.10.0/Google.Cloud.Retail.V2.AddLocalInventoriesRequest)
  * [ 2.9.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Retail.V2/2.9.0/Google.Cloud.Retail.V2.AddLocalInventoriesRequest)
  * [ 2.8.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Retail.V2/2.8.0/Google.Cloud.Retail.V2.AddLocalInventoriesRequest)
  * [ 2.7.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Retail.V2/2.7.0/Google.Cloud.Retail.V2.AddLocalInventoriesRequest)
  * [ 2.6.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Retail.V2/2.6.0/Google.Cloud.Retail.V2.AddLocalInventoriesRequest)
  * [ 2.5.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Retail.V2/2.5.0/Google.Cloud.Retail.V2.AddLocalInventoriesRequest)
  * [ 2.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Retail.V2/2.4.0/Google.Cloud.Retail.V2.AddLocalInventoriesRequest)
  * [ 2.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Retail.V2/2.3.0/Google.Cloud.Retail.V2.AddLocalInventoriesRequest)
  * [ 2.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Retail.V2/2.2.0/Google.Cloud.Retail.V2.AddLocalInventoriesRequest)
  * [ 2.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Retail.V2/2.1.0/Google.Cloud.Retail.V2.AddLocalInventoriesRequest)
  * [ 2.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Retail.V2/2.0.0/Google.Cloud.Retail.V2.AddLocalInventoriesRequest)
  * [ 1.6.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Retail.V2/1.6.0/Google.Cloud.Retail.V2.AddLocalInventoriesRequest)
  * [ 1.5.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Retail.V2/1.5.0/Google.Cloud.Retail.V2.AddLocalInventoriesRequest)
  * [ 1.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Retail.V2/1.4.0/Google.Cloud.Retail.V2.AddLocalInventoriesRequest)
  * [ 1.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Retail.V2/1.3.0/Google.Cloud.Retail.V2.AddLocalInventoriesRequest)
  * [ 1.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Retail.V2/1.2.0/Google.Cloud.Retail.V2.AddLocalInventoriesRequest)
  * [ 1.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Retail.V2/1.1.0/Google.Cloud.Retail.V2.AddLocalInventoriesRequest)
  * [ 1.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Retail.V2/1.0.0/Google.Cloud.Retail.V2.AddLocalInventoriesRequest)


    
    
    public sealed class AddLocalInventoriesRequest : IMessage<AddLocalInventoriesRequest>, IEquatable<AddLocalInventoriesRequest>, IDeepCloneable<AddLocalInventoriesRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the Retail v2 API class AddLocalInventoriesRequest.

Request message for [ProductService.AddLocalInventories][google.cloud.retail.v2.ProductService.AddLocalInventories] method.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > AddLocalInventoriesRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[AddLocalInventoriesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Retail.V2/latest/Google.Cloud.Retail.V2.AddLocalInventoriesRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[AddLocalInventoriesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Retail.V2/latest/Google.Cloud.Retail.V2.AddLocalInventoriesRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[AddLocalInventoriesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Retail.V2/latest/Google.Cloud.Retail.V2.AddLocalInventoriesRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Retail.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Retail.V2/latest/Google.Cloud.Retail.V2)

## Assembly

Google.Cloud.Retail.V2.dll

## Constructors 

### AddLocalInventoriesRequest()
    
    
    public AddLocalInventoriesRequest()

### AddLocalInventoriesRequest(AddLocalInventoriesRequest)
    
    
    public AddLocalInventoriesRequest(AddLocalInventoriesRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[AddLocalInventoriesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Retail.V2/latest/Google.Cloud.Retail.V2.AddLocalInventoriesRequest)`  
  
  
## Properties 

### AddMask
    
    
    public FieldMask AddMask { get; set; }

Indicates which inventory fields in the provided list of [LocalInventory][google.cloud.retail.v2.LocalInventory] to update. The field is updated to the provided value.

If a field is set while the place does not have a previous local inventory, the local inventory at that store is created.

If a field is set while the value of that field is not provided, the original field value, if it exists, is deleted.

If the mask is not set or set with empty paths, all inventory fields will be updated.

If an unsupported or unknown field is provided, an INVALID_ARGUMENT error is returned and the entire update will be ignored.

**Property Value**  
---  
**Type** | **Description**  
`[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)` |   
  
### AddTime
    
    
    public Timestamp AddTime { get; set; }

The time when the inventory updates are issued. Used to prevent out-of-order updates on local inventory fields. If not provided, the internal system time will be used.

**Property Value**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html)` |   
  
### AllowMissing
    
    
    public bool AllowMissing { get; set; }

If set to true, and the [Product][google.cloud.retail.v2.Product] is not found, the local inventory will still be processed and retained for at most 1 day and processed once the [Product][google.cloud.retail.v2.Product] is created. If set to false, a NOT_FOUND error is returned if the [Product][google.cloud.retail.v2.Product] is not found.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### LocalInventories
    
    
    public RepeatedField<LocalInventory> LocalInventories { get; }

Required. A list of inventory information at difference places. Each place is identified by its place ID. At most 3000 inventories are allowed per request.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[LocalInventory](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Retail.V2/latest/Google.Cloud.Retail.V2.LocalInventory)` |   
  
### Product
    
    
    public string Product { get; set; }

Required. Full resource name of [Product][google.cloud.retail.v2.Product], such as `projects/*/locations/global/catalogs/default_catalog/branches/default_branch/products/some_product_id`.

If the caller does not have permission to access the [Product][google.cloud.retail.v2.Product], regardless of whether or not it exists, a PERMISSION_DENIED error is returned.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ProductAsProductName
    
    
    public ProductName ProductAsProductName { get; set; }

[ProductName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Retail.V2/latest/Google.Cloud.Retail.V2.ProductName)-typed view over the [Product](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Retail.V2/latest/Google.Cloud.Retail.V2.AddLocalInventoriesRequest#Google_Cloud_Retail_V2_AddLocalInventoriesRequest_Product) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[ProductName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Retail.V2/latest/Google.Cloud.Retail.V2.ProductName)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
