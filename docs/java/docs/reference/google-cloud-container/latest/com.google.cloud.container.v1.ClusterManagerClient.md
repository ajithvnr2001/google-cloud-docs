---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.cloud.container.v1.ClusterManagerClient
title: Class ClusterManagerClient (2.102.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:41:48.308672+00:00
---

# Class ClusterManagerClient (2.102.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.cloud.container.v1.ClusterManagerClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class ClusterManagerClient (2.102.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.102.0 (latest)  2.98.0  2.97.0  2.96.0  2.94.0  2.91.0  2.90.0  2.88.0  2.86.0  2.85.0  2.84.0  2.83.0  2.81.0  2.79.0  2.78.0  2.77.0  2.76.0  2.75.0  2.73.0  2.71.0  2.70.0  2.67.0  2.66.0  2.65.0  2.63.0  2.62.0  2.61.0  2.60.0  2.59.0  2.58.0  2.57.0  2.56.0  2.55.0  2.54.0  2.52.0  2.51.0  2.50.0  2.49.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.40.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.27.0  2.26.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.2  2.4.1  2.3.8 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-container/google-cloud-container/src/main/java/com/google/cloud/container/v1/ClusterManagerClient.java)| [Product Reference](https://cloud.google.com/kubernetes-engine/)| [REST Documentation](https://cloud.google.com/kubernetes-engine/docs/reference/rest)  
---|---|---  
  
Service Description: Google Kubernetes Engine Cluster Manager v1

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ClusterManagerClient clusterManagerClient = ClusterManagerClient.create()) {
       String parent = "parent-995424086";
       ListClustersResponse response = clusterManagerClient.listClusters(parent);
     }
     

Note: close() needs to be called on the ClusterManagerClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
ListClusters |  Lists all clusters owned by a project in either the specified zone or all zones. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listClusters(ListClustersRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listClusters(String parent) 
  * listClusters(String projectId, String zone) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listClustersCallable() 

  
GetCluster |  Gets the details of a specific cluster. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getCluster(GetClusterRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getCluster(String name) 
  * getCluster(String projectId, String zone, String clusterId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getClusterCallable() 

  
CreateCluster |  Creates a cluster, consisting of the specified number and type of Google Compute Engine instances.  By default, the cluster is created in the project's [default network](https://cloud.google.com/compute/docs/networks-and-firewalls#networks).  One firewall is added for the cluster. After cluster creation, the kubelet creates routes for each node to allow the containers on that node to communicate with all other instances in the cluster.  Finally, an entry is added to the project's global metadata indicating which CIDR range the cluster is using. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createCluster(CreateClusterRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * createCluster(String parent, Cluster cluster) 
  * createCluster(String projectId, String zone, Cluster cluster) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createClusterCallable() 

  
UpdateCluster |  Updates the settings of a specific cluster. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateCluster(UpdateClusterRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updateCluster(String name, ClusterUpdate update) 
  * updateCluster(String projectId, String zone, String clusterId, ClusterUpdate update) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateClusterCallable() 

  
UpdateNodePool |  Updates the version and/or image type for the specified node pool. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateNodePool(UpdateNodePoolRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateNodePoolCallable() 

  
SetNodePoolAutoscaling |  Sets the autoscaling settings for the specified node pool. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * setNodePoolAutoscaling(SetNodePoolAutoscalingRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * setNodePoolAutoscalingCallable() 

  
SetLoggingService |  Sets the logging service for a specific cluster. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * setLoggingService(SetLoggingServiceRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * setLoggingService(String name, String loggingService) 
  * setLoggingService(String projectId, String zone, String clusterId, String loggingService) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * setLoggingServiceCallable() 

  
SetMonitoringService |  Sets the monitoring service for a specific cluster. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * setMonitoringService(SetMonitoringServiceRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * setMonitoringService(String name, String monitoringService) 
  * setMonitoringService(String projectId, String zone, String clusterId, String monitoringService) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * setMonitoringServiceCallable() 

  
SetAddonsConfig |  Sets the addons for a specific cluster. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * setAddonsConfig(SetAddonsConfigRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * setAddonsConfig(String name, AddonsConfig addonsConfig) 
  * setAddonsConfig(String projectId, String zone, String clusterId, AddonsConfig addonsConfig) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * setAddonsConfigCallable() 

  
SetLocations |  Sets the locations for a specific cluster. Deprecated. Use [projects.locations.clusters.update](https://cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters/update) instead. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * setLocations(SetLocationsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * setLocations(String name, List<String> locations) 
  * setLocations(String projectId, String zone, String clusterId, List<String> locations) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * setLocationsCallable() 

  
UpdateMaster |  Updates the master for a specific cluster. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateMaster(UpdateMasterRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updateMaster(String name, String masterVersion) 
  * updateMaster(String projectId, String zone, String clusterId, String masterVersion) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateMasterCallable() 

  
SetMasterAuth |  Sets master auth materials. Currently supports changing the admin password or a specific cluster, either via password generation or explicitly setting the password. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * setMasterAuth(SetMasterAuthRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * setMasterAuthCallable() 

  
DeleteCluster |  Deletes the cluster, including the Kubernetes endpoint and all worker nodes.  Firewalls and routes that were configured during cluster creation are also deleted.  Other Google Compute Engine resources that might be in use by the cluster, such as load balancer resources, are not deleted if they weren't present when the cluster was initially created. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteCluster(DeleteClusterRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * deleteCluster(String name) 
  * deleteCluster(String projectId, String zone, String clusterId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteClusterCallable() 

  
ListOperations |  Lists all operations in a project in a specific zone or all zones. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listOperations(ListOperationsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listOperations(String parent) 
  * listOperations(String projectId, String zone) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listOperationsCallable() 

  
GetOperation |  Gets the specified operation. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getOperation(GetOperationRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getOperation(String name) 
  * getOperation(String projectId, String zone, String operationId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getOperationCallable() 

  
CancelOperation |  Cancels the specified operation. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * cancelOperation(CancelOperationRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * cancelOperation(String name) 
  * cancelOperation(String projectId, String zone, String operationId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * cancelOperationCallable() 

  
GetServerConfig |  Returns configuration info about the Google Kubernetes Engine service. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getServerConfig(GetServerConfigRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getServerConfig(String name) 
  * getServerConfig(String projectId, String zone) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getServerConfigCallable() 

  
GetJSONWebKeys |  Gets the public component of the cluster signing keys in JSON Web Key format. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getJSONWebKeys(GetJSONWebKeysRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getJSONWebKeysCallable() 

  
ListNodePools |  Lists the node pools for a cluster. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listNodePools(ListNodePoolsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listNodePools(String parent) 
  * listNodePools(String projectId, String zone, String clusterId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listNodePoolsCallable() 

  
GetNodePool |  Retrieves the requested node pool. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getNodePool(GetNodePoolRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getNodePool(String name) 
  * getNodePool(String projectId, String zone, String clusterId, String nodePoolId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getNodePoolCallable() 

  
CreateNodePool |  Creates a node pool for a cluster. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createNodePool(CreateNodePoolRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * createNodePool(String parent, NodePool nodePool) 
  * createNodePool(String projectId, String zone, String clusterId, NodePool nodePool) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createNodePoolCallable() 

  
DeleteNodePool |  Deletes a node pool from a cluster. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteNodePool(DeleteNodePoolRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * deleteNodePool(String name) 
  * deleteNodePool(String projectId, String zone, String clusterId, String nodePoolId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteNodePoolCallable() 

  
CompleteNodePoolUpgrade |  CompleteNodePoolUpgrade will signal an on-going node pool upgrade to complete. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * completeNodePoolUpgrade(CompleteNodePoolUpgradeRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * completeNodePoolUpgradeCallable() 

  
RollbackNodePoolUpgrade |  Rolls back a previously Aborted or Failed NodePool upgrade. This makes no changes if the last upgrade successfully completed. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * rollbackNodePoolUpgrade(RollbackNodePoolUpgradeRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * rollbackNodePoolUpgrade(String name) 
  * rollbackNodePoolUpgrade(String projectId, String zone, String clusterId, String nodePoolId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * rollbackNodePoolUpgradeCallable() 

  
SetNodePoolManagement |  Sets the NodeManagement options for a node pool. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * setNodePoolManagement(SetNodePoolManagementRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * setNodePoolManagementCallable() 

  
SetLabels |  Sets labels on a cluster. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * setLabels(SetLabelsRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * setLabelsCallable() 

  
SetLegacyAbac |  Enables or disables the ABAC authorization mechanism on a cluster. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * setLegacyAbac(SetLegacyAbacRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * setLegacyAbac(String name, boolean enabled) 
  * setLegacyAbac(String projectId, String zone, String clusterId, boolean enabled) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * setLegacyAbacCallable() 

  
StartIPRotation |  Starts master IP rotation. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * startIPRotation(StartIPRotationRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * startIPRotation(String name) 
  * startIPRotation(String projectId, String zone, String clusterId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * startIPRotationCallable() 

  
CompleteIPRotation |  Completes master IP rotation. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * completeIPRotation(CompleteIPRotationRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * completeIPRotation(String name) 
  * completeIPRotation(String projectId, String zone, String clusterId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * completeIPRotationCallable() 

  
SetNodePoolSize |  Sets the size for a specific node pool. The new size will be used for all replicas, including future replicas created by modifying NodePool.locations. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * setNodePoolSize(SetNodePoolSizeRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * setNodePoolSizeCallable() 

  
SetNetworkPolicy |  Enables or disables Network Policy for a cluster. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * setNetworkPolicy(SetNetworkPolicyRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * setNetworkPolicy(String name, NetworkPolicy networkPolicy) 
  * setNetworkPolicy(String projectId, String zone, String clusterId, NetworkPolicy networkPolicy) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * setNetworkPolicyCallable() 

  
SetMaintenancePolicy |  Sets the maintenance policy for a cluster. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * setMaintenancePolicy(SetMaintenancePolicyRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * setMaintenancePolicy(String name, MaintenancePolicy maintenancePolicy) 
  * setMaintenancePolicy(String projectId, String zone, String clusterId, MaintenancePolicy maintenancePolicy) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * setMaintenancePolicyCallable() 

  
ListUsableSubnetworks |  Lists subnetworks that are usable for creating clusters in a project. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listUsableSubnetworks(ListUsableSubnetworksRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listUsableSubnetworksPagedCallable() 
  * listUsableSubnetworksCallable() 

  
CheckAutopilotCompatibility |  Checks the cluster compatibility with Autopilot mode, and returns a list of compatibility issues. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * checkAutopilotCompatibility(CheckAutopilotCompatibilityRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * checkAutopilotCompatibilityCallable() 

  
FetchClusterUpgradeInfo |  Fetch upgrade information of a specific cluster. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * fetchClusterUpgradeInfo(FetchClusterUpgradeInfoRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * fetchClusterUpgradeInfo(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * fetchClusterUpgradeInfoCallable() 

  
FetchNodePoolUpgradeInfo |  Fetch upgrade information of a specific node pool. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * fetchNodePoolUpgradeInfo(FetchNodePoolUpgradeInfoRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * fetchNodePoolUpgradeInfo(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * fetchNodePoolUpgradeInfoCallable() 

  
CompleteControlPlaneUpgrade |  CompleteControlPlaneUpgrade completes the rollback-safe upgrade by performing the step two upgrade for a specific cluster. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * completeControlPlaneUpgrade(CompleteControlPlaneUpgradeRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * completeControlPlaneUpgradeCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of ClusterManagerSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     ClusterManagerSettings clusterManagerSettings =
         ClusterManagerSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     ClusterManagerClient clusterManagerClient = ClusterManagerClient.create(clusterManagerSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     ClusterManagerSettings clusterManagerSettings =
         ClusterManagerSettings.newBuilder().setEndpoint(myEndpoint).build();
     ClusterManagerClient clusterManagerClient = ClusterManagerClient.create(clusterManagerSettings);
     

To use REST (HTTP1.1/JSON) transport (instead of gRPC) for sending and receiving requests over the wire:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     ClusterManagerSettings clusterManagerSettings =
         ClusterManagerSettings.newHttpJsonBuilder().build();
     ClusterManagerClient clusterManagerClient = ClusterManagerClient.create(clusterManagerSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > ClusterManagerClient

## Static Methods 

### create()
    
    
    public static final ClusterManagerClient create()

Constructs an instance of ClusterManagerClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[ClusterManagerClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.cloud.container.v1.ClusterManagerClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(ClusterManagerSettings settings)
    
    
    public static final ClusterManagerClient create(ClusterManagerSettings settings)

Constructs an instance of ClusterManagerClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[ClusterManagerSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.cloud.container.v1.ClusterManagerSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterManagerClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.cloud.container.v1.ClusterManagerClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(ClusterManagerStub stub)
    
    
    public static final ClusterManagerClient create(ClusterManagerStub stub)

Constructs an instance of ClusterManagerClient, using the given stub for making calls. This is for advanced usage - prefer using create(ClusterManagerSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[ClusterManagerStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.cloud.container.v1.stub.ClusterManagerStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterManagerClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.cloud.container.v1.ClusterManagerClient)` |   
  
## Constructors 

### ClusterManagerClient(ClusterManagerSettings settings)
    
    
    protected ClusterManagerClient(ClusterManagerSettings settings)

Constructs an instance of ClusterManagerClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[ClusterManagerSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.cloud.container.v1.ClusterManagerSettings)`  
  
  
### ClusterManagerClient(ClusterManagerStub stub)
    
    
    protected ClusterManagerClient(ClusterManagerStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[ClusterManagerStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.cloud.container.v1.stub.ClusterManagerStub)`  
  
  
## Methods 

### awaitTermination(long duration, TimeUnit unit)
    
    
    public boolean awaitTermination(long duration, TimeUnit unit)

**Parameters**  
---  
**Name** | **Description**  
`duration` | `[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`unit` | `[TimeUnit](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/TimeUnit.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[InterruptedException](https://docs.oracle.com/javase/8/docs/api/java/lang/InterruptedException.html)` |   
  
### cancelOperation(CancelOperationRequest request)
    
    
    public final void cancelOperation(CancelOperationRequest request)

Cancels the specified operation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ClusterManagerClient clusterManagerClient = ClusterManagerClient.create()) {
       CancelOperationRequest request =
           CancelOperationRequest.newBuilder()
               .setProjectId("projectId-894832108")
               .setZone("zone3744684")
               .setOperationId("operationId129704162")
               .setName("name3373707")
               .build();
       clusterManagerClient.cancelOperation(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CancelOperationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.CancelOperationRequest)`  
The request object containing all of the parameters for the API call.  
  
### cancelOperation(String name)
    
    
    public final void cancelOperation(String name)

Cancels the specified operation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ClusterManagerClient clusterManagerClient = ClusterManagerClient.create()) {
       String name = "name3373707";
       clusterManagerClient.cancelOperation(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name (project, location, operation id) of the operation to cancel. Specified in the format `projects/*/locations/*/operations/*`.  
  
### cancelOperation(String projectId, String zone, String operationId)
    
    
    public final void cancelOperation(String projectId, String zone, String operationId)

Cancels the specified operation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ClusterManagerClient clusterManagerClient = ClusterManagerClient.create()) {
       String projectId = "projectId-894832108";
       String zone = "zone3744684";
       String operationId = "operationId129704162";
       clusterManagerClient.cancelOperation(projectId, zone, operationId);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Deprecated. The Google Developers Console [project ID or project number](https://cloud.google.com/resource-manager/docs/creating-managing-projects). This field has been deprecated and replaced by the name field.  
`zone` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Deprecated. The name of the Google Compute Engine [zone](https://cloud.google.com/compute/docs/zones#available) in which the operation resides. This field has been deprecated and replaced by the name field.  
`operationId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Deprecated. The server-assigned `name` of the operation. This field has been deprecated and replaced by the name field.  
  
### cancelOperationCallable()
    
    
    public final UnaryCallable<CancelOperationRequest,Empty> cancelOperationCallable()

Cancels the specified operation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ClusterManagerClient clusterManagerClient = ClusterManagerClient.create()) {
       CancelOperationRequest request =
           CancelOperationRequest.newBuilder()
               .setProjectId("projectId-894832108")
               .setZone("zone3744684")
               .setOperationId("operationId129704162")
               .setName("name3373707")
               .build();
       ApiFuture<Empty> future = clusterManagerClient.cancelOperationCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CancelOperationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.CancelOperationRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### checkAutopilotCompatibility(CheckAutopilotCompatibilityRequest request)
    
    
    public final CheckAutopilotCompatibilityResponse checkAutopilotCompatibility(CheckAutopilotCompatibilityRequest request)

Checks the cluster compatibility with Autopilot mode, and returns a list of compatibility issues.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ClusterManagerClient clusterManagerClient = ClusterManagerClient.create()) {
       CheckAutopilotCompatibilityRequest request =
           CheckAutopilotCompatibilityRequest.newBuilder().setName("name3373707").build();
       CheckAutopilotCompatibilityResponse response =
           clusterManagerClient.checkAutopilotCompatibility(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CheckAutopilotCompatibilityRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.CheckAutopilotCompatibilityRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[CheckAutopilotCompatibilityResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.CheckAutopilotCompatibilityResponse)` |   
  
### checkAutopilotCompatibilityCallable()
    
    
    public final UnaryCallable<CheckAutopilotCompatibilityRequest,CheckAutopilotCompatibilityResponse> checkAutopilotCompatibilityCallable()

Checks the cluster compatibility with Autopilot mode, and returns a list of compatibility issues.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ClusterManagerClient clusterManagerClient = ClusterManagerClient.create()) {
       CheckAutopilotCompatibilityRequest request =
           CheckAutopilotCompatibilityRequest.newBuilder().setName("name3373707").build();
       ApiFuture<CheckAutopilotCompatibilityResponse> future =
           clusterManagerClient.checkAutopilotCompatibilityCallable().futureCall(request);
       // Do something.
       CheckAutopilotCompatibilityResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CheckAutopilotCompatibilityRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.CheckAutopilotCompatibilityRequest),[CheckAutopilotCompatibilityResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.CheckAutopilotCompatibilityResponse)>` |   
  
### close()
    
    
    public final void close()

### completeControlPlaneUpgrade(CompleteControlPlaneUpgradeRequest request)
    
    
    public final Operation completeControlPlaneUpgrade(CompleteControlPlaneUpgradeRequest request)

CompleteControlPlaneUpgrade completes the rollback-safe upgrade by performing the step two upgrade for a specific cluster.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ClusterManagerClient clusterManagerClient = ClusterManagerClient.create()) {
       CompleteControlPlaneUpgradeRequest request =
           CompleteControlPlaneUpgradeRequest.newBuilder()
               .setName("name3373707")
               .setVersion("version351608024")
               .build();
       Operation response = clusterManagerClient.completeControlPlaneUpgrade(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CompleteControlPlaneUpgradeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.CompleteControlPlaneUpgradeRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.Operation)` |   
  
### completeControlPlaneUpgradeCallable()
    
    
    public final UnaryCallable<CompleteControlPlaneUpgradeRequest,Operation> completeControlPlaneUpgradeCallable()

CompleteControlPlaneUpgrade completes the rollback-safe upgrade by performing the step two upgrade for a specific cluster.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ClusterManagerClient clusterManagerClient = ClusterManagerClient.create()) {
       CompleteControlPlaneUpgradeRequest request =
           CompleteControlPlaneUpgradeRequest.newBuilder()
               .setName("name3373707")
               .setVersion("version351608024")
               .build();
       ApiFuture<Operation> future =
           clusterManagerClient.completeControlPlaneUpgradeCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CompleteControlPlaneUpgradeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.CompleteControlPlaneUpgradeRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.Operation)>` |   
  
### completeIPRotation(CompleteIPRotationRequest request)
    
    
    public final Operation completeIPRotation(CompleteIPRotationRequest request)

Completes master IP rotation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ClusterManagerClient clusterManagerClient = ClusterManagerClient.create()) {
       CompleteIPRotationRequest request =
           CompleteIPRotationRequest.newBuilder()
               .setProjectId("projectId-894832108")
               .setZone("zone3744684")
               .setClusterId("clusterId561939637")
               .setName("name3373707")
               .build();
       Operation response = clusterManagerClient.completeIPRotation(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CompleteIPRotationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.CompleteIPRotationRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.Operation)` |   
  
### completeIPRotation(String name)
    
    
    public final Operation completeIPRotation(String name)

Completes master IP rotation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ClusterManagerClient clusterManagerClient = ClusterManagerClient.create()) {
       String name = "name3373707";
       Operation response = clusterManagerClient.completeIPRotation(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name (project, location, cluster name) of the cluster to complete IP rotation. Specified in the format `projects/*/locations/*/clusters/*`.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.Operation)` |   
  
### completeIPRotation(String projectId, String zone, String clusterId)
    
    
    public final Operation completeIPRotation(String projectId, String zone, String clusterId)

Completes master IP rotation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ClusterManagerClient clusterManagerClient = ClusterManagerClient.create()) {
       String projectId = "projectId-894832108";
       String zone = "zone3744684";
       String clusterId = "clusterId561939637";
       Operation response = clusterManagerClient.completeIPRotation(projectId, zone, clusterId);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Deprecated. The Google Developers Console [project ID or project number](https://cloud.google.com/resource-manager/docs/creating-managing-projects). This field has been deprecated and replaced by the name field.  
`zone` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Deprecated. The name of the Google Compute Engine [zone](https://cloud.google.com/compute/docs/zones#available) in which the cluster resides. This field has been deprecated and replaced by the name field.  
`clusterId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Deprecated. The name of the cluster. This field has been deprecated and replaced by the name field.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.Operation)` |   
  
### completeIPRotationCallable()
    
    
    public final UnaryCallable<CompleteIPRotationRequest,Operation> completeIPRotationCallable()

Completes master IP rotation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ClusterManagerClient clusterManagerClient = ClusterManagerClient.create()) {
       CompleteIPRotationRequest request =
           CompleteIPRotationRequest.newBuilder()
               .setProjectId("projectId-894832108")
               .setZone("zone3744684")
               .setClusterId("clusterId561939637")
               .setName("name3373707")
               .build();
       ApiFuture<Operation> future =
           clusterManagerClient.completeIPRotationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CompleteIPRotationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.CompleteIPRotationRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.Operation)>` |   
  
### completeNodePoolUpgrade(CompleteNodePoolUpgradeRequest request)
    
    
    public final void completeNodePoolUpgrade(CompleteNodePoolUpgradeRequest request)

CompleteNodePoolUpgrade will signal an on-going node pool upgrade to complete.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ClusterManagerClient clusterManagerClient = ClusterManagerClient.create()) {
       CompleteNodePoolUpgradeRequest request =
           CompleteNodePoolUpgradeRequest.newBuilder().setName("name3373707").build();
       clusterManagerClient.completeNodePoolUpgrade(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CompleteNodePoolUpgradeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.CompleteNodePoolUpgradeRequest)`  
The request object containing all of the parameters for the API call.  
  
### completeNodePoolUpgradeCallable()
    
    
    public final UnaryCallable<CompleteNodePoolUpgradeRequest,Empty> completeNodePoolUpgradeCallable()

CompleteNodePoolUpgrade will signal an on-going node pool upgrade to complete.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ClusterManagerClient clusterManagerClient = ClusterManagerClient.create()) {
       CompleteNodePoolUpgradeRequest request =
           CompleteNodePoolUpgradeRequest.newBuilder().setName("name3373707").build();
       ApiFuture<Empty> future =
           clusterManagerClient.completeNodePoolUpgradeCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CompleteNodePoolUpgradeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.CompleteNodePoolUpgradeRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### createCluster(CreateClusterRequest request)
    
    
    public final Operation createCluster(CreateClusterRequest request)

Creates a cluster, consisting of the specified number and type of Google Compute Engine instances.

By default, the cluster is created in the project's [default network](https://cloud.google.com/compute/docs/networks-and-firewalls#networks).

One firewall is added for the cluster. After cluster creation, the kubelet creates routes for each node to allow the containers on that node to communicate with all other instances in the cluster.

Finally, an entry is added to the project's global metadata indicating which CIDR range the cluster is using.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ClusterManagerClient clusterManagerClient = ClusterManagerClient.create()) {
       CreateClusterRequest request =
           CreateClusterRequest.newBuilder()
               .setProjectId("projectId-894832108")
               .setZone("zone3744684")
               .setCluster(Cluster.newBuilder().build())
               .setParent("parent-995424086")
               .build();
       Operation response = clusterManagerClient.createCluster(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.CreateClusterRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.Operation)` |   
  
### createCluster(String parent, Cluster cluster)
    
    
    public final Operation createCluster(String parent, Cluster cluster)

Creates a cluster, consisting of the specified number and type of Google Compute Engine instances.

By default, the cluster is created in the project's [default network](https://cloud.google.com/compute/docs/networks-and-firewalls#networks).

One firewall is added for the cluster. After cluster creation, the kubelet creates routes for each node to allow the containers on that node to communicate with all other instances in the cluster.

Finally, an entry is added to the project's global metadata indicating which CIDR range the cluster is using.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ClusterManagerClient clusterManagerClient = ClusterManagerClient.create()) {
       String parent = "parent-995424086";
       Cluster cluster = Cluster.newBuilder().build();
       Operation response = clusterManagerClient.createCluster(parent, cluster);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The parent (project and location) where the cluster will be created. Specified in the format `projects/*/locations/*`.  
`cluster` | `[Cluster](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.Cluster)`  
Required. A [cluster resource](https://cloud.google.com/container-engine/reference/rest/v1/projects.locations.clusters)  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.Operation)` |   
  
### createCluster(String projectId, String zone, Cluster cluster)
    
    
    public final Operation createCluster(String projectId, String zone, Cluster cluster)

Creates a cluster, consisting of the specified number and type of Google Compute Engine instances.

By default, the cluster is created in the project's [default network](https://cloud.google.com/compute/docs/networks-and-firewalls#networks).

One firewall is added for the cluster. After cluster creation, the kubelet creates routes for each node to allow the containers on that node to communicate with all other instances in the cluster.

Finally, an entry is added to the project's global metadata indicating which CIDR range the cluster is using.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ClusterManagerClient clusterManagerClient = ClusterManagerClient.create()) {
       String projectId = "projectId-894832108";
       String zone = "zone3744684";
       Cluster cluster = Cluster.newBuilder().build();
       Operation response = clusterManagerClient.createCluster(projectId, zone, cluster);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Deprecated. The Google Developers Console [project ID or project number](https://cloud.google.com/resource-manager/docs/creating-managing-projects). This field has been deprecated and replaced by the parent field.  
`zone` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Deprecated. The name of the Google Compute Engine [zone](https://cloud.google.com/compute/docs/zones#available) in which the cluster resides. This field has been deprecated and replaced by the parent field.  
`cluster` | `[Cluster](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.Cluster)`  
Required. A [cluster resource](https://cloud.google.com/container-engine/reference/rest/v1/projects.locations.clusters)  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.Operation)` |   
  
### createClusterCallable()
    
    
    public final UnaryCallable<CreateClusterRequest,Operation> createClusterCallable()

Creates a cluster, consisting of the specified number and type of Google Compute Engine instances.

By default, the cluster is created in the project's [default network](https://cloud.google.com/compute/docs/networks-and-firewalls#networks).

One firewall is added for the cluster. After cluster creation, the kubelet creates routes for each node to allow the containers on that node to communicate with all other instances in the cluster.

Finally, an entry is added to the project's global metadata indicating which CIDR range the cluster is using.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ClusterManagerClient clusterManagerClient = ClusterManagerClient.create()) {
       CreateClusterRequest request =
           CreateClusterRequest.newBuilder()
               .setProjectId("projectId-894832108")
               .setZone("zone3744684")
               .setCluster(Cluster.newBuilder().build())
               .setParent("parent-995424086")
               .build();
       ApiFuture<Operation> future =
           clusterManagerClient.createClusterCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.CreateClusterRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.Operation)>` |   
  
### createNodePool(CreateNodePoolRequest request)
    
    
    public final Operation createNodePool(CreateNodePoolRequest request)

Creates a node pool for a cluster.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ClusterManagerClient clusterManagerClient = ClusterManagerClient.create()) {
       CreateNodePoolRequest request =
           CreateNodePoolRequest.newBuilder()
               .setProjectId("projectId-894832108")
               .setZone("zone3744684")
               .setClusterId("clusterId561939637")
               .setNodePool(NodePool.newBuilder().build())
               .setParent("parent-995424086")
               .build();
       Operation response = clusterManagerClient.createNodePool(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateNodePoolRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.CreateNodePoolRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.Operation)` |   
  
### createNodePool(String parent, NodePool nodePool)
    
    
    public final Operation createNodePool(String parent, NodePool nodePool)

Creates a node pool for a cluster.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ClusterManagerClient clusterManagerClient = ClusterManagerClient.create()) {
       String parent = "parent-995424086";
       NodePool nodePool = NodePool.newBuilder().build();
       Operation response = clusterManagerClient.createNodePool(parent, nodePool);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The parent (project, location, cluster name) where the node pool will be created. Specified in the format `projects/*/locations/*/clusters/*`.  
`nodePool` | `[NodePool](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.NodePool)`  
Required. The node pool to create.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.Operation)` |   
  
### createNodePool(String projectId, String zone, String clusterId, NodePool nodePool)
    
    
    public final Operation createNodePool(String projectId, String zone, String clusterId, NodePool nodePool)

Creates a node pool for a cluster.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ClusterManagerClient clusterManagerClient = ClusterManagerClient.create()) {
       String projectId = "projectId-894832108";
       String zone = "zone3744684";
       String clusterId = "clusterId561939637";
       NodePool nodePool = NodePool.newBuilder().build();
       Operation response =
           clusterManagerClient.createNodePool(projectId, zone, clusterId, nodePool);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Deprecated. The Google Developers Console [project ID or project number](https://cloud.google.com/resource-manager/docs/creating-managing-projects). This field has been deprecated and replaced by the parent field.  
`zone` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Deprecated. The name of the Google Compute Engine [zone](https://cloud.google.com/compute/docs/zones#available) in which the cluster resides. This field has been deprecated and replaced by the parent field.  
`clusterId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Deprecated. The name of the cluster. This field has been deprecated and replaced by the parent field.  
`nodePool` | `[NodePool](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.NodePool)`  
Required. The node pool to create.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.Operation)` |   
  
### createNodePoolCallable()
    
    
    public final UnaryCallable<CreateNodePoolRequest,Operation> createNodePoolCallable()

Creates a node pool for a cluster.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ClusterManagerClient clusterManagerClient = ClusterManagerClient.create()) {
       CreateNodePoolRequest request =
           CreateNodePoolRequest.newBuilder()
               .setProjectId("projectId-894832108")
               .setZone("zone3744684")
               .setClusterId("clusterId561939637")
               .setNodePool(NodePool.newBuilder().build())
               .setParent("parent-995424086")
               .build();
       ApiFuture<Operation> future =
           clusterManagerClient.createNodePoolCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateNodePoolRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.CreateNodePoolRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.Operation)>` |   
  
### deleteCluster(DeleteClusterRequest request)
    
    
    public final Operation deleteCluster(DeleteClusterRequest request)

Deletes the cluster, including the Kubernetes endpoint and all worker nodes.

Firewalls and routes that were configured during cluster creation are also deleted.

Other Google Compute Engine resources that might be in use by the cluster, such as load balancer resources, are not deleted if they weren't present when the cluster was initially created.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ClusterManagerClient clusterManagerClient = ClusterManagerClient.create()) {
       DeleteClusterRequest request =
           DeleteClusterRequest.newBuilder()
               .setProjectId("projectId-894832108")
               .setZone("zone3744684")
               .setClusterId("clusterId561939637")
               .setName("name3373707")
               .build();
       Operation response = clusterManagerClient.deleteCluster(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.DeleteClusterRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.Operation)` |   
  
### deleteCluster(String name)
    
    
    public final Operation deleteCluster(String name)

Deletes the cluster, including the Kubernetes endpoint and all worker nodes.

Firewalls and routes that were configured during cluster creation are also deleted.

Other Google Compute Engine resources that might be in use by the cluster, such as load balancer resources, are not deleted if they weren't present when the cluster was initially created.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ClusterManagerClient clusterManagerClient = ClusterManagerClient.create()) {
       String name = "name3373707";
       Operation response = clusterManagerClient.deleteCluster(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name (project, location, cluster) of the cluster to delete. Specified in the format `projects/*/locations/*/clusters/*`.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.Operation)` |   
  
### deleteCluster(String projectId, String zone, String clusterId)
    
    
    public final Operation deleteCluster(String projectId, String zone, String clusterId)

Deletes the cluster, including the Kubernetes endpoint and all worker nodes.

Firewalls and routes that were configured during cluster creation are also deleted.

Other Google Compute Engine resources that might be in use by the cluster, such as load balancer resources, are not deleted if they weren't present when the cluster was initially created.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ClusterManagerClient clusterManagerClient = ClusterManagerClient.create()) {
       String projectId = "projectId-894832108";
       String zone = "zone3744684";
       String clusterId = "clusterId561939637";
       Operation response = clusterManagerClient.deleteCluster(projectId, zone, clusterId);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Deprecated. The Google Developers Console [project ID or project number](https://cloud.google.com/resource-manager/docs/creating-managing-projects). This field has been deprecated and replaced by the name field.  
`zone` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Deprecated. The name of the Google Compute Engine [zone](https://cloud.google.com/compute/docs/zones#available) in which the cluster resides. This field has been deprecated and replaced by the name field.  
`clusterId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Deprecated. The name of the cluster to delete. This field has been deprecated and replaced by the name field.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.Operation)` |   
  
### deleteClusterCallable()
    
    
    public final UnaryCallable<DeleteClusterRequest,Operation> deleteClusterCallable()

Deletes the cluster, including the Kubernetes endpoint and all worker nodes.

Firewalls and routes that were configured during cluster creation are also deleted.

Other Google Compute Engine resources that might be in use by the cluster, such as load balancer resources, are not deleted if they weren't present when the cluster was initially created.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ClusterManagerClient clusterManagerClient = ClusterManagerClient.create()) {
       DeleteClusterRequest request =
           DeleteClusterRequest.newBuilder()
               .setProjectId("projectId-894832108")
               .setZone("zone3744684")
               .setClusterId("clusterId561939637")
               .setName("name3373707")
               .build();
       ApiFuture<Operation> future =
           clusterManagerClient.deleteClusterCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.DeleteClusterRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.Operation)>` |   
  
### deleteNodePool(DeleteNodePoolRequest request)
    
    
    public final Operation deleteNodePool(DeleteNodePoolRequest request)

Deletes a node pool from a cluster.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ClusterManagerClient clusterManagerClient = ClusterManagerClient.create()) {
       DeleteNodePoolRequest request =
           DeleteNodePoolRequest.newBuilder()
               .setProjectId("projectId-894832108")
               .setZone("zone3744684")
               .setClusterId("clusterId561939637")
               .setNodePoolId("nodePoolId1121557241")
               .setName("name3373707")
               .build();
       Operation response = clusterManagerClient.deleteNodePool(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteNodePoolRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.DeleteNodePoolRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.Operation)` |   
  
### deleteNodePool(String name)
    
    
    public final Operation deleteNodePool(String name)

Deletes a node pool from a cluster.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ClusterManagerClient clusterManagerClient = ClusterManagerClient.create()) {
       String name = "name3373707";
       Operation response = clusterManagerClient.deleteNodePool(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name (project, location, cluster, node pool id) of the node pool to delete. Specified in the format `projects/*/locations/*/clusters/*/nodePools/*`.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.Operation)` |   
  
### deleteNodePool(String projectId, String zone, String clusterId, String nodePoolId)
    
    
    public final Operation deleteNodePool(String projectId, String zone, String clusterId, String nodePoolId)

Deletes a node pool from a cluster.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ClusterManagerClient clusterManagerClient = ClusterManagerClient.create()) {
       String projectId = "projectId-894832108";
       String zone = "zone3744684";
       String clusterId = "clusterId561939637";
       String nodePoolId = "nodePoolId1121557241";
       Operation response =
           clusterManagerClient.deleteNodePool(projectId, zone, clusterId, nodePoolId);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Deprecated. The Google Developers Console [project ID or project number](https://cloud.google.com/resource-manager/docs/creating-managing-projects). This field has been deprecated and replaced by the name field.  
`zone` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Deprecated. The name of the Google Compute Engine [zone](https://cloud.google.com/compute/docs/zones#available) in which the cluster resides. This field has been deprecated and replaced by the name field.  
`clusterId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Deprecated. The name of the cluster. This field has been deprecated and replaced by the name field.  
`nodePoolId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Deprecated. The name of the node pool to delete. This field has been deprecated and replaced by the name field.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.Operation)` |   
  
### deleteNodePoolCallable()
    
    
    public final UnaryCallable<DeleteNodePoolRequest,Operation> deleteNodePoolCallable()

Deletes a node pool from a cluster.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ClusterManagerClient clusterManagerClient = ClusterManagerClient.create()) {
       DeleteNodePoolRequest request =
           DeleteNodePoolRequest.newBuilder()
               .setProjectId("projectId-894832108")
               .setZone("zone3744684")
               .setClusterId("clusterId561939637")
               .setNodePoolId("nodePoolId1121557241")
               .setName("name3373707")
               .build();
       ApiFuture<Operation> future =
           clusterManagerClient.deleteNodePoolCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteNodePoolRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.DeleteNodePoolRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.Operation)>` |   
  
### fetchClusterUpgradeInfo(FetchClusterUpgradeInfoRequest request)
    
    
    public final ClusterUpgradeInfo fetchClusterUpgradeInfo(FetchClusterUpgradeInfoRequest request)

Fetch upgrade information of a specific cluster.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ClusterManagerClient clusterManagerClient = ClusterManagerClient.create()) {
       FetchClusterUpgradeInfoRequest request =
           FetchClusterUpgradeInfoRequest.newBuilder()
               .setName("name3373707")
               .setVersion("version351608024")
               .build();
       ClusterUpgradeInfo response = clusterManagerClient.fetchClusterUpgradeInfo(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[FetchClusterUpgradeInfoRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.FetchClusterUpgradeInfoRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpgradeInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.ClusterUpgradeInfo)` |   
  
### fetchClusterUpgradeInfo(String name)
    
    
    public final ClusterUpgradeInfo fetchClusterUpgradeInfo(String name)

Fetch upgrade information of a specific cluster.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ClusterManagerClient clusterManagerClient = ClusterManagerClient.create()) {
       String name = "name3373707";
       ClusterUpgradeInfo response = clusterManagerClient.fetchClusterUpgradeInfo(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name (project, location, cluster) of the cluster to get. Specified in the format `projects/*/locations/*/clusters/*` or `projects/*/zones/*/clusters/*`.  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpgradeInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.ClusterUpgradeInfo)` |   
  
### fetchClusterUpgradeInfoCallable()
    
    
    public final UnaryCallable<FetchClusterUpgradeInfoRequest,ClusterUpgradeInfo> fetchClusterUpgradeInfoCallable()

Fetch upgrade information of a specific cluster.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ClusterManagerClient clusterManagerClient = ClusterManagerClient.create()) {
       FetchClusterUpgradeInfoRequest request =
           FetchClusterUpgradeInfoRequest.newBuilder()
               .setName("name3373707")
               .setVersion("version351608024")
               .build();
       ApiFuture<ClusterUpgradeInfo> future =
           clusterManagerClient.fetchClusterUpgradeInfoCallable().futureCall(request);
       // Do something.
       ClusterUpgradeInfo response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[FetchClusterUpgradeInfoRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.FetchClusterUpgradeInfoRequest),[ClusterUpgradeInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.ClusterUpgradeInfo)>` |   
  
### fetchNodePoolUpgradeInfo(FetchNodePoolUpgradeInfoRequest request)
    
    
    public final NodePoolUpgradeInfo fetchNodePoolUpgradeInfo(FetchNodePoolUpgradeInfoRequest request)

Fetch upgrade information of a specific node pool.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ClusterManagerClient clusterManagerClient = ClusterManagerClient.create()) {
       FetchNodePoolUpgradeInfoRequest request =
           FetchNodePoolUpgradeInfoRequest.newBuilder()
               .setName("name3373707")
               .setVersion("version351608024")
               .build();
       NodePoolUpgradeInfo response = clusterManagerClient.fetchNodePoolUpgradeInfo(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[FetchNodePoolUpgradeInfoRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.FetchNodePoolUpgradeInfoRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[NodePoolUpgradeInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.NodePoolUpgradeInfo)` |   
  
### fetchNodePoolUpgradeInfo(String name)
    
    
    public final NodePoolUpgradeInfo fetchNodePoolUpgradeInfo(String name)

Fetch upgrade information of a specific node pool.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ClusterManagerClient clusterManagerClient = ClusterManagerClient.create()) {
       String name = "name3373707";
       NodePoolUpgradeInfo response = clusterManagerClient.fetchNodePoolUpgradeInfo(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name (project, location, cluster, node pool) of the node pool to get. Specified in the format `projects/*/locations/*/clusters/*/nodePools/*` or `projects/*/zones/*/clusters/*/nodePools/*`.  
**Returns**  
---  
**Type** | **Description**  
`[NodePoolUpgradeInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.NodePoolUpgradeInfo)` |   
  
### fetchNodePoolUpgradeInfoCallable()
    
    
    public final UnaryCallable<FetchNodePoolUpgradeInfoRequest,NodePoolUpgradeInfo> fetchNodePoolUpgradeInfoCallable()

Fetch upgrade information of a specific node pool.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ClusterManagerClient clusterManagerClient = ClusterManagerClient.create()) {
       FetchNodePoolUpgradeInfoRequest request =
           FetchNodePoolUpgradeInfoRequest.newBuilder()
               .setName("name3373707")
               .setVersion("version351608024")
               .build();
       ApiFuture<NodePoolUpgradeInfo> future =
           clusterManagerClient.fetchNodePoolUpgradeInfoCallable().futureCall(request);
       // Do something.
       NodePoolUpgradeInfo response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[FetchNodePoolUpgradeInfoRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.FetchNodePoolUpgradeInfoRequest),[NodePoolUpgradeInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.NodePoolUpgradeInfo)>` |   
  
### getCluster(GetClusterRequest request)
    
    
    public final Cluster getCluster(GetClusterRequest request)

Gets the details of a specific cluster.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ClusterManagerClient clusterManagerClient = ClusterManagerClient.create()) {
       GetClusterRequest request =
           GetClusterRequest.newBuilder()
               .setProjectId("projectId-894832108")
               .setZone("zone3744684")
               .setClusterId("clusterId561939637")
               .setName("name3373707")
               .build();
       Cluster response = clusterManagerClient.getCluster(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.GetClusterRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Cluster](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.Cluster)` |   
  
### getCluster(String name)
    
    
    public final Cluster getCluster(String name)

Gets the details of a specific cluster.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ClusterManagerClient clusterManagerClient = ClusterManagerClient.create()) {
       String name = "name3373707";
       Cluster response = clusterManagerClient.getCluster(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name (project, location, cluster) of the cluster to retrieve. Specified in the format `projects/*/locations/*/clusters/*`.  
**Returns**  
---  
**Type** | **Description**  
`[Cluster](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.Cluster)` |   
  
### getCluster(String projectId, String zone, String clusterId)
    
    
    public final Cluster getCluster(String projectId, String zone, String clusterId)

Gets the details of a specific cluster.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ClusterManagerClient clusterManagerClient = ClusterManagerClient.create()) {
       String projectId = "projectId-894832108";
       String zone = "zone3744684";
       String clusterId = "clusterId561939637";
       Cluster response = clusterManagerClient.getCluster(projectId, zone, clusterId);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Deprecated. The Google Developers Console [project ID or project number](https://cloud.google.com/resource-manager/docs/creating-managing-projects). This field has been deprecated and replaced by the name field.  
`zone` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Deprecated. The name of the Google Compute Engine [zone](https://cloud.google.com/compute/docs/zones#available) in which the cluster resides. This field has been deprecated and replaced by the name field.  
`clusterId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Deprecated. The name of the cluster to retrieve. This field has been deprecated and replaced by the name field.  
**Returns**  
---  
**Type** | **Description**  
`[Cluster](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.Cluster)` |   
  
### getClusterCallable()
    
    
    public final UnaryCallable<GetClusterRequest,Cluster> getClusterCallable()

Gets the details of a specific cluster.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ClusterManagerClient clusterManagerClient = ClusterManagerClient.create()) {
       GetClusterRequest request =
           GetClusterRequest.newBuilder()
               .setProjectId("projectId-894832108")
               .setZone("zone3744684")
               .setClusterId("clusterId561939637")
               .setName("name3373707")
               .build();
       ApiFuture<Cluster> future = clusterManagerClient.getClusterCallable().futureCall(request);
       // Do something.
       Cluster response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.GetClusterRequest),[Cluster](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.Cluster)>` |   
  
### getJSONWebKeys(GetJSONWebKeysRequest request)
    
    
    public final GetJSONWebKeysResponse getJSONWebKeys(GetJSONWebKeysRequest request)

Gets the public component of the cluster signing keys in JSON Web Key format.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ClusterManagerClient clusterManagerClient = ClusterManagerClient.create()) {
       GetJSONWebKeysRequest request =
           GetJSONWebKeysRequest.newBuilder().setParent("parent-995424086").build();
       GetJSONWebKeysResponse response = clusterManagerClient.getJSONWebKeys(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetJSONWebKeysRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.GetJSONWebKeysRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[GetJSONWebKeysResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.GetJSONWebKeysResponse)` |   
  
### getJSONWebKeysCallable()
    
    
    public final UnaryCallable<GetJSONWebKeysRequest,GetJSONWebKeysResponse> getJSONWebKeysCallable()

Gets the public component of the cluster signing keys in JSON Web Key format.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ClusterManagerClient clusterManagerClient = ClusterManagerClient.create()) {
       GetJSONWebKeysRequest request =
           GetJSONWebKeysRequest.newBuilder().setParent("parent-995424086").build();
       ApiFuture<GetJSONWebKeysResponse> future =
           clusterManagerClient.getJSONWebKeysCallable().futureCall(request);
       // Do something.
       GetJSONWebKeysResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetJSONWebKeysRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.GetJSONWebKeysRequest),[GetJSONWebKeysResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.GetJSONWebKeysResponse)>` |   
  
### getNodePool(GetNodePoolRequest request)
    
    
    public final NodePool getNodePool(GetNodePoolRequest request)

Retrieves the requested node pool.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ClusterManagerClient clusterManagerClient = ClusterManagerClient.create()) {
       GetNodePoolRequest request =
           GetNodePoolRequest.newBuilder()
               .setProjectId("projectId-894832108")
               .setZone("zone3744684")
               .setClusterId("clusterId561939637")
               .setNodePoolId("nodePoolId1121557241")
               .setName("name3373707")
               .build();
       NodePool response = clusterManagerClient.getNodePool(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetNodePoolRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.GetNodePoolRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[NodePool](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.NodePool)` |   
  
### getNodePool(String name)
    
    
    public final NodePool getNodePool(String name)

Retrieves the requested node pool.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ClusterManagerClient clusterManagerClient = ClusterManagerClient.create()) {
       String name = "name3373707";
       NodePool response = clusterManagerClient.getNodePool(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name (project, location, cluster, node pool id) of the node pool to get. Specified in the format `projects/*/locations/*/clusters/*/nodePools/*`.  
**Returns**  
---  
**Type** | **Description**  
`[NodePool](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.NodePool)` |   
  
### getNodePool(String projectId, String zone, String clusterId, String nodePoolId)
    
    
    public final NodePool getNodePool(String projectId, String zone, String clusterId, String nodePoolId)

Retrieves the requested node pool.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ClusterManagerClient clusterManagerClient = ClusterManagerClient.create()) {
       String projectId = "projectId-894832108";
       String zone = "zone3744684";
       String clusterId = "clusterId561939637";
       String nodePoolId = "nodePoolId1121557241";
       NodePool response = clusterManagerClient.getNodePool(projectId, zone, clusterId, nodePoolId);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Deprecated. The Google Developers Console [project ID or project number](https://cloud.google.com/resource-manager/docs/creating-managing-projects). This field has been deprecated and replaced by the name field.  
`zone` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Deprecated. The name of the Google Compute Engine [zone](https://cloud.google.com/compute/docs/zones#available) in which the cluster resides. This field has been deprecated and replaced by the name field.  
`clusterId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Deprecated. The name of the cluster. This field has been deprecated and replaced by the name field.  
`nodePoolId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Deprecated. The name of the node pool. This field has been deprecated and replaced by the name field.  
**Returns**  
---  
**Type** | **Description**  
`[NodePool](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.NodePool)` |   
  
### getNodePoolCallable()
    
    
    public final UnaryCallable<GetNodePoolRequest,NodePool> getNodePoolCallable()

Retrieves the requested node pool.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ClusterManagerClient clusterManagerClient = ClusterManagerClient.create()) {
       GetNodePoolRequest request =
           GetNodePoolRequest.newBuilder()
               .setProjectId("projectId-894832108")
               .setZone("zone3744684")
               .setClusterId("clusterId561939637")
               .setNodePoolId("nodePoolId1121557241")
               .setName("name3373707")
               .build();
       ApiFuture<NodePool> future = clusterManagerClient.getNodePoolCallable().futureCall(request);
       // Do something.
       NodePool response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetNodePoolRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.GetNodePoolRequest),[NodePool](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.NodePool)>` |   
  
### getOperation(GetOperationRequest request)
    
    
    public final Operation getOperation(GetOperationRequest request)

Gets the specified operation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ClusterManagerClient clusterManagerClient = ClusterManagerClient.create()) {
       GetOperationRequest request =
           GetOperationRequest.newBuilder()
               .setProjectId("projectId-894832108")
               .setZone("zone3744684")
               .setOperationId("operationId129704162")
               .setName("name3373707")
               .build();
       Operation response = clusterManagerClient.getOperation(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetOperationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.GetOperationRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.Operation)` |   
  
### getOperation(String name)
    
    
    public final Operation getOperation(String name)

Gets the specified operation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ClusterManagerClient clusterManagerClient = ClusterManagerClient.create()) {
       String name = "name3373707";
       Operation response = clusterManagerClient.getOperation(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name (project, location, operation id) of the operation to get. Specified in the format `projects/*/locations/*/operations/*`.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.Operation)` |   
  
### getOperation(String projectId, String zone, String operationId)
    
    
    public final Operation getOperation(String projectId, String zone, String operationId)

Gets the specified operation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ClusterManagerClient clusterManagerClient = ClusterManagerClient.create()) {
       String projectId = "projectId-894832108";
       String zone = "zone3744684";
       String operationId = "operationId129704162";
       Operation response = clusterManagerClient.getOperation(projectId, zone, operationId);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Deprecated. The Google Developers Console [project ID or project number](https://cloud.google.com/resource-manager/docs/creating-managing-projects). This field has been deprecated and replaced by the name field.  
`zone` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Deprecated. The name of the Google Compute Engine [zone](https://cloud.google.com/compute/docs/zones#available) in which the cluster resides. This field has been deprecated and replaced by the name field.  
`operationId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Deprecated. The server-assigned `name` of the operation. This field has been deprecated and replaced by the name field.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.Operation)` |   
  
### getOperationCallable()
    
    
    public final UnaryCallable<GetOperationRequest,Operation> getOperationCallable()

Gets the specified operation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ClusterManagerClient clusterManagerClient = ClusterManagerClient.create()) {
       GetOperationRequest request =
           GetOperationRequest.newBuilder()
               .setProjectId("projectId-894832108")
               .setZone("zone3744684")
               .setOperationId("operationId129704162")
               .setName("name3373707")
               .build();
       ApiFuture<Operation> future = clusterManagerClient.getOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetOperationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.GetOperationRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.Operation)>` |   
  
### getServerConfig(GetServerConfigRequest request)
    
    
    public final ServerConfig getServerConfig(GetServerConfigRequest request)

Returns configuration info about the Google Kubernetes Engine service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ClusterManagerClient clusterManagerClient = ClusterManagerClient.create()) {
       GetServerConfigRequest request =
           GetServerConfigRequest.newBuilder()
               .setProjectId("projectId-894832108")
               .setZone("zone3744684")
               .setName("name3373707")
               .build();
       ServerConfig response = clusterManagerClient.getServerConfig(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetServerConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.GetServerConfigRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ServerConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.ServerConfig)` |   
  
### getServerConfig(String name)
    
    
    public final ServerConfig getServerConfig(String name)

Returns configuration info about the Google Kubernetes Engine service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ClusterManagerClient clusterManagerClient = ClusterManagerClient.create()) {
       String name = "name3373707";
       ServerConfig response = clusterManagerClient.getServerConfig(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name (project and location) of the server config to get, specified in the format `projects/*/locations/*`.  
**Returns**  
---  
**Type** | **Description**  
`[ServerConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.ServerConfig)` |   
  
### getServerConfig(String projectId, String zone)
    
    
    public final ServerConfig getServerConfig(String projectId, String zone)

Returns configuration info about the Google Kubernetes Engine service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ClusterManagerClient clusterManagerClient = ClusterManagerClient.create()) {
       String projectId = "projectId-894832108";
       String zone = "zone3744684";
       ServerConfig response = clusterManagerClient.getServerConfig(projectId, zone);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Deprecated. The Google Developers Console [project ID or project number](https://cloud.google.com/resource-manager/docs/creating-managing-projects). This field has been deprecated and replaced by the name field.  
`zone` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Deprecated. The name of the Google Compute Engine [zone](https://cloud.google.com/compute/docs/zones#available) to return operations for. This field has been deprecated and replaced by the name field.  
**Returns**  
---  
**Type** | **Description**  
`[ServerConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.ServerConfig)` |   
  
### getServerConfigCallable()
    
    
    public final UnaryCallable<GetServerConfigRequest,ServerConfig> getServerConfigCallable()

Returns configuration info about the Google Kubernetes Engine service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ClusterManagerClient clusterManagerClient = ClusterManagerClient.create()) {
       GetServerConfigRequest request =
           GetServerConfigRequest.newBuilder()
               .setProjectId("projectId-894832108")
               .setZone("zone3744684")
               .setName("name3373707")
               .build();
       ApiFuture<ServerConfig> future =
           clusterManagerClient.getServerConfigCallable().futureCall(request);
       // Do something.
       ServerConfig response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetServerConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.GetServerConfigRequest),[ServerConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.ServerConfig)>` |   
  
### getSettings()
    
    
    public final @Nullable ClusterManagerSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.container.v1.ClusterManagerSettings` |   
  
### getStub()
    
    
    public ClusterManagerStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[ClusterManagerStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.cloud.container.v1.stub.ClusterManagerStub)` |   
  
### isShutdown()
    
    
    public boolean isShutdown()

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### isTerminated()
    
    
    public boolean isTerminated()

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### listClusters(ListClustersRequest request)
    
    
    public final ListClustersResponse listClusters(ListClustersRequest request)

Lists all clusters owned by a project in either the specified zone or all zones.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ClusterManagerClient clusterManagerClient = ClusterManagerClient.create()) {
       ListClustersRequest request =
           ListClustersRequest.newBuilder()
               .setProjectId("projectId-894832108")
               .setZone("zone3744684")
               .setParent("parent-995424086")
               .build();
       ListClustersResponse response = clusterManagerClient.listClusters(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListClustersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.ListClustersRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ListClustersResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.ListClustersResponse)` |   
  
### listClusters(String parent)
    
    
    public final ListClustersResponse listClusters(String parent)

Lists all clusters owned by a project in either the specified zone or all zones.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ClusterManagerClient clusterManagerClient = ClusterManagerClient.create()) {
       String parent = "parent-995424086";
       ListClustersResponse response = clusterManagerClient.listClusters(parent);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The parent (project and location) where the clusters will be listed. Specified in the format `projects/*/locations/*`. Location "-" matches all zones and all regions.  
**Returns**  
---  
**Type** | **Description**  
`[ListClustersResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.ListClustersResponse)` |   
  
### listClusters(String projectId, String zone)
    
    
    public final ListClustersResponse listClusters(String projectId, String zone)

Lists all clusters owned by a project in either the specified zone or all zones.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ClusterManagerClient clusterManagerClient = ClusterManagerClient.create()) {
       String projectId = "projectId-894832108";
       String zone = "zone3744684";
       ListClustersResponse response = clusterManagerClient.listClusters(projectId, zone);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Deprecated. The Google Developers Console [project ID or project number](https://cloud.google.com/resource-manager/docs/creating-managing-projects). This field has been deprecated and replaced by the parent field.  
`zone` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Deprecated. The name of the Google Compute Engine [zone](https://cloud.google.com/compute/docs/zones#available) in which the cluster resides, or "-" for all zones. This field has been deprecated and replaced by the parent field.  
**Returns**  
---  
**Type** | **Description**  
`[ListClustersResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.ListClustersResponse)` |   
  
### listClustersCallable()
    
    
    public final UnaryCallable<ListClustersRequest,ListClustersResponse> listClustersCallable()

Lists all clusters owned by a project in either the specified zone or all zones.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ClusterManagerClient clusterManagerClient = ClusterManagerClient.create()) {
       ListClustersRequest request =
           ListClustersRequest.newBuilder()
               .setProjectId("projectId-894832108")
               .setZone("zone3744684")
               .setParent("parent-995424086")
               .build();
       ApiFuture<ListClustersResponse> future =
           clusterManagerClient.listClustersCallable().futureCall(request);
       // Do something.
       ListClustersResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListClustersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.ListClustersRequest),[ListClustersResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.ListClustersResponse)>` |   
  
### listNodePools(ListNodePoolsRequest request)
    
    
    public final ListNodePoolsResponse listNodePools(ListNodePoolsRequest request)

Lists the node pools for a cluster.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ClusterManagerClient clusterManagerClient = ClusterManagerClient.create()) {
       ListNodePoolsRequest request =
           ListNodePoolsRequest.newBuilder()
               .setProjectId("projectId-894832108")
               .setZone("zone3744684")
               .setClusterId("clusterId561939637")
               .setParent("parent-995424086")
               .build();
       ListNodePoolsResponse response = clusterManagerClient.listNodePools(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListNodePoolsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.ListNodePoolsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ListNodePoolsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.ListNodePoolsResponse)` |   
  
### listNodePools(String parent)
    
    
    public final ListNodePoolsResponse listNodePools(String parent)

Lists the node pools for a cluster.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ClusterManagerClient clusterManagerClient = ClusterManagerClient.create()) {
       String parent = "parent-995424086";
       ListNodePoolsResponse response = clusterManagerClient.listNodePools(parent);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The parent (project, location, cluster name) where the node pools will be listed. Specified in the format `projects/*/locations/*/clusters/*`.  
**Returns**  
---  
**Type** | **Description**  
`[ListNodePoolsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.ListNodePoolsResponse)` |   
  
### listNodePools(String projectId, String zone, String clusterId)
    
    
    public final ListNodePoolsResponse listNodePools(String projectId, String zone, String clusterId)

Lists the node pools for a cluster.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ClusterManagerClient clusterManagerClient = ClusterManagerClient.create()) {
       String projectId = "projectId-894832108";
       String zone = "zone3744684";
       String clusterId = "clusterId561939637";
       ListNodePoolsResponse response =
           clusterManagerClient.listNodePools(projectId, zone, clusterId);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Deprecated. The Google Developers Console [project ID or project number](https://cloud.google.com/resource-manager/docs/creating-managing-projects). This field has been deprecated and replaced by the parent field.  
`zone` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Deprecated. The name of the Google Compute Engine [zone](https://cloud.google.com/compute/docs/zones#available) in which the cluster resides. This field has been deprecated and replaced by the parent field.  
`clusterId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Deprecated. The name of the cluster. This field has been deprecated and replaced by the parent field.  
**Returns**  
---  
**Type** | **Description**  
`[ListNodePoolsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.ListNodePoolsResponse)` |   
  
### listNodePoolsCallable()
    
    
    public final UnaryCallable<ListNodePoolsRequest,ListNodePoolsResponse> listNodePoolsCallable()

Lists the node pools for a cluster.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ClusterManagerClient clusterManagerClient = ClusterManagerClient.create()) {
       ListNodePoolsRequest request =
           ListNodePoolsRequest.newBuilder()
               .setProjectId("projectId-894832108")
               .setZone("zone3744684")
               .setClusterId("clusterId561939637")
               .setParent("parent-995424086")
               .build();
       ApiFuture<ListNodePoolsResponse> future =
           clusterManagerClient.listNodePoolsCallable().futureCall(request);
       // Do something.
       ListNodePoolsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListNodePoolsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.ListNodePoolsRequest),[ListNodePoolsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.ListNodePoolsResponse)>` |   
  
### listOperations(ListOperationsRequest request)
    
    
    public final ListOperationsResponse listOperations(ListOperationsRequest request)

Lists all operations in a project in a specific zone or all zones.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ClusterManagerClient clusterManagerClient = ClusterManagerClient.create()) {
       ListOperationsRequest request =
           ListOperationsRequest.newBuilder()
               .setProjectId("projectId-894832108")
               .setZone("zone3744684")
               .setParent("parent-995424086")
               .build();
       ListOperationsResponse response = clusterManagerClient.listOperations(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListOperationsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.ListOperationsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ListOperationsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.ListOperationsResponse)` |   
  
### listOperations(String parent)
    
    
    public final ListOperationsResponse listOperations(String parent)

Lists all operations in a project in a specific zone or all zones.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ClusterManagerClient clusterManagerClient = ClusterManagerClient.create()) {
       String parent = "parent-995424086";
       ListOperationsResponse response = clusterManagerClient.listOperations(parent);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The parent (project and location) where the operations will be listed. Specified in the format `projects/*/locations/*`. Location "-" matches all zones and all regions.  
**Returns**  
---  
**Type** | **Description**  
`[ListOperationsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.ListOperationsResponse)` |   
  
### listOperations(String projectId, String zone)
    
    
    public final ListOperationsResponse listOperations(String projectId, String zone)

Lists all operations in a project in a specific zone or all zones.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ClusterManagerClient clusterManagerClient = ClusterManagerClient.create()) {
       String projectId = "projectId-894832108";
       String zone = "zone3744684";
       ListOperationsResponse response = clusterManagerClient.listOperations(projectId, zone);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Deprecated. The Google Developers Console [project ID or project number](https://cloud.google.com/resource-manager/docs/creating-managing-projects). This field has been deprecated and replaced by the parent field.  
`zone` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Deprecated. The name of the Google Compute Engine [zone](https://cloud.google.com/compute/docs/zones#available) to return operations for, or `-` for all zones. This field has been deprecated and replaced by the parent field.  
**Returns**  
---  
**Type** | **Description**  
`[ListOperationsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.ListOperationsResponse)` |   
  
### listOperationsCallable()
    
    
    public final UnaryCallable<ListOperationsRequest,ListOperationsResponse> listOperationsCallable()

Lists all operations in a project in a specific zone or all zones.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ClusterManagerClient clusterManagerClient = ClusterManagerClient.create()) {
       ListOperationsRequest request =
           ListOperationsRequest.newBuilder()
               .setProjectId("projectId-894832108")
               .setZone("zone3744684")
               .setParent("parent-995424086")
               .build();
       ApiFuture<ListOperationsResponse> future =
           clusterManagerClient.listOperationsCallable().futureCall(request);
       // Do something.
       ListOperationsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListOperationsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.ListOperationsRequest),[ListOperationsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.ListOperationsResponse)>` |   
  
### listUsableSubnetworks(ListUsableSubnetworksRequest request)
    
    
    public final ClusterManagerClient.ListUsableSubnetworksPagedResponse listUsableSubnetworks(ListUsableSubnetworksRequest request)

Lists subnetworks that are usable for creating clusters in a project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ClusterManagerClient clusterManagerClient = ClusterManagerClient.create()) {
       ListUsableSubnetworksRequest request =
           ListUsableSubnetworksRequest.newBuilder()
               .setParent("parent-995424086")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (UsableSubnetwork element :
           clusterManagerClient.listUsableSubnetworks(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListUsableSubnetworksRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.ListUsableSubnetworksRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ClusterManagerClient.ListUsableSubnetworksPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.cloud.container.v1.ClusterManagerClient.ListUsableSubnetworksPagedResponse)` |   
  
### listUsableSubnetworksCallable()
    
    
    public final UnaryCallable<ListUsableSubnetworksRequest,ListUsableSubnetworksResponse> listUsableSubnetworksCallable()

Lists subnetworks that are usable for creating clusters in a project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ClusterManagerClient clusterManagerClient = ClusterManagerClient.create()) {
       ListUsableSubnetworksRequest request =
           ListUsableSubnetworksRequest.newBuilder()
               .setParent("parent-995424086")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListUsableSubnetworksResponse response =
             clusterManagerClient.listUsableSubnetworksCallable().call(request);
         for (UsableSubnetwork element : response.getSubnetworksList()) {
           // doThingsWith(element);
         }
         String nextPageToken = response.getNextPageToken();
         if (!Strings.isNullOrEmpty(nextPageToken)) {
           request = request.toBuilder().setPageToken(nextPageToken).build();
         } else {
           break;
         }
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListUsableSubnetworksRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.ListUsableSubnetworksRequest),[ListUsableSubnetworksResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.ListUsableSubnetworksResponse)>` |   
  
### listUsableSubnetworksPagedCallable()
    
    
    public final UnaryCallable<ListUsableSubnetworksRequest,ClusterManagerClient.ListUsableSubnetworksPagedResponse> listUsableSubnetworksPagedCallable()

Lists subnetworks that are usable for creating clusters in a project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ClusterManagerClient clusterManagerClient = ClusterManagerClient.create()) {
       ListUsableSubnetworksRequest request =
           ListUsableSubnetworksRequest.newBuilder()
               .setParent("parent-995424086")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<UsableSubnetwork> future =
           clusterManagerClient.listUsableSubnetworksPagedCallable().futureCall(request);
       // Do something.
       for (UsableSubnetwork element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListUsableSubnetworksRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.ListUsableSubnetworksRequest),[ListUsableSubnetworksPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.cloud.container.v1.ClusterManagerClient.ListUsableSubnetworksPagedResponse)>` |   
  
### rollbackNodePoolUpgrade(RollbackNodePoolUpgradeRequest request)
    
    
    public final Operation rollbackNodePoolUpgrade(RollbackNodePoolUpgradeRequest request)

Rolls back a previously Aborted or Failed NodePool upgrade. This makes no changes if the last upgrade successfully completed.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ClusterManagerClient clusterManagerClient = ClusterManagerClient.create()) {
       RollbackNodePoolUpgradeRequest request =
           RollbackNodePoolUpgradeRequest.newBuilder()
               .setProjectId("projectId-894832108")
               .setZone("zone3744684")
               .setClusterId("clusterId561939637")
               .setNodePoolId("nodePoolId1121557241")
               .setName("name3373707")
               .setRespectPdb(true)
               .build();
       Operation response = clusterManagerClient.rollbackNodePoolUpgrade(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[RollbackNodePoolUpgradeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.RollbackNodePoolUpgradeRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.Operation)` |   
  
### rollbackNodePoolUpgrade(String name)
    
    
    public final Operation rollbackNodePoolUpgrade(String name)

Rolls back a previously Aborted or Failed NodePool upgrade. This makes no changes if the last upgrade successfully completed.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ClusterManagerClient clusterManagerClient = ClusterManagerClient.create()) {
       String name = "name3373707";
       Operation response = clusterManagerClient.rollbackNodePoolUpgrade(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name (project, location, cluster, node pool id) of the node poll to rollback upgrade. Specified in the format `projects/*/locations/*/clusters/*/nodePools/*`.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.Operation)` |   
  
### rollbackNodePoolUpgrade(String projectId, String zone, String clusterId, String nodePoolId)
    
    
    public final Operation rollbackNodePoolUpgrade(String projectId, String zone, String clusterId, String nodePoolId)

Rolls back a previously Aborted or Failed NodePool upgrade. This makes no changes if the last upgrade successfully completed.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ClusterManagerClient clusterManagerClient = ClusterManagerClient.create()) {
       String projectId = "projectId-894832108";
       String zone = "zone3744684";
       String clusterId = "clusterId561939637";
       String nodePoolId = "nodePoolId1121557241";
       Operation response =
           clusterManagerClient.rollbackNodePoolUpgrade(projectId, zone, clusterId, nodePoolId);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Deprecated. The Google Developers Console [project ID or project number](https://cloud.google.com/resource-manager/docs/creating-managing-projects). This field has been deprecated and replaced by the name field.  
`zone` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Deprecated. The name of the Google Compute Engine [zone](https://cloud.google.com/compute/docs/zones#available) in which the cluster resides. This field has been deprecated and replaced by the name field.  
`clusterId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Deprecated. The name of the cluster to rollback. This field has been deprecated and replaced by the name field.  
`nodePoolId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Deprecated. The name of the node pool to rollback. This field has been deprecated and replaced by the name field.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.Operation)` |   
  
### rollbackNodePoolUpgradeCallable()
    
    
    public final UnaryCallable<RollbackNodePoolUpgradeRequest,Operation> rollbackNodePoolUpgradeCallable()

Rolls back a previously Aborted or Failed NodePool upgrade. This makes no changes if the last upgrade successfully completed.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ClusterManagerClient clusterManagerClient = ClusterManagerClient.create()) {
       RollbackNodePoolUpgradeRequest request =
           RollbackNodePoolUpgradeRequest.newBuilder()
               .setProjectId("projectId-894832108")
               .setZone("zone3744684")
               .setClusterId("clusterId561939637")
               .setNodePoolId("nodePoolId1121557241")
               .setName("name3373707")
               .setRespectPdb(true)
               .build();
       ApiFuture<Operation> future =
           clusterManagerClient.rollbackNodePoolUpgradeCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[RollbackNodePoolUpgradeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.RollbackNodePoolUpgradeRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.Operation)>` |   
  
### setAddonsConfig(SetAddonsConfigRequest request)
    
    
    public final Operation setAddonsConfig(SetAddonsConfigRequest request)

Sets the addons for a specific cluster.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ClusterManagerClient clusterManagerClient = ClusterManagerClient.create()) {
       SetAddonsConfigRequest request =
           SetAddonsConfigRequest.newBuilder()
               .setProjectId("projectId-894832108")
               .setZone("zone3744684")
               .setClusterId("clusterId561939637")
               .setAddonsConfig(AddonsConfig.newBuilder().build())
               .setName("name3373707")
               .build();
       Operation response = clusterManagerClient.setAddonsConfig(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SetAddonsConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.SetAddonsConfigRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.Operation)` |   
  
### setAddonsConfig(String name, AddonsConfig addonsConfig)
    
    
    public final Operation setAddonsConfig(String name, AddonsConfig addonsConfig)

Sets the addons for a specific cluster.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ClusterManagerClient clusterManagerClient = ClusterManagerClient.create()) {
       String name = "name3373707";
       AddonsConfig addonsConfig = AddonsConfig.newBuilder().build();
       Operation response = clusterManagerClient.setAddonsConfig(name, addonsConfig);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name (project, location, cluster) of the cluster to set addons. Specified in the format `projects/*/locations/*/clusters/*`.  
`addonsConfig` | `[AddonsConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.AddonsConfig)`  
Required. The desired configurations for the various addons available to run in the cluster.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.Operation)` |   
  
### setAddonsConfig(String projectId, String zone, String clusterId, AddonsConfig addonsConfig)
    
    
    public final Operation setAddonsConfig(String projectId, String zone, String clusterId, AddonsConfig addonsConfig)

Sets the addons for a specific cluster.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ClusterManagerClient clusterManagerClient = ClusterManagerClient.create()) {
       String projectId = "projectId-894832108";
       String zone = "zone3744684";
       String clusterId = "clusterId561939637";
       AddonsConfig addonsConfig = AddonsConfig.newBuilder().build();
       Operation response =
           clusterManagerClient.setAddonsConfig(projectId, zone, clusterId, addonsConfig);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Deprecated. The Google Developers Console [project ID or project number](https://cloud.google.com/resource-manager/docs/creating-managing-projects). This field has been deprecated and replaced by the name field.  
`zone` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Deprecated. The name of the Google Compute Engine [zone](https://cloud.google.com/compute/docs/zones#available) in which the cluster resides. This field has been deprecated and replaced by the name field.  
`clusterId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Deprecated. The name of the cluster to upgrade. This field has been deprecated and replaced by the name field.  
`addonsConfig` | `[AddonsConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.AddonsConfig)`  
Required. The desired configurations for the various addons available to run in the cluster.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.Operation)` |   
  
### setAddonsConfigCallable()
    
    
    public final UnaryCallable<SetAddonsConfigRequest,Operation> setAddonsConfigCallable()

Sets the addons for a specific cluster.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ClusterManagerClient clusterManagerClient = ClusterManagerClient.create()) {
       SetAddonsConfigRequest request =
           SetAddonsConfigRequest.newBuilder()
               .setProjectId("projectId-894832108")
               .setZone("zone3744684")
               .setClusterId("clusterId561939637")
               .setAddonsConfig(AddonsConfig.newBuilder().build())
               .setName("name3373707")
               .build();
       ApiFuture<Operation> future =
           clusterManagerClient.setAddonsConfigCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SetAddonsConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.SetAddonsConfigRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.Operation)>` |   
  
### setLabels(SetLabelsRequest request)
    
    
    public final Operation setLabels(SetLabelsRequest request)

Sets labels on a cluster.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ClusterManagerClient clusterManagerClient = ClusterManagerClient.create()) {
       SetLabelsRequest request =
           SetLabelsRequest.newBuilder()
               .setProjectId("projectId-894832108")
               .setZone("zone3744684")
               .setClusterId("clusterId561939637")
               .putAllResourceLabels(new HashMap<String, String>())
               .setLabelFingerprint("labelFingerprint379449680")
               .setName("name3373707")
               .build();
       Operation response = clusterManagerClient.setLabels(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SetLabelsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.SetLabelsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.Operation)` |   
  
### setLabelsCallable()
    
    
    public final UnaryCallable<SetLabelsRequest,Operation> setLabelsCallable()

Sets labels on a cluster.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ClusterManagerClient clusterManagerClient = ClusterManagerClient.create()) {
       SetLabelsRequest request =
           SetLabelsRequest.newBuilder()
               .setProjectId("projectId-894832108")
               .setZone("zone3744684")
               .setClusterId("clusterId561939637")
               .putAllResourceLabels(new HashMap<String, String>())
               .setLabelFingerprint("labelFingerprint379449680")
               .setName("name3373707")
               .build();
       ApiFuture<Operation> future = clusterManagerClient.setLabelsCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SetLabelsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.SetLabelsRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.Operation)>` |   
  
### setLegacyAbac(SetLegacyAbacRequest request)
    
    
    public final Operation setLegacyAbac(SetLegacyAbacRequest request)

Enables or disables the ABAC authorization mechanism on a cluster.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ClusterManagerClient clusterManagerClient = ClusterManagerClient.create()) {
       SetLegacyAbacRequest request =
           SetLegacyAbacRequest.newBuilder()
               .setProjectId("projectId-894832108")
               .setZone("zone3744684")
               .setClusterId("clusterId561939637")
               .setEnabled(true)
               .setName("name3373707")
               .build();
       Operation response = clusterManagerClient.setLegacyAbac(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SetLegacyAbacRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.SetLegacyAbacRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.Operation)` |   
  
### setLegacyAbac(String name, boolean enabled)
    
    
    public final Operation setLegacyAbac(String name, boolean enabled)

Enables or disables the ABAC authorization mechanism on a cluster.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ClusterManagerClient clusterManagerClient = ClusterManagerClient.create()) {
       String name = "name3373707";
       boolean enabled = true;
       Operation response = clusterManagerClient.setLegacyAbac(name, enabled);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name (project, location, cluster name) of the cluster to set legacy abac. Specified in the format `projects/*/locations/*/clusters/*`.  
`enabled` | `[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
Required. Whether ABAC authorization will be enabled in the cluster.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.Operation)` |   
  
### setLegacyAbac(String projectId, String zone, String clusterId, boolean enabled)
    
    
    public final Operation setLegacyAbac(String projectId, String zone, String clusterId, boolean enabled)

Enables or disables the ABAC authorization mechanism on a cluster.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ClusterManagerClient clusterManagerClient = ClusterManagerClient.create()) {
       String projectId = "projectId-894832108";
       String zone = "zone3744684";
       String clusterId = "clusterId561939637";
       boolean enabled = true;
       Operation response = clusterManagerClient.setLegacyAbac(projectId, zone, clusterId, enabled);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Deprecated. The Google Developers Console [project ID or project number](https://cloud.google.com/resource-manager/docs/creating-managing-projects). This field has been deprecated and replaced by the name field.  
`zone` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Deprecated. The name of the Google Compute Engine [zone](https://cloud.google.com/compute/docs/zones#available) in which the cluster resides. This field has been deprecated and replaced by the name field.  
`clusterId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Deprecated. The name of the cluster to update. This field has been deprecated and replaced by the name field.  
`enabled` | `[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
Required. Whether ABAC authorization will be enabled in the cluster.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.Operation)` |   
  
### setLegacyAbacCallable()
    
    
    public final UnaryCallable<SetLegacyAbacRequest,Operation> setLegacyAbacCallable()

Enables or disables the ABAC authorization mechanism on a cluster.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ClusterManagerClient clusterManagerClient = ClusterManagerClient.create()) {
       SetLegacyAbacRequest request =
           SetLegacyAbacRequest.newBuilder()
               .setProjectId("projectId-894832108")
               .setZone("zone3744684")
               .setClusterId("clusterId561939637")
               .setEnabled(true)
               .setName("name3373707")
               .build();
       ApiFuture<Operation> future =
           clusterManagerClient.setLegacyAbacCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SetLegacyAbacRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.SetLegacyAbacRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.Operation)>` |   
  
### setLocations(SetLocationsRequest request) (deprecated)
    
    
    public final Operation setLocations(SetLocationsRequest request)

**Deprecated.** _This method is deprecated and will be removed in the next major version update._

Sets the locations for a specific cluster. Deprecated. Use [projects.locations.clusters.update](https://cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters/update) instead.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ClusterManagerClient clusterManagerClient = ClusterManagerClient.create()) {
       SetLocationsRequest request =
           SetLocationsRequest.newBuilder()
               .setProjectId("projectId-894832108")
               .setZone("zone3744684")
               .setClusterId("clusterId561939637")
               .addAllLocations(new ArrayList<String>())
               .setName("name3373707")
               .build();
       Operation response = clusterManagerClient.setLocations(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SetLocationsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.SetLocationsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.Operation)` |   
  
### setLocations(String projectId, String zone, String clusterId, List<String> locations) (deprecated)
    
    
    public final Operation setLocations(String projectId, String zone, String clusterId, List<String> locations)

**Deprecated.** _This method is deprecated and will be removed in the next major version update._

Sets the locations for a specific cluster. Deprecated. Use [projects.locations.clusters.update](https://cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters/update) instead.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ClusterManagerClient clusterManagerClient = ClusterManagerClient.create()) {
       String projectId = "projectId-894832108";
       String zone = "zone3744684";
       String clusterId = "clusterId561939637";
       List<String> locations = new ArrayList<>();
       Operation response = clusterManagerClient.setLocations(projectId, zone, clusterId, locations);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Deprecated. The Google Developers Console [project ID or project number](https://cloud.google.com/resource-manager/docs/creating-managing-projects). This field has been deprecated and replaced by the name field.  
`zone` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Deprecated. The name of the Google Compute Engine [zone](https://cloud.google.com/compute/docs/zones#available) in which the cluster resides. This field has been deprecated and replaced by the name field.  
`clusterId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Deprecated. The name of the cluster to upgrade. This field has been deprecated and replaced by the name field.  
`locations` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
Required. The desired list of Google Compute Engine [zones](https://cloud.google.com/compute/docs/zones#available) in which the cluster's nodes should be located. Changing the locations a cluster is in will result in nodes being either created or removed from the cluster, depending on whether locations are being added or removed. This list must always include the cluster's primary zone.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.Operation)` |   
  
### setLocations(String name, List<String> locations) (deprecated)
    
    
    public final Operation setLocations(String name, List<String> locations)

**Deprecated.** _This method is deprecated and will be removed in the next major version update._

Sets the locations for a specific cluster. Deprecated. Use [projects.locations.clusters.update](https://cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters/update) instead.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ClusterManagerClient clusterManagerClient = ClusterManagerClient.create()) {
       String name = "name3373707";
       List<String> locations = new ArrayList<>();
       Operation response = clusterManagerClient.setLocations(name, locations);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name (project, location, cluster) of the cluster to set locations. Specified in the format `projects/*/locations/*/clusters/*`.  
`locations` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
Required. The desired list of Google Compute Engine [zones](https://cloud.google.com/compute/docs/zones#available) in which the cluster's nodes should be located. Changing the locations a cluster is in will result in nodes being either created or removed from the cluster, depending on whether locations are being added or removed. This list must always include the cluster's primary zone.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.Operation)` |   
  
### setLocationsCallable() (deprecated)
    
    
    public final UnaryCallable<SetLocationsRequest,Operation> setLocationsCallable()

**Deprecated.** _This method is deprecated and will be removed in the next major version update._

Sets the locations for a specific cluster. Deprecated. Use [projects.locations.clusters.update](https://cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters/update) instead.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ClusterManagerClient clusterManagerClient = ClusterManagerClient.create()) {
       SetLocationsRequest request =
           SetLocationsRequest.newBuilder()
               .setProjectId("projectId-894832108")
               .setZone("zone3744684")
               .setClusterId("clusterId561939637")
               .addAllLocations(new ArrayList<String>())
               .setName("name3373707")
               .build();
       ApiFuture<Operation> future = clusterManagerClient.setLocationsCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SetLocationsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.SetLocationsRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.Operation)>` |   
  
### setLoggingService(SetLoggingServiceRequest request)
    
    
    public final Operation setLoggingService(SetLoggingServiceRequest request)

Sets the logging service for a specific cluster.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ClusterManagerClient clusterManagerClient = ClusterManagerClient.create()) {
       SetLoggingServiceRequest request =
           SetLoggingServiceRequest.newBuilder()
               .setProjectId("projectId-894832108")
               .setZone("zone3744684")
               .setClusterId("clusterId561939637")
               .setLoggingService("loggingService1098570326")
               .setName("name3373707")
               .build();
       Operation response = clusterManagerClient.setLoggingService(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SetLoggingServiceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.SetLoggingServiceRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.Operation)` |   
  
### setLoggingService(String name, String loggingService)
    
    
    public final Operation setLoggingService(String name, String loggingService)

Sets the logging service for a specific cluster.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ClusterManagerClient clusterManagerClient = ClusterManagerClient.create()) {
       String name = "name3373707";
       String loggingService = "loggingService1098570326";
       Operation response = clusterManagerClient.setLoggingService(name, loggingService);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name (project, location, cluster) of the cluster to set logging. Specified in the format `projects/*/locations/*/clusters/*`.  
`loggingService` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The logging service the cluster should use to write logs. Currently available options: 

  * `logging.googleapis.com/kubernetes` \- The Cloud Logging service with a Kubernetes-native resource model 
  * `logging.googleapis.com` \- The legacy Cloud Logging service (no longer available as of GKE 1.15). 
  * `none` \- no logs will be exported from the cluster. 

If left as an empty string,`logging.googleapis.com/kubernetes` will be used for GKE 1.14+ or `logging.googleapis.com` for earlier versions.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.Operation)` |   
  
### setLoggingService(String projectId, String zone, String clusterId, String loggingService)
    
    
    public final Operation setLoggingService(String projectId, String zone, String clusterId, String loggingService)

Sets the logging service for a specific cluster.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ClusterManagerClient clusterManagerClient = ClusterManagerClient.create()) {
       String projectId = "projectId-894832108";
       String zone = "zone3744684";
       String clusterId = "clusterId561939637";
       String loggingService = "loggingService1098570326";
       Operation response =
           clusterManagerClient.setLoggingService(projectId, zone, clusterId, loggingService);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Deprecated. The Google Developers Console [project ID or project number](https://cloud.google.com/resource-manager/docs/creating-managing-projects). This field has been deprecated and replaced by the name field.  
`zone` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Deprecated. The name of the Google Compute Engine [zone](https://cloud.google.com/compute/docs/zones#available) in which the cluster resides. This field has been deprecated and replaced by the name field.  
`clusterId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Deprecated. The name of the cluster to upgrade. This field has been deprecated and replaced by the name field.  
`loggingService` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The logging service the cluster should use to write logs. Currently available options: 

  * `logging.googleapis.com/kubernetes` \- The Cloud Logging service with a Kubernetes-native resource model 
  * `logging.googleapis.com` \- The legacy Cloud Logging service (no longer available as of GKE 1.15). 
  * `none` \- no logs will be exported from the cluster. 

If left as an empty string,`logging.googleapis.com/kubernetes` will be used for GKE 1.14+ or `logging.googleapis.com` for earlier versions.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.Operation)` |   
  
### setLoggingServiceCallable()
    
    
    public final UnaryCallable<SetLoggingServiceRequest,Operation> setLoggingServiceCallable()

Sets the logging service for a specific cluster.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ClusterManagerClient clusterManagerClient = ClusterManagerClient.create()) {
       SetLoggingServiceRequest request =
           SetLoggingServiceRequest.newBuilder()
               .setProjectId("projectId-894832108")
               .setZone("zone3744684")
               .setClusterId("clusterId561939637")
               .setLoggingService("loggingService1098570326")
               .setName("name3373707")
               .build();
       ApiFuture<Operation> future =
           clusterManagerClient.setLoggingServiceCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SetLoggingServiceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.SetLoggingServiceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.Operation)>` |   
  
### setMaintenancePolicy(SetMaintenancePolicyRequest request)
    
    
    public final Operation setMaintenancePolicy(SetMaintenancePolicyRequest request)

Sets the maintenance policy for a cluster.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ClusterManagerClient clusterManagerClient = ClusterManagerClient.create()) {
       SetMaintenancePolicyRequest request =
           SetMaintenancePolicyRequest.newBuilder()
               .setProjectId("projectId-894832108")
               .setZone("zone3744684")
               .setClusterId("clusterId561939637")
               .setMaintenancePolicy(MaintenancePolicy.newBuilder().build())
               .setName("name3373707")
               .build();
       Operation response = clusterManagerClient.setMaintenancePolicy(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SetMaintenancePolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.SetMaintenancePolicyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.Operation)` |   
  
### setMaintenancePolicy(String name, MaintenancePolicy maintenancePolicy)
    
    
    public final Operation setMaintenancePolicy(String name, MaintenancePolicy maintenancePolicy)

Sets the maintenance policy for a cluster.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ClusterManagerClient clusterManagerClient = ClusterManagerClient.create()) {
       String name = "name3373707";
       MaintenancePolicy maintenancePolicy = MaintenancePolicy.newBuilder().build();
       Operation response = clusterManagerClient.setMaintenancePolicy(name, maintenancePolicy);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name (project, location, cluster name) of the cluster to set maintenance policy. Specified in the format `projects/*/locations/*/clusters/*`.  
`maintenancePolicy` | `[MaintenancePolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.MaintenancePolicy)`  
Required. The maintenance policy to be set for the cluster. An empty field clears the existing maintenance policy.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.Operation)` |   
  
### setMaintenancePolicy(String projectId, String zone, String clusterId, MaintenancePolicy maintenancePolicy)
    
    
    public final Operation setMaintenancePolicy(String projectId, String zone, String clusterId, MaintenancePolicy maintenancePolicy)

Sets the maintenance policy for a cluster.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ClusterManagerClient clusterManagerClient = ClusterManagerClient.create()) {
       String projectId = "projectId-894832108";
       String zone = "zone3744684";
       String clusterId = "clusterId561939637";
       MaintenancePolicy maintenancePolicy = MaintenancePolicy.newBuilder().build();
       Operation response =
           clusterManagerClient.setMaintenancePolicy(projectId, zone, clusterId, maintenancePolicy);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The Google Developers Console [project ID or project number](https://cloud.google.com/resource-manager/docs/creating-managing-projects).  
`zone` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the Google Compute Engine [zone](https://cloud.google.com/compute/docs/zones#available) in which the cluster resides.  
`clusterId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the cluster to update.  
`maintenancePolicy` | `[MaintenancePolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.MaintenancePolicy)`  
Required. The maintenance policy to be set for the cluster. An empty field clears the existing maintenance policy.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.Operation)` |   
  
### setMaintenancePolicyCallable()
    
    
    public final UnaryCallable<SetMaintenancePolicyRequest,Operation> setMaintenancePolicyCallable()

Sets the maintenance policy for a cluster.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ClusterManagerClient clusterManagerClient = ClusterManagerClient.create()) {
       SetMaintenancePolicyRequest request =
           SetMaintenancePolicyRequest.newBuilder()
               .setProjectId("projectId-894832108")
               .setZone("zone3744684")
               .setClusterId("clusterId561939637")
               .setMaintenancePolicy(MaintenancePolicy.newBuilder().build())
               .setName("name3373707")
               .build();
       ApiFuture<Operation> future =
           clusterManagerClient.setMaintenancePolicyCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SetMaintenancePolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.SetMaintenancePolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.Operation)>` |   
  
### setMasterAuth(SetMasterAuthRequest request)
    
    
    public final Operation setMasterAuth(SetMasterAuthRequest request)

Sets master auth materials. Currently supports changing the admin password or a specific cluster, either via password generation or explicitly setting the password.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ClusterManagerClient clusterManagerClient = ClusterManagerClient.create()) {
       SetMasterAuthRequest request =
           SetMasterAuthRequest.newBuilder()
               .setProjectId("projectId-894832108")
               .setZone("zone3744684")
               .setClusterId("clusterId561939637")
               .setUpdate(MasterAuth.newBuilder().build())
               .setName("name3373707")
               .build();
       Operation response = clusterManagerClient.setMasterAuth(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SetMasterAuthRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.SetMasterAuthRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.Operation)` |   
  
### setMasterAuthCallable()
    
    
    public final UnaryCallable<SetMasterAuthRequest,Operation> setMasterAuthCallable()

Sets master auth materials. Currently supports changing the admin password or a specific cluster, either via password generation or explicitly setting the password.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ClusterManagerClient clusterManagerClient = ClusterManagerClient.create()) {
       SetMasterAuthRequest request =
           SetMasterAuthRequest.newBuilder()
               .setProjectId("projectId-894832108")
               .setZone("zone3744684")
               .setClusterId("clusterId561939637")
               .setUpdate(MasterAuth.newBuilder().build())
               .setName("name3373707")
               .build();
       ApiFuture<Operation> future =
           clusterManagerClient.setMasterAuthCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SetMasterAuthRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.SetMasterAuthRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.Operation)>` |   
  
### setMonitoringService(SetMonitoringServiceRequest request)
    
    
    public final Operation setMonitoringService(SetMonitoringServiceRequest request)

Sets the monitoring service for a specific cluster.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ClusterManagerClient clusterManagerClient = ClusterManagerClient.create()) {
       SetMonitoringServiceRequest request =
           SetMonitoringServiceRequest.newBuilder()
               .setProjectId("projectId-894832108")
               .setZone("zone3744684")
               .setClusterId("clusterId561939637")
               .setMonitoringService("monitoringService-1431578291")
               .setName("name3373707")
               .build();
       Operation response = clusterManagerClient.setMonitoringService(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SetMonitoringServiceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.SetMonitoringServiceRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.Operation)` |   
  
### setMonitoringService(String name, String monitoringService)
    
    
    public final Operation setMonitoringService(String name, String monitoringService)

Sets the monitoring service for a specific cluster.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ClusterManagerClient clusterManagerClient = ClusterManagerClient.create()) {
       String name = "name3373707";
       String monitoringService = "monitoringService-1431578291";
       Operation response = clusterManagerClient.setMonitoringService(name, monitoringService);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name (project, location, cluster) of the cluster to set monitoring. Specified in the format `projects/*/locations/*/clusters/*`.  
`monitoringService` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The monitoring service the cluster should use to write metrics. Currently available options: 

  * `monitoring.googleapis.com/kubernetes` \- The Cloud Monitoring service with a Kubernetes-native resource model 
  * `monitoring.googleapis.com` \- The legacy Cloud Monitoring service (no longer available as of GKE 1.15). 
  * `none` \- No metrics will be exported from the cluster. 

If left as an empty string,`monitoring.googleapis.com/kubernetes` will be used for GKE 1.14+ or `monitoring.googleapis.com` for earlier versions.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.Operation)` |   
  
### setMonitoringService(String projectId, String zone, String clusterId, String monitoringService)
    
    
    public final Operation setMonitoringService(String projectId, String zone, String clusterId, String monitoringService)

Sets the monitoring service for a specific cluster.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ClusterManagerClient clusterManagerClient = ClusterManagerClient.create()) {
       String projectId = "projectId-894832108";
       String zone = "zone3744684";
       String clusterId = "clusterId561939637";
       String monitoringService = "monitoringService-1431578291";
       Operation response =
           clusterManagerClient.setMonitoringService(projectId, zone, clusterId, monitoringService);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Deprecated. The Google Developers Console [project ID or project number](https://cloud.google.com/resource-manager/docs/creating-managing-projects). This field has been deprecated and replaced by the name field.  
`zone` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Deprecated. The name of the Google Compute Engine [zone](https://cloud.google.com/compute/docs/zones#available) in which the cluster resides. This field has been deprecated and replaced by the name field.  
`clusterId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Deprecated. The name of the cluster to upgrade. This field has been deprecated and replaced by the name field.  
`monitoringService` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The monitoring service the cluster should use to write metrics. Currently available options: 

  * `monitoring.googleapis.com/kubernetes` \- The Cloud Monitoring service with a Kubernetes-native resource model 
  * `monitoring.googleapis.com` \- The legacy Cloud Monitoring service (no longer available as of GKE 1.15). 
  * `none` \- No metrics will be exported from the cluster. 

If left as an empty string,`monitoring.googleapis.com/kubernetes` will be used for GKE 1.14+ or `monitoring.googleapis.com` for earlier versions.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.Operation)` |   
  
### setMonitoringServiceCallable()
    
    
    public final UnaryCallable<SetMonitoringServiceRequest,Operation> setMonitoringServiceCallable()

Sets the monitoring service for a specific cluster.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ClusterManagerClient clusterManagerClient = ClusterManagerClient.create()) {
       SetMonitoringServiceRequest request =
           SetMonitoringServiceRequest.newBuilder()
               .setProjectId("projectId-894832108")
               .setZone("zone3744684")
               .setClusterId("clusterId561939637")
               .setMonitoringService("monitoringService-1431578291")
               .setName("name3373707")
               .build();
       ApiFuture<Operation> future =
           clusterManagerClient.setMonitoringServiceCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SetMonitoringServiceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.SetMonitoringServiceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.Operation)>` |   
  
### setNetworkPolicy(SetNetworkPolicyRequest request)
    
    
    public final Operation setNetworkPolicy(SetNetworkPolicyRequest request)

Enables or disables Network Policy for a cluster.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ClusterManagerClient clusterManagerClient = ClusterManagerClient.create()) {
       SetNetworkPolicyRequest request =
           SetNetworkPolicyRequest.newBuilder()
               .setProjectId("projectId-894832108")
               .setZone("zone3744684")
               .setClusterId("clusterId561939637")
               .setNetworkPolicy(NetworkPolicy.newBuilder().build())
               .setName("name3373707")
               .build();
       Operation response = clusterManagerClient.setNetworkPolicy(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SetNetworkPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.SetNetworkPolicyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.Operation)` |   
  
### setNetworkPolicy(String name, NetworkPolicy networkPolicy)
    
    
    public final Operation setNetworkPolicy(String name, NetworkPolicy networkPolicy)

Enables or disables Network Policy for a cluster.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ClusterManagerClient clusterManagerClient = ClusterManagerClient.create()) {
       String name = "name3373707";
       NetworkPolicy networkPolicy = NetworkPolicy.newBuilder().build();
       Operation response = clusterManagerClient.setNetworkPolicy(name, networkPolicy);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name (project, location, cluster name) of the cluster to set networking policy. Specified in the format `projects/*/locations/*/clusters/*`.  
`networkPolicy` | `[NetworkPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.NetworkPolicy)`  
Required. Configuration options for the NetworkPolicy feature.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.Operation)` |   
  
### setNetworkPolicy(String projectId, String zone, String clusterId, NetworkPolicy networkPolicy)
    
    
    public final Operation setNetworkPolicy(String projectId, String zone, String clusterId, NetworkPolicy networkPolicy)

Enables or disables Network Policy for a cluster.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ClusterManagerClient clusterManagerClient = ClusterManagerClient.create()) {
       String projectId = "projectId-894832108";
       String zone = "zone3744684";
       String clusterId = "clusterId561939637";
       NetworkPolicy networkPolicy = NetworkPolicy.newBuilder().build();
       Operation response =
           clusterManagerClient.setNetworkPolicy(projectId, zone, clusterId, networkPolicy);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Deprecated. The Google Developers Console [project ID or project number](https://cloud.google.com/resource-manager/docs/creating-managing-projects). This field has been deprecated and replaced by the name field.  
`zone` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Deprecated. The name of the Google Compute Engine [zone](https://cloud.google.com/compute/docs/zones#available) in which the cluster resides. This field has been deprecated and replaced by the name field.  
`clusterId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Deprecated. The name of the cluster. This field has been deprecated and replaced by the name field.  
`networkPolicy` | `[NetworkPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.NetworkPolicy)`  
Required. Configuration options for the NetworkPolicy feature.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.Operation)` |   
  
### setNetworkPolicyCallable()
    
    
    public final UnaryCallable<SetNetworkPolicyRequest,Operation> setNetworkPolicyCallable()

Enables or disables Network Policy for a cluster.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ClusterManagerClient clusterManagerClient = ClusterManagerClient.create()) {
       SetNetworkPolicyRequest request =
           SetNetworkPolicyRequest.newBuilder()
               .setProjectId("projectId-894832108")
               .setZone("zone3744684")
               .setClusterId("clusterId561939637")
               .setNetworkPolicy(NetworkPolicy.newBuilder().build())
               .setName("name3373707")
               .build();
       ApiFuture<Operation> future =
           clusterManagerClient.setNetworkPolicyCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SetNetworkPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.SetNetworkPolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.Operation)>` |   
  
### setNodePoolAutoscaling(SetNodePoolAutoscalingRequest request)
    
    
    public final Operation setNodePoolAutoscaling(SetNodePoolAutoscalingRequest request)

Sets the autoscaling settings for the specified node pool.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ClusterManagerClient clusterManagerClient = ClusterManagerClient.create()) {
       SetNodePoolAutoscalingRequest request =
           SetNodePoolAutoscalingRequest.newBuilder()
               .setProjectId("projectId-894832108")
               .setZone("zone3744684")
               .setClusterId("clusterId561939637")
               .setNodePoolId("nodePoolId1121557241")
               .setAutoscaling(NodePoolAutoscaling.newBuilder().build())
               .setName("name3373707")
               .build();
       Operation response = clusterManagerClient.setNodePoolAutoscaling(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SetNodePoolAutoscalingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.SetNodePoolAutoscalingRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.Operation)` |   
  
### setNodePoolAutoscalingCallable()
    
    
    public final UnaryCallable<SetNodePoolAutoscalingRequest,Operation> setNodePoolAutoscalingCallable()

Sets the autoscaling settings for the specified node pool.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ClusterManagerClient clusterManagerClient = ClusterManagerClient.create()) {
       SetNodePoolAutoscalingRequest request =
           SetNodePoolAutoscalingRequest.newBuilder()
               .setProjectId("projectId-894832108")
               .setZone("zone3744684")
               .setClusterId("clusterId561939637")
               .setNodePoolId("nodePoolId1121557241")
               .setAutoscaling(NodePoolAutoscaling.newBuilder().build())
               .setName("name3373707")
               .build();
       ApiFuture<Operation> future =
           clusterManagerClient.setNodePoolAutoscalingCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SetNodePoolAutoscalingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.SetNodePoolAutoscalingRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.Operation)>` |   
  
### setNodePoolManagement(SetNodePoolManagementRequest request)
    
    
    public final Operation setNodePoolManagement(SetNodePoolManagementRequest request)

Sets the NodeManagement options for a node pool.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ClusterManagerClient clusterManagerClient = ClusterManagerClient.create()) {
       SetNodePoolManagementRequest request =
           SetNodePoolManagementRequest.newBuilder()
               .setProjectId("projectId-894832108")
               .setZone("zone3744684")
               .setClusterId("clusterId561939637")
               .setNodePoolId("nodePoolId1121557241")
               .setManagement(NodeManagement.newBuilder().build())
               .setName("name3373707")
               .build();
       Operation response = clusterManagerClient.setNodePoolManagement(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SetNodePoolManagementRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.SetNodePoolManagementRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.Operation)` |   
  
### setNodePoolManagementCallable()
    
    
    public final UnaryCallable<SetNodePoolManagementRequest,Operation> setNodePoolManagementCallable()

Sets the NodeManagement options for a node pool.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ClusterManagerClient clusterManagerClient = ClusterManagerClient.create()) {
       SetNodePoolManagementRequest request =
           SetNodePoolManagementRequest.newBuilder()
               .setProjectId("projectId-894832108")
               .setZone("zone3744684")
               .setClusterId("clusterId561939637")
               .setNodePoolId("nodePoolId1121557241")
               .setManagement(NodeManagement.newBuilder().build())
               .setName("name3373707")
               .build();
       ApiFuture<Operation> future =
           clusterManagerClient.setNodePoolManagementCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SetNodePoolManagementRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.SetNodePoolManagementRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.Operation)>` |   
  
### setNodePoolSize(SetNodePoolSizeRequest request)
    
    
    public final Operation setNodePoolSize(SetNodePoolSizeRequest request)

Sets the size for a specific node pool. The new size will be used for all replicas, including future replicas created by modifying NodePool.locations.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ClusterManagerClient clusterManagerClient = ClusterManagerClient.create()) {
       SetNodePoolSizeRequest request =
           SetNodePoolSizeRequest.newBuilder()
               .setProjectId("projectId-894832108")
               .setZone("zone3744684")
               .setClusterId("clusterId561939637")
               .setNodePoolId("nodePoolId1121557241")
               .setNodeCount(1539922066)
               .setName("name3373707")
               .build();
       Operation response = clusterManagerClient.setNodePoolSize(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SetNodePoolSizeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.SetNodePoolSizeRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.Operation)` |   
  
### setNodePoolSizeCallable()
    
    
    public final UnaryCallable<SetNodePoolSizeRequest,Operation> setNodePoolSizeCallable()

Sets the size for a specific node pool. The new size will be used for all replicas, including future replicas created by modifying NodePool.locations.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ClusterManagerClient clusterManagerClient = ClusterManagerClient.create()) {
       SetNodePoolSizeRequest request =
           SetNodePoolSizeRequest.newBuilder()
               .setProjectId("projectId-894832108")
               .setZone("zone3744684")
               .setClusterId("clusterId561939637")
               .setNodePoolId("nodePoolId1121557241")
               .setNodeCount(1539922066)
               .setName("name3373707")
               .build();
       ApiFuture<Operation> future =
           clusterManagerClient.setNodePoolSizeCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SetNodePoolSizeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.SetNodePoolSizeRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.Operation)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### startIPRotation(StartIPRotationRequest request)
    
    
    public final Operation startIPRotation(StartIPRotationRequest request)

Starts master IP rotation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ClusterManagerClient clusterManagerClient = ClusterManagerClient.create()) {
       StartIPRotationRequest request =
           StartIPRotationRequest.newBuilder()
               .setProjectId("projectId-894832108")
               .setZone("zone3744684")
               .setClusterId("clusterId561939637")
               .setName("name3373707")
               .setRotateCredentials(true)
               .build();
       Operation response = clusterManagerClient.startIPRotation(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[StartIPRotationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.StartIPRotationRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.Operation)` |   
  
### startIPRotation(String name)
    
    
    public final Operation startIPRotation(String name)

Starts master IP rotation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ClusterManagerClient clusterManagerClient = ClusterManagerClient.create()) {
       String name = "name3373707";
       Operation response = clusterManagerClient.startIPRotation(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name (project, location, cluster name) of the cluster to start IP rotation. Specified in the format `projects/*/locations/*/clusters/*`.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.Operation)` |   
  
### startIPRotation(String projectId, String zone, String clusterId)
    
    
    public final Operation startIPRotation(String projectId, String zone, String clusterId)

Starts master IP rotation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ClusterManagerClient clusterManagerClient = ClusterManagerClient.create()) {
       String projectId = "projectId-894832108";
       String zone = "zone3744684";
       String clusterId = "clusterId561939637";
       Operation response = clusterManagerClient.startIPRotation(projectId, zone, clusterId);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Deprecated. The Google Developers Console [project ID or project number](https://cloud.google.com/resource-manager/docs/creating-managing-projects). This field has been deprecated and replaced by the name field.  
`zone` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Deprecated. The name of the Google Compute Engine [zone](https://cloud.google.com/compute/docs/zones#available) in which the cluster resides. This field has been deprecated and replaced by the name field.  
`clusterId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Deprecated. The name of the cluster. This field has been deprecated and replaced by the name field.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.Operation)` |   
  
### startIPRotationCallable()
    
    
    public final UnaryCallable<StartIPRotationRequest,Operation> startIPRotationCallable()

Starts master IP rotation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ClusterManagerClient clusterManagerClient = ClusterManagerClient.create()) {
       StartIPRotationRequest request =
           StartIPRotationRequest.newBuilder()
               .setProjectId("projectId-894832108")
               .setZone("zone3744684")
               .setClusterId("clusterId561939637")
               .setName("name3373707")
               .setRotateCredentials(true)
               .build();
       ApiFuture<Operation> future =
           clusterManagerClient.startIPRotationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[StartIPRotationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.StartIPRotationRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.Operation)>` |   
  
### updateCluster(UpdateClusterRequest request)
    
    
    public final Operation updateCluster(UpdateClusterRequest request)

Updates the settings of a specific cluster.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ClusterManagerClient clusterManagerClient = ClusterManagerClient.create()) {
       UpdateClusterRequest request =
           UpdateClusterRequest.newBuilder()
               .setProjectId("projectId-894832108")
               .setZone("zone3744684")
               .setClusterId("clusterId561939637")
               .setUpdate(ClusterUpdate.newBuilder().build())
               .setName("name3373707")
               .build();
       Operation response = clusterManagerClient.updateCluster(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.UpdateClusterRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.Operation)` |   
  
### updateCluster(String name, ClusterUpdate update)
    
    
    public final Operation updateCluster(String name, ClusterUpdate update)

Updates the settings of a specific cluster.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ClusterManagerClient clusterManagerClient = ClusterManagerClient.create()) {
       String name = "name3373707";
       ClusterUpdate update = ClusterUpdate.newBuilder().build();
       Operation response = clusterManagerClient.updateCluster(name, update);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name (project, location, cluster) of the cluster to update. Specified in the format `projects/*/locations/*/clusters/*`.  
`update` | `[ClusterUpdate](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.ClusterUpdate)`  
Required. A description of the update.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.Operation)` |   
  
### updateCluster(String projectId, String zone, String clusterId, ClusterUpdate update)
    
    
    public final Operation updateCluster(String projectId, String zone, String clusterId, ClusterUpdate update)

Updates the settings of a specific cluster.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ClusterManagerClient clusterManagerClient = ClusterManagerClient.create()) {
       String projectId = "projectId-894832108";
       String zone = "zone3744684";
       String clusterId = "clusterId561939637";
       ClusterUpdate update = ClusterUpdate.newBuilder().build();
       Operation response = clusterManagerClient.updateCluster(projectId, zone, clusterId, update);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Deprecated. The Google Developers Console [project ID or project number](https://cloud.google.com/resource-manager/docs/creating-managing-projects). This field has been deprecated and replaced by the name field.  
`zone` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Deprecated. The name of the Google Compute Engine [zone](https://cloud.google.com/compute/docs/zones#available) in which the cluster resides. This field has been deprecated and replaced by the name field.  
`clusterId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Deprecated. The name of the cluster to upgrade. This field has been deprecated and replaced by the name field.  
`update` | `[ClusterUpdate](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.ClusterUpdate)`  
Required. A description of the update.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.Operation)` |   
  
### updateClusterCallable()
    
    
    public final UnaryCallable<UpdateClusterRequest,Operation> updateClusterCallable()

Updates the settings of a specific cluster.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ClusterManagerClient clusterManagerClient = ClusterManagerClient.create()) {
       UpdateClusterRequest request =
           UpdateClusterRequest.newBuilder()
               .setProjectId("projectId-894832108")
               .setZone("zone3744684")
               .setClusterId("clusterId561939637")
               .setUpdate(ClusterUpdate.newBuilder().build())
               .setName("name3373707")
               .build();
       ApiFuture<Operation> future =
           clusterManagerClient.updateClusterCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.UpdateClusterRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.Operation)>` |   
  
### updateMaster(UpdateMasterRequest request)
    
    
    public final Operation updateMaster(UpdateMasterRequest request)

Updates the master for a specific cluster.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ClusterManagerClient clusterManagerClient = ClusterManagerClient.create()) {
       UpdateMasterRequest request =
           UpdateMasterRequest.newBuilder()
               .setProjectId("projectId-894832108")
               .setZone("zone3744684")
               .setClusterId("clusterId561939637")
               .setMasterVersion("masterVersion1167095830")
               .setName("name3373707")
               .build();
       Operation response = clusterManagerClient.updateMaster(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateMasterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.UpdateMasterRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.Operation)` |   
  
### updateMaster(String name, String masterVersion)
    
    
    public final Operation updateMaster(String name, String masterVersion)

Updates the master for a specific cluster.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ClusterManagerClient clusterManagerClient = ClusterManagerClient.create()) {
       String name = "name3373707";
       String masterVersion = "masterVersion1167095830";
       Operation response = clusterManagerClient.updateMaster(name, masterVersion);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name (project, location, cluster) of the cluster to update. Specified in the format `projects/*/locations/*/clusters/*`.  
`masterVersion` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The Kubernetes version to change the master to. Users may specify either explicit versions offered by Kubernetes Engine or version aliases, which have the following behavior: \- "latest": picks the highest valid Kubernetes version - "1.X": picks the highest valid patch+gke.N patch in the 1.X version - "1.X.Y": picks the highest valid gke.N patch in the 1.X.Y version - "1.X.Y-gke.N": picks an explicit Kubernetes version - "-": picks the default Kubernetes version  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.Operation)` |   
  
### updateMaster(String projectId, String zone, String clusterId, String masterVersion)
    
    
    public final Operation updateMaster(String projectId, String zone, String clusterId, String masterVersion)

Updates the master for a specific cluster.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ClusterManagerClient clusterManagerClient = ClusterManagerClient.create()) {
       String projectId = "projectId-894832108";
       String zone = "zone3744684";
       String clusterId = "clusterId561939637";
       String masterVersion = "masterVersion1167095830";
       Operation response =
           clusterManagerClient.updateMaster(projectId, zone, clusterId, masterVersion);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Deprecated. The Google Developers Console [project ID or project number](https://cloud.google.com/resource-manager/docs/creating-managing-projects). This field has been deprecated and replaced by the name field.  
`zone` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Deprecated. The name of the Google Compute Engine [zone](https://cloud.google.com/compute/docs/zones#available) in which the cluster resides. This field has been deprecated and replaced by the name field.  
`clusterId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Deprecated. The name of the cluster to upgrade. This field has been deprecated and replaced by the name field.  
`masterVersion` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The Kubernetes version to change the master to. Users may specify either explicit versions offered by Kubernetes Engine or version aliases, which have the following behavior: \- "latest": picks the highest valid Kubernetes version - "1.X": picks the highest valid patch+gke.N patch in the 1.X version - "1.X.Y": picks the highest valid gke.N patch in the 1.X.Y version - "1.X.Y-gke.N": picks an explicit Kubernetes version - "-": picks the default Kubernetes version  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.Operation)` |   
  
### updateMasterCallable()
    
    
    public final UnaryCallable<UpdateMasterRequest,Operation> updateMasterCallable()

Updates the master for a specific cluster.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ClusterManagerClient clusterManagerClient = ClusterManagerClient.create()) {
       UpdateMasterRequest request =
           UpdateMasterRequest.newBuilder()
               .setProjectId("projectId-894832108")
               .setZone("zone3744684")
               .setClusterId("clusterId561939637")
               .setMasterVersion("masterVersion1167095830")
               .setName("name3373707")
               .build();
       ApiFuture<Operation> future = clusterManagerClient.updateMasterCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateMasterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.UpdateMasterRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.Operation)>` |   
  
### updateNodePool(UpdateNodePoolRequest request)
    
    
    public final Operation updateNodePool(UpdateNodePoolRequest request)

Updates the version and/or image type for the specified node pool.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ClusterManagerClient clusterManagerClient = ClusterManagerClient.create()) {
       UpdateNodePoolRequest request =
           UpdateNodePoolRequest.newBuilder()
               .setProjectId("projectId-894832108")
               .setZone("zone3744684")
               .setClusterId("clusterId561939637")
               .setNodePoolId("nodePoolId1121557241")
               .setNodeVersion("nodeVersion1155309686")
               .setImageType("imageType-878147787")
               .setName("name3373707")
               .setImage("image100313435")
               .setImageProject("imageProject288951614")
               .addAllLocations(new ArrayList<String>())
               .setWorkloadMetadataConfig(WorkloadMetadataConfig.newBuilder().build())
               .setUpgradeSettings(NodePool.UpgradeSettings.newBuilder().build())
               .setTags(NetworkTags.newBuilder().build())
               .setTaints(NodeTaints.newBuilder().build())
               .setLabels(NodeLabels.newBuilder().build())
               .setLinuxNodeConfig(LinuxNodeConfig.newBuilder().build())
               .setKubeletConfig(NodeKubeletConfig.newBuilder().build())
               .setNodeNetworkConfig(NodeNetworkConfig.newBuilder().build())
               .setGcfsConfig(GcfsConfig.newBuilder().build())
               .setConfidentialNodes(ConfidentialNodes.newBuilder().build())
               .setGvnic(VirtualNIC.newBuilder().build())
               .setEtag("etag3123477")
               .setFastSocket(FastSocket.newBuilder().build())
               .setLoggingConfig(NodePoolLoggingConfig.newBuilder().build())
               .setResourceLabels(ResourceLabels.newBuilder().build())
               .setWindowsNodeConfig(WindowsNodeConfig.newBuilder().build())
               .addAllAccelerators(new ArrayList<AcceleratorConfig>())
               .setMachineType("machineType-218117087")
               .setDiskType("diskType279771767")
               .setDiskSizeGb(-757478089)
               .setResourceManagerTags(ResourceManagerTags.newBuilder().build())
               .setContainerdConfig(ContainerdConfig.newBuilder().build())
               .setQueuedProvisioning(NodePool.QueuedProvisioning.newBuilder().build())
               .addAllStoragePools(new ArrayList<String>())
               .setMaxRunDuration(Duration.newBuilder().build())
               .setFlexStart(true)
               .setBootDisk(BootDisk.newBuilder().build())
               .setNodeDrainConfig(NodePool.NodeDrainConfig.newBuilder().build())
               .setConsolidationDelay(Duration.newBuilder().build())
               .setTaintConfig(TaintConfig.newBuilder().build())
               .setMaintenancePolicy(NodePool.NodePoolMaintenancePolicy.newBuilder().build())
               .build();
       Operation response = clusterManagerClient.updateNodePool(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateNodePoolRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.UpdateNodePoolRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.Operation)` |   
  
### updateNodePoolCallable()
    
    
    public final UnaryCallable<UpdateNodePoolRequest,Operation> updateNodePoolCallable()

Updates the version and/or image type for the specified node pool.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ClusterManagerClient clusterManagerClient = ClusterManagerClient.create()) {
       UpdateNodePoolRequest request =
           UpdateNodePoolRequest.newBuilder()
               .setProjectId("projectId-894832108")
               .setZone("zone3744684")
               .setClusterId("clusterId561939637")
               .setNodePoolId("nodePoolId1121557241")
               .setNodeVersion("nodeVersion1155309686")
               .setImageType("imageType-878147787")
               .setName("name3373707")
               .setImage("image100313435")
               .setImageProject("imageProject288951614")
               .addAllLocations(new ArrayList<String>())
               .setWorkloadMetadataConfig(WorkloadMetadataConfig.newBuilder().build())
               .setUpgradeSettings(NodePool.UpgradeSettings.newBuilder().build())
               .setTags(NetworkTags.newBuilder().build())
               .setTaints(NodeTaints.newBuilder().build())
               .setLabels(NodeLabels.newBuilder().build())
               .setLinuxNodeConfig(LinuxNodeConfig.newBuilder().build())
               .setKubeletConfig(NodeKubeletConfig.newBuilder().build())
               .setNodeNetworkConfig(NodeNetworkConfig.newBuilder().build())
               .setGcfsConfig(GcfsConfig.newBuilder().build())
               .setConfidentialNodes(ConfidentialNodes.newBuilder().build())
               .setGvnic(VirtualNIC.newBuilder().build())
               .setEtag("etag3123477")
               .setFastSocket(FastSocket.newBuilder().build())
               .setLoggingConfig(NodePoolLoggingConfig.newBuilder().build())
               .setResourceLabels(ResourceLabels.newBuilder().build())
               .setWindowsNodeConfig(WindowsNodeConfig.newBuilder().build())
               .addAllAccelerators(new ArrayList<AcceleratorConfig>())
               .setMachineType("machineType-218117087")
               .setDiskType("diskType279771767")
               .setDiskSizeGb(-757478089)
               .setResourceManagerTags(ResourceManagerTags.newBuilder().build())
               .setContainerdConfig(ContainerdConfig.newBuilder().build())
               .setQueuedProvisioning(NodePool.QueuedProvisioning.newBuilder().build())
               .addAllStoragePools(new ArrayList<String>())
               .setMaxRunDuration(Duration.newBuilder().build())
               .setFlexStart(true)
               .setBootDisk(BootDisk.newBuilder().build())
               .setNodeDrainConfig(NodePool.NodeDrainConfig.newBuilder().build())
               .setConsolidationDelay(Duration.newBuilder().build())
               .setTaintConfig(TaintConfig.newBuilder().build())
               .setMaintenancePolicy(NodePool.NodePoolMaintenancePolicy.newBuilder().build())
               .build();
       ApiFuture<Operation> future =
           clusterManagerClient.updateNodePoolCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateNodePoolRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.UpdateNodePoolRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.Operation)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
