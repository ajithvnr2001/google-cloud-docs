---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-beyondcorp-appconnectors/latest/com.google.cloud.beyondcorp.appconnectors.v1.stub.AppConnectorsServiceStub
title: Class AppConnectorsServiceStub (0.97.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:00:28.804212+00:00
---

# Class AppConnectorsServiceStub (0.97.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-beyondcorp-appconnectors/latest/com.google.cloud.beyondcorp.appconnectors.v1.stub.AppConnectorsServiceStub

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class AppConnectorsServiceStub (0.97.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.97.0 (latest)  0.93.0  0.92.0  0.91.0  0.89.0  0.86.0  0.85.0  0.83.0  0.81.0  0.80.0  0.79.0  0.78.0  0.76.0  0.74.0  0.73.0  0.72.0  0.71.0  0.70.0  0.68.0  0.66.0  0.65.0  0.62.0  0.61.0  0.60.0  0.58.0  0.57.0  0.56.0  0.55.0  0.54.0  0.53.0  0.52.0  0.51.0  0.50.0  0.49.0  0.47.0  0.46.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.38.0  0.37.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.25.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public abstract class AppConnectorsServiceStub implements BackgroundResource

Base stub class for the AppConnectorsService service API.

This class is for advanced usage and reflects the underlying API directly.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > AppConnectorsServiceStub

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

### AppConnectorsServiceStub()
    
    
    public AppConnectorsServiceStub()

## Methods 

### close()
    
    
    public abstract void close()

### createAppConnectorCallable()
    
    
    public UnaryCallable<CreateAppConnectorRequest,Operation> createAppConnectorCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateAppConnectorRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-beyondcorp-appconnectors/latest/com.google.cloud.beyondcorp.appconnectors.v1.CreateAppConnectorRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createAppConnectorOperationCallable()
    
    
    public OperationCallable<CreateAppConnectorRequest,AppConnector,AppConnectorOperationMetadata> createAppConnectorOperationCallable()

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateAppConnectorRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-beyondcorp-appconnectors/latest/com.google.cloud.beyondcorp.appconnectors.v1.CreateAppConnectorRequest),[AppConnector](https://docs.cloud.google.com/java/docs/reference/google-cloud-beyondcorp-appconnectors/latest/com.google.cloud.beyondcorp.appconnectors.v1.AppConnector),[AppConnectorOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-beyondcorp-appconnectors/latest/com.google.cloud.beyondcorp.appconnectors.v1.AppConnectorOperationMetadata)>` |   
  
### deleteAppConnectorCallable()
    
    
    public UnaryCallable<DeleteAppConnectorRequest,Operation> deleteAppConnectorCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteAppConnectorRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-beyondcorp-appconnectors/latest/com.google.cloud.beyondcorp.appconnectors.v1.DeleteAppConnectorRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteAppConnectorOperationCallable()
    
    
    public OperationCallable<DeleteAppConnectorRequest,Empty,AppConnectorOperationMetadata> deleteAppConnectorOperationCallable()

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteAppConnectorRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-beyondcorp-appconnectors/latest/com.google.cloud.beyondcorp.appconnectors.v1.DeleteAppConnectorRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[AppConnectorOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-beyondcorp-appconnectors/latest/com.google.cloud.beyondcorp.appconnectors.v1.AppConnectorOperationMetadata)>` |   
  
### getAppConnectorCallable()
    
    
    public UnaryCallable<GetAppConnectorRequest,AppConnector> getAppConnectorCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetAppConnectorRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-beyondcorp-appconnectors/latest/com.google.cloud.beyondcorp.appconnectors.v1.GetAppConnectorRequest),[AppConnector](https://docs.cloud.google.com/java/docs/reference/google-cloud-beyondcorp-appconnectors/latest/com.google.cloud.beyondcorp.appconnectors.v1.AppConnector)>` |   
  
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
  
### listAppConnectorsCallable()
    
    
    public UnaryCallable<ListAppConnectorsRequest,ListAppConnectorsResponse> listAppConnectorsCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListAppConnectorsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-beyondcorp-appconnectors/latest/com.google.cloud.beyondcorp.appconnectors.v1.ListAppConnectorsRequest),[ListAppConnectorsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-beyondcorp-appconnectors/latest/com.google.cloud.beyondcorp.appconnectors.v1.ListAppConnectorsResponse)>` |   
  
### listAppConnectorsPagedCallable()
    
    
    public UnaryCallable<ListAppConnectorsRequest,AppConnectorsServiceClient.ListAppConnectorsPagedResponse> listAppConnectorsPagedCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListAppConnectorsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-beyondcorp-appconnectors/latest/com.google.cloud.beyondcorp.appconnectors.v1.ListAppConnectorsRequest),[ListAppConnectorsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-beyondcorp-appconnectors/latest/com.google.cloud.beyondcorp.appconnectors.v1.AppConnectorsServiceClient.ListAppConnectorsPagedResponse)>` |   
  
### listLocationsCallable()
    
    
    public UnaryCallable<ListLocationsRequest,ListLocationsResponse> listLocationsCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.ListLocationsRequest,com.google.cloud.location.ListLocationsResponse>` |   
  
### listLocationsPagedCallable()
    
    
    public UnaryCallable<ListLocationsRequest,AppConnectorsServiceClient.ListLocationsPagedResponse> listLocationsPagedCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.ListLocationsRequest,[ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-beyondcorp-appconnectors/latest/com.google.cloud.beyondcorp.appconnectors.v1.AppConnectorsServiceClient.ListLocationsPagedResponse)>` |   
  
### reportStatusCallable()
    
    
    public UnaryCallable<ReportStatusRequest,Operation> reportStatusCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ReportStatusRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-beyondcorp-appconnectors/latest/com.google.cloud.beyondcorp.appconnectors.v1.ReportStatusRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### reportStatusOperationCallable()
    
    
    public OperationCallable<ReportStatusRequest,AppConnector,AppConnectorOperationMetadata> reportStatusOperationCallable()

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[ReportStatusRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-beyondcorp-appconnectors/latest/com.google.cloud.beyondcorp.appconnectors.v1.ReportStatusRequest),[AppConnector](https://docs.cloud.google.com/java/docs/reference/google-cloud-beyondcorp-appconnectors/latest/com.google.cloud.beyondcorp.appconnectors.v1.AppConnector),[AppConnectorOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-beyondcorp-appconnectors/latest/com.google.cloud.beyondcorp.appconnectors.v1.AppConnectorOperationMetadata)>` |   
  
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
  
### updateAppConnectorCallable()
    
    
    public UnaryCallable<UpdateAppConnectorRequest,Operation> updateAppConnectorCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateAppConnectorRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-beyondcorp-appconnectors/latest/com.google.cloud.beyondcorp.appconnectors.v1.UpdateAppConnectorRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateAppConnectorOperationCallable()
    
    
    public OperationCallable<UpdateAppConnectorRequest,AppConnector,AppConnectorOperationMetadata> updateAppConnectorOperationCallable()

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdateAppConnectorRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-beyondcorp-appconnectors/latest/com.google.cloud.beyondcorp.appconnectors.v1.UpdateAppConnectorRequest),[AppConnector](https://docs.cloud.google.com/java/docs/reference/google-cloud-beyondcorp-appconnectors/latest/com.google.cloud.beyondcorp.appconnectors.v1.AppConnector),[AppConnectorOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-beyondcorp-appconnectors/latest/com.google.cloud.beyondcorp.appconnectors.v1.AppConnectorOperationMetadata)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
