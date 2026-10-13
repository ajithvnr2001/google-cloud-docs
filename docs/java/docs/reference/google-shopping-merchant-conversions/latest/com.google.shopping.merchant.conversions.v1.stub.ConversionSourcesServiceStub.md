---
url: https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-conversions/latest/com.google.shopping.merchant.conversions.v1.stub.ConversionSourcesServiceStub
title: Class ConversionSourcesServiceStub (1.27.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:14:57.284998+00:00
---

# Class ConversionSourcesServiceStub (1.27.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-conversions/latest/com.google.shopping.merchant.conversions.v1.stub.ConversionSourcesServiceStub

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class ConversionSourcesServiceStub (1.27.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.27.0 (latest)  1.23.0  1.22.0  1.21.0  1.19.0  1.16.0  1.15.0  1.13.0  1.11.0  1.10.0  1.8.0  1.6.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0  0.29.0  0.27.0  0.26.0  0.23.0  0.22.0  0.21.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public abstract class ConversionSourcesServiceStub implements BackgroundResource

Base stub class for the ConversionSourcesService service API.

This class is for advanced usage and reflects the underlying API directly.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > ConversionSourcesServiceStub

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

### ConversionSourcesServiceStub()
    
    
    public ConversionSourcesServiceStub()

## Methods 

### close()
    
    
    public abstract void close()

### createConversionSourceCallable()
    
    
    public UnaryCallable<CreateConversionSourceRequest,ConversionSource> createConversionSourceCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateConversionSourceRequest](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-conversions/latest/com.google.shopping.merchant.conversions.v1.CreateConversionSourceRequest),[ConversionSource](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-conversions/latest/com.google.shopping.merchant.conversions.v1.ConversionSource)>` |   
  
### deleteConversionSourceCallable()
    
    
    public UnaryCallable<DeleteConversionSourceRequest,Empty> deleteConversionSourceCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteConversionSourceRequest](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-conversions/latest/com.google.shopping.merchant.conversions.v1.DeleteConversionSourceRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### getConversionSourceCallable()
    
    
    public UnaryCallable<GetConversionSourceRequest,ConversionSource> getConversionSourceCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetConversionSourceRequest](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-conversions/latest/com.google.shopping.merchant.conversions.v1.GetConversionSourceRequest),[ConversionSource](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-conversions/latest/com.google.shopping.merchant.conversions.v1.ConversionSource)>` |   
  
### listConversionSourcesCallable()
    
    
    public UnaryCallable<ListConversionSourcesRequest,ListConversionSourcesResponse> listConversionSourcesCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListConversionSourcesRequest](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-conversions/latest/com.google.shopping.merchant.conversions.v1.ListConversionSourcesRequest),[ListConversionSourcesResponse](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-conversions/latest/com.google.shopping.merchant.conversions.v1.ListConversionSourcesResponse)>` |   
  
### listConversionSourcesPagedCallable()
    
    
    public UnaryCallable<ListConversionSourcesRequest,ConversionSourcesServiceClient.ListConversionSourcesPagedResponse> listConversionSourcesPagedCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListConversionSourcesRequest](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-conversions/latest/com.google.shopping.merchant.conversions.v1.ListConversionSourcesRequest),[ListConversionSourcesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-conversions/latest/com.google.shopping.merchant.conversions.v1.ConversionSourcesServiceClient.ListConversionSourcesPagedResponse)>` |   
  
### undeleteConversionSourceCallable()
    
    
    public UnaryCallable<UndeleteConversionSourceRequest,ConversionSource> undeleteConversionSourceCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UndeleteConversionSourceRequest](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-conversions/latest/com.google.shopping.merchant.conversions.v1.UndeleteConversionSourceRequest),[ConversionSource](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-conversions/latest/com.google.shopping.merchant.conversions.v1.ConversionSource)>` |   
  
### updateConversionSourceCallable()
    
    
    public UnaryCallable<UpdateConversionSourceRequest,ConversionSource> updateConversionSourceCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateConversionSourceRequest](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-conversions/latest/com.google.shopping.merchant.conversions.v1.UpdateConversionSourceRequest),[ConversionSource](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-conversions/latest/com.google.shopping.merchant.conversions.v1.ConversionSource)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
