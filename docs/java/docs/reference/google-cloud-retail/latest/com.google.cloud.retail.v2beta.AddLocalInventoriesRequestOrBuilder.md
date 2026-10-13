---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2beta.AddLocalInventoriesRequestOrBuilder
title: Interface AddLocalInventoriesRequestOrBuilder (2.101.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:35:45.031721+00:00
---

# Interface AddLocalInventoriesRequestOrBuilder (2.101.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2beta.AddLocalInventoriesRequestOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface AddLocalInventoriesRequestOrBuilder (2.101.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.101.0 (latest)  2.97.0  2.96.0  2.95.0  2.93.0  2.90.0  2.89.0  2.87.0  2.85.0  2.84.0  2.82.0  2.80.0  2.78.0  2.77.0  2.76.0  2.75.0  2.74.0  2.72.0  2.70.0  2.69.0  2.66.0  2.65.0  2.64.0  2.62.0  2.61.0  2.60.0  2.59.0  2.58.0  2.57.0  2.56.0  2.55.0  2.54.0  2.53.0  2.51.0  2.50.0  2.49.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.26.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.1  2.4.0  2.3.0  2.2.3  2.1.0  2.0.19 
    
    
    public interface AddLocalInventoriesRequestOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getAddMask()
    
    
    public abstract FieldMask getAddMask()

Indicates which inventory fields in the provided list of LocalInventory to update. The field is updated to the provided value.

If a field is set while the place does not have a previous local inventory, the local inventory at that store is created.

If a field is set while the value of that field is not provided, the original field value, if it exists, is deleted.

If the mask is not set or set with empty paths, all inventory fields will be updated.

If an unsupported or unknown field is provided, an INVALID_ARGUMENT error is returned and the entire update will be ignored.

`.google.protobuf.FieldMask add_mask = 4;`

**Returns**  
---  
**Type** | **Description**  
`[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)` | The addMask.  
  
### getAddMaskOrBuilder()
    
    
    public abstract FieldMaskOrBuilder getAddMaskOrBuilder()

Indicates which inventory fields in the provided list of LocalInventory to update. The field is updated to the provided value.

If a field is set while the place does not have a previous local inventory, the local inventory at that store is created.

If a field is set while the value of that field is not provided, the original field value, if it exists, is deleted.

If the mask is not set or set with empty paths, all inventory fields will be updated.

If an unsupported or unknown field is provided, an INVALID_ARGUMENT error is returned and the entire update will be ignored.

`.google.protobuf.FieldMask add_mask = 4;`

**Returns**  
---  
**Type** | **Description**  
`[FieldMaskOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMaskOrBuilder.html)` |   
  
### getAddTime()
    
    
    public abstract Timestamp getAddTime()

The time when the inventory updates are issued. Used to prevent out-of-order updates on local inventory fields. If not provided, the internal system time will be used.

`.google.protobuf.Timestamp add_time = 5;`

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The addTime.  
  
### getAddTimeOrBuilder()
    
    
    public abstract TimestampOrBuilder getAddTimeOrBuilder()

The time when the inventory updates are issued. Used to prevent out-of-order updates on local inventory fields. If not provided, the internal system time will be used.

`.google.protobuf.Timestamp add_time = 5;`

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### getAllowMissing()
    
    
    public abstract boolean getAllowMissing()

If set to true, and the Product is not found, the local inventory will still be processed and retained for at most 1 day and processed once the Product is created. If set to false, a NOT_FOUND error is returned if the Product is not found.

`bool allow_missing = 6;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The allowMissing.  
  
### getLocalInventories(int index)
    
    
    public abstract LocalInventory getLocalInventories(int index)

Required. A list of inventory information at difference places. Each place is identified by its place ID. At most 3000 inventories are allowed per request.

` repeated .google.cloud.retail.v2beta.LocalInventory local_inventories = 2 [(.google.api.field_behavior) = REQUIRED]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[LocalInventory](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2beta.LocalInventory)` |   
  
### getLocalInventoriesCount()
    
    
    public abstract int getLocalInventoriesCount()

Required. A list of inventory information at difference places. Each place is identified by its place ID. At most 3000 inventories are allowed per request.

` repeated .google.cloud.retail.v2beta.LocalInventory local_inventories = 2 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getLocalInventoriesList()
    
    
    public abstract List<LocalInventory> getLocalInventoriesList()

Required. A list of inventory information at difference places. Each place is identified by its place ID. At most 3000 inventories are allowed per request.

` repeated .google.cloud.retail.v2beta.LocalInventory local_inventories = 2 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[LocalInventory](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2beta.LocalInventory)>` |   
  
### getLocalInventoriesOrBuilder(int index)
    
    
    public abstract LocalInventoryOrBuilder getLocalInventoriesOrBuilder(int index)

Required. A list of inventory information at difference places. Each place is identified by its place ID. At most 3000 inventories are allowed per request.

` repeated .google.cloud.retail.v2beta.LocalInventory local_inventories = 2 [(.google.api.field_behavior) = REQUIRED]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[LocalInventoryOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2beta.LocalInventoryOrBuilder)` |   
  
### getLocalInventoriesOrBuilderList()
    
    
    public abstract List<? extends LocalInventoryOrBuilder> getLocalInventoriesOrBuilderList()

Required. A list of inventory information at difference places. Each place is identified by its place ID. At most 3000 inventories are allowed per request.

` repeated .google.cloud.retail.v2beta.LocalInventory local_inventories = 2 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.retail.v2beta.LocalInventoryOrBuilder>` |   
  
### getProduct()
    
    
    public abstract String getProduct()

Required. Full resource name of Product, such as `projects/*/locations/global/catalogs/default_catalog/branches/default_branch/products/some_product_id`.

If the caller does not have permission to access the Product, regardless of whether or not it exists, a PERMISSION_DENIED error is returned.

` string product = 1 [(.google.api.field_behavior) = REQUIRED, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The product.  
  
### getProductBytes()
    
    
    public abstract ByteString getProductBytes()

Required. Full resource name of Product, such as `projects/*/locations/global/catalogs/default_catalog/branches/default_branch/products/some_product_id`.

If the caller does not have permission to access the Product, regardless of whether or not it exists, a PERMISSION_DENIED error is returned.

` string product = 1 [(.google.api.field_behavior) = REQUIRED, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for product.  
  
### hasAddMask()
    
    
    public abstract boolean hasAddMask()

Indicates which inventory fields in the provided list of LocalInventory to update. The field is updated to the provided value.

If a field is set while the place does not have a previous local inventory, the local inventory at that store is created.

If a field is set while the value of that field is not provided, the original field value, if it exists, is deleted.

If the mask is not set or set with empty paths, all inventory fields will be updated.

If an unsupported or unknown field is provided, an INVALID_ARGUMENT error is returned and the entire update will be ignored.

`.google.protobuf.FieldMask add_mask = 4;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the addMask field is set.  
  
### hasAddTime()
    
    
    public abstract boolean hasAddTime()

The time when the inventory updates are issued. Used to prevent out-of-order updates on local inventory fields. If not provided, the internal system time will be used.

`.google.protobuf.Timestamp add_time = 5;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the addTime field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
