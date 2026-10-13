---
url: https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-inventories/latest/com.google.shopping.merchant.inventories.v1beta.stub.RegionalInventoryServiceStub
title: Class RegionalInventoryServiceStub (1.27.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:52:31.176623+00:00
---

# Class RegionalInventoryServiceStub (1.27.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-inventories/latest/com.google.shopping.merchant.inventories.v1beta.stub.RegionalInventoryServiceStub

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class RegionalInventoryServiceStub (1.27.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.27.0 (latest)  1.23.0  1.22.0  1.21.0  1.19.0  1.16.0  1.15.0  1.13.0  1.11.0  1.10.0  1.8.0  1.6.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0  0.46.0  0.44.0  0.43.0  0.40.0  0.39.0  0.38.0  0.36.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 
    
    
    public abstract class RegionalInventoryServiceStub implements BackgroundResource

Base stub class for the RegionalInventoryService service API.

This class is for advanced usage and reflects the underlying API directly.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > RegionalInventoryServiceStub

## Implements

[BackgroundResource](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.core.BackgroundResource.html)

## Inherited Members

[Object.clone()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#clone--)

[Object.equals(Object)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#equals-java.lang.Object-)

[Object.finalize()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#finalize--)

[Object.getClass()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#getClass--)

[Object.hashCode()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#hashCode--)

[Object.notify()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notify--)

[Object.notifyAll()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notifyAll--)

[Object.toString()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#toString--)

[Object.wait()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait--)

[Object.wait(long)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-)

[Object.wait(long,int)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-int-)

## Constructors 

### RegionalInventoryServiceStub()
    
    
    public RegionalInventoryServiceStub()

## Methods 

### close()
    
    
    public abstract void close()

### deleteRegionalInventoryCallable()
    
    
    public UnaryCallable<DeleteRegionalInventoryRequest,Empty> deleteRegionalInventoryCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteRegionalInventoryRequest](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-inventories/latest/com.google.shopping.merchant.inventories.v1beta.DeleteRegionalInventoryRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### insertRegionalInventoryCallable()
    
    
    public UnaryCallable<InsertRegionalInventoryRequest,RegionalInventory> insertRegionalInventoryCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[InsertRegionalInventoryRequest](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-inventories/latest/com.google.shopping.merchant.inventories.v1beta.InsertRegionalInventoryRequest),[RegionalInventory](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-inventories/latest/com.google.shopping.merchant.inventories.v1beta.RegionalInventory)>` |   
  
### listRegionalInventoriesCallable()
    
    
    public UnaryCallable<ListRegionalInventoriesRequest,ListRegionalInventoriesResponse> listRegionalInventoriesCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListRegionalInventoriesRequest](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-inventories/latest/com.google.shopping.merchant.inventories.v1beta.ListRegionalInventoriesRequest),[ListRegionalInventoriesResponse](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-inventories/latest/com.google.shopping.merchant.inventories.v1beta.ListRegionalInventoriesResponse)>` |   
  
### listRegionalInventoriesPagedCallable()
    
    
    public UnaryCallable<ListRegionalInventoriesRequest,RegionalInventoryServiceClient.ListRegionalInventoriesPagedResponse> listRegionalInventoriesPagedCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListRegionalInventoriesRequest](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-inventories/latest/com.google.shopping.merchant.inventories.v1beta.ListRegionalInventoriesRequest),[ListRegionalInventoriesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-inventories/latest/com.google.shopping.merchant.inventories.v1beta.RegionalInventoryServiceClient.ListRegionalInventoriesPagedResponse)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
