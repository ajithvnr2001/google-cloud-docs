---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-service-usage/latest/com.google.api.serviceusage.v1beta1.stub.ServiceUsageStub
title: Class ServiceUsageStub (2.99.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:40:15.071555+00:00
---

# Class ServiceUsageStub (2.99.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-service-usage/latest/com.google.api.serviceusage.v1beta1.stub.ServiceUsageStub

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class ServiceUsageStub (2.99.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.99.0 (latest)  2.95.0  2.94.0  2.93.0  2.91.0  2.88.0  2.87.0  2.85.0  2.83.0  2.82.0  2.80.0  2.78.0  2.76.0  2.75.0  2.74.0  2.73.0  2.72.0  2.70.0  2.68.0  2.67.0  2.64.0  2.63.0  2.62.0  2.60.0  2.59.0  2.58.0  2.57.0  2.56.0  2.55.0  2.54.0  2.53.0  2.52.0  2.51.0  2.49.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.39.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.0  2.27.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.7  2.2.8 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 
    
    
    public abstract class ServiceUsageStub implements BackgroundResource

Base stub class for the ServiceUsage service API.

This class is for advanced usage and reflects the underlying API directly.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > ServiceUsageStub

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

### ServiceUsageStub()
    
    
    public ServiceUsageStub()

## Methods 

### batchEnableServicesCallable() (deprecated)
    
    
    public UnaryCallable<BatchEnableServicesRequest,Operation> batchEnableServicesCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchEnableServicesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-service-usage/latest/com.google.api.serviceusage.v1beta1.BatchEnableServicesRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### batchEnableServicesOperationCallable() (deprecated)
    
    
    public OperationCallable<BatchEnableServicesRequest,Empty,OperationMetadata> batchEnableServicesOperationCallable()

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[BatchEnableServicesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-service-usage/latest/com.google.api.serviceusage.v1beta1.BatchEnableServicesRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-service-usage/latest/com.google.api.serviceusage.v1beta1.OperationMetadata)>` |   
  
### close()
    
    
    public abstract void close()

### createAdminOverrideCallable()
    
    
    public UnaryCallable<CreateAdminOverrideRequest,Operation> createAdminOverrideCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateAdminOverrideRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-service-usage/latest/com.google.api.serviceusage.v1beta1.CreateAdminOverrideRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createAdminOverrideOperationCallable()
    
    
    public OperationCallable<CreateAdminOverrideRequest,QuotaOverride,OperationMetadata> createAdminOverrideOperationCallable()

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateAdminOverrideRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-service-usage/latest/com.google.api.serviceusage.v1beta1.CreateAdminOverrideRequest),[QuotaOverride](https://docs.cloud.google.com/java/docs/reference/google-cloud-service-usage/latest/com.google.api.serviceusage.v1beta1.QuotaOverride),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-service-usage/latest/com.google.api.serviceusage.v1beta1.OperationMetadata)>` |   
  
### createConsumerOverrideCallable()
    
    
    public UnaryCallable<CreateConsumerOverrideRequest,Operation> createConsumerOverrideCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateConsumerOverrideRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-service-usage/latest/com.google.api.serviceusage.v1beta1.CreateConsumerOverrideRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createConsumerOverrideOperationCallable()
    
    
    public OperationCallable<CreateConsumerOverrideRequest,QuotaOverride,OperationMetadata> createConsumerOverrideOperationCallable()

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateConsumerOverrideRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-service-usage/latest/com.google.api.serviceusage.v1beta1.CreateConsumerOverrideRequest),[QuotaOverride](https://docs.cloud.google.com/java/docs/reference/google-cloud-service-usage/latest/com.google.api.serviceusage.v1beta1.QuotaOverride),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-service-usage/latest/com.google.api.serviceusage.v1beta1.OperationMetadata)>` |   
  
### deleteAdminOverrideCallable()
    
    
    public UnaryCallable<DeleteAdminOverrideRequest,Operation> deleteAdminOverrideCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteAdminOverrideRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-service-usage/latest/com.google.api.serviceusage.v1beta1.DeleteAdminOverrideRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteAdminOverrideOperationCallable()
    
    
    public OperationCallable<DeleteAdminOverrideRequest,Empty,OperationMetadata> deleteAdminOverrideOperationCallable()

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteAdminOverrideRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-service-usage/latest/com.google.api.serviceusage.v1beta1.DeleteAdminOverrideRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-service-usage/latest/com.google.api.serviceusage.v1beta1.OperationMetadata)>` |   
  
### deleteConsumerOverrideCallable()
    
    
    public UnaryCallable<DeleteConsumerOverrideRequest,Operation> deleteConsumerOverrideCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteConsumerOverrideRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-service-usage/latest/com.google.api.serviceusage.v1beta1.DeleteConsumerOverrideRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteConsumerOverrideOperationCallable()
    
    
    public OperationCallable<DeleteConsumerOverrideRequest,Empty,OperationMetadata> deleteConsumerOverrideOperationCallable()

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteConsumerOverrideRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-service-usage/latest/com.google.api.serviceusage.v1beta1.DeleteConsumerOverrideRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-service-usage/latest/com.google.api.serviceusage.v1beta1.OperationMetadata)>` |   
  
### disableServiceCallable() (deprecated)
    
    
    public UnaryCallable<DisableServiceRequest,Operation> disableServiceCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DisableServiceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-service-usage/latest/com.google.api.serviceusage.v1beta1.DisableServiceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### disableServiceOperationCallable() (deprecated)
    
    
    public OperationCallable<DisableServiceRequest,Empty,OperationMetadata> disableServiceOperationCallable()

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DisableServiceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-service-usage/latest/com.google.api.serviceusage.v1beta1.DisableServiceRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-service-usage/latest/com.google.api.serviceusage.v1beta1.OperationMetadata)>` |   
  
### enableServiceCallable() (deprecated)
    
    
    public UnaryCallable<EnableServiceRequest,Operation> enableServiceCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[EnableServiceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-service-usage/latest/com.google.api.serviceusage.v1beta1.EnableServiceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### enableServiceOperationCallable() (deprecated)
    
    
    public OperationCallable<EnableServiceRequest,Empty,OperationMetadata> enableServiceOperationCallable()

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[EnableServiceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-service-usage/latest/com.google.api.serviceusage.v1beta1.EnableServiceRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-service-usage/latest/com.google.api.serviceusage.v1beta1.OperationMetadata)>` |   
  
### generateServiceIdentityCallable()
    
    
    public UnaryCallable<GenerateServiceIdentityRequest,Operation> generateServiceIdentityCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GenerateServiceIdentityRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-service-usage/latest/com.google.api.serviceusage.v1beta1.GenerateServiceIdentityRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### generateServiceIdentityOperationCallable()
    
    
    public OperationCallable<GenerateServiceIdentityRequest,ServiceIdentity,Empty> generateServiceIdentityOperationCallable()

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[GenerateServiceIdentityRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-service-usage/latest/com.google.api.serviceusage.v1beta1.GenerateServiceIdentityRequest),[ServiceIdentity](https://docs.cloud.google.com/java/docs/reference/google-cloud-service-usage/latest/com.google.api.serviceusage.v1beta1.ServiceIdentity),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### getConsumerQuotaLimitCallable()
    
    
    public UnaryCallable<GetConsumerQuotaLimitRequest,ConsumerQuotaLimit> getConsumerQuotaLimitCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetConsumerQuotaLimitRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-service-usage/latest/com.google.api.serviceusage.v1beta1.GetConsumerQuotaLimitRequest),[ConsumerQuotaLimit](https://docs.cloud.google.com/java/docs/reference/google-cloud-service-usage/latest/com.google.api.serviceusage.v1beta1.ConsumerQuotaLimit)>` |   
  
### getConsumerQuotaMetricCallable()
    
    
    public UnaryCallable<GetConsumerQuotaMetricRequest,ConsumerQuotaMetric> getConsumerQuotaMetricCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetConsumerQuotaMetricRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-service-usage/latest/com.google.api.serviceusage.v1beta1.GetConsumerQuotaMetricRequest),[ConsumerQuotaMetric](https://docs.cloud.google.com/java/docs/reference/google-cloud-service-usage/latest/com.google.api.serviceusage.v1beta1.ConsumerQuotaMetric)>` |   
  
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
  
### getServiceCallable() (deprecated)
    
    
    public UnaryCallable<GetServiceRequest,Service> getServiceCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetServiceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-service-usage/latest/com.google.api.serviceusage.v1beta1.GetServiceRequest),[Service](https://docs.cloud.google.com/java/docs/reference/google-cloud-service-usage/latest/com.google.api.serviceusage.v1beta1.Service)>` |   
  
### importAdminOverridesCallable()
    
    
    public UnaryCallable<ImportAdminOverridesRequest,Operation> importAdminOverridesCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ImportAdminOverridesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-service-usage/latest/com.google.api.serviceusage.v1beta1.ImportAdminOverridesRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### importAdminOverridesOperationCallable()
    
    
    public OperationCallable<ImportAdminOverridesRequest,ImportAdminOverridesResponse,ImportAdminOverridesMetadata> importAdminOverridesOperationCallable()

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[ImportAdminOverridesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-service-usage/latest/com.google.api.serviceusage.v1beta1.ImportAdminOverridesRequest),[ImportAdminOverridesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-service-usage/latest/com.google.api.serviceusage.v1beta1.ImportAdminOverridesResponse),[ImportAdminOverridesMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-service-usage/latest/com.google.api.serviceusage.v1beta1.ImportAdminOverridesMetadata)>` |   
  
### importConsumerOverridesCallable()
    
    
    public UnaryCallable<ImportConsumerOverridesRequest,Operation> importConsumerOverridesCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ImportConsumerOverridesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-service-usage/latest/com.google.api.serviceusage.v1beta1.ImportConsumerOverridesRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### importConsumerOverridesOperationCallable()
    
    
    public OperationCallable<ImportConsumerOverridesRequest,ImportConsumerOverridesResponse,ImportConsumerOverridesMetadata> importConsumerOverridesOperationCallable()

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[ImportConsumerOverridesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-service-usage/latest/com.google.api.serviceusage.v1beta1.ImportConsumerOverridesRequest),[ImportConsumerOverridesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-service-usage/latest/com.google.api.serviceusage.v1beta1.ImportConsumerOverridesResponse),[ImportConsumerOverridesMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-service-usage/latest/com.google.api.serviceusage.v1beta1.ImportConsumerOverridesMetadata)>` |   
  
### listAdminOverridesCallable()
    
    
    public UnaryCallable<ListAdminOverridesRequest,ListAdminOverridesResponse> listAdminOverridesCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListAdminOverridesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-service-usage/latest/com.google.api.serviceusage.v1beta1.ListAdminOverridesRequest),[ListAdminOverridesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-service-usage/latest/com.google.api.serviceusage.v1beta1.ListAdminOverridesResponse)>` |   
  
### listAdminOverridesPagedCallable()
    
    
    public UnaryCallable<ListAdminOverridesRequest,ServiceUsageClient.ListAdminOverridesPagedResponse> listAdminOverridesPagedCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListAdminOverridesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-service-usage/latest/com.google.api.serviceusage.v1beta1.ListAdminOverridesRequest),[ListAdminOverridesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-service-usage/latest/com.google.api.serviceusage.v1beta1.ServiceUsageClient.ListAdminOverridesPagedResponse)>` |   
  
### listConsumerOverridesCallable()
    
    
    public UnaryCallable<ListConsumerOverridesRequest,ListConsumerOverridesResponse> listConsumerOverridesCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListConsumerOverridesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-service-usage/latest/com.google.api.serviceusage.v1beta1.ListConsumerOverridesRequest),[ListConsumerOverridesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-service-usage/latest/com.google.api.serviceusage.v1beta1.ListConsumerOverridesResponse)>` |   
  
### listConsumerOverridesPagedCallable()
    
    
    public UnaryCallable<ListConsumerOverridesRequest,ServiceUsageClient.ListConsumerOverridesPagedResponse> listConsumerOverridesPagedCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListConsumerOverridesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-service-usage/latest/com.google.api.serviceusage.v1beta1.ListConsumerOverridesRequest),[ListConsumerOverridesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-service-usage/latest/com.google.api.serviceusage.v1beta1.ServiceUsageClient.ListConsumerOverridesPagedResponse)>` |   
  
### listConsumerQuotaMetricsCallable()
    
    
    public UnaryCallable<ListConsumerQuotaMetricsRequest,ListConsumerQuotaMetricsResponse> listConsumerQuotaMetricsCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListConsumerQuotaMetricsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-service-usage/latest/com.google.api.serviceusage.v1beta1.ListConsumerQuotaMetricsRequest),[ListConsumerQuotaMetricsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-service-usage/latest/com.google.api.serviceusage.v1beta1.ListConsumerQuotaMetricsResponse)>` |   
  
### listConsumerQuotaMetricsPagedCallable()
    
    
    public UnaryCallable<ListConsumerQuotaMetricsRequest,ServiceUsageClient.ListConsumerQuotaMetricsPagedResponse> listConsumerQuotaMetricsPagedCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListConsumerQuotaMetricsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-service-usage/latest/com.google.api.serviceusage.v1beta1.ListConsumerQuotaMetricsRequest),[ListConsumerQuotaMetricsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-service-usage/latest/com.google.api.serviceusage.v1beta1.ServiceUsageClient.ListConsumerQuotaMetricsPagedResponse)>` |   
  
### listServicesCallable() (deprecated)
    
    
    public UnaryCallable<ListServicesRequest,ListServicesResponse> listServicesCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListServicesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-service-usage/latest/com.google.api.serviceusage.v1beta1.ListServicesRequest),[ListServicesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-service-usage/latest/com.google.api.serviceusage.v1beta1.ListServicesResponse)>` |   
  
### listServicesPagedCallable() (deprecated)
    
    
    public UnaryCallable<ListServicesRequest,ServiceUsageClient.ListServicesPagedResponse> listServicesPagedCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListServicesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-service-usage/latest/com.google.api.serviceusage.v1beta1.ListServicesRequest),[ListServicesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-service-usage/latest/com.google.api.serviceusage.v1beta1.ServiceUsageClient.ListServicesPagedResponse)>` |   
  
### updateAdminOverrideCallable()
    
    
    public UnaryCallable<UpdateAdminOverrideRequest,Operation> updateAdminOverrideCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateAdminOverrideRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-service-usage/latest/com.google.api.serviceusage.v1beta1.UpdateAdminOverrideRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateAdminOverrideOperationCallable()
    
    
    public OperationCallable<UpdateAdminOverrideRequest,QuotaOverride,OperationMetadata> updateAdminOverrideOperationCallable()

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdateAdminOverrideRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-service-usage/latest/com.google.api.serviceusage.v1beta1.UpdateAdminOverrideRequest),[QuotaOverride](https://docs.cloud.google.com/java/docs/reference/google-cloud-service-usage/latest/com.google.api.serviceusage.v1beta1.QuotaOverride),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-service-usage/latest/com.google.api.serviceusage.v1beta1.OperationMetadata)>` |   
  
### updateConsumerOverrideCallable()
    
    
    public UnaryCallable<UpdateConsumerOverrideRequest,Operation> updateConsumerOverrideCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateConsumerOverrideRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-service-usage/latest/com.google.api.serviceusage.v1beta1.UpdateConsumerOverrideRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateConsumerOverrideOperationCallable()
    
    
    public OperationCallable<UpdateConsumerOverrideRequest,QuotaOverride,OperationMetadata> updateConsumerOverrideOperationCallable()

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdateConsumerOverrideRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-service-usage/latest/com.google.api.serviceusage.v1beta1.UpdateConsumerOverrideRequest),[QuotaOverride](https://docs.cloud.google.com/java/docs/reference/google-cloud-service-usage/latest/com.google.api.serviceusage.v1beta1.QuotaOverride),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-service-usage/latest/com.google.api.serviceusage.v1beta1.OperationMetadata)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
