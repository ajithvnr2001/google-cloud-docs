---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-gke-multi-cloud/latest/com.google.cloud.gkemulticloud.v1.AttachedClustersGrpc.AttachedClustersBlockingV2Stub
title: Class AttachedClustersGrpc.AttachedClustersBlockingV2Stub (0.98.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:47:30.938070+00:00
---

# Class AttachedClustersGrpc.AttachedClustersBlockingV2Stub (0.98.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-gke-multi-cloud/latest/com.google.cloud.gkemulticloud.v1.AttachedClustersGrpc.AttachedClustersBlockingV2Stub

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class AttachedClustersGrpc.AttachedClustersBlockingV2Stub (0.98.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.98.0 (latest)  0.94.0  0.93.0  0.92.0  0.90.0  0.87.0  0.86.0  0.84.0  0.82.0  0.81.0  0.80.0  0.79.0  0.77.0  0.75.0  0.74.0  0.73.0  0.72.0  0.71.0  0.69.0  0.67.0  0.66.0  0.63.0  0.62.0  0.61.0  0.59.0  0.58.0  0.57.0  0.56.0  0.55.0  0.54.0  0.53.0  0.52.0  0.51.0  0.50.0  0.48.0  0.47.0  0.46.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.38.0  0.36.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.6  0.1.0 
    
    
    public static final class AttachedClustersGrpc.AttachedClustersBlockingV2Stub extends AbstractBlockingStub<AttachedClustersGrpc.AttachedClustersBlockingV2Stub>

A stub to allow clients to do synchronous rpc calls to service AttachedClusters.

The AttachedClusters API provides a single centrally managed service to register and manage Anthos attached clusters that run on customer's owned infrastructure.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > io.grpc.stub.AbstractStub > io.grpc.stub.AbstractBlockingStub > AttachedClustersGrpc.AttachedClustersBlockingV2Stub

## Inherited Members

io.grpc.stub.AbstractBlockingStub.<T>newStub(io.grpc.stub.AbstractStub.StubFactory<T>,io.grpc.Channel)

io.grpc.stub.AbstractBlockingStub.<T>newStub(io.grpc.stub.AbstractStub.StubFactory<T>,io.grpc.Channel,io.grpc.CallOptions)

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
    
    
    protected AttachedClustersGrpc.AttachedClustersBlockingV2Stub build(Channel channel, CallOptions callOptions)

**Parameters**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
`callOptions` | `io.grpc.CallOptions`  
  
**Returns**  
---  
**Type** | **Description**  
`[AttachedClustersGrpc.AttachedClustersBlockingV2Stub](https://docs.cloud.google.com/java/docs/reference/google-cloud-gke-multi-cloud/latest/com.google.cloud.gkemulticloud.v1.AttachedClustersGrpc.AttachedClustersBlockingV2Stub)` |   
**Overrides**

io.grpc.stub.AbstractStub.build(io.grpc.Channel,io.grpc.CallOptions)

### createAttachedCluster(CreateAttachedClusterRequest request)
    
    
    public Operation createAttachedCluster(CreateAttachedClusterRequest request)

Creates a new AttachedCluster resource on a given Google Cloud Platform project and region. If successful, the response contains a newly created Operation resource that can be described to track the status of the operation.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateAttachedClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gke-multi-cloud/latest/com.google.cloud.gkemulticloud.v1.CreateAttachedClusterRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### deleteAttachedCluster(DeleteAttachedClusterRequest request)
    
    
    public Operation deleteAttachedCluster(DeleteAttachedClusterRequest request)

Deletes a specific AttachedCluster resource. If successful, the response contains a newly created Operation resource that can be described to track the status of the operation.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteAttachedClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gke-multi-cloud/latest/com.google.cloud.gkemulticloud.v1.DeleteAttachedClusterRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### generateAttachedClusterAgentToken(GenerateAttachedClusterAgentTokenRequest request)
    
    
    public GenerateAttachedClusterAgentTokenResponse generateAttachedClusterAgentToken(GenerateAttachedClusterAgentTokenRequest request)

Generates an access token for a cluster agent.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GenerateAttachedClusterAgentTokenRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gke-multi-cloud/latest/com.google.cloud.gkemulticloud.v1.GenerateAttachedClusterAgentTokenRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[GenerateAttachedClusterAgentTokenResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-gke-multi-cloud/latest/com.google.cloud.gkemulticloud.v1.GenerateAttachedClusterAgentTokenResponse)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### generateAttachedClusterInstallManifest(GenerateAttachedClusterInstallManifestRequest request)
    
    
    public GenerateAttachedClusterInstallManifestResponse generateAttachedClusterInstallManifest(GenerateAttachedClusterInstallManifestRequest request)

Generates the install manifest to be installed on the target cluster.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GenerateAttachedClusterInstallManifestRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gke-multi-cloud/latest/com.google.cloud.gkemulticloud.v1.GenerateAttachedClusterInstallManifestRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[GenerateAttachedClusterInstallManifestResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-gke-multi-cloud/latest/com.google.cloud.gkemulticloud.v1.GenerateAttachedClusterInstallManifestResponse)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### getAttachedCluster(GetAttachedClusterRequest request)
    
    
    public AttachedCluster getAttachedCluster(GetAttachedClusterRequest request)

Describes a specific AttachedCluster resource.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetAttachedClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gke-multi-cloud/latest/com.google.cloud.gkemulticloud.v1.GetAttachedClusterRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[AttachedCluster](https://docs.cloud.google.com/java/docs/reference/google-cloud-gke-multi-cloud/latest/com.google.cloud.gkemulticloud.v1.AttachedCluster)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### getAttachedServerConfig(GetAttachedServerConfigRequest request)
    
    
    public AttachedServerConfig getAttachedServerConfig(GetAttachedServerConfigRequest request)

Returns information, such as supported Kubernetes versions, on a given Google Cloud location.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetAttachedServerConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gke-multi-cloud/latest/com.google.cloud.gkemulticloud.v1.GetAttachedServerConfigRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[AttachedServerConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-gke-multi-cloud/latest/com.google.cloud.gkemulticloud.v1.AttachedServerConfig)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### importAttachedCluster(ImportAttachedClusterRequest request)
    
    
    public Operation importAttachedCluster(ImportAttachedClusterRequest request)

Imports creates a new AttachedCluster resource by importing an existing Fleet Membership resource. Attached Clusters created before the introduction of the Anthos Multi-Cloud API can be imported through this method. If successful, the response contains a newly created Operation resource that can be described to track the status of the operation.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ImportAttachedClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gke-multi-cloud/latest/com.google.cloud.gkemulticloud.v1.ImportAttachedClusterRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### listAttachedClusters(ListAttachedClustersRequest request)
    
    
    public ListAttachedClustersResponse listAttachedClusters(ListAttachedClustersRequest request)

Lists all AttachedCluster resources on a given Google Cloud project and region.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListAttachedClustersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gke-multi-cloud/latest/com.google.cloud.gkemulticloud.v1.ListAttachedClustersRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ListAttachedClustersResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-gke-multi-cloud/latest/com.google.cloud.gkemulticloud.v1.ListAttachedClustersResponse)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### updateAttachedCluster(UpdateAttachedClusterRequest request)
    
    
    public Operation updateAttachedCluster(UpdateAttachedClusterRequest request)

Updates an AttachedCluster.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateAttachedClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gke-multi-cloud/latest/com.google.cloud.gkemulticloud.v1.UpdateAttachedClusterRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
