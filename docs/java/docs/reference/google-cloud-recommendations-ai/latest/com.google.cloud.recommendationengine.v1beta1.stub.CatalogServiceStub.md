---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-recommendations-ai/latest/com.google.cloud.recommendationengine.v1beta1.stub.CatalogServiceStub
title: Class CatalogServiceStub (0.106.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:24:25.705263+00:00
---

# Class CatalogServiceStub (0.106.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-recommendations-ai/latest/com.google.cloud.recommendationengine.v1beta1.stub.CatalogServiceStub

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class CatalogServiceStub (0.106.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.106.0 (latest)  0.102.0  0.101.0  0.100.0  0.98.0  0.95.0  0.94.0  0.92.0  0.90.0  0.89.0  0.87.0  0.85.0  0.83.0  0.82.0  0.81.0  0.80.0  0.79.0  0.77.0  0.75.0  0.74.0  0.71.0  0.70.0  0.69.0  0.67.0  0.66.0  0.65.0  0.64.0  0.63.0  0.62.0  0.61.0  0.60.0  0.59.0  0.58.0  0.56.0  0.55.0  0.54.0  0.53.0  0.52.0  0.51.0  0.50.0  0.49.0  0.48.0  0.47.0  0.46.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.38.0  0.37.0  0.36.0  0.35.0  0.34.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.4  0.8.10 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 
    
    
    public abstract class CatalogServiceStub implements BackgroundResource

Base stub class for the CatalogService service API.

This class is for advanced usage and reflects the underlying API directly.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > CatalogServiceStub

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

### CatalogServiceStub()
    
    
    public CatalogServiceStub()

## Methods 

### close()
    
    
    public abstract void close()

### createCatalogItemCallable()
    
    
    public UnaryCallable<CreateCatalogItemRequest,CatalogItem> createCatalogItemCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateCatalogItemRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-recommendations-ai/latest/com.google.cloud.recommendationengine.v1beta1.CreateCatalogItemRequest),[CatalogItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-recommendations-ai/latest/com.google.cloud.recommendationengine.v1beta1.CatalogItem)>` |   
  
### deleteCatalogItemCallable()
    
    
    public UnaryCallable<DeleteCatalogItemRequest,Empty> deleteCatalogItemCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteCatalogItemRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-recommendations-ai/latest/com.google.cloud.recommendationengine.v1beta1.DeleteCatalogItemRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### getCatalogItemCallable()
    
    
    public UnaryCallable<GetCatalogItemRequest,CatalogItem> getCatalogItemCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetCatalogItemRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-recommendations-ai/latest/com.google.cloud.recommendationengine.v1beta1.GetCatalogItemRequest),[CatalogItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-recommendations-ai/latest/com.google.cloud.recommendationengine.v1beta1.CatalogItem)>` |   
  
### getHttpJsonOperationsStub()
    
    
    public @Nullable OperationsStub getHttpJsonOperationsStub()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.api.gax.httpjson.longrunning.stub.OperationsStub` |   
  
### getOperationsStub()
    
    
    public @Nullable OperationsStub getOperationsStub()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.longrunning.stub.OperationsStub` |   
  
### importCatalogItemsCallable()
    
    
    public UnaryCallable<ImportCatalogItemsRequest,Operation> importCatalogItemsCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ImportCatalogItemsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-recommendations-ai/latest/com.google.cloud.recommendationengine.v1beta1.ImportCatalogItemsRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### importCatalogItemsOperationCallable()
    
    
    public OperationCallable<ImportCatalogItemsRequest,ImportCatalogItemsResponse,ImportMetadata> importCatalogItemsOperationCallable()

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[ImportCatalogItemsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-recommendations-ai/latest/com.google.cloud.recommendationengine.v1beta1.ImportCatalogItemsRequest),[ImportCatalogItemsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-recommendations-ai/latest/com.google.cloud.recommendationengine.v1beta1.ImportCatalogItemsResponse),[ImportMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-recommendations-ai/latest/com.google.cloud.recommendationengine.v1beta1.ImportMetadata)>` |   
  
### listCatalogItemsCallable()
    
    
    public UnaryCallable<ListCatalogItemsRequest,ListCatalogItemsResponse> listCatalogItemsCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListCatalogItemsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-recommendations-ai/latest/com.google.cloud.recommendationengine.v1beta1.ListCatalogItemsRequest),[ListCatalogItemsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-recommendations-ai/latest/com.google.cloud.recommendationengine.v1beta1.ListCatalogItemsResponse)>` |   
  
### listCatalogItemsPagedCallable()
    
    
    public UnaryCallable<ListCatalogItemsRequest,CatalogServiceClient.ListCatalogItemsPagedResponse> listCatalogItemsPagedCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListCatalogItemsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-recommendations-ai/latest/com.google.cloud.recommendationengine.v1beta1.ListCatalogItemsRequest),[ListCatalogItemsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-recommendations-ai/latest/com.google.cloud.recommendationengine.v1beta1.CatalogServiceClient.ListCatalogItemsPagedResponse)>` |   
  
### updateCatalogItemCallable()
    
    
    public UnaryCallable<UpdateCatalogItemRequest,CatalogItem> updateCatalogItemCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateCatalogItemRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-recommendations-ai/latest/com.google.cloud.recommendationengine.v1beta1.UpdateCatalogItemRequest),[CatalogItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-recommendations-ai/latest/com.google.cloud.recommendationengine.v1beta1.CatalogItem)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
