---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-notebooks/latest/com.google.cloud.notebooks.v1beta1.NotebookServiceGrpc.AsyncService
title: Interface NotebookServiceGrpc.AsyncService (1.97.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:09:51.468341+00:00
---

# Interface NotebookServiceGrpc.AsyncService (1.97.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-notebooks/latest/com.google.cloud.notebooks.v1beta1.NotebookServiceGrpc.AsyncService

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface NotebookServiceGrpc.AsyncService (1.97.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.97.0 (latest)  1.93.0  1.92.0  1.91.0  1.89.0  1.86.0  1.85.0  1.83.0  1.81.0  1.80.0  1.78.0  1.76.0  1.74.0  1.73.0  1.72.0  1.71.0  1.70.0  1.68.0  1.66.0  1.65.0  1.62.0  1.61.0  1.60.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.50.0  1.49.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.37.0  1.35.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.26.0  1.25.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.0  1.11.0  1.10.0  1.9.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.3  1.0.6  0.6.2 
    
    
    public static interface NotebookServiceGrpc.AsyncService

API v1beta1 service for Cloud AI Platform Notebooks.

## Methods 

### createEnvironment(CreateEnvironmentRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void createEnvironment(CreateEnvironmentRequest request, StreamObserver<Operation> responseObserver)

Creates a new Environment.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateEnvironmentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-notebooks/latest/com.google.cloud.notebooks.v1beta1.CreateEnvironmentRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### createInstance(CreateInstanceRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void createInstance(CreateInstanceRequest request, StreamObserver<Operation> responseObserver)

Creates a new Instance in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-notebooks/latest/com.google.cloud.notebooks.v1beta1.CreateInstanceRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### deleteEnvironment(DeleteEnvironmentRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void deleteEnvironment(DeleteEnvironmentRequest request, StreamObserver<Operation> responseObserver)

Deletes a single Environment.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteEnvironmentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-notebooks/latest/com.google.cloud.notebooks.v1beta1.DeleteEnvironmentRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### deleteInstance(DeleteInstanceRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void deleteInstance(DeleteInstanceRequest request, StreamObserver<Operation> responseObserver)

Deletes a single Instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-notebooks/latest/com.google.cloud.notebooks.v1beta1.DeleteInstanceRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### getEnvironment(GetEnvironmentRequest request, StreamObserver<Environment> responseObserver)
    
    
    public default void getEnvironment(GetEnvironmentRequest request, StreamObserver<Environment> responseObserver)

Gets details of a single Environment.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetEnvironmentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-notebooks/latest/com.google.cloud.notebooks.v1beta1.GetEnvironmentRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Environment](https://docs.cloud.google.com/java/docs/reference/google-cloud-notebooks/latest/com.google.cloud.notebooks.v1beta1.Environment)>`  
  
  
### getInstance(GetInstanceRequest request, StreamObserver<Instance> responseObserver)
    
    
    public default void getInstance(GetInstanceRequest request, StreamObserver<Instance> responseObserver)

Gets details of a single Instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-notebooks/latest/com.google.cloud.notebooks.v1beta1.GetInstanceRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-notebooks/latest/com.google.cloud.notebooks.v1beta1.Instance)>`  
  
  
### isInstanceUpgradeable(IsInstanceUpgradeableRequest request, StreamObserver<IsInstanceUpgradeableResponse> responseObserver) (deprecated)
    
    
    public default void isInstanceUpgradeable(IsInstanceUpgradeableRequest request, StreamObserver<IsInstanceUpgradeableResponse> responseObserver)

Check if a notebook instance is upgradable. Deprecated. Please consider using v1.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[IsInstanceUpgradeableRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-notebooks/latest/com.google.cloud.notebooks.v1beta1.IsInstanceUpgradeableRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[IsInstanceUpgradeableResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-notebooks/latest/com.google.cloud.notebooks.v1beta1.IsInstanceUpgradeableResponse)>`  
  
  
### listEnvironments(ListEnvironmentsRequest request, StreamObserver<ListEnvironmentsResponse> responseObserver)
    
    
    public default void listEnvironments(ListEnvironmentsRequest request, StreamObserver<ListEnvironmentsResponse> responseObserver)

Lists environments in a project.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListEnvironmentsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-notebooks/latest/com.google.cloud.notebooks.v1beta1.ListEnvironmentsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListEnvironmentsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-notebooks/latest/com.google.cloud.notebooks.v1beta1.ListEnvironmentsResponse)>`  
  
  
### listInstances(ListInstancesRequest request, StreamObserver<ListInstancesResponse> responseObserver)
    
    
    public default void listInstances(ListInstancesRequest request, StreamObserver<ListInstancesResponse> responseObserver)

Lists instances in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListInstancesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-notebooks/latest/com.google.cloud.notebooks.v1beta1.ListInstancesRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListInstancesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-notebooks/latest/com.google.cloud.notebooks.v1beta1.ListInstancesResponse)>`  
  
  
### registerInstance(RegisterInstanceRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void registerInstance(RegisterInstanceRequest request, StreamObserver<Operation> responseObserver)

Registers an existing legacy notebook instance to the Notebooks API server. Legacy instances are instances created with the legacy Compute Engine calls. They are not manageable by the Notebooks API out of the box. This call makes these instances manageable by the Notebooks API.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[RegisterInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-notebooks/latest/com.google.cloud.notebooks.v1beta1.RegisterInstanceRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### reportInstanceInfo(ReportInstanceInfoRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void reportInstanceInfo(ReportInstanceInfoRequest request, StreamObserver<Operation> responseObserver)

Allows notebook instances to report their latest instance information to the Notebooks API server. The server will merge the reported information to the instance metadata store. Do not use this method directly.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ReportInstanceInfoRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-notebooks/latest/com.google.cloud.notebooks.v1beta1.ReportInstanceInfoRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### resetInstance(ResetInstanceRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void resetInstance(ResetInstanceRequest request, StreamObserver<Operation> responseObserver)

Resets a notebook instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ResetInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-notebooks/latest/com.google.cloud.notebooks.v1beta1.ResetInstanceRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### setInstanceAccelerator(SetInstanceAcceleratorRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void setInstanceAccelerator(SetInstanceAcceleratorRequest request, StreamObserver<Operation> responseObserver)

Updates the guest accelerators of a single Instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SetInstanceAcceleratorRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-notebooks/latest/com.google.cloud.notebooks.v1beta1.SetInstanceAcceleratorRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### setInstanceLabels(SetInstanceLabelsRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void setInstanceLabels(SetInstanceLabelsRequest request, StreamObserver<Operation> responseObserver)

Updates the labels of an Instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SetInstanceLabelsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-notebooks/latest/com.google.cloud.notebooks.v1beta1.SetInstanceLabelsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### setInstanceMachineType(SetInstanceMachineTypeRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void setInstanceMachineType(SetInstanceMachineTypeRequest request, StreamObserver<Operation> responseObserver)

Updates the machine type of a single Instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SetInstanceMachineTypeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-notebooks/latest/com.google.cloud.notebooks.v1beta1.SetInstanceMachineTypeRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### startInstance(StartInstanceRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void startInstance(StartInstanceRequest request, StreamObserver<Operation> responseObserver)

Starts a notebook instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[StartInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-notebooks/latest/com.google.cloud.notebooks.v1beta1.StartInstanceRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### stopInstance(StopInstanceRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void stopInstance(StopInstanceRequest request, StreamObserver<Operation> responseObserver)

Stops a notebook instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[StopInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-notebooks/latest/com.google.cloud.notebooks.v1beta1.StopInstanceRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### upgradeInstance(UpgradeInstanceRequest request, StreamObserver<Operation> responseObserver) (deprecated)
    
    
    public default void upgradeInstance(UpgradeInstanceRequest request, StreamObserver<Operation> responseObserver)

Upgrades a notebook instance to the latest version. Deprecated. Please consider using v1.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpgradeInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-notebooks/latest/com.google.cloud.notebooks.v1beta1.UpgradeInstanceRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### upgradeInstanceInternal(UpgradeInstanceInternalRequest request, StreamObserver<Operation> responseObserver) (deprecated)
    
    
    public default void upgradeInstanceInternal(UpgradeInstanceInternalRequest request, StreamObserver<Operation> responseObserver)

Allows notebook instances to call this endpoint to upgrade themselves. Do not use this method directly. Deprecated. Please consider using v1.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpgradeInstanceInternalRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-notebooks/latest/com.google.cloud.notebooks.v1beta1.UpgradeInstanceInternalRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
