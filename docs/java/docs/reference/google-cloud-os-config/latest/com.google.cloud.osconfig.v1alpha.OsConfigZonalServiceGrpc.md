---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1alpha.OsConfigZonalServiceGrpc
title: Class OsConfigZonalServiceGrpc (2.101.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:08:12.350057+00:00
---

# Class OsConfigZonalServiceGrpc (2.101.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1alpha.OsConfigZonalServiceGrpc

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class OsConfigZonalServiceGrpc (2.101.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.101.0 (latest)  2.97.0  2.96.0  2.95.0  2.93.0  2.90.0  2.89.0  2.87.0  2.85.0  2.84.0  2.82.0  2.80.0  2.78.0  2.77.0  2.76.0  2.75.0  2.74.0  2.72.0  2.70.0  2.69.0  2.66.0  2.65.0  2.64.0  2.62.0  2.61.0  2.60.0  2.59.0  2.58.0  2.57.0  2.56.0  2.55.0  2.54.0  2.53.0  2.51.0  2.50.0  2.49.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.26.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.6  2.4.3  2.3.2 
    
    
    public final class OsConfigZonalServiceGrpc

Zonal OS Config API The OS Config service is the server-side component that allows users to manage package installations and patch jobs for Compute Engine VM instances.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > OsConfigZonalServiceGrpc

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

## Static Fields 

### SERVICE_NAME
    
    
    public static final String SERVICE_NAME

**Field Value**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
## Static Methods 

### bindService(OsConfigZonalServiceGrpc.AsyncService service)
    
    
    public static final ServerServiceDefinition bindService(OsConfigZonalServiceGrpc.AsyncService service)

**Parameter**  
---  
**Name** | **Description**  
`service` | `[OsConfigZonalServiceGrpc.AsyncService](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1alpha.OsConfigZonalServiceGrpc.AsyncService)`  
  
**Returns**  
---  
**Type** | **Description**  
`io.grpc.ServerServiceDefinition` |   
  
### getCreateOSPolicyAssignmentMethod()
    
    
    public static MethodDescriptor<CreateOSPolicyAssignmentRequest,Operation> getCreateOSPolicyAssignmentMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[CreateOSPolicyAssignmentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1alpha.CreateOSPolicyAssignmentRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### getDeleteOSPolicyAssignmentMethod()
    
    
    public static MethodDescriptor<DeleteOSPolicyAssignmentRequest,Operation> getDeleteOSPolicyAssignmentMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[DeleteOSPolicyAssignmentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1alpha.DeleteOSPolicyAssignmentRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### getGetInstanceOSPoliciesComplianceMethod()
    
    
    public static MethodDescriptor<GetInstanceOSPoliciesComplianceRequest,InstanceOSPoliciesCompliance> getGetInstanceOSPoliciesComplianceMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[GetInstanceOSPoliciesComplianceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1alpha.GetInstanceOSPoliciesComplianceRequest),[InstanceOSPoliciesCompliance](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1alpha.InstanceOSPoliciesCompliance)>` |   
  
### getGetInventoryMethod()
    
    
    public static MethodDescriptor<GetInventoryRequest,Inventory> getGetInventoryMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[GetInventoryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1alpha.GetInventoryRequest),[Inventory](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1alpha.Inventory)>` |   
  
### getGetOSPolicyAssignmentMethod()
    
    
    public static MethodDescriptor<GetOSPolicyAssignmentRequest,OSPolicyAssignment> getGetOSPolicyAssignmentMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[GetOSPolicyAssignmentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1alpha.GetOSPolicyAssignmentRequest),[OSPolicyAssignment](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1alpha.OSPolicyAssignment)>` |   
  
### getGetOSPolicyAssignmentReportMethod()
    
    
    public static MethodDescriptor<GetOSPolicyAssignmentReportRequest,OSPolicyAssignmentReport> getGetOSPolicyAssignmentReportMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[GetOSPolicyAssignmentReportRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1alpha.GetOSPolicyAssignmentReportRequest),[OSPolicyAssignmentReport](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1alpha.OSPolicyAssignmentReport)>` |   
  
### getGetVulnerabilityReportMethod()
    
    
    public static MethodDescriptor<GetVulnerabilityReportRequest,VulnerabilityReport> getGetVulnerabilityReportMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[GetVulnerabilityReportRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1alpha.GetVulnerabilityReportRequest),[VulnerabilityReport](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1alpha.VulnerabilityReport)>` |   
  
### getListInstanceOSPoliciesCompliancesMethod()
    
    
    public static MethodDescriptor<ListInstanceOSPoliciesCompliancesRequest,ListInstanceOSPoliciesCompliancesResponse> getListInstanceOSPoliciesCompliancesMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[ListInstanceOSPoliciesCompliancesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1alpha.ListInstanceOSPoliciesCompliancesRequest),[ListInstanceOSPoliciesCompliancesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1alpha.ListInstanceOSPoliciesCompliancesResponse)>` |   
  
### getListInventoriesMethod()
    
    
    public static MethodDescriptor<ListInventoriesRequest,ListInventoriesResponse> getListInventoriesMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[ListInventoriesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1alpha.ListInventoriesRequest),[ListInventoriesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1alpha.ListInventoriesResponse)>` |   
  
### getListOSPolicyAssignmentReportsMethod()
    
    
    public static MethodDescriptor<ListOSPolicyAssignmentReportsRequest,ListOSPolicyAssignmentReportsResponse> getListOSPolicyAssignmentReportsMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[ListOSPolicyAssignmentReportsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1alpha.ListOSPolicyAssignmentReportsRequest),[ListOSPolicyAssignmentReportsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1alpha.ListOSPolicyAssignmentReportsResponse)>` |   
  
### getListOSPolicyAssignmentRevisionsMethod()
    
    
    public static MethodDescriptor<ListOSPolicyAssignmentRevisionsRequest,ListOSPolicyAssignmentRevisionsResponse> getListOSPolicyAssignmentRevisionsMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[ListOSPolicyAssignmentRevisionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1alpha.ListOSPolicyAssignmentRevisionsRequest),[ListOSPolicyAssignmentRevisionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1alpha.ListOSPolicyAssignmentRevisionsResponse)>` |   
  
### getListOSPolicyAssignmentsMethod()
    
    
    public static MethodDescriptor<ListOSPolicyAssignmentsRequest,ListOSPolicyAssignmentsResponse> getListOSPolicyAssignmentsMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[ListOSPolicyAssignmentsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1alpha.ListOSPolicyAssignmentsRequest),[ListOSPolicyAssignmentsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1alpha.ListOSPolicyAssignmentsResponse)>` |   
  
### getListVulnerabilityReportsMethod()
    
    
    public static MethodDescriptor<ListVulnerabilityReportsRequest,ListVulnerabilityReportsResponse> getListVulnerabilityReportsMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[ListVulnerabilityReportsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1alpha.ListVulnerabilityReportsRequest),[ListVulnerabilityReportsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1alpha.ListVulnerabilityReportsResponse)>` |   
  
### getServiceDescriptor()
    
    
    public static ServiceDescriptor getServiceDescriptor()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.ServiceDescriptor` |   
  
### getUpdateOSPolicyAssignmentMethod()
    
    
    public static MethodDescriptor<UpdateOSPolicyAssignmentRequest,Operation> getUpdateOSPolicyAssignmentMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[UpdateOSPolicyAssignmentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1alpha.UpdateOSPolicyAssignmentRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### newBlockingStub(Channel channel)
    
    
    public static OsConfigZonalServiceGrpc.OsConfigZonalServiceBlockingStub newBlockingStub(Channel channel)

Creates a new blocking-style stub that supports unary and streaming output calls on the service

**Parameter**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
**Returns**  
---  
**Type** | **Description**  
`[OsConfigZonalServiceGrpc.OsConfigZonalServiceBlockingStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1alpha.OsConfigZonalServiceGrpc.OsConfigZonalServiceBlockingStub)` |   
  
### newBlockingV2Stub(Channel channel)
    
    
    public static OsConfigZonalServiceGrpc.OsConfigZonalServiceBlockingV2Stub newBlockingV2Stub(Channel channel)

Creates a new blocking-style stub that supports all types of calls on the service

**Parameter**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
**Returns**  
---  
**Type** | **Description**  
`[OsConfigZonalServiceGrpc.OsConfigZonalServiceBlockingV2Stub](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1alpha.OsConfigZonalServiceGrpc.OsConfigZonalServiceBlockingV2Stub)` |   
  
### newFutureStub(Channel channel)
    
    
    public static OsConfigZonalServiceGrpc.OsConfigZonalServiceFutureStub newFutureStub(Channel channel)

Creates a new ListenableFuture-style stub that supports unary calls on the service

**Parameter**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
**Returns**  
---  
**Type** | **Description**  
`[OsConfigZonalServiceGrpc.OsConfigZonalServiceFutureStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1alpha.OsConfigZonalServiceGrpc.OsConfigZonalServiceFutureStub)` |   
  
### newStub(Channel channel)
    
    
    public static OsConfigZonalServiceGrpc.OsConfigZonalServiceStub newStub(Channel channel)

Creates a new async stub that supports all call types for the service

**Parameter**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
**Returns**  
---  
**Type** | **Description**  
`[OsConfigZonalServiceGrpc.OsConfigZonalServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1alpha.OsConfigZonalServiceGrpc.OsConfigZonalServiceStub)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
