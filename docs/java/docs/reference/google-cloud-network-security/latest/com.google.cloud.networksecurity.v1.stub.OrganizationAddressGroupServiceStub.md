---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.stub.OrganizationAddressGroupServiceStub
title: Class OrganizationAddressGroupServiceStub (0.102.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:47:01.162362+00:00
---

# Class OrganizationAddressGroupServiceStub (0.102.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.stub.OrganizationAddressGroupServiceStub

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class OrganizationAddressGroupServiceStub (0.102.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.102.0 (latest)  0.98.0  0.97.0  0.96.0  0.94.0  0.91.0  0.90.0  0.88.0  0.86.0  0.85.0  0.83.0  0.81.0  0.79.0  0.78.0  0.77.0  0.76.0  0.75.0  0.73.0  0.71.0  0.70.0  0.67.0  0.66.0  0.65.0  0.63.0  0.62.0  0.61.0  0.60.0  0.59.0  0.58.0  0.57.0  0.56.0  0.55.0  0.54.0  0.52.0  0.51.0  0.50.0  0.49.0  0.48.0  0.47.0  0.46.0  0.45.0  0.44.0  0.43.0  0.42.0  0.40.0  0.39.0  0.38.0  0.37.0  0.36.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.30.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.4  0.5.1  0.4.4 
    
    
    public abstract class OrganizationAddressGroupServiceStub implements BackgroundResource

Base stub class for the OrganizationAddressGroupService service API.

This class is for advanced usage and reflects the underlying API directly.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > OrganizationAddressGroupServiceStub

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

### OrganizationAddressGroupServiceStub()
    
    
    public OrganizationAddressGroupServiceStub()

## Methods 

### addAddressGroupItemsCallable()
    
    
    public UnaryCallable<AddAddressGroupItemsRequest,Operation> addAddressGroupItemsCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[AddAddressGroupItemsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.AddAddressGroupItemsRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### addAddressGroupItemsOperationCallable()
    
    
    public OperationCallable<AddAddressGroupItemsRequest,AddressGroup,OperationMetadata> addAddressGroupItemsOperationCallable()

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[AddAddressGroupItemsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.AddAddressGroupItemsRequest),[AddressGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.AddressGroup),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.OperationMetadata)>` |   
  
### cloneAddressGroupItemsCallable()
    
    
    public UnaryCallable<CloneAddressGroupItemsRequest,Operation> cloneAddressGroupItemsCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CloneAddressGroupItemsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.CloneAddressGroupItemsRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### cloneAddressGroupItemsOperationCallable()
    
    
    public OperationCallable<CloneAddressGroupItemsRequest,AddressGroup,OperationMetadata> cloneAddressGroupItemsOperationCallable()

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CloneAddressGroupItemsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.CloneAddressGroupItemsRequest),[AddressGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.AddressGroup),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.OperationMetadata)>` |   
  
### close()
    
    
    public abstract void close()

### createAddressGroupCallable()
    
    
    public UnaryCallable<CreateAddressGroupRequest,Operation> createAddressGroupCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateAddressGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.CreateAddressGroupRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createAddressGroupOperationCallable()
    
    
    public OperationCallable<CreateAddressGroupRequest,AddressGroup,OperationMetadata> createAddressGroupOperationCallable()

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateAddressGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.CreateAddressGroupRequest),[AddressGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.AddressGroup),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.OperationMetadata)>` |   
  
### deleteAddressGroupCallable()
    
    
    public UnaryCallable<DeleteAddressGroupRequest,Operation> deleteAddressGroupCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteAddressGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.DeleteAddressGroupRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteAddressGroupOperationCallable()
    
    
    public OperationCallable<DeleteAddressGroupRequest,Empty,OperationMetadata> deleteAddressGroupOperationCallable()

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteAddressGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.DeleteAddressGroupRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.OperationMetadata)>` |   
  
### getAddressGroupCallable()
    
    
    public UnaryCallable<GetAddressGroupRequest,AddressGroup> getAddressGroupCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetAddressGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.GetAddressGroupRequest),[AddressGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.AddressGroup)>` |   
  
### getIamPolicyCallable()
    
    
    public UnaryCallable<GetIamPolicyRequest,Policy> getIamPolicyCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.iam.v1.GetIamPolicyRequest,com.google.iam.v1.Policy>` |   
  
### getLocationCallable()
    
    
    public UnaryCallable<GetLocationRequest,Location> getLocationCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.GetLocationRequest,com.google.cloud.location.Location>` |   
  
### getOperationsStub()
    
    
    public @Nullable OperationsStub getOperationsStub()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.longrunning.stub.OperationsStub` |   
  
### listAddressGroupReferencesCallable()
    
    
    public UnaryCallable<ListAddressGroupReferencesRequest,ListAddressGroupReferencesResponse> listAddressGroupReferencesCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListAddressGroupReferencesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.ListAddressGroupReferencesRequest),[ListAddressGroupReferencesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.ListAddressGroupReferencesResponse)>` |   
  
### listAddressGroupReferencesPagedCallable()
    
    
    public UnaryCallable<ListAddressGroupReferencesRequest,OrganizationAddressGroupServiceClient.ListAddressGroupReferencesPagedResponse> listAddressGroupReferencesPagedCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListAddressGroupReferencesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.ListAddressGroupReferencesRequest),[ListAddressGroupReferencesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.OrganizationAddressGroupServiceClient.ListAddressGroupReferencesPagedResponse)>` |   
  
### listAddressGroupsCallable()
    
    
    public UnaryCallable<ListAddressGroupsRequest,ListAddressGroupsResponse> listAddressGroupsCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListAddressGroupsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.ListAddressGroupsRequest),[ListAddressGroupsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.ListAddressGroupsResponse)>` |   
  
### listAddressGroupsPagedCallable()
    
    
    public UnaryCallable<ListAddressGroupsRequest,OrganizationAddressGroupServiceClient.ListAddressGroupsPagedResponse> listAddressGroupsPagedCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListAddressGroupsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.ListAddressGroupsRequest),[ListAddressGroupsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.OrganizationAddressGroupServiceClient.ListAddressGroupsPagedResponse)>` |   
  
### listLocationsCallable()
    
    
    public UnaryCallable<ListLocationsRequest,ListLocationsResponse> listLocationsCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.ListLocationsRequest,com.google.cloud.location.ListLocationsResponse>` |   
  
### listLocationsPagedCallable()
    
    
    public UnaryCallable<ListLocationsRequest,OrganizationAddressGroupServiceClient.ListLocationsPagedResponse> listLocationsPagedCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.ListLocationsRequest,[ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.OrganizationAddressGroupServiceClient.ListLocationsPagedResponse)>` |   
  
### removeAddressGroupItemsCallable()
    
    
    public UnaryCallable<RemoveAddressGroupItemsRequest,Operation> removeAddressGroupItemsCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[RemoveAddressGroupItemsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.RemoveAddressGroupItemsRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### removeAddressGroupItemsOperationCallable()
    
    
    public OperationCallable<RemoveAddressGroupItemsRequest,AddressGroup,OperationMetadata> removeAddressGroupItemsOperationCallable()

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[RemoveAddressGroupItemsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.RemoveAddressGroupItemsRequest),[AddressGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.AddressGroup),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.OperationMetadata)>` |   
  
### setIamPolicyCallable()
    
    
    public UnaryCallable<SetIamPolicyRequest,Policy> setIamPolicyCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.iam.v1.SetIamPolicyRequest,com.google.iam.v1.Policy>` |   
  
### testIamPermissionsCallable()
    
    
    public UnaryCallable<TestIamPermissionsRequest,TestIamPermissionsResponse> testIamPermissionsCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.iam.v1.TestIamPermissionsRequest,com.google.iam.v1.TestIamPermissionsResponse>` |   
  
### updateAddressGroupCallable()
    
    
    public UnaryCallable<UpdateAddressGroupRequest,Operation> updateAddressGroupCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateAddressGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.UpdateAddressGroupRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateAddressGroupOperationCallable()
    
    
    public OperationCallable<UpdateAddressGroupRequest,AddressGroup,OperationMetadata> updateAddressGroupOperationCallable()

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdateAddressGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.UpdateAddressGroupRequest),[AddressGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.AddressGroup),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.OperationMetadata)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
