---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.VmwareEngineClient
title: Class VmwareEngineClient (0.93.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:47:57.485301+00:00
---

# Class VmwareEngineClient (0.93.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.VmwareEngineClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class VmwareEngineClient (0.93.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.93.0 (latest)  0.89.0  0.88.0  0.87.0  0.85.0  0.82.0  0.81.0  0.79.0  0.77.0  0.76.0  0.74.0  0.72.0  0.70.0  0.69.0  0.68.0  0.67.0  0.66.0  0.64.0  0.62.0  0.61.0  0.58.0  0.57.0  0.56.0  0.54.0  0.53.0  0.52.0  0.51.0  0.50.0  0.49.0  0.48.0  0.47.0  0.46.0  0.45.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.38.0  0.37.0  0.36.0  0.35.0  0.34.0  0.33.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.3.0  0.2.0  0.1.0 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-vmwareengine/google-cloud-vmwareengine/src/main/java/com/google/cloud/vmwareengine/v1/VmwareEngineClient.java)| [Product Reference](https://cloud.google.com/vmware-engine/)| [REST Documentation](https://cloud.google.com/vmware-engine/docs/reference/rest)  
---|---|---  
  
Service Description: VMwareEngine manages VMware's private clusters in the Cloud.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       PrivateCloudName name = PrivateCloudName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_CLOUD]");
       PrivateCloud response = vmwareEngineClient.getPrivateCloud(name);
     }
     

Note: close() needs to be called on the VmwareEngineClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
ListPrivateClouds |  Lists `PrivateCloud` resources in a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listPrivateClouds(ListPrivateCloudsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listPrivateClouds(LocationName parent) 
  * listPrivateClouds(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listPrivateCloudsPagedCallable() 
  * listPrivateCloudsCallable() 

  
GetPrivateCloud |  Retrieves a `PrivateCloud` resource by its resource name. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getPrivateCloud(GetPrivateCloudRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getPrivateCloud(PrivateCloudName name) 
  * getPrivateCloud(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getPrivateCloudCallable() 

  
CreatePrivateCloud |  Creates a new `PrivateCloud` resource in a given project and location. Private clouds of type `STANDARD` and `TIME_LIMITED` are zonal resources, `STRETCHED` private clouds are regional. Creating a private cloud also creates a [management cluster](https://cloud.google.com/vmware-engine/docs/concepts-vmware-components) for that private cloud. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createPrivateCloudAsync(CreatePrivateCloudRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * createPrivateCloudAsync(LocationName parent, PrivateCloud privateCloud, String privateCloudId) 
  * createPrivateCloudAsync(String parent, PrivateCloud privateCloud, String privateCloudId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createPrivateCloudOperationCallable() 
  * createPrivateCloudCallable() 

  
UpdatePrivateCloud |  Modifies a `PrivateCloud` resource. Only the following fields can be updated: `description`. Only fields specified in `updateMask` are applied.  During operation processing, the resource is temporarily in the `ACTIVE` state before the operation fully completes. For that period of time, you can't update the resource. Use the operation status to determine when the processing fully completes. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updatePrivateCloudAsync(UpdatePrivateCloudRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * updatePrivateCloudAsync(PrivateCloud privateCloud, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updatePrivateCloudOperationCallable() 
  * updatePrivateCloudCallable() 

  
DeletePrivateCloud |  Schedules a `PrivateCloud` resource for deletion.  A `PrivateCloud` resource scheduled for deletion has `PrivateCloud.state` set to `DELETED` and `expireTime` set to the time when deletion is final and can no longer be reversed. The delete operation is marked as done as soon as the `PrivateCloud` is successfully scheduled for deletion (this also applies when `delayHours` is set to zero), and the operation is not kept in pending state until `PrivateCloud` is purged. `PrivateCloud` can be restored using `UndeletePrivateCloud` method before the `expireTime` elapses. When `expireTime` is reached, deletion is final and all private cloud resources are irreversibly removed and billing stops. During the final removal process, `PrivateCloud.state` is set to `PURGING`. `PrivateCloud` can be polled using standard `GET` method for the whole period of deletion and purging. It will not be returned only when it is completely purged. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deletePrivateCloudAsync(DeletePrivateCloudRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deletePrivateCloudAsync(PrivateCloudName name) 
  * deletePrivateCloudAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deletePrivateCloudOperationCallable() 
  * deletePrivateCloudCallable() 

  
UndeletePrivateCloud |  Restores a private cloud that was previously scheduled for deletion by `DeletePrivateCloud`. A `PrivateCloud` resource scheduled for deletion has `PrivateCloud.state` set to `DELETED` and `PrivateCloud.expireTime` set to the time when deletion can no longer be reversed. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * undeletePrivateCloudAsync(UndeletePrivateCloudRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * undeletePrivateCloudAsync(PrivateCloudName name) 
  * undeletePrivateCloudAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * undeletePrivateCloudOperationCallable() 
  * undeletePrivateCloudCallable() 

  
ListClusters |  Lists `Cluster` resources in a given private cloud. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listClusters(ListClustersRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listClusters(PrivateCloudName parent) 
  * listClusters(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listClustersPagedCallable() 
  * listClustersCallable() 

  
GetCluster |  Retrieves a `Cluster` resource by its resource name. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getCluster(GetClusterRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getCluster(ClusterName name) 
  * getCluster(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getClusterCallable() 

  
CreateCluster |  Creates a new cluster in a given private cloud. Creating a new cluster provides additional nodes for use in the parent private cloud and requires sufficient [node quota](https://cloud.google.com/vmware-engine/quotas). |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createClusterAsync(CreateClusterRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * createClusterAsync(PrivateCloudName parent, Cluster cluster, String clusterId) 
  * createClusterAsync(String parent, Cluster cluster, String clusterId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createClusterOperationCallable() 
  * createClusterCallable() 

  
UpdateCluster |  Modifies a `Cluster` resource. Only fields specified in `updateMask` are applied.  During operation processing, the resource is temporarily in the `ACTIVE` state before the operation fully completes. For that period of time, you can't update the resource. Use the operation status to determine when the processing fully completes. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateClusterAsync(UpdateClusterRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * updateClusterAsync(Cluster cluster, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateClusterOperationCallable() 
  * updateClusterCallable() 

  
DeleteCluster |  Deletes a `Cluster` resource. To avoid unintended data loss, migrate or gracefully shut down any workloads running on the cluster before deletion. You cannot delete the management cluster of a private cloud using this method. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteClusterAsync(DeleteClusterRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteClusterAsync(ClusterName name) 
  * deleteClusterAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteClusterOperationCallable() 
  * deleteClusterCallable() 

  
ListNodes |  Lists nodes in a given cluster. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listNodes(ListNodesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listNodes(ClusterName parent) 
  * listNodes(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listNodesPagedCallable() 
  * listNodesCallable() 

  
GetNode |  Gets details of a single node. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getNode(GetNodeRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getNode(NodeName name) 
  * getNode(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getNodeCallable() 

  
ListExternalAddresses |  Lists external IP addresses assigned to VMware workload VMs in a given private cloud. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listExternalAddresses(ListExternalAddressesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listExternalAddresses(PrivateCloudName parent) 
  * listExternalAddresses(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listExternalAddressesPagedCallable() 
  * listExternalAddressesCallable() 

  
FetchNetworkPolicyExternalAddresses |  Lists external IP addresses assigned to VMware workload VMs within the scope of the given network policy. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * fetchNetworkPolicyExternalAddresses(FetchNetworkPolicyExternalAddressesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * fetchNetworkPolicyExternalAddresses(NetworkPolicyName networkPolicy) 
  * fetchNetworkPolicyExternalAddresses(String networkPolicy) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * fetchNetworkPolicyExternalAddressesPagedCallable() 
  * fetchNetworkPolicyExternalAddressesCallable() 

  
GetExternalAddress |  Gets details of a single external IP address. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getExternalAddress(GetExternalAddressRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getExternalAddress(ExternalAddressName name) 
  * getExternalAddress(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getExternalAddressCallable() 

  
CreateExternalAddress |  Creates a new `ExternalAddress` resource in a given private cloud. The network policy that corresponds to the private cloud must have the external IP address network service enabled (`NetworkPolicy.external_ip`). |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createExternalAddressAsync(CreateExternalAddressRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * createExternalAddressAsync(PrivateCloudName parent, ExternalAddress externalAddress, String externalAddressId) 
  * createExternalAddressAsync(String parent, ExternalAddress externalAddress, String externalAddressId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createExternalAddressOperationCallable() 
  * createExternalAddressCallable() 

  
UpdateExternalAddress |  Updates the parameters of a single external IP address. Only fields specified in `update_mask` are applied.  During operation processing, the resource is temporarily in the `ACTIVE` state before the operation fully completes. For that period of time, you can't update the resource. Use the operation status to determine when the processing fully completes. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateExternalAddressAsync(UpdateExternalAddressRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * updateExternalAddressAsync(ExternalAddress externalAddress, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateExternalAddressOperationCallable() 
  * updateExternalAddressCallable() 

  
DeleteExternalAddress |  Deletes a single external IP address. When you delete an external IP address, connectivity between the external IP address and the corresponding internal IP address is lost. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteExternalAddressAsync(DeleteExternalAddressRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteExternalAddressAsync(ExternalAddressName name) 
  * deleteExternalAddressAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteExternalAddressOperationCallable() 
  * deleteExternalAddressCallable() 

  
ListSubnets |  Lists subnets in a given private cloud. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listSubnets(ListSubnetsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listSubnets(PrivateCloudName parent) 
  * listSubnets(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listSubnetsPagedCallable() 
  * listSubnetsCallable() 

  
GetSubnet |  Gets details of a single subnet. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getSubnet(GetSubnetRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getSubnet(SubnetName name) 
  * getSubnet(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getSubnetCallable() 

  
UpdateSubnet |  Updates the parameters of a single subnet. Only fields specified in `update_mask` are applied.  *Note*: This API is synchronous and always returns a successful `google.longrunning.Operation` (LRO). The returned LRO will only have `done` and `response` fields. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateSubnetAsync(UpdateSubnetRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * updateSubnetAsync(Subnet subnet, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateSubnetOperationCallable() 
  * updateSubnetCallable() 

  
ListExternalAccessRules |  Lists `ExternalAccessRule` resources in the specified network policy. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listExternalAccessRules(ListExternalAccessRulesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listExternalAccessRules(NetworkPolicyName parent) 
  * listExternalAccessRules(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listExternalAccessRulesPagedCallable() 
  * listExternalAccessRulesCallable() 

  
GetExternalAccessRule |  Gets details of a single external access rule. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getExternalAccessRule(GetExternalAccessRuleRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getExternalAccessRule(ExternalAccessRuleName name) 
  * getExternalAccessRule(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getExternalAccessRuleCallable() 

  
CreateExternalAccessRule |  Creates a new external access rule in a given network policy. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createExternalAccessRuleAsync(CreateExternalAccessRuleRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * createExternalAccessRuleAsync(NetworkPolicyName parent, ExternalAccessRule externalAccessRule, String externalAccessRuleId) 
  * createExternalAccessRuleAsync(String parent, ExternalAccessRule externalAccessRule, String externalAccessRuleId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createExternalAccessRuleOperationCallable() 
  * createExternalAccessRuleCallable() 

  
UpdateExternalAccessRule |  Updates the parameters of a single external access rule. Only fields specified in `update_mask` are applied. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateExternalAccessRuleAsync(UpdateExternalAccessRuleRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * updateExternalAccessRuleAsync(ExternalAccessRule externalAccessRule, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateExternalAccessRuleOperationCallable() 
  * updateExternalAccessRuleCallable() 

  
DeleteExternalAccessRule |  Deletes a single external access rule. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteExternalAccessRuleAsync(DeleteExternalAccessRuleRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteExternalAccessRuleAsync(ExternalAccessRuleName name) 
  * deleteExternalAccessRuleAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteExternalAccessRuleOperationCallable() 
  * deleteExternalAccessRuleCallable() 

  
ListLoggingServers |  Lists logging servers configured for a given private cloud. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listLoggingServers(ListLoggingServersRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listLoggingServers(PrivateCloudName parent) 
  * listLoggingServers(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listLoggingServersPagedCallable() 
  * listLoggingServersCallable() 

  
GetLoggingServer |  Gets details of a logging server. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getLoggingServer(GetLoggingServerRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getLoggingServer(LoggingServerName name) 
  * getLoggingServer(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getLoggingServerCallable() 

  
CreateLoggingServer |  Create a new logging server for a given private cloud. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createLoggingServerAsync(CreateLoggingServerRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * createLoggingServerAsync(PrivateCloudName parent, LoggingServer loggingServer, String loggingServerId) 
  * createLoggingServerAsync(String parent, LoggingServer loggingServer, String loggingServerId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createLoggingServerOperationCallable() 
  * createLoggingServerCallable() 

  
UpdateLoggingServer |  Updates the parameters of a single logging server. Only fields specified in `update_mask` are applied. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateLoggingServerAsync(UpdateLoggingServerRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * updateLoggingServerAsync(LoggingServer loggingServer, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateLoggingServerOperationCallable() 
  * updateLoggingServerCallable() 

  
DeleteLoggingServer |  Deletes a single logging server. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteLoggingServerAsync(DeleteLoggingServerRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteLoggingServerAsync(LoggingServerName name) 
  * deleteLoggingServerAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteLoggingServerOperationCallable() 
  * deleteLoggingServerCallable() 

  
ListNodeTypes |  Lists node types |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listNodeTypes(ListNodeTypesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listNodeTypes(LocationName parent) 
  * listNodeTypes(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listNodeTypesPagedCallable() 
  * listNodeTypesCallable() 

  
GetNodeType |  Gets details of a single `NodeType`. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getNodeType(GetNodeTypeRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getNodeType(NodeTypeName name) 
  * getNodeType(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getNodeTypeCallable() 

  
ShowNsxCredentials |  Gets details of credentials for NSX appliance. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * showNsxCredentials(ShowNsxCredentialsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * showNsxCredentials(PrivateCloudName privateCloud) 
  * showNsxCredentials(String privateCloud) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * showNsxCredentialsCallable() 

  
ShowVcenterCredentials |  Gets details of credentials for Vcenter appliance. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * showVcenterCredentials(ShowVcenterCredentialsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * showVcenterCredentials(PrivateCloudName privateCloud) 
  * showVcenterCredentials(String privateCloud) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * showVcenterCredentialsCallable() 

  
ResetNsxCredentials |  Resets credentials of the NSX appliance. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * resetNsxCredentialsAsync(ResetNsxCredentialsRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * resetNsxCredentialsAsync(PrivateCloudName privateCloud) 
  * resetNsxCredentialsAsync(String privateCloud) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * resetNsxCredentialsOperationCallable() 
  * resetNsxCredentialsCallable() 

  
ResetVcenterCredentials |  Resets credentials of the Vcenter appliance. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * resetVcenterCredentialsAsync(ResetVcenterCredentialsRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * resetVcenterCredentialsAsync(PrivateCloudName privateCloud) 
  * resetVcenterCredentialsAsync(String privateCloud) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * resetVcenterCredentialsOperationCallable() 
  * resetVcenterCredentialsCallable() 

  
GetDnsForwarding |  Gets details of the `DnsForwarding` config. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getDnsForwarding(GetDnsForwardingRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getDnsForwarding(DnsForwardingName name) 
  * getDnsForwarding(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getDnsForwardingCallable() 

  
UpdateDnsForwarding |  Updates the parameters of the `DnsForwarding` config, like associated domains. Only fields specified in `update_mask` are applied. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateDnsForwardingAsync(UpdateDnsForwardingRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * updateDnsForwardingAsync(DnsForwarding dnsForwarding, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateDnsForwardingOperationCallable() 
  * updateDnsForwardingCallable() 

  
GetNetworkPeering |  Retrieves a `NetworkPeering` resource by its resource name. The resource contains details of the network peering, such as peered networks, import and export custom route configurations, and peering state. NetworkPeering is a global resource and location can only be global. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getNetworkPeering(GetNetworkPeeringRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getNetworkPeering(NetworkPeeringName name) 
  * getNetworkPeering(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getNetworkPeeringCallable() 

  
ListNetworkPeerings |  Lists `NetworkPeering` resources in a given project. NetworkPeering is a global resource and location can only be global. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listNetworkPeerings(ListNetworkPeeringsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listNetworkPeerings(LocationName parent) 
  * listNetworkPeerings(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listNetworkPeeringsPagedCallable() 
  * listNetworkPeeringsCallable() 

  
CreateNetworkPeering |  Creates a new network peering between the peer network and VMware Engine network provided in a `NetworkPeering` resource. NetworkPeering is a global resource and location can only be global. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createNetworkPeeringAsync(CreateNetworkPeeringRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * createNetworkPeeringAsync(LocationName parent, NetworkPeering networkPeering, String networkPeeringId) 
  * createNetworkPeeringAsync(String parent, NetworkPeering networkPeering, String networkPeeringId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createNetworkPeeringOperationCallable() 
  * createNetworkPeeringCallable() 

  
DeleteNetworkPeering |  Deletes a `NetworkPeering` resource. When a network peering is deleted for a VMware Engine network, the peer network becomes inaccessible to that VMware Engine network. NetworkPeering is a global resource and location can only be global. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteNetworkPeeringAsync(DeleteNetworkPeeringRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteNetworkPeeringAsync(NetworkPeeringName name) 
  * deleteNetworkPeeringAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteNetworkPeeringOperationCallable() 
  * deleteNetworkPeeringCallable() 

  
UpdateNetworkPeering |  Modifies a `NetworkPeering` resource. Only the `description` field can be updated. Only fields specified in `updateMask` are applied. NetworkPeering is a global resource and location can only be global. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateNetworkPeeringAsync(UpdateNetworkPeeringRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * updateNetworkPeeringAsync(NetworkPeering networkPeering, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateNetworkPeeringOperationCallable() 
  * updateNetworkPeeringCallable() 

  
ListPeeringRoutes |  Lists the network peering routes exchanged over a peering connection. NetworkPeering is a global resource and location can only be global. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listPeeringRoutes(ListPeeringRoutesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listPeeringRoutes(NetworkPeeringName parent) 
  * listPeeringRoutes(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listPeeringRoutesPagedCallable() 
  * listPeeringRoutesCallable() 

  
CreateHcxActivationKey |  Creates a new HCX activation key in a given private cloud. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createHcxActivationKeyAsync(CreateHcxActivationKeyRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * createHcxActivationKeyAsync(PrivateCloudName parent, HcxActivationKey hcxActivationKey, String hcxActivationKeyId) 
  * createHcxActivationKeyAsync(String parent, HcxActivationKey hcxActivationKey, String hcxActivationKeyId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createHcxActivationKeyOperationCallable() 
  * createHcxActivationKeyCallable() 

  
ListHcxActivationKeys |  Lists `HcxActivationKey` resources in a given private cloud. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listHcxActivationKeys(ListHcxActivationKeysRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listHcxActivationKeys(PrivateCloudName parent) 
  * listHcxActivationKeys(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listHcxActivationKeysPagedCallable() 
  * listHcxActivationKeysCallable() 

  
GetHcxActivationKey |  Retrieves a `HcxActivationKey` resource by its resource name. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getHcxActivationKey(GetHcxActivationKeyRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getHcxActivationKey(HcxActivationKeyName name) 
  * getHcxActivationKey(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getHcxActivationKeyCallable() 

  
GetNetworkPolicy |  Retrieves a `NetworkPolicy` resource by its resource name. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getNetworkPolicy(GetNetworkPolicyRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getNetworkPolicy(NetworkPolicyName name) 
  * getNetworkPolicy(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getNetworkPolicyCallable() 

  
ListNetworkPolicies |  Lists `NetworkPolicy` resources in a specified project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listNetworkPolicies(ListNetworkPoliciesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listNetworkPolicies(LocationName parent) 
  * listNetworkPolicies(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listNetworkPoliciesPagedCallable() 
  * listNetworkPoliciesCallable() 

  
CreateNetworkPolicy |  Creates a new network policy in a given VMware Engine network of a project and location (region). A new network policy cannot be created if another network policy already exists in the same scope. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createNetworkPolicyAsync(CreateNetworkPolicyRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * createNetworkPolicyAsync(LocationName parent, NetworkPolicy networkPolicy, String networkPolicyId) 
  * createNetworkPolicyAsync(String parent, NetworkPolicy networkPolicy, String networkPolicyId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createNetworkPolicyOperationCallable() 
  * createNetworkPolicyCallable() 

  
UpdateNetworkPolicy |  Modifies a `NetworkPolicy` resource. Only the following fields can be updated: `internet_access`, `external_ip`, `edge_services_cidr`. Only fields specified in `updateMask` are applied. When updating a network policy, the external IP network service can only be disabled if there are no external IP addresses present in the scope of the policy. Also, a `NetworkService` cannot be updated when `NetworkService.state` is set to `RECONCILING`.  During operation processing, the resource is temporarily in the `ACTIVE` state before the operation fully completes. For that period of time, you can't update the resource. Use the operation status to determine when the processing fully completes. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateNetworkPolicyAsync(UpdateNetworkPolicyRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * updateNetworkPolicyAsync(NetworkPolicy networkPolicy, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateNetworkPolicyOperationCallable() 
  * updateNetworkPolicyCallable() 

  
DeleteNetworkPolicy |  Deletes a `NetworkPolicy` resource. A network policy cannot be deleted when `NetworkService.state` is set to `RECONCILING` for either its external IP or internet access service. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteNetworkPolicyAsync(DeleteNetworkPolicyRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteNetworkPolicyAsync(NetworkPolicyName name) 
  * deleteNetworkPolicyAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteNetworkPolicyOperationCallable() 
  * deleteNetworkPolicyCallable() 

  
ListManagementDnsZoneBindings |  Lists Consumer VPCs bound to Management DNS Zone of a given private cloud. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listManagementDnsZoneBindings(ListManagementDnsZoneBindingsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listManagementDnsZoneBindings(PrivateCloudName parent) 
  * listManagementDnsZoneBindings(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listManagementDnsZoneBindingsPagedCallable() 
  * listManagementDnsZoneBindingsCallable() 

  
GetManagementDnsZoneBinding |  Retrieves a 'ManagementDnsZoneBinding' resource by its resource name. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getManagementDnsZoneBinding(GetManagementDnsZoneBindingRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getManagementDnsZoneBinding(ManagementDnsZoneBindingName name) 
  * getManagementDnsZoneBinding(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getManagementDnsZoneBindingCallable() 

  
CreateManagementDnsZoneBinding |  Creates a new `ManagementDnsZoneBinding` resource in a private cloud. This RPC creates the DNS binding and the resource that represents the DNS binding of the consumer VPC network to the management DNS zone. A management DNS zone is the Cloud DNS cross-project binding zone that VMware Engine creates for each private cloud. It contains FQDNs and corresponding IP addresses for the private cloud's ESXi hosts and management VM appliances like vCenter and NSX Manager. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createManagementDnsZoneBindingAsync(CreateManagementDnsZoneBindingRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * createManagementDnsZoneBindingAsync(PrivateCloudName parent, ManagementDnsZoneBinding managementDnsZoneBinding, String managementDnsZoneBindingId) 
  * createManagementDnsZoneBindingAsync(String parent, ManagementDnsZoneBinding managementDnsZoneBinding, String managementDnsZoneBindingId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createManagementDnsZoneBindingOperationCallable() 
  * createManagementDnsZoneBindingCallable() 

  
UpdateManagementDnsZoneBinding |  Updates a `ManagementDnsZoneBinding` resource. Only fields specified in `update_mask` are applied. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateManagementDnsZoneBindingAsync(UpdateManagementDnsZoneBindingRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * updateManagementDnsZoneBindingAsync(ManagementDnsZoneBinding managementDnsZoneBinding, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateManagementDnsZoneBindingOperationCallable() 
  * updateManagementDnsZoneBindingCallable() 

  
DeleteManagementDnsZoneBinding |  Deletes a `ManagementDnsZoneBinding` resource. When a management DNS zone binding is deleted, the corresponding consumer VPC network is no longer bound to the management DNS zone. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteManagementDnsZoneBindingAsync(DeleteManagementDnsZoneBindingRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteManagementDnsZoneBindingAsync(ManagementDnsZoneBindingName name) 
  * deleteManagementDnsZoneBindingAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteManagementDnsZoneBindingOperationCallable() 
  * deleteManagementDnsZoneBindingCallable() 

  
RepairManagementDnsZoneBinding |  Retries to create a `ManagementDnsZoneBinding` resource that is in failed state. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * repairManagementDnsZoneBindingAsync(RepairManagementDnsZoneBindingRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * repairManagementDnsZoneBindingAsync(ManagementDnsZoneBindingName name) 
  * repairManagementDnsZoneBindingAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * repairManagementDnsZoneBindingOperationCallable() 
  * repairManagementDnsZoneBindingCallable() 

  
CreateVmwareEngineNetwork |  Creates a new VMware Engine network that can be used by a private cloud. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createVmwareEngineNetworkAsync(CreateVmwareEngineNetworkRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * createVmwareEngineNetworkAsync(LocationName parent, VmwareEngineNetwork vmwareEngineNetwork, String vmwareEngineNetworkId) 
  * createVmwareEngineNetworkAsync(String parent, VmwareEngineNetwork vmwareEngineNetwork, String vmwareEngineNetworkId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createVmwareEngineNetworkOperationCallable() 
  * createVmwareEngineNetworkCallable() 

  
UpdateVmwareEngineNetwork |  Modifies a VMware Engine network resource. Only the following fields can be updated: `description`. Only fields specified in `updateMask` are applied. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateVmwareEngineNetworkAsync(UpdateVmwareEngineNetworkRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * updateVmwareEngineNetworkAsync(VmwareEngineNetwork vmwareEngineNetwork, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateVmwareEngineNetworkOperationCallable() 
  * updateVmwareEngineNetworkCallable() 

  
DeleteVmwareEngineNetwork |  Deletes a `VmwareEngineNetwork` resource. You can only delete a VMware Engine network after all resources that refer to it are deleted. For example, a private cloud, a network peering, and a network policy can all refer to the same VMware Engine network. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteVmwareEngineNetworkAsync(DeleteVmwareEngineNetworkRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteVmwareEngineNetworkAsync(VmwareEngineNetworkName name) 
  * deleteVmwareEngineNetworkAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteVmwareEngineNetworkOperationCallable() 
  * deleteVmwareEngineNetworkCallable() 

  
GetVmwareEngineNetwork |  Retrieves a `VmwareEngineNetwork` resource by its resource name. The resource contains details of the VMware Engine network, such as its VMware Engine network type, peered networks in a service project, and state (for example, `CREATING`, `ACTIVE`, `DELETING`). |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getVmwareEngineNetwork(GetVmwareEngineNetworkRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getVmwareEngineNetwork(VmwareEngineNetworkName name) 
  * getVmwareEngineNetwork(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getVmwareEngineNetworkCallable() 

  
ListVmwareEngineNetworks |  Lists `VmwareEngineNetwork` resources in a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listVmwareEngineNetworks(ListVmwareEngineNetworksRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listVmwareEngineNetworks(LocationName parent) 
  * listVmwareEngineNetworks(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listVmwareEngineNetworksPagedCallable() 
  * listVmwareEngineNetworksCallable() 

  
CreatePrivateConnection |  Creates a new private connection that can be used for accessing private Clouds. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createPrivateConnectionAsync(CreatePrivateConnectionRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * createPrivateConnectionAsync(LocationName parent, PrivateConnection privateConnection, String privateConnectionId) 
  * createPrivateConnectionAsync(String parent, PrivateConnection privateConnection, String privateConnectionId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createPrivateConnectionOperationCallable() 
  * createPrivateConnectionCallable() 

  
GetPrivateConnection |  Retrieves a `PrivateConnection` resource by its resource name. The resource contains details of the private connection, such as connected network, routing mode and state. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getPrivateConnection(GetPrivateConnectionRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getPrivateConnection(PrivateConnectionName name) 
  * getPrivateConnection(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getPrivateConnectionCallable() 

  
ListPrivateConnections |  Lists `PrivateConnection` resources in a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listPrivateConnections(ListPrivateConnectionsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listPrivateConnections(LocationName parent) 
  * listPrivateConnections(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listPrivateConnectionsPagedCallable() 
  * listPrivateConnectionsCallable() 

  
UpdatePrivateConnection |  Modifies a `PrivateConnection` resource. Only `description` and `routing_mode` fields can be updated. Only fields specified in `updateMask` are applied. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updatePrivateConnectionAsync(UpdatePrivateConnectionRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * updatePrivateConnectionAsync(PrivateConnection privateConnection, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updatePrivateConnectionOperationCallable() 
  * updatePrivateConnectionCallable() 

  
DeletePrivateConnection |  Deletes a `PrivateConnection` resource. When a private connection is deleted for a VMware Engine network, the connected network becomes inaccessible to that VMware Engine network. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deletePrivateConnectionAsync(DeletePrivateConnectionRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deletePrivateConnectionAsync(PrivateConnectionName name) 
  * deletePrivateConnectionAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deletePrivateConnectionOperationCallable() 
  * deletePrivateConnectionCallable() 

  
ListPrivateConnectionPeeringRoutes |  Lists the private connection routes exchanged over a peering connection. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listPrivateConnectionPeeringRoutes(ListPrivateConnectionPeeringRoutesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listPrivateConnectionPeeringRoutes(PrivateConnectionName parent) 
  * listPrivateConnectionPeeringRoutes(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listPrivateConnectionPeeringRoutesPagedCallable() 
  * listPrivateConnectionPeeringRoutesCallable() 

  
GrantDnsBindPermission |  Grants the bind permission to the customer provided principal(user / service account) to bind their DNS zone with the intranet VPC associated with the project. DnsBindPermission is a global resource and location can only be global. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * grantDnsBindPermissionAsync(GrantDnsBindPermissionRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * grantDnsBindPermissionAsync(DnsBindPermissionName name, Principal principal) 
  * grantDnsBindPermissionAsync(String name, Principal principal) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * grantDnsBindPermissionOperationCallable() 
  * grantDnsBindPermissionCallable() 

  
GetDnsBindPermission |  Gets all the principals having bind permission on the intranet VPC associated with the consumer project granted by the Grant API. DnsBindPermission is a global resource and location can only be global. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getDnsBindPermission(GetDnsBindPermissionRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getDnsBindPermission(DnsBindPermissionName name) 
  * getDnsBindPermission(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getDnsBindPermissionCallable() 

  
RevokeDnsBindPermission |  Revokes the bind permission from the customer provided principal(user / service account) on the intranet VPC associated with the consumer project. DnsBindPermission is a global resource and location can only be global. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * revokeDnsBindPermissionAsync(RevokeDnsBindPermissionRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * revokeDnsBindPermissionAsync(DnsBindPermissionName name, Principal principal) 
  * revokeDnsBindPermissionAsync(String name, Principal principal) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * revokeDnsBindPermissionOperationCallable() 
  * revokeDnsBindPermissionCallable() 

  
ListLocations |  Lists information about the supported locations for this service. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listLocations(ListLocationsRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listLocationsPagedCallable() 
  * listLocationsCallable() 

  
GetLocation |  Gets information about a location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getLocation(GetLocationRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getLocationCallable() 

  
SetIamPolicy |  Sets the access control policy on the specified resource. Replacesany existing policy.  Can return `NOT_FOUND`, `INVALID_ARGUMENT`, and `PERMISSION_DENIED`errors. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * setIamPolicy(SetIamPolicyRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * setIamPolicyCallable() 

  
GetIamPolicy |  Gets the access control policy for a resource. Returns an empty policyif the resource exists and does not have a policy set. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getIamPolicy(GetIamPolicyRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getIamPolicyCallable() 

  
TestIamPermissions |  Returns permissions that a caller has on the specified resource. If theresource does not exist, this will return an empty set ofpermissions, not a `NOT_FOUND` error.  Note: This operation is designed to be used for buildingpermission-aware UIs and command-line tools, not for authorizationchecking. This operation may "fail open" without warning. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * testIamPermissions(TestIamPermissionsRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * testIamPermissionsCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of VmwareEngineSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     VmwareEngineSettings vmwareEngineSettings =
         VmwareEngineSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create(vmwareEngineSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     VmwareEngineSettings vmwareEngineSettings =
         VmwareEngineSettings.newBuilder().setEndpoint(myEndpoint).build();
     VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create(vmwareEngineSettings);
     

To use REST (HTTP1.1/JSON) transport (instead of gRPC) for sending and receiving requests over the wire:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     VmwareEngineSettings vmwareEngineSettings = VmwareEngineSettings.newHttpJsonBuilder().build();
     VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create(vmwareEngineSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > VmwareEngineClient

## Static Methods 

### create()
    
    
    public static final VmwareEngineClient create()

Constructs an instance of VmwareEngineClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[VmwareEngineClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.VmwareEngineClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(VmwareEngineSettings settings)
    
    
    public static final VmwareEngineClient create(VmwareEngineSettings settings)

Constructs an instance of VmwareEngineClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[VmwareEngineSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.VmwareEngineSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[VmwareEngineClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.VmwareEngineClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(VmwareEngineStub stub)
    
    
    public static final VmwareEngineClient create(VmwareEngineStub stub)

Constructs an instance of VmwareEngineClient, using the given stub for making calls. This is for advanced usage - prefer using create(VmwareEngineSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[VmwareEngineStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.stub.VmwareEngineStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[VmwareEngineClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.VmwareEngineClient)` |   
  
## Constructors 

### VmwareEngineClient(VmwareEngineSettings settings)
    
    
    protected VmwareEngineClient(VmwareEngineSettings settings)

Constructs an instance of VmwareEngineClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[VmwareEngineSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.VmwareEngineSettings)`  
  
  
### VmwareEngineClient(VmwareEngineStub stub)
    
    
    protected VmwareEngineClient(VmwareEngineStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[VmwareEngineStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.stub.VmwareEngineStub)`  
  
  
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
  
### close()
    
    
    public final void close()

### createClusterAsync(@Nullable PrivateCloudName parent, Cluster cluster, String clusterId)
    
    
    public final OperationFuture<Cluster,OperationMetadata> createClusterAsync(@Nullable PrivateCloudName parent, Cluster cluster, String clusterId)

Creates a new cluster in a given private cloud. Creating a new cluster provides additional nodes for use in the parent private cloud and requires sufficient [node quota](https://cloud.google.com/vmware-engine/quotas).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       PrivateCloudName parent = PrivateCloudName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_CLOUD]");
       Cluster cluster = Cluster.newBuilder().build();
       String clusterId = "clusterId561939637";
       Cluster response = vmwareEngineClient.createClusterAsync(parent, cluster, clusterId).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.vmwareengine.v1.PrivateCloudName`  
Required. The resource name of the private cloud to create a new cluster in. Resource names are schemeless URIs that follow the conventions in <https://cloud.google.com/apis/design/resource_names>. For example: `projects/my-project/locations/us-central1-a/privateClouds/my-cloud`  
`cluster` | `[Cluster](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.Cluster)`  
Required. The initial description of the new cluster.  
`clusterId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The user-provided identifier of the new `Cluster`. This identifier must be unique among clusters within the parent and becomes the final token in the name URI. The identifier must meet the following requirements: 

  * Only contains 1-63 alphanumeric characters and hyphens 
  * Begins with an alphabetical character 
  * Ends with a non-hyphen character 
  * Not formatted as a UUID 
  * Complies with [RFC 1034](https://datatracker.ietf.org/doc/html/rfc1034) (section 3.5) 

  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Cluster](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.Cluster),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.OperationMetadata)>` |   
  
### createClusterAsync(CreateClusterRequest request)
    
    
    public final OperationFuture<Cluster,OperationMetadata> createClusterAsync(CreateClusterRequest request)

Creates a new cluster in a given private cloud. Creating a new cluster provides additional nodes for use in the parent private cloud and requires sufficient [node quota](https://cloud.google.com/vmware-engine/quotas).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       CreateClusterRequest request =
           CreateClusterRequest.newBuilder()
               .setParent(
                   PrivateCloudName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_CLOUD]").toString())
               .setClusterId("clusterId561939637")
               .setCluster(Cluster.newBuilder().build())
               .setRequestId("requestId693933066")
               .setValidateOnly(true)
               .build();
       Cluster response = vmwareEngineClient.createClusterAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.CreateClusterRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Cluster](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.Cluster),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.OperationMetadata)>` |   
  
### createClusterAsync(String parent, Cluster cluster, String clusterId)
    
    
    public final OperationFuture<Cluster,OperationMetadata> createClusterAsync(String parent, Cluster cluster, String clusterId)

Creates a new cluster in a given private cloud. Creating a new cluster provides additional nodes for use in the parent private cloud and requires sufficient [node quota](https://cloud.google.com/vmware-engine/quotas).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       String parent = PrivateCloudName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_CLOUD]").toString();
       Cluster cluster = Cluster.newBuilder().build();
       String clusterId = "clusterId561939637";
       Cluster response = vmwareEngineClient.createClusterAsync(parent, cluster, clusterId).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the private cloud to create a new cluster in. Resource names are schemeless URIs that follow the conventions in <https://cloud.google.com/apis/design/resource_names>. For example: `projects/my-project/locations/us-central1-a/privateClouds/my-cloud`  
`cluster` | `[Cluster](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.Cluster)`  
Required. The initial description of the new cluster.  
`clusterId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The user-provided identifier of the new `Cluster`. This identifier must be unique among clusters within the parent and becomes the final token in the name URI. The identifier must meet the following requirements: 

  * Only contains 1-63 alphanumeric characters and hyphens 
  * Begins with an alphabetical character 
  * Ends with a non-hyphen character 
  * Not formatted as a UUID 
  * Complies with [RFC 1034](https://datatracker.ietf.org/doc/html/rfc1034) (section 3.5) 

  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Cluster](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.Cluster),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.OperationMetadata)>` |   
  
### createClusterCallable()
    
    
    public final UnaryCallable<CreateClusterRequest,Operation> createClusterCallable()

Creates a new cluster in a given private cloud. Creating a new cluster provides additional nodes for use in the parent private cloud and requires sufficient [node quota](https://cloud.google.com/vmware-engine/quotas).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       CreateClusterRequest request =
           CreateClusterRequest.newBuilder()
               .setParent(
                   PrivateCloudName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_CLOUD]").toString())
               .setClusterId("clusterId561939637")
               .setCluster(Cluster.newBuilder().build())
               .setRequestId("requestId693933066")
               .setValidateOnly(true)
               .build();
       ApiFuture<Operation> future = vmwareEngineClient.createClusterCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.CreateClusterRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createClusterOperationCallable()
    
    
    public final OperationCallable<CreateClusterRequest,Cluster,OperationMetadata> createClusterOperationCallable()

Creates a new cluster in a given private cloud. Creating a new cluster provides additional nodes for use in the parent private cloud and requires sufficient [node quota](https://cloud.google.com/vmware-engine/quotas).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       CreateClusterRequest request =
           CreateClusterRequest.newBuilder()
               .setParent(
                   PrivateCloudName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_CLOUD]").toString())
               .setClusterId("clusterId561939637")
               .setCluster(Cluster.newBuilder().build())
               .setRequestId("requestId693933066")
               .setValidateOnly(true)
               .build();
       OperationFuture<Cluster, OperationMetadata> future =
           vmwareEngineClient.createClusterOperationCallable().futureCall(request);
       // Do something.
       Cluster response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.CreateClusterRequest),[Cluster](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.Cluster),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.OperationMetadata)>` |   
  
### createExternalAccessRuleAsync(@Nullable NetworkPolicyName parent, ExternalAccessRule externalAccessRule, String externalAccessRuleId)
    
    
    public final OperationFuture<ExternalAccessRule,OperationMetadata> createExternalAccessRuleAsync(@Nullable NetworkPolicyName parent, ExternalAccessRule externalAccessRule, String externalAccessRuleId)

Creates a new external access rule in a given network policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       NetworkPolicyName parent =
           NetworkPolicyName.of("[PROJECT]", "[LOCATION]", "[NETWORK_POLICY]");
       ExternalAccessRule externalAccessRule = ExternalAccessRule.newBuilder().build();
       String externalAccessRuleId = "externalAccessRuleId1937389350";
       ExternalAccessRule response =
           vmwareEngineClient
               .createExternalAccessRuleAsync(parent, externalAccessRule, externalAccessRuleId)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.vmwareengine.v1.NetworkPolicyName`  
Required. The resource name of the network policy to create a new external access firewall rule in. Resource names are schemeless URIs that follow the conventions in <https://cloud.google.com/apis/design/resource_names>. For example: `projects/my-project/locations/us-central1/networkPolicies/my-policy`  
`externalAccessRule` | `[ExternalAccessRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.ExternalAccessRule)`  
Required. The initial description of a new external access rule.  
`externalAccessRuleId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The user-provided identifier of the `ExternalAccessRule` to be created. This identifier must be unique among `ExternalAccessRule` resources within the parent and becomes the final token in the name URI. The identifier must meet the following requirements: 

  * Only contains 1-63 alphanumeric characters and hyphens 
  * Begins with an alphabetical character 
  * Ends with a non-hyphen character 
  * Not formatted as a UUID 
  * Complies with [RFC 1034](https://datatracker.ietf.org/doc/html/rfc1034) (section 3.5) 

  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[ExternalAccessRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.ExternalAccessRule),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.OperationMetadata)>` |   
  
### createExternalAccessRuleAsync(CreateExternalAccessRuleRequest request)
    
    
    public final OperationFuture<ExternalAccessRule,OperationMetadata> createExternalAccessRuleAsync(CreateExternalAccessRuleRequest request)

Creates a new external access rule in a given network policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       CreateExternalAccessRuleRequest request =
           CreateExternalAccessRuleRequest.newBuilder()
               .setParent(
                   NetworkPolicyName.of("[PROJECT]", "[LOCATION]", "[NETWORK_POLICY]").toString())
               .setExternalAccessRule(ExternalAccessRule.newBuilder().build())
               .setExternalAccessRuleId("externalAccessRuleId1937389350")
               .setRequestId("requestId693933066")
               .build();
       ExternalAccessRule response = vmwareEngineClient.createExternalAccessRuleAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateExternalAccessRuleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.CreateExternalAccessRuleRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[ExternalAccessRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.ExternalAccessRule),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.OperationMetadata)>` |   
  
### createExternalAccessRuleAsync(String parent, ExternalAccessRule externalAccessRule, String externalAccessRuleId)
    
    
    public final OperationFuture<ExternalAccessRule,OperationMetadata> createExternalAccessRuleAsync(String parent, ExternalAccessRule externalAccessRule, String externalAccessRuleId)

Creates a new external access rule in a given network policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       String parent =
           NetworkPolicyName.of("[PROJECT]", "[LOCATION]", "[NETWORK_POLICY]").toString();
       ExternalAccessRule externalAccessRule = ExternalAccessRule.newBuilder().build();
       String externalAccessRuleId = "externalAccessRuleId1937389350";
       ExternalAccessRule response =
           vmwareEngineClient
               .createExternalAccessRuleAsync(parent, externalAccessRule, externalAccessRuleId)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the network policy to create a new external access firewall rule in. Resource names are schemeless URIs that follow the conventions in <https://cloud.google.com/apis/design/resource_names>. For example: `projects/my-project/locations/us-central1/networkPolicies/my-policy`  
`externalAccessRule` | `[ExternalAccessRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.ExternalAccessRule)`  
Required. The initial description of a new external access rule.  
`externalAccessRuleId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The user-provided identifier of the `ExternalAccessRule` to be created. This identifier must be unique among `ExternalAccessRule` resources within the parent and becomes the final token in the name URI. The identifier must meet the following requirements: 

  * Only contains 1-63 alphanumeric characters and hyphens 
  * Begins with an alphabetical character 
  * Ends with a non-hyphen character 
  * Not formatted as a UUID 
  * Complies with [RFC 1034](https://datatracker.ietf.org/doc/html/rfc1034) (section 3.5) 

  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[ExternalAccessRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.ExternalAccessRule),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.OperationMetadata)>` |   
  
### createExternalAccessRuleCallable()
    
    
    public final UnaryCallable<CreateExternalAccessRuleRequest,Operation> createExternalAccessRuleCallable()

Creates a new external access rule in a given network policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       CreateExternalAccessRuleRequest request =
           CreateExternalAccessRuleRequest.newBuilder()
               .setParent(
                   NetworkPolicyName.of("[PROJECT]", "[LOCATION]", "[NETWORK_POLICY]").toString())
               .setExternalAccessRule(ExternalAccessRule.newBuilder().build())
               .setExternalAccessRuleId("externalAccessRuleId1937389350")
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           vmwareEngineClient.createExternalAccessRuleCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateExternalAccessRuleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.CreateExternalAccessRuleRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createExternalAccessRuleOperationCallable()
    
    
    public final OperationCallable<CreateExternalAccessRuleRequest,ExternalAccessRule,OperationMetadata> createExternalAccessRuleOperationCallable()

Creates a new external access rule in a given network policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       CreateExternalAccessRuleRequest request =
           CreateExternalAccessRuleRequest.newBuilder()
               .setParent(
                   NetworkPolicyName.of("[PROJECT]", "[LOCATION]", "[NETWORK_POLICY]").toString())
               .setExternalAccessRule(ExternalAccessRule.newBuilder().build())
               .setExternalAccessRuleId("externalAccessRuleId1937389350")
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<ExternalAccessRule, OperationMetadata> future =
           vmwareEngineClient.createExternalAccessRuleOperationCallable().futureCall(request);
       // Do something.
       ExternalAccessRule response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateExternalAccessRuleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.CreateExternalAccessRuleRequest),[ExternalAccessRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.ExternalAccessRule),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.OperationMetadata)>` |   
  
### createExternalAddressAsync(@Nullable PrivateCloudName parent, ExternalAddress externalAddress, String externalAddressId)
    
    
    public final OperationFuture<ExternalAddress,OperationMetadata> createExternalAddressAsync(@Nullable PrivateCloudName parent, ExternalAddress externalAddress, String externalAddressId)

Creates a new `ExternalAddress` resource in a given private cloud. The network policy that corresponds to the private cloud must have the external IP address network service enabled (`NetworkPolicy.external_ip`).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       PrivateCloudName parent = PrivateCloudName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_CLOUD]");
       ExternalAddress externalAddress = ExternalAddress.newBuilder().build();
       String externalAddressId = "externalAddressId221595812";
       ExternalAddress response =
           vmwareEngineClient
               .createExternalAddressAsync(parent, externalAddress, externalAddressId)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.vmwareengine.v1.PrivateCloudName`  
Required. The resource name of the private cloud to create a new external IP address in. Resource names are schemeless URIs that follow the conventions in <https://cloud.google.com/apis/design/resource_names>. For example: `projects/my-project/locations/us-central1-a/privateClouds/my-cloud`  
`externalAddress` | `[ExternalAddress](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.ExternalAddress)`  
Required. The initial description of a new external IP address.  
`externalAddressId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The user-provided identifier of the `ExternalAddress` to be created. This identifier must be unique among `ExternalAddress` resources within the parent and becomes the final token in the name URI. The identifier must meet the following requirements: 

  * Only contains 1-63 alphanumeric characters and hyphens 
  * Begins with an alphabetical character 
  * Ends with a non-hyphen character 
  * Not formatted as a UUID 
  * Complies with [RFC 1034](https://datatracker.ietf.org/doc/html/rfc1034) (section 3.5) 

  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[ExternalAddress](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.ExternalAddress),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.OperationMetadata)>` |   
  
### createExternalAddressAsync(CreateExternalAddressRequest request)
    
    
    public final OperationFuture<ExternalAddress,OperationMetadata> createExternalAddressAsync(CreateExternalAddressRequest request)

Creates a new `ExternalAddress` resource in a given private cloud. The network policy that corresponds to the private cloud must have the external IP address network service enabled (`NetworkPolicy.external_ip`).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       CreateExternalAddressRequest request =
           CreateExternalAddressRequest.newBuilder()
               .setParent(
                   PrivateCloudName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_CLOUD]").toString())
               .setExternalAddress(ExternalAddress.newBuilder().build())
               .setExternalAddressId("externalAddressId221595812")
               .setRequestId("requestId693933066")
               .build();
       ExternalAddress response = vmwareEngineClient.createExternalAddressAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateExternalAddressRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.CreateExternalAddressRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[ExternalAddress](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.ExternalAddress),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.OperationMetadata)>` |   
  
### createExternalAddressAsync(String parent, ExternalAddress externalAddress, String externalAddressId)
    
    
    public final OperationFuture<ExternalAddress,OperationMetadata> createExternalAddressAsync(String parent, ExternalAddress externalAddress, String externalAddressId)

Creates a new `ExternalAddress` resource in a given private cloud. The network policy that corresponds to the private cloud must have the external IP address network service enabled (`NetworkPolicy.external_ip`).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       String parent = PrivateCloudName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_CLOUD]").toString();
       ExternalAddress externalAddress = ExternalAddress.newBuilder().build();
       String externalAddressId = "externalAddressId221595812";
       ExternalAddress response =
           vmwareEngineClient
               .createExternalAddressAsync(parent, externalAddress, externalAddressId)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the private cloud to create a new external IP address in. Resource names are schemeless URIs that follow the conventions in <https://cloud.google.com/apis/design/resource_names>. For example: `projects/my-project/locations/us-central1-a/privateClouds/my-cloud`  
`externalAddress` | `[ExternalAddress](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.ExternalAddress)`  
Required. The initial description of a new external IP address.  
`externalAddressId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The user-provided identifier of the `ExternalAddress` to be created. This identifier must be unique among `ExternalAddress` resources within the parent and becomes the final token in the name URI. The identifier must meet the following requirements: 

  * Only contains 1-63 alphanumeric characters and hyphens 
  * Begins with an alphabetical character 
  * Ends with a non-hyphen character 
  * Not formatted as a UUID 
  * Complies with [RFC 1034](https://datatracker.ietf.org/doc/html/rfc1034) (section 3.5) 

  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[ExternalAddress](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.ExternalAddress),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.OperationMetadata)>` |   
  
### createExternalAddressCallable()
    
    
    public final UnaryCallable<CreateExternalAddressRequest,Operation> createExternalAddressCallable()

Creates a new `ExternalAddress` resource in a given private cloud. The network policy that corresponds to the private cloud must have the external IP address network service enabled (`NetworkPolicy.external_ip`).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       CreateExternalAddressRequest request =
           CreateExternalAddressRequest.newBuilder()
               .setParent(
                   PrivateCloudName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_CLOUD]").toString())
               .setExternalAddress(ExternalAddress.newBuilder().build())
               .setExternalAddressId("externalAddressId221595812")
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           vmwareEngineClient.createExternalAddressCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateExternalAddressRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.CreateExternalAddressRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createExternalAddressOperationCallable()
    
    
    public final OperationCallable<CreateExternalAddressRequest,ExternalAddress,OperationMetadata> createExternalAddressOperationCallable()

Creates a new `ExternalAddress` resource in a given private cloud. The network policy that corresponds to the private cloud must have the external IP address network service enabled (`NetworkPolicy.external_ip`).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       CreateExternalAddressRequest request =
           CreateExternalAddressRequest.newBuilder()
               .setParent(
                   PrivateCloudName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_CLOUD]").toString())
               .setExternalAddress(ExternalAddress.newBuilder().build())
               .setExternalAddressId("externalAddressId221595812")
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<ExternalAddress, OperationMetadata> future =
           vmwareEngineClient.createExternalAddressOperationCallable().futureCall(request);
       // Do something.
       ExternalAddress response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateExternalAddressRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.CreateExternalAddressRequest),[ExternalAddress](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.ExternalAddress),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.OperationMetadata)>` |   
  
### createHcxActivationKeyAsync(@Nullable PrivateCloudName parent, HcxActivationKey hcxActivationKey, String hcxActivationKeyId)
    
    
    public final OperationFuture<HcxActivationKey,OperationMetadata> createHcxActivationKeyAsync(@Nullable PrivateCloudName parent, HcxActivationKey hcxActivationKey, String hcxActivationKeyId)

Creates a new HCX activation key in a given private cloud.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       PrivateCloudName parent = PrivateCloudName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_CLOUD]");
       HcxActivationKey hcxActivationKey = HcxActivationKey.newBuilder().build();
       String hcxActivationKeyId = "hcxActivationKeyId-645871673";
       HcxActivationKey response =
           vmwareEngineClient
               .createHcxActivationKeyAsync(parent, hcxActivationKey, hcxActivationKeyId)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.vmwareengine.v1.PrivateCloudName`  
Required. The resource name of the private cloud to create the key for. Resource names are schemeless URIs that follow the conventions in <https://cloud.google.com/apis/design/resource_names>. For example: `projects/my-project/locations/us-central1/privateClouds/my-cloud`  
`hcxActivationKey` | `[HcxActivationKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.HcxActivationKey)`  
Required. The initial description of a new HCX activation key. When creating a new key, this field must be an empty object.  
`hcxActivationKeyId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The user-provided identifier of the `HcxActivationKey` to be created. This identifier must be unique among `HcxActivationKey` resources within the parent and becomes the final token in the name URI. The identifier must meet the following requirements: 

  * Only contains 1-63 alphanumeric characters and hyphens 
  * Begins with an alphabetical character 
  * Ends with a non-hyphen character 
  * Not formatted as a UUID 
  * Complies with [RFC 1034](https://datatracker.ietf.org/doc/html/rfc1034) (section 3.5) 

  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[HcxActivationKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.HcxActivationKey),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.OperationMetadata)>` |   
  
### createHcxActivationKeyAsync(CreateHcxActivationKeyRequest request)
    
    
    public final OperationFuture<HcxActivationKey,OperationMetadata> createHcxActivationKeyAsync(CreateHcxActivationKeyRequest request)

Creates a new HCX activation key in a given private cloud.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       CreateHcxActivationKeyRequest request =
           CreateHcxActivationKeyRequest.newBuilder()
               .setParent(
                   PrivateCloudName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_CLOUD]").toString())
               .setHcxActivationKey(HcxActivationKey.newBuilder().build())
               .setHcxActivationKeyId("hcxActivationKeyId-645871673")
               .setRequestId("requestId693933066")
               .build();
       HcxActivationKey response = vmwareEngineClient.createHcxActivationKeyAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateHcxActivationKeyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.CreateHcxActivationKeyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[HcxActivationKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.HcxActivationKey),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.OperationMetadata)>` |   
  
### createHcxActivationKeyAsync(String parent, HcxActivationKey hcxActivationKey, String hcxActivationKeyId)
    
    
    public final OperationFuture<HcxActivationKey,OperationMetadata> createHcxActivationKeyAsync(String parent, HcxActivationKey hcxActivationKey, String hcxActivationKeyId)

Creates a new HCX activation key in a given private cloud.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       String parent = PrivateCloudName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_CLOUD]").toString();
       HcxActivationKey hcxActivationKey = HcxActivationKey.newBuilder().build();
       String hcxActivationKeyId = "hcxActivationKeyId-645871673";
       HcxActivationKey response =
           vmwareEngineClient
               .createHcxActivationKeyAsync(parent, hcxActivationKey, hcxActivationKeyId)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the private cloud to create the key for. Resource names are schemeless URIs that follow the conventions in <https://cloud.google.com/apis/design/resource_names>. For example: `projects/my-project/locations/us-central1/privateClouds/my-cloud`  
`hcxActivationKey` | `[HcxActivationKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.HcxActivationKey)`  
Required. The initial description of a new HCX activation key. When creating a new key, this field must be an empty object.  
`hcxActivationKeyId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The user-provided identifier of the `HcxActivationKey` to be created. This identifier must be unique among `HcxActivationKey` resources within the parent and becomes the final token in the name URI. The identifier must meet the following requirements: 

  * Only contains 1-63 alphanumeric characters and hyphens 
  * Begins with an alphabetical character 
  * Ends with a non-hyphen character 
  * Not formatted as a UUID 
  * Complies with [RFC 1034](https://datatracker.ietf.org/doc/html/rfc1034) (section 3.5) 

  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[HcxActivationKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.HcxActivationKey),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.OperationMetadata)>` |   
  
### createHcxActivationKeyCallable()
    
    
    public final UnaryCallable<CreateHcxActivationKeyRequest,Operation> createHcxActivationKeyCallable()

Creates a new HCX activation key in a given private cloud.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       CreateHcxActivationKeyRequest request =
           CreateHcxActivationKeyRequest.newBuilder()
               .setParent(
                   PrivateCloudName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_CLOUD]").toString())
               .setHcxActivationKey(HcxActivationKey.newBuilder().build())
               .setHcxActivationKeyId("hcxActivationKeyId-645871673")
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           vmwareEngineClient.createHcxActivationKeyCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateHcxActivationKeyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.CreateHcxActivationKeyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createHcxActivationKeyOperationCallable()
    
    
    public final OperationCallable<CreateHcxActivationKeyRequest,HcxActivationKey,OperationMetadata> createHcxActivationKeyOperationCallable()

Creates a new HCX activation key in a given private cloud.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       CreateHcxActivationKeyRequest request =
           CreateHcxActivationKeyRequest.newBuilder()
               .setParent(
                   PrivateCloudName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_CLOUD]").toString())
               .setHcxActivationKey(HcxActivationKey.newBuilder().build())
               .setHcxActivationKeyId("hcxActivationKeyId-645871673")
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<HcxActivationKey, OperationMetadata> future =
           vmwareEngineClient.createHcxActivationKeyOperationCallable().futureCall(request);
       // Do something.
       HcxActivationKey response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateHcxActivationKeyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.CreateHcxActivationKeyRequest),[HcxActivationKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.HcxActivationKey),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.OperationMetadata)>` |   
  
### createLoggingServerAsync(@Nullable PrivateCloudName parent, LoggingServer loggingServer, String loggingServerId)
    
    
    public final OperationFuture<LoggingServer,OperationMetadata> createLoggingServerAsync(@Nullable PrivateCloudName parent, LoggingServer loggingServer, String loggingServerId)

Create a new logging server for a given private cloud.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       PrivateCloudName parent = PrivateCloudName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_CLOUD]");
       LoggingServer loggingServer = LoggingServer.newBuilder().build();
       String loggingServerId = "loggingServerId-304163779";
       LoggingServer response =
           vmwareEngineClient.createLoggingServerAsync(parent, loggingServer, loggingServerId).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.vmwareengine.v1.PrivateCloudName`  
Required. The resource name of the private cloud to create a new Logging Server in. Resource names are schemeless URIs that follow the conventions in <https://cloud.google.com/apis/design/resource_names>. For example: `projects/my-project/locations/us-central1-a/privateClouds/my-cloud`  
`loggingServer` | `[LoggingServer](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.LoggingServer)`  
Required. The initial description of a new logging server.  
`loggingServerId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The user-provided identifier of the `LoggingServer` to be created. This identifier must be unique among `LoggingServer` resources within the parent and becomes the final token in the name URI. The identifier must meet the following requirements: 

  * Only contains 1-63 alphanumeric characters and hyphens 
  * Begins with an alphabetical character 
  * Ends with a non-hyphen character 
  * Not formatted as a UUID 
  * Complies with [RFC 1034](https://datatracker.ietf.org/doc/html/rfc1034) (section 3.5) 

  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[LoggingServer](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.LoggingServer),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.OperationMetadata)>` |   
  
### createLoggingServerAsync(CreateLoggingServerRequest request)
    
    
    public final OperationFuture<LoggingServer,OperationMetadata> createLoggingServerAsync(CreateLoggingServerRequest request)

Create a new logging server for a given private cloud.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       CreateLoggingServerRequest request =
           CreateLoggingServerRequest.newBuilder()
               .setParent(
                   PrivateCloudName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_CLOUD]").toString())
               .setLoggingServer(LoggingServer.newBuilder().build())
               .setLoggingServerId("loggingServerId-304163779")
               .setRequestId("requestId693933066")
               .build();
       LoggingServer response = vmwareEngineClient.createLoggingServerAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateLoggingServerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.CreateLoggingServerRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[LoggingServer](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.LoggingServer),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.OperationMetadata)>` |   
  
### createLoggingServerAsync(String parent, LoggingServer loggingServer, String loggingServerId)
    
    
    public final OperationFuture<LoggingServer,OperationMetadata> createLoggingServerAsync(String parent, LoggingServer loggingServer, String loggingServerId)

Create a new logging server for a given private cloud.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       String parent = PrivateCloudName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_CLOUD]").toString();
       LoggingServer loggingServer = LoggingServer.newBuilder().build();
       String loggingServerId = "loggingServerId-304163779";
       LoggingServer response =
           vmwareEngineClient.createLoggingServerAsync(parent, loggingServer, loggingServerId).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the private cloud to create a new Logging Server in. Resource names are schemeless URIs that follow the conventions in <https://cloud.google.com/apis/design/resource_names>. For example: `projects/my-project/locations/us-central1-a/privateClouds/my-cloud`  
`loggingServer` | `[LoggingServer](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.LoggingServer)`  
Required. The initial description of a new logging server.  
`loggingServerId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The user-provided identifier of the `LoggingServer` to be created. This identifier must be unique among `LoggingServer` resources within the parent and becomes the final token in the name URI. The identifier must meet the following requirements: 

  * Only contains 1-63 alphanumeric characters and hyphens 
  * Begins with an alphabetical character 
  * Ends with a non-hyphen character 
  * Not formatted as a UUID 
  * Complies with [RFC 1034](https://datatracker.ietf.org/doc/html/rfc1034) (section 3.5) 

  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[LoggingServer](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.LoggingServer),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.OperationMetadata)>` |   
  
### createLoggingServerCallable()
    
    
    public final UnaryCallable<CreateLoggingServerRequest,Operation> createLoggingServerCallable()

Create a new logging server for a given private cloud.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       CreateLoggingServerRequest request =
           CreateLoggingServerRequest.newBuilder()
               .setParent(
                   PrivateCloudName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_CLOUD]").toString())
               .setLoggingServer(LoggingServer.newBuilder().build())
               .setLoggingServerId("loggingServerId-304163779")
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           vmwareEngineClient.createLoggingServerCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateLoggingServerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.CreateLoggingServerRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createLoggingServerOperationCallable()
    
    
    public final OperationCallable<CreateLoggingServerRequest,LoggingServer,OperationMetadata> createLoggingServerOperationCallable()

Create a new logging server for a given private cloud.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       CreateLoggingServerRequest request =
           CreateLoggingServerRequest.newBuilder()
               .setParent(
                   PrivateCloudName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_CLOUD]").toString())
               .setLoggingServer(LoggingServer.newBuilder().build())
               .setLoggingServerId("loggingServerId-304163779")
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<LoggingServer, OperationMetadata> future =
           vmwareEngineClient.createLoggingServerOperationCallable().futureCall(request);
       // Do something.
       LoggingServer response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateLoggingServerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.CreateLoggingServerRequest),[LoggingServer](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.LoggingServer),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.OperationMetadata)>` |   
  
### createManagementDnsZoneBindingAsync(@Nullable PrivateCloudName parent, ManagementDnsZoneBinding managementDnsZoneBinding, String managementDnsZoneBindingId)
    
    
    public final OperationFuture<ManagementDnsZoneBinding,OperationMetadata> createManagementDnsZoneBindingAsync(@Nullable PrivateCloudName parent, ManagementDnsZoneBinding managementDnsZoneBinding, String managementDnsZoneBindingId)

Creates a new `ManagementDnsZoneBinding` resource in a private cloud. This RPC creates the DNS binding and the resource that represents the DNS binding of the consumer VPC network to the management DNS zone. A management DNS zone is the Cloud DNS cross-project binding zone that VMware Engine creates for each private cloud. It contains FQDNs and corresponding IP addresses for the private cloud's ESXi hosts and management VM appliances like vCenter and NSX Manager.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       PrivateCloudName parent = PrivateCloudName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_CLOUD]");
       ManagementDnsZoneBinding managementDnsZoneBinding =
           ManagementDnsZoneBinding.newBuilder().build();
       String managementDnsZoneBindingId = "managementDnsZoneBindingId-288984082";
       ManagementDnsZoneBinding response =
           vmwareEngineClient
               .createManagementDnsZoneBindingAsync(
                   parent, managementDnsZoneBinding, managementDnsZoneBindingId)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.vmwareengine.v1.PrivateCloudName`  
Required. The resource name of the private cloud to create a new management DNS zone binding for. Resource names are schemeless URIs that follow the conventions in <https://cloud.google.com/apis/design/resource_names>. For example: `projects/my-project/locations/us-central1-a/privateClouds/my-cloud`  
`managementDnsZoneBinding` | `[ManagementDnsZoneBinding](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.ManagementDnsZoneBinding)`  
Required. The initial values for a new management DNS zone binding.  
`managementDnsZoneBindingId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The user-provided identifier of the `ManagementDnsZoneBinding` resource to be created. This identifier must be unique among `ManagementDnsZoneBinding` resources within the parent and becomes the final token in the name URI. The identifier must meet the following requirements: 

  * Only contains 1-63 alphanumeric characters and hyphens 
  * Begins with an alphabetical character 
  * Ends with a non-hyphen character 
  * Not formatted as a UUID 
  * Complies with [RFC 1034](https://datatracker.ietf.org/doc/html/rfc1034) (section 3.5) 

  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[ManagementDnsZoneBinding](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.ManagementDnsZoneBinding),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.OperationMetadata)>` |   
  
### createManagementDnsZoneBindingAsync(CreateManagementDnsZoneBindingRequest request)
    
    
    public final OperationFuture<ManagementDnsZoneBinding,OperationMetadata> createManagementDnsZoneBindingAsync(CreateManagementDnsZoneBindingRequest request)

Creates a new `ManagementDnsZoneBinding` resource in a private cloud. This RPC creates the DNS binding and the resource that represents the DNS binding of the consumer VPC network to the management DNS zone. A management DNS zone is the Cloud DNS cross-project binding zone that VMware Engine creates for each private cloud. It contains FQDNs and corresponding IP addresses for the private cloud's ESXi hosts and management VM appliances like vCenter and NSX Manager.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       CreateManagementDnsZoneBindingRequest request =
           CreateManagementDnsZoneBindingRequest.newBuilder()
               .setParent(
                   PrivateCloudName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_CLOUD]").toString())
               .setManagementDnsZoneBinding(ManagementDnsZoneBinding.newBuilder().build())
               .setManagementDnsZoneBindingId("managementDnsZoneBindingId-288984082")
               .setRequestId("requestId693933066")
               .build();
       ManagementDnsZoneBinding response =
           vmwareEngineClient.createManagementDnsZoneBindingAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateManagementDnsZoneBindingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.CreateManagementDnsZoneBindingRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[ManagementDnsZoneBinding](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.ManagementDnsZoneBinding),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.OperationMetadata)>` |   
  
### createManagementDnsZoneBindingAsync(String parent, ManagementDnsZoneBinding managementDnsZoneBinding, String managementDnsZoneBindingId)
    
    
    public final OperationFuture<ManagementDnsZoneBinding,OperationMetadata> createManagementDnsZoneBindingAsync(String parent, ManagementDnsZoneBinding managementDnsZoneBinding, String managementDnsZoneBindingId)

Creates a new `ManagementDnsZoneBinding` resource in a private cloud. This RPC creates the DNS binding and the resource that represents the DNS binding of the consumer VPC network to the management DNS zone. A management DNS zone is the Cloud DNS cross-project binding zone that VMware Engine creates for each private cloud. It contains FQDNs and corresponding IP addresses for the private cloud's ESXi hosts and management VM appliances like vCenter and NSX Manager.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       String parent = PrivateCloudName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_CLOUD]").toString();
       ManagementDnsZoneBinding managementDnsZoneBinding =
           ManagementDnsZoneBinding.newBuilder().build();
       String managementDnsZoneBindingId = "managementDnsZoneBindingId-288984082";
       ManagementDnsZoneBinding response =
           vmwareEngineClient
               .createManagementDnsZoneBindingAsync(
                   parent, managementDnsZoneBinding, managementDnsZoneBindingId)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the private cloud to create a new management DNS zone binding for. Resource names are schemeless URIs that follow the conventions in <https://cloud.google.com/apis/design/resource_names>. For example: `projects/my-project/locations/us-central1-a/privateClouds/my-cloud`  
`managementDnsZoneBinding` | `[ManagementDnsZoneBinding](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.ManagementDnsZoneBinding)`  
Required. The initial values for a new management DNS zone binding.  
`managementDnsZoneBindingId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The user-provided identifier of the `ManagementDnsZoneBinding` resource to be created. This identifier must be unique among `ManagementDnsZoneBinding` resources within the parent and becomes the final token in the name URI. The identifier must meet the following requirements: 

  * Only contains 1-63 alphanumeric characters and hyphens 
  * Begins with an alphabetical character 
  * Ends with a non-hyphen character 
  * Not formatted as a UUID 
  * Complies with [RFC 1034](https://datatracker.ietf.org/doc/html/rfc1034) (section 3.5) 

  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[ManagementDnsZoneBinding](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.ManagementDnsZoneBinding),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.OperationMetadata)>` |   
  
### createManagementDnsZoneBindingCallable()
    
    
    public final UnaryCallable<CreateManagementDnsZoneBindingRequest,Operation> createManagementDnsZoneBindingCallable()

Creates a new `ManagementDnsZoneBinding` resource in a private cloud. This RPC creates the DNS binding and the resource that represents the DNS binding of the consumer VPC network to the management DNS zone. A management DNS zone is the Cloud DNS cross-project binding zone that VMware Engine creates for each private cloud. It contains FQDNs and corresponding IP addresses for the private cloud's ESXi hosts and management VM appliances like vCenter and NSX Manager.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       CreateManagementDnsZoneBindingRequest request =
           CreateManagementDnsZoneBindingRequest.newBuilder()
               .setParent(
                   PrivateCloudName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_CLOUD]").toString())
               .setManagementDnsZoneBinding(ManagementDnsZoneBinding.newBuilder().build())
               .setManagementDnsZoneBindingId("managementDnsZoneBindingId-288984082")
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           vmwareEngineClient.createManagementDnsZoneBindingCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateManagementDnsZoneBindingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.CreateManagementDnsZoneBindingRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createManagementDnsZoneBindingOperationCallable()
    
    
    public final OperationCallable<CreateManagementDnsZoneBindingRequest,ManagementDnsZoneBinding,OperationMetadata> createManagementDnsZoneBindingOperationCallable()

Creates a new `ManagementDnsZoneBinding` resource in a private cloud. This RPC creates the DNS binding and the resource that represents the DNS binding of the consumer VPC network to the management DNS zone. A management DNS zone is the Cloud DNS cross-project binding zone that VMware Engine creates for each private cloud. It contains FQDNs and corresponding IP addresses for the private cloud's ESXi hosts and management VM appliances like vCenter and NSX Manager.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       CreateManagementDnsZoneBindingRequest request =
           CreateManagementDnsZoneBindingRequest.newBuilder()
               .setParent(
                   PrivateCloudName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_CLOUD]").toString())
               .setManagementDnsZoneBinding(ManagementDnsZoneBinding.newBuilder().build())
               .setManagementDnsZoneBindingId("managementDnsZoneBindingId-288984082")
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<ManagementDnsZoneBinding, OperationMetadata> future =
           vmwareEngineClient.createManagementDnsZoneBindingOperationCallable().futureCall(request);
       // Do something.
       ManagementDnsZoneBinding response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateManagementDnsZoneBindingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.CreateManagementDnsZoneBindingRequest),[ManagementDnsZoneBinding](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.ManagementDnsZoneBinding),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.OperationMetadata)>` |   
  
### createNetworkPeeringAsync(@Nullable LocationName parent, NetworkPeering networkPeering, String networkPeeringId)
    
    
    public final OperationFuture<NetworkPeering,OperationMetadata> createNetworkPeeringAsync(@Nullable LocationName parent, NetworkPeering networkPeering, String networkPeeringId)

Creates a new network peering between the peer network and VMware Engine network provided in a `NetworkPeering` resource. NetworkPeering is a global resource and location can only be global.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       NetworkPeering networkPeering = NetworkPeering.newBuilder().build();
       String networkPeeringId = "networkPeeringId1321772525";
       NetworkPeering response =
           vmwareEngineClient
               .createNetworkPeeringAsync(parent, networkPeering, networkPeeringId)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.vmwareengine.v1.LocationName`  
Required. The resource name of the location to create the new network peering in. This value is always `global`, because `NetworkPeering` is a global resource. Resource names are schemeless URIs that follow the conventions in <https://cloud.google.com/apis/design/resource_names>. For example: `projects/my-project/locations/global`  
`networkPeering` | `[NetworkPeering](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.NetworkPeering)`  
Required. The initial description of the new network peering.  
`networkPeeringId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The user-provided identifier of the new `NetworkPeering`. This identifier must be unique among `NetworkPeering` resources within the parent and becomes the final token in the name URI. The identifier must meet the following requirements: 

  * Only contains 1-63 alphanumeric characters and hyphens 
  * Begins with an alphabetical character 
  * Ends with a non-hyphen character 
  * Not formatted as a UUID 
  * Complies with [RFC 1034](https://datatracker.ietf.org/doc/html/rfc1034) (section 3.5) 

  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[NetworkPeering](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.NetworkPeering),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.OperationMetadata)>` |   
  
### createNetworkPeeringAsync(CreateNetworkPeeringRequest request)
    
    
    public final OperationFuture<NetworkPeering,OperationMetadata> createNetworkPeeringAsync(CreateNetworkPeeringRequest request)

Creates a new network peering between the peer network and VMware Engine network provided in a `NetworkPeering` resource. NetworkPeering is a global resource and location can only be global.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       CreateNetworkPeeringRequest request =
           CreateNetworkPeeringRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setNetworkPeeringId("networkPeeringId1321772525")
               .setNetworkPeering(NetworkPeering.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       NetworkPeering response = vmwareEngineClient.createNetworkPeeringAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateNetworkPeeringRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.CreateNetworkPeeringRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[NetworkPeering](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.NetworkPeering),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.OperationMetadata)>` |   
  
### createNetworkPeeringAsync(String parent, NetworkPeering networkPeering, String networkPeeringId)
    
    
    public final OperationFuture<NetworkPeering,OperationMetadata> createNetworkPeeringAsync(String parent, NetworkPeering networkPeering, String networkPeeringId)

Creates a new network peering between the peer network and VMware Engine network provided in a `NetworkPeering` resource. NetworkPeering is a global resource and location can only be global.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       NetworkPeering networkPeering = NetworkPeering.newBuilder().build();
       String networkPeeringId = "networkPeeringId1321772525";
       NetworkPeering response =
           vmwareEngineClient
               .createNetworkPeeringAsync(parent, networkPeering, networkPeeringId)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the location to create the new network peering in. This value is always `global`, because `NetworkPeering` is a global resource. Resource names are schemeless URIs that follow the conventions in <https://cloud.google.com/apis/design/resource_names>. For example: `projects/my-project/locations/global`  
`networkPeering` | `[NetworkPeering](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.NetworkPeering)`  
Required. The initial description of the new network peering.  
`networkPeeringId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The user-provided identifier of the new `NetworkPeering`. This identifier must be unique among `NetworkPeering` resources within the parent and becomes the final token in the name URI. The identifier must meet the following requirements: 

  * Only contains 1-63 alphanumeric characters and hyphens 
  * Begins with an alphabetical character 
  * Ends with a non-hyphen character 
  * Not formatted as a UUID 
  * Complies with [RFC 1034](https://datatracker.ietf.org/doc/html/rfc1034) (section 3.5) 

  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[NetworkPeering](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.NetworkPeering),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.OperationMetadata)>` |   
  
### createNetworkPeeringCallable()
    
    
    public final UnaryCallable<CreateNetworkPeeringRequest,Operation> createNetworkPeeringCallable()

Creates a new network peering between the peer network and VMware Engine network provided in a `NetworkPeering` resource. NetworkPeering is a global resource and location can only be global.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       CreateNetworkPeeringRequest request =
           CreateNetworkPeeringRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setNetworkPeeringId("networkPeeringId1321772525")
               .setNetworkPeering(NetworkPeering.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           vmwareEngineClient.createNetworkPeeringCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateNetworkPeeringRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.CreateNetworkPeeringRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createNetworkPeeringOperationCallable()
    
    
    public final OperationCallable<CreateNetworkPeeringRequest,NetworkPeering,OperationMetadata> createNetworkPeeringOperationCallable()

Creates a new network peering between the peer network and VMware Engine network provided in a `NetworkPeering` resource. NetworkPeering is a global resource and location can only be global.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       CreateNetworkPeeringRequest request =
           CreateNetworkPeeringRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setNetworkPeeringId("networkPeeringId1321772525")
               .setNetworkPeering(NetworkPeering.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<NetworkPeering, OperationMetadata> future =
           vmwareEngineClient.createNetworkPeeringOperationCallable().futureCall(request);
       // Do something.
       NetworkPeering response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateNetworkPeeringRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.CreateNetworkPeeringRequest),[NetworkPeering](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.NetworkPeering),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.OperationMetadata)>` |   
  
### createNetworkPolicyAsync(@Nullable LocationName parent, NetworkPolicy networkPolicy, String networkPolicyId)
    
    
    public final OperationFuture<NetworkPolicy,OperationMetadata> createNetworkPolicyAsync(@Nullable LocationName parent, NetworkPolicy networkPolicy, String networkPolicyId)

Creates a new network policy in a given VMware Engine network of a project and location (region). A new network policy cannot be created if another network policy already exists in the same scope.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       NetworkPolicy networkPolicy = NetworkPolicy.newBuilder().build();
       String networkPolicyId = "networkPolicyId-727262661";
       NetworkPolicy response =
           vmwareEngineClient.createNetworkPolicyAsync(parent, networkPolicy, networkPolicyId).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.vmwareengine.v1.LocationName`  
Required. The resource name of the location (region) to create the new network policy in. Resource names are schemeless URIs that follow the conventions in <https://cloud.google.com/apis/design/resource_names>. For example: `projects/my-project/locations/us-central1`  
`networkPolicy` | `[NetworkPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.NetworkPolicy)`  
Required. The network policy configuration to use in the request.  
`networkPolicyId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The user-provided identifier of the network policy to be created. This identifier must be unique within parent `projects/{my-project}/locations/{us-central1}/networkPolicies` and becomes the final token in the name URI. The identifier must meet the following requirements: 

  * Only contains 1-63 alphanumeric characters and hyphens 
  * Begins with an alphabetical character 
  * Ends with a non-hyphen character 
  * Not formatted as a UUID 
  * Complies with [RFC 1034](https://datatracker.ietf.org/doc/html/rfc1034) (section 3.5) 

  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[NetworkPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.NetworkPolicy),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.OperationMetadata)>` |   
  
### createNetworkPolicyAsync(CreateNetworkPolicyRequest request)
    
    
    public final OperationFuture<NetworkPolicy,OperationMetadata> createNetworkPolicyAsync(CreateNetworkPolicyRequest request)

Creates a new network policy in a given VMware Engine network of a project and location (region). A new network policy cannot be created if another network policy already exists in the same scope.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       CreateNetworkPolicyRequest request =
           CreateNetworkPolicyRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setNetworkPolicyId("networkPolicyId-727262661")
               .setNetworkPolicy(NetworkPolicy.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       NetworkPolicy response = vmwareEngineClient.createNetworkPolicyAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateNetworkPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.CreateNetworkPolicyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[NetworkPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.NetworkPolicy),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.OperationMetadata)>` |   
  
### createNetworkPolicyAsync(String parent, NetworkPolicy networkPolicy, String networkPolicyId)
    
    
    public final OperationFuture<NetworkPolicy,OperationMetadata> createNetworkPolicyAsync(String parent, NetworkPolicy networkPolicy, String networkPolicyId)

Creates a new network policy in a given VMware Engine network of a project and location (region). A new network policy cannot be created if another network policy already exists in the same scope.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       NetworkPolicy networkPolicy = NetworkPolicy.newBuilder().build();
       String networkPolicyId = "networkPolicyId-727262661";
       NetworkPolicy response =
           vmwareEngineClient.createNetworkPolicyAsync(parent, networkPolicy, networkPolicyId).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the location (region) to create the new network policy in. Resource names are schemeless URIs that follow the conventions in <https://cloud.google.com/apis/design/resource_names>. For example: `projects/my-project/locations/us-central1`  
`networkPolicy` | `[NetworkPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.NetworkPolicy)`  
Required. The network policy configuration to use in the request.  
`networkPolicyId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The user-provided identifier of the network policy to be created. This identifier must be unique within parent `projects/{my-project}/locations/{us-central1}/networkPolicies` and becomes the final token in the name URI. The identifier must meet the following requirements: 

  * Only contains 1-63 alphanumeric characters and hyphens 
  * Begins with an alphabetical character 
  * Ends with a non-hyphen character 
  * Not formatted as a UUID 
  * Complies with [RFC 1034](https://datatracker.ietf.org/doc/html/rfc1034) (section 3.5) 

  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[NetworkPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.NetworkPolicy),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.OperationMetadata)>` |   
  
### createNetworkPolicyCallable()
    
    
    public final UnaryCallable<CreateNetworkPolicyRequest,Operation> createNetworkPolicyCallable()

Creates a new network policy in a given VMware Engine network of a project and location (region). A new network policy cannot be created if another network policy already exists in the same scope.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       CreateNetworkPolicyRequest request =
           CreateNetworkPolicyRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setNetworkPolicyId("networkPolicyId-727262661")
               .setNetworkPolicy(NetworkPolicy.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           vmwareEngineClient.createNetworkPolicyCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateNetworkPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.CreateNetworkPolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createNetworkPolicyOperationCallable()
    
    
    public final OperationCallable<CreateNetworkPolicyRequest,NetworkPolicy,OperationMetadata> createNetworkPolicyOperationCallable()

Creates a new network policy in a given VMware Engine network of a project and location (region). A new network policy cannot be created if another network policy already exists in the same scope.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       CreateNetworkPolicyRequest request =
           CreateNetworkPolicyRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setNetworkPolicyId("networkPolicyId-727262661")
               .setNetworkPolicy(NetworkPolicy.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<NetworkPolicy, OperationMetadata> future =
           vmwareEngineClient.createNetworkPolicyOperationCallable().futureCall(request);
       // Do something.
       NetworkPolicy response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateNetworkPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.CreateNetworkPolicyRequest),[NetworkPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.NetworkPolicy),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.OperationMetadata)>` |   
  
### createPrivateCloudAsync(@Nullable LocationName parent, PrivateCloud privateCloud, String privateCloudId)
    
    
    public final OperationFuture<PrivateCloud,OperationMetadata> createPrivateCloudAsync(@Nullable LocationName parent, PrivateCloud privateCloud, String privateCloudId)

Creates a new `PrivateCloud` resource in a given project and location. Private clouds of type `STANDARD` and `TIME_LIMITED` are zonal resources, `STRETCHED` private clouds are regional. Creating a private cloud also creates a [management cluster](https://cloud.google.com/vmware-engine/docs/concepts-vmware-components) for that private cloud.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       PrivateCloud privateCloud = PrivateCloud.newBuilder().build();
       String privateCloudId = "privateCloudId573896493";
       PrivateCloud response =
           vmwareEngineClient.createPrivateCloudAsync(parent, privateCloud, privateCloudId).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.vmwareengine.v1.LocationName`  
Required. The resource name of the location to create the new private cloud in. Resource names are schemeless URIs that follow the conventions in <https://cloud.google.com/apis/design/resource_names>. For example: `projects/my-project/locations/us-central1-a`  
`privateCloud` | `[PrivateCloud](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.PrivateCloud)`  
Required. The initial description of the new private cloud.  
`privateCloudId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The user-provided identifier of the private cloud to be created. This identifier must be unique among each `PrivateCloud` within the parent and becomes the final token in the name URI. The identifier must meet the following requirements: 

  * Only contains 1-63 alphanumeric characters and hyphens 
  * Begins with an alphabetical character 
  * Ends with a non-hyphen character 
  * Not formatted as a UUID 
  * Complies with [RFC 1034](https://datatracker.ietf.org/doc/html/rfc1034) (section 3.5) 

  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[PrivateCloud](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.PrivateCloud),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.OperationMetadata)>` |   
  
### createPrivateCloudAsync(CreatePrivateCloudRequest request)
    
    
    public final OperationFuture<PrivateCloud,OperationMetadata> createPrivateCloudAsync(CreatePrivateCloudRequest request)

Creates a new `PrivateCloud` resource in a given project and location. Private clouds of type `STANDARD` and `TIME_LIMITED` are zonal resources, `STRETCHED` private clouds are regional. Creating a private cloud also creates a [management cluster](https://cloud.google.com/vmware-engine/docs/concepts-vmware-components) for that private cloud.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       CreatePrivateCloudRequest request =
           CreatePrivateCloudRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPrivateCloudId("privateCloudId573896493")
               .setPrivateCloud(PrivateCloud.newBuilder().build())
               .setRequestId("requestId693933066")
               .setValidateOnly(true)
               .build();
       PrivateCloud response = vmwareEngineClient.createPrivateCloudAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreatePrivateCloudRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.CreatePrivateCloudRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[PrivateCloud](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.PrivateCloud),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.OperationMetadata)>` |   
  
### createPrivateCloudAsync(String parent, PrivateCloud privateCloud, String privateCloudId)
    
    
    public final OperationFuture<PrivateCloud,OperationMetadata> createPrivateCloudAsync(String parent, PrivateCloud privateCloud, String privateCloudId)

Creates a new `PrivateCloud` resource in a given project and location. Private clouds of type `STANDARD` and `TIME_LIMITED` are zonal resources, `STRETCHED` private clouds are regional. Creating a private cloud also creates a [management cluster](https://cloud.google.com/vmware-engine/docs/concepts-vmware-components) for that private cloud.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       PrivateCloud privateCloud = PrivateCloud.newBuilder().build();
       String privateCloudId = "privateCloudId573896493";
       PrivateCloud response =
           vmwareEngineClient.createPrivateCloudAsync(parent, privateCloud, privateCloudId).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the location to create the new private cloud in. Resource names are schemeless URIs that follow the conventions in <https://cloud.google.com/apis/design/resource_names>. For example: `projects/my-project/locations/us-central1-a`  
`privateCloud` | `[PrivateCloud](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.PrivateCloud)`  
Required. The initial description of the new private cloud.  
`privateCloudId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The user-provided identifier of the private cloud to be created. This identifier must be unique among each `PrivateCloud` within the parent and becomes the final token in the name URI. The identifier must meet the following requirements: 

  * Only contains 1-63 alphanumeric characters and hyphens 
  * Begins with an alphabetical character 
  * Ends with a non-hyphen character 
  * Not formatted as a UUID 
  * Complies with [RFC 1034](https://datatracker.ietf.org/doc/html/rfc1034) (section 3.5) 

  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[PrivateCloud](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.PrivateCloud),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.OperationMetadata)>` |   
  
### createPrivateCloudCallable()
    
    
    public final UnaryCallable<CreatePrivateCloudRequest,Operation> createPrivateCloudCallable()

Creates a new `PrivateCloud` resource in a given project and location. Private clouds of type `STANDARD` and `TIME_LIMITED` are zonal resources, `STRETCHED` private clouds are regional. Creating a private cloud also creates a [management cluster](https://cloud.google.com/vmware-engine/docs/concepts-vmware-components) for that private cloud.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       CreatePrivateCloudRequest request =
           CreatePrivateCloudRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPrivateCloudId("privateCloudId573896493")
               .setPrivateCloud(PrivateCloud.newBuilder().build())
               .setRequestId("requestId693933066")
               .setValidateOnly(true)
               .build();
       ApiFuture<Operation> future =
           vmwareEngineClient.createPrivateCloudCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreatePrivateCloudRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.CreatePrivateCloudRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createPrivateCloudOperationCallable()
    
    
    public final OperationCallable<CreatePrivateCloudRequest,PrivateCloud,OperationMetadata> createPrivateCloudOperationCallable()

Creates a new `PrivateCloud` resource in a given project and location. Private clouds of type `STANDARD` and `TIME_LIMITED` are zonal resources, `STRETCHED` private clouds are regional. Creating a private cloud also creates a [management cluster](https://cloud.google.com/vmware-engine/docs/concepts-vmware-components) for that private cloud.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       CreatePrivateCloudRequest request =
           CreatePrivateCloudRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPrivateCloudId("privateCloudId573896493")
               .setPrivateCloud(PrivateCloud.newBuilder().build())
               .setRequestId("requestId693933066")
               .setValidateOnly(true)
               .build();
       OperationFuture<PrivateCloud, OperationMetadata> future =
           vmwareEngineClient.createPrivateCloudOperationCallable().futureCall(request);
       // Do something.
       PrivateCloud response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreatePrivateCloudRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.CreatePrivateCloudRequest),[PrivateCloud](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.PrivateCloud),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.OperationMetadata)>` |   
  
### createPrivateConnectionAsync(@Nullable LocationName parent, PrivateConnection privateConnection, String privateConnectionId)
    
    
    public final OperationFuture<PrivateConnection,OperationMetadata> createPrivateConnectionAsync(@Nullable LocationName parent, PrivateConnection privateConnection, String privateConnectionId)

Creates a new private connection that can be used for accessing private Clouds.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       PrivateConnection privateConnection = PrivateConnection.newBuilder().build();
       String privateConnectionId = "privateConnectionId-1926654532";
       PrivateConnection response =
           vmwareEngineClient
               .createPrivateConnectionAsync(parent, privateConnection, privateConnectionId)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.vmwareengine.v1.LocationName`  
Required. The resource name of the location to create the new private connection in. Private connection is a regional resource. Resource names are schemeless URIs that follow the conventions in <https://cloud.google.com/apis/design/resource_names>. For example: `projects/my-project/locations/us-central1`  
`privateConnection` | `[PrivateConnection](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.PrivateConnection)`  
Required. The initial description of the new private connection.  
`privateConnectionId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The user-provided identifier of the new private connection. This identifier must be unique among private connection resources within the parent and becomes the final token in the name URI. The identifier must meet the following requirements: 

  * Only contains 1-63 alphanumeric characters and hyphens 
  * Begins with an alphabetical character 
  * Ends with a non-hyphen character 
  * Not formatted as a UUID 
  * Complies with [RFC 1034](https://datatracker.ietf.org/doc/html/rfc1034) (section 3.5) 

  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[PrivateConnection](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.PrivateConnection),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.OperationMetadata)>` |   
  
### createPrivateConnectionAsync(CreatePrivateConnectionRequest request)
    
    
    public final OperationFuture<PrivateConnection,OperationMetadata> createPrivateConnectionAsync(CreatePrivateConnectionRequest request)

Creates a new private connection that can be used for accessing private Clouds.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       CreatePrivateConnectionRequest request =
           CreatePrivateConnectionRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPrivateConnectionId("privateConnectionId-1926654532")
               .setPrivateConnection(PrivateConnection.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       PrivateConnection response = vmwareEngineClient.createPrivateConnectionAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreatePrivateConnectionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.CreatePrivateConnectionRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[PrivateConnection](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.PrivateConnection),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.OperationMetadata)>` |   
  
### createPrivateConnectionAsync(String parent, PrivateConnection privateConnection, String privateConnectionId)
    
    
    public final OperationFuture<PrivateConnection,OperationMetadata> createPrivateConnectionAsync(String parent, PrivateConnection privateConnection, String privateConnectionId)

Creates a new private connection that can be used for accessing private Clouds.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       PrivateConnection privateConnection = PrivateConnection.newBuilder().build();
       String privateConnectionId = "privateConnectionId-1926654532";
       PrivateConnection response =
           vmwareEngineClient
               .createPrivateConnectionAsync(parent, privateConnection, privateConnectionId)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the location to create the new private connection in. Private connection is a regional resource. Resource names are schemeless URIs that follow the conventions in <https://cloud.google.com/apis/design/resource_names>. For example: `projects/my-project/locations/us-central1`  
`privateConnection` | `[PrivateConnection](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.PrivateConnection)`  
Required. The initial description of the new private connection.  
`privateConnectionId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The user-provided identifier of the new private connection. This identifier must be unique among private connection resources within the parent and becomes the final token in the name URI. The identifier must meet the following requirements: 

  * Only contains 1-63 alphanumeric characters and hyphens 
  * Begins with an alphabetical character 
  * Ends with a non-hyphen character 
  * Not formatted as a UUID 
  * Complies with [RFC 1034](https://datatracker.ietf.org/doc/html/rfc1034) (section 3.5) 

  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[PrivateConnection](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.PrivateConnection),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.OperationMetadata)>` |   
  
### createPrivateConnectionCallable()
    
    
    public final UnaryCallable<CreatePrivateConnectionRequest,Operation> createPrivateConnectionCallable()

Creates a new private connection that can be used for accessing private Clouds.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       CreatePrivateConnectionRequest request =
           CreatePrivateConnectionRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPrivateConnectionId("privateConnectionId-1926654532")
               .setPrivateConnection(PrivateConnection.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           vmwareEngineClient.createPrivateConnectionCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreatePrivateConnectionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.CreatePrivateConnectionRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createPrivateConnectionOperationCallable()
    
    
    public final OperationCallable<CreatePrivateConnectionRequest,PrivateConnection,OperationMetadata> createPrivateConnectionOperationCallable()

Creates a new private connection that can be used for accessing private Clouds.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       CreatePrivateConnectionRequest request =
           CreatePrivateConnectionRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPrivateConnectionId("privateConnectionId-1926654532")
               .setPrivateConnection(PrivateConnection.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<PrivateConnection, OperationMetadata> future =
           vmwareEngineClient.createPrivateConnectionOperationCallable().futureCall(request);
       // Do something.
       PrivateConnection response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreatePrivateConnectionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.CreatePrivateConnectionRequest),[PrivateConnection](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.PrivateConnection),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.OperationMetadata)>` |   
  
### createVmwareEngineNetworkAsync(@Nullable LocationName parent, VmwareEngineNetwork vmwareEngineNetwork, String vmwareEngineNetworkId)
    
    
    public final OperationFuture<VmwareEngineNetwork,OperationMetadata> createVmwareEngineNetworkAsync(@Nullable LocationName parent, VmwareEngineNetwork vmwareEngineNetwork, String vmwareEngineNetworkId)

Creates a new VMware Engine network that can be used by a private cloud.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       VmwareEngineNetwork vmwareEngineNetwork = VmwareEngineNetwork.newBuilder().build();
       String vmwareEngineNetworkId = "vmwareEngineNetworkId532532083";
       VmwareEngineNetwork response =
           vmwareEngineClient
               .createVmwareEngineNetworkAsync(parent, vmwareEngineNetwork, vmwareEngineNetworkId)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.vmwareengine.v1.LocationName`  
Required. The resource name of the location to create the new VMware Engine network in. A VMware Engine network of type `LEGACY` is a regional resource, and a VMware Engine network of type `STANDARD` is a global resource. Resource names are schemeless URIs that follow the conventions in <https://cloud.google.com/apis/design/resource_names>. For example: `projects/my-project/locations/global`  
`vmwareEngineNetwork` | `[VmwareEngineNetwork](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.VmwareEngineNetwork)`  
Required. The initial description of the new VMware Engine network.  
`vmwareEngineNetworkId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The user-provided identifier of the new VMware Engine network. This identifier must be unique among VMware Engine network resources within the parent and becomes the final token in the name URI. The identifier must meet the following requirements: 

  * For networks of type LEGACY, adheres to the format: `{region-id}-default`. Replace `{region-id}` with the region where you want to create the VMware Engine network. For example, "us-central1-default". 
  * Only contains 1-63 alphanumeric characters and hyphens 
  * Begins with an alphabetical character 
  * Ends with a non-hyphen character 
  * Not formatted as a UUID 
  * Complies with [RFC 1034](https://datatracker.ietf.org/doc/html/rfc1034) (section 3.5) 

  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[VmwareEngineNetwork](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.VmwareEngineNetwork),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.OperationMetadata)>` |   
  
### createVmwareEngineNetworkAsync(CreateVmwareEngineNetworkRequest request)
    
    
    public final OperationFuture<VmwareEngineNetwork,OperationMetadata> createVmwareEngineNetworkAsync(CreateVmwareEngineNetworkRequest request)

Creates a new VMware Engine network that can be used by a private cloud.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       CreateVmwareEngineNetworkRequest request =
           CreateVmwareEngineNetworkRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setVmwareEngineNetworkId("vmwareEngineNetworkId532532083")
               .setVmwareEngineNetwork(VmwareEngineNetwork.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       VmwareEngineNetwork response =
           vmwareEngineClient.createVmwareEngineNetworkAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateVmwareEngineNetworkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.CreateVmwareEngineNetworkRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[VmwareEngineNetwork](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.VmwareEngineNetwork),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.OperationMetadata)>` |   
  
### createVmwareEngineNetworkAsync(String parent, VmwareEngineNetwork vmwareEngineNetwork, String vmwareEngineNetworkId)
    
    
    public final OperationFuture<VmwareEngineNetwork,OperationMetadata> createVmwareEngineNetworkAsync(String parent, VmwareEngineNetwork vmwareEngineNetwork, String vmwareEngineNetworkId)

Creates a new VMware Engine network that can be used by a private cloud.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       VmwareEngineNetwork vmwareEngineNetwork = VmwareEngineNetwork.newBuilder().build();
       String vmwareEngineNetworkId = "vmwareEngineNetworkId532532083";
       VmwareEngineNetwork response =
           vmwareEngineClient
               .createVmwareEngineNetworkAsync(parent, vmwareEngineNetwork, vmwareEngineNetworkId)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the location to create the new VMware Engine network in. A VMware Engine network of type `LEGACY` is a regional resource, and a VMware Engine network of type `STANDARD` is a global resource. Resource names are schemeless URIs that follow the conventions in <https://cloud.google.com/apis/design/resource_names>. For example: `projects/my-project/locations/global`  
`vmwareEngineNetwork` | `[VmwareEngineNetwork](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.VmwareEngineNetwork)`  
Required. The initial description of the new VMware Engine network.  
`vmwareEngineNetworkId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The user-provided identifier of the new VMware Engine network. This identifier must be unique among VMware Engine network resources within the parent and becomes the final token in the name URI. The identifier must meet the following requirements: 

  * For networks of type LEGACY, adheres to the format: `{region-id}-default`. Replace `{region-id}` with the region where you want to create the VMware Engine network. For example, "us-central1-default". 
  * Only contains 1-63 alphanumeric characters and hyphens 
  * Begins with an alphabetical character 
  * Ends with a non-hyphen character 
  * Not formatted as a UUID 
  * Complies with [RFC 1034](https://datatracker.ietf.org/doc/html/rfc1034) (section 3.5) 

  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[VmwareEngineNetwork](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.VmwareEngineNetwork),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.OperationMetadata)>` |   
  
### createVmwareEngineNetworkCallable()
    
    
    public final UnaryCallable<CreateVmwareEngineNetworkRequest,Operation> createVmwareEngineNetworkCallable()

Creates a new VMware Engine network that can be used by a private cloud.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       CreateVmwareEngineNetworkRequest request =
           CreateVmwareEngineNetworkRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setVmwareEngineNetworkId("vmwareEngineNetworkId532532083")
               .setVmwareEngineNetwork(VmwareEngineNetwork.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           vmwareEngineClient.createVmwareEngineNetworkCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateVmwareEngineNetworkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.CreateVmwareEngineNetworkRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createVmwareEngineNetworkOperationCallable()
    
    
    public final OperationCallable<CreateVmwareEngineNetworkRequest,VmwareEngineNetwork,OperationMetadata> createVmwareEngineNetworkOperationCallable()

Creates a new VMware Engine network that can be used by a private cloud.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       CreateVmwareEngineNetworkRequest request =
           CreateVmwareEngineNetworkRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setVmwareEngineNetworkId("vmwareEngineNetworkId532532083")
               .setVmwareEngineNetwork(VmwareEngineNetwork.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<VmwareEngineNetwork, OperationMetadata> future =
           vmwareEngineClient.createVmwareEngineNetworkOperationCallable().futureCall(request);
       // Do something.
       VmwareEngineNetwork response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateVmwareEngineNetworkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.CreateVmwareEngineNetworkRequest),[VmwareEngineNetwork](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.VmwareEngineNetwork),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.OperationMetadata)>` |   
  
### deleteClusterAsync(@Nullable ClusterName name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteClusterAsync(@Nullable ClusterName name)

Deletes a `Cluster` resource. To avoid unintended data loss, migrate or gracefully shut down any workloads running on the cluster before deletion. You cannot delete the management cluster of a private cloud using this method.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       ClusterName name = ClusterName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_CLOUD]", "[CLUSTER]");
       vmwareEngineClient.deleteClusterAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.vmwareengine.v1.ClusterName`  
Required. The resource name of the cluster to delete. Resource names are schemeless URIs that follow the conventions in <https://cloud.google.com/apis/design/resource_names>. For example: `projects/my-project/locations/us-central1-a/privateClouds/my-cloud/clusters/my-cluster`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.OperationMetadata)>` |   
  
### deleteClusterAsync(DeleteClusterRequest request)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteClusterAsync(DeleteClusterRequest request)

Deletes a `Cluster` resource. To avoid unintended data loss, migrate or gracefully shut down any workloads running on the cluster before deletion. You cannot delete the management cluster of a private cloud using this method.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       DeleteClusterRequest request =
           DeleteClusterRequest.newBuilder()
               .setName(
                   ClusterName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_CLOUD]", "[CLUSTER]")
                       .toString())
               .setRequestId("requestId693933066")
               .build();
       vmwareEngineClient.deleteClusterAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.DeleteClusterRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.OperationMetadata)>` |   
  
### deleteClusterAsync(String name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteClusterAsync(String name)

Deletes a `Cluster` resource. To avoid unintended data loss, migrate or gracefully shut down any workloads running on the cluster before deletion. You cannot delete the management cluster of a private cloud using this method.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       String name =
           ClusterName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_CLOUD]", "[CLUSTER]").toString();
       vmwareEngineClient.deleteClusterAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the cluster to delete. Resource names are schemeless URIs that follow the conventions in <https://cloud.google.com/apis/design/resource_names>. For example: `projects/my-project/locations/us-central1-a/privateClouds/my-cloud/clusters/my-cluster`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.OperationMetadata)>` |   
  
### deleteClusterCallable()
    
    
    public final UnaryCallable<DeleteClusterRequest,Operation> deleteClusterCallable()

Deletes a `Cluster` resource. To avoid unintended data loss, migrate or gracefully shut down any workloads running on the cluster before deletion. You cannot delete the management cluster of a private cloud using this method.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       DeleteClusterRequest request =
           DeleteClusterRequest.newBuilder()
               .setName(
                   ClusterName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_CLOUD]", "[CLUSTER]")
                       .toString())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future = vmwareEngineClient.deleteClusterCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.DeleteClusterRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteClusterOperationCallable()
    
    
    public final OperationCallable<DeleteClusterRequest,Empty,OperationMetadata> deleteClusterOperationCallable()

Deletes a `Cluster` resource. To avoid unintended data loss, migrate or gracefully shut down any workloads running on the cluster before deletion. You cannot delete the management cluster of a private cloud using this method.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       DeleteClusterRequest request =
           DeleteClusterRequest.newBuilder()
               .setName(
                   ClusterName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_CLOUD]", "[CLUSTER]")
                       .toString())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Empty, OperationMetadata> future =
           vmwareEngineClient.deleteClusterOperationCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.DeleteClusterRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.OperationMetadata)>` |   
  
### deleteExternalAccessRuleAsync(@Nullable ExternalAccessRuleName name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteExternalAccessRuleAsync(@Nullable ExternalAccessRuleName name)

Deletes a single external access rule.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       ExternalAccessRuleName name =
           ExternalAccessRuleName.of(
               "[PROJECT]", "[LOCATION]", "[NETWORK_POLICY]", "[EXTERNAL_ACCESS_RULE]");
       vmwareEngineClient.deleteExternalAccessRuleAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.vmwareengine.v1.ExternalAccessRuleName`  
Required. The resource name of the external access firewall rule to delete. Resource names are schemeless URIs that follow the conventions in <https://cloud.google.com/apis/design/resource_names>. For example: `projects/my-project/locations/us-central1/networkPolicies/my-policy/externalAccessRules/my-rule`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.OperationMetadata)>` |   
  
### deleteExternalAccessRuleAsync(DeleteExternalAccessRuleRequest request)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteExternalAccessRuleAsync(DeleteExternalAccessRuleRequest request)

Deletes a single external access rule.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       DeleteExternalAccessRuleRequest request =
           DeleteExternalAccessRuleRequest.newBuilder()
               .setName(
                   ExternalAccessRuleName.of(
                           "[PROJECT]", "[LOCATION]", "[NETWORK_POLICY]", "[EXTERNAL_ACCESS_RULE]")
                       .toString())
               .setRequestId("requestId693933066")
               .build();
       vmwareEngineClient.deleteExternalAccessRuleAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteExternalAccessRuleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.DeleteExternalAccessRuleRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.OperationMetadata)>` |   
  
### deleteExternalAccessRuleAsync(String name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteExternalAccessRuleAsync(String name)

Deletes a single external access rule.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       String name =
           ExternalAccessRuleName.of(
                   "[PROJECT]", "[LOCATION]", "[NETWORK_POLICY]", "[EXTERNAL_ACCESS_RULE]")
               .toString();
       vmwareEngineClient.deleteExternalAccessRuleAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the external access firewall rule to delete. Resource names are schemeless URIs that follow the conventions in <https://cloud.google.com/apis/design/resource_names>. For example: `projects/my-project/locations/us-central1/networkPolicies/my-policy/externalAccessRules/my-rule`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.OperationMetadata)>` |   
  
### deleteExternalAccessRuleCallable()
    
    
    public final UnaryCallable<DeleteExternalAccessRuleRequest,Operation> deleteExternalAccessRuleCallable()

Deletes a single external access rule.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       DeleteExternalAccessRuleRequest request =
           DeleteExternalAccessRuleRequest.newBuilder()
               .setName(
                   ExternalAccessRuleName.of(
                           "[PROJECT]", "[LOCATION]", "[NETWORK_POLICY]", "[EXTERNAL_ACCESS_RULE]")
                       .toString())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           vmwareEngineClient.deleteExternalAccessRuleCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteExternalAccessRuleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.DeleteExternalAccessRuleRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteExternalAccessRuleOperationCallable()
    
    
    public final OperationCallable<DeleteExternalAccessRuleRequest,Empty,OperationMetadata> deleteExternalAccessRuleOperationCallable()

Deletes a single external access rule.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       DeleteExternalAccessRuleRequest request =
           DeleteExternalAccessRuleRequest.newBuilder()
               .setName(
                   ExternalAccessRuleName.of(
                           "[PROJECT]", "[LOCATION]", "[NETWORK_POLICY]", "[EXTERNAL_ACCESS_RULE]")
                       .toString())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Empty, OperationMetadata> future =
           vmwareEngineClient.deleteExternalAccessRuleOperationCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteExternalAccessRuleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.DeleteExternalAccessRuleRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.OperationMetadata)>` |   
  
### deleteExternalAddressAsync(@Nullable ExternalAddressName name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteExternalAddressAsync(@Nullable ExternalAddressName name)

Deletes a single external IP address. When you delete an external IP address, connectivity between the external IP address and the corresponding internal IP address is lost.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       ExternalAddressName name =
           ExternalAddressName.of(
               "[PROJECT]", "[LOCATION]", "[PRIVATE_CLOUD]", "[EXTERNAL_ADDRESS]");
       vmwareEngineClient.deleteExternalAddressAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.vmwareengine.v1.ExternalAddressName`  
Required. The resource name of the external IP address to delete. Resource names are schemeless URIs that follow the conventions in <https://cloud.google.com/apis/design/resource_names>. For example: `projects/my-project/locations/us-central1-a/privateClouds/my-cloud/externalAddresses/my-ip`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.OperationMetadata)>` |   
  
### deleteExternalAddressAsync(DeleteExternalAddressRequest request)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteExternalAddressAsync(DeleteExternalAddressRequest request)

Deletes a single external IP address. When you delete an external IP address, connectivity between the external IP address and the corresponding internal IP address is lost.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       DeleteExternalAddressRequest request =
           DeleteExternalAddressRequest.newBuilder()
               .setName(
                   ExternalAddressName.of(
                           "[PROJECT]", "[LOCATION]", "[PRIVATE_CLOUD]", "[EXTERNAL_ADDRESS]")
                       .toString())
               .setRequestId("requestId693933066")
               .build();
       vmwareEngineClient.deleteExternalAddressAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteExternalAddressRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.DeleteExternalAddressRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.OperationMetadata)>` |   
  
### deleteExternalAddressAsync(String name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteExternalAddressAsync(String name)

Deletes a single external IP address. When you delete an external IP address, connectivity between the external IP address and the corresponding internal IP address is lost.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       String name =
           ExternalAddressName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_CLOUD]", "[EXTERNAL_ADDRESS]")
               .toString();
       vmwareEngineClient.deleteExternalAddressAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the external IP address to delete. Resource names are schemeless URIs that follow the conventions in <https://cloud.google.com/apis/design/resource_names>. For example: `projects/my-project/locations/us-central1-a/privateClouds/my-cloud/externalAddresses/my-ip`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.OperationMetadata)>` |   
  
### deleteExternalAddressCallable()
    
    
    public final UnaryCallable<DeleteExternalAddressRequest,Operation> deleteExternalAddressCallable()

Deletes a single external IP address. When you delete an external IP address, connectivity between the external IP address and the corresponding internal IP address is lost.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       DeleteExternalAddressRequest request =
           DeleteExternalAddressRequest.newBuilder()
               .setName(
                   ExternalAddressName.of(
                           "[PROJECT]", "[LOCATION]", "[PRIVATE_CLOUD]", "[EXTERNAL_ADDRESS]")
                       .toString())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           vmwareEngineClient.deleteExternalAddressCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteExternalAddressRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.DeleteExternalAddressRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteExternalAddressOperationCallable()
    
    
    public final OperationCallable<DeleteExternalAddressRequest,Empty,OperationMetadata> deleteExternalAddressOperationCallable()

Deletes a single external IP address. When you delete an external IP address, connectivity between the external IP address and the corresponding internal IP address is lost.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       DeleteExternalAddressRequest request =
           DeleteExternalAddressRequest.newBuilder()
               .setName(
                   ExternalAddressName.of(
                           "[PROJECT]", "[LOCATION]", "[PRIVATE_CLOUD]", "[EXTERNAL_ADDRESS]")
                       .toString())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Empty, OperationMetadata> future =
           vmwareEngineClient.deleteExternalAddressOperationCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteExternalAddressRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.DeleteExternalAddressRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.OperationMetadata)>` |   
  
### deleteLoggingServerAsync(@Nullable LoggingServerName name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteLoggingServerAsync(@Nullable LoggingServerName name)

Deletes a single logging server.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       LoggingServerName name =
           LoggingServerName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_CLOUD]", "[LOGGING_SERVER]");
       vmwareEngineClient.deleteLoggingServerAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.vmwareengine.v1.LoggingServerName`  
Required. The resource name of the logging server to delete. Resource names are schemeless URIs that follow the conventions in <https://cloud.google.com/apis/design/resource_names>. For example: `projects/my-project/locations/us-central1-a/privateClouds/my-cloud/loggingServers/my-logging-server`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.OperationMetadata)>` |   
  
### deleteLoggingServerAsync(DeleteLoggingServerRequest request)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteLoggingServerAsync(DeleteLoggingServerRequest request)

Deletes a single logging server.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       DeleteLoggingServerRequest request =
           DeleteLoggingServerRequest.newBuilder()
               .setName(
                   LoggingServerName.of(
                           "[PROJECT]", "[LOCATION]", "[PRIVATE_CLOUD]", "[LOGGING_SERVER]")
                       .toString())
               .setRequestId("requestId693933066")
               .build();
       vmwareEngineClient.deleteLoggingServerAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteLoggingServerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.DeleteLoggingServerRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.OperationMetadata)>` |   
  
### deleteLoggingServerAsync(String name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteLoggingServerAsync(String name)

Deletes a single logging server.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       String name =
           LoggingServerName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_CLOUD]", "[LOGGING_SERVER]")
               .toString();
       vmwareEngineClient.deleteLoggingServerAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the logging server to delete. Resource names are schemeless URIs that follow the conventions in <https://cloud.google.com/apis/design/resource_names>. For example: `projects/my-project/locations/us-central1-a/privateClouds/my-cloud/loggingServers/my-logging-server`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.OperationMetadata)>` |   
  
### deleteLoggingServerCallable()
    
    
    public final UnaryCallable<DeleteLoggingServerRequest,Operation> deleteLoggingServerCallable()

Deletes a single logging server.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       DeleteLoggingServerRequest request =
           DeleteLoggingServerRequest.newBuilder()
               .setName(
                   LoggingServerName.of(
                           "[PROJECT]", "[LOCATION]", "[PRIVATE_CLOUD]", "[LOGGING_SERVER]")
                       .toString())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           vmwareEngineClient.deleteLoggingServerCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteLoggingServerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.DeleteLoggingServerRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteLoggingServerOperationCallable()
    
    
    public final OperationCallable<DeleteLoggingServerRequest,Empty,OperationMetadata> deleteLoggingServerOperationCallable()

Deletes a single logging server.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       DeleteLoggingServerRequest request =
           DeleteLoggingServerRequest.newBuilder()
               .setName(
                   LoggingServerName.of(
                           "[PROJECT]", "[LOCATION]", "[PRIVATE_CLOUD]", "[LOGGING_SERVER]")
                       .toString())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Empty, OperationMetadata> future =
           vmwareEngineClient.deleteLoggingServerOperationCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteLoggingServerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.DeleteLoggingServerRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.OperationMetadata)>` |   
  
### deleteManagementDnsZoneBindingAsync(@Nullable ManagementDnsZoneBindingName name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteManagementDnsZoneBindingAsync(@Nullable ManagementDnsZoneBindingName name)

Deletes a `ManagementDnsZoneBinding` resource. When a management DNS zone binding is deleted, the corresponding consumer VPC network is no longer bound to the management DNS zone.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       ManagementDnsZoneBindingName name =
           ManagementDnsZoneBindingName.of(
               "[PROJECT]", "[LOCATION]", "[PRIVATE_CLOUD]", "[MANAGEMENT_DNS_ZONE_BINDING]");
       vmwareEngineClient.deleteManagementDnsZoneBindingAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.vmwareengine.v1.ManagementDnsZoneBindingName`  
Required. The resource name of the management DNS zone binding to delete. Resource names are schemeless URIs that follow the conventions in <https://cloud.google.com/apis/design/resource_names>. For example: `projects/my-project/locations/us-central1-a/privateClouds/my-cloud/managementDnsZoneBindings/my-management-dns-zone-binding`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.OperationMetadata)>` |   
  
### deleteManagementDnsZoneBindingAsync(DeleteManagementDnsZoneBindingRequest request)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteManagementDnsZoneBindingAsync(DeleteManagementDnsZoneBindingRequest request)

Deletes a `ManagementDnsZoneBinding` resource. When a management DNS zone binding is deleted, the corresponding consumer VPC network is no longer bound to the management DNS zone.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       DeleteManagementDnsZoneBindingRequest request =
           DeleteManagementDnsZoneBindingRequest.newBuilder()
               .setName(
                   ManagementDnsZoneBindingName.of(
                           "[PROJECT]",
                           "[LOCATION]",
                           "[PRIVATE_CLOUD]",
                           "[MANAGEMENT_DNS_ZONE_BINDING]")
                       .toString())
               .setRequestId("requestId693933066")
               .build();
       vmwareEngineClient.deleteManagementDnsZoneBindingAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteManagementDnsZoneBindingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.DeleteManagementDnsZoneBindingRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.OperationMetadata)>` |   
  
### deleteManagementDnsZoneBindingAsync(String name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteManagementDnsZoneBindingAsync(String name)

Deletes a `ManagementDnsZoneBinding` resource. When a management DNS zone binding is deleted, the corresponding consumer VPC network is no longer bound to the management DNS zone.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       String name =
           ManagementDnsZoneBindingName.of(
                   "[PROJECT]", "[LOCATION]", "[PRIVATE_CLOUD]", "[MANAGEMENT_DNS_ZONE_BINDING]")
               .toString();
       vmwareEngineClient.deleteManagementDnsZoneBindingAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the management DNS zone binding to delete. Resource names are schemeless URIs that follow the conventions in <https://cloud.google.com/apis/design/resource_names>. For example: `projects/my-project/locations/us-central1-a/privateClouds/my-cloud/managementDnsZoneBindings/my-management-dns-zone-binding`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.OperationMetadata)>` |   
  
### deleteManagementDnsZoneBindingCallable()
    
    
    public final UnaryCallable<DeleteManagementDnsZoneBindingRequest,Operation> deleteManagementDnsZoneBindingCallable()

Deletes a `ManagementDnsZoneBinding` resource. When a management DNS zone binding is deleted, the corresponding consumer VPC network is no longer bound to the management DNS zone.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       DeleteManagementDnsZoneBindingRequest request =
           DeleteManagementDnsZoneBindingRequest.newBuilder()
               .setName(
                   ManagementDnsZoneBindingName.of(
                           "[PROJECT]",
                           "[LOCATION]",
                           "[PRIVATE_CLOUD]",
                           "[MANAGEMENT_DNS_ZONE_BINDING]")
                       .toString())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           vmwareEngineClient.deleteManagementDnsZoneBindingCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteManagementDnsZoneBindingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.DeleteManagementDnsZoneBindingRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteManagementDnsZoneBindingOperationCallable()
    
    
    public final OperationCallable<DeleteManagementDnsZoneBindingRequest,Empty,OperationMetadata> deleteManagementDnsZoneBindingOperationCallable()

Deletes a `ManagementDnsZoneBinding` resource. When a management DNS zone binding is deleted, the corresponding consumer VPC network is no longer bound to the management DNS zone.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       DeleteManagementDnsZoneBindingRequest request =
           DeleteManagementDnsZoneBindingRequest.newBuilder()
               .setName(
                   ManagementDnsZoneBindingName.of(
                           "[PROJECT]",
                           "[LOCATION]",
                           "[PRIVATE_CLOUD]",
                           "[MANAGEMENT_DNS_ZONE_BINDING]")
                       .toString())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Empty, OperationMetadata> future =
           vmwareEngineClient.deleteManagementDnsZoneBindingOperationCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteManagementDnsZoneBindingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.DeleteManagementDnsZoneBindingRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.OperationMetadata)>` |   
  
### deleteNetworkPeeringAsync(@Nullable NetworkPeeringName name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteNetworkPeeringAsync(@Nullable NetworkPeeringName name)

Deletes a `NetworkPeering` resource. When a network peering is deleted for a VMware Engine network, the peer network becomes inaccessible to that VMware Engine network. NetworkPeering is a global resource and location can only be global.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       NetworkPeeringName name =
           NetworkPeeringName.of("[PROJECT]", "[LOCATION]", "[NETWORK_PEERING]");
       vmwareEngineClient.deleteNetworkPeeringAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.vmwareengine.v1.NetworkPeeringName`  
Required. The resource name of the network peering to be deleted. Resource names are schemeless URIs that follow the conventions in <https://cloud.google.com/apis/design/resource_names>. For example: `projects/my-project/locations/global/networkPeerings/my-peering`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.OperationMetadata)>` |   
  
### deleteNetworkPeeringAsync(DeleteNetworkPeeringRequest request)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteNetworkPeeringAsync(DeleteNetworkPeeringRequest request)

Deletes a `NetworkPeering` resource. When a network peering is deleted for a VMware Engine network, the peer network becomes inaccessible to that VMware Engine network. NetworkPeering is a global resource and location can only be global.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       DeleteNetworkPeeringRequest request =
           DeleteNetworkPeeringRequest.newBuilder()
               .setName(
                   NetworkPeeringName.of("[PROJECT]", "[LOCATION]", "[NETWORK_PEERING]").toString())
               .setRequestId("requestId693933066")
               .build();
       vmwareEngineClient.deleteNetworkPeeringAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteNetworkPeeringRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.DeleteNetworkPeeringRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.OperationMetadata)>` |   
  
### deleteNetworkPeeringAsync(String name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteNetworkPeeringAsync(String name)

Deletes a `NetworkPeering` resource. When a network peering is deleted for a VMware Engine network, the peer network becomes inaccessible to that VMware Engine network. NetworkPeering is a global resource and location can only be global.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       String name =
           NetworkPeeringName.of("[PROJECT]", "[LOCATION]", "[NETWORK_PEERING]").toString();
       vmwareEngineClient.deleteNetworkPeeringAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the network peering to be deleted. Resource names are schemeless URIs that follow the conventions in <https://cloud.google.com/apis/design/resource_names>. For example: `projects/my-project/locations/global/networkPeerings/my-peering`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.OperationMetadata)>` |   
  
### deleteNetworkPeeringCallable()
    
    
    public final UnaryCallable<DeleteNetworkPeeringRequest,Operation> deleteNetworkPeeringCallable()

Deletes a `NetworkPeering` resource. When a network peering is deleted for a VMware Engine network, the peer network becomes inaccessible to that VMware Engine network. NetworkPeering is a global resource and location can only be global.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       DeleteNetworkPeeringRequest request =
           DeleteNetworkPeeringRequest.newBuilder()
               .setName(
                   NetworkPeeringName.of("[PROJECT]", "[LOCATION]", "[NETWORK_PEERING]").toString())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           vmwareEngineClient.deleteNetworkPeeringCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteNetworkPeeringRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.DeleteNetworkPeeringRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteNetworkPeeringOperationCallable()
    
    
    public final OperationCallable<DeleteNetworkPeeringRequest,Empty,OperationMetadata> deleteNetworkPeeringOperationCallable()

Deletes a `NetworkPeering` resource. When a network peering is deleted for a VMware Engine network, the peer network becomes inaccessible to that VMware Engine network. NetworkPeering is a global resource and location can only be global.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       DeleteNetworkPeeringRequest request =
           DeleteNetworkPeeringRequest.newBuilder()
               .setName(
                   NetworkPeeringName.of("[PROJECT]", "[LOCATION]", "[NETWORK_PEERING]").toString())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Empty, OperationMetadata> future =
           vmwareEngineClient.deleteNetworkPeeringOperationCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteNetworkPeeringRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.DeleteNetworkPeeringRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.OperationMetadata)>` |   
  
### deleteNetworkPolicyAsync(@Nullable NetworkPolicyName name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteNetworkPolicyAsync(@Nullable NetworkPolicyName name)

Deletes a `NetworkPolicy` resource. A network policy cannot be deleted when `NetworkService.state` is set to `RECONCILING` for either its external IP or internet access service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       NetworkPolicyName name = NetworkPolicyName.of("[PROJECT]", "[LOCATION]", "[NETWORK_POLICY]");
       vmwareEngineClient.deleteNetworkPolicyAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.vmwareengine.v1.NetworkPolicyName`  
Required. The resource name of the network policy to delete. Resource names are schemeless URIs that follow the conventions in <https://cloud.google.com/apis/design/resource_names>. For example: `projects/my-project/locations/us-central1/networkPolicies/my-network-policy`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.OperationMetadata)>` |   
  
### deleteNetworkPolicyAsync(DeleteNetworkPolicyRequest request)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteNetworkPolicyAsync(DeleteNetworkPolicyRequest request)

Deletes a `NetworkPolicy` resource. A network policy cannot be deleted when `NetworkService.state` is set to `RECONCILING` for either its external IP or internet access service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       DeleteNetworkPolicyRequest request =
           DeleteNetworkPolicyRequest.newBuilder()
               .setName(
                   NetworkPolicyName.of("[PROJECT]", "[LOCATION]", "[NETWORK_POLICY]").toString())
               .setRequestId("requestId693933066")
               .build();
       vmwareEngineClient.deleteNetworkPolicyAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteNetworkPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.DeleteNetworkPolicyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.OperationMetadata)>` |   
  
### deleteNetworkPolicyAsync(String name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteNetworkPolicyAsync(String name)

Deletes a `NetworkPolicy` resource. A network policy cannot be deleted when `NetworkService.state` is set to `RECONCILING` for either its external IP or internet access service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       String name = NetworkPolicyName.of("[PROJECT]", "[LOCATION]", "[NETWORK_POLICY]").toString();
       vmwareEngineClient.deleteNetworkPolicyAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the network policy to delete. Resource names are schemeless URIs that follow the conventions in <https://cloud.google.com/apis/design/resource_names>. For example: `projects/my-project/locations/us-central1/networkPolicies/my-network-policy`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.OperationMetadata)>` |   
  
### deleteNetworkPolicyCallable()
    
    
    public final UnaryCallable<DeleteNetworkPolicyRequest,Operation> deleteNetworkPolicyCallable()

Deletes a `NetworkPolicy` resource. A network policy cannot be deleted when `NetworkService.state` is set to `RECONCILING` for either its external IP or internet access service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       DeleteNetworkPolicyRequest request =
           DeleteNetworkPolicyRequest.newBuilder()
               .setName(
                   NetworkPolicyName.of("[PROJECT]", "[LOCATION]", "[NETWORK_POLICY]").toString())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           vmwareEngineClient.deleteNetworkPolicyCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteNetworkPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.DeleteNetworkPolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteNetworkPolicyOperationCallable()
    
    
    public final OperationCallable<DeleteNetworkPolicyRequest,Empty,OperationMetadata> deleteNetworkPolicyOperationCallable()

Deletes a `NetworkPolicy` resource. A network policy cannot be deleted when `NetworkService.state` is set to `RECONCILING` for either its external IP or internet access service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       DeleteNetworkPolicyRequest request =
           DeleteNetworkPolicyRequest.newBuilder()
               .setName(
                   NetworkPolicyName.of("[PROJECT]", "[LOCATION]", "[NETWORK_POLICY]").toString())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Empty, OperationMetadata> future =
           vmwareEngineClient.deleteNetworkPolicyOperationCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteNetworkPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.DeleteNetworkPolicyRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.OperationMetadata)>` |   
  
### deletePrivateCloudAsync(@Nullable PrivateCloudName name)
    
    
    public final OperationFuture<PrivateCloud,OperationMetadata> deletePrivateCloudAsync(@Nullable PrivateCloudName name)

Schedules a `PrivateCloud` resource for deletion.

A `PrivateCloud` resource scheduled for deletion has `PrivateCloud.state` set to `DELETED` and `expireTime` set to the time when deletion is final and can no longer be reversed. The delete operation is marked as done as soon as the `PrivateCloud` is successfully scheduled for deletion (this also applies when `delayHours` is set to zero), and the operation is not kept in pending state until `PrivateCloud` is purged. `PrivateCloud` can be restored using `UndeletePrivateCloud` method before the `expireTime` elapses. When `expireTime` is reached, deletion is final and all private cloud resources are irreversibly removed and billing stops. During the final removal process, `PrivateCloud.state` is set to `PURGING`. `PrivateCloud` can be polled using standard `GET` method for the whole period of deletion and purging. It will not be returned only when it is completely purged.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       PrivateCloudName name = PrivateCloudName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_CLOUD]");
       PrivateCloud response = vmwareEngineClient.deletePrivateCloudAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.vmwareengine.v1.PrivateCloudName`  
Required. The resource name of the private cloud to delete. Resource names are schemeless URIs that follow the conventions in <https://cloud.google.com/apis/design/resource_names>. For example: `projects/my-project/locations/us-central1-a/privateClouds/my-cloud`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[PrivateCloud](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.PrivateCloud),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.OperationMetadata)>` |   
  
### deletePrivateCloudAsync(DeletePrivateCloudRequest request)
    
    
    public final OperationFuture<PrivateCloud,OperationMetadata> deletePrivateCloudAsync(DeletePrivateCloudRequest request)

Schedules a `PrivateCloud` resource for deletion.

A `PrivateCloud` resource scheduled for deletion has `PrivateCloud.state` set to `DELETED` and `expireTime` set to the time when deletion is final and can no longer be reversed. The delete operation is marked as done as soon as the `PrivateCloud` is successfully scheduled for deletion (this also applies when `delayHours` is set to zero), and the operation is not kept in pending state until `PrivateCloud` is purged. `PrivateCloud` can be restored using `UndeletePrivateCloud` method before the `expireTime` elapses. When `expireTime` is reached, deletion is final and all private cloud resources are irreversibly removed and billing stops. During the final removal process, `PrivateCloud.state` is set to `PURGING`. `PrivateCloud` can be polled using standard `GET` method for the whole period of deletion and purging. It will not be returned only when it is completely purged.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       DeletePrivateCloudRequest request =
           DeletePrivateCloudRequest.newBuilder()
               .setName(PrivateCloudName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_CLOUD]").toString())
               .setRequestId("requestId693933066")
               .setForce(true)
               .setDelayHours(475821395)
               .build();
       PrivateCloud response = vmwareEngineClient.deletePrivateCloudAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeletePrivateCloudRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.DeletePrivateCloudRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[PrivateCloud](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.PrivateCloud),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.OperationMetadata)>` |   
  
### deletePrivateCloudAsync(String name)
    
    
    public final OperationFuture<PrivateCloud,OperationMetadata> deletePrivateCloudAsync(String name)

Schedules a `PrivateCloud` resource for deletion.

A `PrivateCloud` resource scheduled for deletion has `PrivateCloud.state` set to `DELETED` and `expireTime` set to the time when deletion is final and can no longer be reversed. The delete operation is marked as done as soon as the `PrivateCloud` is successfully scheduled for deletion (this also applies when `delayHours` is set to zero), and the operation is not kept in pending state until `PrivateCloud` is purged. `PrivateCloud` can be restored using `UndeletePrivateCloud` method before the `expireTime` elapses. When `expireTime` is reached, deletion is final and all private cloud resources are irreversibly removed and billing stops. During the final removal process, `PrivateCloud.state` is set to `PURGING`. `PrivateCloud` can be polled using standard `GET` method for the whole period of deletion and purging. It will not be returned only when it is completely purged.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       String name = PrivateCloudName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_CLOUD]").toString();
       PrivateCloud response = vmwareEngineClient.deletePrivateCloudAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the private cloud to delete. Resource names are schemeless URIs that follow the conventions in <https://cloud.google.com/apis/design/resource_names>. For example: `projects/my-project/locations/us-central1-a/privateClouds/my-cloud`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[PrivateCloud](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.PrivateCloud),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.OperationMetadata)>` |   
  
### deletePrivateCloudCallable()
    
    
    public final UnaryCallable<DeletePrivateCloudRequest,Operation> deletePrivateCloudCallable()

Schedules a `PrivateCloud` resource for deletion.

A `PrivateCloud` resource scheduled for deletion has `PrivateCloud.state` set to `DELETED` and `expireTime` set to the time when deletion is final and can no longer be reversed. The delete operation is marked as done as soon as the `PrivateCloud` is successfully scheduled for deletion (this also applies when `delayHours` is set to zero), and the operation is not kept in pending state until `PrivateCloud` is purged. `PrivateCloud` can be restored using `UndeletePrivateCloud` method before the `expireTime` elapses. When `expireTime` is reached, deletion is final and all private cloud resources are irreversibly removed and billing stops. During the final removal process, `PrivateCloud.state` is set to `PURGING`. `PrivateCloud` can be polled using standard `GET` method for the whole period of deletion and purging. It will not be returned only when it is completely purged.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       DeletePrivateCloudRequest request =
           DeletePrivateCloudRequest.newBuilder()
               .setName(PrivateCloudName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_CLOUD]").toString())
               .setRequestId("requestId693933066")
               .setForce(true)
               .setDelayHours(475821395)
               .build();
       ApiFuture<Operation> future =
           vmwareEngineClient.deletePrivateCloudCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeletePrivateCloudRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.DeletePrivateCloudRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deletePrivateCloudOperationCallable()
    
    
    public final OperationCallable<DeletePrivateCloudRequest,PrivateCloud,OperationMetadata> deletePrivateCloudOperationCallable()

Schedules a `PrivateCloud` resource for deletion.

A `PrivateCloud` resource scheduled for deletion has `PrivateCloud.state` set to `DELETED` and `expireTime` set to the time when deletion is final and can no longer be reversed. The delete operation is marked as done as soon as the `PrivateCloud` is successfully scheduled for deletion (this also applies when `delayHours` is set to zero), and the operation is not kept in pending state until `PrivateCloud` is purged. `PrivateCloud` can be restored using `UndeletePrivateCloud` method before the `expireTime` elapses. When `expireTime` is reached, deletion is final and all private cloud resources are irreversibly removed and billing stops. During the final removal process, `PrivateCloud.state` is set to `PURGING`. `PrivateCloud` can be polled using standard `GET` method for the whole period of deletion and purging. It will not be returned only when it is completely purged.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       DeletePrivateCloudRequest request =
           DeletePrivateCloudRequest.newBuilder()
               .setName(PrivateCloudName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_CLOUD]").toString())
               .setRequestId("requestId693933066")
               .setForce(true)
               .setDelayHours(475821395)
               .build();
       OperationFuture<PrivateCloud, OperationMetadata> future =
           vmwareEngineClient.deletePrivateCloudOperationCallable().futureCall(request);
       // Do something.
       PrivateCloud response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeletePrivateCloudRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.DeletePrivateCloudRequest),[PrivateCloud](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.PrivateCloud),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.OperationMetadata)>` |   
  
### deletePrivateConnectionAsync(@Nullable PrivateConnectionName name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deletePrivateConnectionAsync(@Nullable PrivateConnectionName name)

Deletes a `PrivateConnection` resource. When a private connection is deleted for a VMware Engine network, the connected network becomes inaccessible to that VMware Engine network.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       PrivateConnectionName name =
           PrivateConnectionName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_CONNECTION]");
       vmwareEngineClient.deletePrivateConnectionAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.vmwareengine.v1.PrivateConnectionName`  
Required. The resource name of the private connection to be deleted. Resource names are schemeless URIs that follow the conventions in <https://cloud.google.com/apis/design/resource_names>. For example: `projects/my-project/locations/us-central1/privateConnections/my-connection`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.OperationMetadata)>` |   
  
### deletePrivateConnectionAsync(DeletePrivateConnectionRequest request)
    
    
    public final OperationFuture<Empty,OperationMetadata> deletePrivateConnectionAsync(DeletePrivateConnectionRequest request)

Deletes a `PrivateConnection` resource. When a private connection is deleted for a VMware Engine network, the connected network becomes inaccessible to that VMware Engine network.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       DeletePrivateConnectionRequest request =
           DeletePrivateConnectionRequest.newBuilder()
               .setName(
                   PrivateConnectionName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_CONNECTION]")
                       .toString())
               .setRequestId("requestId693933066")
               .build();
       vmwareEngineClient.deletePrivateConnectionAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeletePrivateConnectionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.DeletePrivateConnectionRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.OperationMetadata)>` |   
  
### deletePrivateConnectionAsync(String name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deletePrivateConnectionAsync(String name)

Deletes a `PrivateConnection` resource. When a private connection is deleted for a VMware Engine network, the connected network becomes inaccessible to that VMware Engine network.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       String name =
           PrivateConnectionName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_CONNECTION]").toString();
       vmwareEngineClient.deletePrivateConnectionAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the private connection to be deleted. Resource names are schemeless URIs that follow the conventions in <https://cloud.google.com/apis/design/resource_names>. For example: `projects/my-project/locations/us-central1/privateConnections/my-connection`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.OperationMetadata)>` |   
  
### deletePrivateConnectionCallable()
    
    
    public final UnaryCallable<DeletePrivateConnectionRequest,Operation> deletePrivateConnectionCallable()

Deletes a `PrivateConnection` resource. When a private connection is deleted for a VMware Engine network, the connected network becomes inaccessible to that VMware Engine network.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       DeletePrivateConnectionRequest request =
           DeletePrivateConnectionRequest.newBuilder()
               .setName(
                   PrivateConnectionName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_CONNECTION]")
                       .toString())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           vmwareEngineClient.deletePrivateConnectionCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeletePrivateConnectionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.DeletePrivateConnectionRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deletePrivateConnectionOperationCallable()
    
    
    public final OperationCallable<DeletePrivateConnectionRequest,Empty,OperationMetadata> deletePrivateConnectionOperationCallable()

Deletes a `PrivateConnection` resource. When a private connection is deleted for a VMware Engine network, the connected network becomes inaccessible to that VMware Engine network.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       DeletePrivateConnectionRequest request =
           DeletePrivateConnectionRequest.newBuilder()
               .setName(
                   PrivateConnectionName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_CONNECTION]")
                       .toString())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Empty, OperationMetadata> future =
           vmwareEngineClient.deletePrivateConnectionOperationCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeletePrivateConnectionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.DeletePrivateConnectionRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.OperationMetadata)>` |   
  
### deleteVmwareEngineNetworkAsync(@Nullable VmwareEngineNetworkName name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteVmwareEngineNetworkAsync(@Nullable VmwareEngineNetworkName name)

Deletes a `VmwareEngineNetwork` resource. You can only delete a VMware Engine network after all resources that refer to it are deleted. For example, a private cloud, a network peering, and a network policy can all refer to the same VMware Engine network.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       VmwareEngineNetworkName name =
           VmwareEngineNetworkName.of("[PROJECT]", "[LOCATION]", "[VMWARE_ENGINE_NETWORK]");
       vmwareEngineClient.deleteVmwareEngineNetworkAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.vmwareengine.v1.VmwareEngineNetworkName`  
Required. The resource name of the VMware Engine network to be deleted. Resource names are schemeless URIs that follow the conventions in <https://cloud.google.com/apis/design/resource_names>. For example: `projects/my-project/locations/global/vmwareEngineNetworks/my-network`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.OperationMetadata)>` |   
  
### deleteVmwareEngineNetworkAsync(DeleteVmwareEngineNetworkRequest request)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteVmwareEngineNetworkAsync(DeleteVmwareEngineNetworkRequest request)

Deletes a `VmwareEngineNetwork` resource. You can only delete a VMware Engine network after all resources that refer to it are deleted. For example, a private cloud, a network peering, and a network policy can all refer to the same VMware Engine network.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       DeleteVmwareEngineNetworkRequest request =
           DeleteVmwareEngineNetworkRequest.newBuilder()
               .setName(
                   VmwareEngineNetworkName.of("[PROJECT]", "[LOCATION]", "[VMWARE_ENGINE_NETWORK]")
                       .toString())
               .setRequestId("requestId693933066")
               .setEtag("etag3123477")
               .build();
       vmwareEngineClient.deleteVmwareEngineNetworkAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteVmwareEngineNetworkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.DeleteVmwareEngineNetworkRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.OperationMetadata)>` |   
  
### deleteVmwareEngineNetworkAsync(String name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteVmwareEngineNetworkAsync(String name)

Deletes a `VmwareEngineNetwork` resource. You can only delete a VMware Engine network after all resources that refer to it are deleted. For example, a private cloud, a network peering, and a network policy can all refer to the same VMware Engine network.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       String name =
           VmwareEngineNetworkName.of("[PROJECT]", "[LOCATION]", "[VMWARE_ENGINE_NETWORK]")
               .toString();
       vmwareEngineClient.deleteVmwareEngineNetworkAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the VMware Engine network to be deleted. Resource names are schemeless URIs that follow the conventions in <https://cloud.google.com/apis/design/resource_names>. For example: `projects/my-project/locations/global/vmwareEngineNetworks/my-network`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.OperationMetadata)>` |   
  
### deleteVmwareEngineNetworkCallable()
    
    
    public final UnaryCallable<DeleteVmwareEngineNetworkRequest,Operation> deleteVmwareEngineNetworkCallable()

Deletes a `VmwareEngineNetwork` resource. You can only delete a VMware Engine network after all resources that refer to it are deleted. For example, a private cloud, a network peering, and a network policy can all refer to the same VMware Engine network.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       DeleteVmwareEngineNetworkRequest request =
           DeleteVmwareEngineNetworkRequest.newBuilder()
               .setName(
                   VmwareEngineNetworkName.of("[PROJECT]", "[LOCATION]", "[VMWARE_ENGINE_NETWORK]")
                       .toString())
               .setRequestId("requestId693933066")
               .setEtag("etag3123477")
               .build();
       ApiFuture<Operation> future =
           vmwareEngineClient.deleteVmwareEngineNetworkCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteVmwareEngineNetworkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.DeleteVmwareEngineNetworkRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteVmwareEngineNetworkOperationCallable()
    
    
    public final OperationCallable<DeleteVmwareEngineNetworkRequest,Empty,OperationMetadata> deleteVmwareEngineNetworkOperationCallable()

Deletes a `VmwareEngineNetwork` resource. You can only delete a VMware Engine network after all resources that refer to it are deleted. For example, a private cloud, a network peering, and a network policy can all refer to the same VMware Engine network.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       DeleteVmwareEngineNetworkRequest request =
           DeleteVmwareEngineNetworkRequest.newBuilder()
               .setName(
                   VmwareEngineNetworkName.of("[PROJECT]", "[LOCATION]", "[VMWARE_ENGINE_NETWORK]")
                       .toString())
               .setRequestId("requestId693933066")
               .setEtag("etag3123477")
               .build();
       OperationFuture<Empty, OperationMetadata> future =
           vmwareEngineClient.deleteVmwareEngineNetworkOperationCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteVmwareEngineNetworkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.DeleteVmwareEngineNetworkRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.OperationMetadata)>` |   
  
### fetchNetworkPolicyExternalAddresses(@Nullable NetworkPolicyName networkPolicy)
    
    
    public final VmwareEngineClient.FetchNetworkPolicyExternalAddressesPagedResponse fetchNetworkPolicyExternalAddresses(@Nullable NetworkPolicyName networkPolicy)

Lists external IP addresses assigned to VMware workload VMs within the scope of the given network policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       NetworkPolicyName networkPolicy =
           NetworkPolicyName.of("[PROJECT]", "[LOCATION]", "[NETWORK_POLICY]");
       for (ExternalAddress element :
           vmwareEngineClient.fetchNetworkPolicyExternalAddresses(networkPolicy).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`networkPolicy` | `@org.jspecify.annotations.Nullable com.google.cloud.vmwareengine.v1.NetworkPolicyName`  
Required. The resource name of the network policy to query for assigned external IP addresses. Resource names are schemeless URIs that follow the conventions in <https://cloud.google.com/apis/design/resource_names>. For example: `projects/my-project/locations/us-central1/networkPolicies/my-policy`  
**Returns**  
---  
**Type** | **Description**  
`[VmwareEngineClient.FetchNetworkPolicyExternalAddressesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.VmwareEngineClient.FetchNetworkPolicyExternalAddressesPagedResponse)` |   
  
### fetchNetworkPolicyExternalAddresses(FetchNetworkPolicyExternalAddressesRequest request)
    
    
    public final VmwareEngineClient.FetchNetworkPolicyExternalAddressesPagedResponse fetchNetworkPolicyExternalAddresses(FetchNetworkPolicyExternalAddressesRequest request)

Lists external IP addresses assigned to VMware workload VMs within the scope of the given network policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       FetchNetworkPolicyExternalAddressesRequest request =
           FetchNetworkPolicyExternalAddressesRequest.newBuilder()
               .setNetworkPolicy(
                   NetworkPolicyName.of("[PROJECT]", "[LOCATION]", "[NETWORK_POLICY]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (ExternalAddress element :
           vmwareEngineClient.fetchNetworkPolicyExternalAddresses(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[FetchNetworkPolicyExternalAddressesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.FetchNetworkPolicyExternalAddressesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[VmwareEngineClient.FetchNetworkPolicyExternalAddressesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.VmwareEngineClient.FetchNetworkPolicyExternalAddressesPagedResponse)` |   
  
### fetchNetworkPolicyExternalAddresses(String networkPolicy)
    
    
    public final VmwareEngineClient.FetchNetworkPolicyExternalAddressesPagedResponse fetchNetworkPolicyExternalAddresses(String networkPolicy)

Lists external IP addresses assigned to VMware workload VMs within the scope of the given network policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       String networkPolicy =
           NetworkPolicyName.of("[PROJECT]", "[LOCATION]", "[NETWORK_POLICY]").toString();
       for (ExternalAddress element :
           vmwareEngineClient.fetchNetworkPolicyExternalAddresses(networkPolicy).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`networkPolicy` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the network policy to query for assigned external IP addresses. Resource names are schemeless URIs that follow the conventions in <https://cloud.google.com/apis/design/resource_names>. For example: `projects/my-project/locations/us-central1/networkPolicies/my-policy`  
**Returns**  
---  
**Type** | **Description**  
`[VmwareEngineClient.FetchNetworkPolicyExternalAddressesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.VmwareEngineClient.FetchNetworkPolicyExternalAddressesPagedResponse)` |   
  
### fetchNetworkPolicyExternalAddressesCallable()
    
    
    public final UnaryCallable<FetchNetworkPolicyExternalAddressesRequest,FetchNetworkPolicyExternalAddressesResponse> fetchNetworkPolicyExternalAddressesCallable()

Lists external IP addresses assigned to VMware workload VMs within the scope of the given network policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       FetchNetworkPolicyExternalAddressesRequest request =
           FetchNetworkPolicyExternalAddressesRequest.newBuilder()
               .setNetworkPolicy(
                   NetworkPolicyName.of("[PROJECT]", "[LOCATION]", "[NETWORK_POLICY]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         FetchNetworkPolicyExternalAddressesResponse response =
             vmwareEngineClient.fetchNetworkPolicyExternalAddressesCallable().call(request);
         for (ExternalAddress element : response.getExternalAddressesList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[FetchNetworkPolicyExternalAddressesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.FetchNetworkPolicyExternalAddressesRequest),[FetchNetworkPolicyExternalAddressesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.FetchNetworkPolicyExternalAddressesResponse)>` |   
  
### fetchNetworkPolicyExternalAddressesPagedCallable()
    
    
    public final UnaryCallable<FetchNetworkPolicyExternalAddressesRequest,VmwareEngineClient.FetchNetworkPolicyExternalAddressesPagedResponse> fetchNetworkPolicyExternalAddressesPagedCallable()

Lists external IP addresses assigned to VMware workload VMs within the scope of the given network policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       FetchNetworkPolicyExternalAddressesRequest request =
           FetchNetworkPolicyExternalAddressesRequest.newBuilder()
               .setNetworkPolicy(
                   NetworkPolicyName.of("[PROJECT]", "[LOCATION]", "[NETWORK_POLICY]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<ExternalAddress> future =
           vmwareEngineClient.fetchNetworkPolicyExternalAddressesPagedCallable().futureCall(request);
       // Do something.
       for (ExternalAddress element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[FetchNetworkPolicyExternalAddressesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.FetchNetworkPolicyExternalAddressesRequest),[FetchNetworkPolicyExternalAddressesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.VmwareEngineClient.FetchNetworkPolicyExternalAddressesPagedResponse)>` |   
  
### getCluster(@Nullable ClusterName name)
    
    
    public final Cluster getCluster(@Nullable ClusterName name)

Retrieves a `Cluster` resource by its resource name.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       ClusterName name = ClusterName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_CLOUD]", "[CLUSTER]");
       Cluster response = vmwareEngineClient.getCluster(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.vmwareengine.v1.ClusterName`  
Required. The cluster resource name to retrieve. Resource names are schemeless URIs that follow the conventions in <https://cloud.google.com/apis/design/resource_names>. For example: `projects/my-project/locations/us-central1-a/privateClouds/my-cloud/clusters/my-cluster`  
**Returns**  
---  
**Type** | **Description**  
`[Cluster](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.Cluster)` |   
  
### getCluster(GetClusterRequest request)
    
    
    public final Cluster getCluster(GetClusterRequest request)

Retrieves a `Cluster` resource by its resource name.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       GetClusterRequest request =
           GetClusterRequest.newBuilder()
               .setName(
                   ClusterName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_CLOUD]", "[CLUSTER]")
                       .toString())
               .build();
       Cluster response = vmwareEngineClient.getCluster(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.GetClusterRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Cluster](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.Cluster)` |   
  
### getCluster(String name)
    
    
    public final Cluster getCluster(String name)

Retrieves a `Cluster` resource by its resource name.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       String name =
           ClusterName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_CLOUD]", "[CLUSTER]").toString();
       Cluster response = vmwareEngineClient.getCluster(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The cluster resource name to retrieve. Resource names are schemeless URIs that follow the conventions in <https://cloud.google.com/apis/design/resource_names>. For example: `projects/my-project/locations/us-central1-a/privateClouds/my-cloud/clusters/my-cluster`  
**Returns**  
---  
**Type** | **Description**  
`[Cluster](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.Cluster)` |   
  
### getClusterCallable()
    
    
    public final UnaryCallable<GetClusterRequest,Cluster> getClusterCallable()

Retrieves a `Cluster` resource by its resource name.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       GetClusterRequest request =
           GetClusterRequest.newBuilder()
               .setName(
                   ClusterName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_CLOUD]", "[CLUSTER]")
                       .toString())
               .build();
       ApiFuture<Cluster> future = vmwareEngineClient.getClusterCallable().futureCall(request);
       // Do something.
       Cluster response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.GetClusterRequest),[Cluster](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.Cluster)>` |   
  
### getDnsBindPermission(@Nullable DnsBindPermissionName name)
    
    
    public final DnsBindPermission getDnsBindPermission(@Nullable DnsBindPermissionName name)

Gets all the principals having bind permission on the intranet VPC associated with the consumer project granted by the Grant API. DnsBindPermission is a global resource and location can only be global.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       DnsBindPermissionName name = DnsBindPermissionName.of("[PROJECT]", "[LOCATION]");
       DnsBindPermission response = vmwareEngineClient.getDnsBindPermission(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.vmwareengine.v1.DnsBindPermissionName`  
Required. The name of the resource which stores the users/service accounts having the permission to bind to the corresponding intranet VPC of the consumer project. DnsBindPermission is a global resource. Resource names are schemeless URIs that follow the conventions in <https://cloud.google.com/apis/design/resource_names>. For example: `projects/my-project/locations/global/dnsBindPermission`  
**Returns**  
---  
**Type** | **Description**  
`[DnsBindPermission](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.DnsBindPermission)` |   
  
### getDnsBindPermission(GetDnsBindPermissionRequest request)
    
    
    public final DnsBindPermission getDnsBindPermission(GetDnsBindPermissionRequest request)

Gets all the principals having bind permission on the intranet VPC associated with the consumer project granted by the Grant API. DnsBindPermission is a global resource and location can only be global.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       GetDnsBindPermissionRequest request =
           GetDnsBindPermissionRequest.newBuilder()
               .setName(DnsBindPermissionName.of("[PROJECT]", "[LOCATION]").toString())
               .build();
       DnsBindPermission response = vmwareEngineClient.getDnsBindPermission(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetDnsBindPermissionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.GetDnsBindPermissionRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[DnsBindPermission](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.DnsBindPermission)` |   
  
### getDnsBindPermission(String name)
    
    
    public final DnsBindPermission getDnsBindPermission(String name)

Gets all the principals having bind permission on the intranet VPC associated with the consumer project granted by the Grant API. DnsBindPermission is a global resource and location can only be global.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       String name = DnsBindPermissionName.of("[PROJECT]", "[LOCATION]").toString();
       DnsBindPermission response = vmwareEngineClient.getDnsBindPermission(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the resource which stores the users/service accounts having the permission to bind to the corresponding intranet VPC of the consumer project. DnsBindPermission is a global resource. Resource names are schemeless URIs that follow the conventions in <https://cloud.google.com/apis/design/resource_names>. For example: `projects/my-project/locations/global/dnsBindPermission`  
**Returns**  
---  
**Type** | **Description**  
`[DnsBindPermission](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.DnsBindPermission)` |   
  
### getDnsBindPermissionCallable()
    
    
    public final UnaryCallable<GetDnsBindPermissionRequest,DnsBindPermission> getDnsBindPermissionCallable()

Gets all the principals having bind permission on the intranet VPC associated with the consumer project granted by the Grant API. DnsBindPermission is a global resource and location can only be global.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       GetDnsBindPermissionRequest request =
           GetDnsBindPermissionRequest.newBuilder()
               .setName(DnsBindPermissionName.of("[PROJECT]", "[LOCATION]").toString())
               .build();
       ApiFuture<DnsBindPermission> future =
           vmwareEngineClient.getDnsBindPermissionCallable().futureCall(request);
       // Do something.
       DnsBindPermission response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetDnsBindPermissionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.GetDnsBindPermissionRequest),[DnsBindPermission](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.DnsBindPermission)>` |   
  
### getDnsForwarding(@Nullable DnsForwardingName name)
    
    
    public final DnsForwarding getDnsForwarding(@Nullable DnsForwardingName name)

Gets details of the `DnsForwarding` config.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       DnsForwardingName name = DnsForwardingName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_CLOUD]");
       DnsForwarding response = vmwareEngineClient.getDnsForwarding(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.vmwareengine.v1.DnsForwardingName`  
Required. The resource name of a `DnsForwarding` to retrieve. Resource names are schemeless URIs that follow the conventions in <https://cloud.google.com/apis/design/resource_names>. For example: `projects/my-project/locations/us-central1-a/privateClouds/my-cloud/dnsForwarding`  
**Returns**  
---  
**Type** | **Description**  
`[DnsForwarding](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.DnsForwarding)` |   
  
### getDnsForwarding(GetDnsForwardingRequest request)
    
    
    public final DnsForwarding getDnsForwarding(GetDnsForwardingRequest request)

Gets details of the `DnsForwarding` config.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       GetDnsForwardingRequest request =
           GetDnsForwardingRequest.newBuilder()
               .setName(
                   DnsForwardingName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_CLOUD]").toString())
               .build();
       DnsForwarding response = vmwareEngineClient.getDnsForwarding(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetDnsForwardingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.GetDnsForwardingRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[DnsForwarding](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.DnsForwarding)` |   
  
### getDnsForwarding(String name)
    
    
    public final DnsForwarding getDnsForwarding(String name)

Gets details of the `DnsForwarding` config.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       String name = DnsForwardingName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_CLOUD]").toString();
       DnsForwarding response = vmwareEngineClient.getDnsForwarding(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of a `DnsForwarding` to retrieve. Resource names are schemeless URIs that follow the conventions in <https://cloud.google.com/apis/design/resource_names>. For example: `projects/my-project/locations/us-central1-a/privateClouds/my-cloud/dnsForwarding`  
**Returns**  
---  
**Type** | **Description**  
`[DnsForwarding](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.DnsForwarding)` |   
  
### getDnsForwardingCallable()
    
    
    public final UnaryCallable<GetDnsForwardingRequest,DnsForwarding> getDnsForwardingCallable()

Gets details of the `DnsForwarding` config.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       GetDnsForwardingRequest request =
           GetDnsForwardingRequest.newBuilder()
               .setName(
                   DnsForwardingName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_CLOUD]").toString())
               .build();
       ApiFuture<DnsForwarding> future =
           vmwareEngineClient.getDnsForwardingCallable().futureCall(request);
       // Do something.
       DnsForwarding response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetDnsForwardingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.GetDnsForwardingRequest),[DnsForwarding](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.DnsForwarding)>` |   
  
### getExternalAccessRule(@Nullable ExternalAccessRuleName name)
    
    
    public final ExternalAccessRule getExternalAccessRule(@Nullable ExternalAccessRuleName name)

Gets details of a single external access rule.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       ExternalAccessRuleName name =
           ExternalAccessRuleName.of(
               "[PROJECT]", "[LOCATION]", "[NETWORK_POLICY]", "[EXTERNAL_ACCESS_RULE]");
       ExternalAccessRule response = vmwareEngineClient.getExternalAccessRule(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.vmwareengine.v1.ExternalAccessRuleName`  
Required. The resource name of the external access firewall rule to retrieve. Resource names are schemeless URIs that follow the conventions in <https://cloud.google.com/apis/design/resource_names>. For example: `projects/my-project/locations/us-central1/networkPolicies/my-policy/externalAccessRules/my-rule`  
**Returns**  
---  
**Type** | **Description**  
`[ExternalAccessRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.ExternalAccessRule)` |   
  
### getExternalAccessRule(GetExternalAccessRuleRequest request)
    
    
    public final ExternalAccessRule getExternalAccessRule(GetExternalAccessRuleRequest request)

Gets details of a single external access rule.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       GetExternalAccessRuleRequest request =
           GetExternalAccessRuleRequest.newBuilder()
               .setName(
                   ExternalAccessRuleName.of(
                           "[PROJECT]", "[LOCATION]", "[NETWORK_POLICY]", "[EXTERNAL_ACCESS_RULE]")
                       .toString())
               .build();
       ExternalAccessRule response = vmwareEngineClient.getExternalAccessRule(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetExternalAccessRuleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.GetExternalAccessRuleRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ExternalAccessRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.ExternalAccessRule)` |   
  
### getExternalAccessRule(String name)
    
    
    public final ExternalAccessRule getExternalAccessRule(String name)

Gets details of a single external access rule.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       String name =
           ExternalAccessRuleName.of(
                   "[PROJECT]", "[LOCATION]", "[NETWORK_POLICY]", "[EXTERNAL_ACCESS_RULE]")
               .toString();
       ExternalAccessRule response = vmwareEngineClient.getExternalAccessRule(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the external access firewall rule to retrieve. Resource names are schemeless URIs that follow the conventions in <https://cloud.google.com/apis/design/resource_names>. For example: `projects/my-project/locations/us-central1/networkPolicies/my-policy/externalAccessRules/my-rule`  
**Returns**  
---  
**Type** | **Description**  
`[ExternalAccessRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.ExternalAccessRule)` |   
  
### getExternalAccessRuleCallable()
    
    
    public final UnaryCallable<GetExternalAccessRuleRequest,ExternalAccessRule> getExternalAccessRuleCallable()

Gets details of a single external access rule.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       GetExternalAccessRuleRequest request =
           GetExternalAccessRuleRequest.newBuilder()
               .setName(
                   ExternalAccessRuleName.of(
                           "[PROJECT]", "[LOCATION]", "[NETWORK_POLICY]", "[EXTERNAL_ACCESS_RULE]")
                       .toString())
               .build();
       ApiFuture<ExternalAccessRule> future =
           vmwareEngineClient.getExternalAccessRuleCallable().futureCall(request);
       // Do something.
       ExternalAccessRule response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetExternalAccessRuleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.GetExternalAccessRuleRequest),[ExternalAccessRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.ExternalAccessRule)>` |   
  
### getExternalAddress(@Nullable ExternalAddressName name)
    
    
    public final ExternalAddress getExternalAddress(@Nullable ExternalAddressName name)

Gets details of a single external IP address.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       ExternalAddressName name =
           ExternalAddressName.of(
               "[PROJECT]", "[LOCATION]", "[PRIVATE_CLOUD]", "[EXTERNAL_ADDRESS]");
       ExternalAddress response = vmwareEngineClient.getExternalAddress(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.vmwareengine.v1.ExternalAddressName`  
Required. The resource name of the external IP address to retrieve. Resource names are schemeless URIs that follow the conventions in <https://cloud.google.com/apis/design/resource_names>. For example: `projects/my-project/locations/us-central1-a/privateClouds/my-cloud/externalAddresses/my-ip`  
**Returns**  
---  
**Type** | **Description**  
`[ExternalAddress](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.ExternalAddress)` |   
  
### getExternalAddress(GetExternalAddressRequest request)
    
    
    public final ExternalAddress getExternalAddress(GetExternalAddressRequest request)

Gets details of a single external IP address.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       GetExternalAddressRequest request =
           GetExternalAddressRequest.newBuilder()
               .setName(
                   ExternalAddressName.of(
                           "[PROJECT]", "[LOCATION]", "[PRIVATE_CLOUD]", "[EXTERNAL_ADDRESS]")
                       .toString())
               .build();
       ExternalAddress response = vmwareEngineClient.getExternalAddress(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetExternalAddressRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.GetExternalAddressRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ExternalAddress](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.ExternalAddress)` |   
  
### getExternalAddress(String name)
    
    
    public final ExternalAddress getExternalAddress(String name)

Gets details of a single external IP address.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       String name =
           ExternalAddressName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_CLOUD]", "[EXTERNAL_ADDRESS]")
               .toString();
       ExternalAddress response = vmwareEngineClient.getExternalAddress(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the external IP address to retrieve. Resource names are schemeless URIs that follow the conventions in <https://cloud.google.com/apis/design/resource_names>. For example: `projects/my-project/locations/us-central1-a/privateClouds/my-cloud/externalAddresses/my-ip`  
**Returns**  
---  
**Type** | **Description**  
`[ExternalAddress](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.ExternalAddress)` |   
  
### getExternalAddressCallable()
    
    
    public final UnaryCallable<GetExternalAddressRequest,ExternalAddress> getExternalAddressCallable()

Gets details of a single external IP address.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       GetExternalAddressRequest request =
           GetExternalAddressRequest.newBuilder()
               .setName(
                   ExternalAddressName.of(
                           "[PROJECT]", "[LOCATION]", "[PRIVATE_CLOUD]", "[EXTERNAL_ADDRESS]")
                       .toString())
               .build();
       ApiFuture<ExternalAddress> future =
           vmwareEngineClient.getExternalAddressCallable().futureCall(request);
       // Do something.
       ExternalAddress response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetExternalAddressRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.GetExternalAddressRequest),[ExternalAddress](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.ExternalAddress)>` |   
  
### getHcxActivationKey(@Nullable HcxActivationKeyName name)
    
    
    public final HcxActivationKey getHcxActivationKey(@Nullable HcxActivationKeyName name)

Retrieves a `HcxActivationKey` resource by its resource name.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       HcxActivationKeyName name =
           HcxActivationKeyName.of(
               "[PROJECT]", "[LOCATION]", "[PRIVATE_CLOUD]", "[HCX_ACTIVATION_KEY]");
       HcxActivationKey response = vmwareEngineClient.getHcxActivationKey(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.vmwareengine.v1.HcxActivationKeyName`  
Required. The resource name of the HCX activation key to retrieve. Resource names are schemeless URIs that follow the conventions in <https://cloud.google.com/apis/design/resource_names>. For example: `projects/my-project/locations/us-central1/privateClouds/my-cloud/hcxActivationKeys/my-key`  
**Returns**  
---  
**Type** | **Description**  
`[HcxActivationKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.HcxActivationKey)` |   
  
### getHcxActivationKey(GetHcxActivationKeyRequest request)
    
    
    public final HcxActivationKey getHcxActivationKey(GetHcxActivationKeyRequest request)

Retrieves a `HcxActivationKey` resource by its resource name.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       GetHcxActivationKeyRequest request =
           GetHcxActivationKeyRequest.newBuilder()
               .setName(
                   HcxActivationKeyName.of(
                           "[PROJECT]", "[LOCATION]", "[PRIVATE_CLOUD]", "[HCX_ACTIVATION_KEY]")
                       .toString())
               .build();
       HcxActivationKey response = vmwareEngineClient.getHcxActivationKey(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetHcxActivationKeyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.GetHcxActivationKeyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[HcxActivationKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.HcxActivationKey)` |   
  
### getHcxActivationKey(String name)
    
    
    public final HcxActivationKey getHcxActivationKey(String name)

Retrieves a `HcxActivationKey` resource by its resource name.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       String name =
           HcxActivationKeyName.of(
                   "[PROJECT]", "[LOCATION]", "[PRIVATE_CLOUD]", "[HCX_ACTIVATION_KEY]")
               .toString();
       HcxActivationKey response = vmwareEngineClient.getHcxActivationKey(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the HCX activation key to retrieve. Resource names are schemeless URIs that follow the conventions in <https://cloud.google.com/apis/design/resource_names>. For example: `projects/my-project/locations/us-central1/privateClouds/my-cloud/hcxActivationKeys/my-key`  
**Returns**  
---  
**Type** | **Description**  
`[HcxActivationKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.HcxActivationKey)` |   
  
### getHcxActivationKeyCallable()
    
    
    public final UnaryCallable<GetHcxActivationKeyRequest,HcxActivationKey> getHcxActivationKeyCallable()

Retrieves a `HcxActivationKey` resource by its resource name.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       GetHcxActivationKeyRequest request =
           GetHcxActivationKeyRequest.newBuilder()
               .setName(
                   HcxActivationKeyName.of(
                           "[PROJECT]", "[LOCATION]", "[PRIVATE_CLOUD]", "[HCX_ACTIVATION_KEY]")
                       .toString())
               .build();
       ApiFuture<HcxActivationKey> future =
           vmwareEngineClient.getHcxActivationKeyCallable().futureCall(request);
       // Do something.
       HcxActivationKey response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetHcxActivationKeyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.GetHcxActivationKeyRequest),[HcxActivationKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.HcxActivationKey)>` |   
  
### getHttpJsonOperationsClient()
    
    
    public final OperationsClient getHttpJsonOperationsClient()

**Beta**

This feature is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the launch stage descriptions.

Returns the OperationsClient that can be used to query the status of a long-running operation returned by another API method call.

**Returns**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.httpjson.longrunning.OperationsClient.html)` |   
  
### getIamPolicy(GetIamPolicyRequest request)
    
    
    public final Policy getIamPolicy(GetIamPolicyRequest request)

Gets the access control policy for a resource. Returns an empty policyif the resource exists and does not have a policy set.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       GetIamPolicyRequest request =
           GetIamPolicyRequest.newBuilder()
               .setResource(
                   ClusterName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_CLOUD]", "[CLUSTER]")
                       .toString())
               .setOptions(GetPolicyOptions.newBuilder().build())
               .build();
       Policy response = vmwareEngineClient.getIamPolicy(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `com.google.iam.v1.GetIamPolicyRequest`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`com.google.iam.v1.Policy` |   
  
### getIamPolicyCallable()
    
    
    public final UnaryCallable<GetIamPolicyRequest,Policy> getIamPolicyCallable()

Gets the access control policy for a resource. Returns an empty policyif the resource exists and does not have a policy set.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       GetIamPolicyRequest request =
           GetIamPolicyRequest.newBuilder()
               .setResource(
                   ClusterName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_CLOUD]", "[CLUSTER]")
                       .toString())
               .setOptions(GetPolicyOptions.newBuilder().build())
               .build();
       ApiFuture<Policy> future = vmwareEngineClient.getIamPolicyCallable().futureCall(request);
       // Do something.
       Policy response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.iam.v1.GetIamPolicyRequest,com.google.iam.v1.Policy>` |   
  
### getLocation(GetLocationRequest request)
    
    
    public final Location getLocation(GetLocationRequest request)

Gets information about a location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       Location response = vmwareEngineClient.getLocation(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `com.google.cloud.location.GetLocationRequest`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`com.google.cloud.location.Location` |   
  
### getLocationCallable()
    
    
    public final UnaryCallable<GetLocationRequest,Location> getLocationCallable()

Gets information about a location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       ApiFuture<Location> future = vmwareEngineClient.getLocationCallable().futureCall(request);
       // Do something.
       Location response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.GetLocationRequest,com.google.cloud.location.Location>` |   
  
### getLoggingServer(@Nullable LoggingServerName name)
    
    
    public final LoggingServer getLoggingServer(@Nullable LoggingServerName name)

Gets details of a logging server.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       LoggingServerName name =
           LoggingServerName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_CLOUD]", "[LOGGING_SERVER]");
       LoggingServer response = vmwareEngineClient.getLoggingServer(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.vmwareengine.v1.LoggingServerName`  
Required. The resource name of the Logging Server to retrieve. Resource names are schemeless URIs that follow the conventions in <https://cloud.google.com/apis/design/resource_names>. For example: `projects/my-project/locations/us-central1-a/privateClouds/my-cloud/loggingServers/my-logging-server`  
**Returns**  
---  
**Type** | **Description**  
`[LoggingServer](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.LoggingServer)` |   
  
### getLoggingServer(GetLoggingServerRequest request)
    
    
    public final LoggingServer getLoggingServer(GetLoggingServerRequest request)

Gets details of a logging server.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       GetLoggingServerRequest request =
           GetLoggingServerRequest.newBuilder()
               .setName(
                   LoggingServerName.of(
                           "[PROJECT]", "[LOCATION]", "[PRIVATE_CLOUD]", "[LOGGING_SERVER]")
                       .toString())
               .build();
       LoggingServer response = vmwareEngineClient.getLoggingServer(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetLoggingServerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.GetLoggingServerRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[LoggingServer](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.LoggingServer)` |   
  
### getLoggingServer(String name)
    
    
    public final LoggingServer getLoggingServer(String name)

Gets details of a logging server.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       String name =
           LoggingServerName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_CLOUD]", "[LOGGING_SERVER]")
               .toString();
       LoggingServer response = vmwareEngineClient.getLoggingServer(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the Logging Server to retrieve. Resource names are schemeless URIs that follow the conventions in <https://cloud.google.com/apis/design/resource_names>. For example: `projects/my-project/locations/us-central1-a/privateClouds/my-cloud/loggingServers/my-logging-server`  
**Returns**  
---  
**Type** | **Description**  
`[LoggingServer](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.LoggingServer)` |   
  
### getLoggingServerCallable()
    
    
    public final UnaryCallable<GetLoggingServerRequest,LoggingServer> getLoggingServerCallable()

Gets details of a logging server.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       GetLoggingServerRequest request =
           GetLoggingServerRequest.newBuilder()
               .setName(
                   LoggingServerName.of(
                           "[PROJECT]", "[LOCATION]", "[PRIVATE_CLOUD]", "[LOGGING_SERVER]")
                       .toString())
               .build();
       ApiFuture<LoggingServer> future =
           vmwareEngineClient.getLoggingServerCallable().futureCall(request);
       // Do something.
       LoggingServer response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetLoggingServerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.GetLoggingServerRequest),[LoggingServer](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.LoggingServer)>` |   
  
### getManagementDnsZoneBinding(@Nullable ManagementDnsZoneBindingName name)
    
    
    public final ManagementDnsZoneBinding getManagementDnsZoneBinding(@Nullable ManagementDnsZoneBindingName name)

Retrieves a 'ManagementDnsZoneBinding' resource by its resource name.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       ManagementDnsZoneBindingName name =
           ManagementDnsZoneBindingName.of(
               "[PROJECT]", "[LOCATION]", "[PRIVATE_CLOUD]", "[MANAGEMENT_DNS_ZONE_BINDING]");
       ManagementDnsZoneBinding response = vmwareEngineClient.getManagementDnsZoneBinding(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.vmwareengine.v1.ManagementDnsZoneBindingName`  
Required. The resource name of the management DNS zone binding to retrieve. Resource names are schemeless URIs that follow the conventions in <https://cloud.google.com/apis/design/resource_names>. For example: `projects/my-project/locations/us-central1-a/privateClouds/my-cloud/managementDnsZoneBindings/my-management-dns-zone-binding`  
**Returns**  
---  
**Type** | **Description**  
`[ManagementDnsZoneBinding](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.ManagementDnsZoneBinding)` |   
  
### getManagementDnsZoneBinding(GetManagementDnsZoneBindingRequest request)
    
    
    public final ManagementDnsZoneBinding getManagementDnsZoneBinding(GetManagementDnsZoneBindingRequest request)

Retrieves a 'ManagementDnsZoneBinding' resource by its resource name.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       GetManagementDnsZoneBindingRequest request =
           GetManagementDnsZoneBindingRequest.newBuilder()
               .setName(
                   ManagementDnsZoneBindingName.of(
                           "[PROJECT]",
                           "[LOCATION]",
                           "[PRIVATE_CLOUD]",
                           "[MANAGEMENT_DNS_ZONE_BINDING]")
                       .toString())
               .build();
       ManagementDnsZoneBinding response = vmwareEngineClient.getManagementDnsZoneBinding(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetManagementDnsZoneBindingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.GetManagementDnsZoneBindingRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ManagementDnsZoneBinding](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.ManagementDnsZoneBinding)` |   
  
### getManagementDnsZoneBinding(String name)
    
    
    public final ManagementDnsZoneBinding getManagementDnsZoneBinding(String name)

Retrieves a 'ManagementDnsZoneBinding' resource by its resource name.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       String name =
           ManagementDnsZoneBindingName.of(
                   "[PROJECT]", "[LOCATION]", "[PRIVATE_CLOUD]", "[MANAGEMENT_DNS_ZONE_BINDING]")
               .toString();
       ManagementDnsZoneBinding response = vmwareEngineClient.getManagementDnsZoneBinding(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the management DNS zone binding to retrieve. Resource names are schemeless URIs that follow the conventions in <https://cloud.google.com/apis/design/resource_names>. For example: `projects/my-project/locations/us-central1-a/privateClouds/my-cloud/managementDnsZoneBindings/my-management-dns-zone-binding`  
**Returns**  
---  
**Type** | **Description**  
`[ManagementDnsZoneBinding](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.ManagementDnsZoneBinding)` |   
  
### getManagementDnsZoneBindingCallable()
    
    
    public final UnaryCallable<GetManagementDnsZoneBindingRequest,ManagementDnsZoneBinding> getManagementDnsZoneBindingCallable()

Retrieves a 'ManagementDnsZoneBinding' resource by its resource name.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       GetManagementDnsZoneBindingRequest request =
           GetManagementDnsZoneBindingRequest.newBuilder()
               .setName(
                   ManagementDnsZoneBindingName.of(
                           "[PROJECT]",
                           "[LOCATION]",
                           "[PRIVATE_CLOUD]",
                           "[MANAGEMENT_DNS_ZONE_BINDING]")
                       .toString())
               .build();
       ApiFuture<ManagementDnsZoneBinding> future =
           vmwareEngineClient.getManagementDnsZoneBindingCallable().futureCall(request);
       // Do something.
       ManagementDnsZoneBinding response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetManagementDnsZoneBindingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.GetManagementDnsZoneBindingRequest),[ManagementDnsZoneBinding](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.ManagementDnsZoneBinding)>` |   
  
### getNetworkPeering(@Nullable NetworkPeeringName name)
    
    
    public final NetworkPeering getNetworkPeering(@Nullable NetworkPeeringName name)

Retrieves a `NetworkPeering` resource by its resource name. The resource contains details of the network peering, such as peered networks, import and export custom route configurations, and peering state. NetworkPeering is a global resource and location can only be global.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       NetworkPeeringName name =
           NetworkPeeringName.of("[PROJECT]", "[LOCATION]", "[NETWORK_PEERING]");
       NetworkPeering response = vmwareEngineClient.getNetworkPeering(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.vmwareengine.v1.NetworkPeeringName`  
Required. The resource name of the network peering to retrieve. Resource names are schemeless URIs that follow the conventions in <https://cloud.google.com/apis/design/resource_names>. For example: `projects/my-project/locations/global/networkPeerings/my-peering`  
**Returns**  
---  
**Type** | **Description**  
`[NetworkPeering](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.NetworkPeering)` |   
  
### getNetworkPeering(GetNetworkPeeringRequest request)
    
    
    public final NetworkPeering getNetworkPeering(GetNetworkPeeringRequest request)

Retrieves a `NetworkPeering` resource by its resource name. The resource contains details of the network peering, such as peered networks, import and export custom route configurations, and peering state. NetworkPeering is a global resource and location can only be global.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       GetNetworkPeeringRequest request =
           GetNetworkPeeringRequest.newBuilder()
               .setName(
                   NetworkPeeringName.of("[PROJECT]", "[LOCATION]", "[NETWORK_PEERING]").toString())
               .build();
       NetworkPeering response = vmwareEngineClient.getNetworkPeering(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetNetworkPeeringRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.GetNetworkPeeringRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[NetworkPeering](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.NetworkPeering)` |   
  
### getNetworkPeering(String name)
    
    
    public final NetworkPeering getNetworkPeering(String name)

Retrieves a `NetworkPeering` resource by its resource name. The resource contains details of the network peering, such as peered networks, import and export custom route configurations, and peering state. NetworkPeering is a global resource and location can only be global.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       String name =
           NetworkPeeringName.of("[PROJECT]", "[LOCATION]", "[NETWORK_PEERING]").toString();
       NetworkPeering response = vmwareEngineClient.getNetworkPeering(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the network peering to retrieve. Resource names are schemeless URIs that follow the conventions in <https://cloud.google.com/apis/design/resource_names>. For example: `projects/my-project/locations/global/networkPeerings/my-peering`  
**Returns**  
---  
**Type** | **Description**  
`[NetworkPeering](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.NetworkPeering)` |   
  
### getNetworkPeeringCallable()
    
    
    public final UnaryCallable<GetNetworkPeeringRequest,NetworkPeering> getNetworkPeeringCallable()

Retrieves a `NetworkPeering` resource by its resource name. The resource contains details of the network peering, such as peered networks, import and export custom route configurations, and peering state. NetworkPeering is a global resource and location can only be global.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       GetNetworkPeeringRequest request =
           GetNetworkPeeringRequest.newBuilder()
               .setName(
                   NetworkPeeringName.of("[PROJECT]", "[LOCATION]", "[NETWORK_PEERING]").toString())
               .build();
       ApiFuture<NetworkPeering> future =
           vmwareEngineClient.getNetworkPeeringCallable().futureCall(request);
       // Do something.
       NetworkPeering response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetNetworkPeeringRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.GetNetworkPeeringRequest),[NetworkPeering](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.NetworkPeering)>` |   
  
### getNetworkPolicy(@Nullable NetworkPolicyName name)
    
    
    public final NetworkPolicy getNetworkPolicy(@Nullable NetworkPolicyName name)

Retrieves a `NetworkPolicy` resource by its resource name.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       NetworkPolicyName name = NetworkPolicyName.of("[PROJECT]", "[LOCATION]", "[NETWORK_POLICY]");
       NetworkPolicy response = vmwareEngineClient.getNetworkPolicy(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.vmwareengine.v1.NetworkPolicyName`  
Required. The resource name of the network policy to retrieve. Resource names are schemeless URIs that follow the conventions in <https://cloud.google.com/apis/design/resource_names>. For example: `projects/my-project/locations/us-central1/networkPolicies/my-network-policy`  
**Returns**  
---  
**Type** | **Description**  
`[NetworkPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.NetworkPolicy)` |   
  
### getNetworkPolicy(GetNetworkPolicyRequest request)
    
    
    public final NetworkPolicy getNetworkPolicy(GetNetworkPolicyRequest request)

Retrieves a `NetworkPolicy` resource by its resource name.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       GetNetworkPolicyRequest request =
           GetNetworkPolicyRequest.newBuilder()
               .setName(
                   NetworkPolicyName.of("[PROJECT]", "[LOCATION]", "[NETWORK_POLICY]").toString())
               .build();
       NetworkPolicy response = vmwareEngineClient.getNetworkPolicy(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetNetworkPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.GetNetworkPolicyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[NetworkPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.NetworkPolicy)` |   
  
### getNetworkPolicy(String name)
    
    
    public final NetworkPolicy getNetworkPolicy(String name)

Retrieves a `NetworkPolicy` resource by its resource name.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       String name = NetworkPolicyName.of("[PROJECT]", "[LOCATION]", "[NETWORK_POLICY]").toString();
       NetworkPolicy response = vmwareEngineClient.getNetworkPolicy(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the network policy to retrieve. Resource names are schemeless URIs that follow the conventions in <https://cloud.google.com/apis/design/resource_names>. For example: `projects/my-project/locations/us-central1/networkPolicies/my-network-policy`  
**Returns**  
---  
**Type** | **Description**  
`[NetworkPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.NetworkPolicy)` |   
  
### getNetworkPolicyCallable()
    
    
    public final UnaryCallable<GetNetworkPolicyRequest,NetworkPolicy> getNetworkPolicyCallable()

Retrieves a `NetworkPolicy` resource by its resource name.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       GetNetworkPolicyRequest request =
           GetNetworkPolicyRequest.newBuilder()
               .setName(
                   NetworkPolicyName.of("[PROJECT]", "[LOCATION]", "[NETWORK_POLICY]").toString())
               .build();
       ApiFuture<NetworkPolicy> future =
           vmwareEngineClient.getNetworkPolicyCallable().futureCall(request);
       // Do something.
       NetworkPolicy response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetNetworkPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.GetNetworkPolicyRequest),[NetworkPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.NetworkPolicy)>` |   
  
### getNode(@Nullable NodeName name)
    
    
    public final Node getNode(@Nullable NodeName name)

Gets details of a single node.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       NodeName name =
           NodeName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_CLOUD]", "[CLUSTER]", "[NODE]");
       Node response = vmwareEngineClient.getNode(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.vmwareengine.v1.NodeName`  
Required. The resource name of the node to retrieve. For example: `projects/{project}/locations/{location}/privateClouds/{private_cloud}/clusters/{cluster}/nodes/{node}`  
**Returns**  
---  
**Type** | **Description**  
`[Node](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.Node)` |   
  
### getNode(GetNodeRequest request)
    
    
    public final Node getNode(GetNodeRequest request)

Gets details of a single node.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       GetNodeRequest request =
           GetNodeRequest.newBuilder()
               .setName(
                   NodeName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_CLOUD]", "[CLUSTER]", "[NODE]")
                       .toString())
               .build();
       Node response = vmwareEngineClient.getNode(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetNodeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.GetNodeRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Node](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.Node)` |   
  
### getNode(String name)
    
    
    public final Node getNode(String name)

Gets details of a single node.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       String name =
           NodeName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_CLOUD]", "[CLUSTER]", "[NODE]")
               .toString();
       Node response = vmwareEngineClient.getNode(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the node to retrieve. For example: `projects/{project}/locations/{location}/privateClouds/{private_cloud}/clusters/{cluster}/nodes/{node}`  
**Returns**  
---  
**Type** | **Description**  
`[Node](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.Node)` |   
  
### getNodeCallable()
    
    
    public final UnaryCallable<GetNodeRequest,Node> getNodeCallable()

Gets details of a single node.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       GetNodeRequest request =
           GetNodeRequest.newBuilder()
               .setName(
                   NodeName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_CLOUD]", "[CLUSTER]", "[NODE]")
                       .toString())
               .build();
       ApiFuture<Node> future = vmwareEngineClient.getNodeCallable().futureCall(request);
       // Do something.
       Node response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetNodeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.GetNodeRequest),[Node](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.Node)>` |   
  
### getNodeType(@Nullable NodeTypeName name)
    
    
    public final NodeType getNodeType(@Nullable NodeTypeName name)

Gets details of a single `NodeType`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       NodeTypeName name = NodeTypeName.of("[PROJECT]", "[LOCATION]", "[NODE_TYPE]");
       NodeType response = vmwareEngineClient.getNodeType(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.vmwareengine.v1.NodeTypeName`  
Required. The resource name of the node type to retrieve. Resource names are schemeless URIs that follow the conventions in <https://cloud.google.com/apis/design/resource_names>. For example: `projects/my-proj/locations/us-central1-a/nodeTypes/standard-72`  
**Returns**  
---  
**Type** | **Description**  
`[NodeType](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.NodeType)` |   
  
### getNodeType(GetNodeTypeRequest request)
    
    
    public final NodeType getNodeType(GetNodeTypeRequest request)

Gets details of a single `NodeType`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       GetNodeTypeRequest request =
           GetNodeTypeRequest.newBuilder()
               .setName(NodeTypeName.of("[PROJECT]", "[LOCATION]", "[NODE_TYPE]").toString())
               .build();
       NodeType response = vmwareEngineClient.getNodeType(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetNodeTypeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.GetNodeTypeRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[NodeType](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.NodeType)` |   
  
### getNodeType(String name)
    
    
    public final NodeType getNodeType(String name)

Gets details of a single `NodeType`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       String name = NodeTypeName.of("[PROJECT]", "[LOCATION]", "[NODE_TYPE]").toString();
       NodeType response = vmwareEngineClient.getNodeType(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the node type to retrieve. Resource names are schemeless URIs that follow the conventions in <https://cloud.google.com/apis/design/resource_names>. For example: `projects/my-proj/locations/us-central1-a/nodeTypes/standard-72`  
**Returns**  
---  
**Type** | **Description**  
`[NodeType](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.NodeType)` |   
  
### getNodeTypeCallable()
    
    
    public final UnaryCallable<GetNodeTypeRequest,NodeType> getNodeTypeCallable()

Gets details of a single `NodeType`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       GetNodeTypeRequest request =
           GetNodeTypeRequest.newBuilder()
               .setName(NodeTypeName.of("[PROJECT]", "[LOCATION]", "[NODE_TYPE]").toString())
               .build();
       ApiFuture<NodeType> future = vmwareEngineClient.getNodeTypeCallable().futureCall(request);
       // Do something.
       NodeType response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetNodeTypeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.GetNodeTypeRequest),[NodeType](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.NodeType)>` |   
  
### getOperationsClient()
    
    
    public final OperationsClient getOperationsClient()

Returns the OperationsClient that can be used to query the status of a long-running operation returned by another API method call.

**Returns**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.OperationsClient.html)` |   
  
### getPrivateCloud(@Nullable PrivateCloudName name)
    
    
    public final PrivateCloud getPrivateCloud(@Nullable PrivateCloudName name)

Retrieves a `PrivateCloud` resource by its resource name.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       PrivateCloudName name = PrivateCloudName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_CLOUD]");
       PrivateCloud response = vmwareEngineClient.getPrivateCloud(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.vmwareengine.v1.PrivateCloudName`  
Required. The resource name of the private cloud to retrieve. Resource names are schemeless URIs that follow the conventions in <https://cloud.google.com/apis/design/resource_names>. For example: `projects/my-project/locations/us-central1-a/privateClouds/my-cloud`  
**Returns**  
---  
**Type** | **Description**  
`[PrivateCloud](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.PrivateCloud)` |   
  
### getPrivateCloud(GetPrivateCloudRequest request)
    
    
    public final PrivateCloud getPrivateCloud(GetPrivateCloudRequest request)

Retrieves a `PrivateCloud` resource by its resource name.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       GetPrivateCloudRequest request =
           GetPrivateCloudRequest.newBuilder()
               .setName(PrivateCloudName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_CLOUD]").toString())
               .build();
       PrivateCloud response = vmwareEngineClient.getPrivateCloud(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetPrivateCloudRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.GetPrivateCloudRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[PrivateCloud](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.PrivateCloud)` |   
  
### getPrivateCloud(String name)
    
    
    public final PrivateCloud getPrivateCloud(String name)

Retrieves a `PrivateCloud` resource by its resource name.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       String name = PrivateCloudName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_CLOUD]").toString();
       PrivateCloud response = vmwareEngineClient.getPrivateCloud(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the private cloud to retrieve. Resource names are schemeless URIs that follow the conventions in <https://cloud.google.com/apis/design/resource_names>. For example: `projects/my-project/locations/us-central1-a/privateClouds/my-cloud`  
**Returns**  
---  
**Type** | **Description**  
`[PrivateCloud](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.PrivateCloud)` |   
  
### getPrivateCloudCallable()
    
    
    public final UnaryCallable<GetPrivateCloudRequest,PrivateCloud> getPrivateCloudCallable()

Retrieves a `PrivateCloud` resource by its resource name.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       GetPrivateCloudRequest request =
           GetPrivateCloudRequest.newBuilder()
               .setName(PrivateCloudName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_CLOUD]").toString())
               .build();
       ApiFuture<PrivateCloud> future =
           vmwareEngineClient.getPrivateCloudCallable().futureCall(request);
       // Do something.
       PrivateCloud response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetPrivateCloudRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.GetPrivateCloudRequest),[PrivateCloud](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.PrivateCloud)>` |   
  
### getPrivateConnection(@Nullable PrivateConnectionName name)
    
    
    public final PrivateConnection getPrivateConnection(@Nullable PrivateConnectionName name)

Retrieves a `PrivateConnection` resource by its resource name. The resource contains details of the private connection, such as connected network, routing mode and state.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       PrivateConnectionName name =
           PrivateConnectionName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_CONNECTION]");
       PrivateConnection response = vmwareEngineClient.getPrivateConnection(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.vmwareengine.v1.PrivateConnectionName`  
Required. The resource name of the private connection to retrieve. Resource names are schemeless URIs that follow the conventions in <https://cloud.google.com/apis/design/resource_names>. For example: `projects/my-project/locations/us-central1/privateConnections/my-connection`  
**Returns**  
---  
**Type** | **Description**  
`[PrivateConnection](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.PrivateConnection)` |   
  
### getPrivateConnection(GetPrivateConnectionRequest request)
    
    
    public final PrivateConnection getPrivateConnection(GetPrivateConnectionRequest request)

Retrieves a `PrivateConnection` resource by its resource name. The resource contains details of the private connection, such as connected network, routing mode and state.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       GetPrivateConnectionRequest request =
           GetPrivateConnectionRequest.newBuilder()
               .setName(
                   PrivateConnectionName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_CONNECTION]")
                       .toString())
               .build();
       PrivateConnection response = vmwareEngineClient.getPrivateConnection(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetPrivateConnectionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.GetPrivateConnectionRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[PrivateConnection](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.PrivateConnection)` |   
  
### getPrivateConnection(String name)
    
    
    public final PrivateConnection getPrivateConnection(String name)

Retrieves a `PrivateConnection` resource by its resource name. The resource contains details of the private connection, such as connected network, routing mode and state.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       String name =
           PrivateConnectionName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_CONNECTION]").toString();
       PrivateConnection response = vmwareEngineClient.getPrivateConnection(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the private connection to retrieve. Resource names are schemeless URIs that follow the conventions in <https://cloud.google.com/apis/design/resource_names>. For example: `projects/my-project/locations/us-central1/privateConnections/my-connection`  
**Returns**  
---  
**Type** | **Description**  
`[PrivateConnection](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.PrivateConnection)` |   
  
### getPrivateConnectionCallable()
    
    
    public final UnaryCallable<GetPrivateConnectionRequest,PrivateConnection> getPrivateConnectionCallable()

Retrieves a `PrivateConnection` resource by its resource name. The resource contains details of the private connection, such as connected network, routing mode and state.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       GetPrivateConnectionRequest request =
           GetPrivateConnectionRequest.newBuilder()
               .setName(
                   PrivateConnectionName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_CONNECTION]")
                       .toString())
               .build();
       ApiFuture<PrivateConnection> future =
           vmwareEngineClient.getPrivateConnectionCallable().futureCall(request);
       // Do something.
       PrivateConnection response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetPrivateConnectionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.GetPrivateConnectionRequest),[PrivateConnection](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.PrivateConnection)>` |   
  
### getSettings()
    
    
    public final @Nullable VmwareEngineSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.vmwareengine.v1.VmwareEngineSettings` |   
  
### getStub()
    
    
    public VmwareEngineStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[VmwareEngineStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.stub.VmwareEngineStub)` |   
  
### getSubnet(@Nullable SubnetName name)
    
    
    public final Subnet getSubnet(@Nullable SubnetName name)

Gets details of a single subnet.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       SubnetName name = SubnetName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_CLOUD]", "[SUBNET]");
       Subnet response = vmwareEngineClient.getSubnet(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.vmwareengine.v1.SubnetName`  
Required. The resource name of the subnet to retrieve. Resource names are schemeless URIs that follow the conventions in <https://cloud.google.com/apis/design/resource_names>. For example: `projects/my-project/locations/us-central1-a/privateClouds/my-cloud/subnets/my-subnet`  
**Returns**  
---  
**Type** | **Description**  
`[Subnet](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.Subnet)` |   
  
### getSubnet(GetSubnetRequest request)
    
    
    public final Subnet getSubnet(GetSubnetRequest request)

Gets details of a single subnet.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       GetSubnetRequest request =
           GetSubnetRequest.newBuilder()
               .setName(
                   SubnetName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_CLOUD]", "[SUBNET]")
                       .toString())
               .build();
       Subnet response = vmwareEngineClient.getSubnet(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetSubnetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.GetSubnetRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Subnet](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.Subnet)` |   
  
### getSubnet(String name)
    
    
    public final Subnet getSubnet(String name)

Gets details of a single subnet.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       String name =
           SubnetName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_CLOUD]", "[SUBNET]").toString();
       Subnet response = vmwareEngineClient.getSubnet(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the subnet to retrieve. Resource names are schemeless URIs that follow the conventions in <https://cloud.google.com/apis/design/resource_names>. For example: `projects/my-project/locations/us-central1-a/privateClouds/my-cloud/subnets/my-subnet`  
**Returns**  
---  
**Type** | **Description**  
`[Subnet](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.Subnet)` |   
  
### getSubnetCallable()
    
    
    public final UnaryCallable<GetSubnetRequest,Subnet> getSubnetCallable()

Gets details of a single subnet.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       GetSubnetRequest request =
           GetSubnetRequest.newBuilder()
               .setName(
                   SubnetName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_CLOUD]", "[SUBNET]")
                       .toString())
               .build();
       ApiFuture<Subnet> future = vmwareEngineClient.getSubnetCallable().futureCall(request);
       // Do something.
       Subnet response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetSubnetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.GetSubnetRequest),[Subnet](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.Subnet)>` |   
  
### getVmwareEngineNetwork(@Nullable VmwareEngineNetworkName name)
    
    
    public final VmwareEngineNetwork getVmwareEngineNetwork(@Nullable VmwareEngineNetworkName name)

Retrieves a `VmwareEngineNetwork` resource by its resource name. The resource contains details of the VMware Engine network, such as its VMware Engine network type, peered networks in a service project, and state (for example, `CREATING`, `ACTIVE`, `DELETING`).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       VmwareEngineNetworkName name =
           VmwareEngineNetworkName.of("[PROJECT]", "[LOCATION]", "[VMWARE_ENGINE_NETWORK]");
       VmwareEngineNetwork response = vmwareEngineClient.getVmwareEngineNetwork(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.vmwareengine.v1.VmwareEngineNetworkName`  
Required. The resource name of the VMware Engine network to retrieve. Resource names are schemeless URIs that follow the conventions in <https://cloud.google.com/apis/design/resource_names>. For example: `projects/my-project/locations/global/vmwareEngineNetworks/my-network`  
**Returns**  
---  
**Type** | **Description**  
`[VmwareEngineNetwork](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.VmwareEngineNetwork)` |   
  
### getVmwareEngineNetwork(GetVmwareEngineNetworkRequest request)
    
    
    public final VmwareEngineNetwork getVmwareEngineNetwork(GetVmwareEngineNetworkRequest request)

Retrieves a `VmwareEngineNetwork` resource by its resource name. The resource contains details of the VMware Engine network, such as its VMware Engine network type, peered networks in a service project, and state (for example, `CREATING`, `ACTIVE`, `DELETING`).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       GetVmwareEngineNetworkRequest request =
           GetVmwareEngineNetworkRequest.newBuilder()
               .setName(
                   VmwareEngineNetworkName.of("[PROJECT]", "[LOCATION]", "[VMWARE_ENGINE_NETWORK]")
                       .toString())
               .build();
       VmwareEngineNetwork response = vmwareEngineClient.getVmwareEngineNetwork(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetVmwareEngineNetworkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.GetVmwareEngineNetworkRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[VmwareEngineNetwork](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.VmwareEngineNetwork)` |   
  
### getVmwareEngineNetwork(String name)
    
    
    public final VmwareEngineNetwork getVmwareEngineNetwork(String name)

Retrieves a `VmwareEngineNetwork` resource by its resource name. The resource contains details of the VMware Engine network, such as its VMware Engine network type, peered networks in a service project, and state (for example, `CREATING`, `ACTIVE`, `DELETING`).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       String name =
           VmwareEngineNetworkName.of("[PROJECT]", "[LOCATION]", "[VMWARE_ENGINE_NETWORK]")
               .toString();
       VmwareEngineNetwork response = vmwareEngineClient.getVmwareEngineNetwork(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the VMware Engine network to retrieve. Resource names are schemeless URIs that follow the conventions in <https://cloud.google.com/apis/design/resource_names>. For example: `projects/my-project/locations/global/vmwareEngineNetworks/my-network`  
**Returns**  
---  
**Type** | **Description**  
`[VmwareEngineNetwork](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.VmwareEngineNetwork)` |   
  
### getVmwareEngineNetworkCallable()
    
    
    public final UnaryCallable<GetVmwareEngineNetworkRequest,VmwareEngineNetwork> getVmwareEngineNetworkCallable()

Retrieves a `VmwareEngineNetwork` resource by its resource name. The resource contains details of the VMware Engine network, such as its VMware Engine network type, peered networks in a service project, and state (for example, `CREATING`, `ACTIVE`, `DELETING`).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       GetVmwareEngineNetworkRequest request =
           GetVmwareEngineNetworkRequest.newBuilder()
               .setName(
                   VmwareEngineNetworkName.of("[PROJECT]", "[LOCATION]", "[VMWARE_ENGINE_NETWORK]")
                       .toString())
               .build();
       ApiFuture<VmwareEngineNetwork> future =
           vmwareEngineClient.getVmwareEngineNetworkCallable().futureCall(request);
       // Do something.
       VmwareEngineNetwork response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetVmwareEngineNetworkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.GetVmwareEngineNetworkRequest),[VmwareEngineNetwork](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.VmwareEngineNetwork)>` |   
  
### grantDnsBindPermissionAsync(@Nullable DnsBindPermissionName name, Principal principal)
    
    
    public final OperationFuture<DnsBindPermission,OperationMetadata> grantDnsBindPermissionAsync(@Nullable DnsBindPermissionName name, Principal principal)

Grants the bind permission to the customer provided principal(user / service account) to bind their DNS zone with the intranet VPC associated with the project. DnsBindPermission is a global resource and location can only be global.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       DnsBindPermissionName name = DnsBindPermissionName.of("[PROJECT]", "[LOCATION]");
       Principal principal = Principal.newBuilder().build();
       DnsBindPermission response =
           vmwareEngineClient.grantDnsBindPermissionAsync(name, principal).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.vmwareengine.v1.DnsBindPermissionName`  
Required. The name of the resource which stores the users/service accounts having the permission to bind to the corresponding intranet VPC of the consumer project. DnsBindPermission is a global resource. Resource names are schemeless URIs that follow the conventions in <https://cloud.google.com/apis/design/resource_names>. For example: `projects/my-project/locations/global/dnsBindPermission`  
`principal` | `[Principal](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.Principal)`  
Required. The consumer provided user/service account which needs to be granted permission to bind with the intranet VPC corresponding to the consumer project.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[DnsBindPermission](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.DnsBindPermission),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.OperationMetadata)>` |   
  
### grantDnsBindPermissionAsync(GrantDnsBindPermissionRequest request)
    
    
    public final OperationFuture<DnsBindPermission,OperationMetadata> grantDnsBindPermissionAsync(GrantDnsBindPermissionRequest request)

Grants the bind permission to the customer provided principal(user / service account) to bind their DNS zone with the intranet VPC associated with the project. DnsBindPermission is a global resource and location can only be global.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       GrantDnsBindPermissionRequest request =
           GrantDnsBindPermissionRequest.newBuilder()
               .setName(DnsBindPermissionName.of("[PROJECT]", "[LOCATION]").toString())
               .setPrincipal(Principal.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       DnsBindPermission response = vmwareEngineClient.grantDnsBindPermissionAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GrantDnsBindPermissionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.GrantDnsBindPermissionRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[DnsBindPermission](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.DnsBindPermission),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.OperationMetadata)>` |   
  
### grantDnsBindPermissionAsync(String name, Principal principal)
    
    
    public final OperationFuture<DnsBindPermission,OperationMetadata> grantDnsBindPermissionAsync(String name, Principal principal)

Grants the bind permission to the customer provided principal(user / service account) to bind their DNS zone with the intranet VPC associated with the project. DnsBindPermission is a global resource and location can only be global.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       String name = DnsBindPermissionName.of("[PROJECT]", "[LOCATION]").toString();
       Principal principal = Principal.newBuilder().build();
       DnsBindPermission response =
           vmwareEngineClient.grantDnsBindPermissionAsync(name, principal).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the resource which stores the users/service accounts having the permission to bind to the corresponding intranet VPC of the consumer project. DnsBindPermission is a global resource. Resource names are schemeless URIs that follow the conventions in <https://cloud.google.com/apis/design/resource_names>. For example: `projects/my-project/locations/global/dnsBindPermission`  
`principal` | `[Principal](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.Principal)`  
Required. The consumer provided user/service account which needs to be granted permission to bind with the intranet VPC corresponding to the consumer project.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[DnsBindPermission](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.DnsBindPermission),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.OperationMetadata)>` |   
  
### grantDnsBindPermissionCallable()
    
    
    public final UnaryCallable<GrantDnsBindPermissionRequest,Operation> grantDnsBindPermissionCallable()

Grants the bind permission to the customer provided principal(user / service account) to bind their DNS zone with the intranet VPC associated with the project. DnsBindPermission is a global resource and location can only be global.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       GrantDnsBindPermissionRequest request =
           GrantDnsBindPermissionRequest.newBuilder()
               .setName(DnsBindPermissionName.of("[PROJECT]", "[LOCATION]").toString())
               .setPrincipal(Principal.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           vmwareEngineClient.grantDnsBindPermissionCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GrantDnsBindPermissionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.GrantDnsBindPermissionRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### grantDnsBindPermissionOperationCallable()
    
    
    public final OperationCallable<GrantDnsBindPermissionRequest,DnsBindPermission,OperationMetadata> grantDnsBindPermissionOperationCallable()

Grants the bind permission to the customer provided principal(user / service account) to bind their DNS zone with the intranet VPC associated with the project. DnsBindPermission is a global resource and location can only be global.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       GrantDnsBindPermissionRequest request =
           GrantDnsBindPermissionRequest.newBuilder()
               .setName(DnsBindPermissionName.of("[PROJECT]", "[LOCATION]").toString())
               .setPrincipal(Principal.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<DnsBindPermission, OperationMetadata> future =
           vmwareEngineClient.grantDnsBindPermissionOperationCallable().futureCall(request);
       // Do something.
       DnsBindPermission response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[GrantDnsBindPermissionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.GrantDnsBindPermissionRequest),[DnsBindPermission](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.DnsBindPermission),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.OperationMetadata)>` |   
  
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
  
### listClusters(@Nullable PrivateCloudName parent)
    
    
    public final VmwareEngineClient.ListClustersPagedResponse listClusters(@Nullable PrivateCloudName parent)

Lists `Cluster` resources in a given private cloud.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       PrivateCloudName parent = PrivateCloudName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_CLOUD]");
       for (Cluster element : vmwareEngineClient.listClusters(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.vmwareengine.v1.PrivateCloudName`  
Required. The resource name of the private cloud to query for clusters. Resource names are schemeless URIs that follow the conventions in <https://cloud.google.com/apis/design/resource_names>. For example: `projects/my-project/locations/us-central1-a/privateClouds/my-cloud`  
**Returns**  
---  
**Type** | **Description**  
`[VmwareEngineClient.ListClustersPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.VmwareEngineClient.ListClustersPagedResponse)` |   
  
### listClusters(ListClustersRequest request)
    
    
    public final VmwareEngineClient.ListClustersPagedResponse listClusters(ListClustersRequest request)

Lists `Cluster` resources in a given private cloud.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       ListClustersRequest request =
           ListClustersRequest.newBuilder()
               .setParent(
                   PrivateCloudName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_CLOUD]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       for (Cluster element : vmwareEngineClient.listClusters(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListClustersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.ListClustersRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[VmwareEngineClient.ListClustersPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.VmwareEngineClient.ListClustersPagedResponse)` |   
  
### listClusters(String parent)
    
    
    public final VmwareEngineClient.ListClustersPagedResponse listClusters(String parent)

Lists `Cluster` resources in a given private cloud.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       String parent = PrivateCloudName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_CLOUD]").toString();
       for (Cluster element : vmwareEngineClient.listClusters(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the private cloud to query for clusters. Resource names are schemeless URIs that follow the conventions in <https://cloud.google.com/apis/design/resource_names>. For example: `projects/my-project/locations/us-central1-a/privateClouds/my-cloud`  
**Returns**  
---  
**Type** | **Description**  
`[VmwareEngineClient.ListClustersPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.VmwareEngineClient.ListClustersPagedResponse)` |   
  
### listClustersCallable()
    
    
    public final UnaryCallable<ListClustersRequest,ListClustersResponse> listClustersCallable()

Lists `Cluster` resources in a given private cloud.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       ListClustersRequest request =
           ListClustersRequest.newBuilder()
               .setParent(
                   PrivateCloudName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_CLOUD]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       while (true) {
         ListClustersResponse response = vmwareEngineClient.listClustersCallable().call(request);
         for (Cluster element : response.getClustersList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListClustersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.ListClustersRequest),[ListClustersResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.ListClustersResponse)>` |   
  
### listClustersPagedCallable()
    
    
    public final UnaryCallable<ListClustersRequest,VmwareEngineClient.ListClustersPagedResponse> listClustersPagedCallable()

Lists `Cluster` resources in a given private cloud.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       ListClustersRequest request =
           ListClustersRequest.newBuilder()
               .setParent(
                   PrivateCloudName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_CLOUD]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       ApiFuture<Cluster> future =
           vmwareEngineClient.listClustersPagedCallable().futureCall(request);
       // Do something.
       for (Cluster element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListClustersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.ListClustersRequest),[ListClustersPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.VmwareEngineClient.ListClustersPagedResponse)>` |   
  
### listExternalAccessRules(@Nullable NetworkPolicyName parent)
    
    
    public final VmwareEngineClient.ListExternalAccessRulesPagedResponse listExternalAccessRules(@Nullable NetworkPolicyName parent)

Lists `ExternalAccessRule` resources in the specified network policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       NetworkPolicyName parent =
           NetworkPolicyName.of("[PROJECT]", "[LOCATION]", "[NETWORK_POLICY]");
       for (ExternalAccessRule element :
           vmwareEngineClient.listExternalAccessRules(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.vmwareengine.v1.NetworkPolicyName`  
Required. The resource name of the network policy to query for external access firewall rules. Resource names are schemeless URIs that follow the conventions in <https://cloud.google.com/apis/design/resource_names>. For example: `projects/my-project/locations/us-central1/networkPolicies/my-policy`  
**Returns**  
---  
**Type** | **Description**  
`[VmwareEngineClient.ListExternalAccessRulesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.VmwareEngineClient.ListExternalAccessRulesPagedResponse)` |   
  
### listExternalAccessRules(ListExternalAccessRulesRequest request)
    
    
    public final VmwareEngineClient.ListExternalAccessRulesPagedResponse listExternalAccessRules(ListExternalAccessRulesRequest request)

Lists `ExternalAccessRule` resources in the specified network policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       ListExternalAccessRulesRequest request =
           ListExternalAccessRulesRequest.newBuilder()
               .setParent(
                   NetworkPolicyName.of("[PROJECT]", "[LOCATION]", "[NETWORK_POLICY]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       for (ExternalAccessRule element :
           vmwareEngineClient.listExternalAccessRules(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListExternalAccessRulesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.ListExternalAccessRulesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[VmwareEngineClient.ListExternalAccessRulesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.VmwareEngineClient.ListExternalAccessRulesPagedResponse)` |   
  
### listExternalAccessRules(String parent)
    
    
    public final VmwareEngineClient.ListExternalAccessRulesPagedResponse listExternalAccessRules(String parent)

Lists `ExternalAccessRule` resources in the specified network policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       String parent =
           NetworkPolicyName.of("[PROJECT]", "[LOCATION]", "[NETWORK_POLICY]").toString();
       for (ExternalAccessRule element :
           vmwareEngineClient.listExternalAccessRules(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the network policy to query for external access firewall rules. Resource names are schemeless URIs that follow the conventions in <https://cloud.google.com/apis/design/resource_names>. For example: `projects/my-project/locations/us-central1/networkPolicies/my-policy`  
**Returns**  
---  
**Type** | **Description**  
`[VmwareEngineClient.ListExternalAccessRulesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.VmwareEngineClient.ListExternalAccessRulesPagedResponse)` |   
  
### listExternalAccessRulesCallable()
    
    
    public final UnaryCallable<ListExternalAccessRulesRequest,ListExternalAccessRulesResponse> listExternalAccessRulesCallable()

Lists `ExternalAccessRule` resources in the specified network policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       ListExternalAccessRulesRequest request =
           ListExternalAccessRulesRequest.newBuilder()
               .setParent(
                   NetworkPolicyName.of("[PROJECT]", "[LOCATION]", "[NETWORK_POLICY]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       while (true) {
         ListExternalAccessRulesResponse response =
             vmwareEngineClient.listExternalAccessRulesCallable().call(request);
         for (ExternalAccessRule element : response.getExternalAccessRulesList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListExternalAccessRulesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.ListExternalAccessRulesRequest),[ListExternalAccessRulesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.ListExternalAccessRulesResponse)>` |   
  
### listExternalAccessRulesPagedCallable()
    
    
    public final UnaryCallable<ListExternalAccessRulesRequest,VmwareEngineClient.ListExternalAccessRulesPagedResponse> listExternalAccessRulesPagedCallable()

Lists `ExternalAccessRule` resources in the specified network policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       ListExternalAccessRulesRequest request =
           ListExternalAccessRulesRequest.newBuilder()
               .setParent(
                   NetworkPolicyName.of("[PROJECT]", "[LOCATION]", "[NETWORK_POLICY]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       ApiFuture<ExternalAccessRule> future =
           vmwareEngineClient.listExternalAccessRulesPagedCallable().futureCall(request);
       // Do something.
       for (ExternalAccessRule element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListExternalAccessRulesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.ListExternalAccessRulesRequest),[ListExternalAccessRulesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.VmwareEngineClient.ListExternalAccessRulesPagedResponse)>` |   
  
### listExternalAddresses(@Nullable PrivateCloudName parent)
    
    
    public final VmwareEngineClient.ListExternalAddressesPagedResponse listExternalAddresses(@Nullable PrivateCloudName parent)

Lists external IP addresses assigned to VMware workload VMs in a given private cloud.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       PrivateCloudName parent = PrivateCloudName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_CLOUD]");
       for (ExternalAddress element :
           vmwareEngineClient.listExternalAddresses(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.vmwareengine.v1.PrivateCloudName`  
Required. The resource name of the private cloud to be queried for external IP addresses. Resource names are schemeless URIs that follow the conventions in <https://cloud.google.com/apis/design/resource_names>. For example: `projects/my-project/locations/us-central1-a/privateClouds/my-cloud`  
**Returns**  
---  
**Type** | **Description**  
`[VmwareEngineClient.ListExternalAddressesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.VmwareEngineClient.ListExternalAddressesPagedResponse)` |   
  
### listExternalAddresses(ListExternalAddressesRequest request)
    
    
    public final VmwareEngineClient.ListExternalAddressesPagedResponse listExternalAddresses(ListExternalAddressesRequest request)

Lists external IP addresses assigned to VMware workload VMs in a given private cloud.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       ListExternalAddressesRequest request =
           ListExternalAddressesRequest.newBuilder()
               .setParent(
                   PrivateCloudName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_CLOUD]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       for (ExternalAddress element :
           vmwareEngineClient.listExternalAddresses(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListExternalAddressesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.ListExternalAddressesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[VmwareEngineClient.ListExternalAddressesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.VmwareEngineClient.ListExternalAddressesPagedResponse)` |   
  
### listExternalAddresses(String parent)
    
    
    public final VmwareEngineClient.ListExternalAddressesPagedResponse listExternalAddresses(String parent)

Lists external IP addresses assigned to VMware workload VMs in a given private cloud.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       String parent = PrivateCloudName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_CLOUD]").toString();
       for (ExternalAddress element :
           vmwareEngineClient.listExternalAddresses(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the private cloud to be queried for external IP addresses. Resource names are schemeless URIs that follow the conventions in <https://cloud.google.com/apis/design/resource_names>. For example: `projects/my-project/locations/us-central1-a/privateClouds/my-cloud`  
**Returns**  
---  
**Type** | **Description**  
`[VmwareEngineClient.ListExternalAddressesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.VmwareEngineClient.ListExternalAddressesPagedResponse)` |   
  
### listExternalAddressesCallable()
    
    
    public final UnaryCallable<ListExternalAddressesRequest,ListExternalAddressesResponse> listExternalAddressesCallable()

Lists external IP addresses assigned to VMware workload VMs in a given private cloud.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       ListExternalAddressesRequest request =
           ListExternalAddressesRequest.newBuilder()
               .setParent(
                   PrivateCloudName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_CLOUD]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       while (true) {
         ListExternalAddressesResponse response =
             vmwareEngineClient.listExternalAddressesCallable().call(request);
         for (ExternalAddress element : response.getExternalAddressesList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListExternalAddressesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.ListExternalAddressesRequest),[ListExternalAddressesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.ListExternalAddressesResponse)>` |   
  
### listExternalAddressesPagedCallable()
    
    
    public final UnaryCallable<ListExternalAddressesRequest,VmwareEngineClient.ListExternalAddressesPagedResponse> listExternalAddressesPagedCallable()

Lists external IP addresses assigned to VMware workload VMs in a given private cloud.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       ListExternalAddressesRequest request =
           ListExternalAddressesRequest.newBuilder()
               .setParent(
                   PrivateCloudName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_CLOUD]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       ApiFuture<ExternalAddress> future =
           vmwareEngineClient.listExternalAddressesPagedCallable().futureCall(request);
       // Do something.
       for (ExternalAddress element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListExternalAddressesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.ListExternalAddressesRequest),[ListExternalAddressesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.VmwareEngineClient.ListExternalAddressesPagedResponse)>` |   
  
### listHcxActivationKeys(@Nullable PrivateCloudName parent)
    
    
    public final VmwareEngineClient.ListHcxActivationKeysPagedResponse listHcxActivationKeys(@Nullable PrivateCloudName parent)

Lists `HcxActivationKey` resources in a given private cloud.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       PrivateCloudName parent = PrivateCloudName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_CLOUD]");
       for (HcxActivationKey element :
           vmwareEngineClient.listHcxActivationKeys(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.vmwareengine.v1.PrivateCloudName`  
Required. The resource name of the private cloud to be queried for HCX activation keys. Resource names are schemeless URIs that follow the conventions in <https://cloud.google.com/apis/design/resource_names>. For example: `projects/my-project/locations/us-central1/privateClouds/my-cloud`  
**Returns**  
---  
**Type** | **Description**  
`[VmwareEngineClient.ListHcxActivationKeysPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.VmwareEngineClient.ListHcxActivationKeysPagedResponse)` |   
  
### listHcxActivationKeys(ListHcxActivationKeysRequest request)
    
    
    public final VmwareEngineClient.ListHcxActivationKeysPagedResponse listHcxActivationKeys(ListHcxActivationKeysRequest request)

Lists `HcxActivationKey` resources in a given private cloud.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       ListHcxActivationKeysRequest request =
           ListHcxActivationKeysRequest.newBuilder()
               .setParent(
                   PrivateCloudName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_CLOUD]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (HcxActivationKey element :
           vmwareEngineClient.listHcxActivationKeys(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListHcxActivationKeysRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.ListHcxActivationKeysRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[VmwareEngineClient.ListHcxActivationKeysPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.VmwareEngineClient.ListHcxActivationKeysPagedResponse)` |   
  
### listHcxActivationKeys(String parent)
    
    
    public final VmwareEngineClient.ListHcxActivationKeysPagedResponse listHcxActivationKeys(String parent)

Lists `HcxActivationKey` resources in a given private cloud.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       String parent = PrivateCloudName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_CLOUD]").toString();
       for (HcxActivationKey element :
           vmwareEngineClient.listHcxActivationKeys(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the private cloud to be queried for HCX activation keys. Resource names are schemeless URIs that follow the conventions in <https://cloud.google.com/apis/design/resource_names>. For example: `projects/my-project/locations/us-central1/privateClouds/my-cloud`  
**Returns**  
---  
**Type** | **Description**  
`[VmwareEngineClient.ListHcxActivationKeysPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.VmwareEngineClient.ListHcxActivationKeysPagedResponse)` |   
  
### listHcxActivationKeysCallable()
    
    
    public final UnaryCallable<ListHcxActivationKeysRequest,ListHcxActivationKeysResponse> listHcxActivationKeysCallable()

Lists `HcxActivationKey` resources in a given private cloud.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       ListHcxActivationKeysRequest request =
           ListHcxActivationKeysRequest.newBuilder()
               .setParent(
                   PrivateCloudName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_CLOUD]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListHcxActivationKeysResponse response =
             vmwareEngineClient.listHcxActivationKeysCallable().call(request);
         for (HcxActivationKey element : response.getHcxActivationKeysList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListHcxActivationKeysRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.ListHcxActivationKeysRequest),[ListHcxActivationKeysResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.ListHcxActivationKeysResponse)>` |   
  
### listHcxActivationKeysPagedCallable()
    
    
    public final UnaryCallable<ListHcxActivationKeysRequest,VmwareEngineClient.ListHcxActivationKeysPagedResponse> listHcxActivationKeysPagedCallable()

Lists `HcxActivationKey` resources in a given private cloud.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       ListHcxActivationKeysRequest request =
           ListHcxActivationKeysRequest.newBuilder()
               .setParent(
                   PrivateCloudName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_CLOUD]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<HcxActivationKey> future =
           vmwareEngineClient.listHcxActivationKeysPagedCallable().futureCall(request);
       // Do something.
       for (HcxActivationKey element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListHcxActivationKeysRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.ListHcxActivationKeysRequest),[ListHcxActivationKeysPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.VmwareEngineClient.ListHcxActivationKeysPagedResponse)>` |   
  
### listLocations(ListLocationsRequest request)
    
    
    public final VmwareEngineClient.ListLocationsPagedResponse listLocations(ListLocationsRequest request)

Lists information about the supported locations for this service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (Location element : vmwareEngineClient.listLocations(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `com.google.cloud.location.ListLocationsRequest`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[VmwareEngineClient.ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.VmwareEngineClient.ListLocationsPagedResponse)` |   
  
### listLocationsCallable()
    
    
    public final UnaryCallable<ListLocationsRequest,ListLocationsResponse> listLocationsCallable()

Lists information about the supported locations for this service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListLocationsResponse response = vmwareEngineClient.listLocationsCallable().call(request);
         for (Location element : response.getLocationsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.ListLocationsRequest,com.google.cloud.location.ListLocationsResponse>` |   
  
### listLocationsPagedCallable()
    
    
    public final UnaryCallable<ListLocationsRequest,VmwareEngineClient.ListLocationsPagedResponse> listLocationsPagedCallable()

Lists information about the supported locations for this service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<Location> future =
           vmwareEngineClient.listLocationsPagedCallable().futureCall(request);
       // Do something.
       for (Location element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.ListLocationsRequest,[ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.VmwareEngineClient.ListLocationsPagedResponse)>` |   
  
### listLoggingServers(@Nullable PrivateCloudName parent)
    
    
    public final VmwareEngineClient.ListLoggingServersPagedResponse listLoggingServers(@Nullable PrivateCloudName parent)

Lists logging servers configured for a given private cloud.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       PrivateCloudName parent = PrivateCloudName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_CLOUD]");
       for (LoggingServer element : vmwareEngineClient.listLoggingServers(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.vmwareengine.v1.PrivateCloudName`  
Required. The resource name of the private cloud to be queried for logging servers. Resource names are schemeless URIs that follow the conventions in <https://cloud.google.com/apis/design/resource_names>. For example: `projects/my-project/locations/us-central1-a/privateClouds/my-cloud`  
**Returns**  
---  
**Type** | **Description**  
`[VmwareEngineClient.ListLoggingServersPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.VmwareEngineClient.ListLoggingServersPagedResponse)` |   
  
### listLoggingServers(ListLoggingServersRequest request)
    
    
    public final VmwareEngineClient.ListLoggingServersPagedResponse listLoggingServers(ListLoggingServersRequest request)

Lists logging servers configured for a given private cloud.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       ListLoggingServersRequest request =
           ListLoggingServersRequest.newBuilder()
               .setParent(
                   PrivateCloudName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_CLOUD]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       for (LoggingServer element : vmwareEngineClient.listLoggingServers(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListLoggingServersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.ListLoggingServersRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[VmwareEngineClient.ListLoggingServersPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.VmwareEngineClient.ListLoggingServersPagedResponse)` |   
  
### listLoggingServers(String parent)
    
    
    public final VmwareEngineClient.ListLoggingServersPagedResponse listLoggingServers(String parent)

Lists logging servers configured for a given private cloud.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       String parent = PrivateCloudName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_CLOUD]").toString();
       for (LoggingServer element : vmwareEngineClient.listLoggingServers(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the private cloud to be queried for logging servers. Resource names are schemeless URIs that follow the conventions in <https://cloud.google.com/apis/design/resource_names>. For example: `projects/my-project/locations/us-central1-a/privateClouds/my-cloud`  
**Returns**  
---  
**Type** | **Description**  
`[VmwareEngineClient.ListLoggingServersPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.VmwareEngineClient.ListLoggingServersPagedResponse)` |   
  
### listLoggingServersCallable()
    
    
    public final UnaryCallable<ListLoggingServersRequest,ListLoggingServersResponse> listLoggingServersCallable()

Lists logging servers configured for a given private cloud.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       ListLoggingServersRequest request =
           ListLoggingServersRequest.newBuilder()
               .setParent(
                   PrivateCloudName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_CLOUD]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       while (true) {
         ListLoggingServersResponse response =
             vmwareEngineClient.listLoggingServersCallable().call(request);
         for (LoggingServer element : response.getLoggingServersList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListLoggingServersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.ListLoggingServersRequest),[ListLoggingServersResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.ListLoggingServersResponse)>` |   
  
### listLoggingServersPagedCallable()
    
    
    public final UnaryCallable<ListLoggingServersRequest,VmwareEngineClient.ListLoggingServersPagedResponse> listLoggingServersPagedCallable()

Lists logging servers configured for a given private cloud.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       ListLoggingServersRequest request =
           ListLoggingServersRequest.newBuilder()
               .setParent(
                   PrivateCloudName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_CLOUD]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       ApiFuture<LoggingServer> future =
           vmwareEngineClient.listLoggingServersPagedCallable().futureCall(request);
       // Do something.
       for (LoggingServer element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListLoggingServersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.ListLoggingServersRequest),[ListLoggingServersPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.VmwareEngineClient.ListLoggingServersPagedResponse)>` |   
  
### listManagementDnsZoneBindings(@Nullable PrivateCloudName parent)
    
    
    public final VmwareEngineClient.ListManagementDnsZoneBindingsPagedResponse listManagementDnsZoneBindings(@Nullable PrivateCloudName parent)

Lists Consumer VPCs bound to Management DNS Zone of a given private cloud.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       PrivateCloudName parent = PrivateCloudName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_CLOUD]");
       for (ManagementDnsZoneBinding element :
           vmwareEngineClient.listManagementDnsZoneBindings(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.vmwareengine.v1.PrivateCloudName`  
Required. The resource name of the private cloud to be queried for management DNS zone bindings. Resource names are schemeless URIs that follow the conventions in <https://cloud.google.com/apis/design/resource_names>. For example: `projects/my-project/locations/us-central1-a/privateClouds/my-cloud`  
**Returns**  
---  
**Type** | **Description**  
`[VmwareEngineClient.ListManagementDnsZoneBindingsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.VmwareEngineClient.ListManagementDnsZoneBindingsPagedResponse)` |   
  
### listManagementDnsZoneBindings(ListManagementDnsZoneBindingsRequest request)
    
    
    public final VmwareEngineClient.ListManagementDnsZoneBindingsPagedResponse listManagementDnsZoneBindings(ListManagementDnsZoneBindingsRequest request)

Lists Consumer VPCs bound to Management DNS Zone of a given private cloud.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       ListManagementDnsZoneBindingsRequest request =
           ListManagementDnsZoneBindingsRequest.newBuilder()
               .setParent(
                   PrivateCloudName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_CLOUD]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       for (ManagementDnsZoneBinding element :
           vmwareEngineClient.listManagementDnsZoneBindings(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListManagementDnsZoneBindingsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.ListManagementDnsZoneBindingsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[VmwareEngineClient.ListManagementDnsZoneBindingsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.VmwareEngineClient.ListManagementDnsZoneBindingsPagedResponse)` |   
  
### listManagementDnsZoneBindings(String parent)
    
    
    public final VmwareEngineClient.ListManagementDnsZoneBindingsPagedResponse listManagementDnsZoneBindings(String parent)

Lists Consumer VPCs bound to Management DNS Zone of a given private cloud.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       String parent = PrivateCloudName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_CLOUD]").toString();
       for (ManagementDnsZoneBinding element :
           vmwareEngineClient.listManagementDnsZoneBindings(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the private cloud to be queried for management DNS zone bindings. Resource names are schemeless URIs that follow the conventions in <https://cloud.google.com/apis/design/resource_names>. For example: `projects/my-project/locations/us-central1-a/privateClouds/my-cloud`  
**Returns**  
---  
**Type** | **Description**  
`[VmwareEngineClient.ListManagementDnsZoneBindingsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.VmwareEngineClient.ListManagementDnsZoneBindingsPagedResponse)` |   
  
### listManagementDnsZoneBindingsCallable()
    
    
    public final UnaryCallable<ListManagementDnsZoneBindingsRequest,ListManagementDnsZoneBindingsResponse> listManagementDnsZoneBindingsCallable()

Lists Consumer VPCs bound to Management DNS Zone of a given private cloud.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       ListManagementDnsZoneBindingsRequest request =
           ListManagementDnsZoneBindingsRequest.newBuilder()
               .setParent(
                   PrivateCloudName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_CLOUD]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       while (true) {
         ListManagementDnsZoneBindingsResponse response =
             vmwareEngineClient.listManagementDnsZoneBindingsCallable().call(request);
         for (ManagementDnsZoneBinding element : response.getManagementDnsZoneBindingsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListManagementDnsZoneBindingsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.ListManagementDnsZoneBindingsRequest),[ListManagementDnsZoneBindingsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.ListManagementDnsZoneBindingsResponse)>` |   
  
### listManagementDnsZoneBindingsPagedCallable()
    
    
    public final UnaryCallable<ListManagementDnsZoneBindingsRequest,VmwareEngineClient.ListManagementDnsZoneBindingsPagedResponse> listManagementDnsZoneBindingsPagedCallable()

Lists Consumer VPCs bound to Management DNS Zone of a given private cloud.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       ListManagementDnsZoneBindingsRequest request =
           ListManagementDnsZoneBindingsRequest.newBuilder()
               .setParent(
                   PrivateCloudName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_CLOUD]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       ApiFuture<ManagementDnsZoneBinding> future =
           vmwareEngineClient.listManagementDnsZoneBindingsPagedCallable().futureCall(request);
       // Do something.
       for (ManagementDnsZoneBinding element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListManagementDnsZoneBindingsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.ListManagementDnsZoneBindingsRequest),[ListManagementDnsZoneBindingsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.VmwareEngineClient.ListManagementDnsZoneBindingsPagedResponse)>` |   
  
### listNetworkPeerings(@Nullable LocationName parent)
    
    
    public final VmwareEngineClient.ListNetworkPeeringsPagedResponse listNetworkPeerings(@Nullable LocationName parent)

Lists `NetworkPeering` resources in a given project. NetworkPeering is a global resource and location can only be global.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (NetworkPeering element : vmwareEngineClient.listNetworkPeerings(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.vmwareengine.v1.LocationName`  
Required. The resource name of the location (global) to query for network peerings. Resource names are schemeless URIs that follow the conventions in <https://cloud.google.com/apis/design/resource_names>. For example: `projects/my-project/locations/global`  
**Returns**  
---  
**Type** | **Description**  
`[VmwareEngineClient.ListNetworkPeeringsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.VmwareEngineClient.ListNetworkPeeringsPagedResponse)` |   
  
### listNetworkPeerings(ListNetworkPeeringsRequest request)
    
    
    public final VmwareEngineClient.ListNetworkPeeringsPagedResponse listNetworkPeerings(ListNetworkPeeringsRequest request)

Lists `NetworkPeering` resources in a given project. NetworkPeering is a global resource and location can only be global.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       ListNetworkPeeringsRequest request =
           ListNetworkPeeringsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       for (NetworkPeering element : vmwareEngineClient.listNetworkPeerings(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListNetworkPeeringsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.ListNetworkPeeringsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[VmwareEngineClient.ListNetworkPeeringsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.VmwareEngineClient.ListNetworkPeeringsPagedResponse)` |   
  
### listNetworkPeerings(String parent)
    
    
    public final VmwareEngineClient.ListNetworkPeeringsPagedResponse listNetworkPeerings(String parent)

Lists `NetworkPeering` resources in a given project. NetworkPeering is a global resource and location can only be global.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (NetworkPeering element : vmwareEngineClient.listNetworkPeerings(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the location (global) to query for network peerings. Resource names are schemeless URIs that follow the conventions in <https://cloud.google.com/apis/design/resource_names>. For example: `projects/my-project/locations/global`  
**Returns**  
---  
**Type** | **Description**  
`[VmwareEngineClient.ListNetworkPeeringsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.VmwareEngineClient.ListNetworkPeeringsPagedResponse)` |   
  
### listNetworkPeeringsCallable()
    
    
    public final UnaryCallable<ListNetworkPeeringsRequest,ListNetworkPeeringsResponse> listNetworkPeeringsCallable()

Lists `NetworkPeering` resources in a given project. NetworkPeering is a global resource and location can only be global.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       ListNetworkPeeringsRequest request =
           ListNetworkPeeringsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       while (true) {
         ListNetworkPeeringsResponse response =
             vmwareEngineClient.listNetworkPeeringsCallable().call(request);
         for (NetworkPeering element : response.getNetworkPeeringsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListNetworkPeeringsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.ListNetworkPeeringsRequest),[ListNetworkPeeringsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.ListNetworkPeeringsResponse)>` |   
  
### listNetworkPeeringsPagedCallable()
    
    
    public final UnaryCallable<ListNetworkPeeringsRequest,VmwareEngineClient.ListNetworkPeeringsPagedResponse> listNetworkPeeringsPagedCallable()

Lists `NetworkPeering` resources in a given project. NetworkPeering is a global resource and location can only be global.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       ListNetworkPeeringsRequest request =
           ListNetworkPeeringsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       ApiFuture<NetworkPeering> future =
           vmwareEngineClient.listNetworkPeeringsPagedCallable().futureCall(request);
       // Do something.
       for (NetworkPeering element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListNetworkPeeringsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.ListNetworkPeeringsRequest),[ListNetworkPeeringsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.VmwareEngineClient.ListNetworkPeeringsPagedResponse)>` |   
  
### listNetworkPolicies(@Nullable LocationName parent)
    
    
    public final VmwareEngineClient.ListNetworkPoliciesPagedResponse listNetworkPolicies(@Nullable LocationName parent)

Lists `NetworkPolicy` resources in a specified project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (NetworkPolicy element : vmwareEngineClient.listNetworkPolicies(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.vmwareengine.v1.LocationName`  
Required. The resource name of the location (region) to query for network policies. Resource names are schemeless URIs that follow the conventions in <https://cloud.google.com/apis/design/resource_names>. For example: `projects/my-project/locations/us-central1`  
**Returns**  
---  
**Type** | **Description**  
`[VmwareEngineClient.ListNetworkPoliciesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.VmwareEngineClient.ListNetworkPoliciesPagedResponse)` |   
  
### listNetworkPolicies(ListNetworkPoliciesRequest request)
    
    
    public final VmwareEngineClient.ListNetworkPoliciesPagedResponse listNetworkPolicies(ListNetworkPoliciesRequest request)

Lists `NetworkPolicy` resources in a specified project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       ListNetworkPoliciesRequest request =
           ListNetworkPoliciesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       for (NetworkPolicy element : vmwareEngineClient.listNetworkPolicies(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListNetworkPoliciesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.ListNetworkPoliciesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[VmwareEngineClient.ListNetworkPoliciesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.VmwareEngineClient.ListNetworkPoliciesPagedResponse)` |   
  
### listNetworkPolicies(String parent)
    
    
    public final VmwareEngineClient.ListNetworkPoliciesPagedResponse listNetworkPolicies(String parent)

Lists `NetworkPolicy` resources in a specified project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (NetworkPolicy element : vmwareEngineClient.listNetworkPolicies(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the location (region) to query for network policies. Resource names are schemeless URIs that follow the conventions in <https://cloud.google.com/apis/design/resource_names>. For example: `projects/my-project/locations/us-central1`  
**Returns**  
---  
**Type** | **Description**  
`[VmwareEngineClient.ListNetworkPoliciesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.VmwareEngineClient.ListNetworkPoliciesPagedResponse)` |   
  
### listNetworkPoliciesCallable()
    
    
    public final UnaryCallable<ListNetworkPoliciesRequest,ListNetworkPoliciesResponse> listNetworkPoliciesCallable()

Lists `NetworkPolicy` resources in a specified project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       ListNetworkPoliciesRequest request =
           ListNetworkPoliciesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       while (true) {
         ListNetworkPoliciesResponse response =
             vmwareEngineClient.listNetworkPoliciesCallable().call(request);
         for (NetworkPolicy element : response.getNetworkPoliciesList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListNetworkPoliciesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.ListNetworkPoliciesRequest),[ListNetworkPoliciesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.ListNetworkPoliciesResponse)>` |   
  
### listNetworkPoliciesPagedCallable()
    
    
    public final UnaryCallable<ListNetworkPoliciesRequest,VmwareEngineClient.ListNetworkPoliciesPagedResponse> listNetworkPoliciesPagedCallable()

Lists `NetworkPolicy` resources in a specified project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       ListNetworkPoliciesRequest request =
           ListNetworkPoliciesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       ApiFuture<NetworkPolicy> future =
           vmwareEngineClient.listNetworkPoliciesPagedCallable().futureCall(request);
       // Do something.
       for (NetworkPolicy element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListNetworkPoliciesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.ListNetworkPoliciesRequest),[ListNetworkPoliciesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.VmwareEngineClient.ListNetworkPoliciesPagedResponse)>` |   
  
### listNodeTypes(@Nullable LocationName parent)
    
    
    public final VmwareEngineClient.ListNodeTypesPagedResponse listNodeTypes(@Nullable LocationName parent)

Lists node types

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (NodeType element : vmwareEngineClient.listNodeTypes(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.vmwareengine.v1.LocationName`  
Required. The resource name of the location to be queried for node types. Resource names are schemeless URIs that follow the conventions in <https://cloud.google.com/apis/design/resource_names>. For example: `projects/my-project/locations/us-central1-a`  
**Returns**  
---  
**Type** | **Description**  
`[VmwareEngineClient.ListNodeTypesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.VmwareEngineClient.ListNodeTypesPagedResponse)` |   
  
### listNodeTypes(ListNodeTypesRequest request)
    
    
    public final VmwareEngineClient.ListNodeTypesPagedResponse listNodeTypes(ListNodeTypesRequest request)

Lists node types

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       ListNodeTypesRequest request =
           ListNodeTypesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       for (NodeType element : vmwareEngineClient.listNodeTypes(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListNodeTypesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.ListNodeTypesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[VmwareEngineClient.ListNodeTypesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.VmwareEngineClient.ListNodeTypesPagedResponse)` |   
  
### listNodeTypes(String parent)
    
    
    public final VmwareEngineClient.ListNodeTypesPagedResponse listNodeTypes(String parent)

Lists node types

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (NodeType element : vmwareEngineClient.listNodeTypes(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the location to be queried for node types. Resource names are schemeless URIs that follow the conventions in <https://cloud.google.com/apis/design/resource_names>. For example: `projects/my-project/locations/us-central1-a`  
**Returns**  
---  
**Type** | **Description**  
`[VmwareEngineClient.ListNodeTypesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.VmwareEngineClient.ListNodeTypesPagedResponse)` |   
  
### listNodeTypesCallable()
    
    
    public final UnaryCallable<ListNodeTypesRequest,ListNodeTypesResponse> listNodeTypesCallable()

Lists node types

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       ListNodeTypesRequest request =
           ListNodeTypesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       while (true) {
         ListNodeTypesResponse response = vmwareEngineClient.listNodeTypesCallable().call(request);
         for (NodeType element : response.getNodeTypesList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListNodeTypesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.ListNodeTypesRequest),[ListNodeTypesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.ListNodeTypesResponse)>` |   
  
### listNodeTypesPagedCallable()
    
    
    public final UnaryCallable<ListNodeTypesRequest,VmwareEngineClient.ListNodeTypesPagedResponse> listNodeTypesPagedCallable()

Lists node types

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       ListNodeTypesRequest request =
           ListNodeTypesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       ApiFuture<NodeType> future =
           vmwareEngineClient.listNodeTypesPagedCallable().futureCall(request);
       // Do something.
       for (NodeType element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListNodeTypesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.ListNodeTypesRequest),[ListNodeTypesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.VmwareEngineClient.ListNodeTypesPagedResponse)>` |   
  
### listNodes(@Nullable ClusterName parent)
    
    
    public final VmwareEngineClient.ListNodesPagedResponse listNodes(@Nullable ClusterName parent)

Lists nodes in a given cluster.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       ClusterName parent =
           ClusterName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_CLOUD]", "[CLUSTER]");
       for (Node element : vmwareEngineClient.listNodes(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.vmwareengine.v1.ClusterName`  
Required. The resource name of the cluster to be queried for nodes. Resource names are schemeless URIs that follow the conventions in <https://cloud.google.com/apis/design/resource_names>. For example: `projects/my-project/locations/us-central1-a/privateClouds/my-cloud/clusters/my-cluster`  
**Returns**  
---  
**Type** | **Description**  
`[VmwareEngineClient.ListNodesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.VmwareEngineClient.ListNodesPagedResponse)` |   
  
### listNodes(ListNodesRequest request)
    
    
    public final VmwareEngineClient.ListNodesPagedResponse listNodes(ListNodesRequest request)

Lists nodes in a given cluster.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       ListNodesRequest request =
           ListNodesRequest.newBuilder()
               .setParent(
                   ClusterName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_CLOUD]", "[CLUSTER]")
                       .toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (Node element : vmwareEngineClient.listNodes(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListNodesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.ListNodesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[VmwareEngineClient.ListNodesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.VmwareEngineClient.ListNodesPagedResponse)` |   
  
### listNodes(String parent)
    
    
    public final VmwareEngineClient.ListNodesPagedResponse listNodes(String parent)

Lists nodes in a given cluster.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       String parent =
           ClusterName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_CLOUD]", "[CLUSTER]").toString();
       for (Node element : vmwareEngineClient.listNodes(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the cluster to be queried for nodes. Resource names are schemeless URIs that follow the conventions in <https://cloud.google.com/apis/design/resource_names>. For example: `projects/my-project/locations/us-central1-a/privateClouds/my-cloud/clusters/my-cluster`  
**Returns**  
---  
**Type** | **Description**  
`[VmwareEngineClient.ListNodesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.VmwareEngineClient.ListNodesPagedResponse)` |   
  
### listNodesCallable()
    
    
    public final UnaryCallable<ListNodesRequest,ListNodesResponse> listNodesCallable()

Lists nodes in a given cluster.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       ListNodesRequest request =
           ListNodesRequest.newBuilder()
               .setParent(
                   ClusterName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_CLOUD]", "[CLUSTER]")
                       .toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListNodesResponse response = vmwareEngineClient.listNodesCallable().call(request);
         for (Node element : response.getNodesList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListNodesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.ListNodesRequest),[ListNodesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.ListNodesResponse)>` |   
  
### listNodesPagedCallable()
    
    
    public final UnaryCallable<ListNodesRequest,VmwareEngineClient.ListNodesPagedResponse> listNodesPagedCallable()

Lists nodes in a given cluster.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       ListNodesRequest request =
           ListNodesRequest.newBuilder()
               .setParent(
                   ClusterName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_CLOUD]", "[CLUSTER]")
                       .toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<Node> future = vmwareEngineClient.listNodesPagedCallable().futureCall(request);
       // Do something.
       for (Node element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListNodesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.ListNodesRequest),[ListNodesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.VmwareEngineClient.ListNodesPagedResponse)>` |   
  
### listPeeringRoutes(@Nullable NetworkPeeringName parent)
    
    
    public final VmwareEngineClient.ListPeeringRoutesPagedResponse listPeeringRoutes(@Nullable NetworkPeeringName parent)

Lists the network peering routes exchanged over a peering connection. NetworkPeering is a global resource and location can only be global.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       NetworkPeeringName parent =
           NetworkPeeringName.of("[PROJECT]", "[LOCATION]", "[NETWORK_PEERING]");
       for (PeeringRoute element : vmwareEngineClient.listPeeringRoutes(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.vmwareengine.v1.NetworkPeeringName`  
Required. The resource name of the network peering to retrieve peering routes from. Resource names are schemeless URIs that follow the conventions in <https://cloud.google.com/apis/design/resource_names>. For example: `projects/my-project/locations/global/networkPeerings/my-peering`  
**Returns**  
---  
**Type** | **Description**  
`[VmwareEngineClient.ListPeeringRoutesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.VmwareEngineClient.ListPeeringRoutesPagedResponse)` |   
  
### listPeeringRoutes(ListPeeringRoutesRequest request)
    
    
    public final VmwareEngineClient.ListPeeringRoutesPagedResponse listPeeringRoutes(ListPeeringRoutesRequest request)

Lists the network peering routes exchanged over a peering connection. NetworkPeering is a global resource and location can only be global.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       ListPeeringRoutesRequest request =
           ListPeeringRoutesRequest.newBuilder()
               .setParent(
                   NetworkPeeringName.of("[PROJECT]", "[LOCATION]", "[NETWORK_PEERING]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       for (PeeringRoute element : vmwareEngineClient.listPeeringRoutes(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListPeeringRoutesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.ListPeeringRoutesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[VmwareEngineClient.ListPeeringRoutesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.VmwareEngineClient.ListPeeringRoutesPagedResponse)` |   
  
### listPeeringRoutes(String parent)
    
    
    public final VmwareEngineClient.ListPeeringRoutesPagedResponse listPeeringRoutes(String parent)

Lists the network peering routes exchanged over a peering connection. NetworkPeering is a global resource and location can only be global.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       String parent =
           NetworkPeeringName.of("[PROJECT]", "[LOCATION]", "[NETWORK_PEERING]").toString();
       for (PeeringRoute element : vmwareEngineClient.listPeeringRoutes(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the network peering to retrieve peering routes from. Resource names are schemeless URIs that follow the conventions in <https://cloud.google.com/apis/design/resource_names>. For example: `projects/my-project/locations/global/networkPeerings/my-peering`  
**Returns**  
---  
**Type** | **Description**  
`[VmwareEngineClient.ListPeeringRoutesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.VmwareEngineClient.ListPeeringRoutesPagedResponse)` |   
  
### listPeeringRoutesCallable()
    
    
    public final UnaryCallable<ListPeeringRoutesRequest,ListPeeringRoutesResponse> listPeeringRoutesCallable()

Lists the network peering routes exchanged over a peering connection. NetworkPeering is a global resource and location can only be global.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       ListPeeringRoutesRequest request =
           ListPeeringRoutesRequest.newBuilder()
               .setParent(
                   NetworkPeeringName.of("[PROJECT]", "[LOCATION]", "[NETWORK_PEERING]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       while (true) {
         ListPeeringRoutesResponse response =
             vmwareEngineClient.listPeeringRoutesCallable().call(request);
         for (PeeringRoute element : response.getPeeringRoutesList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListPeeringRoutesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.ListPeeringRoutesRequest),[ListPeeringRoutesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.ListPeeringRoutesResponse)>` |   
  
### listPeeringRoutesPagedCallable()
    
    
    public final UnaryCallable<ListPeeringRoutesRequest,VmwareEngineClient.ListPeeringRoutesPagedResponse> listPeeringRoutesPagedCallable()

Lists the network peering routes exchanged over a peering connection. NetworkPeering is a global resource and location can only be global.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       ListPeeringRoutesRequest request =
           ListPeeringRoutesRequest.newBuilder()
               .setParent(
                   NetworkPeeringName.of("[PROJECT]", "[LOCATION]", "[NETWORK_PEERING]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       ApiFuture<PeeringRoute> future =
           vmwareEngineClient.listPeeringRoutesPagedCallable().futureCall(request);
       // Do something.
       for (PeeringRoute element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListPeeringRoutesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.ListPeeringRoutesRequest),[ListPeeringRoutesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.VmwareEngineClient.ListPeeringRoutesPagedResponse)>` |   
  
### listPrivateClouds(@Nullable LocationName parent)
    
    
    public final VmwareEngineClient.ListPrivateCloudsPagedResponse listPrivateClouds(@Nullable LocationName parent)

Lists `PrivateCloud` resources in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (PrivateCloud element : vmwareEngineClient.listPrivateClouds(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.vmwareengine.v1.LocationName`  
Required. The resource name of the private cloud to be queried for clusters. Resource names are schemeless URIs that follow the conventions in <https://cloud.google.com/apis/design/resource_names>. For example: `projects/my-project/locations/us-central1-a`  
**Returns**  
---  
**Type** | **Description**  
`[VmwareEngineClient.ListPrivateCloudsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.VmwareEngineClient.ListPrivateCloudsPagedResponse)` |   
  
### listPrivateClouds(ListPrivateCloudsRequest request)
    
    
    public final VmwareEngineClient.ListPrivateCloudsPagedResponse listPrivateClouds(ListPrivateCloudsRequest request)

Lists `PrivateCloud` resources in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       ListPrivateCloudsRequest request =
           ListPrivateCloudsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       for (PrivateCloud element : vmwareEngineClient.listPrivateClouds(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListPrivateCloudsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.ListPrivateCloudsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[VmwareEngineClient.ListPrivateCloudsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.VmwareEngineClient.ListPrivateCloudsPagedResponse)` |   
  
### listPrivateClouds(String parent)
    
    
    public final VmwareEngineClient.ListPrivateCloudsPagedResponse listPrivateClouds(String parent)

Lists `PrivateCloud` resources in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (PrivateCloud element : vmwareEngineClient.listPrivateClouds(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the private cloud to be queried for clusters. Resource names are schemeless URIs that follow the conventions in <https://cloud.google.com/apis/design/resource_names>. For example: `projects/my-project/locations/us-central1-a`  
**Returns**  
---  
**Type** | **Description**  
`[VmwareEngineClient.ListPrivateCloudsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.VmwareEngineClient.ListPrivateCloudsPagedResponse)` |   
  
### listPrivateCloudsCallable()
    
    
    public final UnaryCallable<ListPrivateCloudsRequest,ListPrivateCloudsResponse> listPrivateCloudsCallable()

Lists `PrivateCloud` resources in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       ListPrivateCloudsRequest request =
           ListPrivateCloudsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       while (true) {
         ListPrivateCloudsResponse response =
             vmwareEngineClient.listPrivateCloudsCallable().call(request);
         for (PrivateCloud element : response.getPrivateCloudsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListPrivateCloudsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.ListPrivateCloudsRequest),[ListPrivateCloudsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.ListPrivateCloudsResponse)>` |   
  
### listPrivateCloudsPagedCallable()
    
    
    public final UnaryCallable<ListPrivateCloudsRequest,VmwareEngineClient.ListPrivateCloudsPagedResponse> listPrivateCloudsPagedCallable()

Lists `PrivateCloud` resources in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       ListPrivateCloudsRequest request =
           ListPrivateCloudsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       ApiFuture<PrivateCloud> future =
           vmwareEngineClient.listPrivateCloudsPagedCallable().futureCall(request);
       // Do something.
       for (PrivateCloud element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListPrivateCloudsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.ListPrivateCloudsRequest),[ListPrivateCloudsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.VmwareEngineClient.ListPrivateCloudsPagedResponse)>` |   
  
### listPrivateConnectionPeeringRoutes(@Nullable PrivateConnectionName parent)
    
    
    public final VmwareEngineClient.ListPrivateConnectionPeeringRoutesPagedResponse listPrivateConnectionPeeringRoutes(@Nullable PrivateConnectionName parent)

Lists the private connection routes exchanged over a peering connection.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       PrivateConnectionName parent =
           PrivateConnectionName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_CONNECTION]");
       for (PeeringRoute element :
           vmwareEngineClient.listPrivateConnectionPeeringRoutes(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.vmwareengine.v1.PrivateConnectionName`  
Required. The resource name of the private connection to retrieve peering routes from. Resource names are schemeless URIs that follow the conventions in <https://cloud.google.com/apis/design/resource_names>. For example: `projects/my-project/locations/us-west1/privateConnections/my-connection`  
**Returns**  
---  
**Type** | **Description**  
`[VmwareEngineClient.ListPrivateConnectionPeeringRoutesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.VmwareEngineClient.ListPrivateConnectionPeeringRoutesPagedResponse)` |   
  
### listPrivateConnectionPeeringRoutes(ListPrivateConnectionPeeringRoutesRequest request)
    
    
    public final VmwareEngineClient.ListPrivateConnectionPeeringRoutesPagedResponse listPrivateConnectionPeeringRoutes(ListPrivateConnectionPeeringRoutesRequest request)

Lists the private connection routes exchanged over a peering connection.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       ListPrivateConnectionPeeringRoutesRequest request =
           ListPrivateConnectionPeeringRoutesRequest.newBuilder()
               .setParent(
                   PrivateConnectionName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_CONNECTION]")
                       .toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (PeeringRoute element :
           vmwareEngineClient.listPrivateConnectionPeeringRoutes(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListPrivateConnectionPeeringRoutesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.ListPrivateConnectionPeeringRoutesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[VmwareEngineClient.ListPrivateConnectionPeeringRoutesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.VmwareEngineClient.ListPrivateConnectionPeeringRoutesPagedResponse)` |   
  
### listPrivateConnectionPeeringRoutes(String parent)
    
    
    public final VmwareEngineClient.ListPrivateConnectionPeeringRoutesPagedResponse listPrivateConnectionPeeringRoutes(String parent)

Lists the private connection routes exchanged over a peering connection.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       String parent =
           PrivateConnectionName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_CONNECTION]").toString();
       for (PeeringRoute element :
           vmwareEngineClient.listPrivateConnectionPeeringRoutes(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the private connection to retrieve peering routes from. Resource names are schemeless URIs that follow the conventions in <https://cloud.google.com/apis/design/resource_names>. For example: `projects/my-project/locations/us-west1/privateConnections/my-connection`  
**Returns**  
---  
**Type** | **Description**  
`[VmwareEngineClient.ListPrivateConnectionPeeringRoutesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.VmwareEngineClient.ListPrivateConnectionPeeringRoutesPagedResponse)` |   
  
### listPrivateConnectionPeeringRoutesCallable()
    
    
    public final UnaryCallable<ListPrivateConnectionPeeringRoutesRequest,ListPrivateConnectionPeeringRoutesResponse> listPrivateConnectionPeeringRoutesCallable()

Lists the private connection routes exchanged over a peering connection.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       ListPrivateConnectionPeeringRoutesRequest request =
           ListPrivateConnectionPeeringRoutesRequest.newBuilder()
               .setParent(
                   PrivateConnectionName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_CONNECTION]")
                       .toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListPrivateConnectionPeeringRoutesResponse response =
             vmwareEngineClient.listPrivateConnectionPeeringRoutesCallable().call(request);
         for (PeeringRoute element : response.getPeeringRoutesList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListPrivateConnectionPeeringRoutesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.ListPrivateConnectionPeeringRoutesRequest),[ListPrivateConnectionPeeringRoutesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.ListPrivateConnectionPeeringRoutesResponse)>` |   
  
### listPrivateConnectionPeeringRoutesPagedCallable()
    
    
    public final UnaryCallable<ListPrivateConnectionPeeringRoutesRequest,VmwareEngineClient.ListPrivateConnectionPeeringRoutesPagedResponse> listPrivateConnectionPeeringRoutesPagedCallable()

Lists the private connection routes exchanged over a peering connection.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       ListPrivateConnectionPeeringRoutesRequest request =
           ListPrivateConnectionPeeringRoutesRequest.newBuilder()
               .setParent(
                   PrivateConnectionName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_CONNECTION]")
                       .toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<PeeringRoute> future =
           vmwareEngineClient.listPrivateConnectionPeeringRoutesPagedCallable().futureCall(request);
       // Do something.
       for (PeeringRoute element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListPrivateConnectionPeeringRoutesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.ListPrivateConnectionPeeringRoutesRequest),[ListPrivateConnectionPeeringRoutesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.VmwareEngineClient.ListPrivateConnectionPeeringRoutesPagedResponse)>` |   
  
### listPrivateConnections(@Nullable LocationName parent)
    
    
    public final VmwareEngineClient.ListPrivateConnectionsPagedResponse listPrivateConnections(@Nullable LocationName parent)

Lists `PrivateConnection` resources in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (PrivateConnection element :
           vmwareEngineClient.listPrivateConnections(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.vmwareengine.v1.LocationName`  
Required. The resource name of the location to query for private connections. Resource names are schemeless URIs that follow the conventions in <https://cloud.google.com/apis/design/resource_names>. For example: `projects/my-project/locations/us-central1`  
**Returns**  
---  
**Type** | **Description**  
`[VmwareEngineClient.ListPrivateConnectionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.VmwareEngineClient.ListPrivateConnectionsPagedResponse)` |   
  
### listPrivateConnections(ListPrivateConnectionsRequest request)
    
    
    public final VmwareEngineClient.ListPrivateConnectionsPagedResponse listPrivateConnections(ListPrivateConnectionsRequest request)

Lists `PrivateConnection` resources in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       ListPrivateConnectionsRequest request =
           ListPrivateConnectionsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       for (PrivateConnection element :
           vmwareEngineClient.listPrivateConnections(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListPrivateConnectionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.ListPrivateConnectionsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[VmwareEngineClient.ListPrivateConnectionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.VmwareEngineClient.ListPrivateConnectionsPagedResponse)` |   
  
### listPrivateConnections(String parent)
    
    
    public final VmwareEngineClient.ListPrivateConnectionsPagedResponse listPrivateConnections(String parent)

Lists `PrivateConnection` resources in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (PrivateConnection element :
           vmwareEngineClient.listPrivateConnections(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the location to query for private connections. Resource names are schemeless URIs that follow the conventions in <https://cloud.google.com/apis/design/resource_names>. For example: `projects/my-project/locations/us-central1`  
**Returns**  
---  
**Type** | **Description**  
`[VmwareEngineClient.ListPrivateConnectionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.VmwareEngineClient.ListPrivateConnectionsPagedResponse)` |   
  
### listPrivateConnectionsCallable()
    
    
    public final UnaryCallable<ListPrivateConnectionsRequest,ListPrivateConnectionsResponse> listPrivateConnectionsCallable()

Lists `PrivateConnection` resources in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       ListPrivateConnectionsRequest request =
           ListPrivateConnectionsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       while (true) {
         ListPrivateConnectionsResponse response =
             vmwareEngineClient.listPrivateConnectionsCallable().call(request);
         for (PrivateConnection element : response.getPrivateConnectionsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListPrivateConnectionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.ListPrivateConnectionsRequest),[ListPrivateConnectionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.ListPrivateConnectionsResponse)>` |   
  
### listPrivateConnectionsPagedCallable()
    
    
    public final UnaryCallable<ListPrivateConnectionsRequest,VmwareEngineClient.ListPrivateConnectionsPagedResponse> listPrivateConnectionsPagedCallable()

Lists `PrivateConnection` resources in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       ListPrivateConnectionsRequest request =
           ListPrivateConnectionsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       ApiFuture<PrivateConnection> future =
           vmwareEngineClient.listPrivateConnectionsPagedCallable().futureCall(request);
       // Do something.
       for (PrivateConnection element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListPrivateConnectionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.ListPrivateConnectionsRequest),[ListPrivateConnectionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.VmwareEngineClient.ListPrivateConnectionsPagedResponse)>` |   
  
### listSubnets(@Nullable PrivateCloudName parent)
    
    
    public final VmwareEngineClient.ListSubnetsPagedResponse listSubnets(@Nullable PrivateCloudName parent)

Lists subnets in a given private cloud.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       PrivateCloudName parent = PrivateCloudName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_CLOUD]");
       for (Subnet element : vmwareEngineClient.listSubnets(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.vmwareengine.v1.PrivateCloudName`  
Required. The resource name of the private cloud to be queried for subnets. Resource names are schemeless URIs that follow the conventions in <https://cloud.google.com/apis/design/resource_names>. For example: `projects/my-project/locations/us-central1-a/privateClouds/my-cloud`  
**Returns**  
---  
**Type** | **Description**  
`[VmwareEngineClient.ListSubnetsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.VmwareEngineClient.ListSubnetsPagedResponse)` |   
  
### listSubnets(ListSubnetsRequest request)
    
    
    public final VmwareEngineClient.ListSubnetsPagedResponse listSubnets(ListSubnetsRequest request)

Lists subnets in a given private cloud.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       ListSubnetsRequest request =
           ListSubnetsRequest.newBuilder()
               .setParent(
                   PrivateCloudName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_CLOUD]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (Subnet element : vmwareEngineClient.listSubnets(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListSubnetsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.ListSubnetsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[VmwareEngineClient.ListSubnetsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.VmwareEngineClient.ListSubnetsPagedResponse)` |   
  
### listSubnets(String parent)
    
    
    public final VmwareEngineClient.ListSubnetsPagedResponse listSubnets(String parent)

Lists subnets in a given private cloud.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       String parent = PrivateCloudName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_CLOUD]").toString();
       for (Subnet element : vmwareEngineClient.listSubnets(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the private cloud to be queried for subnets. Resource names are schemeless URIs that follow the conventions in <https://cloud.google.com/apis/design/resource_names>. For example: `projects/my-project/locations/us-central1-a/privateClouds/my-cloud`  
**Returns**  
---  
**Type** | **Description**  
`[VmwareEngineClient.ListSubnetsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.VmwareEngineClient.ListSubnetsPagedResponse)` |   
  
### listSubnetsCallable()
    
    
    public final UnaryCallable<ListSubnetsRequest,ListSubnetsResponse> listSubnetsCallable()

Lists subnets in a given private cloud.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       ListSubnetsRequest request =
           ListSubnetsRequest.newBuilder()
               .setParent(
                   PrivateCloudName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_CLOUD]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListSubnetsResponse response = vmwareEngineClient.listSubnetsCallable().call(request);
         for (Subnet element : response.getSubnetsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListSubnetsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.ListSubnetsRequest),[ListSubnetsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.ListSubnetsResponse)>` |   
  
### listSubnetsPagedCallable()
    
    
    public final UnaryCallable<ListSubnetsRequest,VmwareEngineClient.ListSubnetsPagedResponse> listSubnetsPagedCallable()

Lists subnets in a given private cloud.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       ListSubnetsRequest request =
           ListSubnetsRequest.newBuilder()
               .setParent(
                   PrivateCloudName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_CLOUD]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<Subnet> future = vmwareEngineClient.listSubnetsPagedCallable().futureCall(request);
       // Do something.
       for (Subnet element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListSubnetsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.ListSubnetsRequest),[ListSubnetsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.VmwareEngineClient.ListSubnetsPagedResponse)>` |   
  
### listVmwareEngineNetworks(@Nullable LocationName parent)
    
    
    public final VmwareEngineClient.ListVmwareEngineNetworksPagedResponse listVmwareEngineNetworks(@Nullable LocationName parent)

Lists `VmwareEngineNetwork` resources in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (VmwareEngineNetwork element :
           vmwareEngineClient.listVmwareEngineNetworks(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.vmwareengine.v1.LocationName`  
Required. The resource name of the location to query for VMware Engine networks. Resource names are schemeless URIs that follow the conventions in <https://cloud.google.com/apis/design/resource_names>. For example: `projects/my-project/locations/global`  
**Returns**  
---  
**Type** | **Description**  
`[VmwareEngineClient.ListVmwareEngineNetworksPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.VmwareEngineClient.ListVmwareEngineNetworksPagedResponse)` |   
  
### listVmwareEngineNetworks(ListVmwareEngineNetworksRequest request)
    
    
    public final VmwareEngineClient.ListVmwareEngineNetworksPagedResponse listVmwareEngineNetworks(ListVmwareEngineNetworksRequest request)

Lists `VmwareEngineNetwork` resources in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       ListVmwareEngineNetworksRequest request =
           ListVmwareEngineNetworksRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       for (VmwareEngineNetwork element :
           vmwareEngineClient.listVmwareEngineNetworks(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListVmwareEngineNetworksRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.ListVmwareEngineNetworksRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[VmwareEngineClient.ListVmwareEngineNetworksPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.VmwareEngineClient.ListVmwareEngineNetworksPagedResponse)` |   
  
### listVmwareEngineNetworks(String parent)
    
    
    public final VmwareEngineClient.ListVmwareEngineNetworksPagedResponse listVmwareEngineNetworks(String parent)

Lists `VmwareEngineNetwork` resources in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (VmwareEngineNetwork element :
           vmwareEngineClient.listVmwareEngineNetworks(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the location to query for VMware Engine networks. Resource names are schemeless URIs that follow the conventions in <https://cloud.google.com/apis/design/resource_names>. For example: `projects/my-project/locations/global`  
**Returns**  
---  
**Type** | **Description**  
`[VmwareEngineClient.ListVmwareEngineNetworksPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.VmwareEngineClient.ListVmwareEngineNetworksPagedResponse)` |   
  
### listVmwareEngineNetworksCallable()
    
    
    public final UnaryCallable<ListVmwareEngineNetworksRequest,ListVmwareEngineNetworksResponse> listVmwareEngineNetworksCallable()

Lists `VmwareEngineNetwork` resources in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       ListVmwareEngineNetworksRequest request =
           ListVmwareEngineNetworksRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       while (true) {
         ListVmwareEngineNetworksResponse response =
             vmwareEngineClient.listVmwareEngineNetworksCallable().call(request);
         for (VmwareEngineNetwork element : response.getVmwareEngineNetworksList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListVmwareEngineNetworksRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.ListVmwareEngineNetworksRequest),[ListVmwareEngineNetworksResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.ListVmwareEngineNetworksResponse)>` |   
  
### listVmwareEngineNetworksPagedCallable()
    
    
    public final UnaryCallable<ListVmwareEngineNetworksRequest,VmwareEngineClient.ListVmwareEngineNetworksPagedResponse> listVmwareEngineNetworksPagedCallable()

Lists `VmwareEngineNetwork` resources in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       ListVmwareEngineNetworksRequest request =
           ListVmwareEngineNetworksRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       ApiFuture<VmwareEngineNetwork> future =
           vmwareEngineClient.listVmwareEngineNetworksPagedCallable().futureCall(request);
       // Do something.
       for (VmwareEngineNetwork element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListVmwareEngineNetworksRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.ListVmwareEngineNetworksRequest),[ListVmwareEngineNetworksPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.VmwareEngineClient.ListVmwareEngineNetworksPagedResponse)>` |   
  
### repairManagementDnsZoneBindingAsync(@Nullable ManagementDnsZoneBindingName name)
    
    
    public final OperationFuture<ManagementDnsZoneBinding,OperationMetadata> repairManagementDnsZoneBindingAsync(@Nullable ManagementDnsZoneBindingName name)

Retries to create a `ManagementDnsZoneBinding` resource that is in failed state.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       ManagementDnsZoneBindingName name =
           ManagementDnsZoneBindingName.of(
               "[PROJECT]", "[LOCATION]", "[PRIVATE_CLOUD]", "[MANAGEMENT_DNS_ZONE_BINDING]");
       ManagementDnsZoneBinding response =
           vmwareEngineClient.repairManagementDnsZoneBindingAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.vmwareengine.v1.ManagementDnsZoneBindingName`  
Required. The resource name of the management DNS zone binding to repair. Resource names are schemeless URIs that follow the conventions in <https://cloud.google.com/apis/design/resource_names>. For example: `projects/my-project/locations/us-central1-a/privateClouds/my-cloud/managementDnsZoneBindings/my-management-dns-zone-binding`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[ManagementDnsZoneBinding](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.ManagementDnsZoneBinding),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.OperationMetadata)>` |   
  
### repairManagementDnsZoneBindingAsync(RepairManagementDnsZoneBindingRequest request)
    
    
    public final OperationFuture<ManagementDnsZoneBinding,OperationMetadata> repairManagementDnsZoneBindingAsync(RepairManagementDnsZoneBindingRequest request)

Retries to create a `ManagementDnsZoneBinding` resource that is in failed state.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       RepairManagementDnsZoneBindingRequest request =
           RepairManagementDnsZoneBindingRequest.newBuilder()
               .setName(
                   ManagementDnsZoneBindingName.of(
                           "[PROJECT]",
                           "[LOCATION]",
                           "[PRIVATE_CLOUD]",
                           "[MANAGEMENT_DNS_ZONE_BINDING]")
                       .toString())
               .setRequestId("requestId693933066")
               .build();
       ManagementDnsZoneBinding response =
           vmwareEngineClient.repairManagementDnsZoneBindingAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[RepairManagementDnsZoneBindingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.RepairManagementDnsZoneBindingRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[ManagementDnsZoneBinding](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.ManagementDnsZoneBinding),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.OperationMetadata)>` |   
  
### repairManagementDnsZoneBindingAsync(String name)
    
    
    public final OperationFuture<ManagementDnsZoneBinding,OperationMetadata> repairManagementDnsZoneBindingAsync(String name)

Retries to create a `ManagementDnsZoneBinding` resource that is in failed state.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       String name =
           ManagementDnsZoneBindingName.of(
                   "[PROJECT]", "[LOCATION]", "[PRIVATE_CLOUD]", "[MANAGEMENT_DNS_ZONE_BINDING]")
               .toString();
       ManagementDnsZoneBinding response =
           vmwareEngineClient.repairManagementDnsZoneBindingAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the management DNS zone binding to repair. Resource names are schemeless URIs that follow the conventions in <https://cloud.google.com/apis/design/resource_names>. For example: `projects/my-project/locations/us-central1-a/privateClouds/my-cloud/managementDnsZoneBindings/my-management-dns-zone-binding`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[ManagementDnsZoneBinding](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.ManagementDnsZoneBinding),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.OperationMetadata)>` |   
  
### repairManagementDnsZoneBindingCallable()
    
    
    public final UnaryCallable<RepairManagementDnsZoneBindingRequest,Operation> repairManagementDnsZoneBindingCallable()

Retries to create a `ManagementDnsZoneBinding` resource that is in failed state.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       RepairManagementDnsZoneBindingRequest request =
           RepairManagementDnsZoneBindingRequest.newBuilder()
               .setName(
                   ManagementDnsZoneBindingName.of(
                           "[PROJECT]",
                           "[LOCATION]",
                           "[PRIVATE_CLOUD]",
                           "[MANAGEMENT_DNS_ZONE_BINDING]")
                       .toString())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           vmwareEngineClient.repairManagementDnsZoneBindingCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[RepairManagementDnsZoneBindingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.RepairManagementDnsZoneBindingRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### repairManagementDnsZoneBindingOperationCallable()
    
    
    public final OperationCallable<RepairManagementDnsZoneBindingRequest,ManagementDnsZoneBinding,OperationMetadata> repairManagementDnsZoneBindingOperationCallable()

Retries to create a `ManagementDnsZoneBinding` resource that is in failed state.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       RepairManagementDnsZoneBindingRequest request =
           RepairManagementDnsZoneBindingRequest.newBuilder()
               .setName(
                   ManagementDnsZoneBindingName.of(
                           "[PROJECT]",
                           "[LOCATION]",
                           "[PRIVATE_CLOUD]",
                           "[MANAGEMENT_DNS_ZONE_BINDING]")
                       .toString())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<ManagementDnsZoneBinding, OperationMetadata> future =
           vmwareEngineClient.repairManagementDnsZoneBindingOperationCallable().futureCall(request);
       // Do something.
       ManagementDnsZoneBinding response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[RepairManagementDnsZoneBindingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.RepairManagementDnsZoneBindingRequest),[ManagementDnsZoneBinding](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.ManagementDnsZoneBinding),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.OperationMetadata)>` |   
  
### resetNsxCredentialsAsync(@Nullable PrivateCloudName privateCloud)
    
    
    public final OperationFuture<PrivateCloud,OperationMetadata> resetNsxCredentialsAsync(@Nullable PrivateCloudName privateCloud)

Resets credentials of the NSX appliance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       PrivateCloudName privateCloud =
           PrivateCloudName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_CLOUD]");
       PrivateCloud response = vmwareEngineClient.resetNsxCredentialsAsync(privateCloud).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`privateCloud` | `@org.jspecify.annotations.Nullable com.google.cloud.vmwareengine.v1.PrivateCloudName`  
Required. The resource name of the private cloud to reset credentials for. Resource names are schemeless URIs that follow the conventions in <https://cloud.google.com/apis/design/resource_names>. For example: `projects/my-project/locations/us-central1-a/privateClouds/my-cloud`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[PrivateCloud](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.PrivateCloud),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.OperationMetadata)>` |   
  
### resetNsxCredentialsAsync(ResetNsxCredentialsRequest request)
    
    
    public final OperationFuture<PrivateCloud,OperationMetadata> resetNsxCredentialsAsync(ResetNsxCredentialsRequest request)

Resets credentials of the NSX appliance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       ResetNsxCredentialsRequest request =
           ResetNsxCredentialsRequest.newBuilder()
               .setPrivateCloud(
                   PrivateCloudName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_CLOUD]").toString())
               .setRequestId("requestId693933066")
               .build();
       PrivateCloud response = vmwareEngineClient.resetNsxCredentialsAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ResetNsxCredentialsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.ResetNsxCredentialsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[PrivateCloud](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.PrivateCloud),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.OperationMetadata)>` |   
  
### resetNsxCredentialsAsync(String privateCloud)
    
    
    public final OperationFuture<PrivateCloud,OperationMetadata> resetNsxCredentialsAsync(String privateCloud)

Resets credentials of the NSX appliance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       String privateCloud =
           PrivateCloudName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_CLOUD]").toString();
       PrivateCloud response = vmwareEngineClient.resetNsxCredentialsAsync(privateCloud).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`privateCloud` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the private cloud to reset credentials for. Resource names are schemeless URIs that follow the conventions in <https://cloud.google.com/apis/design/resource_names>. For example: `projects/my-project/locations/us-central1-a/privateClouds/my-cloud`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[PrivateCloud](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.PrivateCloud),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.OperationMetadata)>` |   
  
### resetNsxCredentialsCallable()
    
    
    public final UnaryCallable<ResetNsxCredentialsRequest,Operation> resetNsxCredentialsCallable()

Resets credentials of the NSX appliance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       ResetNsxCredentialsRequest request =
           ResetNsxCredentialsRequest.newBuilder()
               .setPrivateCloud(
                   PrivateCloudName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_CLOUD]").toString())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           vmwareEngineClient.resetNsxCredentialsCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ResetNsxCredentialsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.ResetNsxCredentialsRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### resetNsxCredentialsOperationCallable()
    
    
    public final OperationCallable<ResetNsxCredentialsRequest,PrivateCloud,OperationMetadata> resetNsxCredentialsOperationCallable()

Resets credentials of the NSX appliance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       ResetNsxCredentialsRequest request =
           ResetNsxCredentialsRequest.newBuilder()
               .setPrivateCloud(
                   PrivateCloudName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_CLOUD]").toString())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<PrivateCloud, OperationMetadata> future =
           vmwareEngineClient.resetNsxCredentialsOperationCallable().futureCall(request);
       // Do something.
       PrivateCloud response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[ResetNsxCredentialsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.ResetNsxCredentialsRequest),[PrivateCloud](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.PrivateCloud),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.OperationMetadata)>` |   
  
### resetVcenterCredentialsAsync(@Nullable PrivateCloudName privateCloud)
    
    
    public final OperationFuture<PrivateCloud,OperationMetadata> resetVcenterCredentialsAsync(@Nullable PrivateCloudName privateCloud)

Resets credentials of the Vcenter appliance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       PrivateCloudName privateCloud =
           PrivateCloudName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_CLOUD]");
       PrivateCloud response = vmwareEngineClient.resetVcenterCredentialsAsync(privateCloud).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`privateCloud` | `@org.jspecify.annotations.Nullable com.google.cloud.vmwareengine.v1.PrivateCloudName`  
Required. The resource name of the private cloud to reset credentials for. Resource names are schemeless URIs that follow the conventions in <https://cloud.google.com/apis/design/resource_names>. For example: `projects/my-project/locations/us-central1-a/privateClouds/my-cloud`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[PrivateCloud](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.PrivateCloud),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.OperationMetadata)>` |   
  
### resetVcenterCredentialsAsync(ResetVcenterCredentialsRequest request)
    
    
    public final OperationFuture<PrivateCloud,OperationMetadata> resetVcenterCredentialsAsync(ResetVcenterCredentialsRequest request)

Resets credentials of the Vcenter appliance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       ResetVcenterCredentialsRequest request =
           ResetVcenterCredentialsRequest.newBuilder()
               .setPrivateCloud(
                   PrivateCloudName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_CLOUD]").toString())
               .setRequestId("requestId693933066")
               .setUsername("username-265713450")
               .build();
       PrivateCloud response = vmwareEngineClient.resetVcenterCredentialsAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ResetVcenterCredentialsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.ResetVcenterCredentialsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[PrivateCloud](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.PrivateCloud),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.OperationMetadata)>` |   
  
### resetVcenterCredentialsAsync(String privateCloud)
    
    
    public final OperationFuture<PrivateCloud,OperationMetadata> resetVcenterCredentialsAsync(String privateCloud)

Resets credentials of the Vcenter appliance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       String privateCloud =
           PrivateCloudName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_CLOUD]").toString();
       PrivateCloud response = vmwareEngineClient.resetVcenterCredentialsAsync(privateCloud).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`privateCloud` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the private cloud to reset credentials for. Resource names are schemeless URIs that follow the conventions in <https://cloud.google.com/apis/design/resource_names>. For example: `projects/my-project/locations/us-central1-a/privateClouds/my-cloud`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[PrivateCloud](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.PrivateCloud),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.OperationMetadata)>` |   
  
### resetVcenterCredentialsCallable()
    
    
    public final UnaryCallable<ResetVcenterCredentialsRequest,Operation> resetVcenterCredentialsCallable()

Resets credentials of the Vcenter appliance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       ResetVcenterCredentialsRequest request =
           ResetVcenterCredentialsRequest.newBuilder()
               .setPrivateCloud(
                   PrivateCloudName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_CLOUD]").toString())
               .setRequestId("requestId693933066")
               .setUsername("username-265713450")
               .build();
       ApiFuture<Operation> future =
           vmwareEngineClient.resetVcenterCredentialsCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ResetVcenterCredentialsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.ResetVcenterCredentialsRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### resetVcenterCredentialsOperationCallable()
    
    
    public final OperationCallable<ResetVcenterCredentialsRequest,PrivateCloud,OperationMetadata> resetVcenterCredentialsOperationCallable()

Resets credentials of the Vcenter appliance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       ResetVcenterCredentialsRequest request =
           ResetVcenterCredentialsRequest.newBuilder()
               .setPrivateCloud(
                   PrivateCloudName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_CLOUD]").toString())
               .setRequestId("requestId693933066")
               .setUsername("username-265713450")
               .build();
       OperationFuture<PrivateCloud, OperationMetadata> future =
           vmwareEngineClient.resetVcenterCredentialsOperationCallable().futureCall(request);
       // Do something.
       PrivateCloud response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[ResetVcenterCredentialsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.ResetVcenterCredentialsRequest),[PrivateCloud](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.PrivateCloud),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.OperationMetadata)>` |   
  
### revokeDnsBindPermissionAsync(@Nullable DnsBindPermissionName name, Principal principal)
    
    
    public final OperationFuture<DnsBindPermission,OperationMetadata> revokeDnsBindPermissionAsync(@Nullable DnsBindPermissionName name, Principal principal)

Revokes the bind permission from the customer provided principal(user / service account) on the intranet VPC associated with the consumer project. DnsBindPermission is a global resource and location can only be global.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       DnsBindPermissionName name = DnsBindPermissionName.of("[PROJECT]", "[LOCATION]");
       Principal principal = Principal.newBuilder().build();
       DnsBindPermission response =
           vmwareEngineClient.revokeDnsBindPermissionAsync(name, principal).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.vmwareengine.v1.DnsBindPermissionName`  
Required. The name of the resource which stores the users/service accounts having the permission to bind to the corresponding intranet VPC of the consumer project. DnsBindPermission is a global resource. Resource names are schemeless URIs that follow the conventions in <https://cloud.google.com/apis/design/resource_names>. For example: `projects/my-project/locations/global/dnsBindPermission`  
`principal` | `[Principal](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.Principal)`  
Required. The consumer provided user/service account which needs to be granted permission to bind with the intranet VPC corresponding to the consumer project.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[DnsBindPermission](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.DnsBindPermission),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.OperationMetadata)>` |   
  
### revokeDnsBindPermissionAsync(RevokeDnsBindPermissionRequest request)
    
    
    public final OperationFuture<DnsBindPermission,OperationMetadata> revokeDnsBindPermissionAsync(RevokeDnsBindPermissionRequest request)

Revokes the bind permission from the customer provided principal(user / service account) on the intranet VPC associated with the consumer project. DnsBindPermission is a global resource and location can only be global.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       RevokeDnsBindPermissionRequest request =
           RevokeDnsBindPermissionRequest.newBuilder()
               .setName(DnsBindPermissionName.of("[PROJECT]", "[LOCATION]").toString())
               .setPrincipal(Principal.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       DnsBindPermission response = vmwareEngineClient.revokeDnsBindPermissionAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[RevokeDnsBindPermissionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.RevokeDnsBindPermissionRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[DnsBindPermission](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.DnsBindPermission),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.OperationMetadata)>` |   
  
### revokeDnsBindPermissionAsync(String name, Principal principal)
    
    
    public final OperationFuture<DnsBindPermission,OperationMetadata> revokeDnsBindPermissionAsync(String name, Principal principal)

Revokes the bind permission from the customer provided principal(user / service account) on the intranet VPC associated with the consumer project. DnsBindPermission is a global resource and location can only be global.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       String name = DnsBindPermissionName.of("[PROJECT]", "[LOCATION]").toString();
       Principal principal = Principal.newBuilder().build();
       DnsBindPermission response =
           vmwareEngineClient.revokeDnsBindPermissionAsync(name, principal).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the resource which stores the users/service accounts having the permission to bind to the corresponding intranet VPC of the consumer project. DnsBindPermission is a global resource. Resource names are schemeless URIs that follow the conventions in <https://cloud.google.com/apis/design/resource_names>. For example: `projects/my-project/locations/global/dnsBindPermission`  
`principal` | `[Principal](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.Principal)`  
Required. The consumer provided user/service account which needs to be granted permission to bind with the intranet VPC corresponding to the consumer project.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[DnsBindPermission](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.DnsBindPermission),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.OperationMetadata)>` |   
  
### revokeDnsBindPermissionCallable()
    
    
    public final UnaryCallable<RevokeDnsBindPermissionRequest,Operation> revokeDnsBindPermissionCallable()

Revokes the bind permission from the customer provided principal(user / service account) on the intranet VPC associated with the consumer project. DnsBindPermission is a global resource and location can only be global.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       RevokeDnsBindPermissionRequest request =
           RevokeDnsBindPermissionRequest.newBuilder()
               .setName(DnsBindPermissionName.of("[PROJECT]", "[LOCATION]").toString())
               .setPrincipal(Principal.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           vmwareEngineClient.revokeDnsBindPermissionCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[RevokeDnsBindPermissionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.RevokeDnsBindPermissionRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### revokeDnsBindPermissionOperationCallable()
    
    
    public final OperationCallable<RevokeDnsBindPermissionRequest,DnsBindPermission,OperationMetadata> revokeDnsBindPermissionOperationCallable()

Revokes the bind permission from the customer provided principal(user / service account) on the intranet VPC associated with the consumer project. DnsBindPermission is a global resource and location can only be global.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       RevokeDnsBindPermissionRequest request =
           RevokeDnsBindPermissionRequest.newBuilder()
               .setName(DnsBindPermissionName.of("[PROJECT]", "[LOCATION]").toString())
               .setPrincipal(Principal.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<DnsBindPermission, OperationMetadata> future =
           vmwareEngineClient.revokeDnsBindPermissionOperationCallable().futureCall(request);
       // Do something.
       DnsBindPermission response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[RevokeDnsBindPermissionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.RevokeDnsBindPermissionRequest),[DnsBindPermission](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.DnsBindPermission),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.OperationMetadata)>` |   
  
### setIamPolicy(SetIamPolicyRequest request)
    
    
    public final Policy setIamPolicy(SetIamPolicyRequest request)

Sets the access control policy on the specified resource. Replacesany existing policy.

Can return `NOT_FOUND`, `INVALID_ARGUMENT`, and `PERMISSION_DENIED`errors.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       SetIamPolicyRequest request =
           SetIamPolicyRequest.newBuilder()
               .setResource(
                   ClusterName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_CLOUD]", "[CLUSTER]")
                       .toString())
               .setPolicy(Policy.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       Policy response = vmwareEngineClient.setIamPolicy(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `com.google.iam.v1.SetIamPolicyRequest`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`com.google.iam.v1.Policy` |   
  
### setIamPolicyCallable()
    
    
    public final UnaryCallable<SetIamPolicyRequest,Policy> setIamPolicyCallable()

Sets the access control policy on the specified resource. Replacesany existing policy.

Can return `NOT_FOUND`, `INVALID_ARGUMENT`, and `PERMISSION_DENIED`errors.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       SetIamPolicyRequest request =
           SetIamPolicyRequest.newBuilder()
               .setResource(
                   ClusterName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_CLOUD]", "[CLUSTER]")
                       .toString())
               .setPolicy(Policy.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<Policy> future = vmwareEngineClient.setIamPolicyCallable().futureCall(request);
       // Do something.
       Policy response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.iam.v1.SetIamPolicyRequest,com.google.iam.v1.Policy>` |   
  
### showNsxCredentials(@Nullable PrivateCloudName privateCloud)
    
    
    public final Credentials showNsxCredentials(@Nullable PrivateCloudName privateCloud)

Gets details of credentials for NSX appliance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       PrivateCloudName privateCloud =
           PrivateCloudName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_CLOUD]");
       Credentials response = vmwareEngineClient.showNsxCredentials(privateCloud);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`privateCloud` | `@org.jspecify.annotations.Nullable com.google.cloud.vmwareengine.v1.PrivateCloudName`  
Required. The resource name of the private cloud to be queried for credentials. Resource names are schemeless URIs that follow the conventions in <https://cloud.google.com/apis/design/resource_names>. For example: `projects/my-project/locations/us-central1-a/privateClouds/my-cloud`  
**Returns**  
---  
**Type** | **Description**  
`[Credentials](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.Credentials)` |   
  
### showNsxCredentials(ShowNsxCredentialsRequest request)
    
    
    public final Credentials showNsxCredentials(ShowNsxCredentialsRequest request)

Gets details of credentials for NSX appliance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       ShowNsxCredentialsRequest request =
           ShowNsxCredentialsRequest.newBuilder()
               .setPrivateCloud(
                   PrivateCloudName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_CLOUD]").toString())
               .build();
       Credentials response = vmwareEngineClient.showNsxCredentials(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ShowNsxCredentialsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.ShowNsxCredentialsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Credentials](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.Credentials)` |   
  
### showNsxCredentials(String privateCloud)
    
    
    public final Credentials showNsxCredentials(String privateCloud)

Gets details of credentials for NSX appliance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       String privateCloud =
           PrivateCloudName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_CLOUD]").toString();
       Credentials response = vmwareEngineClient.showNsxCredentials(privateCloud);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`privateCloud` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the private cloud to be queried for credentials. Resource names are schemeless URIs that follow the conventions in <https://cloud.google.com/apis/design/resource_names>. For example: `projects/my-project/locations/us-central1-a/privateClouds/my-cloud`  
**Returns**  
---  
**Type** | **Description**  
`[Credentials](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.Credentials)` |   
  
### showNsxCredentialsCallable()
    
    
    public final UnaryCallable<ShowNsxCredentialsRequest,Credentials> showNsxCredentialsCallable()

Gets details of credentials for NSX appliance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       ShowNsxCredentialsRequest request =
           ShowNsxCredentialsRequest.newBuilder()
               .setPrivateCloud(
                   PrivateCloudName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_CLOUD]").toString())
               .build();
       ApiFuture<Credentials> future =
           vmwareEngineClient.showNsxCredentialsCallable().futureCall(request);
       // Do something.
       Credentials response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ShowNsxCredentialsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.ShowNsxCredentialsRequest),[Credentials](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.Credentials)>` |   
  
### showVcenterCredentials(@Nullable PrivateCloudName privateCloud)
    
    
    public final Credentials showVcenterCredentials(@Nullable PrivateCloudName privateCloud)

Gets details of credentials for Vcenter appliance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       PrivateCloudName privateCloud =
           PrivateCloudName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_CLOUD]");
       Credentials response = vmwareEngineClient.showVcenterCredentials(privateCloud);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`privateCloud` | `@org.jspecify.annotations.Nullable com.google.cloud.vmwareengine.v1.PrivateCloudName`  
Required. The resource name of the private cloud to be queried for credentials. Resource names are schemeless URIs that follow the conventions in <https://cloud.google.com/apis/design/resource_names>. For example: `projects/my-project/locations/us-central1-a/privateClouds/my-cloud`  
**Returns**  
---  
**Type** | **Description**  
`[Credentials](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.Credentials)` |   
  
### showVcenterCredentials(ShowVcenterCredentialsRequest request)
    
    
    public final Credentials showVcenterCredentials(ShowVcenterCredentialsRequest request)

Gets details of credentials for Vcenter appliance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       ShowVcenterCredentialsRequest request =
           ShowVcenterCredentialsRequest.newBuilder()
               .setPrivateCloud(
                   PrivateCloudName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_CLOUD]").toString())
               .setUsername("username-265713450")
               .build();
       Credentials response = vmwareEngineClient.showVcenterCredentials(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ShowVcenterCredentialsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.ShowVcenterCredentialsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Credentials](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.Credentials)` |   
  
### showVcenterCredentials(String privateCloud)
    
    
    public final Credentials showVcenterCredentials(String privateCloud)

Gets details of credentials for Vcenter appliance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       String privateCloud =
           PrivateCloudName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_CLOUD]").toString();
       Credentials response = vmwareEngineClient.showVcenterCredentials(privateCloud);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`privateCloud` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the private cloud to be queried for credentials. Resource names are schemeless URIs that follow the conventions in <https://cloud.google.com/apis/design/resource_names>. For example: `projects/my-project/locations/us-central1-a/privateClouds/my-cloud`  
**Returns**  
---  
**Type** | **Description**  
`[Credentials](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.Credentials)` |   
  
### showVcenterCredentialsCallable()
    
    
    public final UnaryCallable<ShowVcenterCredentialsRequest,Credentials> showVcenterCredentialsCallable()

Gets details of credentials for Vcenter appliance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       ShowVcenterCredentialsRequest request =
           ShowVcenterCredentialsRequest.newBuilder()
               .setPrivateCloud(
                   PrivateCloudName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_CLOUD]").toString())
               .setUsername("username-265713450")
               .build();
       ApiFuture<Credentials> future =
           vmwareEngineClient.showVcenterCredentialsCallable().futureCall(request);
       // Do something.
       Credentials response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ShowVcenterCredentialsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.ShowVcenterCredentialsRequest),[Credentials](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.Credentials)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### testIamPermissions(TestIamPermissionsRequest request)
    
    
    public final TestIamPermissionsResponse testIamPermissions(TestIamPermissionsRequest request)

Returns permissions that a caller has on the specified resource. If theresource does not exist, this will return an empty set ofpermissions, not a `NOT_FOUND` error.

Note: This operation is designed to be used for buildingpermission-aware UIs and command-line tools, not for authorizationchecking. This operation may "fail open" without warning.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       TestIamPermissionsRequest request =
           TestIamPermissionsRequest.newBuilder()
               .setResource(
                   ClusterName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_CLOUD]", "[CLUSTER]")
                       .toString())
               .addAllPermissions(new ArrayList<String>())
               .build();
       TestIamPermissionsResponse response = vmwareEngineClient.testIamPermissions(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `com.google.iam.v1.TestIamPermissionsRequest`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`com.google.iam.v1.TestIamPermissionsResponse` |   
  
### testIamPermissionsCallable()
    
    
    public final UnaryCallable<TestIamPermissionsRequest,TestIamPermissionsResponse> testIamPermissionsCallable()

Returns permissions that a caller has on the specified resource. If theresource does not exist, this will return an empty set ofpermissions, not a `NOT_FOUND` error.

Note: This operation is designed to be used for buildingpermission-aware UIs and command-line tools, not for authorizationchecking. This operation may "fail open" without warning.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       TestIamPermissionsRequest request =
           TestIamPermissionsRequest.newBuilder()
               .setResource(
                   ClusterName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_CLOUD]", "[CLUSTER]")
                       .toString())
               .addAllPermissions(new ArrayList<String>())
               .build();
       ApiFuture<TestIamPermissionsResponse> future =
           vmwareEngineClient.testIamPermissionsCallable().futureCall(request);
       // Do something.
       TestIamPermissionsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.iam.v1.TestIamPermissionsRequest,com.google.iam.v1.TestIamPermissionsResponse>` |   
  
### undeletePrivateCloudAsync(@Nullable PrivateCloudName name)
    
    
    public final OperationFuture<PrivateCloud,OperationMetadata> undeletePrivateCloudAsync(@Nullable PrivateCloudName name)

Restores a private cloud that was previously scheduled for deletion by `DeletePrivateCloud`. A `PrivateCloud` resource scheduled for deletion has `PrivateCloud.state` set to `DELETED` and `PrivateCloud.expireTime` set to the time when deletion can no longer be reversed.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       PrivateCloudName name = PrivateCloudName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_CLOUD]");
       PrivateCloud response = vmwareEngineClient.undeletePrivateCloudAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.vmwareengine.v1.PrivateCloudName`  
Required. The resource name of the private cloud scheduled for deletion. Resource names are schemeless URIs that follow the conventions in <https://cloud.google.com/apis/design/resource_names>. For example: `projects/my-project/locations/us-central1-a/privateClouds/my-cloud`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[PrivateCloud](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.PrivateCloud),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.OperationMetadata)>` |   
  
### undeletePrivateCloudAsync(UndeletePrivateCloudRequest request)
    
    
    public final OperationFuture<PrivateCloud,OperationMetadata> undeletePrivateCloudAsync(UndeletePrivateCloudRequest request)

Restores a private cloud that was previously scheduled for deletion by `DeletePrivateCloud`. A `PrivateCloud` resource scheduled for deletion has `PrivateCloud.state` set to `DELETED` and `PrivateCloud.expireTime` set to the time when deletion can no longer be reversed.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       UndeletePrivateCloudRequest request =
           UndeletePrivateCloudRequest.newBuilder()
               .setName(PrivateCloudName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_CLOUD]").toString())
               .setRequestId("requestId693933066")
               .build();
       PrivateCloud response = vmwareEngineClient.undeletePrivateCloudAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UndeletePrivateCloudRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.UndeletePrivateCloudRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[PrivateCloud](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.PrivateCloud),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.OperationMetadata)>` |   
  
### undeletePrivateCloudAsync(String name)
    
    
    public final OperationFuture<PrivateCloud,OperationMetadata> undeletePrivateCloudAsync(String name)

Restores a private cloud that was previously scheduled for deletion by `DeletePrivateCloud`. A `PrivateCloud` resource scheduled for deletion has `PrivateCloud.state` set to `DELETED` and `PrivateCloud.expireTime` set to the time when deletion can no longer be reversed.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       String name = PrivateCloudName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_CLOUD]").toString();
       PrivateCloud response = vmwareEngineClient.undeletePrivateCloudAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the private cloud scheduled for deletion. Resource names are schemeless URIs that follow the conventions in <https://cloud.google.com/apis/design/resource_names>. For example: `projects/my-project/locations/us-central1-a/privateClouds/my-cloud`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[PrivateCloud](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.PrivateCloud),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.OperationMetadata)>` |   
  
### undeletePrivateCloudCallable()
    
    
    public final UnaryCallable<UndeletePrivateCloudRequest,Operation> undeletePrivateCloudCallable()

Restores a private cloud that was previously scheduled for deletion by `DeletePrivateCloud`. A `PrivateCloud` resource scheduled for deletion has `PrivateCloud.state` set to `DELETED` and `PrivateCloud.expireTime` set to the time when deletion can no longer be reversed.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       UndeletePrivateCloudRequest request =
           UndeletePrivateCloudRequest.newBuilder()
               .setName(PrivateCloudName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_CLOUD]").toString())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           vmwareEngineClient.undeletePrivateCloudCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UndeletePrivateCloudRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.UndeletePrivateCloudRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### undeletePrivateCloudOperationCallable()
    
    
    public final OperationCallable<UndeletePrivateCloudRequest,PrivateCloud,OperationMetadata> undeletePrivateCloudOperationCallable()

Restores a private cloud that was previously scheduled for deletion by `DeletePrivateCloud`. A `PrivateCloud` resource scheduled for deletion has `PrivateCloud.state` set to `DELETED` and `PrivateCloud.expireTime` set to the time when deletion can no longer be reversed.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       UndeletePrivateCloudRequest request =
           UndeletePrivateCloudRequest.newBuilder()
               .setName(PrivateCloudName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_CLOUD]").toString())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<PrivateCloud, OperationMetadata> future =
           vmwareEngineClient.undeletePrivateCloudOperationCallable().futureCall(request);
       // Do something.
       PrivateCloud response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UndeletePrivateCloudRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.UndeletePrivateCloudRequest),[PrivateCloud](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.PrivateCloud),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.OperationMetadata)>` |   
  
### updateClusterAsync(Cluster cluster, FieldMask updateMask)
    
    
    public final OperationFuture<Cluster,OperationMetadata> updateClusterAsync(Cluster cluster, FieldMask updateMask)

Modifies a `Cluster` resource. Only fields specified in `updateMask` are applied.

During operation processing, the resource is temporarily in the `ACTIVE` state before the operation fully completes. For that period of time, you can't update the resource. Use the operation status to determine when the processing fully completes.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       Cluster cluster = Cluster.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       Cluster response = vmwareEngineClient.updateClusterAsync(cluster, updateMask).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`cluster` | `[Cluster](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.Cluster)`  
Required. The description of the cluster.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Required. Field mask is used to specify the fields to be overwritten in the `Cluster` resource by the update. The fields specified in the `updateMask` are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields will be overwritten.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Cluster](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.Cluster),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.OperationMetadata)>` |   
  
### updateClusterAsync(UpdateClusterRequest request)
    
    
    public final OperationFuture<Cluster,OperationMetadata> updateClusterAsync(UpdateClusterRequest request)

Modifies a `Cluster` resource. Only fields specified in `updateMask` are applied.

During operation processing, the resource is temporarily in the `ACTIVE` state before the operation fully completes. For that period of time, you can't update the resource. Use the operation status to determine when the processing fully completes.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       UpdateClusterRequest request =
           UpdateClusterRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setCluster(Cluster.newBuilder().build())
               .setRequestId("requestId693933066")
               .setValidateOnly(true)
               .build();
       Cluster response = vmwareEngineClient.updateClusterAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.UpdateClusterRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Cluster](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.Cluster),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.OperationMetadata)>` |   
  
### updateClusterCallable()
    
    
    public final UnaryCallable<UpdateClusterRequest,Operation> updateClusterCallable()

Modifies a `Cluster` resource. Only fields specified in `updateMask` are applied.

During operation processing, the resource is temporarily in the `ACTIVE` state before the operation fully completes. For that period of time, you can't update the resource. Use the operation status to determine when the processing fully completes.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       UpdateClusterRequest request =
           UpdateClusterRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setCluster(Cluster.newBuilder().build())
               .setRequestId("requestId693933066")
               .setValidateOnly(true)
               .build();
       ApiFuture<Operation> future = vmwareEngineClient.updateClusterCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.UpdateClusterRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateClusterOperationCallable()
    
    
    public final OperationCallable<UpdateClusterRequest,Cluster,OperationMetadata> updateClusterOperationCallable()

Modifies a `Cluster` resource. Only fields specified in `updateMask` are applied.

During operation processing, the resource is temporarily in the `ACTIVE` state before the operation fully completes. For that period of time, you can't update the resource. Use the operation status to determine when the processing fully completes.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       UpdateClusterRequest request =
           UpdateClusterRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setCluster(Cluster.newBuilder().build())
               .setRequestId("requestId693933066")
               .setValidateOnly(true)
               .build();
       OperationFuture<Cluster, OperationMetadata> future =
           vmwareEngineClient.updateClusterOperationCallable().futureCall(request);
       // Do something.
       Cluster response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdateClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.UpdateClusterRequest),[Cluster](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.Cluster),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.OperationMetadata)>` |   
  
### updateDnsForwardingAsync(DnsForwarding dnsForwarding, FieldMask updateMask)
    
    
    public final OperationFuture<DnsForwarding,OperationMetadata> updateDnsForwardingAsync(DnsForwarding dnsForwarding, FieldMask updateMask)

Updates the parameters of the `DnsForwarding` config, like associated domains. Only fields specified in `update_mask` are applied.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       DnsForwarding dnsForwarding = DnsForwarding.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       DnsForwarding response =
           vmwareEngineClient.updateDnsForwardingAsync(dnsForwarding, updateMask).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`dnsForwarding` | `[DnsForwarding](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.DnsForwarding)`  
Required. DnsForwarding config details.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Required. Field mask is used to specify the fields to be overwritten in the `DnsForwarding` resource by the update. The fields specified in the `update_mask` are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields will be overwritten.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[DnsForwarding](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.DnsForwarding),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.OperationMetadata)>` |   
  
### updateDnsForwardingAsync(UpdateDnsForwardingRequest request)
    
    
    public final OperationFuture<DnsForwarding,OperationMetadata> updateDnsForwardingAsync(UpdateDnsForwardingRequest request)

Updates the parameters of the `DnsForwarding` config, like associated domains. Only fields specified in `update_mask` are applied.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       UpdateDnsForwardingRequest request =
           UpdateDnsForwardingRequest.newBuilder()
               .setDnsForwarding(DnsForwarding.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       DnsForwarding response = vmwareEngineClient.updateDnsForwardingAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateDnsForwardingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.UpdateDnsForwardingRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[DnsForwarding](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.DnsForwarding),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.OperationMetadata)>` |   
  
### updateDnsForwardingCallable()
    
    
    public final UnaryCallable<UpdateDnsForwardingRequest,Operation> updateDnsForwardingCallable()

Updates the parameters of the `DnsForwarding` config, like associated domains. Only fields specified in `update_mask` are applied.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       UpdateDnsForwardingRequest request =
           UpdateDnsForwardingRequest.newBuilder()
               .setDnsForwarding(DnsForwarding.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           vmwareEngineClient.updateDnsForwardingCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateDnsForwardingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.UpdateDnsForwardingRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateDnsForwardingOperationCallable()
    
    
    public final OperationCallable<UpdateDnsForwardingRequest,DnsForwarding,OperationMetadata> updateDnsForwardingOperationCallable()

Updates the parameters of the `DnsForwarding` config, like associated domains. Only fields specified in `update_mask` are applied.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       UpdateDnsForwardingRequest request =
           UpdateDnsForwardingRequest.newBuilder()
               .setDnsForwarding(DnsForwarding.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<DnsForwarding, OperationMetadata> future =
           vmwareEngineClient.updateDnsForwardingOperationCallable().futureCall(request);
       // Do something.
       DnsForwarding response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdateDnsForwardingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.UpdateDnsForwardingRequest),[DnsForwarding](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.DnsForwarding),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.OperationMetadata)>` |   
  
### updateExternalAccessRuleAsync(ExternalAccessRule externalAccessRule, FieldMask updateMask)
    
    
    public final OperationFuture<ExternalAccessRule,OperationMetadata> updateExternalAccessRuleAsync(ExternalAccessRule externalAccessRule, FieldMask updateMask)

Updates the parameters of a single external access rule. Only fields specified in `update_mask` are applied.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       ExternalAccessRule externalAccessRule = ExternalAccessRule.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       ExternalAccessRule response =
           vmwareEngineClient.updateExternalAccessRuleAsync(externalAccessRule, updateMask).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`externalAccessRule` | `[ExternalAccessRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.ExternalAccessRule)`  
Required. Description of the external access rule.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Required. Field mask is used to specify the fields to be overwritten in the `ExternalAccessRule` resource by the update. The fields specified in the `update_mask` are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields will be overwritten.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[ExternalAccessRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.ExternalAccessRule),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.OperationMetadata)>` |   
  
### updateExternalAccessRuleAsync(UpdateExternalAccessRuleRequest request)
    
    
    public final OperationFuture<ExternalAccessRule,OperationMetadata> updateExternalAccessRuleAsync(UpdateExternalAccessRuleRequest request)

Updates the parameters of a single external access rule. Only fields specified in `update_mask` are applied.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       UpdateExternalAccessRuleRequest request =
           UpdateExternalAccessRuleRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setExternalAccessRule(ExternalAccessRule.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       ExternalAccessRule response = vmwareEngineClient.updateExternalAccessRuleAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateExternalAccessRuleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.UpdateExternalAccessRuleRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[ExternalAccessRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.ExternalAccessRule),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.OperationMetadata)>` |   
  
### updateExternalAccessRuleCallable()
    
    
    public final UnaryCallable<UpdateExternalAccessRuleRequest,Operation> updateExternalAccessRuleCallable()

Updates the parameters of a single external access rule. Only fields specified in `update_mask` are applied.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       UpdateExternalAccessRuleRequest request =
           UpdateExternalAccessRuleRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setExternalAccessRule(ExternalAccessRule.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           vmwareEngineClient.updateExternalAccessRuleCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateExternalAccessRuleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.UpdateExternalAccessRuleRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateExternalAccessRuleOperationCallable()
    
    
    public final OperationCallable<UpdateExternalAccessRuleRequest,ExternalAccessRule,OperationMetadata> updateExternalAccessRuleOperationCallable()

Updates the parameters of a single external access rule. Only fields specified in `update_mask` are applied.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       UpdateExternalAccessRuleRequest request =
           UpdateExternalAccessRuleRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setExternalAccessRule(ExternalAccessRule.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<ExternalAccessRule, OperationMetadata> future =
           vmwareEngineClient.updateExternalAccessRuleOperationCallable().futureCall(request);
       // Do something.
       ExternalAccessRule response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdateExternalAccessRuleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.UpdateExternalAccessRuleRequest),[ExternalAccessRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.ExternalAccessRule),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.OperationMetadata)>` |   
  
### updateExternalAddressAsync(ExternalAddress externalAddress, FieldMask updateMask)
    
    
    public final OperationFuture<ExternalAddress,OperationMetadata> updateExternalAddressAsync(ExternalAddress externalAddress, FieldMask updateMask)

Updates the parameters of a single external IP address. Only fields specified in `update_mask` are applied.

During operation processing, the resource is temporarily in the `ACTIVE` state before the operation fully completes. For that period of time, you can't update the resource. Use the operation status to determine when the processing fully completes.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       ExternalAddress externalAddress = ExternalAddress.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       ExternalAddress response =
           vmwareEngineClient.updateExternalAddressAsync(externalAddress, updateMask).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`externalAddress` | `[ExternalAddress](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.ExternalAddress)`  
Required. External IP address description.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Required. Field mask is used to specify the fields to be overwritten in the `ExternalAddress` resource by the update. The fields specified in the `update_mask` are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields will be overwritten.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[ExternalAddress](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.ExternalAddress),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.OperationMetadata)>` |   
  
### updateExternalAddressAsync(UpdateExternalAddressRequest request)
    
    
    public final OperationFuture<ExternalAddress,OperationMetadata> updateExternalAddressAsync(UpdateExternalAddressRequest request)

Updates the parameters of a single external IP address. Only fields specified in `update_mask` are applied.

During operation processing, the resource is temporarily in the `ACTIVE` state before the operation fully completes. For that period of time, you can't update the resource. Use the operation status to determine when the processing fully completes.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       UpdateExternalAddressRequest request =
           UpdateExternalAddressRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setExternalAddress(ExternalAddress.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       ExternalAddress response = vmwareEngineClient.updateExternalAddressAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateExternalAddressRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.UpdateExternalAddressRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[ExternalAddress](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.ExternalAddress),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.OperationMetadata)>` |   
  
### updateExternalAddressCallable()
    
    
    public final UnaryCallable<UpdateExternalAddressRequest,Operation> updateExternalAddressCallable()

Updates the parameters of a single external IP address. Only fields specified in `update_mask` are applied.

During operation processing, the resource is temporarily in the `ACTIVE` state before the operation fully completes. For that period of time, you can't update the resource. Use the operation status to determine when the processing fully completes.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       UpdateExternalAddressRequest request =
           UpdateExternalAddressRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setExternalAddress(ExternalAddress.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           vmwareEngineClient.updateExternalAddressCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateExternalAddressRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.UpdateExternalAddressRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateExternalAddressOperationCallable()
    
    
    public final OperationCallable<UpdateExternalAddressRequest,ExternalAddress,OperationMetadata> updateExternalAddressOperationCallable()

Updates the parameters of a single external IP address. Only fields specified in `update_mask` are applied.

During operation processing, the resource is temporarily in the `ACTIVE` state before the operation fully completes. For that period of time, you can't update the resource. Use the operation status to determine when the processing fully completes.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       UpdateExternalAddressRequest request =
           UpdateExternalAddressRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setExternalAddress(ExternalAddress.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<ExternalAddress, OperationMetadata> future =
           vmwareEngineClient.updateExternalAddressOperationCallable().futureCall(request);
       // Do something.
       ExternalAddress response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdateExternalAddressRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.UpdateExternalAddressRequest),[ExternalAddress](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.ExternalAddress),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.OperationMetadata)>` |   
  
### updateLoggingServerAsync(LoggingServer loggingServer, FieldMask updateMask)
    
    
    public final OperationFuture<LoggingServer,OperationMetadata> updateLoggingServerAsync(LoggingServer loggingServer, FieldMask updateMask)

Updates the parameters of a single logging server. Only fields specified in `update_mask` are applied.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       LoggingServer loggingServer = LoggingServer.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       LoggingServer response =
           vmwareEngineClient.updateLoggingServerAsync(loggingServer, updateMask).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`loggingServer` | `[LoggingServer](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.LoggingServer)`  
Required. Logging server description.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Required. Field mask is used to specify the fields to be overwritten in the `LoggingServer` resource by the update. The fields specified in the `update_mask` are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields will be overwritten.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[LoggingServer](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.LoggingServer),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.OperationMetadata)>` |   
  
### updateLoggingServerAsync(UpdateLoggingServerRequest request)
    
    
    public final OperationFuture<LoggingServer,OperationMetadata> updateLoggingServerAsync(UpdateLoggingServerRequest request)

Updates the parameters of a single logging server. Only fields specified in `update_mask` are applied.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       UpdateLoggingServerRequest request =
           UpdateLoggingServerRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setLoggingServer(LoggingServer.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       LoggingServer response = vmwareEngineClient.updateLoggingServerAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateLoggingServerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.UpdateLoggingServerRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[LoggingServer](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.LoggingServer),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.OperationMetadata)>` |   
  
### updateLoggingServerCallable()
    
    
    public final UnaryCallable<UpdateLoggingServerRequest,Operation> updateLoggingServerCallable()

Updates the parameters of a single logging server. Only fields specified in `update_mask` are applied.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       UpdateLoggingServerRequest request =
           UpdateLoggingServerRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setLoggingServer(LoggingServer.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           vmwareEngineClient.updateLoggingServerCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateLoggingServerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.UpdateLoggingServerRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateLoggingServerOperationCallable()
    
    
    public final OperationCallable<UpdateLoggingServerRequest,LoggingServer,OperationMetadata> updateLoggingServerOperationCallable()

Updates the parameters of a single logging server. Only fields specified in `update_mask` are applied.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       UpdateLoggingServerRequest request =
           UpdateLoggingServerRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setLoggingServer(LoggingServer.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<LoggingServer, OperationMetadata> future =
           vmwareEngineClient.updateLoggingServerOperationCallable().futureCall(request);
       // Do something.
       LoggingServer response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdateLoggingServerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.UpdateLoggingServerRequest),[LoggingServer](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.LoggingServer),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.OperationMetadata)>` |   
  
### updateManagementDnsZoneBindingAsync(ManagementDnsZoneBinding managementDnsZoneBinding, FieldMask updateMask)
    
    
    public final OperationFuture<ManagementDnsZoneBinding,OperationMetadata> updateManagementDnsZoneBindingAsync(ManagementDnsZoneBinding managementDnsZoneBinding, FieldMask updateMask)

Updates a `ManagementDnsZoneBinding` resource. Only fields specified in `update_mask` are applied.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       ManagementDnsZoneBinding managementDnsZoneBinding =
           ManagementDnsZoneBinding.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       ManagementDnsZoneBinding response =
           vmwareEngineClient
               .updateManagementDnsZoneBindingAsync(managementDnsZoneBinding, updateMask)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`managementDnsZoneBinding` | `[ManagementDnsZoneBinding](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.ManagementDnsZoneBinding)`  
Required. New values to update the management DNS zone binding with.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Required. Field mask is used to specify the fields to be overwritten in the `ManagementDnsZoneBinding` resource by the update. The fields specified in the `update_mask` are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields will be overwritten.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[ManagementDnsZoneBinding](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.ManagementDnsZoneBinding),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.OperationMetadata)>` |   
  
### updateManagementDnsZoneBindingAsync(UpdateManagementDnsZoneBindingRequest request)
    
    
    public final OperationFuture<ManagementDnsZoneBinding,OperationMetadata> updateManagementDnsZoneBindingAsync(UpdateManagementDnsZoneBindingRequest request)

Updates a `ManagementDnsZoneBinding` resource. Only fields specified in `update_mask` are applied.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       UpdateManagementDnsZoneBindingRequest request =
           UpdateManagementDnsZoneBindingRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setManagementDnsZoneBinding(ManagementDnsZoneBinding.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       ManagementDnsZoneBinding response =
           vmwareEngineClient.updateManagementDnsZoneBindingAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateManagementDnsZoneBindingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.UpdateManagementDnsZoneBindingRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[ManagementDnsZoneBinding](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.ManagementDnsZoneBinding),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.OperationMetadata)>` |   
  
### updateManagementDnsZoneBindingCallable()
    
    
    public final UnaryCallable<UpdateManagementDnsZoneBindingRequest,Operation> updateManagementDnsZoneBindingCallable()

Updates a `ManagementDnsZoneBinding` resource. Only fields specified in `update_mask` are applied.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       UpdateManagementDnsZoneBindingRequest request =
           UpdateManagementDnsZoneBindingRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setManagementDnsZoneBinding(ManagementDnsZoneBinding.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           vmwareEngineClient.updateManagementDnsZoneBindingCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateManagementDnsZoneBindingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.UpdateManagementDnsZoneBindingRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateManagementDnsZoneBindingOperationCallable()
    
    
    public final OperationCallable<UpdateManagementDnsZoneBindingRequest,ManagementDnsZoneBinding,OperationMetadata> updateManagementDnsZoneBindingOperationCallable()

Updates a `ManagementDnsZoneBinding` resource. Only fields specified in `update_mask` are applied.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       UpdateManagementDnsZoneBindingRequest request =
           UpdateManagementDnsZoneBindingRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setManagementDnsZoneBinding(ManagementDnsZoneBinding.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<ManagementDnsZoneBinding, OperationMetadata> future =
           vmwareEngineClient.updateManagementDnsZoneBindingOperationCallable().futureCall(request);
       // Do something.
       ManagementDnsZoneBinding response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdateManagementDnsZoneBindingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.UpdateManagementDnsZoneBindingRequest),[ManagementDnsZoneBinding](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.ManagementDnsZoneBinding),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.OperationMetadata)>` |   
  
### updateNetworkPeeringAsync(NetworkPeering networkPeering, FieldMask updateMask)
    
    
    public final OperationFuture<NetworkPeering,OperationMetadata> updateNetworkPeeringAsync(NetworkPeering networkPeering, FieldMask updateMask)

Modifies a `NetworkPeering` resource. Only the `description` field can be updated. Only fields specified in `updateMask` are applied. NetworkPeering is a global resource and location can only be global.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       NetworkPeering networkPeering = NetworkPeering.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       NetworkPeering response =
           vmwareEngineClient.updateNetworkPeeringAsync(networkPeering, updateMask).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`networkPeering` | `[NetworkPeering](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.NetworkPeering)`  
Required. Network peering description.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Required. Field mask is used to specify the fields to be overwritten in the `NetworkPeering` resource by the update. The fields specified in the `update_mask` are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields will be overwritten.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[NetworkPeering](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.NetworkPeering),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.OperationMetadata)>` |   
  
### updateNetworkPeeringAsync(UpdateNetworkPeeringRequest request)
    
    
    public final OperationFuture<NetworkPeering,OperationMetadata> updateNetworkPeeringAsync(UpdateNetworkPeeringRequest request)

Modifies a `NetworkPeering` resource. Only the `description` field can be updated. Only fields specified in `updateMask` are applied. NetworkPeering is a global resource and location can only be global.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       UpdateNetworkPeeringRequest request =
           UpdateNetworkPeeringRequest.newBuilder()
               .setNetworkPeering(NetworkPeering.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       NetworkPeering response = vmwareEngineClient.updateNetworkPeeringAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateNetworkPeeringRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.UpdateNetworkPeeringRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[NetworkPeering](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.NetworkPeering),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.OperationMetadata)>` |   
  
### updateNetworkPeeringCallable()
    
    
    public final UnaryCallable<UpdateNetworkPeeringRequest,Operation> updateNetworkPeeringCallable()

Modifies a `NetworkPeering` resource. Only the `description` field can be updated. Only fields specified in `updateMask` are applied. NetworkPeering is a global resource and location can only be global.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       UpdateNetworkPeeringRequest request =
           UpdateNetworkPeeringRequest.newBuilder()
               .setNetworkPeering(NetworkPeering.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           vmwareEngineClient.updateNetworkPeeringCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateNetworkPeeringRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.UpdateNetworkPeeringRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateNetworkPeeringOperationCallable()
    
    
    public final OperationCallable<UpdateNetworkPeeringRequest,NetworkPeering,OperationMetadata> updateNetworkPeeringOperationCallable()

Modifies a `NetworkPeering` resource. Only the `description` field can be updated. Only fields specified in `updateMask` are applied. NetworkPeering is a global resource and location can only be global.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       UpdateNetworkPeeringRequest request =
           UpdateNetworkPeeringRequest.newBuilder()
               .setNetworkPeering(NetworkPeering.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<NetworkPeering, OperationMetadata> future =
           vmwareEngineClient.updateNetworkPeeringOperationCallable().futureCall(request);
       // Do something.
       NetworkPeering response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdateNetworkPeeringRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.UpdateNetworkPeeringRequest),[NetworkPeering](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.NetworkPeering),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.OperationMetadata)>` |   
  
### updateNetworkPolicyAsync(NetworkPolicy networkPolicy, FieldMask updateMask)
    
    
    public final OperationFuture<NetworkPolicy,OperationMetadata> updateNetworkPolicyAsync(NetworkPolicy networkPolicy, FieldMask updateMask)

Modifies a `NetworkPolicy` resource. Only the following fields can be updated: `internet_access`, `external_ip`, `edge_services_cidr`. Only fields specified in `updateMask` are applied. When updating a network policy, the external IP network service can only be disabled if there are no external IP addresses present in the scope of the policy. Also, a `NetworkService` cannot be updated when `NetworkService.state` is set to `RECONCILING`.

During operation processing, the resource is temporarily in the `ACTIVE` state before the operation fully completes. For that period of time, you can't update the resource. Use the operation status to determine when the processing fully completes.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       NetworkPolicy networkPolicy = NetworkPolicy.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       NetworkPolicy response =
           vmwareEngineClient.updateNetworkPolicyAsync(networkPolicy, updateMask).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`networkPolicy` | `[NetworkPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.NetworkPolicy)`  
Required. Network policy description.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Required. Field mask is used to specify the fields to be overwritten in the `NetworkPolicy` resource by the update. The fields specified in the `update_mask` are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields will be overwritten.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[NetworkPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.NetworkPolicy),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.OperationMetadata)>` |   
  
### updateNetworkPolicyAsync(UpdateNetworkPolicyRequest request)
    
    
    public final OperationFuture<NetworkPolicy,OperationMetadata> updateNetworkPolicyAsync(UpdateNetworkPolicyRequest request)

Modifies a `NetworkPolicy` resource. Only the following fields can be updated: `internet_access`, `external_ip`, `edge_services_cidr`. Only fields specified in `updateMask` are applied. When updating a network policy, the external IP network service can only be disabled if there are no external IP addresses present in the scope of the policy. Also, a `NetworkService` cannot be updated when `NetworkService.state` is set to `RECONCILING`.

During operation processing, the resource is temporarily in the `ACTIVE` state before the operation fully completes. For that period of time, you can't update the resource. Use the operation status to determine when the processing fully completes.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       UpdateNetworkPolicyRequest request =
           UpdateNetworkPolicyRequest.newBuilder()
               .setNetworkPolicy(NetworkPolicy.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       NetworkPolicy response = vmwareEngineClient.updateNetworkPolicyAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateNetworkPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.UpdateNetworkPolicyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[NetworkPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.NetworkPolicy),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.OperationMetadata)>` |   
  
### updateNetworkPolicyCallable()
    
    
    public final UnaryCallable<UpdateNetworkPolicyRequest,Operation> updateNetworkPolicyCallable()

Modifies a `NetworkPolicy` resource. Only the following fields can be updated: `internet_access`, `external_ip`, `edge_services_cidr`. Only fields specified in `updateMask` are applied. When updating a network policy, the external IP network service can only be disabled if there are no external IP addresses present in the scope of the policy. Also, a `NetworkService` cannot be updated when `NetworkService.state` is set to `RECONCILING`.

During operation processing, the resource is temporarily in the `ACTIVE` state before the operation fully completes. For that period of time, you can't update the resource. Use the operation status to determine when the processing fully completes.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       UpdateNetworkPolicyRequest request =
           UpdateNetworkPolicyRequest.newBuilder()
               .setNetworkPolicy(NetworkPolicy.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           vmwareEngineClient.updateNetworkPolicyCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateNetworkPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.UpdateNetworkPolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateNetworkPolicyOperationCallable()
    
    
    public final OperationCallable<UpdateNetworkPolicyRequest,NetworkPolicy,OperationMetadata> updateNetworkPolicyOperationCallable()

Modifies a `NetworkPolicy` resource. Only the following fields can be updated: `internet_access`, `external_ip`, `edge_services_cidr`. Only fields specified in `updateMask` are applied. When updating a network policy, the external IP network service can only be disabled if there are no external IP addresses present in the scope of the policy. Also, a `NetworkService` cannot be updated when `NetworkService.state` is set to `RECONCILING`.

During operation processing, the resource is temporarily in the `ACTIVE` state before the operation fully completes. For that period of time, you can't update the resource. Use the operation status to determine when the processing fully completes.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       UpdateNetworkPolicyRequest request =
           UpdateNetworkPolicyRequest.newBuilder()
               .setNetworkPolicy(NetworkPolicy.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<NetworkPolicy, OperationMetadata> future =
           vmwareEngineClient.updateNetworkPolicyOperationCallable().futureCall(request);
       // Do something.
       NetworkPolicy response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdateNetworkPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.UpdateNetworkPolicyRequest),[NetworkPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.NetworkPolicy),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.OperationMetadata)>` |   
  
### updatePrivateCloudAsync(PrivateCloud privateCloud, FieldMask updateMask)
    
    
    public final OperationFuture<PrivateCloud,OperationMetadata> updatePrivateCloudAsync(PrivateCloud privateCloud, FieldMask updateMask)

Modifies a `PrivateCloud` resource. Only the following fields can be updated: `description`. Only fields specified in `updateMask` are applied.

During operation processing, the resource is temporarily in the `ACTIVE` state before the operation fully completes. For that period of time, you can't update the resource. Use the operation status to determine when the processing fully completes.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       PrivateCloud privateCloud = PrivateCloud.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       PrivateCloud response =
           vmwareEngineClient.updatePrivateCloudAsync(privateCloud, updateMask).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`privateCloud` | `[PrivateCloud](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.PrivateCloud)`  
Required. Private cloud description.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Required. Field mask is used to specify the fields to be overwritten in the `PrivateCloud` resource by the update. The fields specified in `updateMask` are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields will be overwritten.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[PrivateCloud](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.PrivateCloud),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.OperationMetadata)>` |   
  
### updatePrivateCloudAsync(UpdatePrivateCloudRequest request)
    
    
    public final OperationFuture<PrivateCloud,OperationMetadata> updatePrivateCloudAsync(UpdatePrivateCloudRequest request)

Modifies a `PrivateCloud` resource. Only the following fields can be updated: `description`. Only fields specified in `updateMask` are applied.

During operation processing, the resource is temporarily in the `ACTIVE` state before the operation fully completes. For that period of time, you can't update the resource. Use the operation status to determine when the processing fully completes.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       UpdatePrivateCloudRequest request =
           UpdatePrivateCloudRequest.newBuilder()
               .setPrivateCloud(PrivateCloud.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       PrivateCloud response = vmwareEngineClient.updatePrivateCloudAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdatePrivateCloudRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.UpdatePrivateCloudRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[PrivateCloud](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.PrivateCloud),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.OperationMetadata)>` |   
  
### updatePrivateCloudCallable()
    
    
    public final UnaryCallable<UpdatePrivateCloudRequest,Operation> updatePrivateCloudCallable()

Modifies a `PrivateCloud` resource. Only the following fields can be updated: `description`. Only fields specified in `updateMask` are applied.

During operation processing, the resource is temporarily in the `ACTIVE` state before the operation fully completes. For that period of time, you can't update the resource. Use the operation status to determine when the processing fully completes.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       UpdatePrivateCloudRequest request =
           UpdatePrivateCloudRequest.newBuilder()
               .setPrivateCloud(PrivateCloud.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           vmwareEngineClient.updatePrivateCloudCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdatePrivateCloudRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.UpdatePrivateCloudRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updatePrivateCloudOperationCallable()
    
    
    public final OperationCallable<UpdatePrivateCloudRequest,PrivateCloud,OperationMetadata> updatePrivateCloudOperationCallable()

Modifies a `PrivateCloud` resource. Only the following fields can be updated: `description`. Only fields specified in `updateMask` are applied.

During operation processing, the resource is temporarily in the `ACTIVE` state before the operation fully completes. For that period of time, you can't update the resource. Use the operation status to determine when the processing fully completes.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       UpdatePrivateCloudRequest request =
           UpdatePrivateCloudRequest.newBuilder()
               .setPrivateCloud(PrivateCloud.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<PrivateCloud, OperationMetadata> future =
           vmwareEngineClient.updatePrivateCloudOperationCallable().futureCall(request);
       // Do something.
       PrivateCloud response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdatePrivateCloudRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.UpdatePrivateCloudRequest),[PrivateCloud](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.PrivateCloud),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.OperationMetadata)>` |   
  
### updatePrivateConnectionAsync(PrivateConnection privateConnection, FieldMask updateMask)
    
    
    public final OperationFuture<PrivateConnection,OperationMetadata> updatePrivateConnectionAsync(PrivateConnection privateConnection, FieldMask updateMask)

Modifies a `PrivateConnection` resource. Only `description` and `routing_mode` fields can be updated. Only fields specified in `updateMask` are applied.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       PrivateConnection privateConnection = PrivateConnection.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       PrivateConnection response =
           vmwareEngineClient.updatePrivateConnectionAsync(privateConnection, updateMask).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`privateConnection` | `[PrivateConnection](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.PrivateConnection)`  
Required. Private connection description.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Required. Field mask is used to specify the fields to be overwritten in the `PrivateConnection` resource by the update. The fields specified in the `update_mask` are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields will be overwritten.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[PrivateConnection](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.PrivateConnection),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.OperationMetadata)>` |   
  
### updatePrivateConnectionAsync(UpdatePrivateConnectionRequest request)
    
    
    public final OperationFuture<PrivateConnection,OperationMetadata> updatePrivateConnectionAsync(UpdatePrivateConnectionRequest request)

Modifies a `PrivateConnection` resource. Only `description` and `routing_mode` fields can be updated. Only fields specified in `updateMask` are applied.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       UpdatePrivateConnectionRequest request =
           UpdatePrivateConnectionRequest.newBuilder()
               .setPrivateConnection(PrivateConnection.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       PrivateConnection response = vmwareEngineClient.updatePrivateConnectionAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdatePrivateConnectionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.UpdatePrivateConnectionRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[PrivateConnection](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.PrivateConnection),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.OperationMetadata)>` |   
  
### updatePrivateConnectionCallable()
    
    
    public final UnaryCallable<UpdatePrivateConnectionRequest,Operation> updatePrivateConnectionCallable()

Modifies a `PrivateConnection` resource. Only `description` and `routing_mode` fields can be updated. Only fields specified in `updateMask` are applied.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       UpdatePrivateConnectionRequest request =
           UpdatePrivateConnectionRequest.newBuilder()
               .setPrivateConnection(PrivateConnection.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           vmwareEngineClient.updatePrivateConnectionCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdatePrivateConnectionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.UpdatePrivateConnectionRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updatePrivateConnectionOperationCallable()
    
    
    public final OperationCallable<UpdatePrivateConnectionRequest,PrivateConnection,OperationMetadata> updatePrivateConnectionOperationCallable()

Modifies a `PrivateConnection` resource. Only `description` and `routing_mode` fields can be updated. Only fields specified in `updateMask` are applied.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       UpdatePrivateConnectionRequest request =
           UpdatePrivateConnectionRequest.newBuilder()
               .setPrivateConnection(PrivateConnection.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<PrivateConnection, OperationMetadata> future =
           vmwareEngineClient.updatePrivateConnectionOperationCallable().futureCall(request);
       // Do something.
       PrivateConnection response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdatePrivateConnectionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.UpdatePrivateConnectionRequest),[PrivateConnection](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.PrivateConnection),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.OperationMetadata)>` |   
  
### updateSubnetAsync(Subnet subnet, FieldMask updateMask)
    
    
    public final OperationFuture<Subnet,OperationMetadata> updateSubnetAsync(Subnet subnet, FieldMask updateMask)

Updates the parameters of a single subnet. Only fields specified in `update_mask` are applied.

*Note*: This API is synchronous and always returns a successful `google.longrunning.Operation` (LRO). The returned LRO will only have `done` and `response` fields.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       Subnet subnet = Subnet.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       Subnet response = vmwareEngineClient.updateSubnetAsync(subnet, updateMask).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`subnet` | `[Subnet](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.Subnet)`  
Required. Subnet description.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Required. Field mask is used to specify the fields to be overwritten in the `Subnet` resource by the update. The fields specified in the `update_mask` are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields will be overwritten.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Subnet](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.Subnet),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.OperationMetadata)>` |   
  
### updateSubnetAsync(UpdateSubnetRequest request)
    
    
    public final OperationFuture<Subnet,OperationMetadata> updateSubnetAsync(UpdateSubnetRequest request)

Updates the parameters of a single subnet. Only fields specified in `update_mask` are applied.

*Note*: This API is synchronous and always returns a successful `google.longrunning.Operation` (LRO). The returned LRO will only have `done` and `response` fields.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       UpdateSubnetRequest request =
           UpdateSubnetRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setSubnet(Subnet.newBuilder().build())
               .build();
       Subnet response = vmwareEngineClient.updateSubnetAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateSubnetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.UpdateSubnetRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Subnet](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.Subnet),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.OperationMetadata)>` |   
  
### updateSubnetCallable()
    
    
    public final UnaryCallable<UpdateSubnetRequest,Operation> updateSubnetCallable()

Updates the parameters of a single subnet. Only fields specified in `update_mask` are applied.

*Note*: This API is synchronous and always returns a successful `google.longrunning.Operation` (LRO). The returned LRO will only have `done` and `response` fields.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       UpdateSubnetRequest request =
           UpdateSubnetRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setSubnet(Subnet.newBuilder().build())
               .build();
       ApiFuture<Operation> future = vmwareEngineClient.updateSubnetCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateSubnetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.UpdateSubnetRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateSubnetOperationCallable()
    
    
    public final OperationCallable<UpdateSubnetRequest,Subnet,OperationMetadata> updateSubnetOperationCallable()

Updates the parameters of a single subnet. Only fields specified in `update_mask` are applied.

*Note*: This API is synchronous and always returns a successful `google.longrunning.Operation` (LRO). The returned LRO will only have `done` and `response` fields.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       UpdateSubnetRequest request =
           UpdateSubnetRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setSubnet(Subnet.newBuilder().build())
               .build();
       OperationFuture<Subnet, OperationMetadata> future =
           vmwareEngineClient.updateSubnetOperationCallable().futureCall(request);
       // Do something.
       Subnet response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdateSubnetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.UpdateSubnetRequest),[Subnet](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.Subnet),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.OperationMetadata)>` |   
  
### updateVmwareEngineNetworkAsync(UpdateVmwareEngineNetworkRequest request)
    
    
    public final OperationFuture<VmwareEngineNetwork,OperationMetadata> updateVmwareEngineNetworkAsync(UpdateVmwareEngineNetworkRequest request)

Modifies a VMware Engine network resource. Only the following fields can be updated: `description`. Only fields specified in `updateMask` are applied.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       UpdateVmwareEngineNetworkRequest request =
           UpdateVmwareEngineNetworkRequest.newBuilder()
               .setVmwareEngineNetwork(VmwareEngineNetwork.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       VmwareEngineNetwork response =
           vmwareEngineClient.updateVmwareEngineNetworkAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateVmwareEngineNetworkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.UpdateVmwareEngineNetworkRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[VmwareEngineNetwork](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.VmwareEngineNetwork),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.OperationMetadata)>` |   
  
### updateVmwareEngineNetworkAsync(VmwareEngineNetwork vmwareEngineNetwork, FieldMask updateMask)
    
    
    public final OperationFuture<VmwareEngineNetwork,OperationMetadata> updateVmwareEngineNetworkAsync(VmwareEngineNetwork vmwareEngineNetwork, FieldMask updateMask)

Modifies a VMware Engine network resource. Only the following fields can be updated: `description`. Only fields specified in `updateMask` are applied.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       VmwareEngineNetwork vmwareEngineNetwork = VmwareEngineNetwork.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       VmwareEngineNetwork response =
           vmwareEngineClient.updateVmwareEngineNetworkAsync(vmwareEngineNetwork, updateMask).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`vmwareEngineNetwork` | `[VmwareEngineNetwork](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.VmwareEngineNetwork)`  
Required. VMware Engine network description.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Required. Field mask is used to specify the fields to be overwritten in the VMware Engine network resource by the update. The fields specified in the `update_mask` are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields will be overwritten. Only the following fields can be updated: `description`.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[VmwareEngineNetwork](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.VmwareEngineNetwork),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.OperationMetadata)>` |   
  
### updateVmwareEngineNetworkCallable()
    
    
    public final UnaryCallable<UpdateVmwareEngineNetworkRequest,Operation> updateVmwareEngineNetworkCallable()

Modifies a VMware Engine network resource. Only the following fields can be updated: `description`. Only fields specified in `updateMask` are applied.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       UpdateVmwareEngineNetworkRequest request =
           UpdateVmwareEngineNetworkRequest.newBuilder()
               .setVmwareEngineNetwork(VmwareEngineNetwork.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           vmwareEngineClient.updateVmwareEngineNetworkCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateVmwareEngineNetworkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.UpdateVmwareEngineNetworkRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateVmwareEngineNetworkOperationCallable()
    
    
    public final OperationCallable<UpdateVmwareEngineNetworkRequest,VmwareEngineNetwork,OperationMetadata> updateVmwareEngineNetworkOperationCallable()

Modifies a VMware Engine network resource. Only the following fields can be updated: `description`. Only fields specified in `updateMask` are applied.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VmwareEngineClient vmwareEngineClient = VmwareEngineClient.create()) {
       UpdateVmwareEngineNetworkRequest request =
           UpdateVmwareEngineNetworkRequest.newBuilder()
               .setVmwareEngineNetwork(VmwareEngineNetwork.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<VmwareEngineNetwork, OperationMetadata> future =
           vmwareEngineClient.updateVmwareEngineNetworkOperationCallable().futureCall(request);
       // Do something.
       VmwareEngineNetwork response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdateVmwareEngineNetworkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.UpdateVmwareEngineNetworkRequest),[VmwareEngineNetwork](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.VmwareEngineNetwork),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.OperationMetadata)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
