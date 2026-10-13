---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-capacityplanner/latest/com.google.cloud.capacityplanner.v1beta.stub.UsageServiceStub
title: Class UsageServiceStub (0.22.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:28:07.702143+00:00
---

# Class UsageServiceStub (0.22.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-capacityplanner/latest/com.google.cloud.capacityplanner.v1beta.stub.UsageServiceStub

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class UsageServiceStub (0.22.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.22.0 (latest)  0.18.0  0.17.0  0.16.0  0.14.0  0.11.0  0.10.0  0.8.0  0.6.0  0.5.0  0.4.0  0.3.0  0.1.0 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 
    
    
    public abstract class UsageServiceStub implements BackgroundResource

Base stub class for the UsageService service API.

This class is for advanced usage and reflects the underlying API directly.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > UsageServiceStub

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

### UsageServiceStub()
    
    
    public UsageServiceStub()

## Methods 

### close()
    
    
    public abstract void close()

### exportForecastsCallable()
    
    
    public UnaryCallable<ExportForecastsRequest,Operation> exportForecastsCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ExportForecastsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-capacityplanner/latest/com.google.cloud.capacityplanner.v1beta.ExportForecastsRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### exportForecastsOperationCallable()
    
    
    public OperationCallable<ExportForecastsRequest,ExportForecastsResponse,OperationMetadata> exportForecastsOperationCallable()

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[ExportForecastsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-capacityplanner/latest/com.google.cloud.capacityplanner.v1beta.ExportForecastsRequest),[ExportForecastsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-capacityplanner/latest/com.google.cloud.capacityplanner.v1beta.ExportForecastsResponse),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-capacityplanner/latest/com.google.cloud.capacityplanner.v1beta.OperationMetadata)>` |   
  
### exportReservationsUsageCallable()
    
    
    public UnaryCallable<ExportReservationsUsageRequest,Operation> exportReservationsUsageCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ExportReservationsUsageRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-capacityplanner/latest/com.google.cloud.capacityplanner.v1beta.ExportReservationsUsageRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### exportReservationsUsageOperationCallable()
    
    
    public OperationCallable<ExportReservationsUsageRequest,ExportReservationsUsageResponse,OperationMetadata> exportReservationsUsageOperationCallable()

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[ExportReservationsUsageRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-capacityplanner/latest/com.google.cloud.capacityplanner.v1beta.ExportReservationsUsageRequest),[ExportReservationsUsageResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-capacityplanner/latest/com.google.cloud.capacityplanner.v1beta.ExportReservationsUsageResponse),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-capacityplanner/latest/com.google.cloud.capacityplanner.v1beta.OperationMetadata)>` |   
  
### exportUsageHistoriesCallable()
    
    
    public UnaryCallable<ExportUsageHistoriesRequest,Operation> exportUsageHistoriesCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ExportUsageHistoriesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-capacityplanner/latest/com.google.cloud.capacityplanner.v1beta.ExportUsageHistoriesRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### exportUsageHistoriesOperationCallable()
    
    
    public OperationCallable<ExportUsageHistoriesRequest,ExportUsageHistoriesResponse,OperationMetadata> exportUsageHistoriesOperationCallable()

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[ExportUsageHistoriesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-capacityplanner/latest/com.google.cloud.capacityplanner.v1beta.ExportUsageHistoriesRequest),[ExportUsageHistoriesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-capacityplanner/latest/com.google.cloud.capacityplanner.v1beta.ExportUsageHistoriesResponse),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-capacityplanner/latest/com.google.cloud.capacityplanner.v1beta.OperationMetadata)>` |   
  
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
  
### queryForecastsCallable()
    
    
    public UnaryCallable<QueryForecastsRequest,QueryForecastsResponse> queryForecastsCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[QueryForecastsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-capacityplanner/latest/com.google.cloud.capacityplanner.v1beta.QueryForecastsRequest),[QueryForecastsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-capacityplanner/latest/com.google.cloud.capacityplanner.v1beta.QueryForecastsResponse)>` |   
  
### queryReservationsCallable()
    
    
    public UnaryCallable<QueryReservationsRequest,QueryReservationsResponse> queryReservationsCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[QueryReservationsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-capacityplanner/latest/com.google.cloud.capacityplanner.v1beta.QueryReservationsRequest),[QueryReservationsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-capacityplanner/latest/com.google.cloud.capacityplanner.v1beta.QueryReservationsResponse)>` |   
  
### queryUsageHistoriesCallable()
    
    
    public UnaryCallable<QueryUsageHistoriesRequest,QueryUsageHistoriesResponse> queryUsageHistoriesCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[QueryUsageHistoriesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-capacityplanner/latest/com.google.cloud.capacityplanner.v1beta.QueryUsageHistoriesRequest),[QueryUsageHistoriesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-capacityplanner/latest/com.google.cloud.capacityplanner.v1beta.QueryUsageHistoriesResponse)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
