---
url: https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-accounts/latest/com.google.shopping.merchant.accounts.v1beta.ShippingSettingsOrBuilder
title: Interface ShippingSettingsOrBuilder (1.27.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:53:20.778423+00:00
---

# Interface ShippingSettingsOrBuilder (1.27.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-accounts/latest/com.google.shopping.merchant.accounts.v1beta.ShippingSettingsOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface ShippingSettingsOrBuilder (1.27.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.27.0 (latest)  1.23.0  1.22.0  1.21.0  1.19.0  1.16.0  1.15.0  1.13.0  1.11.0  1.10.0  1.8.0  1.6.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0  0.26.0  0.24.0  0.23.0  0.20.0  0.19.0  0.18.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public interface ShippingSettingsOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getEtag()
    
    
    public abstract String getEtag()

Required. This field is used for avoid async issue. Make sure shipping setting data didn't change between get call and insert call. The user should do following steps：

  1. Set etag field as empty string for initial shipping setting creation.

  2. After initial creation, call get method to obtain an etag and current shipping setting data before call insert.

  3. Modify to wanted shipping setting information.

  4. Call insert method with the wanted shipping setting information with the etag obtained from step 2.

  5. If shipping setting data changed between step 2 and step 4. Insert request will fail because the etag changes every time the shipping setting data changes. User should repeate step 2-4 with the new etag.




`string etag = 4 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The etag.  
  
### getEtagBytes()
    
    
    public abstract ByteString getEtagBytes()

Required. This field is used for avoid async issue. Make sure shipping setting data didn't change between get call and insert call. The user should do following steps：

  1. Set etag field as empty string for initial shipping setting creation.

  2. After initial creation, call get method to obtain an etag and current shipping setting data before call insert.

  3. Modify to wanted shipping setting information.

  4. Call insert method with the wanted shipping setting information with the etag obtained from step 2.

  5. If shipping setting data changed between step 2 and step 4. Insert request will fail because the etag changes every time the shipping setting data changes. User should repeate step 2-4 with the new etag.




`string etag = 4 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for etag.  
  
### getName()
    
    
    public abstract String getName()

Identifier. The resource name of the shipping setting. Format: `accounts/{account}/shippingSetting`

`string name = 1 [(.google.api.field_behavior) = IDENTIFIER];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The name.  
  
### getNameBytes()
    
    
    public abstract ByteString getNameBytes()

Identifier. The resource name of the shipping setting. Format: `accounts/{account}/shippingSetting`

`string name = 1 [(.google.api.field_behavior) = IDENTIFIER];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for name.  
  
### getServices(int index)
    
    
    public abstract Service getServices(int index)

Optional. The target account's list of services.

` repeated .google.shopping.merchant.accounts.v1beta.Service services = 2 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Service](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-accounts/latest/com.google.shopping.merchant.accounts.v1beta.Service)` |   
  
### getServicesCount()
    
    
    public abstract int getServicesCount()

Optional. The target account's list of services.

` repeated .google.shopping.merchant.accounts.v1beta.Service services = 2 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getServicesList()
    
    
    public abstract List<Service> getServicesList()

Optional. The target account's list of services.

` repeated .google.shopping.merchant.accounts.v1beta.Service services = 2 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Service](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-accounts/latest/com.google.shopping.merchant.accounts.v1beta.Service)>` |   
  
### getServicesOrBuilder(int index)
    
    
    public abstract ServiceOrBuilder getServicesOrBuilder(int index)

Optional. The target account's list of services.

` repeated .google.shopping.merchant.accounts.v1beta.Service services = 2 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ServiceOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-accounts/latest/com.google.shopping.merchant.accounts.v1beta.ServiceOrBuilder)` |   
  
### getServicesOrBuilderList()
    
    
    public abstract List<? extends ServiceOrBuilder> getServicesOrBuilderList()

Optional. The target account's list of services.

` repeated .google.shopping.merchant.accounts.v1beta.Service services = 2 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.shopping.merchant.accounts.v1beta.ServiceOrBuilder>` |   
  
### getWarehouses(int index)
    
    
    public abstract Warehouse getWarehouses(int index)

Optional. A list of warehouses which can be referred to in `services`.

` repeated .google.shopping.merchant.accounts.v1beta.Warehouse warehouses = 3 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Warehouse](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-accounts/latest/com.google.shopping.merchant.accounts.v1beta.Warehouse)` |   
  
### getWarehousesCount()
    
    
    public abstract int getWarehousesCount()

Optional. A list of warehouses which can be referred to in `services`.

` repeated .google.shopping.merchant.accounts.v1beta.Warehouse warehouses = 3 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getWarehousesList()
    
    
    public abstract List<Warehouse> getWarehousesList()

Optional. A list of warehouses which can be referred to in `services`.

` repeated .google.shopping.merchant.accounts.v1beta.Warehouse warehouses = 3 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Warehouse](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-accounts/latest/com.google.shopping.merchant.accounts.v1beta.Warehouse)>` |   
  
### getWarehousesOrBuilder(int index)
    
    
    public abstract WarehouseOrBuilder getWarehousesOrBuilder(int index)

Optional. A list of warehouses which can be referred to in `services`.

` repeated .google.shopping.merchant.accounts.v1beta.Warehouse warehouses = 3 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[WarehouseOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-accounts/latest/com.google.shopping.merchant.accounts.v1beta.WarehouseOrBuilder)` |   
  
### getWarehousesOrBuilderList()
    
    
    public abstract List<? extends WarehouseOrBuilder> getWarehousesOrBuilderList()

Optional. A list of warehouses which can be referred to in `services`.

` repeated .google.shopping.merchant.accounts.v1beta.Warehouse warehouses = 3 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.shopping.merchant.accounts.v1beta.WarehouseOrBuilder>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
