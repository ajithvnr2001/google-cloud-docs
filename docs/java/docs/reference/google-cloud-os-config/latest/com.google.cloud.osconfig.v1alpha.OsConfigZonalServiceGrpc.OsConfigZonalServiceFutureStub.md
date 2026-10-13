---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1alpha.OsConfigZonalServiceGrpc.OsConfigZonalServiceFutureStub
title: Class OsConfigZonalServiceGrpc.OsConfigZonalServiceFutureStub (2.101.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:43:02.669750+00:00
---

# Class OsConfigZonalServiceGrpc.OsConfigZonalServiceFutureStub (2.101.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1alpha.OsConfigZonalServiceGrpc.OsConfigZonalServiceFutureStub

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class OsConfigZonalServiceGrpc.OsConfigZonalServiceFutureStub (2.101.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.101.0 (latest)  2.97.0  2.96.0  2.95.0  2.93.0  2.90.0  2.89.0  2.87.0  2.85.0  2.84.0  2.82.0  2.80.0  2.78.0  2.77.0  2.76.0  2.75.0  2.74.0  2.72.0  2.70.0  2.69.0  2.66.0  2.65.0  2.64.0  2.62.0  2.61.0  2.60.0  2.59.0  2.58.0  2.57.0  2.56.0  2.55.0  2.54.0  2.53.0  2.51.0  2.50.0  2.49.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.26.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.6  2.4.3  2.3.2 
    
    
    public static final class OsConfigZonalServiceGrpc.OsConfigZonalServiceFutureStub extends AbstractFutureStub<OsConfigZonalServiceGrpc.OsConfigZonalServiceFutureStub>

A stub to allow clients to do ListenableFuture-style rpc calls to service OsConfigZonalService.

Zonal OS Config API The OS Config service is the server-side component that allows users to manage package installations and patch jobs for Compute Engine VM instances.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > io.grpc.stub.AbstractStub > io.grpc.stub.AbstractFutureStub > OsConfigZonalServiceGrpc.OsConfigZonalServiceFutureStub

## Inherited Members

io.grpc.stub.AbstractFutureStub.<T>newStub(io.grpc.stub.AbstractStub.StubFactory<T>,io.grpc.Channel)

io.grpc.stub.AbstractFutureStub.<T>newStub(io.grpc.stub.AbstractStub.StubFactory<T>,io.grpc.Channel,io.grpc.CallOptions)

io.grpc.stub.AbstractStub.<T>withOption(io.grpc.CallOptions.Key<T>,T)

io.grpc.stub.AbstractStub.build(io.grpc.Channel,io.grpc.CallOptions)

io.grpc.stub.AbstractStub.getCallOptions()

io.grpc.stub.AbstractStub.getChannel()

io.grpc.stub.AbstractStub.withCallCredentials(io.grpc.CallCredentials)

io.grpc.stub.AbstractStub.withChannel(io.grpc.Channel)

io.grpc.stub.AbstractStub.withCompression(java.lang.String)

io.grpc.stub.AbstractStub.withDeadline(io.grpc.Deadline)

io.grpc.stub.AbstractStub.withDeadlineAfter(java.time.Duration)

io.grpc.stub.AbstractStub.withDeadlineAfter(long,java.util.concurrent.TimeUnit)

io.grpc.stub.AbstractStub.withExecutor(java.util.concurrent.Executor)

io.grpc.stub.AbstractStub.withInterceptors(io.grpc.ClientInterceptor...)

io.grpc.stub.AbstractStub.withMaxInboundMessageSize(int)

io.grpc.stub.AbstractStub.withMaxOutboundMessageSize(int)

io.grpc.stub.AbstractStub.withOnReadyThreshold(int)

io.grpc.stub.AbstractStub.withWaitForReady()

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

## Methods 

### build(Channel channel, CallOptions callOptions)
    
    
    protected OsConfigZonalServiceGrpc.OsConfigZonalServiceFutureStub build(Channel channel, CallOptions callOptions)

**Parameters**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
`callOptions` | `io.grpc.CallOptions`  
  
**Returns**  
---  
**Type** | **Description**  
`[OsConfigZonalServiceGrpc.OsConfigZonalServiceFutureStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1alpha.OsConfigZonalServiceGrpc.OsConfigZonalServiceFutureStub)` |   
**Overrides**

io.grpc.stub.AbstractStub.build(io.grpc.Channel,io.grpc.CallOptions)

### createOSPolicyAssignment(CreateOSPolicyAssignmentRequest request)
    
    
    public ListenableFuture<Operation> createOSPolicyAssignment(CreateOSPolicyAssignmentRequest request)

Create an OS policy assignment. This method also creates the first revision of the OS policy assignment. This method returns a long running operation (LRO) that contains the rollout details. The rollout can be cancelled by cancelling the LRO. For more information, see [Method: projects.locations.osPolicyAssignments.operations.cancel](https://cloud.google.com/compute/docs/osconfig/rest/v1alpha/projects.locations.osPolicyAssignments.operations/cancel).

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateOSPolicyAssignmentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1alpha.CreateOSPolicyAssignmentRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteOSPolicyAssignment(DeleteOSPolicyAssignmentRequest request)
    
    
    public ListenableFuture<Operation> deleteOSPolicyAssignment(DeleteOSPolicyAssignmentRequest request)

Delete the OS policy assignment. This method creates a new revision of the OS policy assignment. This method returns a long running operation (LRO) that contains the rollout details. The rollout can be cancelled by cancelling the LRO. If the LRO completes and is not cancelled, all revisions associated with the OS policy assignment are deleted. For more information, see [Method: projects.locations.osPolicyAssignments.operations.cancel](https://cloud.google.com/compute/docs/osconfig/rest/v1alpha/projects.locations.osPolicyAssignments.operations/cancel).

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteOSPolicyAssignmentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1alpha.DeleteOSPolicyAssignmentRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### getInstanceOSPoliciesCompliance(GetInstanceOSPoliciesComplianceRequest request) (deprecated)
    
    
    public ListenableFuture<InstanceOSPoliciesCompliance> getInstanceOSPoliciesCompliance(GetInstanceOSPoliciesComplianceRequest request)

Get OS policies compliance data for the specified Compute Engine VM instance.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetInstanceOSPoliciesComplianceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1alpha.GetInstanceOSPoliciesComplianceRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[InstanceOSPoliciesCompliance](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1alpha.InstanceOSPoliciesCompliance)>` |   
  
### getInventory(GetInventoryRequest request)
    
    
    public ListenableFuture<Inventory> getInventory(GetInventoryRequest request)

Get inventory data for the specified VM instance. If the VM has no associated inventory, the message `NOT_FOUND` is returned.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetInventoryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1alpha.GetInventoryRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Inventory](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1alpha.Inventory)>` |   
  
### getOSPolicyAssignment(GetOSPolicyAssignmentRequest request)
    
    
    public ListenableFuture<OSPolicyAssignment> getOSPolicyAssignment(GetOSPolicyAssignmentRequest request)

Retrieve an existing OS policy assignment. This method always returns the latest revision. In order to retrieve a previous revision of the assignment, also provide the revision ID in the `name` parameter.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetOSPolicyAssignmentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1alpha.GetOSPolicyAssignmentRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[OSPolicyAssignment](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1alpha.OSPolicyAssignment)>` |   
  
### getOSPolicyAssignmentReport(GetOSPolicyAssignmentReportRequest request)
    
    
    public ListenableFuture<OSPolicyAssignmentReport> getOSPolicyAssignmentReport(GetOSPolicyAssignmentReportRequest request)

Get the OS policy asssignment report for the specified Compute Engine VM instance.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetOSPolicyAssignmentReportRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1alpha.GetOSPolicyAssignmentReportRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[OSPolicyAssignmentReport](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1alpha.OSPolicyAssignmentReport)>` |   
  
### getVulnerabilityReport(GetVulnerabilityReportRequest request)
    
    
    public ListenableFuture<VulnerabilityReport> getVulnerabilityReport(GetVulnerabilityReportRequest request)

Gets the vulnerability report for the specified VM instance. Only VMs with inventory data have vulnerability reports associated with them.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetVulnerabilityReportRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1alpha.GetVulnerabilityReportRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[VulnerabilityReport](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1alpha.VulnerabilityReport)>` |   
  
### listInstanceOSPoliciesCompliances(ListInstanceOSPoliciesCompliancesRequest request) (deprecated)
    
    
    public ListenableFuture<ListInstanceOSPoliciesCompliancesResponse> listInstanceOSPoliciesCompliances(ListInstanceOSPoliciesCompliancesRequest request)

List OS policies compliance data for all Compute Engine VM instances in the specified zone.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListInstanceOSPoliciesCompliancesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1alpha.ListInstanceOSPoliciesCompliancesRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[ListInstanceOSPoliciesCompliancesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1alpha.ListInstanceOSPoliciesCompliancesResponse)>` |   
  
### listInventories(ListInventoriesRequest request)
    
    
    public ListenableFuture<ListInventoriesResponse> listInventories(ListInventoriesRequest request)

List inventory data for all VM instances in the specified zone.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListInventoriesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1alpha.ListInventoriesRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[ListInventoriesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1alpha.ListInventoriesResponse)>` |   
  
### listOSPolicyAssignmentReports(ListOSPolicyAssignmentReportsRequest request)
    
    
    public ListenableFuture<ListOSPolicyAssignmentReportsResponse> listOSPolicyAssignmentReports(ListOSPolicyAssignmentReportsRequest request)

List OS policy asssignment reports for all Compute Engine VM instances in the specified zone.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListOSPolicyAssignmentReportsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1alpha.ListOSPolicyAssignmentReportsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[ListOSPolicyAssignmentReportsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1alpha.ListOSPolicyAssignmentReportsResponse)>` |   
  
### listOSPolicyAssignmentRevisions(ListOSPolicyAssignmentRevisionsRequest request)
    
    
    public ListenableFuture<ListOSPolicyAssignmentRevisionsResponse> listOSPolicyAssignmentRevisions(ListOSPolicyAssignmentRevisionsRequest request)

List the OS policy assignment revisions for a given OS policy assignment.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListOSPolicyAssignmentRevisionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1alpha.ListOSPolicyAssignmentRevisionsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[ListOSPolicyAssignmentRevisionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1alpha.ListOSPolicyAssignmentRevisionsResponse)>` |   
  
### listOSPolicyAssignments(ListOSPolicyAssignmentsRequest request)
    
    
    public ListenableFuture<ListOSPolicyAssignmentsResponse> listOSPolicyAssignments(ListOSPolicyAssignmentsRequest request)

List the OS policy assignments under the parent resource. For each OS policy assignment, the latest revision is returned.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListOSPolicyAssignmentsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1alpha.ListOSPolicyAssignmentsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[ListOSPolicyAssignmentsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1alpha.ListOSPolicyAssignmentsResponse)>` |   
  
### listVulnerabilityReports(ListVulnerabilityReportsRequest request)
    
    
    public ListenableFuture<ListVulnerabilityReportsResponse> listVulnerabilityReports(ListVulnerabilityReportsRequest request)

List vulnerability reports for all VM instances in the specified zone.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListVulnerabilityReportsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1alpha.ListVulnerabilityReportsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[ListVulnerabilityReportsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1alpha.ListVulnerabilityReportsResponse)>` |   
  
### updateOSPolicyAssignment(UpdateOSPolicyAssignmentRequest request)
    
    
    public ListenableFuture<Operation> updateOSPolicyAssignment(UpdateOSPolicyAssignmentRequest request)

Update an existing OS policy assignment. This method creates a new revision of the OS policy assignment. This method returns a long running operation (LRO) that contains the rollout details. The rollout can be cancelled by cancelling the LRO. For more information, see [Method: projects.locations.osPolicyAssignments.operations.cancel](https://cloud.google.com/compute/docs/osconfig/rest/v1alpha/projects.locations.osPolicyAssignments.operations/cancel).

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateOSPolicyAssignmentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1alpha.UpdateOSPolicyAssignmentRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
