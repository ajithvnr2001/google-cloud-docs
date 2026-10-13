---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.stub.SaasDeploymentsStub
title: Class SaasDeploymentsStub (0.29.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:45:38.572355+00:00
---

# Class SaasDeploymentsStub (0.29.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.stub.SaasDeploymentsStub

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class SaasDeploymentsStub (0.29.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.29.0 (latest)  0.25.0  0.24.0  0.23.0  0.21.0  0.18.0  0.17.0  0.15.0  0.13.0  0.12.0  0.10.0  0.8.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 
    
    
    public abstract class SaasDeploymentsStub implements BackgroundResource

Base stub class for the SaasDeployments service API.

This class is for advanced usage and reflects the underlying API directly.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > SaasDeploymentsStub

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

### SaasDeploymentsStub()
    
    
    public SaasDeploymentsStub()

## Methods 

### close()
    
    
    public abstract void close()

### createReleaseCallable()
    
    
    public UnaryCallable<CreateReleaseRequest,Release> createReleaseCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateReleaseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.CreateReleaseRequest),[Release](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.Release)>` |   
  
### createSaasCallable()
    
    
    public UnaryCallable<CreateSaasRequest,Saas> createSaasCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateSaasRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.CreateSaasRequest),[Saas](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.Saas)>` |   
  
### createTenantCallable()
    
    
    public UnaryCallable<CreateTenantRequest,Tenant> createTenantCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateTenantRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.CreateTenantRequest),[Tenant](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.Tenant)>` |   
  
### createUnitCallable()
    
    
    public UnaryCallable<CreateUnitRequest,Unit> createUnitCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateUnitRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.CreateUnitRequest),[Unit](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.Unit)>` |   
  
### createUnitKindCallable()
    
    
    public UnaryCallable<CreateUnitKindRequest,UnitKind> createUnitKindCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateUnitKindRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.CreateUnitKindRequest),[UnitKind](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.UnitKind)>` |   
  
### createUnitOperationCallable()
    
    
    public UnaryCallable<CreateUnitOperationRequest,UnitOperation> createUnitOperationCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateUnitOperationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.CreateUnitOperationRequest),[UnitOperation](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.UnitOperation)>` |   
  
### deleteReleaseCallable()
    
    
    public UnaryCallable<DeleteReleaseRequest,Empty> deleteReleaseCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteReleaseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.DeleteReleaseRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### deleteSaasCallable()
    
    
    public UnaryCallable<DeleteSaasRequest,Empty> deleteSaasCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteSaasRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.DeleteSaasRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### deleteTenantCallable()
    
    
    public UnaryCallable<DeleteTenantRequest,Empty> deleteTenantCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteTenantRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.DeleteTenantRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### deleteUnitCallable()
    
    
    public UnaryCallable<DeleteUnitRequest,Empty> deleteUnitCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteUnitRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.DeleteUnitRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### deleteUnitKindCallable()
    
    
    public UnaryCallable<DeleteUnitKindRequest,Empty> deleteUnitKindCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteUnitKindRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.DeleteUnitKindRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### deleteUnitOperationCallable()
    
    
    public UnaryCallable<DeleteUnitOperationRequest,Empty> deleteUnitOperationCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteUnitOperationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.DeleteUnitOperationRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### getLocationCallable()
    
    
    public UnaryCallable<GetLocationRequest,Location> getLocationCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.GetLocationRequest,com.google.cloud.location.Location>` |   
  
### getReleaseCallable()
    
    
    public UnaryCallable<GetReleaseRequest,Release> getReleaseCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetReleaseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.GetReleaseRequest),[Release](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.Release)>` |   
  
### getSaasCallable()
    
    
    public UnaryCallable<GetSaasRequest,Saas> getSaasCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetSaasRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.GetSaasRequest),[Saas](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.Saas)>` |   
  
### getTenantCallable()
    
    
    public UnaryCallable<GetTenantRequest,Tenant> getTenantCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetTenantRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.GetTenantRequest),[Tenant](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.Tenant)>` |   
  
### getUnitCallable()
    
    
    public UnaryCallable<GetUnitRequest,Unit> getUnitCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetUnitRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.GetUnitRequest),[Unit](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.Unit)>` |   
  
### getUnitKindCallable()
    
    
    public UnaryCallable<GetUnitKindRequest,UnitKind> getUnitKindCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetUnitKindRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.GetUnitKindRequest),[UnitKind](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.UnitKind)>` |   
  
### getUnitOperationCallable()
    
    
    public UnaryCallable<GetUnitOperationRequest,UnitOperation> getUnitOperationCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetUnitOperationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.GetUnitOperationRequest),[UnitOperation](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.UnitOperation)>` |   
  
### listLocationsCallable()
    
    
    public UnaryCallable<ListLocationsRequest,ListLocationsResponse> listLocationsCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.ListLocationsRequest,com.google.cloud.location.ListLocationsResponse>` |   
  
### listLocationsPagedCallable()
    
    
    public UnaryCallable<ListLocationsRequest,SaasDeploymentsClient.ListLocationsPagedResponse> listLocationsPagedCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.ListLocationsRequest,[ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeploymentsClient.ListLocationsPagedResponse)>` |   
  
### listReleasesCallable()
    
    
    public UnaryCallable<ListReleasesRequest,ListReleasesResponse> listReleasesCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListReleasesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.ListReleasesRequest),[ListReleasesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.ListReleasesResponse)>` |   
  
### listReleasesPagedCallable()
    
    
    public UnaryCallable<ListReleasesRequest,SaasDeploymentsClient.ListReleasesPagedResponse> listReleasesPagedCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListReleasesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.ListReleasesRequest),[ListReleasesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeploymentsClient.ListReleasesPagedResponse)>` |   
  
### listSaasCallable()
    
    
    public UnaryCallable<ListSaasRequest,ListSaasResponse> listSaasCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListSaasRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.ListSaasRequest),[ListSaasResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.ListSaasResponse)>` |   
  
### listSaasPagedCallable()
    
    
    public UnaryCallable<ListSaasRequest,SaasDeploymentsClient.ListSaasPagedResponse> listSaasPagedCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListSaasRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.ListSaasRequest),[ListSaasPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeploymentsClient.ListSaasPagedResponse)>` |   
  
### listTenantsCallable()
    
    
    public UnaryCallable<ListTenantsRequest,ListTenantsResponse> listTenantsCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListTenantsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.ListTenantsRequest),[ListTenantsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.ListTenantsResponse)>` |   
  
### listTenantsPagedCallable()
    
    
    public UnaryCallable<ListTenantsRequest,SaasDeploymentsClient.ListTenantsPagedResponse> listTenantsPagedCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListTenantsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.ListTenantsRequest),[ListTenantsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeploymentsClient.ListTenantsPagedResponse)>` |   
  
### listUnitKindsCallable()
    
    
    public UnaryCallable<ListUnitKindsRequest,ListUnitKindsResponse> listUnitKindsCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListUnitKindsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.ListUnitKindsRequest),[ListUnitKindsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.ListUnitKindsResponse)>` |   
  
### listUnitKindsPagedCallable()
    
    
    public UnaryCallable<ListUnitKindsRequest,SaasDeploymentsClient.ListUnitKindsPagedResponse> listUnitKindsPagedCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListUnitKindsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.ListUnitKindsRequest),[ListUnitKindsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeploymentsClient.ListUnitKindsPagedResponse)>` |   
  
### listUnitOperationsCallable()
    
    
    public UnaryCallable<ListUnitOperationsRequest,ListUnitOperationsResponse> listUnitOperationsCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListUnitOperationsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.ListUnitOperationsRequest),[ListUnitOperationsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.ListUnitOperationsResponse)>` |   
  
### listUnitOperationsPagedCallable()
    
    
    public UnaryCallable<ListUnitOperationsRequest,SaasDeploymentsClient.ListUnitOperationsPagedResponse> listUnitOperationsPagedCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListUnitOperationsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.ListUnitOperationsRequest),[ListUnitOperationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeploymentsClient.ListUnitOperationsPagedResponse)>` |   
  
### listUnitsCallable()
    
    
    public UnaryCallable<ListUnitsRequest,ListUnitsResponse> listUnitsCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListUnitsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.ListUnitsRequest),[ListUnitsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.ListUnitsResponse)>` |   
  
### listUnitsPagedCallable()
    
    
    public UnaryCallable<ListUnitsRequest,SaasDeploymentsClient.ListUnitsPagedResponse> listUnitsPagedCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListUnitsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.ListUnitsRequest),[ListUnitsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeploymentsClient.ListUnitsPagedResponse)>` |   
  
### updateReleaseCallable()
    
    
    public UnaryCallable<UpdateReleaseRequest,Release> updateReleaseCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateReleaseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.UpdateReleaseRequest),[Release](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.Release)>` |   
  
### updateSaasCallable()
    
    
    public UnaryCallable<UpdateSaasRequest,Saas> updateSaasCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateSaasRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.UpdateSaasRequest),[Saas](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.Saas)>` |   
  
### updateTenantCallable()
    
    
    public UnaryCallable<UpdateTenantRequest,Tenant> updateTenantCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateTenantRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.UpdateTenantRequest),[Tenant](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.Tenant)>` |   
  
### updateUnitCallable()
    
    
    public UnaryCallable<UpdateUnitRequest,Unit> updateUnitCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateUnitRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.UpdateUnitRequest),[Unit](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.Unit)>` |   
  
### updateUnitKindCallable()
    
    
    public UnaryCallable<UpdateUnitKindRequest,UnitKind> updateUnitKindCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateUnitKindRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.UpdateUnitKindRequest),[UnitKind](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.UnitKind)>` |   
  
### updateUnitOperationCallable()
    
    
    public UnaryCallable<UpdateUnitOperationRequest,UnitOperation> updateUnitOperationCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateUnitOperationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.UpdateUnitOperationRequest),[UnitOperation](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.UnitOperation)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
