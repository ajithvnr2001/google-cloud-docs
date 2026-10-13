---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-gkehub/latest/com.google.cloud.gkehub.v1.GkeHubGrpc.GkeHubBlockingV2Stub
title: Class GkeHubGrpc.GkeHubBlockingV2Stub (1.99.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:40:18.779325+00:00
---

# Class GkeHubGrpc.GkeHubBlockingV2Stub (1.99.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-gkehub/latest/com.google.cloud.gkehub.v1.GkeHubGrpc.GkeHubBlockingV2Stub

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class GkeHubGrpc.GkeHubBlockingV2Stub (1.99.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.99.0 (latest)  1.95.0  1.94.0  1.93.0  1.91.0  1.88.0  1.87.0  1.85.0  1.83.0  1.82.0  1.81.0  1.80.0  1.78.0  1.76.0  1.75.0  1.74.0  1.73.0  1.72.0  1.70.0  1.68.0  1.67.0  1.64.0  1.63.0  1.62.0  1.60.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.49.0  1.48.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.37.0  1.36.0  1.35.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.24.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.0  1.11.0  1.9.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.6  1.2.1  1.1.0  1.0.1  0.5.4 
    
    
    public static final class GkeHubGrpc.GkeHubBlockingV2Stub extends AbstractBlockingStub<GkeHubGrpc.GkeHubBlockingV2Stub>

A stub to allow clients to do synchronous rpc calls to service GkeHub.

The GKE Hub service handles the registration of many Kubernetes clusters to Google Cloud, and the management of multi-cluster features over those clusters. The GKE Hub service operates on the following resources:

  * Membership
  * Feature GKE Hub is currently available in the global region and all regions in <https://cloud.google.com/compute/docs/regions-zones>. Feature is only available in global region while membership is global region and all the regions. **Membership management may be non-trivial:** it is recommended to use one of the Google-provided client libraries or tools where possible when working with Membership resources.



## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > io.grpc.stub.AbstractStub > io.grpc.stub.AbstractBlockingStub > GkeHubGrpc.GkeHubBlockingV2Stub

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
    
    
    protected GkeHubGrpc.GkeHubBlockingV2Stub build(Channel channel, CallOptions callOptions)

**Parameters**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
`callOptions` | `io.grpc.CallOptions`  
  
**Returns**  
---  
**Type** | **Description**  
`[GkeHubGrpc.GkeHubBlockingV2Stub](https://docs.cloud.google.com/java/docs/reference/google-cloud-gkehub/latest/com.google.cloud.gkehub.v1.GkeHubGrpc.GkeHubBlockingV2Stub)` |   
**Overrides**

io.grpc.stub.AbstractStub.build(io.grpc.Channel,io.grpc.CallOptions)

### createFeature(CreateFeatureRequest request)
    
    
    public Operation createFeature(CreateFeatureRequest request)

Adds a new Feature.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateFeatureRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gkehub/latest/com.google.cloud.gkehub.v1.CreateFeatureRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### createFleet(CreateFleetRequest request)
    
    
    public Operation createFleet(CreateFleetRequest request)

Creates a fleet.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateFleetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gkehub/latest/com.google.cloud.gkehub.v1.CreateFleetRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### createMembership(CreateMembershipRequest request)
    
    
    public Operation createMembership(CreateMembershipRequest request)

Creates a new Membership. **This is currently only supported for GKE clusters on Google Cloud**. To register other clusters, follow the instructions at <https://cloud.google.com/anthos/multicluster-management/connect/registering-a-cluster>.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateMembershipRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gkehub/latest/com.google.cloud.gkehub.v1.CreateMembershipRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### createMembershipBinding(CreateMembershipBindingRequest request)
    
    
    public Operation createMembershipBinding(CreateMembershipBindingRequest request)

Creates a MembershipBinding.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateMembershipBindingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gkehub/latest/com.google.cloud.gkehub.v1.CreateMembershipBindingRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### createMembershipRBACRoleBinding(CreateMembershipRBACRoleBindingRequest request)
    
    
    public Operation createMembershipRBACRoleBinding(CreateMembershipRBACRoleBindingRequest request)

Creates a Membership RBACRoleBinding.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateMembershipRBACRoleBindingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gkehub/latest/com.google.cloud.gkehub.v1.CreateMembershipRBACRoleBindingRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### createScope(CreateScopeRequest request)
    
    
    public Operation createScope(CreateScopeRequest request)

Creates a Scope.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateScopeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gkehub/latest/com.google.cloud.gkehub.v1.CreateScopeRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### createScopeNamespace(CreateScopeNamespaceRequest request)
    
    
    public Operation createScopeNamespace(CreateScopeNamespaceRequest request)

Creates a fleet namespace.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateScopeNamespaceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gkehub/latest/com.google.cloud.gkehub.v1.CreateScopeNamespaceRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### createScopeRBACRoleBinding(CreateScopeRBACRoleBindingRequest request)
    
    
    public Operation createScopeRBACRoleBinding(CreateScopeRBACRoleBindingRequest request)

Creates a Scope RBACRoleBinding.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateScopeRBACRoleBindingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gkehub/latest/com.google.cloud.gkehub.v1.CreateScopeRBACRoleBindingRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### deleteFeature(DeleteFeatureRequest request)
    
    
    public Operation deleteFeature(DeleteFeatureRequest request)

Removes a Feature.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteFeatureRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gkehub/latest/com.google.cloud.gkehub.v1.DeleteFeatureRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### deleteFleet(DeleteFleetRequest request)
    
    
    public Operation deleteFleet(DeleteFleetRequest request)

Removes a Fleet. There must be no memberships remaining in the Fleet.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteFleetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gkehub/latest/com.google.cloud.gkehub.v1.DeleteFleetRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### deleteMembership(DeleteMembershipRequest request)
    
    
    public Operation deleteMembership(DeleteMembershipRequest request)

Removes a Membership. **This is currently only supported for GKE clusters on Google Cloud**. To unregister other clusters, follow the instructions at <https://cloud.google.com/anthos/multicluster-management/connect/unregistering-a-cluster>.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteMembershipRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gkehub/latest/com.google.cloud.gkehub.v1.DeleteMembershipRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### deleteMembershipBinding(DeleteMembershipBindingRequest request)
    
    
    public Operation deleteMembershipBinding(DeleteMembershipBindingRequest request)

Deletes a MembershipBinding.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteMembershipBindingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gkehub/latest/com.google.cloud.gkehub.v1.DeleteMembershipBindingRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### deleteMembershipRBACRoleBinding(DeleteMembershipRBACRoleBindingRequest request)
    
    
    public Operation deleteMembershipRBACRoleBinding(DeleteMembershipRBACRoleBindingRequest request)

Deletes a Membership RBACRoleBinding.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteMembershipRBACRoleBindingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gkehub/latest/com.google.cloud.gkehub.v1.DeleteMembershipRBACRoleBindingRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### deleteScope(DeleteScopeRequest request)
    
    
    public Operation deleteScope(DeleteScopeRequest request)

Deletes a Scope.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteScopeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gkehub/latest/com.google.cloud.gkehub.v1.DeleteScopeRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### deleteScopeNamespace(DeleteScopeNamespaceRequest request)
    
    
    public Operation deleteScopeNamespace(DeleteScopeNamespaceRequest request)

Deletes a fleet namespace.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteScopeNamespaceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gkehub/latest/com.google.cloud.gkehub.v1.DeleteScopeNamespaceRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### deleteScopeRBACRoleBinding(DeleteScopeRBACRoleBindingRequest request)
    
    
    public Operation deleteScopeRBACRoleBinding(DeleteScopeRBACRoleBindingRequest request)

Deletes a Scope RBACRoleBinding.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteScopeRBACRoleBindingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gkehub/latest/com.google.cloud.gkehub.v1.DeleteScopeRBACRoleBindingRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### generateConnectManifest(GenerateConnectManifestRequest request)
    
    
    public GenerateConnectManifestResponse generateConnectManifest(GenerateConnectManifestRequest request)

Generates the manifest for deployment of the GKE connect agent. **This method is used internally by Google-provided libraries.** Most clients should not need to call this method directly.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GenerateConnectManifestRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gkehub/latest/com.google.cloud.gkehub.v1.GenerateConnectManifestRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[GenerateConnectManifestResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-gkehub/latest/com.google.cloud.gkehub.v1.GenerateConnectManifestResponse)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### generateMembershipRBACRoleBindingYAML(GenerateMembershipRBACRoleBindingYAMLRequest request)
    
    
    public GenerateMembershipRBACRoleBindingYAMLResponse generateMembershipRBACRoleBindingYAML(GenerateMembershipRBACRoleBindingYAMLRequest request)

Generates a YAML of the RBAC policies for the specified RoleBinding and its associated impersonation resources.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GenerateMembershipRBACRoleBindingYAMLRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gkehub/latest/com.google.cloud.gkehub.v1.GenerateMembershipRBACRoleBindingYAMLRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[GenerateMembershipRBACRoleBindingYAMLResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-gkehub/latest/com.google.cloud.gkehub.v1.GenerateMembershipRBACRoleBindingYAMLResponse)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### getFeature(GetFeatureRequest request)
    
    
    public Feature getFeature(GetFeatureRequest request)

Gets details of a single Feature.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetFeatureRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gkehub/latest/com.google.cloud.gkehub.v1.GetFeatureRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Feature](https://docs.cloud.google.com/java/docs/reference/google-cloud-gkehub/latest/com.google.cloud.gkehub.v1.Feature)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### getFleet(GetFleetRequest request)
    
    
    public Fleet getFleet(GetFleetRequest request)

Returns the details of a fleet.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetFleetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gkehub/latest/com.google.cloud.gkehub.v1.GetFleetRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Fleet](https://docs.cloud.google.com/java/docs/reference/google-cloud-gkehub/latest/com.google.cloud.gkehub.v1.Fleet)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### getMembership(GetMembershipRequest request)
    
    
    public Membership getMembership(GetMembershipRequest request)

Gets the details of a Membership.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetMembershipRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gkehub/latest/com.google.cloud.gkehub.v1.GetMembershipRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Membership](https://docs.cloud.google.com/java/docs/reference/google-cloud-gkehub/latest/com.google.cloud.gkehub.v1.Membership)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### getMembershipBinding(GetMembershipBindingRequest request)
    
    
    public MembershipBinding getMembershipBinding(GetMembershipBindingRequest request)

Returns the details of a MembershipBinding.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetMembershipBindingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gkehub/latest/com.google.cloud.gkehub.v1.GetMembershipBindingRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[MembershipBinding](https://docs.cloud.google.com/java/docs/reference/google-cloud-gkehub/latest/com.google.cloud.gkehub.v1.MembershipBinding)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### getMembershipRBACRoleBinding(GetMembershipRBACRoleBindingRequest request)
    
    
    public RBACRoleBinding getMembershipRBACRoleBinding(GetMembershipRBACRoleBindingRequest request)

Returns the details of a Membership RBACRoleBinding.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetMembershipRBACRoleBindingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gkehub/latest/com.google.cloud.gkehub.v1.GetMembershipRBACRoleBindingRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[RBACRoleBinding](https://docs.cloud.google.com/java/docs/reference/google-cloud-gkehub/latest/com.google.cloud.gkehub.v1.RBACRoleBinding)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### getScope(GetScopeRequest request)
    
    
    public Scope getScope(GetScopeRequest request)

Returns the details of a Scope.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetScopeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gkehub/latest/com.google.cloud.gkehub.v1.GetScopeRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Scope](https://docs.cloud.google.com/java/docs/reference/google-cloud-gkehub/latest/com.google.cloud.gkehub.v1.Scope)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### getScopeNamespace(GetScopeNamespaceRequest request)
    
    
    public Namespace getScopeNamespace(GetScopeNamespaceRequest request)

Returns the details of a fleet namespace.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetScopeNamespaceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gkehub/latest/com.google.cloud.gkehub.v1.GetScopeNamespaceRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Namespace](https://docs.cloud.google.com/java/docs/reference/google-cloud-gkehub/latest/com.google.cloud.gkehub.v1.Namespace)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### getScopeRBACRoleBinding(GetScopeRBACRoleBindingRequest request)
    
    
    public RBACRoleBinding getScopeRBACRoleBinding(GetScopeRBACRoleBindingRequest request)

Returns the details of a Scope RBACRoleBinding.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetScopeRBACRoleBindingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gkehub/latest/com.google.cloud.gkehub.v1.GetScopeRBACRoleBindingRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[RBACRoleBinding](https://docs.cloud.google.com/java/docs/reference/google-cloud-gkehub/latest/com.google.cloud.gkehub.v1.RBACRoleBinding)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### listBoundMemberships(ListBoundMembershipsRequest request)
    
    
    public ListBoundMembershipsResponse listBoundMemberships(ListBoundMembershipsRequest request)

Lists Memberships bound to a Scope. The response includes relevant Memberships from all regions.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListBoundMembershipsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gkehub/latest/com.google.cloud.gkehub.v1.ListBoundMembershipsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ListBoundMembershipsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-gkehub/latest/com.google.cloud.gkehub.v1.ListBoundMembershipsResponse)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### listFeatures(ListFeaturesRequest request)
    
    
    public ListFeaturesResponse listFeatures(ListFeaturesRequest request)

Lists Features in a given project and location.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListFeaturesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gkehub/latest/com.google.cloud.gkehub.v1.ListFeaturesRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ListFeaturesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-gkehub/latest/com.google.cloud.gkehub.v1.ListFeaturesResponse)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### listFleets(ListFleetsRequest request)
    
    
    public ListFleetsResponse listFleets(ListFleetsRequest request)

Returns all fleets within an organization or a project that the caller has access to.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListFleetsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gkehub/latest/com.google.cloud.gkehub.v1.ListFleetsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ListFleetsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-gkehub/latest/com.google.cloud.gkehub.v1.ListFleetsResponse)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### listMembershipBindings(ListMembershipBindingsRequest request)
    
    
    public ListMembershipBindingsResponse listMembershipBindings(ListMembershipBindingsRequest request)

Lists MembershipBindings.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListMembershipBindingsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gkehub/latest/com.google.cloud.gkehub.v1.ListMembershipBindingsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ListMembershipBindingsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-gkehub/latest/com.google.cloud.gkehub.v1.ListMembershipBindingsResponse)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### listMembershipRBACRoleBindings(ListMembershipRBACRoleBindingsRequest request)
    
    
    public ListMembershipRBACRoleBindingsResponse listMembershipRBACRoleBindings(ListMembershipRBACRoleBindingsRequest request)

Lists all Membership RBACRoleBindings.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListMembershipRBACRoleBindingsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gkehub/latest/com.google.cloud.gkehub.v1.ListMembershipRBACRoleBindingsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ListMembershipRBACRoleBindingsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-gkehub/latest/com.google.cloud.gkehub.v1.ListMembershipRBACRoleBindingsResponse)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### listMemberships(ListMembershipsRequest request)
    
    
    public ListMembershipsResponse listMemberships(ListMembershipsRequest request)

Lists Memberships in a given project and location.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListMembershipsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gkehub/latest/com.google.cloud.gkehub.v1.ListMembershipsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ListMembershipsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-gkehub/latest/com.google.cloud.gkehub.v1.ListMembershipsResponse)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### listPermittedScopes(ListPermittedScopesRequest request)
    
    
    public ListPermittedScopesResponse listPermittedScopes(ListPermittedScopesRequest request)

Lists permitted Scopes.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListPermittedScopesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gkehub/latest/com.google.cloud.gkehub.v1.ListPermittedScopesRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ListPermittedScopesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-gkehub/latest/com.google.cloud.gkehub.v1.ListPermittedScopesResponse)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### listScopeNamespaces(ListScopeNamespacesRequest request)
    
    
    public ListScopeNamespacesResponse listScopeNamespaces(ListScopeNamespacesRequest request)

Lists fleet namespaces.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListScopeNamespacesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gkehub/latest/com.google.cloud.gkehub.v1.ListScopeNamespacesRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ListScopeNamespacesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-gkehub/latest/com.google.cloud.gkehub.v1.ListScopeNamespacesResponse)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### listScopeRBACRoleBindings(ListScopeRBACRoleBindingsRequest request)
    
    
    public ListScopeRBACRoleBindingsResponse listScopeRBACRoleBindings(ListScopeRBACRoleBindingsRequest request)

Lists all Scope RBACRoleBindings.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListScopeRBACRoleBindingsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gkehub/latest/com.google.cloud.gkehub.v1.ListScopeRBACRoleBindingsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ListScopeRBACRoleBindingsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-gkehub/latest/com.google.cloud.gkehub.v1.ListScopeRBACRoleBindingsResponse)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### listScopes(ListScopesRequest request)
    
    
    public ListScopesResponse listScopes(ListScopesRequest request)

Lists Scopes.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListScopesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gkehub/latest/com.google.cloud.gkehub.v1.ListScopesRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ListScopesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-gkehub/latest/com.google.cloud.gkehub.v1.ListScopesResponse)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### updateFeature(UpdateFeatureRequest request)
    
    
    public Operation updateFeature(UpdateFeatureRequest request)

Updates an existing Feature.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateFeatureRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gkehub/latest/com.google.cloud.gkehub.v1.UpdateFeatureRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### updateFleet(UpdateFleetRequest request)
    
    
    public Operation updateFleet(UpdateFleetRequest request)

Updates a fleet.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateFleetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gkehub/latest/com.google.cloud.gkehub.v1.UpdateFleetRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### updateMembership(UpdateMembershipRequest request)
    
    
    public Operation updateMembership(UpdateMembershipRequest request)

Updates an existing Membership.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateMembershipRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gkehub/latest/com.google.cloud.gkehub.v1.UpdateMembershipRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### updateMembershipBinding(UpdateMembershipBindingRequest request)
    
    
    public Operation updateMembershipBinding(UpdateMembershipBindingRequest request)

Updates a MembershipBinding.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateMembershipBindingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gkehub/latest/com.google.cloud.gkehub.v1.UpdateMembershipBindingRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### updateMembershipRBACRoleBinding(UpdateMembershipRBACRoleBindingRequest request)
    
    
    public Operation updateMembershipRBACRoleBinding(UpdateMembershipRBACRoleBindingRequest request)

Updates a Membership RBACRoleBinding.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateMembershipRBACRoleBindingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gkehub/latest/com.google.cloud.gkehub.v1.UpdateMembershipRBACRoleBindingRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### updateScope(UpdateScopeRequest request)
    
    
    public Operation updateScope(UpdateScopeRequest request)

Updates a scopes.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateScopeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gkehub/latest/com.google.cloud.gkehub.v1.UpdateScopeRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### updateScopeNamespace(UpdateScopeNamespaceRequest request)
    
    
    public Operation updateScopeNamespace(UpdateScopeNamespaceRequest request)

Updates a fleet namespace.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateScopeNamespaceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gkehub/latest/com.google.cloud.gkehub.v1.UpdateScopeNamespaceRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### updateScopeRBACRoleBinding(UpdateScopeRBACRoleBindingRequest request)
    
    
    public Operation updateScopeRBACRoleBinding(UpdateScopeRBACRoleBindingRequest request)

Updates a Scope RBACRoleBinding.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateScopeRBACRoleBindingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gkehub/latest/com.google.cloud.gkehub.v1.UpdateScopeRBACRoleBindingRequest)`  
  
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
